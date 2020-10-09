from typing import Optional, Final


class ReplayQuery:

    replay_hash: Final[Optional[str]]

    def __init__(self, replay_hash: Optional[str] = None):
        self.replay_hash = replay_hash
