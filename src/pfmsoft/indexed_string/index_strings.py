"""Some utility functions for IndexedStrings."""

from collections.abc import Callable, Iterable, Iterator
from pathlib import Path
from uuid import NAMESPACE_DNS, UUID, uuid5

from pfmsoft.indexed_string.model import (
    IndexedString,
    IndexedStringProtocol,
    IndexedStringTD,
)


def index_strings(
    strings: Iterable[str],
    string_filter: Callable[[IndexedStringProtocol], bool] | None = None,
    index_start: int = 0,
) -> Iterator[IndexedString]:
    """Enumerate and filter a string iterable, yields an `IndexedString`.

    Args:
        strings: An iterable of strings.
        string_filter: Used to filter strings.
        index_start: Defaults to 0.

    Yields:
        The matched indexed strings.
    """
    for idx, txt in enumerate(strings, start=index_start):
        indexed_string = IndexedString(idx=idx, txt=txt)
        if string_filter is not None:
            if string_filter(indexed_string):
                yield indexed_string
        yield indexed_string


def index_lines_in_file(
    file_path: Path,
    string_filter: Callable[[IndexedStringProtocol], bool] | None = None,
    index_start: int = 1,
) -> Iterator[IndexedString]:
    """Enumerate and filter a text file, yields an `IndexedString`.

    Args:
        file_path: Path to a text file.
        string_filter: Used to filter strings.
        index_start: Defaults to 1.

    Yields:
        The matched indexed strings.
    """
    with open(file_path, encoding="utf-8") as file:
        for idx, line in enumerate(file, start=index_start):
            indexed_string = IndexedString(idx=idx, txt=line)
            if string_filter is not None:
                if string_filter(indexed_string):
                    yield indexed_string
            yield indexed_string


def make_uuid(
    indexed_string: IndexedStringProtocol, namespace: UUID = NAMESPACE_DNS
) -> UUID:
    """Make a uuid from one IndexedString."""
    string_value = f"{indexed_string.idx}: {indexed_string.txt}"
    return uuid5(namespace=namespace, name=string_value)


def make_uuid_iter(
    indexed_strings: Iterable[IndexedStringProtocol], namespace: UUID = NAMESPACE_DNS
) -> UUID:
    """Make a uuid from an iterable of IndexedStrings."""
    string_value = "".join(f"{x.idx}: {x.txt}" for x in indexed_strings)
    return uuid5(namespace=namespace, name=string_value)


def make_uuid_dict(
    indexed_string_td: IndexedStringTD, namespace: UUID = NAMESPACE_DNS
) -> UUID:
    """Make a uuid from one IndexedString."""
    string_value = f"{indexed_string_td['idx']}: {indexed_string_td['txt']}"
    return uuid5(namespace=namespace, name=string_value)


def make_uuid_iter_dict(
    indexed_string_tds: Iterable[IndexedStringTD], namespace: UUID = NAMESPACE_DNS
) -> UUID:
    """Make a uuid from an iterable of IndexedStrings."""
    string_value = "".join(f"{x['idx']}: {x['txt']}" for x in indexed_string_tds)
    return uuid5(namespace=namespace, name=string_value)
