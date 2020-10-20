from typing import Final

import sc2reader
import sc2reader.resources

from cerebrate.core import Replay
from cerebrate.db import ReplayStore

from .extractor import ReplayDataExtractor
from .generator import create_tag_generators
from .preprocessor import create_preprocessors
from ..util import flatten


class ReplayProcessor:
    _replay_store: Final[ReplayStore]

    def __init__(self, replay_store: ReplayStore):
        self._replay_store = replay_store

    def process_replay(self, replay: Replay) -> Replay:
        replay_data_extractor = ReplayDataExtractor(replay)

        for preprocessor in create_preprocessors(self._replay_store):
            replay = preprocessor.preprocess_replay(replay, replay_data_extractor)

        tag_generators = create_tag_generators()
        for tag in flatten(
            tag_generator.tags_to_remove() for tag_generator in tag_generators
        ):
            replay.remove_tag(tag)

        new_tags = (
            flatten(
                tag_generator.generate_tags(replay, replay_data_extractor)
                for tag_generator in tag_generators
            )
            + replay.tags
        )

        replay.set_tags(new_tags)

        return replay
