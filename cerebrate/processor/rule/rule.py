import abc

from cerebrate.core import Replay


class Rule(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def apply_replay_rule(self, replay: Replay) -> Replay:
        return replay
