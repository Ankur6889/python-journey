from drills.s23_sort_key import make_distance_key, order_by_distance


def test_orders_by_distance_from_five():
    assert order_by_distance([10, 4, 7], 5) == [4, 7, 10]


def test_orders_by_distance_from_nine():
    assert order_by_distance([10, 4, 7], 9) == [10, 7, 4]


def test_original_list_is_not_reordered():
    values = [10, 4, 7]
    order_by_distance(values, 5)
    assert values == [10, 4, 7]


def test_key_takes_exactly_one_argument():
    key = make_distance_key(5)
    assert key(7) == 2
    assert key(5) == 0
    assert key(1) == 4


def test_two_keys_do_not_interfere():
    key_five = make_distance_key(5)
    key_nine = make_distance_key(9)
    assert key_five(10) == 5
    assert key_nine(10) == 1
    assert key_five(10) == 5


def test_key_works_when_handed_to_sorted():
    key = make_distance_key(9)
    assert sorted([10, 4, 7], key=key) == [10, 7, 4]
