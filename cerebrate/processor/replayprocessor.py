from typing import Final

import sc2reader
import sc2reader.resources

from cerebrate.core import Replay
from cerebrate.db import ReplayStore

from .extractor import ReplayDataExtractor
from .generator import create_tag_generators
from .preprocessor import create_preprocessors


class ReplayProcessor:
    _replay_store: Final[ReplayStore]

    def __init__(self, replay_store: ReplayStore):
        self._replay_store = replay_store

    def process_replay(self, replay: Replay) -> Replay:
        replay_data_extractor = ReplayDataExtractor(replay)

        for preprocessor in create_preprocessors(self._replay_store):
            replay = preprocessor.preprocess_replay(replay, replay_data_extractor)

        for tag_generator in create_tag_generators():
            for tag in tag_generator.tags_to_remove():
                replay.remove_tag(tag)
            for tag in tag_generator.generate_tags(replay, replay_data_extractor):
                replay.prepend_tag(tag)

        return replay
