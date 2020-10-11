from typing import List

from .race_tag_generator import RaceTagGenerator
from .tag_generator import TagGenerator


def create_tag_generators() -> List[TagGenerator]:
    return [RaceTagGenerator()]
