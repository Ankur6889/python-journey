"""Acceptance tests for build block 02. WRITTEN BY THE MENTOR — do not edit.

pytest is not taught in Layer 0 and writing these is not your job.
Your job is validator.py. This file decides whether it works.

Run from the repo root:  python3 -m pytest builds/block_02_episode_validator -q
One level only:          python3 -m pytest builds/block_02_episode_validator -q -k L1
"""

import copy
import traceback

import pytest

from validator import faults, validate_all, validate_logged, UnidentifiedEpisode


def _origin(excinfo):
    """Name of the function the exception was actually raised in."""
    return traceback.extract_tb(excinfo.tb)[-1].name


GOOD = {"id": 7, "frames": 240, "fps": 30, "task": "pick up the red block"}


# --------------------------------------------------------------------------
# L1 — faults(record)
# --------------------------------------------------------------------------

def test_L1_clean_record_has_no_faults():
    assert faults(GOOD) == []


def test_L1_negative_id():
    assert faults({"id": -1, "frames": 240, "fps": 30, "task": "grasp"}) == ["id"]


def test_L1_three_faults_in_spec_order():
    record = {"id": 4, "frames": 0, "fps": 7, "task": ""}
    assert faults(record) == ["frames", "fps", "task"]


def test_L1_missing_key_is_its_own_code():
    assert faults({"id": 3, "frames": 90, "fps": 30}) == ["missing:task"]


def test_L1_every_key_missing():
    assert faults({}) == ["missing:id", "missing:frames",
                          "missing:fps", "missing:task"]


def test_L1_wrong_type_is_a_value_fault_not_a_missing_one():
    record = {"id": 3, "frames": "90", "fps": 30, "task": "grasp"}
    assert faults(record) == ["frames"]


def test_L1_wrong_type_on_id_and_on_task():
    record = {"id": "3", "frames": 90, "fps": 30, "task": 5}
    assert faults(record) == ["id", "task"]


def test_L1_zero_id_is_allowed_but_zero_frames_is_not():
    # id >= 0, frames >= 1. The two boundaries sit on either side of 0.
    assert faults({"id": 0, "frames": 1, "fps": 10, "task": "x"}) == []
    assert faults({"id": 0, "frames": 0, "fps": 10, "task": "x"}) == ["frames"]


def test_L1_fps_boundaries_of_the_allowed_set():
    assert faults({"id": 1, "frames": 5, "fps": 10, "task": "x"}) == []
    assert faults({"id": 1, "frames": 5, "fps": 50, "task": "x"}) == []
    assert faults({"id": 1, "frames": 5, "fps": 60, "task": "x"}) == ["fps"]
    assert faults({"id": 1, "frames": 5, "fps": 0, "task": "x"}) == ["fps"]


def test_L1_does_not_mutate_the_record():
    record = {"id": 4, "frames": 0, "fps": 7, "task": ""}
    before = copy.deepcopy(record)
    faults(record)
    assert record == before


# --------------------------------------------------------------------------
# L2 — validate_all(records)
# --------------------------------------------------------------------------

def test_L2_empty_dataset():
    assert validate_all([]) == {"clean": [], "faulty": {}}


def test_L2_the_worked_example():
    records = [
        {"id": 7, "frames": 240, "fps": 30, "task": "pick up the red block"},
        {"id": 4, "frames": 0, "fps": 7, "task": ""},
    ]
    assert validate_all(records) == {"clean": [7],
                                     "faulty": {4: ["frames", "fps", "task"]}}


def test_L2_clean_ids_keep_dataset_order():
    records = [
        {"id": 9, "frames": 5, "fps": 30, "task": "a"},
        {"id": 2, "frames": 5, "fps": 30, "task": "b"},
        {"id": 5, "frames": 5, "fps": 30, "task": "c"},
    ]
    assert validate_all(records)["clean"] == [9, 2, 5]


def test_L2_id_zero_is_a_real_id():
    records = [{"id": 0, "frames": 5, "fps": 30, "task": "a"}]
    assert validate_all(records) == {"clean": [0], "faulty": {}}


