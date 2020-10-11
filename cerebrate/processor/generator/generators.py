from typing import List

from .matchup_tag_generator import MatchupTagGenerator
from .race_tag_generator import RaceTagGenerator
from .random_tag_generator import RandomTagGenerator
from .result_tag_generator import ResultTagGenerator
from .tag_generator import TagGenerator


def create_tag_generators() -> List[TagGenerator]:
    return [
        RaceTagGenerator(),
        RandomTagGenerator(),
        ResultTagGenerator(),
        MatchupTagGenerator(),
    ]
