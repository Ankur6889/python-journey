from drills.s25_closure import make_clamp, clamp_all


def test_clamps_above_limit():
    shoulder = make_clamp(90)
    assert shoulder(120) == 90


def test_clamps_below_negative_limit():
    shoulder = make_clamp(90)
    assert shoulder(-120) == -90


def test_leaves_inside_value_alone():
    shoulder = make_clamp(90)
    assert shoulder(45) == 45


def test_boundary_value_is_unchanged():
    shoulder = make_clamp(90)
    assert shoulder(90) == 90
    assert shoulder(-90) == -90


def test_two_clamps_do_not_interfere():
    shoulder = make_clamp(90)
    wrist = make_clamp(15)
    assert wrist(120) == 15
    assert shoulder(120) == 90
    assert wrist(-120) == -15


def test_tool_takes_exactly_one_argument():
    shoulder = make_clamp(90)
    assert shoulder(0) == 0


def test_tool_survives_and_stays_correct_after_many_calls():
    shoulder = make_clamp(90)
    for _ in range(10000):
        shoulder(120)
    assert shoulder(120) == 90


def test_clamp_all_returns_new_list_with_clamped_values():
    angles = [120, -120, 45]
    assert clamp_all(angles, 90) == [90, -90, 45]


def test_clamp_all_does_not_touch_the_callers_list():
    angles = [120, -120, 45]
    clamp_all(angles, 90)
    assert angles == [120, -120, 45]


def test_clamp_all_on_empty_list():
    assert clamp_all([], 90) == []
