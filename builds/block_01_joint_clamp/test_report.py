"""Block 01 — the tests report() never had. Written by the mentor."""

from clamp import clamp_joints, report

LIMITS = {"shoulder": (-90, 90), "elbow": (0, 145), "wrist": (-180, 180)}


def test_report_returns_the_clamped_values_not_an_empty_dict():
    assert report(-200, 300, 0, **LIMITS) == {
        "shoulder": -90,
        "elbow": 145,
        "wrist": 0,
    }


def test_report_agrees_with_clamp_joints():
    angles = (-200, 300, 0)
    assert report(*angles, **LIMITS) == clamp_joints(*angles, **LIMITS)


def test_report_agrees_when_nothing_needs_clamping():
    angles = (0, 10, 20)
    assert report(*angles, **LIMITS) == clamp_joints(*angles, **LIMITS)


def test_report_BOUNDARY_exactly_on_a_limit():
    assert report(-90, 145, 180, **LIMITS) == {
        "shoulder": -90,
        "elbow": 145,
        "wrist": 180,
    }


def test_report_KHAALI_no_joints_at_all():
    assert report() == {}


def test_report_still_prints_one_line_per_joint(capsys):
    report(-200, 300, 0, **LIMITS)
    printed = capsys.readouterr().out
    assert "shoulder" in printed
    assert "elbow" in printed
    assert "wrist" in printed
    assert "CLAMPED" in printed
    assert "ok" in printed
