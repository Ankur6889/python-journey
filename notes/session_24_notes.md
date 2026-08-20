# SESSION 24 NOTES — Thursday 20 August 2026

**Gap since S23: 1 day.** Interval gate applied — all cold work today was
promotable. Seventh session running that the gate was applied without being
asked for.

**Yield:** **1.8 OPENED.** Indexing defined for the first time in the course,
slicing taught in full (the S20 debt discharged), the list method roster
exercised cold, and **the S17 discriminator corrected to a one-directional
rule.** `drills/s24_lists.py` — 11/11. **Zero promotions, correctly:
everything taught was same-session.**

---

## SELF-TEST — answer these cold before reading on

1. A list has 4 items. What is the highest valid index, and what is `len`?
   Say both, in the right words.
2. `tools[1]` gives `'saw'`. What does `tools[1:2]` give?
3. `tools[10]` raises. `tools[10:20]` does not. Why does one raise and the
   other not?
4. What is `l[:]` for, and what makes it work?
5. Of `append`, `extend`, `insert`, `sort`, `remove`, `pop` — which mutate,
   and which one does **not** return `None`?
6. Complete both directions: "returns `None` ⇒ ______" and
   "mutating ⇒ returns `None`" — true or false, and name the counterexample.
7. `sort` and `sorted`. Which mutates, which builds a new list?
8. Name the five checks. (Hook: *Boundary pe khaali ek bahar mila.*)
9. What does **`mila`** compare against what?
10. `readings[-3:]` where `readings` is `[]`. What comes back, and why does
    it not raise?

---

## FULL TEACHING

### 1. Indexing — never formally taught until today

This was found by checking the curriculum before teaching slicing, **not** by
being caught. `__closure__[0]` had been in use since S22 with the `[]`
operator never defined. Same class of gap as `traceback` (S20), `list()`
(S15) and slicing itself (S20).

```python
tools = ['drill', 'saw', 'clamp', 'vice']

print(tools[0])    # drill
print(tools[1])    # saw
print(tools[3])    # vice
print(tools[-1])   # vice
print(len(tools))  # 4
print(tools[4])    # IndexError: list index out of range
```

**Mechanism.** `[]` after a list is the **index operator**. It takes a
**position** and hands back **the object at that position**. Positions start
at **0**, so the last valid index is `len - 1`. Negative indices count
**backward from the end**, `-1` being the last item.

**Precision fix issued, and it is an interview-grade one.** You said *"the
length is `len(list) - 1`"*. **The length is 4.** What equals `len - 1` is
the **last index**. Length counts items; indices label positions. Say:
*"the last index is `len - 1`, so 4 is one past the end."*

---

### 2. Slicing — the S20 debt discharged

```python
tools = ['drill', 'saw', 'clamp', 'vice']

print(tools[1:3])   # ['saw', 'clamp']
print(tools[0:2])   # ['drill', 'saw']
print(tools[1])     # saw
print(tools[1:2])   # ['saw']
```

**Mechanism.** `[start:stop]` is a **slice**. It is **half-open** — it starts
*at* `start` and stops *before* `stop`. **The same rule as `range()`**, which
you already own, so this is one rule reused rather than a new one.

**The distinction that matters, and you reached it unprompted:** indexing
hands back **one object**; slicing **builds a new list**. `tools[1]` is the
string `'saw'`; `tools[1:2]` is the list `['saw']`.

#### Step — the third parameter

```python
tools = ['drill', 'saw', 'clamp', 'vice']

print(tools[0:4:2])   # ['drill', 'clamp']
print(tools[::2])     # ['drill', 'clamp']
print(tools[::-1])    # ['vice', 'clamp', 'saw', 'drill']
print(tools[10:20])   # []
print(tools[10])      # IndexError: list index out of range
```

`[start:stop:step]`. Step is how far to jump each time; default `1`. A
**negative** step walks backward — that is what `l[::-1]` is.

#### Why the slice does not raise and the index does

**Indexing must return one specific object. If it is not there, there is
nothing to return, so it must raise. Slicing builds a list, and a list is
perfectly entitled to be empty.**

⚠ **Interview trap:** slicing **never** raises `IndexError`. Convenient, and
also how out-of-range bugs go silent — you get `[]` instead of a crash.

