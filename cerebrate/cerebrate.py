import os
import shutil
import traceback
from typing import BinaryIO, Final, Optional, List, Dict

import collections
import typing

from cerebrate.core import Replay
from cerebrate.db import ReplayStore
from cerebrate.core.replay_query import ReplayQuery
from cerebrate.processor import ReplayProcessor
from cerebrate.replaysearch import ReplaySearcher
from cerebrate.util import flatten

APP_DATA_PATH = os.path.normpath(os.path.expanduser("~/.cerebrate"))


def _calculate_tag_frequency(tag: str, replays: List[Replay]) -> int:
    return sum([1 if tag in replay.tags else 0 for replay in replays])


class Cerebrate:
    replay_store: Final[ReplayStore]
    replay_processor: Final[ReplayProcessor]

    @staticmethod
    def find_most_recent_replay_path() -> Optional[str]:
        return ReplaySearcher.get_most_recently_played_replay_path()

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

    def find_replays(self, query: ReplayQuery) -> List[Replay]:
        return self.replay_store.query_replays(query)

    def forget_replay(self, replay_hash: str):
        self.replay_store.remove_replay_by_hash(replay_hash)

    @staticmethod
    def export_replays_to_directory(replays: List[Replay], export_path: str):
        canonical_export_path = os.path.realpath(export_path)
        if not os.path.exists(canonical_export_path):
            os.makedirs(canonical_export_path)

        if not os.path.isdir(canonical_export_path):
            raise ValueError("export path must be a directory")

        for replay in replays:
            shutil.copy(replay.path, canonical_export_path)

    @staticmethod
    def calculate_tag_frequency_table(
        replays: List[Replay], ignore_tags: List[str]
    ) -> typing.OrderedDict[str, int]:
        tag_set = set(flatten(replay.tags for replay in replays))
        frequency_table: Dict[str, int] = dict(
            (tag, _calculate_tag_frequency(tag, replays))
            for tag in tag_set.difference(ignore_tags)
        )
        return collections.OrderedDict(
            sorted(
                ((tag, freq) for tag, freq in frequency_table.items()),
                key=lambda x: x[1],
                reverse=True,
            )
        )

    def regenerate_saved_replay_info(self):
        replays = self.replay_store.all_replays()
        for replay in replays:
            replay = self.replay_processor.process_replay(replay)
            self.replay_store.update_or_insert_replay(replay, overwrite_all=True)
