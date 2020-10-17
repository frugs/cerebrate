import os
import shutil
import typing
from collections import OrderedDict
from typing import BinaryIO, Final, List, Optional, Iterable, Set

import tinydb

from cerebrate.core.replay import Replay, Team


def _replay_from_doc(doc: dict) -> Replay:
    teams = None
    if (
        doc.get("teams")
        and doc.get("team_names")
        and len(doc.get("teams")) == len(doc.get("team_names"))
    ):
        teams = [
            Team(team_id, name)
            for team_id, name in zip(doc.get("teams"), doc.get("team_names"))
        ]

    return Replay(
        path=doc["canonical_path"],
        replay_hash=doc["hash"],
        tags=doc.get("tags"),
        notes=doc.get("notes"),
        teams=teams,
        timestamp=doc.get("timestamp"),
        player_team=doc.get("player_team"),
        opponent_team=doc.get("opponent_team"),
    )


def _query_from_filter_tags(filter_tags_set: Set[str]):
    return (
        tinydb.where("tags").test(lambda tags: tags and filter_tags_set.issubset(tags))
        if filter_tags_set
        else (tinydb.where("tags") != None)
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

    def update_or_insert_replay(self, replay: Replay, overwrite_all: bool = False):
        def update_replay(element):
            element["tags"] = replay.tags
            element["notes"] = replay.notes

            if replay.player_team is not None:
                element["player_team"] = replay.player_team

            if replay.opponent_team is not None:
                element["opponent_team"] = replay.opponent_team

            if overwrite_all:
                element["canonical_path"] = replay.path
                element["teams"] = [team.team_id for team in replay.teams]
                element["team_names"] = [team.name for team in replay.teams]
                element["timestamp"] = replay.timestamp

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
                    "team_names": [team.name for team in replay.teams],
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

    def query_replays(self, filter_tags: List[str]) -> Iterable[Replay]:
        if not filter_tags:
            return self.all_replays()

        docs = self._db.search(_query_from_filter_tags(set(filter_tags)))
        return (_replay_from_doc(doc) for doc in docs)

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
        tag_query = _query_from_filter_tags(set(filter_tags))
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