#### The same operator works on strings

```python
word = "clamp"
print(word[:-1])    # clam
print(word[::-1])   # pmalc
print(word[1:3])    # la
```

**This is why `word[:-1]` worked in the S20 recursion drill.** You were given
the minimum then, under protest, and correctly refused to be tested on it.
Now you have the mechanism.

---

### 3. `l[:]` — copy versus alias

```python
tools = ['drill', 'saw', 'clamp', 'vice']
b = tools        # assignment  -> alias
c = tools[:]     # full slice  -> new list
b.append('file')

print(tools)              # ['drill', 'saw', 'clamp', 'vice', 'file']
print(c)                  # ['drill', 'saw', 'clamp', 'vice']
print(tools is b, tools is c)   # True False
```

`append` = adds one item to the end, **in place**.

Omitted `start` means "from the beginning"; omitted `stop` means "to the
end". So `tools[:]` slices the whole list — and **by the rule above, a slice
is a new list object.** That is the copy idiom.

**Your explanation, and it was complete:** `b` is an alias of `tools`; `c` is
a new list; `append` **mutates** the object that `tools` and `b` both name;
**"I didn't see rebinding here."** That last clause is the sharpest thing you
said today — separating mutation from rebinding, cold, unasked, on a later
day.

⚠ **PARKED, NOT TAUGHT:** you called `c` *"an identical new list object"*.
The new list holds **the same item references**, not copies of the items.
That only bites on **nested** structures, and it is parked to the
"nested data structures" bullet in 1.8.

---

### 4. The list method roster — and the correction it produced

Each line run on a fresh `tools = ['drill', 'saw', 'clamp']`, printing what
the **call returned** and what `tools` **became**:

```
append   -> returned None      tools is now ['drill', 'saw', 'clamp', 'vice']
extend   -> returned None      tools is now ['drill', 'saw', 'clamp', 'vice', 'file']
insert   -> returned None      tools is now ['drill', 'vice', 'saw', 'clamp']
sort     -> returned None      tools is now ['clamp', 'drill', 'saw']
remove   -> returned None      tools is now ['drill', 'clamp']
pop      -> returned 'clamp'   tools is now ['drill', 'saw']
```

All six **mutate**. Five return `None`. **`pop` returns the item it removed**,
because "which item did I just take out?" is genuinely useful information.

#### THE CORRECTION — the most important line in these notes

**The S17 tell runs ONE WAY ONLY:**

- returns `None` ⇒ **mutating** ✅ (returning `None` has no other purpose)
- mutating ⇒ returns `None` ❌ — **`pop` is the counterexample**

**So the discriminator is: TYPE first** (immutable ⇒ mutation is impossible,
full stop), **then** the return value as a **one-directional hint** — never
as a biconditional. You had been reading a heuristic as an equivalence.

---

### 5. `mila` — check 5, generalised and finally landed

You asked for it in plain language, and then in Hindi.

**English.** You promised something in words. Your code does something.
`Mila` asks: **do the two match?** Read the promise **one sentence at a
time** and point at the line that keeps it. If a sentence has no line behind
it — or a line that does something slightly different — that is the bug.

**Hindi.**
> *"Mila" matlab — jo tumne promise kiya (docstring / spec) aur jo tumhara
> code sach mein karta hai — kya dono milte hain? Har sentence uthao, aur
> pucho: "iske peeche kaunsi line hai?"*

**The S23 failure case:** docstring said *"last digit"*, code said `% 10`.
For `-13` the two give different answers. **They did not meet. That was the
bug.**

⚠ **You performed `mila` correctly before you could define it.** Asked
whether `take_last([])` raising `IndexError` is a bug, you said: *"I was
specifically told to assume the list is not empty, so the function is not
wrong."* **That IS `mila`** — a sentence of the spec held against the code,
verdict returned. Naming the move you had already made is what landed it.

**The other four checks operate on the INPUT. `Mila` is the only one that
compares your own WORDS against your code.**

---

## ASSIGNMENTS AND WHAT HAPPENED

### Drill — `drills/s24_lists.py` (four functions, contract-only spec)

The docstring stated **only what the caller must be able to observe**. No
mechanism named anywhere — **choosing the right one was the drill.**

