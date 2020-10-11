from typing import Iterable


def flatten(iterable_to_flatten: Iterable[Iterable]):
    return [item for sublist in iterable_to_flatten for item in sublist]
