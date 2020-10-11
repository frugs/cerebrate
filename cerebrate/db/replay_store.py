import os
import shutil
from typing import BinaryIO, Final, List, Optional

import tinydb

from cerebrate.core.replay import Replay
from cerebrate.db.replay_query import ReplayQuery


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
                    "teams": [team.team_id for team in replay.teams],
                    "timestamp": replay.timestamp,
                    "player_team": replay.player_team,
                    "opponent_team": replay.opponent_team,
                }
            )

    def find_replay_by_hash(self, replay_hash: str) -> Optional[Replay]:
        result = self._db.get(tinydb.where("hash") == replay_hash)
        if not result:
            return None

        return Replay(
            path=result["canonical_path"],
            replay_hash=replay_hash,
            tags=result["tags"],
            timestamp=result["timestamp"],
            player_team=result["player_team"],
            opponent_team=result["opponent_team"],
        )

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
