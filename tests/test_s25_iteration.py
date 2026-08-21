import re

from drills.s25_iteration import first_two, drop_first

SOURCE = open("drills/s25_iteration.py").read().split('"""')[2]

BANNED = [r"\bfor\b", r"\bwhile\b", r"\.pop\(", r"\.remove\(",
          r"\.index\(", r"\benumerate\b", r"\[\s*[-\d:]"]


def test_no_banned_construct_is_used():
    used = [p for p in BANNED if re.search(p, SOURCE)]
    assert used == [], f"banned construct(s) used: {used}"


def test_first_two():
    assert first_two([10, 20, 30, 40]) == [10, 20]


def test_first_two_on_exactly_two():
    assert first_two([1, 2]) == [1, 2]


def test_first_two_leaves_caller_list_alone():
    items = [10, 20, 30, 40]
    first_two(items)
    assert items == [10, 20, 30, 40]


def test_drop_first():
    assert drop_first([10, 20, 30, 40]) == [20, 30, 40]


def test_drop_first_on_exactly_two():
    assert drop_first([1, 2]) == [2]


def test_drop_first_leaves_caller_list_alone():
    items = [10, 20, 30, 40]
    drop_first(items)
    assert items == [10, 20, 30, 40]
