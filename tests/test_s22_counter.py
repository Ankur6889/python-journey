from drills.s22_counter import tick, reset


def test_first_tick():
    reset()
    assert tick() == 1


def test_ticks_increment():
    reset()
    tick()
    assert tick() == 2
    assert tick() == 3


def test_reset_starts_over():
    reset()
    tick()
    tick()
    reset()
    assert tick() == 1
