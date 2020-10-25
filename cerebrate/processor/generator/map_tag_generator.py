import re
from typing import List

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor
from .tag_generator import TagGenerator

_MAP_TAG_PREFIX = "map_"


class MapTagGenerator(TagGenerator):
    def tags_to_remove(self) -> List[str]:
        # TODO: Maybe try and find some way of figuring this out statically
        return []

    def generate_tags(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> List[str]:
        map_name: str = replay_data_extractor.source_replay_data.map_name
        map_name = map_name.lower()
        map_name = re.sub(r"[^\w\s]", "", map_name)
        map_name = re.sub(r"\s+", "_", map_name)
        return [Replay.create_game_tag(_MAP_TAG_PREFIX + map_name)]
