from drills.s22_report import report


def test_mixed_call():
    assert report(1, 2, x=3) == ((1, 2), {"x": 3})


def test_empty_call():
    assert report() == ((), {})


def test_only_positionals():
    assert report("a", "b", "c") == (("a", "b", "c"), {})


def test_only_keywords():
    assert report(a=1, b=2) == ((), {"a": 1, "b": 2})
