"""Tests for indexed string uuids."""

from pfmsoft.indexed_string.index_strings import (
    make_uuid,
    make_uuid_dict,
    make_uuid_iter,
    make_uuid_iter_dict,
)
from pfmsoft.indexed_string.model import (
    IndexedString,
    IndexedStringTD,
)


def test_indexed_string():
    """Check that the typed dict and class uuids match for the same data."""
    indexed_string = IndexedString(idx=5, txt="Five")
    indexed_string_TD = IndexedStringTD(idx=5, txt="Five")
    indexed_string_uuid = make_uuid(indexed_string=indexed_string)
    indexed_string_td_uuid = make_uuid_dict(indexed_string_td=indexed_string_TD)
    assert indexed_string_uuid == indexed_string_td_uuid
    different_indexed_string = IndexedString(idx=1, txt="one")
    assert indexed_string_uuid != make_uuid(indexed_string=different_indexed_string)


def test_indexed_string_iter():
    """Check that iterables generate expected uuids."""
    indexed_string = IndexedString(idx=5, txt="Five")
    indexed_string_TD = IndexedStringTD(idx=5, txt="Five")
    indexed_string_uuid = make_uuid(indexed_string=indexed_string)
    indexed_string_td_uuid = make_uuid_dict(indexed_string_td=indexed_string_TD)

    # check that uuids made from a list match,
    # and the single item lists match individual items.
    indexed_strings = [IndexedString(idx=5, txt="Five")]
    indexed_string_TDs = [IndexedStringTD(idx=5, txt="Five")]
    indexed_strings_uuid = make_uuid_iter(indexed_strings=indexed_strings)
    indexed_strings_td_uuid = make_uuid_iter_dict(indexed_string_tds=indexed_string_TDs)
    assert indexed_strings_uuid == indexed_strings_td_uuid
    assert indexed_string_uuid == indexed_strings_uuid
    assert indexed_string_td_uuid == indexed_strings_td_uuid

    # check that lists uuid match.
    indexed_strings = [
        IndexedString(idx=5, txt="Five"),
        IndexedString(idx=1, txt="one"),
    ]
    indexed_string_TDs = [
        IndexedStringTD(idx=5, txt="Five"),
        IndexedStringTD(idx=1, txt="one"),
    ]
    indexed_strings_uuid = make_uuid_iter(indexed_strings=indexed_strings)
    indexed_strings_td_uuid = make_uuid_iter_dict(indexed_string_tds=indexed_string_TDs)
    assert indexed_strings_uuid == indexed_strings_td_uuid
    assert indexed_strings_uuid != indexed_string_uuid