def test_L2_does_not_mutate_the_dataset_or_the_records_in_it():
    records = [
        {"id": 7, "frames": 240, "fps": 30, "task": "grasp"},
        {"id": 4, "frames": 0, "fps": 7, "task": ""},
    ]
    before = copy.deepcopy(records)
    validate_all(records)
    assert records == before


# --------------------------------------------------------------------------
# L3 — UnidentifiedEpisode
# --------------------------------------------------------------------------

def test_L3_missing_id_raises():
    records = [
        {"id": 7, "frames": 240, "fps": 30, "task": "grasp"},
        {"frames": 90, "fps": 30, "task": "place"},
    ]
    with pytest.raises(UnidentifiedEpisode):
        validate_all(records)


def test_L3_message_carries_the_position():
    records = [
        {"id": 7, "frames": 240, "fps": 30, "task": "grasp"},
        {"id": 3, "frames": 90, "fps": 30, "task": "place"},
        {"frames": 90, "fps": 30, "task": "lift"},
    ]
    with pytest.raises(UnidentifiedEpisode) as caught:
        validate_all(records)
    assert "2" in str(caught.value)


def test_L3_id_of_the_wrong_type_is_also_unusable():
    with pytest.raises(UnidentifiedEpisode):
        validate_all([{"id": "7", "frames": 90, "fps": 30, "task": "grasp"}])


def test_L3_negative_id_is_also_unusable():
    with pytest.raises(UnidentifiedEpisode):
        validate_all([{"id": -2, "frames": 90, "fps": 30, "task": "grasp"}])


def test_L3_first_unusable_id_ends_the_call():
    records = [
        {"frames": 90, "fps": 30, "task": "a"},
        {"id": "x", "frames": 90, "fps": 30, "task": "b"},
    ]
    with pytest.raises(UnidentifiedEpisode) as caught:
        validate_all(records)
    assert "0" in str(caught.value)


def test_L3_unusable_id_raises_even_with_other_faults_present():
    with pytest.raises(UnidentifiedEpisode):
        validate_all([{"id": None, "frames": 0, "fps": 7, "task": ""}])


def test_L3_is_an_exception_and_not_a_string_dressed_up():
    assert issubclass(UnidentifiedEpisode, Exception)


# --------------------------------------------------------------------------
# L4 — validate_logged(records, log)
# --------------------------------------------------------------------------

def test_L4_returns_what_validate_all_returns():
    records = [
        {"id": 7, "frames": 240, "fps": 30, "task": "grasp"},
        {"id": 4, "frames": 0, "fps": 7, "task": ""},
    ]
    log = []
    assert validate_logged(records, log) == validate_all(records)


def test_L4_clean_run_leaves_the_log_alone():
    log = []
    result = validate_logged([{"id": 7, "frames": 240, "fps": 30,
                               "task": "grasp"}], log)
    assert result == {"clean": [7], "faulty": {}}
    assert log == []


def test_L4_logs_once_and_lets_the_same_fault_through():
    records = [
        {"id": 7, "frames": 240, "fps": 30, "task": "grasp"},
        {"frames": 90, "fps": 30, "task": "place"},
    ]
    log = []
    with pytest.raises(UnidentifiedEpisode) as caught:
        validate_logged(records, log)
    assert log == ["UNIDENTIFIED"]
    assert "1" in str(caught.value)


def test_L4_the_fault_points_at_exactly_the_same_place():
    records = [{"frames": 90, "fps": 30, "task": "a"}]

    with pytest.raises(UnidentifiedEpisode) as bare:
        validate_all(records)

    log = []
    with pytest.raises(UnidentifiedEpisode) as wrapped:
        validate_logged(records, log)

    # Same message, and the deepest frame in the traceback is the same
    # function -- i.e. the fault the caller sees is the original one, not a
    # new one manufactured inside validate_logged.
    assert str(wrapped.value) == str(bare.value)
    assert _origin(wrapped) == _origin(bare)
