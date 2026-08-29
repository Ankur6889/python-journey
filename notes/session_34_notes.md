# Session 34 — the 1.8 tail
**Sat 29 Aug 2026, ~16:00–18:30 (~2½ h). Same sitting as S33, declared at the open.**
Yield: **1 curriculum tick (tuple), 2 ledger promotions, 36/36 on `drills/s34_tail.py`.**

---

## 0. SELF-TEST (do this cold, before reading on)

1. A set is _______ . Not "has no fixed order" — the precise word. Why does that
   make `s[0]` fail?
2. `["b","a","c"]` → you call `sorted()` on it, then `set()` on the result, then
   `list()`. What order comes out, and why?
3. What does `values.sort()` hand back? What does `sorted(values)` hand back?
4. What does `reversed(x)` do, and what does it hand back?
5. `list(set(names.sort()))` — name the error before you read the traceback.
6. `t = (4, 7, 4, 9)`. Two methods exist on a tuple and only two. Name them, and
   say why an immutable type can only have those.
7. `a` and `b` are dicts. Write, in one expression, the set of names that are a
   key in both — **without** converting either dict.
8. What does `{}` build? How do you write an empty set?
9. The five checks: name them, then say what makes something *a check* rather
   than a claim.

---

## 1. What actually happened

The drill was seven functions in one file, covering the four 1.8 bullets a
same-sitting session could still legitimately test. Six of them went straight in.
The seventh took four attempts and produced most of the session's findings.

**First run: 32/36.**
- `reading_stats` returned `None` for the absent-target case; the spec said `(0, -1)`.
- `unique_sensors` returned `list(set(names))` — deduped, unordered.

**Second run: 31/36.** `reading_stats` fixed. `unique_sensors` regressed to a crash.

**Final: 36/36.**

---

## 2. Full teaching

### 2.1 A set is UNORDERED

Not "doesn't store them in a fixed order". **A set has no positions at all.**

```python
print(list({"b", "a", "c"}))   # ['b', 'c', 'a']  (and not reliably even that)
```

Three consequences, and they are one fact seen three ways:

1. **`s[0]` raises `TypeError: 'set' object is not subscriptable`** — not
   `IndexError`. Python does not offer an operation it cannot make mean anything,
   and there is no "first element" to return. (Four-station hook: this is
   station 3, the TYPE, not station 4.)
2. **`sorted(s)` returns a LIST**, because there is no such thing as a sorted set.
3. **`set()` destroys any order that reached it.** This is the one that bit:

```python
sorted(["b", "a", "c"])              # ['a', 'b', 'c']   order built
set(sorted(["b", "a", "c"]))         # {'a', 'b', 'c'}   order thrown away
list(set(sorted(["b", "a", "c"])))   # ['b', 'c', 'a']   arbitrary again
```

**The ordering must be the LAST step, not an earlier one.** `sorted(set(names))`
works; `set(sorted(names))` cannot.

### 2.2 `sort` vs `sorted` — the pair, in one table

| | kind | mutates? | hands back |
|---|---|---|---|
| `values.sort()` | METHOD on a list | **yes** | **`None`** |
| `sorted(values)` | BUILT-IN, any iterable | **no** | **a NEW list** |

`sorted()` takes any iterable — a set, a tuple, a dict — and always returns a
list. `.sort()` exists only on lists.

### 2.3 `reversed` vs `.reverse` — the other pair, same table shape

| | kind | mutates? | hands back |
|---|---|---|---|
| `x.reverse()` | METHOD on a list | **yes** | **`None`** |
| `reversed(x)` | BUILT-IN | **no** | **an ITERATOR** |

⚠ **Neither of them orders anything.** They reverse the order that is already
there. `reversed(["c","a","b"])` yields `b, a, c` — reversing an arbitrary order
gives another arbitrary order.

**These two tables are the same table.** That is the point of writing them
together: `sort`/`sorted` and `reverse`/`reversed` are one distinction —
method-mutates-returns-`None` vs built-in-builds-something-new — wearing two sets
of names.

