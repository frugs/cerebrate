from typing import List, Optional, Set, Callable

import sc2reader.objects

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor
from cerebrate.util import flatten
from .tag_generator import TagGenerator

HIGH_TECH_UNITS = {
    "Battlecruiser": "battlecruiser",
    "Raven": "raven",
    "Banshee": "banshee",
    "Lurker": "lurker",
    "Mutalisk": "muta",
    "SwarmHost": "swarm_host",
    "VoidRay": "void_ray",
    "Carrier": "carrier",
}


def _make_tag(tag_factory: Callable[[str], str], unit_name: str) -> str:
    return tag_factory(HIGH_TECH_UNITS[unit_name])


class HighTechUnitTagGenerator(TagGenerator):
    def tags_to_remove(self) -> List[str]:
        return flatten(
            [
                [tag_factory(unit_name) for unit_name in HIGH_TECH_UNITS]
                for tag_factory in [
                    Replay.create_player_tag,
                    Replay.create_opponent_tag,
                ]
            ]
        )

    def generate_tags(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> List[str]:
        def get_unit_types(
            participant: Optional[sc2reader.objects.Participant],
        ) -> Set[str]:
            if not participant or not participant.units:
                return set()

            return set(
                ReplayDataExtractor.get_original_unit_name(unit)
                for unit in participant.units
                if unit.is_army
                and unit.started_at <= ReplayDataExtractor.LATE_GAME_START
            )

        def generate_tags_inner(
            tag_factory: Callable[[str], str],
            participant: Optional[sc2reader.objects.Participant],
        ) -> List[str]:
            unit_types = get_unit_types(participant)
            return [
                _make_tag(tag_factory, unit_type)
                for unit_type in unit_types
                if unit_type in HIGH_TECH_UNITS
            ]

        return flatten(
            [
                generate_tags_inner(
                    Replay.create_player_tag, replay_data_extractor.player
                ),
                generate_tags_inner(
                    Replay.create_opponent_tag, replay_data_extractor.opponent
                ),
            ]
        )
