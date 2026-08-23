"""Acceptance tests for build block 01. WRITTEN BY THE MENTOR — do not edit.

You have never been taught pytest as a subject, so you are not expected to
write these. Your job is clamp.py. This file decides whether it works.

Run from the repo root:      python3 -m pytest builds/block_01_joint_clamp -q
Run one level only:          python3 -m pytest builds/block_01_joint_clamp -q -k L1
"""

import pytest

from clamp import clamp_one, clamp_all, clamp_joints


# ── L1 ──────────────────────────────────────────────────────────────────

def test_L1_inside_the_limits_is_unchanged():
    assert clamp_one(0, -90, 90) == 0
    assert clamp_one(90, -180, 180) == 90


def test_L1_below_low_becomes_low():
    assert clamp_one(-10, 0, 145) == 0
    assert clamp_one(-400, -180, 180) == -180


def test_L1_above_high_becomes_high():
    assert clamp_one(120, -90, 90) == 90
    assert clamp_one(200, 0, 145) == 145


def test_L1_BOUNDARY_exactly_on_a_limit_is_unchanged():
    assert clamp_one(-90, -90, 90) == -90
    assert clamp_one(145, 0, 145) == 145


# ── L2 ──────────────────────────────────────────────────────────────────

def test_L2_many_angles_one_shared_limit_pair():
    assert clamp_all(-90, 90, 120, -90, 0, 200) == (90, -90, 0, 90)


def test_L2_EK_a_single_angle():
    assert clamp_all(-90, 90, 45) == (45,)


def test_L2_KHAALI_no_angles_at_all():
    assert clamp_all(-90, 90) == ()


def test_L2_order_in_is_order_out():
    assert clamp_all(0, 10, 5, 99, -99) == (5, 10, 0)


# ── L3 ──────────────────────────────────────────────────────────────────

ARM = {"shoulder": (-90, 90), "elbow": (0, 145), "wrist": (-180, 180)}


def test_L3_each_angle_reaches_its_own_joint():
    assert clamp_joints(120, -10, 90, **ARM) == {
        "shoulder": 90,
        "elbow": 0,
        "wrist": 90,
    }


def test_L3_BAHAR_every_joint_out_of_range_at_once():
    assert clamp_joints(0, 200, -400, **ARM) == {
        "shoulder": 0,
        "elbow": 145,
        "wrist": -180,
    }


def test_L3_BOUNDARY_every_joint_sitting_exactly_on_a_limit():
    assert clamp_joints(-90, 145, 180, **ARM) == {
        "shoulder": -90,
        "elbow": 145,
        "wrist": 180,
    }


def test_L3_KHAALI_no_joints_at_all():
    assert clamp_joints() == {}


def test_L3_EK_one_joint_only():
    assert clamp_joints(120, shoulder=(-90, 90)) == {"shoulder": 90}
