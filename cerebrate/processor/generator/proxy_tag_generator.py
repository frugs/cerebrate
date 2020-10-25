from typing import List, Optional, Callable

import sc2reader.data
import sc2reader.objects

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor
from cerebrate.util import flatten
from .tag_generator import TagGenerator

_PROXY_TAG_PREFIX = "proxy_"

_PRODUCTION_STRUCTURES = [
    "Starport",
    "Factory",
    "Barracks",
    "CommandCenter",
    "RoboticsFacility",
    "Stargate",
    "Gateway",
    "Nexus",
    "Hatchery",
]


def _make_tag(tag_factory: Callable[[str], str], structure_name: str) -> str:
    return tag_factory(_PROXY_TAG_PREFIX + structure_name.lower())


class ProxyTagGenerator(TagGenerator):
    def tags_to_remove(self) -> List[str]:
        tag_factories = [Replay.create_player_tag, Replay.create_opponent_tag]
        return flatten(
            [
                [
                    _make_tag(tag_factory, structure)
                    for structure in _PRODUCTION_STRUCTURES
                ]
                for tag_factory in tag_factories
            ]
        )

    def generate_tags(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> List[str]:
        def get_proxy_structures(
            participant: Optional[sc2reader.objects.Participant],
        ) -> List[str]:
            if not participant:
                return []

            result = [
                ReplayDataExtractor.get_original_unit_name(unit)
                for unit in participant.units
                if unit.started_at <= ReplayDataExtractor.EARLY_GAME_END
                and unit.is_building
                and ReplayDataExtractor.get_original_unit_name(unit)
                in _PRODUCTION_STRUCTURES
                and replay_data_extractor.is_proxy(unit)
            ]
            result.sort(key=lambda structure: _PRODUCTION_STRUCTURES.index(structure))
            return result

        tags = []
        if replay_data_extractor.player:
            proxy_structures = get_proxy_structures(replay_data_extractor.player)
            if proxy_structures:
                # Only tag with primary proxy structure
                tags.append(_make_tag(Replay.create_player_tag, proxy_structures[0]))

        if replay_data_extractor.opponent:
            proxy_structures = get_proxy_structures(replay_data_extractor.opponent)
            if proxy_structures:
                # Only tag with primary proxy structure
                tags.append(_make_tag(Replay.create_opponent_tag, proxy_structures[0]))

        return tags
