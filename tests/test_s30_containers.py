"""S30 containers acceptance tests — written by the mentor, not the student."""

from drills.s30_containers import (
    limits_for,
    shared_joints,
    pop_limit,
    snapshot,
    span,
    total,
)

LIMITS = {"shoulder": (-90, 90), "elbow": (0, 145)}


# 1) limits_for
def test_limits_for_present():
    assert limits_for(LIMITS, "elbow") == (0, 145)


def test_limits_for_absent_shrugs():
    assert limits_for(LIMITS, "wrist") == (0, 0)


def test_limits_for_does_not_add_the_missing_key():
    limits = {"shoulder": (-90, 90)}
    limits_for(limits, "wrist")
    assert limits == {"shoulder": (-90, 90)}


def test_limits_for_returns_a_tuple():
    assert isinstance(limits_for(LIMITS, "shoulder"), tuple)


# 2) shared_joints
def test_shared_joints_intersection():
    assert shared_joints(
        ["shoulder", "elbow", "wrist"], ["elbow", "wrist", "gripper"]
    ) == {"elbow", "wrist"}


def test_shared_joints_dedupes():
    assert shared_joints(["shoulder", "shoulder"], ["shoulder"]) == {"shoulder"}


def test_shared_joints_nothing_in_common():
    assert shared_joints(["shoulder"], ["elbow"]) == set()


def test_shared_joints_returns_a_set():
    assert isinstance(shared_joints(["a"], ["a"]), set)


# 3) pop_limit
def test_pop_limit_returns_the_value_and_removes_it():
    d = {"shoulder": 90, "elbow": 45}
    assert pop_limit(d, "elbow") == 45
    assert d == {"shoulder": 90}


def test_pop_limit_absent_shrugs_and_leaves_the_dict_alone():
    d = {"shoulder": 90}
    assert pop_limit(d, "wrist") is None
    assert d == {"shoulder": 90}


# 4) snapshot
def test_snapshot_same_contents():
    assert snapshot([10, 20, 30]) == [10, 20, 30]


def test_snapshot_is_a_different_object():
    a = [10, 20, 30]
    assert snapshot(a) is not a


def test_snapshot_is_independent():
    a = [10, 20, 30]
    b = snapshot(a)
    b.append(99)
    assert a == [10, 20, 30]
    assert b == [10, 20, 30, 99]


def test_snapshot_empty():
    assert snapshot([]) == []


# 5) span
def test_span_positive():
    assert span(0, 145) == (0, 145, 145)


def test_span_crossing_zero():
    assert span(-90, 90) == (-90, 90, 180)


def test_span_returns_one_tuple():
    result = span(0, 145)
    assert isinstance(result, tuple)
    assert len(result) == 3


# 6) total
def test_total_sums():
    assert total([10, 20, 30]) == 60


def test_total_empty_is_zero():
    assert total([]) == 0
