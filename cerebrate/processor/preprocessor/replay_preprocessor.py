import abc

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor


class ReplayPreprocessor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def preprocess_replay(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> Replay:
        return replay
