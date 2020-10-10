import urllib.request
from typing import ClassVar

import guy

from cerebrate.cerebrate import Cerebrate

from cerebrate.core import Replay


# noinspection PyPep8Naming
class Index(guy.Guy):
    size = (800, 800)

    cerebrate: ClassVar[Cerebrate] = Cerebrate()

    async def selectReplay(self, payload: dict):
        with urllib.request.urlopen(payload["replayData"]) as replay_data:
            replay = Index.cerebrate.save_replay_data(replay_data, payload["replayId"])
        if not replay:
            return

        replay = Index.cerebrate.load_replay_info(replay)
        Index.cerebrate.save_replay_info(replay)
        await self.js.replayLoaded(
            {
                "replayId": replay.replay_hash,
                "replayTimestamp": replay.timestamp,
                "teams": [team.name for team in replay.teams],
                "playerTeam": replay.player_team,
                "opponentTeam": replay.opponent_team,
                "selectedTags": replay.tags,
                "notes": "",
            }
        )

    async def submitTaggedReplay(self, payload: dict):
        with urllib.request.urlopen(payload["replayData"]) as replay_data:
            replay = Index.cerebrate.save_replay_data(replay_data, payload["replayId"])
        if not replay:
            await self.js.replaySubmitted({"success": False})
            return

        Index.cerebrate.save_replay_info(set_replay_info_from_payload(replay, payload))

        await self.js.replayUpdated({"success": True, "replayId": replay.replay_hash})


def set_replay_info_from_payload(replay: Replay, payload: dict) -> Replay:
    replay.tags.extend(payload["selectedTags"])
    replay.player_team = payload["playerTeam"]
    replay.opponent_team = payload["opponentTeam"]
    return replay


def main():
    app = Index()
    app.run(one=True)


if __name__ == "__main__":
    main()
