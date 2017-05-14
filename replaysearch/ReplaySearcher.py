import sys
import os
import glob


def find_most_recent_replay() -> str:
    if sys.platform == "darwin":
        accounts_dir = os.path.expanduser("~/Library/Application Support/Blizzard/StarCraft II/Accounts")
    elif sys.platform == "win32":
        accounts_dir = os.path.expanduser("~/Documents/StarCraft II/Accounts")
    else:
        raise RuntimeError("This platform is not supported for this operation.")

    replays = glob.glob(accounts_dir + "/*/*/Replays/Multiplayer/*.SC2Replay", recursive=True)

    if not replays:
        raise RuntimeError("Could not any replays!")

    return next(iter(sorted([replay for replay in replays], key=os.path.getmtime, reverse=True)))
