"""
S35 five-checks runner.

Run it with:      python3 drills/s35_check.py

It calls YOUR functions in drills/s35_faults.py with the five-check cases
and prints what came back. It does not know the right answers and it does
not judge anything -- deciding "matched, yes or no" is your job.

Unwritten functions will show as None. That is expected until you write them.
"""

from s35_faults import check_angle, measure, safe_angles, total_valid


def show(label, call):
    """Run `call`, print what came back -- including a crash."""
    try:
        print(f"  {label:<34} -> {call()!r}")
    except Exception as exc:
        print(f"  {label:<34} -> {type(exc).__name__}: {exc}")


print("\n--- total_valid ---")
show('worked example ["45","90","n/a","30"]', lambda: total_valid(["45", "90", "n/a", "30"]))
show('khaali  []',                            lambda: total_valid([]))
show('ek      ["7"]',                          lambda: total_valid(["7"]))
show('bahar   ["-5","10"]',                    lambda: total_valid(["-5", "10"]))
show('bahar   ["3.5","2"]',                    lambda: total_valid(["3.5", "2"]))
show('bahar   ["n/a","junk"]',                 lambda: total_valid(["n/a", "junk"]))

print("\n--- check_angle ---")
show("worked example (90, 180)", lambda: check_angle(90, 180))
show("BOUNDARY       (180, 180)", lambda: check_angle(180, 180))
show("BOUNDARY + 1   (181, 180)", lambda: check_angle(181, 180))
show("khaali         (0, 180)", lambda: check_angle(0, 180))
show("bahar          (200, 180)", lambda: check_angle(200, 180))

print("\n--- safe_angles ---")
show("worked example ([45,90,200,30], 180)", lambda: safe_angles([45, 90, 200, 30], 180))
show("khaali         ([], 180)", lambda: safe_angles([], 180))
show("ek allowed     ([45], 180)", lambda: safe_angles([45], 180))
show("ek rejected    ([500], 180)", lambda: safe_angles([500], 180))
show("BOUNDARY       ([180,181], 180)", lambda: safe_angles([180, 181], 180))

_original = [45, 90, 200, 30]
safe_angles(_original, 180)
print(f"  {'input unchanged after call?':<34} -> {_original == [45, 90, 200, 30]}")

print("\n--- measure ---")
_log = []
show('good  measure("45", log)', lambda: measure("45", _log))
print(f"  {'   log is now':<34} -> {_log!r}")

_log2 = []
show('bad   measure("n/a", log)', lambda: measure("n/a", _log2))
print(f"  {'   log is now':<34} -> {_log2!r}")

_log3 = ["opened"]
show('append to existing log', lambda: measure("12", _log3))
print(f"  {'   log is now':<34} -> {_log3!r}")
print()
