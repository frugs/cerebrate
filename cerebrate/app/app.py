import urllib.request
from typing import ClassVar

import guy

from cerebrate.cerebrate import Cerebrate


class Index(guy.Guy):
    size = (800, 800)

    cerebrate: ClassVar[Cerebrate] = Cerebrate()

    # noinspection PyPep8Naming
    def submitTaggedReplay(self, payload: dict):
        with urllib.request.urlopen(payload["replayData"]) as replay_data:
            replay = Index.cerebrate.save_replay_data(replay_data, payload["replayId"])
        if not replay:
            return

        replay.tags.extend(payload["selectedTags"])
        Index.cerebrate.save_tagged_replay(replay)


def main():
    app = Index()
    app.run(one=True)


if __name__ == "__main__":
    main()
