import abc

import sc2reader.resources

from cerebrate.core import Replay


class Extractor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def extract_replay_info(
        self, replay: Replay, sc2reader_replay: sc2reader.resources.Replay
    ) -> Replay:
        return replay
