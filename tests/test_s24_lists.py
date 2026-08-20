from drills.s24_lists import ordered_copy, order_in_place, take_last, last_three


def test_ordered_copy_returns_sorted():
    assert ordered_copy([3, 1, 2]) == [1, 2, 3]


def test_ordered_copy_leaves_caller_list_alone():
    original = [3, 1, 2]
    ordered_copy(original)
    assert original == [3, 1, 2]


def test_order_in_place_mutates_caller_list():
    original = [3, 1, 2]
    order_in_place(original)
    assert original == [1, 2, 3]


def test_order_in_place_evaluates_to_nothing_usable():
    assert order_in_place([3, 1, 2]) is None


def test_take_last_returns_removed_value():
    assert take_last([7, 8, 9]) == 9


def test_take_last_shortens_caller_list():
    original = [7, 8, 9]
    take_last(original)
    assert original == [7, 8]


def test_last_three_typical():
    assert last_three([1, 2, 3, 4, 5]) == [3, 4, 5]


def test_last_three_exactly_three():
    assert last_three([1, 2, 3]) == [1, 2, 3]


def test_last_three_shorter_than_three():
    assert last_three([1]) == [1]


def test_last_three_empty():
    assert last_three([]) == []


def test_last_three_leaves_caller_list_alone():
    original = [1, 2, 3, 4, 5]
    last_three(original)
    assert original == [1, 2, 3, 4, 5]
