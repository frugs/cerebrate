from typing import List

from cerebrate.core import Replay
from cerebrate.processor.extractor import ReplayDataExtractor

from .tag_generator import TagGenerator

MATCHUPS = ["pvp", "pvt", "pvz", "tvp", "tvt", "tvz", "zvp", "zvt", "zvz"]


class MatchupTagGenerator(TagGenerator):
    def tags_to_remove(self) -> List[str]:
        return [Replay.create_game_tag(matchup) for matchup in MATCHUPS]

    def generate_tags(
        self, replay: Replay, replay_data_extractor: ReplayDataExtractor
    ) -> List[str]:
        if (
            not replay_data_extractor.player
            or not replay_data_extractor.player.play_race
            or not replay_data_extractor.opponent
            or not replay_data_extractor.opponent.play_race
        ):
            return []

        matchup = (
            replay_data_extractor.player.play_race[:1]
            + "v"
            + replay_data_extractor.opponent.play_race[:1]
        ).lower()

        return [Replay.create_game_tag(matchup)]
