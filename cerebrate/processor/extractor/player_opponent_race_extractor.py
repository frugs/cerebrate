import sc2reader.objects
import sc2reader.resources

from cerebrate.core import Replay

from .extractor import Extractor


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
        replay.prepend_tag(
            Replay.create_player_tag(player_team_sole_player.pick_race.lower())
        )

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
        replay.prepend_tag(
            Replay.create_opponent_tag(opp_team_sole_player.pick_race.lower())
        )

        return replay
