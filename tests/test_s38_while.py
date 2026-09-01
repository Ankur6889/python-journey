from drills.s38_while import backoff_steps, first_bad


# --- backoff_steps -------------------------------------------------------

def test_backoff_example():
    assert backoff_steps(8) == 4


def test_backoff_zero_gap():
    assert backoff_steps(0) == 0


def test_backoff_one():
    assert backoff_steps(1) == 1


def test_backoff_two():
    assert backoff_steps(2) == 2


def test_backoff_three():
    assert backoff_steps(3) == 2


def test_backoff_seven():
    assert backoff_steps(7) == 3


def test_backoff_large():
    assert backoff_steps(1000) == 10


def test_backoff_returns_int():
    assert type(backoff_steps(5)) == int


# --- first_bad -----------------------------------------------------------

def test_first_bad_example():
    assert first_bad([[1, 2], [3, -4, 5], [-1]]) == (1, 1)


def test_first_bad_none_when_clean():
    assert first_bad([[1, 2], [3, 4]]) is None


def test_first_bad_empty_rows():
    assert first_bad([]) is None


def test_first_bad_all_rows_empty():
    assert first_bad([[], [], []]) is None


def test_first_bad_skips_empty_row_first():
    assert first_bad([[], [7, -2]]) == (1, 1)


def test_first_bad_very_first_cell():
    assert first_bad([[-9, 1], [2]]) == (0, 0)


def test_first_bad_takes_the_first_not_the_last():
    assert first_bad([[1, -2, -3], [-4]]) == (0, 1)


def test_first_bad_zero_is_not_negative():
    assert first_bad([[0, 0], [0, -1]]) == (1, 1)


def test_first_bad_minus_one_counts():
    assert first_bad([[5, 5], [5, -1]]) == (1, 1)


def test_first_bad_returns_tuple():
    assert type(first_bad([[-1]])) == tuple


def test_first_bad_single_row_single_col():
    assert first_bad([[-7]]) == (0, 0)


def test_first_bad_last_cell_of_last_row():
    assert first_bad([[1, 2], [3, 4, -5]]) == (1, 2)
