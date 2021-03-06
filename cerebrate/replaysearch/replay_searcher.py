import glob
import os
import sys
from typing import Optional


class ReplaySearcher:
    @staticmethod
    def get_most_recently_played_replay_path() -> Optional[str]:
        if sys.platform == "darwin":
            accounts_dir = os.path.expanduser(
                "~/Library/Application Support/Blizzard/StarCraft II/Accounts"
            )
        elif sys.platform == "win32":
            accounts_dir = os.path.expanduser("~/Documents/StarCraft II/Accounts")
        else:
            raise RuntimeError("This platform is not supported for this operation.")

        replays = glob.glob(
            accounts_dir + "/*/*/Replays/Multiplayer/*.SC2Replay", recursive=True
        )

        if not replays:
            return None

        return next(
            iter(
                sorted(
                    [replay for replay in replays], key=os.path.getmtime, reverse=True
                )
            )
        )
