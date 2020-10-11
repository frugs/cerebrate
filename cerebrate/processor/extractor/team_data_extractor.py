import sc2reader.resources

from cerebrate.core import Replay
from cerebrate.core.replay import Team

from .extractor import Extractor


class TeamDataExtractor(Extractor):
    def extract_replay_info(
        self, replay: Replay, sc2reader_replay: sc2reader.resources.Replay
    ) -> Replay:
        replay.teams.clear()
        for team in sc2reader_replay.teams:
            team_id = ";".join(player.toon_handle for player in team.players)
            team_name = " ".join(player.name for player in team.players)
            replay.teams.append(Team(team_id=team_id, name=team_name))
        return replay