Your final code:

```python
def ordered_copy(readings):
    readings_copy = readings[:]
    readings_copy.sort()
    return readings_copy

def order_in_place(readings):
    return readings.sort()

def take_last(readings):
    return readings.pop()

def last_three(readings):
    return readings[-3:]
```

```
11 passed in 0.01s
```

**Three of four correct first time.** `last_three` handled the empty and
short-input cases **by construction, before you had been told slices never
raise** — the "right answer, mechanism absent" pattern in its harmless
direction, and worth knowing about yourself.

#### The one failure

```python
return readings[:].sort()
```
```
assert ordered_copy([3, 1, 2]) == [1, 2, 3]
E    assert None == [1, 2, 3]
E     +  where None = ordered_copy([3, 1, 2])
```

Not a crash — a **wrong value**. The slice copy was the correct instinct; the
bug sat downstream of it. `.sort()` mutates and evaluates to `None`, so you
returned `None`. Fixed by separating the mutation from the return, which is
the right shape.

**Style point, interview-relevant.** `return readings.sort()` in
`order_in_place` means *"hand back whatever `sort` hands back."* A reader
cannot tell whether you **meant** `None` or simply did not check. Writing
`readings.sort()` with no `return` states the intent directly. Same
behaviour; visible intent.

#### The five checks applied

You scanned all four functions and found the one real edge case:
**`take_last([])` raises `IndexError`** — `khaali` biting exactly where it
should. You then ruled it **not a bug**, because the spec excludes it. Both
halves were right.

---

## THINKING GAPS THIS SESSION (with error-type classification)

1. **`sort` believed to return a new list — "for sure".**
   *Knowledge gap (retention), plus a calibration miss.* The `sort`/`sorted`
   pair was taught in **S17**. ⚠ **NOT LEDGERED** — the block was declared
   [PREDICT] before it ran, and a PREDICT miss must never be back-dated into
   the ledger (S16 rule 1). Owed as a clean cold [RECALL].

2. **`extend` believed to build a new list.**
   *Reasoning error, not a gap.* Your reasoning was visible and honest —
   *"append already adds elements, so extend must do something different"* —
   which is a real inference, just wrong. The corrective is the TYPE-first
   half of the discriminator: the list is mutable, so mutation is on the
   table for every one of its own methods.

3. **The tell read as a biconditional.**
   *Structural flaw.* Not a memory failure — a logic failure. "Returns
   `None` ⇒ mutating" was silently upgraded to an if-and-only-if. This is the
   known exposure of teaching discriminators instead of rosters, and it is
   why the roster was run rather than handed over.

4. **`mila` glossed as "similar inputs".**
   *Knowledge gap, arbitrary-label class.* The other four checks describe
   input shapes, so the fifth got assimilated to the same pattern. Corrected
   by naming the instance you had already performed.

5. **Depth-before-answer, twice.**
   *Lazy thinking, and both recoveries took one line.* (a) Asked to mark your
   own six answers, you restated the output. (b) Asked what `.sort()`
   evaluates to, you fixed the code instead. **Both re-asks produced the
   correct mechanism immediately.** Same shape as the S20 `digit_sum` trace:
   **you have it and you skip it.** The intervention that works is the
   **re-ask**, not a re-teach.

**PUSHBACKS — three raised, running total 31.**
- **UPHELD (mentor error):** the `last_three` docstring said *"oldest of the
  three"*, importing a time ordering that was nowhere in the spec. Corrected
  in chat, not in the file — the drill file was yours.
- **NOT UPHELD — the first non-upheld challenge in the file's history:**
  *"isn't the corrected code a proof of my understanding?"* A reasonable
  claim, answered with reasoning rather than authority. The fix followed a
  pointer, so it is **guided**, not unaided; and your own S23 record has two
  cases of correct code with the mechanism absent. You accepted it and then
  answered correctly in one line.
- **PARTIALLY UPHELD:** *"shouldn't I just write the relevant cases?"* on the
  five-checks report. **Resolution: SCAN all five, REPORT only what bites.**
  Pre-filtering by "relevant" applies the same assumption that produced the
  bug — exactly how your S20 `n <= 10` boundary looked irrelevant right up
  until it was the bug.

