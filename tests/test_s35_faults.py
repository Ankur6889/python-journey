import inspect

import pytest

from drills.s35_faults import (
    check_angle,
    measure,
    safe_angles,
    total_valid,
)


# ---------------------------------------------------------------- total_valid

def test_total_valid_worked_example():
    assert total_valid(["45", "90", "n/a", "30"]) == 165


def test_total_valid_all_good():
    assert total_valid(["12", "8"]) == 20


def test_total_valid_empty_list():
    assert total_valid([]) == 0


def test_total_valid_single_item():
    assert total_valid(["7"]) == 7


def test_total_valid_all_bad():
    assert total_valid(["n/a", "junk", ""]) == 0


def test_total_valid_negative_numbers_are_whole_numbers():
    assert total_valid(["-5", "10"]) == 5


def test_total_valid_decimal_string_is_not_a_whole_number():
    assert total_valid(["3.5", "2"]) == 2


def test_total_valid_does_not_mutate_input():
    readings = ["45", "n/a", "30"]
    total_valid(readings)
    assert readings == ["45", "n/a", "30"]


# ---------------------------------------------------------------- check_angle

def test_check_angle_allowed_returns_unchanged():
    assert check_angle(90, 180) == 90


def test_check_angle_zero_is_allowed():
    assert check_angle(0, 180) == 0


def test_check_angle_exactly_on_the_limit_is_allowed():
    assert check_angle(180, 180) == 180


def test_check_angle_above_limit_raises_valueerror():
    with pytest.raises(ValueError):
        check_angle(200, 180)


def test_check_angle_one_over_the_limit_raises():
    with pytest.raises(ValueError):
        check_angle(181, 180)


def test_check_angle_message_names_both_numbers_in_order():
    with pytest.raises(ValueError) as excinfo:
        check_angle(200, 180)
    message = str(excinfo.value)
    assert "200" in message
    assert "180" in message
    assert message.index("200") < message.index("180")


# ---------------------------------------------------------------- safe_angles

def test_safe_angles_worked_example():
    assert safe_angles([45, 90, 200, 30], 180) == [45, 90, 30]


def test_safe_angles_empty_list():
    assert safe_angles([], 180) == []


def test_safe_angles_single_allowed():
    assert safe_angles([45], 180) == [45]


def test_safe_angles_single_rejected():
    assert safe_angles([500], 180) == []


def test_safe_angles_boundary_value_is_kept():
    assert safe_angles([180, 181], 180) == [180]


def test_safe_angles_all_rejected():
    assert safe_angles([200, 300], 180) == []


def test_safe_angles_does_not_mutate_input():
    readings = [45, 90, 200, 30]
    safe_angles(readings, 180)
    assert readings == [45, 90, 200, 30]


def test_safe_angles_returns_a_new_list():
    readings = [45, 90]
    assert safe_angles(readings, 180) is not readings


def test_safe_angles_holds_no_second_copy_of_the_rule():
    source = inspect.getsource(safe_angles)
    body = source.split('"""')[-1]
    assert "check_angle" in body, "safe_angles must decide by calling check_angle"
    assert ">" not in body, "safe_angles must not compare an angle to the limit itself"
    assert "<" not in body, "safe_angles must not compare an angle to the limit itself"


# -------------------------------------------------------------------- measure

def test_measure_good_value_returned():
    log = []
    assert measure("45", log) == 45


def test_measure_good_value_logs_closed_once():
    log = []
    measure("45", log)
    assert log == ["closed"]


def test_measure_zero():
    log = []
    assert measure("0", log) == 0
    assert log == ["closed"]


def test_measure_bad_value_still_reaches_the_caller():
    log = []
    with pytest.raises(ValueError):
        measure("n/a", log)


def test_measure_bad_value_logs_closed_once():
    log = []
    try:
        measure("n/a", log)
    except ValueError:
        pass
    assert log == ["closed"]


def test_measure_appends_to_an_existing_log():
    log = ["opened"]
    measure("12", log)
    assert log == ["opened", "closed"]
