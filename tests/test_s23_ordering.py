from drills.s23_ordering import sort_by_last_digit, sort_by_length


def test_orders_by_last_digit():
    assert sort_by_last_digit([21, 45, 13]) == [21, 13, 45]


def test_orders_by_last_digit_ignores_leading_digits():
    assert sort_by_last_digit([109, 32, 47]) == [32, 47, 109]


def test_orders_by_length():
    assert sort_by_length(["bbb", "a", "cc"]) == ["a", "cc", "bbb"]


def test_neither_function_mutates_its_input():
    numbers = [21, 45, 13]
    words = ["bbb", "a", "cc"]
    sort_by_last_digit(numbers)
    sort_by_length(words)
    assert numbers == [21, 45, 13]
    assert words == ["bbb", "a", "cc"]


def test_empty_inputs():
    assert sort_by_last_digit([]) == []
    assert sort_by_length([]) == []


def test_documentation_is_readable_at_runtime():
    for func in (sort_by_last_digit, sort_by_length):
        assert func.__doc__ is not None
        assert func.__doc__.strip() != ""
