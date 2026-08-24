"""S30 acceptance tests — written by the mentor, not the student."""

from drills.s30_comprehensions import over_limit, scaled, names_over, format_row


# 1) over_limit
def test_over_limit_picks_only_above():
    assert over_limit([10, 45, 90, 45, 5], 45) == [90]


def test_over_limit_none_qualify():
    assert over_limit([1, 2, 3], 10) == []


def test_over_limit_negatives():
    assert over_limit([-30, 0, 30], -30) == [0, 30]


def test_over_limit_preserves_order():
    assert over_limit([100, 20, 99, 1, 50], 40) == [100, 99, 50]


def test_over_limit_returns_a_new_list():
    original = [10, 20, 30]
    result = over_limit(original, 5)
    assert result == [10, 20, 30]
    assert result is not original


# 2) scaled
def test_scaled_multiplies_every_value():
    assert scaled({"shoulder": 90, "elbow": 45}, 2) == {"shoulder": 180, "elbow": 90}


def test_scaled_empty():
    assert scaled({}, 5) == {}


def test_scaled_keeps_keys_and_order():
    out = scaled({"a": 1, "b": 2, "c": 3}, 10)
    assert list(out.keys()) == ["a", "b", "c"]
    assert out == {"a": 10, "b": 20, "c": 30}


def test_scaled_does_not_mutate_input():
    limits = {"shoulder": 90}
    out = scaled(limits, 3)
    assert limits == {"shoulder": 90}
    assert out is not limits


# 3) names_over
def test_names_over_picks_names():
    assert names_over({"shoulder": 90, "elbow": 45, "wrist": 120}, 45) == ["shoulder", "wrist"]


def test_names_over_none_qualify():
    assert names_over({"shoulder": 90, "elbow": 45}, 200) == []


def test_names_over_keeps_dict_order():
    limits = {"z": 100, "a": 100, "m": 100}
    assert names_over(limits, 0) == ["z", "a", "m"]


# 4) format_row
def test_format_row_pads_name_and_value():
    assert format_row("shoulder", 12.5) == "shoulder     12.50"


def test_format_row_short_name():
    assert format_row("elbow", 4.0) == "elbow         4.00"


def test_format_row_name_longer_than_the_column():
    assert format_row("wrist_rotation", 100.456) == "wrist_rotation  100.46"


def test_format_row_columns_line_up():
    rows = [format_row("shoulder", 12.5), format_row("elbow", 4.0)]
    assert len(rows[0]) == len(rows[1]) == 18
