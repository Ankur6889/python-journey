from drills.s34_tail import (
    build_queue,
    drop_task,
    ranked,
    rank_in_place,
    reading_stats,
    shared_keys,
    unique_sensors,
)


# --- build_queue -----------------------------------------------------------

def test_build_queue_order():
    assert build_queue(["scan", "grip"], ["lift", "drop"], "estop") == [
        "estop", "scan", "grip", "lift", "drop"
    ]


def test_build_queue_does_not_touch_base():
    base = ["scan", "grip"]
    build_queue(base, ["lift"], "estop")
    assert base == ["scan", "grip"]


def test_build_queue_returns_a_different_object():
    base = ["scan"]
    assert build_queue(base, [], "estop") is not base


def test_build_queue_empty_base_and_extras():
    assert build_queue([], [], "estop") == ["estop"]


def test_build_queue_one_extra():
    assert build_queue(["a"], ["b"], "z") == ["z", "a", "b"]


# --- drop_task -------------------------------------------------------------

def test_drop_task_removes_first_occurrence_only():
    q = ["scan", "grip", "scan"]
    drop_task(q, "scan")
    assert q == ["grip", "scan"]


def test_drop_task_absent_name_leaves_queue_alone():
    q = ["grip", "scan"]
    drop_task(q, "weld")
    assert q == ["grip", "scan"]


def test_drop_task_returns_none():
    q = ["grip"]
    assert drop_task(q, "grip") is None


def test_drop_task_on_empty_queue():
    q = []
    drop_task(q, "grip")
    assert q == []


def test_drop_task_mutates_the_same_object():
    q = ["grip", "scan"]
    same = q
    drop_task(q, "grip")
    assert same == ["scan"]


# --- ranked ----------------------------------------------------------------

def test_ranked_sorts():
    assert ranked([3, 1, 2]) == [1, 2, 3]


def test_ranked_does_not_touch_input():
    v = [3, 1, 2]
    ranked(v)
    assert v == [3, 1, 2]


def test_ranked_empty():
    assert ranked([]) == []


def test_ranked_single():
    assert ranked([7]) == [7]


def test_ranked_negatives_and_duplicates():
    assert ranked([0, -5, 3, -5]) == [-5, -5, 0, 3]


# --- rank_in_place ---------------------------------------------------------

def test_rank_in_place_orders_the_original():
    v = [3, 1, 2]
    rank_in_place(v)
    assert v == [1, 2, 3]


def test_rank_in_place_returns_none():
    assert rank_in_place([3, 1]) is None


def test_rank_in_place_keeps_the_same_object():
    v = [3, 1, 2]
    same = v
    rank_in_place(v)
    assert same is v and same == [1, 2, 3]


def test_rank_in_place_empty():
    v = []
    rank_in_place(v)
    assert v == []


# --- reading_stats ---------------------------------------------------------

def test_reading_stats_repeated_target():
    assert reading_stats((4, 7, 4, 9), 4) == (2, 0)


def test_reading_stats_single_target():
    assert reading_stats((4, 7, 4, 9), 7) == (1, 1)


def test_reading_stats_missing_target():
    assert reading_stats((4, 7, 4, 9), 5) == (0, -1)


def test_reading_stats_empty_tuple():
    assert reading_stats((), 4) == (0, -1)


def test_reading_stats_target_at_the_end():
    assert reading_stats((4, 7, 9), 9) == (1, 2)


def test_reading_stats_returns_a_tuple():
    assert isinstance(reading_stats((4,), 4), tuple)


# --- shared_keys -----------------------------------------------------------

def test_shared_keys_one_in_common():
    assert shared_keys({"x": 1, "y": 2}, {"y": 9, "z": 3}) == {"y"}


def test_shared_keys_none_in_common():
    assert shared_keys({"x": 1}, {"z": 3}) == set()


def test_shared_keys_all_in_common():
    assert shared_keys({"x": 1, "y": 2}, {"x": 0, "y": 0}) == {"x", "y"}


def test_shared_keys_empty_dict():
    assert shared_keys({}, {"z": 3}) == set()


def test_shared_keys_returns_a_set():
    assert isinstance(shared_keys({"x": 1}, {"x": 2}), set)


def test_shared_keys_ignores_values():
    assert shared_keys({"x": 1}, {"x": 999}) == {"x"}


# --- unique_sensors --------------------------------------------------------

def test_unique_sensors_dedupes_and_orders():
    assert unique_sensors(["b", "a", "b", "c"]) == ["a", "b", "c"]


def test_unique_sensors_already_unique():
    assert unique_sensors(["c", "a"]) == ["a", "c"]


def test_unique_sensors_empty():
    assert unique_sensors([]) == []


def test_unique_sensors_one_name_repeated():
    assert unique_sensors(["a", "a", "a"]) == ["a"]


def test_unique_sensors_returns_a_list():
    assert isinstance(unique_sensors(["a"]), list)
