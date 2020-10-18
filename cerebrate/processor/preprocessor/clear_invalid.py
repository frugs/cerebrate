from typing import final

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor
from .replay_preprocessor import ReplayPreprocessor


class ClearInvalid(ReplayPreprocessor):
    @final
    def preprocess_replay(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> Replay:
        if replay.opponent_team is not None or replay.player_team is not None:
            # Player and opponent team shouldn't be the same
            if replay.opponent_team == replay.player_team:
                replay.player_team = None
                replay.opponent_team = None

        return replay
