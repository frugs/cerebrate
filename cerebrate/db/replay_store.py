import os
import shutil
from typing import List, ClassVar, Final

import tinydb

from cerebrate.core.replay import Replay
from cerebrate.db.replay_query import ReplayQuery


class ReplayStore:
    __REPLAY_ARCHIVE_SUBDIRECTORY_NAME: Final[ClassVar] = "replay_archive"
    __DB_FILE_NAME: Final[ClassVar] = "replays.json"

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
