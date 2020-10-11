from typing import Final

import sc2reader
import sc2reader.resources

from cerebrate.core import Replay


class ReplayDataExtractor:
    replay_info: Final[Replay]
    source_replay_data: Final[sc2reader.resources.Replay]

    def __init__(self, replay: Replay):
        self.replay_info = replay
        # noinspection PyUnresolvedReferences
        self.source_replay_data = sc2reader.load_replay(replay.path, load_level=4)
