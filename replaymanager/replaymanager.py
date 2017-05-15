import hashlib
import functools
import os
import shutil

import tinydb

REPLAY_ARCHIVE_SUBDIRECTORY_NAME = "replay_archive"
DB_FILE_NAME = "replays.json"


def _add_tags(tags: list):
    def transform(element):
        element['tags'] = list(set(element['tags'] + tags))

    return transform


def _remove_tags(tags: list):
    def transform(element):
        element['tags'] = list(set(element['tags']) - set(tags))

    return transform


def _match_all_tags(tags: list):
    def match(replay_tags):
        return bool(all(tag in replay_tags for tag in tags))

    return match


def _match_any_tags(tags: list):
    def match(replay_tags):
        return bool(any(tag in replay_tags for tag in tags))

    return match


def _hash_replay(replay_path):
    with open(replay_path, "rb") as replay_file:
        hash_calculator = hashlib.sha256()

        for buf in iter(functools.partial(replay_file.read, 4096), b''):
            hash_calculator.update(buf)

        replay_hash = hash_calculator.hexdigest()
    return replay_hash


class ReplayManager:
    def __init__(self, app_data_path: str):
        if not os.path.exists(app_data_path):
            os.makedirs(app_data_path)

        replay_archive_path = os.path.join(app_data_path, REPLAY_ARCHIVE_SUBDIRECTORY_NAME)
        if not os.path.exists(replay_archive_path):
            os.makedirs(replay_archive_path)

        db_path = os.path.join(app_data_path, DB_FILE_NAME)
        if not os.path.exists(db_path):
            open(db_path, 'a').close()

        self.__db = tinydb.TinyDB(db_path)
        self.__replay_archive_path = replay_archive_path

    def tag_replay(self, replay_path: str, tags: list):
        replay_hash = _hash_replay(replay_path)

        replay = tinydb.Query()
        replay_updated = self.__db.update(_add_tags(tags), replay['hash'] == replay_hash)
        if not replay_updated:
            replay_canonical_path = os.path.join(self.__replay_archive_path, replay_hash + ".SC2Replay")
            shutil.copyfile(replay_path, replay_canonical_path)
            self.__db.insert({'hash': replay_hash, 'canonical_path': replay_canonical_path, 'tags': tags})

    def untag_replay(self, replay_path: str, tags: list):
        replay_hash = _hash_replay(replay_path)

        replay = tinydb.Query()
        self.__db.update(_remove_tags(tags), replay['hash'] == replay_hash)

    def query_replays(self, match_any_tag: bool, inverse: bool, replays_to_query_from: list, tags: list) -> list:

        replay_hashes = map(_hash_replay, replays_to_query_from)

        replay = tinydb.Query()

        query = replay['tags'].any(tags) if match_any_tag else replay['tags'].all(tags)
        query = ~query if inverse else query
        query = query | replay['hash'].test(lambda x: x in replay_hashes) if replay_hashes else query

        matches = self.__db.search(query)

        return [match['canonical_path'] for match in matches]

