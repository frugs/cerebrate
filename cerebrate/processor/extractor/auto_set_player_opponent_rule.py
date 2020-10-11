from typing import Final

from cerebrate.core import Replay
from cerebrate.db import ReplayStore

from .rule import Rule


class AutoSetPlayerOpponentRule(Rule):

    replay_store: Final[ReplayStore]

    def __init__(self, replay_store: ReplayStore):
        self.replay_store = replay_store

    def apply_replay_rule(self, replay: Replay) -> Replay:
        if not replay.teams:
            return replay

        if replay.player_team is not None or replay.opponent_team is not None:
            return replay

        potential_player_teams = [
            index
            for index, team in enumerate(replay.teams)
            if team.team_id in self.replay_store.get_replay_player_team_ids()
        ]
        if len(potential_player_teams) != 1:
            return replay

        replay.player_team = potential_player_teams[0]

        potential_opponent_teams = [
            index for index in range(len(replay.teams)) if index != replay.player_team
        ]
        if len(potential_opponent_teams) != 1:
            return replay

        replay.opponent_team = potential_opponent_teams[0]

        return replay
