import sc2reader
import sc2reader.resources

from cerebrate.core import Replay
from cerebrate.processor.rule import get_rules
from cerebrate.processor.extractor import get_extractors


class ReplayProcessor:
    def process_replay(self, replay: Replay) -> Replay:
        # noinspection PyUnresolvedReferences
        sc2reader_replay: sc2reader.resources.Replay = sc2reader.load_replay(replay.path, load_level=4)

        for extractor in get_extractors():
            replay = extractor.extract_replay_info(replay, sc2reader_replay)

        for rule in get_rules():
            replay = rule.apply_replay_rule(replay)

        return replay
