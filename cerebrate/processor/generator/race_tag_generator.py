from typing import Callable, List

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor
from cerebrate.util import flatten

from .tag_generator import TagGenerator

RACE_NAMES = [
    "protoss",
    "terran",
    "zerg",
]


class RaceTagGenerator(TagGenerator):
    def tags_to_remove(self) -> List[str]:
        race_tag_factories: List[Callable[[str], str]] = [
            Replay.create_player_tag,
            Replay.create_opponent_tag,
        ]
        return flatten(
            [
                [race_tag_factory(race_name) for race_name in RACE_NAMES]
                for race_tag_factory in race_tag_factories
            ]
        )

    def generate_tags(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> List[str]:
        tags = []

        if not replay_data_extractor.player:
            return tags

        player_race = replay_data_extractor.player.play_race.lower()
        tags.append(Replay.create_player_tag(player_race))

        if not replay_data_extractor.opponent:
            return tags

        opponent_race = replay_data_extractor.opponent.play_race.lower()
        tags.append(Replay.create_opponent_tag(opponent_race))

        return tags
