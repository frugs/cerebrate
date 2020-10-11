from typing import Callable, List, Iterable

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
        if (
            replay.player_team is None
            or not len(replay_data_extractor.source_replay_data.teams) > replay.player_team
        ):
            return tags

        sc2reader_player_team: sc2reader.objects.Team = replay_data_extractor.source_replay_data.teams[
            replay.player_team
        ]
        if len(sc2reader_player_team.players) != 1:
            return tags

        player_team_sole_player: sc2reader.objects.Player = (
            sc2reader_player_team.players[0]
        )
        player_race_tag = Replay.create_player_tag(
            player_team_sole_player.pick_race.lower()
        )
        tags.append(player_race_tag)

        if (
            replay.opponent_team is None
            or not len(replay_data_extractor.source_replay_data.teams) > replay.opponent_team
        ):
            return tags

        sc2reader_opp_team: sc2reader.objects.Team = replay_data_extractor.source_replay_data.teams[
            replay.opponent_team
        ]
        if len(sc2reader_opp_team.players) != 1:
            return tags

        opp_team_sole_player: sc2reader.objects.Player = sc2reader_opp_team.players[0]
        opp_race_tag = Replay.create_opponent_tag(
            opp_team_sole_player.pick_race.lower()
        )
        tags.append(opp_race_tag)

        return tags
