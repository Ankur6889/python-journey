#!/usr/bin/env python3
"""
retest.py -- the spaced re-test queue for the Python journey.

WHY THIS EXISTS (Session 35 ruling, 30 Aug 2026):
    The queue lived in a markdown table in STATE.md and was scheduled by the
    mentor from memory, mid-session. It reached 75+ rows against RULES
    proposal 6's ~30-row trigger, and hand-scheduling demonstrably failed:
    `while` mechanics went eight sessions overdue, `.keys()`/`.values()` was
    never asked after S26, `SyntaxError` was missed in S27 and again in S32.
    The student ruled: build the script, do not write a rule. He also ruled
    that he never has to touch it -- this is a MENTOR tool.

USAGE (mentor only)
    python3 tools/retest.py                 # what is due today, shuffled
    python3 tools/retest.py -n 12           # ask for more rows
    python3 tools/retest.py --overdue       # only what is past due
    python3 tools/retest.py --all           # the whole queue, by due date
    python3 tools/retest.py --answers       # include the decode hooks
    python3 tools/retest.py --stats         # size / status / overdue counts

    python3 tools/retest.py --asked "set - UNORDERED" --result pass --rating 7
    python3 tools/retest.py --asked "SyntaxError"     --result fail

    Recording a result stamps today's date and recomputes the next due date
    from the rating, per RULES proposal 2: correctness promotes, the
    confidence rating sets the INTERVAL.
"""

import argparse
import datetime
import json
import pathlib
import random
import sys

QUEUE = pathlib.Path(__file__).with_name("queue.json")

# rating -> days until the next ask. A fail always comes back immediately.
FAIL_INTERVAL = 1
PASS_INTERVALS = [
    (5, 2),     # rated <= 5  -> 2 days
    (7, 5),     # rated <= 7  -> 5 days
    (9, 12),    # rated <= 9  -> 12 days
    (10, 25),   # rated 10    -> 25 days
]
UNRATED_INTERVAL = 3   # promoted with no rating taken -> short, per S34


def today():
    return datetime.date.today()


def load():
    with QUEUE.open() as fh:
        return json.load(fh)


def save(rows):
    with QUEUE.open("w") as fh:
        json.dump(rows, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def parse_date(text):
    return datetime.date.fromisoformat(text) if text else None


def days_overdue(row, ref):
    due = parse_date(row.get("next_due"))
    if due is None:
        return 9999          # never scheduled == maximally overdue
    return (ref - due).days


def interval_for(result, rating):
    if result == "fail":
        return FAIL_INTERVAL
    if rating is None:
        return UNRATED_INTERVAL
    for ceiling, days in PASS_INTERVALS:
        if rating <= ceiling:
            return days
    return PASS_INTERVALS[-1][1]


def render(rows, ref, show_answers):
    if not rows:
        print("\n  nothing due. say 'gap' and move on.\n")
        return
    width = max(len(r["term"]) for r in rows)
    print()
    for i, row in enumerate(rows, 1):
        over = days_overdue(row, ref)
        flag = "  " if over <= 0 else ("!!" if over > 14 else " !")
        due = row.get("next_due") or "never asked"
        print(f"{flag} {i:>2}. {row['term']:<{width}}  [{row['status']}]  due {due}")
        if show_answers:
            print(f"      -> {row['hook']}")
    print(f"\n  {len(rows)} item(s).  ! = overdue, !! = 14+ days overdue\n")


def main(argv=None):
    p = argparse.ArgumentParser(add_help=True)
    p.add_argument("-n", "--count", type=int, default=8)
    p.add_argument("--all", action="store_true")
    p.add_argument("--overdue", action="store_true")
    p.add_argument("--answers", action="store_true")
    p.add_argument("--stats", action="store_true")
    p.add_argument("--asked", metavar="TERM")
    p.add_argument("--result", choices=["pass", "fail"])
    p.add_argument("--rating", type=int, default=None)
    p.add_argument("--seed", type=int, default=None,
                   help="fix the shuffle, for reproducing a session")
    args = p.parse_args(argv)

    rows = load()
    ref = today()

    if args.asked:
        matches = [r for r in rows if args.asked.lower() in r["term"].lower()]
        if len(matches) != 1:
            print(f"'{args.asked}' matched {len(matches)} rows:", file=sys.stderr)
            for r in matches:
                print("   ", r["term"], file=sys.stderr)
            return 1
        if not args.result:
            print("--asked needs --result pass|fail", file=sys.stderr)
            return 1
        row = matches[0]
        gap = interval_for(args.result, args.rating)
        row["last_asked"] = ref.isoformat()
        row["next_due"] = (ref + datetime.timedelta(days=gap)).isoformat()
        row["rating"] = args.rating
        if args.result == "fail":
            row["status"] = "~"          # a failed re-test reverts to [~]
        else:
            # RULES proposal 2 (adopted S21): promotion = CORRECTNESS. A pass
            # recorded here has already been judged unaided and later-day by
            # the mentor, so it promotes. The rating sets the INTERVAL only.
            # BUG FIXED S36: this branch did not exist, so the script demoted
            # on failure but never promoted on success -- every pass since the
            # script was built would have been silently under-recorded.
            row["status"] = "x"
        save(rows)
        rated = f", rated {args.rating}" if args.rating is not None else ""
        print(f"{row['term']}: {args.result}{rated} -> next due {row['next_due']} "
              f"[{row['status']}]")
        return 0

    if args.stats:
        overdue = [r for r in rows if days_overdue(r, ref) > 0]
        never = [r for r in rows if not r.get("next_due")]
        print(f"\n  rows        : {len(rows)}")
        print(f"  [x]         : {sum(1 for r in rows if r['status'] == 'x')}")
        print(f"  [~]         : {sum(1 for r in rows if r['status'] == '~')}")
        print(f"  overdue     : {len(overdue)}")
        print(f"  never asked : {len(never)}\n")
        return 0

    if args.all:
        pool = sorted(rows, key=lambda r: r.get("next_due") or "0000-00-00")
        render(pool, ref, args.answers)
        return 0

    pool = [r for r in rows if days_overdue(r, ref) >= 0]
    if args.overdue:
        pool = [r for r in rows if days_overdue(r, ref) > 0]

    rng = random.Random(args.seed)
    rng.shuffle(pool)
    # the worst offenders always make the cut; the rest is genuinely random
    pool.sort(key=lambda r: -days_overdue(r, ref))
    head, tail = pool[:3], pool[3:]
    rng.shuffle(tail)
    picked = (head + tail)[: args.count]
    rng.shuffle(picked)
    render(picked, ref, args.answers)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