### 2.4 The mutating tell — and which third of it is missing

Three parts:

1. **TYPE FIRST.** On an immutable object, mutation is not on the table at all.
2. **THE TELL.** Returns `None` ⇒ it mutated. Nothing else is worth returning
   `None` for.
3. **THE DIRECTION IT DOES NOT RUN.** A value coming back tells you **nothing**.
   `.pop()` returns the item *and* mutates.

This session showed that (1) and (2)'s premise are intact and only the
**return-value** half is gone. See §4.

### 2.5 Tuple: the two-method roster

An immutable type can only carry methods that **report**, never methods that
change. So there are exactly two:

```python
t = (4, 7, 4, 9)
t.count(4)   # 2   — how many
t.index(4)   # 0   — position of the first
```

`.index()` raises `ValueError` if the value is absent, which is why the guard
matters when the spec asks for a sentinel like `(0, -1)`.

### 2.6 Dict keys as a set — and the half still owed

```python
a = {"x": 1, "y": 2}
b = {"y": 9, "z": 3}

set(a) & set(b)          # {'y'}   — works. `set(a)` builds a set of the KEYS.
a.keys() & b.keys()      # {'y'}   — the same answer with no conversion
```

Both are correct. The second matters because **`.keys()` returns a VIEW, and
views support set operations directly** — `commanded.keys() - supported` is a
real robot check with no loop and no conversion. **This was owed as a cold ask
this session and was not fired; it is the first thing in S35.**

---

## 3. The code

```python
def build_queue(base, extras, urgent):
    new_queue = base[:]
    new_queue = new_queue + extras
    new_queue.insert(0, urgent)
    return new_queue

def drop_task(queue, name):
    if name in queue:
        return queue.remove(name)
    else:
        return None

def ranked(values):
    return sorted(values)          # not values.sort() — that mutates the caller's list

def rank_in_place(values):
    return values.sort()

def reading_stats(readings, target):
    if target in readings:
        return readings.count(target), readings.index(target)
    else:
        return (0, -1)

def shared_keys(a, b):
    return set(a) & set(b)

def unique_sensors(names):
    return sorted(list(set(names)))
```

Two style notes, neither an error:

- `drop_task` — `return queue.remove(name)` works *because* `.remove()` returns
  `None`, so the function returns `None` as specified. It is leaning on the tell
  rather than stating it. `queue.remove(name)` on its own line is clearer.
- `unique_sensors` — the inner `list()` is redundant. `sorted()` takes any
  iterable and always returns a list: `sorted(set(names))`.

---

## 4. Thinking gaps this session

**GAP 1 — the return-value third of the mutating tell. Error type: knowledge gap,
narrow and precisely located.**
In `ranked` he wrote, unaided and unprompted: *"could have also used
`values.sort()` but that will mutate the passed list so not using that."* **TYPE
owned, MUTATES owned.** Ninety seconds later, two functions down:

```python
return list(set(names.sort()))
# TypeError: 'NoneType' object is not iterable
```

He knows `.sort()` mutates. He does not know it hands back `None`. **The row has
been re-taught as three parts four sessions running; only one part is missing.**

**GAP 2 — `reversed()` reached for as a sorter. Error type: name collision (label
floating over intact machinery).**
Offered `return reversed(list(set(names)))` for a docstring asking for ascending
alphabetical order. **In S33, one day earlier, he avoided `reversed()` because he
believed it mutates.** Avoided as a mutator, then deployed as a sorter — two
opposite errors on one pair in twenty-four hours.

**GAP 3 — the five checks were reported without being run. Error type: structural
flaw in the working method, not a knowledge gap.**
The report given was *"khaali actually taken care of by if condition, ek also
taken care of, bahar also taken care of"* — for `reading_stats`, which failed both
the empty-input case and the absent-target case; and *"checks N/A"* for
`unique_sensors`, which failed on the worked example printed in its own docstring.
**Written by reading the code and seeing an `if`.** An `if` in the body is not a
check. **A check is a case you ran and a value you looked at.**

