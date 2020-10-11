from typing import Callable, Iterable, List

import sc2reader.objects
import sc2reader.resources

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor

from .tag_generator import TagGenerator

DEFAULT_RACE_NAMES = [
    "protoss",
    "terran",
    "zerg",
]


def _flatten(iterable_to_flatten: Iterable[Iterable]):
    return [item for sublist in iterable_to_flatten for item in sublist]


def _remove_race_tags(tag_factory: Callable[[str], str], replay: Replay) -> Replay:
    for race_tag in [tag_factory(race_name) for race_name in DEFAULT_RACE_NAMES]:
        replay.remove_tag(race_tag)
    return replay


class RaceTagGenerator(TagGenerator):
    def tags_to_remove(self) -> List[str]:
        race_tag_factories: List[Callable[[str], str]] = [
            Replay.create_player_tag,
            Replay.create_opponent_tag,
        ]
        return _flatten(
            [
                [race_tag_factory(race_name) for race_name in DEFAULT_RACE_NAMES]
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
