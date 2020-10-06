import functools
import hashlib
from typing import Set, Final, final, ClassVar


@final
class Replay:
    SELF_TAG_PREFIX: Final[ClassVar] = "self:"
    OPP_TAG_PREFIX: Final[ClassVar] = "opp:"
    GAME_TAG_PREFIX: Final[ClassVar] = "game:"

    path: Final[str]
    replay_hash: Final[str]
    tags: Final[Set[str]]

    @classmethod
    def hash_replay(cls, replay_path: str) -> str:
        with open(replay_path, "rb") as replay_file:
            hash_calculator = hashlib.sha256()

            for buf in iter(functools.partial(replay_file.read, 4096), b""):
                hash_calculator.update(buf)

            replay_hash = hash_calculator.hexdigest()
        return replay_hash

    def __init__(self, path: str, replay_hash: str = "", tags=None):
        if not replay_hash:
            replay_hash = Replay.hash_replay(path)

        if tags is None:
            tags = {}

        self.path = path
        self.replay_hash = replay_hash
        self.tags = tags

    def add_tag(self, tag: str):
        self.tags.add(tag)

    def remove_tag(self, tag: str):
        self.tags.remove(tag)

    def add_self_tag(self, self_tag: str):
        self.add_tag(Replay.SELF_TAG_PREFIX + self_tag)

    def remove_self_tag(self, self_tag: str):
        self.remove_tag(Replay.SELF_TAG_PREFIX + self_tag)

    def add_opp_tag(self, opp_tag: str):
        self.add_tag(Replay.OPP_TAG_PREFIX + opp_tag)

    def remove_opp_tag(self, opp_tag: str):
        self.remove_tag(Replay.OPP_TAG_PREFIX + opp_tag)
        
    def add_game_tag(self, game_tag: str):
        self.add_tag(Replay.GAME_TAG_PREFIX + game_tag)

    def remove_game_tag(self, game_tag: str):
        self.remove_tag(Replay.GAME_TAG_PREFIX + game_tag)