**GAP 4 — could not name the error without the traceback. Error type: honest gap,
declared — and the interesting part is what happened next.**
Shown the failing line he said *"I can't see the fault, that's the thing, I
believe its correct"*, then described a completely sound three-step intent.
Shown the traceback he found it in one line, unaided: *"ah fuck `.sort` returns
`None`."* **The reasoning is not the gap. Not running the thing is the gap** —
which is Gap 3 again, from the other side.

**NOT A GAP, and worth recording as the session's best moment.** Asked to trace
`list(set(sorted(["b","a","c"])))`, he demolished his own proposed fix using the
fact he had been promoted on twenty minutes earlier: *"oh right, set doesn't
store elements in a sequence."* **He self-corrects reliably when asked to trace,
and not at all when asked to write.**

---

## 5. Teaching mistakes this session

1. ⚠⚠ **A gate was made impossible to discharge.** The five checks were enforced
   on the word "done" — correct — but the form demanded was `python3 -m pytest`,
   which he has never been taught and which STATE explicitly forbids asking of
   him. He was held to it **twice** before stopping it: *"I am not able to run the
   test myself... don't delay the session for unnecessary things."* **Upheld in
   full.** The five checks are run by calling his own function and looking at what
   comes back. **Check an instruction is executable by him before enforcing it.**

2. ⚠ **A promised ask was never fired.** `.keys()`-as-a-view was announced as
   coming after the drill, then lost to debugging. It is the last thing blocking
   the 1.8 dict bullet.

3. ⚠ **Only one confidence rating was taken all session** (7/10 on set-unordered).
   `sort`/`sorted` was promoted without one; the interval defaults to short.

4. ⚠ **The session's one raising snippet arrived by accident**, out of his own
   bug, rather than by design. Second session running this has been written down.

---

## 6. Reference checklist

| Name | What it does | The trap |
|---|---|---|
| **set — unordered** | no positions at all | not "no *fixed* order" — **none**. `s[0]` is `TypeError`, not `IndexError` |
| **`set()` in a pipeline** | builds a set from an iterable | **it destroys order.** Sort LAST, never before a `set()` |
| **`sorted(x)`** | built-in; new LIST from any iterable | always a list, even from a set or dict |
| **`x.sort()`** | list method; orders in place | **returns `None`** |
| **`reversed(x)`** | built-in; an ITERATOR, back-to-front | **it does not sort.** Reversing arbitrary order gives arbitrary order |
| **`x.reverse()`** | list method; reverses in place | **returns `None`**; the name is one letter from `reversed` |
| **the tell** | returns `None` ⇒ it mutated | **one direction only.** A value back tells you nothing — `.pop()` returns *and* mutates |
| **tuple roster** | `.count()`, `.index()` — and only those | `.index()` raises `ValueError` when absent |
| **`.keys()`** | a VIEW of the keys | supports `&` `\|` `-` **directly** — no `set()` needed |
| **`{}`** | an empty **dict** | `set()` is the only way to write an empty set |
| **the five checks** | boundary, khaali, ek, bahar, mila | **a check is a case you RAN.** An `if` in the body is not a check |

---

## 7. What's next — Session 35

1. The rule ruling he is owed (random spaced revision → recommendation: build the
   queue script, don't write a rule).
2. Two one-line asks that close two 1.8 bullets: **`{}` builds a dict**, and
   **what `a.keys()` is and why `&` works on it**.
3. The return-value third of the mutating tell — that third alone.
4. `reversed` vs `.reverse` as a pair, in one table, and the unanswered question:
   **what does `reversed(x)` hand back?**
5. **Then 1.9 — error handling**, with the overdue label set (`SyntaxError`,
   `AttributeError`, the four-station hook by name) run *inside* the subsection
   rather than ahead of it.
