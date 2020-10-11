from typing import List

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor

from .tag_generator import TagGenerator

PLAYER_RANDOM_TAG = Replay.create_player_tag("random")
OPPONENT_RANDOM_TAG = Replay.create_opponent_tag("random")


class RandomTagGenerator(TagGenerator):
    def tags_to_remove(self) -> List[str]:
        return [PLAYER_RANDOM_TAG, OPPONENT_RANDOM_TAG]

    def generate_tags(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> List[str]:
        tags: List[str] = []

        if (
            not replay_data_extractor.player
            or not replay_data_extractor.player.pick_race
        ):
            return tags

        if replay_data_extractor.player.pick_race == "Random":
            tags.append(PLAYER_RANDOM_TAG)

        if (
            not replay_data_extractor.opponent
            or not replay_data_extractor.opponent.pick_race
        ):
            return tags

        if replay_data_extractor.opponent.pick_race == "Random":
            tags.append(OPPONENT_RANDOM_TAG)

        return tags
