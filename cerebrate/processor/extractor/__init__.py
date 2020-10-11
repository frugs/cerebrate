from typing import List

from .extractor import Extractor
from .replay_date_extractor import ReplayDateExtractor as _ReplayDateExtractor
from .team_data_extractor import TeamDataExtractor as _TeamDataExtractor


def create_extractors() -> List[Extractor]:
    return [
        _ReplayDateExtractor(),
        _TeamDataExtractor()
    ]
