from typing import List

from cerebrate.db import ReplayStore
from cerebrate.processor.rule.rule import Rule

from .auto_set_player_opponent_rule import \
    AutoSetPlayerOpponentRule as _AutoSetPlayerOpponentRule


def create_rules(replay_store: ReplayStore) -> List[Rule]:
    return [_AutoSetPlayerOpponentRule(replay_store)]
