import math
from typing import Final, Optional, Tuple

import sc2reader.objects
import sc2reader.resources
from sc2reader.data import Unit

from cerebrate.core import Replay


class ReplayDataExtractor:
    DEFAULT_FPS: Final = 16
    EARLY_RUSH_END: Final = 60 * 3 * DEFAULT_FPS
    EARLY_GAME_END: Final = 60 * 5 * DEFAULT_FPS
    LATE_GAME_START: Final = 60 * 12 * DEFAULT_FPS

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
        pass

    @staticmethod
    def get_original_unit_name(unit: Optional[Unit]) -> Optional[str]:
        if not unit.type_history:
            return None
        return next(iter(unit.type_history.values())).name

    @staticmethod
    def is_base_structure(unit: Unit) -> bool:
        original_unit_name = ReplayDataExtractor.get_original_unit_name(unit)
        return original_unit_name and original_unit_name in [
            "Hatchery",
            "Nexus",
            "CommandCenter",
        ]

    @staticmethod
    def get_main_base_location(
        participant: Optional[sc2reader.objects.Participant],
    ) -> Optional[Tuple[int, int]]:
        if not participant:
            return None

        starting_units = [unit for unit in participant.units if unit.started_at <= 0]
        if not starting_units:
            return None

        base_structures = [
            unit
            for unit in starting_units
            if ReplayDataExtractor.is_base_structure(unit)
        ]
        if not base_structures or len(base_structures) != 1:
            return None

        main_base_structure = base_structures[0]

        return main_base_structure.location

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

    # noinspection PyUnresolvedReferences
    def is_proxy(self, unit: Optional[Unit]) -> bool:
        if not self.player or not self.opponent:
            return False

        if not unit or not unit.is_building or not unit.location:
            return False

        def is_proxy_inner(
            unit_location: Tuple[int, int],
            main_base_location: Tuple[int, int],
            enemy_base_location: Tuple[int, int],
        ) -> bool:
            """returns True if unit is located more than 40% of the distance towards the enemy base"""

            dist_from_main_base = math.sqrt(
                math.pow(main_base_location[0] - unit_location[0], 2)
                + math.pow(main_base_location[1] - unit_location[1], 2)
            )
            dist_from_enemy_base = math.sqrt(
                math.pow(enemy_base_location[0] - unit_location[0], 2)
                + math.pow(enemy_base_location[1] - unit_location[1], 2)
            )
            return dist_from_main_base > 0.4 * (
                dist_from_main_base + dist_from_enemy_base
            )

        if unit.owner == self.player:
            return is_proxy_inner(
                unit.location,
                ReplayDataExtractor.get_main_base_location(self.player),
                ReplayDataExtractor.get_main_base_location(self.opponent),
            )
        elif unit.owner == self.opponent:
            return is_proxy_inner(
                unit.location,
                ReplayDataExtractor.get_main_base_location(self.opponent),
                ReplayDataExtractor.get_main_base_location(self.player),
            )
        else:
            return False
