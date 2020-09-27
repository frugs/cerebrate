import glob
import os

import click

from cerebrate import replaysearch, replaymanager

APP_DATA_PATH = os.path.expanduser("~/.cerebrate")

_replay_manager = replaymanager.ReplayManager(APP_DATA_PATH)


def add_tag(most_recent_replay, replay, tags):
    """
    Add tags to a replay.
    """
    if not replay and not most_recent_replay:
        raise click.UsageError("replay to tag not specified")

    if not replay and most_recent_replay:
        replay = replaysearch.find_most_recent_replay()

    _replay_manager.tag_replay(replay, list(tags))


def remove_tag(most_recent_replay, replay, tags):
    """
    Remove tags from a replay.
    """
    if not replay and not most_recent_replay:
        raise click.UsageError("replay to tag not specified")

    if not replay and most_recent_replay:
        replay = replaysearch.find_most_recent_replay()

    _replay_manager.untag_replay(replay, list(tags))


def query_replays(source_list, source_dir, output_dir, match_any_tag, inverse, tags):
    if output_dir and not os.path.isdir(output_dir):
        raise click.UsageError("output directory is not a directory")

    source_replays = find_and_add_source_replays(source_list, source_dir)

    replays_paths = _replay_manager.query_replays(
        match_any_tag, inverse, source_replays, list(tags)
    )

    return replays_paths


def tag_frequency(source_list, source_dir):
    source_replays = find_and_add_source_replays(source_list, source_dir)

    return _replay_manager.tag_frequency(source_replays)


def find_and_add_source_replays(source_list, source_dir):
    source_replays = []
    if source_list:
        while True:
            source = source_list.readline()
            if source:
                source_replays.append(source)
            else:
                break
    if source_dir:
        if not os.path.isdir(source_dir):
            raise click.UsageError("source dir should be a directory!")

        source_replays.extend(glob.glob(os.path.join(source_dir, "*.SC2Replay")))
    for replay in source_replays:
        _replay_manager.tag_replay(replay, [])
    return source_replays
