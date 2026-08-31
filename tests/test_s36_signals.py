import inspect

import pytest

from drills.s36_signals import (
    OverLimit,
    audited,
    check_limit,
    read_limit,
    sort_faults,
)


# ------------------------------------------------------------------ OverLimit

def test_overlimit_is_an_exception():
    assert issubclass(OverLimit, Exception)


def test_overlimit_can_be_raised_and_caught_by_name():
    with pytest.raises(OverLimit):
        raise OverLimit("angle 200 exceeds limit 180")


def test_overlimit_is_caught_by_the_general_family():
    try:
        raise OverLimit("angle 200 exceeds limit 180")
    except Exception as e:
        assert isinstance(e, OverLimit)
    else:
        pytest.fail("OverLimit was not caught by `except Exception`")


def test_overlimit_is_separable_from_a_bad_value():
    # a caller reacting to text-that-is-not-a-number must NOT also catch this
    assert not issubclass(OverLimit, ValueError)


# ----------------------------------------------------------------- check_limit

def test_check_limit_worked_example():
    assert check_limit(90, 180) == 90


def test_check_limit_on_the_boundary_is_allowed():
    assert check_limit(180, 180) == 180


def test_check_limit_just_over_the_boundary():
    with pytest.raises(OverLimit):
        check_limit(181, 180)


def test_check_limit_raises_overlimit_not_something_else():
    with pytest.raises(OverLimit):
        check_limit(200, 180)


def test_check_limit_message_carries_both_numbers_in_order():
    with pytest.raises(OverLimit) as excinfo:
        check_limit(200, 180)
    msg = str(excinfo.value)
    assert "200" in msg, f"angle missing from message: {msg!r}"
    assert "180" in msg, f"limit missing from message: {msg!r}"
    assert msg.index("200") < msg.index("180"), f"wrong order: {msg!r}"


def test_check_limit_prints_nothing(capsys):
    check_limit(90, 180)
    with pytest.raises(OverLimit):
        check_limit(200, 180)
    assert capsys.readouterr().out == ""


# ------------------------------------------------------------------ read_limit

def test_read_limit_worked_example():
    assert read_limit({"elbow": 150, "wrist": 90}, "elbow") == 150


def test_read_limit_other_key():
    assert read_limit({"elbow": 150, "wrist": 90}, "wrist") == 90


def test_read_limit_missing_joint_does_not_hand_back_a_value():
    with pytest.raises(Exception) as excinfo:
        read_limit({"elbow": 150, "wrist": 90}, "elbw")
    assert "elbw" in str(excinfo.value), (
        "the report does not name the joint that was asked for"
    )


def test_read_limit_prints_nothing(capsys):
    read_limit({"elbow": 150}, "elbow")
    with pytest.raises(Exception):
        read_limit({"elbow": 150}, "elbw")
    assert capsys.readouterr().out == ""


# ------------------------------------------------------------------ sort_faults

def test_sort_faults_worked_example():
    assert sort_faults(["45", "200", "n/a", "90"], 180) == {
        "ok": [45, 90],
        "over": [200],
        "broken": ["n/a"],
    }


def test_sort_faults_empty_list():
    assert sort_faults([], 180) == {"ok": [], "over": [], "broken": []}


def test_sort_faults_one_of_each():
    assert sort_faults(["10", "999", "--"], 180) == {
        "ok": [10],
        "over": [999],
        "broken": ["--"],
    }


def test_sort_faults_boundary_reading_is_ok_not_over():
    assert sort_faults(["180"], 180) == {"ok": [180], "over": [], "broken": []}


def test_sort_faults_just_over_the_boundary():
    assert sort_faults(["181"], 180) == {"ok": [], "over": [181], "broken": []}


def test_sort_faults_all_broken():
    assert sort_faults(["n/a", "", "12.5"], 180) == {
        "ok": [],
        "over": [],
        "broken": ["n/a", "", "12.5"],
    }


def test_sort_faults_keeps_order():
    assert sort_faults(["200", "45", "201", "46"], 180)["over"] == [200, 201]


def test_sort_faults_does_not_mutate_its_input():
    readings = ["45", "200", "n/a"]
    before = list(readings)
    sort_faults(readings, 180)
    assert readings == before


def test_sort_faults_returns_exactly_three_keys():
    assert set(sort_faults(["45"], 180)) == {"ok", "over", "broken"}


def test_sort_faults_holds_no_second_copy_of_the_limit_rule():
    src = inspect.getsource(sort_faults)
    assert "check_limit" in src, (
        "sort_faults must decide 'allowed' by calling check_limit"
    )


def test_sort_faults_prints_nothing(capsys):
    sort_faults(["45", "200", "n/a"], 180)
    assert capsys.readouterr().out == ""


# --------------------------------------------------------------------- audited

def test_audited_all_allowed_returns_them_all():
    log = []
    assert audited([45, 90], 180, log) == [45, 90]


def test_audited_all_allowed_leaves_the_log_untouched():
    log = []
    audited([45, 90], 180, log)
    assert log == []


def test_audited_empty_readings():
    log = []
    assert audited([], 180, log) == []
    assert log == []


def test_audited_boundary_is_allowed():
    log = []
    assert audited([180], 180, log) == [180]
    assert log == []


def test_audited_lets_the_fault_reach_the_caller():
    log = []
    with pytest.raises(OverLimit):
        audited([45, 200, 90], 180, log)


def test_audited_records_over_exactly_once():
    log = []
    with pytest.raises(OverLimit):
        audited([45, 200, 300], 180, log)
    assert log == ["OVER"]


def test_audited_fault_carries_the_original_message():
    log = []
    with pytest.raises(OverLimit) as excinfo:
        audited([45, 200], 180, log)
    msg = str(excinfo.value)
    assert "200" in msg and "180" in msg, (
        f"the caller was handed a different report than check_limit made: {msg!r}"
    )


def test_audited_fault_still_points_at_check_limit():
    log = []
    with pytest.raises(OverLimit) as excinfo:
        audited([200], 180, log)
    frames = [tb.name for tb in excinfo.traceback]
    assert "check_limit" in frames, (
        "the traceback no longer points at where the fault actually happened; "
        f"frames were {frames}"
    )


def test_audited_does_not_mutate_its_readings():
    readings = [45, 90]
    before = list(readings)
    audited(readings, 180, [])
    assert readings == before


def test_audited_prints_nothing(capsys):
    log = []
    audited([45], 180, log)
    with pytest.raises(OverLimit):
        audited([200], 180, log)
    assert capsys.readouterr().out == ""
