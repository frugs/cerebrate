from typing import List

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor
from .tag_generator import TagGenerator


AI_TAG = "ai"


class AITagGenerator(TagGenerator):
    def tags_to_remove(self) -> List[str]:
        return [
            Replay.create_player_tag(AI_TAG),
            Replay.create_opponent_tag(AI_TAG),
        ]

    def generate_tags(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> List[str]:
        tags: List[str] = []

        if replay_data_extractor.player and not replay_data_extractor.player.is_human:
            tags.append(Replay.create_player_tag(AI_TAG))

        if (
            replay_data_extractor.opponent
            and not replay_data_extractor.opponent.is_human
        ):
            tags.append(Replay.create_opponent_tag(AI_TAG))

        return tags
