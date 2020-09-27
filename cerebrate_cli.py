import os
import shutil

import click

import cerebrate


@click.group()
def cli():
    """
    Use this tool to manage user-defined tags on StarCraft II replay files.
    """
    pass


@click.command(name="add-tag")
@click.option(
    "--most-recent-replay",
    "-m",
    type=bool,
    is_flag=True,
    help="Use your most recent replay.",
)
@click.option("--replay", "-r", type=click.Path(), help="Path to the replay to tag.")
@click.argument("tags", nargs=-1, type=str)
def add_tag(most_recent_replay, replay, tags):
    """
    Add tags to a replay.
    """
    cerebrate.add_tag(most_recent_replay, replay, tags)


@click.command(name="remove-tag")
@click.option(
    "--most-recent-replay",
    "-m",
    type=bool,
    is_flag=True,
    help="Use your most recently replay.",
)
@click.option("--replay", "-r", type=click.Path(), help="Path to the replay to tag.")
@click.argument("tags", nargs=-1, type=str)
def remove_tag(most_recent_replay, replay, tags):
    """
    Remove tags from a replay.
    """
    cerebrate.remove_tag(most_recent_replay, replay, tags)


@click.command(name="query-replays")
@click.option(
    "--source-list",
    "-l",
    type=click.File("r"),
    help="File containing list of replays files to query from.",
)
@click.option(
    "--source-dir",
    "-d",
    type=click.Path(),
    help="Directory containing replay files to query from. Use '-' to accept from stdin.",
)
@click.option(
    "--output-dir",
    "-o",
    type=click.Path(),
    help="Directory to copy matching replays to.",
)
@click.option(
    "--match-any-tag",
    type=bool,
    is_flag=True,
    default=False,
    help="How to match tags on replays. Default is to match all tags.",
)
@click.option(
    "--inverse",
    type=bool,
    is_flag=True,
    help="Search for replays not matching the tags.",
)
@click.argument("tags", nargs=-1, type=str)
def query_replays(source_list, source_dir, output_dir, match_any_tag, inverse, tags):
    """
    Query for replays which match tags.
    """
    replay_paths = cerebrate.query_replays(
        source_list, source_dir, output_dir, match_any_tag, inverse, tags
    )

    if output_dir:
        for path in replay_paths:
            shutil.copyfile(path, os.path.join(output_dir, os.path.basename(path)))
    else:
        for path in replay_paths:
            click.echo(path)


@click.command(name="tag-frequency")
@click.option(
    "--source-list",
    "-l",
    type=click.File("r"),
    help="File containing list of replays files to query from. Use '-' to accept from stdin.",
)
@click.option(
    "--source-dir",
    "-d",
    type=click.Path(),
    help="Directory containing replay files to query from.",
)
def tag_frequency(source_list, source_dir):
    """
    Print the frequency of occurrence of tags.
    """
    tag_frequencies = cerebrate.tag_frequency(source_list, source_dir)
    for tag, frequency in tag_frequencies:
        click.echo(tag + " " + str(frequency))


cli.add_command(add_tag)
cli.add_command(remove_tag)
cli.add_command(query_replays)
cli.add_command(tag_frequency)

if __name__ == "__main__":
    cli()