**CALIBRATION: mixed, so S23's three over-ratings are not yet a drift.** One
hot (*"for sure"* on a wrong answer) against one well-calibrated (5/10 on a
4/5 answer, with an accurate reason).

---

## TEACHING MISTAKES THIS SESSION

1. **The roster volley was mis-tagged [PREDICT].** Five of the six methods
   were genuinely unseen, but **`sort` was taught in S17**, so that line was
   [RECALL] and your inversion of it was a real retention miss that now
   cannot be recorded. Declared to you in session and sent to the re-test
   list rather than back-dated. **The S18 principle — an unseen method on a
   taught type tests the discriminator — is sound, but it does not license
   sweeping a TAUGHT item into the same block. Check every line of a volley
   against the taught set, not just the block as a whole.**

2. **The `last_three` docstring was ambiguous.** *"Oldest of the three
   first"* imported a temporal ordering the drill never established. You were
   right to stop and ask. **A contract-only spec has to be readable as a
   contract; vague wording in a drill about spec-versus-code agreement is a
   particularly bad place to be sloppy.**

3. **The parked rule was put to you twice.** Once is the rule; the second ask
   spent a turn. You had already answered it by choosing material.

**What went right and should be repeated:** the missing `indexing` definition
was found by **searching the curriculum before teaching**, rather than by you
catching it. That is the first time a define-before-building gap in this
course was caught pre-emptively by the mentor.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| **index operator `[]`** | takes a POSITION, returns the object there | 0-based; last valid index is `len - 1`; length ≠ last index |
| **negative index** | counts backward from the end, `-1` = last | `-len` is the first; anything beyond raises |
| **`IndexError`** | raised when the position does not exist | **only indexing raises it — slicing never does** |
| **slice `[start:stop]`** | builds a **NEW list** | **half-open** — stops *before* `stop`; same rule as `range()` |
| **step `[start:stop:step]`** | how far to jump; negative walks backward | `l[::-1]` is a reversed **copy**, not a reversal in place |
| **`l[:]`** | full slice = the copy idiom | copies the **references**, not the items — matters when nested |
| **out-of-range slice** | returns `[]` | **silent** — no crash, so out-of-range bugs hide |
| **`append`** | adds ONE item at the end, in place | returns `None` |
| **`extend`** | adds MANY items at the end, in place | not a new list — mutates, returns `None` |
| **`insert(i, x)`** | puts `x` at position `i`, in place | returns `None`; shifts everything right |
| **`remove(x)`** | deletes the first occurrence of the VALUE | takes a value, not an index; returns `None` |
| **`pop()`** | removes the last item **and returns it** | **the counterexample to the tell** — mutates but does NOT return `None` |
| **`sort()`** | orders the list **in place** | returns `None` — `return l.sort()` returns `None` |
| **`sorted()`** | builds a **new** ordered list | leaves the original alone |
| **the tell** | returns `None` ⇒ mutating | **ONE-DIRECTIONAL** — mutating does *not* imply returns `None` |
| **the discriminator** | TYPE first, then the return value | immutable type ⇒ mutation impossible, no method can do it |
| **`mila`** | holds the PROMISE against the CODE, sentence by sentence | the only check that looks at your own words instead of the input |

---

## WHAT'S COMING NEXT — SESSION 25

**You asked for the recall block first. It runs first.**

1. **Saturday 22 Aug cold build block** — how did it go.
2. **[RECALL] the closure definition, cold.** Third attempt; the first two
   failed with the same two defects, and the root cause turned out to be
   mentor-side (cells taught as labels, fixed in S23).
3. **[RECALL] the iteration protocol** — `next()` and `StopIteration` by
   name.
4. **[RECALL] the docstring mechanism** — position, not punctuation.
5. **[RECALL] the five checks — one clean 5/5 promotes the set.**
6. **[RECALL] `sort` vs `sorted`, both halves separately** — the S24 debt.
7. **Term-tax failures still owed from S23:** `pass`, loop `else`, ternary,
   `print()` `sep`, associativity alone, `continue` precision.
8. **Then 1.8 continues:** tuple → dict → set → when-to-use-which.
   ⚠ **Comprehensions stay shut until the iteration protocol passes** — they
   are built on it, and it is currently `[~]`.
