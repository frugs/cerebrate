from typing import List

from .ai_tag_generator import AITagGenerator
from .game_type_tag_generator import GameTypeTagGenerator
from .map_tag_generator import MapTagGenerator
from .matchup_tag_generator import MatchupTagGenerator
from .mech_bio_tag_generator import MechBioTagGenerator
from .proxy_tag_generator import ProxyTagGenerator
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
        AITagGenerator(),
        GameTypeTagGenerator(),
        MapTagGenerator(),
        ProxyTagGenerator(),
        MechBioTagGenerator(),
    ]
