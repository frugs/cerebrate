from typing import List, Optional


class ReplayQuery:
    include_tags: List[str]

    def __init__(self, include_tags: Optional[List[str]]):
        if include_tags is None:
            include_tags = []

        self.include_tags = include_tags
