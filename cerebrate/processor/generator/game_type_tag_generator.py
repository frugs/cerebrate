from typing import List

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor
from .tag_generator import TagGenerator


GAME_TYPES = ["1v1", "2v2", "3v3", "4v4", "ffa"]


class GameTypeTagGenerator(TagGenerator):
    def tags_to_remove(self) -> List[str]:
        return [Replay.create_game_tag(game_type) for game_type in GAME_TYPES]

    def generate_tags(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> List[str]:

        game_type = replay_data_extractor.source_replay_data.game_type.lower()
        if game_type in GAME_TYPES:
            return [Replay.create_game_tag(game_type)]

        return []
