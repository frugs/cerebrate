import base64
import os
import subprocess
import sys
import tempfile
import urllib.request
from typing import ClassVar, Optional, List

import guy

from cerebrate.app import native_gui_utils
from cerebrate.cerebrate import Cerebrate
from cerebrate.core import Replay
from cerebrate.core.replay_query import ReplayQuery


def _make_replay_payload(replay: Replay, force: bool = False) -> dict:
    return {
        "replayId": replay.replay_hash,
        "replayTimestamp": replay.timestamp,
        "teams": [team.name for team in replay.teams],
        "playerTeam": replay.player_team,
        "opponentTeam": replay.opponent_team,
        "selectedTags": replay.tags,
        "notes": "",
        "force": force,
    }


def _set_replay_info_from_payload(replay: Replay, payload: dict) -> Replay:
    replay.set_tags(payload.get("selectedTags", []))
    replay.notes = payload.get("notes", "")
    replay.player_team = payload.get("playerTeam")
    replay.opponent_team = payload.get("opponentTeam")
    return replay


def _replays_from_hashes(cerebrate: Cerebrate, replay_hashes: List[str]):
    return [cerebrate.find_replay(replay_hash) for replay_hash in replay_hashes]


def _cross_platform_open(path: str):
    if sys.platform == "win32":
        os.startfile(path)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


# noinspection PyPep8Naming, PyMethodMayBeStatic
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
        replay_hash: str = payload["replayId"]
        replay_url: Optional[str] = payload.get("replayData")
        if replay_url:
            with urllib.request.urlopen(replay_url) as replay_data:
                replay = Index.cerebrate.save_replay_data(replay_data, replay_hash)
        else:
            replay = Index.cerebrate.find_replay(replay_hash)

        if not replay:
            return

        replay = Index.cerebrate.load_replay_info(replay)
        Index.cerebrate.update_replay_info(replay)
        await self.js.replayLoaded(
            _make_replay_payload(replay, payload.get("force", False))
        )

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
        replay_hash: str = payload["replayId"]
        replay_url: Optional[str] = payload.get("replayData")
        if replay_url:
            with urllib.request.urlopen(replay_url) as replay_data:
                replay = Index.cerebrate.save_replay_data(replay_data, replay_hash)
        else:
            replay = Index.cerebrate.find_replay(replay_hash)

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
            start_timestamp=payload.get("startTimestamp"),
            end_timestamp=payload.get("endTimestamp"),
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

    async def forgetReplays(self, payload: dict):
        replay_hashes: List[str] = payload.get("replayIds", [])
        for replay_hash in replay_hashes:
            self.cerebrate.forget_replay(replay_hash)

    async def exportReplaysToTempDir(self, payload: dict):
        # no automatic cleanup - let os handle cleanup
        export_path = tempfile.mkdtemp()
        replay_hashes: List[str] = payload.get("replayIds", [])
        replays = _replays_from_hashes(self.cerebrate, replay_hashes)
        Cerebrate.export_replays_to_directory(replays, export_path)
        return export_path

    async def exportReplaysToTargetDir(self, payload: dict):
        export_path = await native_gui_utils.open_directory_picker(
            title="Export to directory"
        )
        if not export_path:
            return None

        replay_hashes: List[str] = payload.get("replayIds", [])
        replays = _replays_from_hashes(self.cerebrate, replay_hashes)
        Cerebrate.export_replays_to_directory(replays, export_path)
        return export_path

    async def openDirInFileManager(self, payload: dict):
        path = payload.get("dirPath")
        if not path:
            return None

        _cross_platform_open(path)

    async def getScelightPath(self):
        return self.cerebrate.settings.scelight_path

    async def selectScelightPath(self):
        scelight_path = await native_gui_utils.open_file_picker(
            title="Choose Scelight installation"
        )
        if not scelight_path:
            return None

        self.cerebrate.settings.scelight_path = os.path.normpath(scelight_path)

        return scelight_path


def main():
    app = Index()
    app.run(one=True)


if __name__ == "__main__":
    main()
