from typing import final

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor

from .replay_preprocessor import ReplayPreprocessor


class SetReplayTimestamp(ReplayPreprocessor):
    @final
    def preprocess_replay(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> Replay:
        replay.timestamp = replay_data_extractor.source_replay_data.unix_timestamp
        return replay
