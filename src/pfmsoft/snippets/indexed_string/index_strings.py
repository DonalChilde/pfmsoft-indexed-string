from pathlib import Path
from typing import Callable, Iterable, Iterator

from pfmsoft.snippets.indexed_string.model import IndexedString, IndexedStringProtocol


def index_strings(
    strings: Iterable[str],
    string_filter: Callable[[IndexedStringProtocol], bool] | None = None,
    index_start: int = 0,
) -> Iterator[IndexedString]:
    """
    Enumerate and filter a string iterable, yields an `IndexedString`

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
    """
    Enumerate and filter a text file, yields an `IndexedString`

    Args:
        file_path: Path to a text file.
        string_filter: Used to filter strings.
        index_start: Defaults to 1.

    Yields:
        The matched indexed strings.
    """

    with open(file_path, mode="rt", encoding="utf-8") as file:
        for idx, line in enumerate(file, start=index_start):
            indexed_string = IndexedString(idx=idx, txt=line)
            if string_filter is not None:
                if string_filter(indexed_string):
                    yield indexed_string
            yield indexed_string
