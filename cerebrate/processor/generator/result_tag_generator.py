from typing import Callable, List

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor
from cerebrate.util import flatten

from .tag_generator import TagGenerator

OUTCOMES = [
    "win",
    "loss",
    "tie",
]


class ResultTagGenerator(TagGenerator):
    def tags_to_remove(self) -> List[str]:
        tag_factories: List[Callable[[str], str]] = [
            Replay.create_player_tag,
            Replay.create_opponent_tag,
        ]
        return flatten(
            [
                [tag_factory(outcome) for outcome in OUTCOMES]
                for tag_factory in tag_factories
            ]
        )

    def generate_tags(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> List[str]:
        if (
            not replay_data_extractor.player
            or not replay_data_extractor.player.result
            or not replay_data_extractor.opponent
            or not replay_data_extractor.opponent.result
        ):
            return []

        return [
            Replay.create_player_tag(replay_data_extractor.player.result.lower()),
            Replay.create_opponent_tag(replay_data_extractor.opponent.result.lower()),
        ]
