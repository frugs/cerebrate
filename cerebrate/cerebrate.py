import os
from typing import BinaryIO, Final, Optional

from cerebrate.core import Replay
from cerebrate.db import ReplayStore
from cerebrate.processor import ReplayProcessor

APP_DATA_PATH = os.path.normpath(os.path.expanduser("~/.cerebrate"))


class Cerebrate:
    replay_store: Final[ReplayStore]
    replay_processor: Final[ReplayProcessor]

    def __init__(self):
        self.replay_store = ReplayStore(APP_DATA_PATH)
        self.replay_processor = ReplayProcessor(self.replay_store)

    def save_replay_data(
        self, replay_data: BinaryIO, replay_hash: Optional[str] = None
    ) -> Optional[Replay]:
        return self.replay_store.insert_replay_data(replay_data, replay_hash)

    def update_replay_info(self, replay: Replay):
        self.replay_store.update_or_insert_replay(replay)

    def load_replay_info(self, replay: Replay) -> Replay:
        result = self.replay_store.find_replay_by_hash(replay.replay_hash)
        return self.replay_processor.process_replay(result if result else replay)

    def find_replay(self, replay_hash: str) -> Optional[Replay]:
        result = self.replay_store.find_replay_by_hash(replay_hash)
        if not result:
            return None

        return self.replay_processor.process_replay(result)
