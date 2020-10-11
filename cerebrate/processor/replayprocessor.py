from typing import Final

import sc2reader
import sc2reader.resources

from cerebrate.core import Replay
from cerebrate.db import ReplayStore
from cerebrate.processor.extractor import create_extractors
from cerebrate.processor.rule import create_rules


class ReplayProcessor:
    replay_store: Final[ReplayStore]

    def __init__(self, replay_store: ReplayStore):
        self.replay_store = replay_store

    def process_replay(self, replay: Replay) -> Replay:
        # noinspection PyUnresolvedReferences
        sc2reader_replay: sc2reader.resources.Replay = sc2reader.load_replay(
            replay.path, load_level=4
        )

        for extractor in create_extractors():
            replay = extractor.extract_replay_info(replay, sc2reader_replay)

        for rule in create_rules(self.replay_store):
            replay = rule.apply_replay_rule(replay)

        return replay
