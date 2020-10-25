from typing import List, Optional, Callable

import sc2reader.data
import sc2reader.objects

from sc2reader.data import Unit

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor
from cerebrate.util import flatten
from .tag_generator import TagGenerator

BIO_TAG_NAME = "bio"
MECH_TAG_NAME = "mech"

_BIO_UNITS = [
    "Marine",
    "Marauder",
    "Medivac",
]

_MECH_UNITS = [
    "Hellion",
    "BattleHellion",
    "Cyclone",
    "SiegeTank",
    "Thor",
]


class MechBioTagGenerator(TagGenerator):
    def tags_to_remove(self) -> List[str]:
        return flatten(
            [
                [tag_factory(BIO_TAG_NAME), tag_factory(MECH_TAG_NAME)]
                for tag_factory in [
                    Replay.create_player_tag,
                    Replay.create_opponent_tag,
                ]
            ]
        )

    def generate_tags(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> List[str]:
        def get_army_supply(
            participant: Optional[sc2reader.objects.Participant],
            predicate: Callable[[Unit], bool] = None,
        ) -> float:
            def apply_predicate(unit: Unit) -> bool:
                return True if predicate is None else predicate(unit)

            if not participant:
                return 0

            army_units = [
                unit
                for unit in participant.units
                if unit.is_army
                and apply_predicate(unit)
                and unit.started_at < ReplayDataExtractor.LATE_GAME_START
            ]
            return sum(unit.supply for unit in army_units)

        def get_bio_supply(
            participant: Optional[sc2reader.objects.Participant],
        ) -> float:
            return get_army_supply(
                participant,
                lambda unit: ReplayDataExtractor.get_original_unit_name(unit)
                in _BIO_UNITS,
            )

        def get_mech_supply(
            participant: Optional[sc2reader.objects.Participant],
        ) -> float:
            return get_army_supply(
                participant,
                lambda unit: ReplayDataExtractor.get_original_unit_name(unit)
                in _MECH_UNITS,
            )

        def generate_tags_inner(
            participant: Optional[sc2reader.objects.Participant],
            tag_factory: Callable[[str], str],
        ) -> List[str]:
            bio_supply = get_bio_supply(participant)
            mech_supply = get_mech_supply(participant)
            army_supply = get_army_supply(participant)

            tags = []
            if (
                bio_supply > mech_supply
                and bio_supply > army_supply * 0.5
                and bio_supply > 35
            ):
                tags.append(tag_factory(BIO_TAG_NAME))
            if (
                mech_supply > bio_supply
                and mech_supply > army_supply * 0.5
                and mech_supply > 35
            ):
                tags.append(tag_factory(MECH_TAG_NAME))
            return tags

        return flatten(
            [
                generate_tags_inner(
                    replay_data_extractor.player, Replay.create_player_tag
                ),
                generate_tags_inner(
                    replay_data_extractor.opponent, Replay.create_opponent_tag
                ),
            ]
        )
