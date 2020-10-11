from typing import final

from cerebrate.core import Replay
from cerebrate.core.replay import Team
from cerebrate.processor.extractor import ReplayDataExtractor

from . import ReplayPreprocessor


class SetTeams(ReplayPreprocessor):
    @final
    def preprocess_replay(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> Replay:
        replay.teams.clear()
        for team in replay_data_extractor.source_replay_data.teams:
            team_id = ";".join(player.toon_handle for player in team.players)
            team_name = " ".join(player.name for player in team.players)
            replay.teams.append(Team(team_id=team_id, name=team_name))
        return replay
