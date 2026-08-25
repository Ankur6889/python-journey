"""S31 raise-vs-shrug acceptance tests — written by the mentor, not the student."""

import pytest

from drills.s31_shrug import (
    limit_for,
    must_limit,
    drop_limit,
    must_drop,
    retire,
    must_retire,
)

LIMITS = {"shoulder": (-90, 90), "elbow": (0, 145)}


def fresh():
    return {"shoulder": (-90, 90), "elbow": (0, 145)}


# --- PAIR 1 -------------------------------------------------------------

def test_limit_for_present():
    assert limit_for(LIMITS, "elbow") == (0, 145)


def test_limit_for_absent_shrugs():
    assert limit_for(LIMITS, "gripper") == (-180, 180)


def test_limit_for_does_not_add_the_missing_key():
    d = fresh()
    limit_for(d, "gripper")
    assert d == fresh()


def test_must_limit_present():
    assert must_limit(LIMITS, "shoulder") == (-90, 90)


def test_must_limit_absent_raises():
    with pytest.raises(KeyError):
        must_limit(LIMITS, "gripper")


# --- PAIR 2 -------------------------------------------------------------

def test_drop_limit_present_returns_the_value():
    d = fresh()
    assert drop_limit(d, "elbow") == (0, 145)


def test_drop_limit_present_actually_removes_it():
    d = fresh()
    drop_limit(d, "elbow")
    assert d == {"shoulder": (-90, 90)}


def test_drop_limit_absent_shrugs():
    d = fresh()
    assert drop_limit(d, "gripper") is None


def test_drop_limit_absent_leaves_the_dict_alone():
    d = fresh()
    drop_limit(d, "gripper")
    assert d == fresh()


def test_must_drop_present_returns_the_value():
    d = fresh()
    assert must_drop(d, "shoulder") == (-90, 90)
    assert d == {"elbow": (0, 145)}


def test_must_drop_absent_raises():
    d = fresh()
    with pytest.raises(KeyError):
        must_drop(d, "gripper")


# --- PAIR 3 -------------------------------------------------------------

def test_retire_present():
    assert retire({"shoulder", "elbow"}, "elbow") == {"shoulder"}


def test_retire_absent_shrugs():
    assert retire({"shoulder", "elbow"}, "gripper") == {"shoulder", "elbow"}


def test_retire_changes_the_set_it_was_given():
    s = {"shoulder", "elbow"}
    out = retire(s, "elbow")
    assert out is s


def test_must_retire_present():
    assert must_retire({"shoulder", "elbow"}, "elbow") == {"shoulder"}


def test_must_retire_absent_raises():
    with pytest.raises(KeyError):
        must_retire({"shoulder", "elbow"}, "gripper")


# --- THE CONSTRAINT IS PART OF THE ACCEPTANCE ---------------------------

def test_no_hand_rolled_guards():
    import re
    from pathlib import Path

    src = Path(__file__).resolve().parents[1] / "drills" / "s31_shrug.py"
    body = src.read_text().split('"""')[2]
    banned = [w for w in ("if", "in", "else", "try") if re.search(rf"\b{w}\b", body)]
    assert banned == [], f"banned keyword(s) used below the docstring: {banned}"
