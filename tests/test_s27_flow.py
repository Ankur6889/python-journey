from drills.s27_flow import first_big, total_positive, find_index, label, todo


# ---- 1. first_big ----------------------------------------------------

def test_first_big_returns_the_first_one_not_the_biggest():
    assert first_big([1, 7, 9, 2], 5) == 7


def test_first_big_boundary_equal_does_not_count():
    assert first_big([5, 5, 5], 5) is None


def test_first_big_boundary_just_over():
    assert first_big([5, 6], 5) == 6


def test_first_big_none_when_nothing_qualifies():
    assert first_big([1, 2, 3], 10) is None


def test_first_big_empty_list():
    assert first_big([], 0) is None


# ---- 2. total_positive -----------------------------------------------

def test_total_positive_mixed_signs():
    assert total_positive([3, -4, 10, -1]) == 13


def test_total_positive_boundary_zero_excluded():
    assert total_positive([0, 0, 4]) == 4


def test_total_positive_all_negative():
    assert total_positive([-1, -2]) == 0


def test_total_positive_empty_list():
    assert total_positive([]) == 0


# ---- 3. find_index ---------------------------------------------------

def test_find_index_found():
    assert find_index([10, 20, 30], 20) == 1


def test_find_index_first_occurrence_only():
    assert find_index([7, 7, 7], 7) == 0


def test_find_index_last_position():
    assert find_index([1, 2, 3], 3) == 2


def test_find_index_missing_returns_none(capsys):
    assert find_index([1, 2, 3], 99) is None


def test_find_index_missing_prints_the_word(capsys):
    find_index([1, 2, 3], 99)
    assert capsys.readouterr().out == "missing\n"


def test_find_index_found_prints_nothing(capsys):
    find_index([1, 2, 3], 2)
    assert capsys.readouterr().out == ""


def test_find_index_empty_list_is_missing(capsys):
    assert find_index([], 1) is None
    assert capsys.readouterr().out == "missing\n"


# ---- 4. label --------------------------------------------------------

def test_label_high():
    assert label(11) == "high"


def test_label_boundary_ten_is_low():
    assert label(10) == "low"


def test_label_low():
    assert label(-3) == "low"


# ---- 5. todo ---------------------------------------------------------

def test_todo_does_not_crash_and_gives_none():
    assert todo(123) is None
