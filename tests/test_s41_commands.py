import inspect

import pytest

import drills.s41_commands as mod
from drills.s41_commands import BadCommand, LIMITS, check, run, to_angle


# ------------------------------------------------------------------ BadCommand

def test_badcommand_is_an_exception():
    assert issubclass(BadCommand, Exception)


def test_badcommand_can_be_raised_and_caught_by_name():
    with pytest.raises(BadCommand):
        raise BadCommand("no such joint: wrist")


def test_badcommand_is_caught_by_a_caller_reacting_to_a_wrong_value():
    try:
        raise BadCommand("no such joint: wrist")
    except ValueError as e:
        assert isinstance(e, BadCommand)
    else:
        pytest.fail("BadCommand was not caught by `except ValueError`")


def test_badcommand_is_caught_by_the_general_family():
    try:
        raise BadCommand("no such joint: wrist")
    except Exception as e:
        assert isinstance(e, BadCommand)
    else:
        pytest.fail("BadCommand was not caught by `except Exception`")


# -------------------------------------------------------------------- to_angle

def test_to_angle_worked_example():
    assert to_angle("45") == 45


def test_to_angle_zero():
    assert to_angle("0") == 0


def test_to_angle_not_a_number_is_a_bad_command():
    with pytest.raises(BadCommand):
        to_angle("n/a")


def test_to_angle_empty_string_is_a_bad_command():
    with pytest.raises(BadCommand):
        to_angle("")


def test_to_angle_decimal_text_is_a_bad_command():
    with pytest.raises(BadCommand):
        to_angle("12.5")


def test_to_angle_message_carries_the_text_as_it_arrived():
    with pytest.raises(BadCommand) as excinfo:
        to_angle("n/a")
    assert "n/a" in str(excinfo.value)


def test_to_angle_prints_nothing(capsys):
    to_angle("45")
    with pytest.raises(BadCommand):
        to_angle("n/a")
    assert capsys.readouterr().out == ""


# ----------------------------------------------------------------------- check

def test_check_worked_example():
    assert check("shoulder", 45) == 45


def test_check_on_the_upper_boundary_is_allowed():
    assert check("shoulder", 90) == 90


def test_check_just_over_the_upper_boundary():
    with pytest.raises(BadCommand):
        check("shoulder", 91)


def test_check_on_the_lower_boundary_is_allowed():
    assert check("elbow", 0) == 0


def test_check_just_under_the_lower_boundary():
    with pytest.raises(BadCommand):
        check("elbow", -1)


def test_check_uses_the_limit_of_the_named_joint():
    assert check("base", 150) == 150
    with pytest.raises(BadCommand):
        check("elbow", 150)


def test_check_unknown_joint_is_a_bad_command_naming_the_joint():
    with pytest.raises(BadCommand) as excinfo:
        check("wrist", 10)
    assert "wrist" in str(excinfo.value)


def test_check_out_of_range_message_carries_angle_and_limit():
    with pytest.raises(BadCommand) as excinfo:
        check("shoulder", 200)
    msg = str(excinfo.value)
    assert "200" in msg, f"angle missing from message: {msg!r}"
    assert "90" in msg, f"limit missing from message: {msg!r}"


def test_check_text_angle_is_a_type_error_not_a_bad_command():
    with pytest.raises(TypeError):
        check("shoulder", "45")


def test_check_float_angle_is_a_type_error_not_a_bad_command():
    with pytest.raises(TypeError):
        check("shoulder", 45.0)


def test_check_does_not_mutate_limits():
    before = dict(LIMITS)
    check("shoulder", 45)
    with pytest.raises(BadCommand):
        check("wrist", 10)
    assert LIMITS == before


def test_check_prints_nothing(capsys):
    check("shoulder", 45)
    with pytest.raises(BadCommand):
        check("shoulder", 200)
    assert capsys.readouterr().out == ""


# ------------------------------------------------------------------------- run

def test_run_worked_example_return_value():
    log = []
    assert run([("shoulder", "45"), ("elbow", "n/a"), ("base", "200")], log) == 1


def test_run_worked_example_log():
    log = []
    run([("shoulder", "45"), ("elbow", "n/a"), ("base", "200")], log)
    assert log == [
        ("ok", "shoulder", 45),
        ("bad", "elbow", "n/a"),
        ("bad", "base", "200"),
        ("done", 1),
    ]


def test_run_empty():
    log = []
    assert run([], log) == 0
    assert log == [("done", 0)]


def test_run_all_ok():
    log = []
    assert run([("base", "10"), ("elbow", "120")], log) == 2
    assert log == [("ok", "base", 10), ("ok", "elbow", 120), ("done", 2)]


def test_run_unknown_joint_is_bad_not_a_crash():
    log = []
    assert run([("wrist", "10")], log) == 0
    assert log == [("bad", "wrist", "10"), ("done", 0)]


def test_run_appends_to_the_callers_list():
    log = [("earlier", 0)]
    run([("shoulder", "45")], log)
    assert log[0] == ("earlier", 0)
    assert log[-1] == ("done", 1)


def test_run_lets_any_other_report_reach_the_caller():
    log = []
    with pytest.raises(TypeError):
        run([("shoulder", "45"), ("elbow", None)], log)


def test_run_still_writes_done_on_the_way_out():
    log = []
    with pytest.raises(TypeError):
        run([("shoulder", "45"), ("elbow", None), ("base", "10")], log)
    assert log == [("ok", "shoulder", 45), ("done", 1)]


def test_run_decides_nothing_itself():
    src = inspect.getsource(run)
    assert "to_angle" in src, "run must convert with to_angle"
    assert "check" in src, "run must validate with check"
    assert "LIMITS" not in src, "run must not hold its own copy of the limit rule"


def test_run_prints_nothing(capsys):
    log = []
    run([("shoulder", "45"), ("elbow", "n/a")], log)
    assert capsys.readouterr().out == ""


# -------------------------------------------------------------- whole module

def test_no_catch_all_anywhere_in_the_module():
    src = inspect.getsource(mod)
    body = src.split('"""', 2)[-1]  # skip the module docstring
    assert "except:" not in body, "a bare except swallows every report"
    assert "except Exception" not in body, "except Exception swallows every report"
