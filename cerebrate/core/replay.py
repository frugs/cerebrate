import functools
import hashlib
import os
from typing import BinaryIO, Final, List, Optional, final


@final
class Team:
    team_id: Final[str]
    name: Final[str]

    def __init__(self, team_id: str, name: str):
        self.team_id = team_id
        self.name = name


@final
class Replay:
    PLAYER_TAG_PREFIX: Final = "player:"
    OPP_TAG_PREFIX: Final = "opponent:"
    GAME_TAG_PREFIX: Final = "game:"

    path: Final[str]
    replay_hash: Final[str]

    tags: Final[List[str]]
    teams: Final[List[Team]]
    timestamp: Optional[int]
    player_team: Optional[int]
    opponent_team: Optional[int]

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

    @classmethod
    def create_player_tag(cls, tag_name: str):
        return Replay.PLAYER_TAG_PREFIX + tag_name

    @classmethod
    def create_opponent_tag(cls, tag_name: str):
        return Replay.OPP_TAG_PREFIX + tag_name

    @classmethod
    def create_game_tag(cls, tag_name: str):
        return Replay.GAME_TAG_PREFIX + tag_name

    def __init__(
        self,
        path: str,
        replay_hash: str = "",
        tags: Optional[List[str]] = None,
        teams: Optional[List[Team]] = None,
        timestamp: Optional[int] = None,
        player_team: Optional[int] = None,
        opponent_team: Optional[int] = None,
    ):
        if not replay_hash:
            replay_hash = Replay.hash_replay_from_path(path)

        if tags is None:
            tags = []

        if teams is None:
            teams = []

        self.path = os.path.normpath(path)
        self.replay_hash = replay_hash
        self.tags = tags
        self.teams = teams
        self.timestamp = timestamp
        self.player_team = player_team
        self.opponent_team = opponent_team

    def append_tag(self, tag: str):
        if tag not in set(self.tags):
            self.tags.append(tag)

    def prepend_tag(self, tag: str):
        if tag not in set(self.tags):
            new_tags = [tag] + self.tags
            self.tags.clear()
            self.tags.extend(new_tags)

    def remove_tag(self, tag: str):
        self.tags.remove(tag)
