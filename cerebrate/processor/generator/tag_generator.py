import abc
from typing import List

from cerebrate.core import Replay
from cerebrate.processor.extractor.replay_data_extractor import ReplayDataExtractor


class TagGenerator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def tags_to_remove(self) -> List[str]:
        return []

    @abc.abstractmethod
    def generate_tags(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> List[str]:
        return []
