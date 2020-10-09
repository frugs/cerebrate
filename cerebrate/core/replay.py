import functools
import hashlib
from typing import Final, final, BinaryIO, List


@final
class Replay:
    PLAYER_TAG_PREFIX: Final = "player:"
    OPP_TAG_PREFIX: Final = "opponent:"
    GAME_TAG_PREFIX: Final = "game:"

    path: Final[str]
    replay_hash: Final[str]
    tags: Final[List[str]]

    @classmethod
    def hash_replay_data(cls, replay_data: BinaryIO) -> str:
        hash_calculator = hashlib.sha256()

        for buf in iter(functools.partial(replay_data.read, 4096), b""):
            hash_calculator.update(buf)

        return hash_calculator.hexdigest()

    @classmethod
    def hash_replay_from_path(cls, replay_path: str) -> str:
        with open(replay_path, "rb") as replay_file:
            return Replay.hash_replay_data(replay_file)

    def __init__(self, path: str, replay_hash: str = "", tags=None):
        if not replay_hash:
            replay_hash = Replay.hash_replay_from_path(path)

        if tags is None:
            tags = []

        self.path = path
        self.replay_hash = replay_hash
        self.tags = tags

    def add_tag(self, tag: str):
        if tag not in set(self.tags):
            self.tags.append(tag)

    def remove_tag(self, tag: str):
        self.tags.remove(tag)

    def add_player_tag(self, player_tag: str):
        self.add_tag(Replay.PLAYER_TAG_PREFIX + player_tag)

    def remove_player_tag(self, player_tag: str):
        self.remove_tag(Replay.PLAYER_TAG_PREFIX + player_tag)

    def add_opp_tag(self, opp_tag: str):
        self.add_tag(Replay.OPP_TAG_PREFIX + opp_tag)

    def remove_opp_tag(self, opp_tag: str):
        self.remove_tag(Replay.OPP_TAG_PREFIX + opp_tag)

    def add_game_tag(self, game_tag: str):
        self.add_tag(Replay.GAME_TAG_PREFIX + game_tag)

    def remove_game_tag(self, game_tag: str):
        self.remove_tag(Replay.GAME_TAG_PREFIX + game_tag)
