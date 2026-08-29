from drills.s33_copies import snapshot, drop_unsafe, replay_order, missing_joints


# ---------- snapshot ----------

def test_snapshot_is_equal():
    config = {"elbow": [0, 150], "wrist": [-90, 90]}
    assert snapshot(config) == config


def test_snapshot_outer_is_a_new_object():
    config = {"elbow": [0, 150]}
    assert snapshot(config) is not config


def test_snapshot_inner_is_a_new_object():
    config = {"elbow": [0, 150]}
    assert snapshot(config)["elbow"] is not config["elbow"]


def test_editing_the_copy_leaves_the_original_alone():
    config = {"elbow": [0, 150], "wrist": [-90, 90]}
    copy_of = snapshot(config)
    copy_of["elbow"][1] = 90
    assert config == {"elbow": [0, 150], "wrist": [-90, 90]}


def test_editing_the_original_leaves_the_copy_alone():
    config = {"elbow": [0, 150]}
    copy_of = snapshot(config)
    config["elbow"][0] = 77
    assert copy_of == {"elbow": [0, 150]}


def test_snapshot_of_empty_dict():
    assert snapshot({}) == {}


# ---------- drop_unsafe ----------

def test_drop_unsafe_normal():
    assert drop_unsafe([10, 200, 250, 30], 180) == [10, 30]


def test_value_exactly_on_the_ceiling_is_kept():
    assert drop_unsafe([180, 181, 179], 180) == [180, 179]


def test_drop_unsafe_empty():
    assert drop_unsafe([], 180) == []


def test_drop_unsafe_single_item_on_the_boundary():
    assert drop_unsafe([180], 180) == [180]


def test_drop_unsafe_removes_everything():
    assert drop_unsafe([200, 300], 180) == []


def test_drop_unsafe_negative_angles():
    assert drop_unsafe([-200, -10, 400], 180) == [-200, -10]


def test_drop_unsafe_does_not_mutate_its_argument():
    angles = [10, 200, 250, 30]
    drop_unsafe(angles, 180)
    assert angles == [10, 200, 250, 30]


def test_drop_unsafe_returns_a_new_list():
    angles = [5, 7]
    assert drop_unsafe(angles, 100) is not angles


# ---------- replay_order ----------

def test_replay_order_normal():
    assert replay_order(["home", "pick", "lift"]) == ["lift", "pick", "home"]


def test_replay_order_empty():
    assert replay_order([]) == []


def test_replay_order_single():
    assert replay_order(["home"]) == ["home"]


def test_replay_order_does_not_mutate_its_argument():
    steps = ["home", "pick", "lift"]
    replay_order(steps)
    assert steps == ["home", "pick", "lift"]


def test_replay_order_returns_a_new_list():
    steps = ["home"]
    assert replay_order(steps) is not steps


# ---------- missing_joints ----------

def test_missing_joints_normal():
    assert missing_joints(["elbow", "wrist", "base"], ["elbow", "base"]) == {"wrist"}


def test_missing_joints_returns_a_set():
    assert isinstance(missing_joints(["elbow"], []), set)


def test_missing_joints_nothing_missing():
    assert missing_joints(["elbow", "base"], ["elbow", "base"]) == set()


def test_missing_joints_duplicates_in_required():
    assert missing_joints(["wrist", "wrist", "elbow"], ["elbow"]) == {"wrist"}


def test_missing_joints_ignores_extras_in_present():
    assert missing_joints(["elbow"], ["elbow", "wrist", "base"]) == set()


def test_missing_joints_both_empty():
    assert missing_joints([], []) == set()
