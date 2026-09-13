import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "drills"))

from s48_joint import Joint


def test_attributes_are_attached():
    j = Joint("elbow", 10, 90)
    assert j.name == "elbow"
    assert j.angle == 10
    assert j.limit == 90


def test_exactly_three_attributes():
    j = Joint("elbow", 10, 90)
    assert set(vars(j)) == {"name", "angle", "limit"}


def test_two_joints_are_independent():
    a = Joint("elbow", 10, 90)
    b = Joint("wrist", 45, 60)
    a.move(5)
    assert a.angle == 15
    assert b.angle == 45
    assert b.name == "wrist"


def test_move_changes_the_same_object_and_returns_none():
    j = Joint("elbow", 10, 90)
    result = j.move(5)
    assert result is None
    assert j.angle == 15


def test_two_moves_add_up():
    j = Joint("elbow", 10, 90)
    j.move(5)
    j.move(-20)
    assert j.angle == -5


def test_is_safe_inside():
    assert Joint("elbow", 10, 90).is_safe() is True
    assert Joint("elbow", -10, 90).is_safe() is True


def test_is_safe_outside():
    assert Joint("elbow", 91, 90).is_safe() is False
    assert Joint("elbow", -91, 90).is_safe() is False


def test_is_safe_on_the_boundary():
    assert Joint("elbow", 90, 90).is_safe() is True
    assert Joint("elbow", -90, 90).is_safe() is True


def test_is_safe_after_a_move():
    j = Joint("elbow", 80, 90)
    j.move(20)
    assert j.is_safe() is False


def test_describe():
    assert Joint("elbow", 15, 90).describe() == "elbow at 15 deg"
    j = Joint("wrist", 0, 60)
    j.move(-5)
    assert j.describe() == "wrist at -5 deg"
