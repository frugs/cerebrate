from typing import List

from cerebrate.db import ReplayStore

from .auto_set_player_opponent_rule import AutoSetPlayerOpponentRule
from .extractor import Extractor
from .replay_date_extractor import ReplayDateExtractor
from .team_data_extractor import TeamDataExtractor


def create_extractors(replay_store: ReplayStore) -> List[Extractor]:
    return [ReplayDateExtractor(), TeamDataExtractor(), AutoSetPlayerOpponentRule(replay_store)]
