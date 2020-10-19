from typing import List, Optional


class ReplayQuery:
    include_tags: List[str]
    exclude_tags: List[str]
    start_timestamp: Optional[int]
    end_timestamp: Optional[int]

    def __init__(
        self,
        include_tags: Optional[List[str]] = None,
        exclude_tags: Optional[List[str]] = None,
        start_timestamp: Optional[int] = None,
        end_timestamp: Optional[int] = None,
    ):
        if include_tags is None:
            include_tags = []
        if exclude_tags is None:
            exclude_tags = []

        self.include_tags = include_tags
        self.exclude_tags = exclude_tags
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
