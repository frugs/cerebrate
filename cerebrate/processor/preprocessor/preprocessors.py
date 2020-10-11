from typing import List

from cerebrate.db import ReplayStore

from .replay_preprocessor import ReplayPreprocessor
from .set_player_and_opponent import SetPlayerAndOpponent
from .set_replay_timestamp import SetReplayTimestamp
from .set_teams_preprocessor import SetTeams


def create_preprocessors(replay_store: ReplayStore) -> List[ReplayPreprocessor]:
    return [SetReplayTimestamp(), SetTeams(), SetPlayerAndOpponent(replay_store)]
