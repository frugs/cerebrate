import os
import shutil
import typing
from collections import OrderedDict
from typing import BinaryIO, Final, List, Optional, Iterable

import tinydb

from cerebrate.core.replay import Replay
from cerebrate.db.replay_query import ReplayQuery


def _replay_from_doc(doc: dict) -> Replay:
    return Replay(
        path=doc["canonical_path"],
        replay_hash=doc["hash"],
        tags=doc.get("tags"),
        notes=doc.get("notes"),
        timestamp=doc.get("timestamp"),
        player_team=doc.get("player_team"),
        opponent_team=doc.get("opponent_team"),
    )


class ReplayStore:
    _REPLAY_ARCHIVE_SUBDIRECTORY_NAME: Final = "replay_archive"
    _DB_FILE_NAME: Final = "replays.json"

    _db: Final[tinydb.TinyDB]
    _replay_archive_path: Final[str]

    def __init__(self, db_data_path: str):
        if not os.path.exists(db_data_path):
            os.makedirs(db_data_path)

        replay_archive_path = os.path.join(
            db_data_path, ReplayStore._REPLAY_ARCHIVE_SUBDIRECTORY_NAME
        )
        if not os.path.exists(replay_archive_path):
            os.makedirs(replay_archive_path)

        db_path = os.path.join(db_data_path, ReplayStore._DB_FILE_NAME)
        if not os.path.exists(db_path):
            open(db_path, "a").close()

        self._db = tinydb.TinyDB(db_path)
        self._replay_archive_path = replay_archive_path

    def insert_replay_data(
        self, replay_data: BinaryIO, replay_hash: Optional[str] = None
    ) -> Optional[Replay]:
        calculated_hash = Replay.hash_replay_data(replay_data)
        if replay_hash and calculated_hash != replay_hash:
            return None
        replay_data.seek(0)

        canonical_path = os.path.join(
            self._replay_archive_path, calculated_hash + ".SC2Replay"
        )
        with open(canonical_path, "wb") as replay_file:
            shutil.copyfileobj(replay_data, replay_file)

        return Replay(canonical_path, calculated_hash)

    def update_or_insert_replay(self, replay: Replay):
        def update_replay(element):
            element["tags"] = replay.tags
            element["notes"] = replay.notes

            if replay.player_team is not None:
                element["player_team"] = replay.player_team

            if replay.opponent_team is not None:
                element["opponent_team"] = replay.opponent_team

        replay_updated = self._db.update(
            update_replay, tinydb.Query()["hash"] == replay.replay_hash
        )
        if not replay_updated:
            canonical_path = os.path.join(
                self._replay_archive_path, replay.replay_hash + ".SC2Replay"
            )
            if canonical_path != replay.path:
                shutil.copyfile(replay.path, canonical_path)
            self._db.insert(
                {
                    "hash": replay.replay_hash,
                    "canonical_path": canonical_path,
                    "tags": replay.tags,
                    "notes": replay.notes,
                    "teams": [team.team_id for team in replay.teams],
                    "timestamp": replay.timestamp,
                    "player_team": replay.player_team,
                    "opponent_team": replay.opponent_team,
                }
            )

    def find_replay_by_hash(self, replay_hash: str) -> Optional[Replay]:
        result = self._db.get(tinydb.where("hash") == replay_hash)
        return _replay_from_doc(result) if result else None

    def all_replays(self) -> Iterable[Replay]:
        return (_replay_from_doc(doc) for doc in self._db.all())

    def query_replays(self, replay_query: ReplayQuery) -> List[Replay]:
        return []

    def get_replay_player_team_ids(self) -> List[str]:
        result = self._db.search(
            (tinydb.where("player_team") != None) & (tinydb.where("teams") != None)
        )

        is_valid_doc = (
            lambda doc: doc["teams"] and len(doc["teams"]) > doc["player_team"]
        )
        return list(
            set(
                document["teams"][document["player_team"]]
                for document in result
                if is_valid_doc(document)
            )
        )

    def get_tag_frequency_table(self, filter_tags: List[str]) -> typing.OrderedDict:
        frequency_table = {}
        filter_tags_set = set(filter_tags)

        tag_query = (
            tinydb.where("tags").test(
                lambda tags: tags and filter_tags_set.issubset(tags)
            )
            if filter_tags
            else (tinydb.where("tags") != None)
        )
        tagged_replays = self._db.search(tag_query)
        for replay in tagged_replays:
            for tag in replay["tags"]:
                if tag not in frequency_table and tag not in filter_tags:
                    frequency_table[tag] = self._db.count(
                        tag_query
                        & (tinydb.where("tags").test(lambda tags: tag in tags))
                    )
        return OrderedDict(
            sorted(
                ((tag, freq) for tag, freq in frequency_table.items()),
                key=lambda x: x[1],
                reverse=True,
            )
        )
