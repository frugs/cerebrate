from typing import Callable

import sc2reader.objects
import sc2reader.resources

from cerebrate.core import Replay

from .extractor import Extractor

DEFAULT_RACE_NAMES = [
    "protoss",
    "terran",
    "zerg",
]


def _remove_race_tags(tag_factory: Callable[[str], str], replay: Replay) -> Replay:
    for race_tag in [tag_factory(race_name) for race_name in DEFAULT_RACE_NAMES]:
        replay.remove_tag(race_tag)
    return replay


class PlayerOpponentRaceExtractor(Extractor):
    def extract_replay_info(
        self, replay: Replay, sc2reader_replay: sc2reader.resources.Replay
    ) -> Replay:
        if (
            replay.player_team is None
            or not len(sc2reader_replay.teams) > replay.player_team
        ):
            return replay

        sc2reader_player_team: sc2reader.objects.Team = sc2reader_replay.teams[
            replay.player_team
        ]
        if len(sc2reader_player_team.players) != 1:
            return replay

        player_team_sole_player: sc2reader.objects.Player = (
            sc2reader_player_team.players[0]
        )
        player_race_tag = Replay.create_player_tag(
            player_team_sole_player.pick_race.lower()
        )

        replay = _remove_race_tags(Replay.create_player_tag, replay)
        replay.prepend_tag(player_race_tag)

        if (
            replay.opponent_team is None
            or not len(sc2reader_replay.teams) > replay.opponent_team
        ):
            return replay

        sc2reader_opp_team: sc2reader.objects.Team = sc2reader_replay.teams[
            replay.opponent_team
        ]
        if len(sc2reader_opp_team.players) != 1:
            return replay

        opp_team_sole_player: sc2reader.objects.Player = sc2reader_opp_team.players[0]
        opp_race_tag = Replay.create_opponent_tag(
            opp_team_sole_player.pick_race.lower()
        )

        replay = _remove_race_tags(Replay.create_opponent_tag, replay)
        replay.prepend_tag(opp_race_tag)

        return replay
