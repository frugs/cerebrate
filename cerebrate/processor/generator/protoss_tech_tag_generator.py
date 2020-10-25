from typing import List, Optional

import sc2reader.data
import sc2reader.objects

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor
from cerebrate.util import flatten
from .tag_generator import TagGenerator

_PROTOSS_TECH_STRUCTURES = {
    "TwilightCouncil": "twilight",
    "Stargate": "stargate",
    "RoboticsFacility": "robo",
}


class ProtossTechTagGenerator(TagGenerator):
    def tags_to_remove(self) -> List[str]:
        return flatten(
            [
                [
                    tag_factory(tag_name)
                    for _, tag_name in _PROTOSS_TECH_STRUCTURES.items()
                ]
                for tag_factory in [
                    Replay.create_player_tag,
                    Replay.create_opponent_tag,
                ]
            ]
        )

    def generate_tags(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> List[str]:
        def generate_tags_inner(
            participant: Optional[sc2reader.objects.Participant],
        ) -> List[str]:
            if not participant or not participant.units:
                return []

            protoss_tech_structures = [
                unit
                for unit in participant.units
                if unit.started_at <= ReplayDataExtractor.EARLY_GAME_END
                and ReplayDataExtractor.get_original_unit_name(unit)
                in _PROTOSS_TECH_STRUCTURES
            ]
            protoss_tech_structures.sort(key=lambda unit: unit.started_at)

            if not protoss_tech_structures:
                return []

            tech_structure_name = ReplayDataExtractor.get_original_unit_name(
                protoss_tech_structures[0]
            )
            tag_name = _PROTOSS_TECH_STRUCTURES[tech_structure_name]
            return [tag_name]

        return [
            Replay.create_player_tag(tag_name)
            for tag_name in generate_tags_inner(replay_data_extractor.player)
        ] + [
            Replay.create_opponent_tag(tag_name)
            for tag_name in generate_tags_inner(replay_data_extractor.opponent)
        ]
