from typing import List, Optional

import sc2reader.data
import sc2reader.objects
from sc2reader.data import Unit

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor
from .tag_generator import TagGenerator

CANNON_RUSH_TAG_NAME = "cannon_rush"


class CannonRushTagGenerator(TagGenerator):
    def tags_to_remove(self) -> List[str]:
        return [
            Replay.create_player_tag(CANNON_RUSH_TAG_NAME),
            Replay.create_opponent_tag(CANNON_RUSH_TAG_NAME),
        ]

    def generate_tags(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> List[str]:
        def get_cannons(
            participant: Optional[sc2reader.objects.Participant],
        ) -> List[Unit]:
            if not participant or not participant.units:
                return []

            return [
                unit
                for unit in participant.units
                if unit.started_at <= ReplayDataExtractor.EARLY_RUSH_END
                and unit.is_building
                and ReplayDataExtractor.get_original_unit_name(unit) == "PhotonCannon"
            ]

        tags = []

        if any(
            cannon
            for cannon in get_cannons(replay_data_extractor.player)
            if replay_data_extractor.is_proxy(cannon)
        ):
            tags.append(Replay.create_player_tag(CANNON_RUSH_TAG_NAME))

        if any(
            cannon
            for cannon in get_cannons(replay_data_extractor.opponent)
            if replay_data_extractor.is_proxy(cannon)
        ):
            tags.append(Replay.create_opponent_tag(CANNON_RUSH_TAG_NAME))

        return tags
