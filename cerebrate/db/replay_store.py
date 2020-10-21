import os
import shutil
from typing import BinaryIO, Final, List, Optional

import tinydb
import tinydb.table

from cerebrate.core.replay import Replay, Team
from cerebrate.core.replay_query import ReplayQuery


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


def _make_db_query(query: ReplayQuery) -> tinydb.Query:
    include_tags_set = set(query.include_tags)
    exclude_tags_set = set(query.exclude_tags)

    doc = tinydb.Query()
    db_query = doc["tags"].test(
        lambda replay_tags: replay_tags
        and (not include_tags_set or include_tags_set.issubset(replay_tags))
        and (not exclude_tags_set or not exclude_tags_set.intersection(replay_tags))
    )
    if None not in [query.start_timestamp, query.end_timestamp]:
        db_query = (
            db_query
            & (doc["timestamp"] >= query.start_timestamp)
            & (doc["timestamp"] <= query.end_timestamp)
        )

    return db_query


class ReplayStore:
    _REPLAY_ARCHIVE_SUBDIRECTORY_NAME: Final = "replay_archive"
    _DB_FILE_NAME: Final = "replays.json"

    _db: Final[tinydb.TinyDB]
    _table: Final[tinydb.table.Table]
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
        self._table = self._db.table(tinydb.TinyDB.default_table_name)
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
        fields = {
            "tags": replay.tags,
            "notes": replay.notes,
            **(
                {"player_team": replay.player_team}
                if replay.player_team is not None
                else {}
            ),
            **(
                {"opponent_team": replay.opponent_team}
                if replay.opponent_team is not None
                else {}
            ),
            **(
                {
                    "canonical_path": replay.path,
                    "teams": [team.team_id for team in replay.teams],
                    "team_names": [team.name for team in replay.teams],
                    "timestamp": replay.timestamp,
                }
                if overwrite_all
                else {}
            ),
        }

        replay_updated = self._table.update(
            fields, tinydb.Query()["hash"] == replay.replay_hash
        )
        if not replay_updated:
            canonical_path = os.path.join(
                self._replay_archive_path, replay.replay_hash + ".SC2Replay"
            )
            if canonical_path != replay.path:
                shutil.copyfile(replay.path, canonical_path)
            self._table.insert(
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
        result = self._table.get(tinydb.where("hash") == replay_hash)
        return _replay_from_doc(result) if result else None

    def query_replays(self, query: ReplayQuery) -> List[Replay]:
        docs = self._table.search(_make_db_query(query))
        replays = [_replay_from_doc(doc) for doc in docs]
        replays.sort(key=lambda replay: replay.timestamp, reverse=True)
        return replays

    def all_replays(self) -> List[Replay]:
        replays = [_replay_from_doc(doc) for doc in self._table.all()]
        replays.sort(key=lambda replay: replay.timestamp, reverse=True)
        return replays

    def remove_replay_by_hash(self, replay_hash: str):
        self._table.remove(tinydb.where("hash") == replay_hash)

    def get_replay_player_team_ids(self) -> List[str]:
        result = self._table.search(
            (tinydb.where("player_team") != None) & (tinydb.where("teams") != None)
        )

        is_valid_doc = (
            lambda doc: doc["teams"]
            and len(doc["teams"]) > doc["player_team"]
            and doc["player_team"] is not doc["opponent_team"]
        )
        return list(
            set(
                document["teams"][document["player_team"]]
                for document in result
                if is_valid_doc(document)
            )
        )
