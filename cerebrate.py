import os.path
import click
import replaymanager
import replaysearch

APP_DATA_PATH = os.path.expanduser("~/.cerebrate")

_replay_manager = replaymanager.ReplayManager(APP_DATA_PATH)


@click.group()
def cli():
    pass


@click.command(name="add-tag")
@click.option("--most-recent-replay", "-m", type=bool, is_flag=True, help="Use your most recently replay")
@click.option("--replay", "-r", type=click.Path(), help="Path to the replay to tag")
@click.argument('tags', nargs=-1, type=str)
def add_tag(most_recent_replay, replay, tags):
    if not replay and not most_recent_replay:
        raise click.UsageError("replay to tag not specified")

    if not tags:
        raise click.UsageError("no tags specified")

    if not replay and most_recent_replay:
        replay = replaysearch.find_most_recent_replay()

    _replay_manager.tag_replay(replay, list(tags))


@click.command(name="remove-tag")
@click.option("--most-recent-replay", "-m", type=bool, is_flag=True, help="Use your most recently replay")
@click.option("--replay", "-r", type=click.Path(), help="Path to the replay to tag")
@click.argument('tags', nargs=-1, type=str)
def remove_tag(most_recent_replay, replay, tags):
    if not replay and not most_recent_replay:
        raise click.UsageError("replay to tag not specified")

    if not tags:
        raise click.UsageError("no tags specified")

    if not replay and most_recent_replay:
        replay = replaysearch.find_most_recent_replay()

    _replay_manager.untag_replay(replay, list(tags))

cli.add_command(add_tag)
cli.add_command(remove_tag)

if __name__ == '__main__':
    cli()