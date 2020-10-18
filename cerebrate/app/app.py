import base64
import os
import urllib.request
from typing import ClassVar

import guy

from cerebrate.cerebrate import Cerebrate
from cerebrate.core import Replay
from cerebrate.core.replay_query import ReplayQuery


def _make_replay_payload(replay: Replay) -> dict:
    return {
        "replayId": replay.replay_hash,
        "replayTimestamp": replay.timestamp,
        "teams": [team.name for team in replay.teams],
        "playerTeam": replay.player_team,
        "opponentTeam": replay.opponent_team,
        "selectedTags": replay.tags,
        "notes": "",
    }


def _set_replay_info_from_payload(replay: Replay, payload: dict) -> Replay:
    replay.tags.extend(payload["selectedTags"])
    replay.notes = payload["notes"]
    replay.player_team = payload["playerTeam"]
    replay.opponent_team = payload["opponentTeam"]
    return replay


# noinspection PyPep8Naming
class Index(guy.Guy):
    size = (1200, 800)

    cerebrate: ClassVar[Cerebrate] = Cerebrate()

    async def selectMostRecentReplay(self):
        replay_path = Cerebrate.find_most_recent_replay_path()
        if not replay_path:
            return

        with open(replay_path, "rb") as replay_data:
            replay = Index.cerebrate.save_replay_data(replay_data)
            if not replay:
                return

            replay_data.seek(0)
            prefix = "data:application/octet-stream;base64,"
            data_url = prefix + base64.b64encode(replay_data.read()).decode("ascii")

        replay = Index.cerebrate.load_replay_info(replay)
        Index.cerebrate.update_replay_info(replay)
        await self.js.replayLoaded(
            {
                **_make_replay_payload(replay),
                "replayFileName": os.path.split(replay_path)[1],
                "replayData": data_url,
                "force": True,
            }
        )

    async def selectReplay(self, payload: dict):
        with urllib.request.urlopen(payload["replayData"]) as replay_data:
            replay = Index.cerebrate.save_replay_data(replay_data, payload["replayId"])
        if not replay:
            return

        replay = Index.cerebrate.load_replay_info(replay)
        Index.cerebrate.update_replay_info(replay)
        await self.js.replayLoaded(_make_replay_payload(replay))

    async def selectPlayerOpponent(self, payload: dict):
        replay = self.cerebrate.find_replay(payload["replayId"])
        if not replay:
            return

        replay.player_team = payload["playerTeam"]
        replay.opponent_team = payload["opponentTeam"]
        Index.cerebrate.update_replay_info(replay)
        replay = Index.cerebrate.load_replay_info(replay)

        await self.js.replayLoaded(_make_replay_payload(replay))

    async def updateReplayInfo(self, payload: dict):
        with urllib.request.urlopen(payload["replayData"]) as replay_data:
            replay = Index.cerebrate.save_replay_data(replay_data, payload["replayId"])
        if not replay:
            await self.js.replayUpdated({"success": False})
            return

        Index.cerebrate.update_replay_info(
            _set_replay_info_from_payload(replay, payload)
        )

        await self.js.replayUpdated({"success": True, "replayId": replay.replay_hash})

    async def findReplays(self, payload: dict):
        query = ReplayQuery(
            include_tags=payload.get("includeTags"),
            exclude_tags=payload.get("excludeTags"),
        )
        replays = self.cerebrate.find_replays(query)
        frequency_table = self.cerebrate.calculate_tag_frequency_table(
            replays, query.include_tags
        )

        return {
            "replays": [_make_replay_payload(replay) for replay in replays],
            "tagFrequencyTable": [
                {
                    "tag": tag,
                    "frequency": frequency,
                }
                for tag, frequency in frequency_table.items()
            ],
        }


def main():
    app = Index()
    app.run(one=True)


if __name__ == "__main__":
    main()
