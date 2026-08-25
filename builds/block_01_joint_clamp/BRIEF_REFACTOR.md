# BUILD BLOCK 01 — REFACTOR PASS (Session 31)

## WHAT THIS TASK IS

You are not writing new features. You are **rearranging code that already
works, without changing what it does from the outside.** That is what the
word "refactor" means and that is the whole job.

Two things change in `clamp.py`:
  (A) the clamp rule stops being written out four times, and
  (B) `report` starts returning the dict it is supposed to return.

Nothing else changes. Nobody calling your functions should be able to tell
you touched anything — except that `report` now hands back a dict.

## WHY IT EXISTS / WHAT IT BUYS YOU

Right now the clamp rule lives in four places. Suppose tomorrow the rule
changes — say an angle exactly on a limit must be logged. You would have to
find and edit four blocks, and you would miss one. Not "might". Would.
When the rule lives in ONE place, you change it once and every caller gets
the new behaviour for free.

**Not claimed:** that your S29 code was wrong. It passed 13/13 cold. This is
the next thing you do to working code, not a fix for broken code.

---

## PART A — the clamp rule, four copies

Here are the four copies, as they sit in your file today:

```python
# clamp_one, lines 2-5
if angle<low:
    angle = low
elif angle>high:
    angle = high

# clamp_all, lines 13-18
if i<low:
    clamped_joint_angles.append(low)
elif i>high:
    clamped_joint_angles.append(high)
else:
    clamped_joint_angles.append(i)

# clamp_joints, lines 26-31
if angle_value<limits[limits_key][0]:
    clamped_joint_angles[limits_key]=limits[limits_key][0]
elif angle_value > limits[limits_key][1]:
    clamped_joint_angles[limits_key]=limits[limits_key][1]
else:
    clamped_joint_angles[limits_key]=angle_value

# report, lines 40-45  (same decision, buried inside the print calls)
if angle_value<limits[limits_key][0]:
    print(... limits[limits_key][0] ... CLAMPED)
elif angle_value > limits[limits_key][1]:
    print(... limits[limits_key][1] ... CLAMPED)
else:
    print(... angle_value ... ok)
```

**Target for Part A, and this is the exact test you apply to your own file:**

> Read `clamp.py` top to bottom. Count the function bodies that compare an
> angle against a `low` or a `high` using `<` or `>`.
> **When you are done that count must be 1.**

If you can point at two different places in the file that both decide
"below low -> low", you are not finished.

## PART B — `report` must return the dict

Today `report` builds `clamped_joint_angles = {}`, never puts anything in
it, and returns it empty. That is why 4 tests are red.

**`report` must keep printing exactly what it prints today, AND return the
same dict that `clamp_joints` returns for the same call.** Both. Printing is
not enough; returning is not enough.

Exact expected values — these are what the tests assert:

```python
LIMITS = {"shoulder": (-90, 90), "elbow": (0, 145), "wrist": (-180, 180)}

report(-200, 300, 0, **LIMITS)  ==  {"shoulder": -90, "elbow": 145, "wrist": 0}

report(0, 10, 20, **LIMITS)     ==  clamp_joints(0, 10, 20, **LIMITS)

report()                        ==  {}
```

The printed output for the first call must still be the three lines you
already print, in the same format, with `CLAMPED` / `ok` as today.

---

## WHAT YOU MAY AND MAY NOT DO

MAY:
- Add new functions of your own, with any name you like.
- Call any function in the file from any other function in the file.
- Delete, move or rewrite any line inside a function body.

MAY NOT:
- Change these four signatures. They stay character for character:
  ```python
  def clamp_one(angle, low, high)
  def clamp_all(low, high, *angles)
  def clamp_joints(*angles, **limits)
  def report(*angles, **limits)
  ```
- Edit `test_clamp.py` or `test_report.py`. I wrote both. They are the
  acceptance criteria, not material.
- Change the printed format of `report`.

---

## HOW YOU KNOW YOU ARE DONE

Run:

```
python3 -m pytest builds/block_01_joint_clamp -q
```

Right now that says `4 failed, 15 passed`.
**Done means `19 passed`** — and the Part A count above is 1.

---

## STEPS, IN ORDER

1. Do Part A. Re-run the tests. You should still be at `4 failed, 15 passed`
   — Part A is not supposed to fix anything, only to move it.
2. Do Part B. Re-run. Aim for `19 passed`.
3. Run THE FIVE CHECKS on your own file before you tell me it is done.
4. Write `LOG.md` in this folder — where you stalled, what you had to look
   up. One or two lines is fine. This is a step, not a suggestion; it was
   skipped in S29.
5. **Save the file** (Ctrl+S), then say "done".

The SOLUTION is withheld. Nothing else is. If any line above is still
unclear, say which line — that is a legitimate ask, not a hint request.
