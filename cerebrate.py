import os.path
import click
import replaymanager
import replaysearch
import glob

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

    if not replay and most_recent_replay:
        replay = replaysearch.find_most_recent_replay()

    _replay_manager.untag_replay(replay, list(tags))


@click.command(name="search")
@click.option("--source-list", "-l", type=click.File('r'), help="File containing list of replays files to query from")
@click.option("--source-dir", "-d", type=click.Path(), help="Directory containing replay files to query from")
@click.option("--match-any-tag", type=bool, is_flag=True, default=False,
              help="How to match tags on replays. Default is to match all tags.")
@click.option("--inverse", type=bool, is_flag=True, help="Search for replays not matching the tag")
@click.argument('tags', nargs=-1, type=str)
def search(source_list, source_dir, match_any_tag, inverse, tags):
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

    replays_paths = _replay_manager.query_replays(match_any_tag, inverse, source_replays, list(tags))
    for path in replays_paths:
        click.echo(path)

cli.add_command(add_tag)
cli.add_command(remove_tag)
cli.add_command(search)

if __name__ == '__main__':
    cli()
