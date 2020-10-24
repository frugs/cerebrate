from typing import Final, Optional

import sc2reader
import sc2reader.objects
import sc2reader.resources

from cerebrate.core import Replay


class ReplayDataExtractor:
    _player_team: Optional[sc2reader.objects.Team]
    _opponent_team: Optional[sc2reader.objects.Team]
    _player: Optional[sc2reader.objects.Participant]
    _opponent: Optional[sc2reader.objects.Participant]

    def __init__(self, replay: Replay):
        self._player_team = None
        self._opponent_team = None
        self._player = None
        self._opponent = None

        self.replay_info: Final[Replay] = replay
        # noinspection PyUnresolvedReferences
        self.source_replay_data: Final[
            sc2reader.resources.Replay
        ] = sc2reader.load_replay(replay.path, load_level=4)

    @property
    def player_team(self) -> Optional[sc2reader.objects.Team]:
        if self._player_team:
            return self._player_team

        if (
            self.replay_info.player_team is None
            or not len(self.source_replay_data.teams) > self.replay_info.player_team
        ):
            return None

        self._player_team = self.source_replay_data.teams[self.replay_info.player_team]
        return self._player_team

    @property
    def opponent_team(self) -> Optional[sc2reader.objects.Team]:
        if self._opponent_team:
            return self._opponent_team

        if (
            self.replay_info.opponent_team is None
            or not len(self.source_replay_data.teams) > self.replay_info.opponent_team
        ):
            return None

        self._opponent_team = self.source_replay_data.teams[
            self.replay_info.opponent_team
        ]
        return self._opponent_team

    @property
    def player(self) -> Optional[sc2reader.objects.Participant]:
        if self._player:
            return self._player

        if not self.player_team or len(self.player_team.players) != 1:
            return None

        self._player = self.player_team.players[0]
        return self._player

    @property
    def opponent(self) -> Optional[sc2reader.objects.Participant]:
        if self._opponent:
            return self._opponent

        if not self.opponent_team or len(self.opponent_team.players) != 1:
            return None

        self._opponent = self.opponent_team.players[0]
        return self._opponent
