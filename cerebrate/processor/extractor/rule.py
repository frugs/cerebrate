import abc
from typing import final

import sc2reader.resources

from cerebrate.core import Replay

from .extractor import Extractor


class Rule(Extractor):
    @final
    def extract_replay_info(
        self, replay: Replay, _: sc2reader.resources.Replay
    ) -> Replay:
        return self.apply_replay_rule(replay)

    @abc.abstractmethod
    def apply_replay_rule(self, replay: Replay) -> Replay:
        return replay
