import sc2reader.resources

from cerebrate.core import Replay

from .extractor import Extractor


class ReplayDateExtractor(Extractor):
    def extract_replay_info(
        self, replay: Replay, sc2reader_replay: sc2reader.resources.Replay
    ) -> Replay:
        replay.timestamp = sc2reader_replay.unix_timestamp
        return replay
