import os
import shutil
from typing import List, Final, BinaryIO, Optional

import tinydb

from cerebrate.core.replay import Replay
from cerebrate.db.replay_query import ReplayQuery


class ReplayStore:
    __REPLAY_ARCHIVE_SUBDIRECTORY_NAME: Final = "replay_archive"
    __DB_FILE_NAME: Final = "replays.json"

    __db: Final[tinydb.TinyDB]

    def __init__(self, db_data_path: str):
        if not os.path.exists(db_data_path):
            os.makedirs(db_data_path)

        replay_archive_path = os.path.join(
            db_data_path, ReplayStore.__REPLAY_ARCHIVE_SUBDIRECTORY_NAME
        )
        if not os.path.exists(replay_archive_path):
            os.makedirs(replay_archive_path)

        db_path = os.path.join(db_data_path, ReplayStore.__DB_FILE_NAME)
        if not os.path.exists(db_path):
            open(db_path, "a").close()

        self.__db = tinydb.TinyDB(db_path)
        self.__replay_archive_path = replay_archive_path

    def insert_replay_data(
        self, replay_data: BinaryIO, replay_hash: Optional[str] = None
    ) -> Optional[Replay]:
        calculated_hash = Replay.hash_replay_data(replay_data)
        if replay_hash and calculated_hash != replay_hash:
            return None

        canonical_path = os.path.join(
            self.__replay_archive_path, calculated_hash + ".SC2Replay"
        )
        with open(canonical_path, "wb") as replay_file:
            shutil.copyfileobj(replay_data, replay_file)

        return Replay(canonical_path, calculated_hash)

    def update_or_insert_replay(self, replay: Replay):
        def update_tags(element):
            element["tags"] = replay.tags

        replay_updated = self.__db.update(
            update_tags, tinydb.Query()["hash"] == replay.replay_hash
        )
        if not replay_updated:
            canonical_path = os.path.join(
                self.__replay_archive_path, replay.replay_hash + ".SC2Replay"
            )
            if canonical_path != replay.path:
                shutil.copyfile(replay.path, canonical_path)
            self.__db.insert(
                {
                    "hash": replay.replay_hash,
                    "canonical_path": canonical_path,
                    "tags": replay.tags,
                }
            )

    def query_replays(self, query: ReplayQuery) -> List[Replay]:
        return []
