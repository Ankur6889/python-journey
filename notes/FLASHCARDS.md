# Python Journey — Recall Deck

Generated from `notes/flashcards/deck.json` — do not edit by hand.
Cover the right-hand columns and answer cold.

## NAAM → DOT → TYPE → CHEEZ

*The four-station error hook (S26) — with station 0 added in S27*

Python ek line chalate waqt chaar station se guzarti hai. Gaadi jahan ruk gayi, wahi error.

| | | |
|---|---|---|
| 0. SYNTAX | Vaakya sahi hai? | SyntaxError / IndentationError — ek bhi line nahi chalti |
| 1. NAAM | Ye naam hai bhi kahin? | NameError |
| 2. DOT | Dot ke baad wala naam is object pe hai? | AttributeError |
| 3. TYPE | Is type pe ye kaam hota hi hai? | TypeError |
| 4. CHEEZ | Kaam ho sakta hai — par cheez andar hai? | ValueError / IndexError / KeyError |

> Station 4 ke teen bhai — poochho "dhoondh kaise rahe the?": position se → IndexError · chaabi se → KeyError · value se → ValueError.

## The five checks

*Finding edge cases (S20, S23, S25)*

boundary · khaali · ek · bahar · mila

| | | |
|---|---|---|
| boundary | Every condition's boundary | Read the operator; test the exact value ON the boundary |
| khaali | Empty / zero | The container with nothing in it |
| ek | Exactly ONE | Not 'few' — one |
| bahar | The type or sign you silently assumed | Covers TYPE as well as sign |
| mila | Do the base case and the step agree? | Hold the PROMISE against the CODE, sentence by sentence |

> The mnemonic gives you the list, never the thinking.

## Error ka naam batata hai KYA toota

*The full error reference (S26)*

Four families, by how far the program got.

| | | |
|---|---|---|
| A — code chala hi nahi | SyntaxError · IndentationError | Grammar toota, ya colon ne block khola aur andar kuch nahi mila |
| B — naam nahi mila | NameError · UnboundLocalError · AttributeError | Poore LEGB me nahi · local hai par value nahi · object pe attribute hai hi nahi |
| C — kaam nahi ho saka | TypeError · ValueError · IndexError · KeyError · ZeroDivisionError | Type ke liye defined nahi · andar ki cheez galat · position/chaabi hai hi nahi |
| D — galti hai hi nahi | StopIteration · RecursionError | Iterator khatam (for chupchaap pakadta hai) · CPython ka ~1000-frame depth guard |

> IndexError vs slicing: slicing NEVER raises. l[5:9] returns []. Only indexing raises.

---

## S0 — Day Zero

*Onboarding — how engineers think*

**Principles**

| Ask yourself | The answer |
|---|---|
| What is every program you will ever write? | A system. Failure cases are the engineering; the happy path is the easy half. |
| Atomicity — define it, and say where it recurs. | All-or-nothing. It recurs everywhere: banking, databases, distributed systems, AI pipelines. |
| Friction is the signal to do what? | To stay, not to leave. |
| How do the people who build things like LLMs think? | They break every problem into smaller problems, and ask why does this work — not just how do I make it work. They are comfortable sitting with confusion. |

---

## S1 — The Memory Model

*Names, objects, namespaces, id()*

**Principles**

| Ask yourself | The answer |
|---|---|
| Are names containers? | No. Names are labels tied to objects. Nothing is ever stored 'in' a name. |
| Where does type live — on the name or on the object? | The type is a property of the object, never of the name. |
| What is the namespace, concretely? | A real dictionary you can print. |
| What does assignment do to the object on the right-hand side? | Nothing. Assignment rebinds the name. It never edits the object on the right. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `id(obj)` | Returns the object's memory address. | Equal values may share an address — that is reuse, not a rule to rely on. |
| `locals()` | Dumps the current namespace as a dict. | Also shows Python's internal entries. |
| `rebinding` | Points a name at a different object. | Looks like mutation, isn't — other names are unaffected. |
| `refcount` | How many names currently point at an object. | Hits zero → the object is destroyed, automatically. |

---

## S2 — Rebinding, Identity vs Equality

*== vs is, the int cache, operators belong to types*

**Principles**

| Ask yourself | The answer |
|---|---|
| How much of the namespace does a rebinding touch? | One key in the namespace dict. Nothing else moves. |
| == and is — which question is each asking? | == is a value question, is is an identity question. They are not interchangeable, and is on values is a bug waiting for a number above 256. |
| Is the small-int cache a language rule? | No — an implementation optimisation. Never write code that depends on it. |
| Who owns operator behaviour? | The type. + on lists concatenates into a new object; + on NumPy arrays adds elementwise. |
| Mutation and rebinding — one sentence each. | Different verbs. One changes the object, the other changes the name. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `==` | Value comparison via __eq__. | Says nothing about identity. |
| `is` | Identity comparison via id(). | True for small ints by accident; use only for None-style singletons. |
| `int cache −5…256` | CPython reuses these objects. | is 'works' inside the range and fails outside it. |
| `list + list` | Builds a new concatenated list. | Originals untouched; the name is rebound. |
| `list.append(x)` | Mutates the list in place. | Every alias sees the change; returns None. |

---

## S3 — How Python Runs Code

*1.1 — bytecode, the PVM, implementations*

**Principles**

| Ask yourself | The answer |
|---|---|
| Trace the pipeline from your file to execution. | Source → bytecode → PVM. A two-stage pipeline, not a line-by-line translator. |
| What is the PVM? | A virtual CPU in software. Layers, not translations. |
| How do you test compile time vs run time empirically? | Syntax errors stop everything before any line runs; runtime errors only stop what follows. |
| 'The GIL' and 'Python is slow' — facts about what? | About CPython, the implementation — not about the language. |
| What actually costs Python its speed? | Dynamism. Bytecode is not the bottleneck. JIT plus type specialisation is how you make a dynamic language fast. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `bytecode` | Python-specific intermediate instructions. | Not machine code; the CPU never sees it. |
| `.pyc / __pycache__` | Cached bytecode. | Tied to the exact minor version; written on import, not on a direct run. |
| `PVM` | Software CPU that executes bytecode. | It doesn't 'translate for the CPU' — it IS the executor. |
| `CPython` | The reference C implementation. | Its properties get mistaken for the language's. |
| `PyPy` | JIT implementation, 5–10× on hot loops. | cpyext makes C extensions slow/partial — no good for the ML stack. |
| `REPL` | Live read-eval-print process. | State persists, unlike a script run. |
| `GIL` | One thread runs bytecode at a time. | A CPython property, not a language rule. |

---

## S4 — The Call Stack & the REPL

*1.1 closed — frames, LIFO, tracebacks*

**Principles**

| Ask yourself | The answer |
|---|---|
| Stack — the one-line definition. | Push/pop at the top only, LIFO. Plates on a counter. |
| Why is the call stack LIFO? | Because the innermost call always finishes first. A frame is pushed on call and popped on return. |
| What is in a frame? | Local namespace + current line + return address. |
| What is a traceback, and which way do you read it? | A frozen snapshot of the call stack, printed bottom-of-stack first so it reads as a story. Read it bottom-up. LIFO ≠ print direction. |
| REPL or script — which is for what? | REPL is for exploration (auto-print); scripts are for automation (explicit print). |
| Rebinding or mutation — how do you classify? | By what is on the LEFT of the =. The right side never decides. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `call stack` | Holds one frame per active call. | Depth is finite — deep recursion overflows it. |
| `frame` | Locals + current line + return address. | Locals die with the frame. |
| `x[0] = v` | __setitem__ — mutates in place. | Looks like assignment; every alias sees the change. |
| `REPL auto-print` | Echoes each expression's value. | Doesn't happen in scripts. |

---

## S5 — Data Types

*1.3 opened — int, float, bool, type checks*

**Principles**

| Ask yourself | The answer |
|---|---|
| Where does a script start executing? | At <module>, before any function call. |
| int vs float in one line each. | int is exact and unbounded; float is 64-bit and approximate — compare with a tolerance. |
| Is float error a printing quirk? | No. It compounds, and it is a real numeric difference. |
| What is bool, really? | A subclass of int. Same value, different type, different object. |
| isinstance or type() == — how do you pick? | isinstance is permissive (inheritance-aware); type() == is strict. Pick by intent. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `<module>` | The top-level frame. | Not main — main is just its first call. |
| `int` | Arbitrary-precision integer. | No overflow, but big ints cost memory and time. |
| `float` | 64-bit IEEE 754. | == on floats is a bug; use a tolerance. |
| `bool` | Subclass of int. | True == 1 yet True is not 1; the hierarchy inverts easily. |
| `type(x)` | Exact runtime type. | Rejects subclasses — including bool for int. |
| `isinstance(x, T)` | Type check honouring inheritance. | Accepts bool where you may have meant strict int. |
| `abs(a - b) < tol` | Float comparison. | Choosing the tolerance is your problem, not Python's. |

---

## S6 — Frames and the Module Frame

*What a frame is, and what it is not*

**Principles**

| Ask yourself | The answer |
|---|---|
| Frame — full definition. | The container Python creates to run one chunk of code: namespace, current line, return address. Created at runtime, destroyed on return. It is not the code. |
| Do frames require functions? | No. A file with zero defs still gets exactly one frame. |
| Namespace vs frame. | A namespace is a dictionary mapping names to references; a frame owns a namespace. Objects live in memory, not inside namespaces. |
| Why do local names die? | They were entries in that frame's namespace, and the frame is gone. |
| What is true of every frame except the top one? | It is paused, each on its own calling line. A frame on the stack is never finished. |
| Can a paused frame be paused on a def line? | Never. And a line finishing is not a frame finishing. |
| Is the stack chosen? | No. The stack is forced by the shape of the calls, not chosen. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `namespace` | Dict of names → references. | Does not hold objects, and is not global. |
| `traceback.print_stack()` | Dumps the live stack, no exception needed. | Prints bottom-of-stack first, like a traceback. |

---

## S7 — Tracebacks, Object Namespaces, str

*Reading the stack; attributes; immutability*

**Principles**

| Ask yourself | The answer |
|---|---|
| Do objects own namespaces? | Yes. Attributes are entries in the object's own namespace — which is why config.speed = 5 works. |
| A call raised deep below. Has the caller's line finished? | No. A line containing a call is not finished until that call returns — the caller sits paused on it. |
| Compile time and run time — what are they? | Two different moments. CPython produces bytecode at one; the PVM executes it at the other. Frames are created only at the second. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `config.speed = 5` | Sets an attribute in the object's own namespace — mutation. | id(config) does not change. Classify by the LEFT of the =. |
| `s[0] = "X"` | Attempted item assignment on a str. | Raises TypeError — str has no item assignment at all. Contrast obj.attr = …, which succeeds. |
| `p = True; q = 1 → p == q? p is q?` | True, then False. | == calls __eq__ (value); is compares id(). Different type ⇒ different object. |

---

## S9 — Strings, None, and the Left-of-Equals Rule

*Immutable types and the discarded return value*

**Principles**

| Ask yourself | The answer |
|---|---|
| Which way round is binding? | Bind the OBJECT to a NAME — never 'the name to the object'. |
| What decides mutate vs rebind? | The LEFT of the =. The right side never does. Mutation keeps id(); rebinding changes which object a name points at. |
| What happens when you 'change' an immutable object? | You don't. Every change is a new object. |
| Why is None tested with is? | Identity cannot be faked; equality can be overridden by __eq__. |
| A function with no return — what comes back? | None. Every call, including print, gets its own frame; the caller stays alive and paused underneath it. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `.strip()` | Returns a copy with leading/trailing whitespace removed. | Returns a NEW string — discarding the return value is the single most common string bug. Use s = s.strip(). |
| `.upper() / .lower()` | Return a new case-changed copy. | New object at a new id(); the original is unchanged because str is immutable. |
| `.replace(a, b)` | Returns a copy with a replaced by b. | Also a new object — assign it or it is lost. |
| `repr(x)` | The unambiguous printable form of an object. | Use it to SEE whitespace and quotes that print hides ('  culham  '). |
| `None` | The sole NoneType object; 'no value present'. | Not equal to 0 or False even though all are falsy. |
| `is None` | Identity test against the single None object. | Prefer over == None: == calls __eq__ and can be made to lie; is checks the address. |

---

## S10 — Conversion and Mutability

*1.4 — explicit/implicit conversion, aliasing, default args*

**Names**

| Name | What it does | The trap |
|---|---|---|
| `int(x) from a number` | Converts to integer. | Truncates TOWARD ZERO, silently: int(3.9)→3, int(-3.9)→-3. Not rounding. |
| `int(x) from a string` | Parses an integer literal. | Strict. int("3.5") raises ValueError; whitespace is tolerated, a decimal point is not. |
| `float(x)` | Converts to floating point. | float("3.5") works — unlike int. float("nan")/float("inf") are valid and break comparisons (nan != nan). |
| `str(x)` | Builds the string representation. | Almost never raises. str(3) + str(4) is "34" — concatenation, not addition. |
| `bool(x)` | Truthiness test. | Never reads string content. bool("False"), bool("0"), bool(" ") are ALL True. |
| `1 + 2.0` | 3.0, a float. | Python widens int→float because it is safe and lossless. |
| `True + 1` | 2, an int. | bool subclasses int; the value is obvious, the type is the twist. |
| `"5" + 3` | TypeError. | No safe direction — "53" and 8 are both defensible, so Python refuses to guess. |
| `10 / 2  vs  10 // 2` | 5.0 (float) vs 5 (int). | / always returns a float. // floors toward −∞: -7 // 2 is -4, whereas int(-7/2) is -3. |
| `Aliasing (b = a)` | Two or more names referring to the same object. | b = a NEVER copies — mutate via either, see it via both. |
| `Passing an argument` | Is an assignment — binds a new local name to the same object. | The function can mutate the caller's object. |
| `def f(x, bucket=[])` | The default is evaluated ONCE, at def time. | It accumulates across calls; one shared list living in f.__defaults__. |
| `The mutable-default fix` | bucket=None, then if bucket is None: bucket = []. | Use is None, never == None. |
| `Safe vs unsafe defaults` | Safe: 0, "", None, tuples. Unsafe: [], {}, set(), any mutable. | The bug only bites when the default actually applies — supplying your own argument hides it. |

---

## S11 — The Depth Doctrine; 1.4 Closed

*How deep to learn; the complete mutability table*

**Principles**

| Ask yourself | The answer |
|---|---|
| How deep are you learning this? | Level 2 — predict and debug — is the target. Level 3 only for what you intend to build. |
| What is the GIL good and bad for? | It makes threads useless for CPU-bound work and valuable for I/O-bound work. |
| ValueError vs TypeError in six words. | ValueError: right type, unusable value. TypeError: these types don't combine. |
| When does aliasing matter? | Only for mutable objects. |
| Why do mutating methods return None? | They are statements, not expressions. |
| Why does a mutable default accumulate? | It lives on the durable function object, which outlives every call. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `Mutable vs immutable types` | Mutable: list, dict, set. Immutable: int, float, bool, str, tuple. | Same id() after mutation. 'Changing' an immutable builds a NEW object and rebinds the name. |
| `MUTATE vs REBIND inside a function` | lst.append(v) acts on the object; lst = [v] rebinds the local name. | The caller SEES the first and sees NOTHING of the second. |
| `__defaults__` | Tuple on the FUNCTION OBJECT holding the defaults. | Not in the frame, not in the namespace — those are rebuilt each call. |
| `b = a.copy()` | New OUTER object; nested objects are aliased. | Shallow. Nested mutation leaks through. |
| `copy.deepcopy(a)` | New objects all the way down. | Nothing shared. Slower. |

---

## S12 — Operators

*Comparison, logic, precedence, +=*

**Principles**

| Ask yourself | The answer |
|---|---|
| // and int() — when do they differ? | // floors toward −∞; int() truncates toward zero. They agree on positives, which is why positives prove nothing. |
| = and == in three words. | = acts, == asks. |
| Precedence vs associativity. | Precedence is rank; associativity is direction when ranks tie. |
| What decides whether += mutates or rebinds? | Mutability, not the operator. += mutates a list and rebinds an int/str/tuple. id() is the ground truth. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `!=` | True when the two values differ. | 'True' here means 'they differ' — read it slowly. |
| `and / or / not` | and: both true. or: at least one. not: flips one operand. | Sides evaluate to booleans FIRST, then combine — two stages. |
| `Precedence` | Rank decides order: brackets > * / > + −. | Order is by RANK, not by left-to-right position. |
| `Associativity` | Direction when ranks tie: mostly left→right. | ** is the exception: right→left (2**3**2 = 512). |
| `+= on a list` | Mutates the SAME object in place (like .extend). | Every alias sees it; id() is unchanged. |
| `+= on int/str/tuple` | Rebinds the name to a NEW object. | The original and any alias are untouched; id() changes. |

---

## S13 — Side Effects, Membership, Short-Circuiting

*Mutate-vs-build; in; and/or return operands*

**Principles**

| Ask yourself | The answer |
|---|---|
| What are the two independent facts about any call? | Its side effect and its return value. |
| What is the real test for a method's return value? | Mutate → returns None. Build → returns a new object. That is the test — not method-vs-function. |
| What does in mean on a dict? On a string? | On a dict it means keys. On a string it means substring. |
| What makes a guard expression safe? | Short-circuiting: and/or return an operand and stop as soon as the answer is settled. |
| Why do negatives behave oddly under %? | % is defined by the FLOORED quotient, so negatives shift the magnitude, not just the sign. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `in / not in` | Membership test returning a bool. list/tuple/set → elements; str → substring; dict → keys. | On a dict it checks KEYS, not values. Use .values() for values. |
| `and / or (short-circuit)` | Return an OPERAND: and → first falsy else last; or → first truthy else last. Evaluation STOPS when settled. | They return an operand, not True/False. 2 or 1/0 → 2, and 1/0 never runs. |
| `& \| ^ ~ << >>` | Bitwise — operate on the binary bits of ints. | & is bitwise, and is logical — different animals. |
| `% (modulo)` | The leftover forced by floored //: (a//b)*b + r == a. Floor the quotient, then solve for r. | NOT school-remainder on negatives. -7 % 3 = 2, not 1. 'Sign follows divisor' is only the SIGN. |
| `** (power)` | Exponentiation; binds RIGHT-to-left, rightmost pair first. | 2**3**2 = 512, not 64. The only common right-associative operator. |

---

## S14 — Copies, Truthiness, Blocks

*Shallow vs deep; falsy; a block makes no scope*

**Principles**

| Ask yourself | The answer |
|---|---|
| What do shallow copies share? | Their inner objects. Mutation through one is visible through the other — id() settles it. |
| Which comes first, objects or names? | Objects come first; names are tags attached afterwards. |
| Immutable vs mutable, in terms of what moves. | Immutable → the NAME moves. Mutable → the OBJECT changes and the name stays. |
| What is falsy? | Emptiness is falsy, zero is falsy, everything else is truthy. |
| Colon, indent, dedent — and scope? | Colon opens a block, indentation delimits it, dedent ends it — and a block makes NO scope. Only a call does. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `shallow copy` | New outer box, same inner refs (aliases). | Mutating a nested object shows in the original too. |
| `deep copy` | Rebuilds everything recursively. | Slower, but fully independent. |
| `building method` | Returns a NEW object (e.g. str.upper). | You MUST assign its result to keep it. |

---

## S15 — The Iteration Protocol

*iter/next, iterable vs iterator, range, function scope*

**Principles**

| Ask yourself | The answer |
|---|---|
| What is a for loop, mechanically? | iter() ONCE, then next() every pass, until StopIteration. |
| How many next() calls do N items cost? | N+1 — the loop learns it is done by being refused. |
| Why are iterators consumed and iterables not? | Iterators hold forward-only state. Iterables just hand out fresh iterators. |
| Is range an iterator? | No. range is lazy and half-open, and it is an ITERABLE. |
| What creates a scope in Python? | Only def. Python has function scope, not block scope. |
| When is a name bound? | Only on a successful return. A raise binds nothing. An exception is a signal that travels, never a value that lands. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `iterable` | Can hand you an iterator when asked: list, str, dict, tuple, range. | Reusable. Saying 'the iterable is exhausted' is wrong — it never is. |
| `iterator` | Gives the next item on demand; raises StopIteration when spent. | Consumed because it holds forward-only state — NOT because it yields one at a time. |
| `iter()` | Called ONCE by a for loop, at the start, to get the iterator. | Two iter() calls on one iterable give two INDEPENDENT iterators. |
| `StopIteration` | The signal raised by an exhausted iterator; for catches it internally. | A SIGNAL, never a value. It is never bound to a name. |
| `list(x)` | Runs next() to exhaustion and collects everything into a NEW list. | A consumer of the protocol, not part of it. Drains an iterator in one call. |
| `range(n)` | A lazy, half-open stretch of integers from 0 up to (not including) n. | Stop is a fence, not a fencepost. And it is an ITERABLE, not an iterator. |
| `range(0)` | A legal empty range; the body runs zero times. | Not an error — but names created only in the body then never exist. |
| `NameError` | Named after what broke: the NAME does not exist. | 'Never created' is Python's only failure mode here — there is no 'scoped away'. |

---

## S16 — Loops and print

*for vs while, break/continue, nested loops*

**Principles**

| Ask yourself | The answer |
|---|---|
| for vs while in three words. | for asks; while checks. One consumes items from an iterator; the other re-evaluates a condition. |
| break vs continue. | break kills the LOOP; continue kills the ITERATION. Opposites, not variants. |
| Which direction does continue skip? | Downward. Anything below it in the body — including your state update — does not run. |
| Why do inner loops restart? | A fresh for gets a fresh iterator. That is also why a hoisted iterator silently breaks. |
| print and + on a type mismatch. | print converts; + refuses. Two different policies. |
| What does a while condition guard? | Entry to the body — not the printed value. Trace to the last cycle, always. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `print()` | Writes arguments to stdout after calling str() on each. | Returns None, not the text. |
| `sep / end` | sep goes between printed items (default " "); end goes after everything (default newline). | It is \n, not /n; the last newline is invisible; people assume the space lives in the strings. |
| `break` | Exits the innermost loop entirely. | Only one level; there is no break 2. |
| `continue` | Ends this iteration, jumps to the condition check. | Skips the state update below it → infinite while. |
| `Loop else` | Runs if the loop ended without break. | It is not 'otherwise' — nothing to do with if/else. |
| `Chained comparison` | a > b > c means a > b and b > c. | The middle operand is evaluated ONCE. |

---

## S17 — Loop else, pass, Ternaries

*The found-flag, expression vs statement, elif ladders*

**Principles**

| Ask yourself | The answer |
|---|---|
| What does a found-flag actually record? | 'Did the loop finish without breaking?' — which Python already knows. That is what loop else is. |
| Expression vs statement. | An expression evaluates TO a value; a statement performs an action. That is why a ternary fits inside print() and an if/else block does not. |
| What is an elif chain? | One ladder: the first true condition wins and everything below it is never evaluated. |
| How do you classify a method? | TYPE first, return value second. Never by the name. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `found-flag pattern` | Flag False before the loop, True on the hit, checked after. | Three touch-points for one question — which is exactly why loop else exists. |
| `pass` | A no-op. Fills a block the syntax requires but you have nothing to put in. | Not continue (skip iteration), not break (exit loop). And a comment is not a body. |
| `IndentationError` | Raised when a colon opens a block and no indented statement follows. | Comments do not count as a body. Only real statements do. |
| `ternary / conditional expression` | x if condition else y. Evaluates TO a value. | Use only when both branches select one simple value; otherwise write the block. |
| `else in a chain` | Optional catch-all. Evaluates no condition of its own. | Absence of else means nothing runs when all conditions are false. That is legal. |
| `the final loop check` | The loop re-tests the condition one more time than it prints, then exits silently. | Trace-tail truncation: stating the last PRINTED value is not stating the last CYCLE. |
| `non-mutating method` | Returns a new object: copy, sorted, upper, strip, split. | Original untouched — the return value is the only result, so you must bind it. |

---

## S18 — Errors, and Functions Opened

*Exception families; def vs call; LEGB*

**Principles**

| Ask yourself | The answer |
|---|---|
| What do exception names point at? | The broken part: name, value, or type. TypeError is a refusal, not a confusion. |
| When does a traceback appear? | Only when an exception goes UNCAUGHT. An exception travels; it never lands in a variable. |
| def vs the call — what does each build? | def builds the object; the call builds the namespace. |
| Parameter vs argument. | Parameter = name (a slot). Argument = value. |
| LEGB — what stops it, and how is E decided? | It stops at the first hit. E is decided LEXICALLY — where it is written, not where it is called. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `NameError vs ValueError vs TypeError` | Name never created / right type & wrong value / the operation doesn't exist between these types. | int("2.5") is a ValueError; "5" + 3 is a TypeError. Python doesn't guess — it refuses. |
| `a == b*(a//b) + (a%b)` | Defines // and % together. | Floor the quotient FIRST, then solve for r. 17 // -5 is -4, not -3; sign follows the divisor. |
| `in-place mutator` | Changes the object, returns None. | Not ALL methods on mutable types — pop/index/count return values. |
| `sort/sorted, reverse/reversed` | Mutates / returns new. | l = l.sort() silently sets l to None. |
| `def` | Builds a function object and binds a name. | The body does not run; there is no local namespace yet. |
| `implicit None` | Returned when a function ends with no return. | No return, bare return, and return None are all the same. |
| `f = greet` | A second name for the same object — an alias. | No brackets means nothing runs. |
| `function scope` | Only def creates scope; if/for/while/try don't. | That is the L only — a quarter of the LEGB story. |

---

## S19 — Closures

*Cells, free variables, nonlocal, key=*

**Principles**

| Ask yourself | The answer |
|---|---|
| Define a closure in one line. | A function object that binds a free variable from where it was created into its own private CELL, so the value survives after the enclosing frame has died. |
| Why doesn't the dead frame matter? | The bond lives on the OBJECT, not the frame. |
| Five calls to a factory — how many cells? | Five. Every call re-runs def → new object → new cell. Cells are per-object, never shared. |
| What do closures actually add? | No power, only a SHAPE: one argument from outside, the rest sealed inside. Required when someone ELSE calls your function. |
| When is a name decided to be local? | At def time. Assignment ANYWHERE in a body makes the name local for the WHOLE body. |
| Brackets or no brackets? | Brackets give you the return value; no brackets give you the object. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `free variable` | A name a function uses that is not its own local. | It is 'free' relative to that function, not undefined. |
| `cell / __closure__` | Tuple of cells on the function object; the value is in cell.cell_contents. | Per-object — two closures from one factory never share. |
| `enclosing (the E of LEGB)` | The function this one is WRITTEN INSIDE — lexical. | Decided by where it is written, not where it is called from. |
| `key=` | Takes a function; sorted calls it once per element, with one argument. | You never call it yourself; the output holds ORIGINAL elements, not key values. |
| `nonlocal` | Makes assignment target the enclosing cell. | Enclosing only — never module-level global. |
| `UnboundLocalError` | The name IS local, but no value is bound yet. | Distinct from NameError — the name exists, the value doesn't. |

---

## S20 — Recursion and Purity

*Base cases, pre/post-order, pure functions, edge cases*

**Principles**

| Ask yourself | The answer |
|---|---|
| What is recursion, in terms of frames? | Not new machinery: several frames of the same function alive at once, each with its own locals. |
| What are the two required parts of a recursive function? | A base case that returns without recursing, and a recursive case that calls itself on a strictly smaller input. |
| What are the TWO termination conditions? | (1) A base case exists. (2) Every call moves the input strictly closer to it. A base case that gets stepped over is not one. |
| Why does work placed AFTER the recursive call run in reverse order? | Each frame parks mid-body waiting for the call below it; when that returns, the frame resumes — deepest first. |
| What must a base case return, and why? | The IDENTITY for the operation: 0 for +, 1 for *, [] for list concatenation. The wrong one skews every answer. |
| Is RecursionError a law of recursion? | No. It is CPython's default depth guard at 1000 frames, to stop runaway memory use. |
| Printer or calculator — how do you tell? | Does it print or return? A printer uses a bare return and calls itself WITHOUT return in front. A calculator returns on every branch. The calculator is the testable one. |
| What are the two conditions for a pure function? | Output depends only on its arguments, and nothing outside the function changes. |
| How can a function that takes input and returns output still be impure? | If it mutates the object it was handed and returns that same object. The is check exposes it. |
| What is ONE line of a traceback? | One live frame on the call stack — not 'where the error happened', which is only the location half. |
| Why do traceback lines repeat in a recursion crash? | Because there were that many frames, all paused at the same line. The line did not fail repeatedly. |
| What is <stdin>? | The filename slot, for code that came from standard input rather than a file on disk. Nothing deeper. |
| Name the five checks for finding edge cases. | Boundary of every condition; empty/zero; one; the type or sign you silently assumed; whether the base case and the step agree. |
| Which check finds a bug like n <= 10 vs n < 10? | Check 1. Read the operator, test the exact value sitting ON the boundary — not a value near it. |
| Does argument count affect whether returning None is safe? | No. They are unrelated. None is only ever a problem at the point of USE, in the caller. |
| What exactly is __closure__[0]? | A cell object. The value is __closure__[0].cell_contents. And __closure__ is None, not an empty tuple, when there are no free variables. |

---

## S21 — global, *args, **kwargs

*Locality as a compile-time property; collect vs unpack*

**Principles**

| Ask yourself | The answer |
|---|---|
| When is locality decided, and over what span? | At compile time, over the WHOLE body. One assignment anywhere makes the name local everywhere, before any line runs. The LEGB walk only exists for names NOT classified local. |
| The three-way test for needing global/nonlocal. | Read / mutate / rebind. Only REBINDING needs the keyword. |
| Which direction do * and ** go? | Direction-dependent: the SIGNATURE collects, the CALL spreads. |
| Empty-but-typed or None? | Empty-but-typed beats None — () and {} keep the body uniform. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `global x` | Assignments to x inside the function target the module namespace. | Not needed for reads or mutations — only REBINDING. |
| `*args (signature)` | Collects leftover positional args into a TUPLE. | The empty case is (), never None; args is just a conventional name. |
| `**kwargs (signature)` | Collects leftover keyword args into a DICT. | Keys are strings; the empty case is {}. |
| `signature order` | normal params → *args → **kwargs. | Fixed by rule. |
| `* / ** at a CALL` | UNPACK a tuple/dict into separate arguments. | Opposite direction from the signature; produces arguments, not variables. |
| `keyword argument` | name=value in a CALL, matched by NAME. | It is a property of the call, not of the parameter. |

---

## S22 — lambda and Docstrings

*1.6 consolidation*

**Names**

| Name | What it does | The trap |
|---|---|---|
| `lambda` | An expression that evaluates to a function object. | One-expression body; auto-return; the letter λ decodes nothing. |
| `docstring / __doc__` | The first statement of the body, stored on the object. | Absent → None, not "". Comments are not data. |
| `pre-/post-order` | Work before / after the recursive call. | There is no single mutating n — one per frame. |
| `traceback line` | One live frame frozen at its executing line. | Callers' lines are calls, not 'problems'. |
| `forward-only state` | The iterator's position; no rewind. | Not 'one at a time'; iterable ≠ iterator. |
| `compile-time locality` | Assignment anywhere → local everywhere in the body. | Kills the cell inside a closure → UnboundLocalError. |

---

## S23 — Recall Block — Iterators, Closures, lambda

*Re-testing 1.5–1.7*

**Names**

| Name | What it does | The trap |
|---|---|---|
| `int() truncation vs // floor division` | int() drops the fraction toward ZERO; // drops it toward −∞. | int(-5.98) is -5, not -6. They agree only for positives. |
| `iter(x)` | Asks an iterable for a fresh iterator. | Called ONCE per loop, not once per pass. |
| `next(it)` | Asks the iterator for the next item. | Moves the position FORWARD ONLY. |
| `exhausted iterator` | Position sits past the end. | The loop body runs ZERO times; no error. |
| `cell` | A TYPE — a one-slot box holding a free variable. | cell_contents is the VALUE; __closure__ is the TUPLE. |
| `__closure__` | Tuple of cells, one per free variable. | None when there are none — not (). |
| `f vs f()` | The object handed over vs the function run now. | key=f() runs it immediately and fails. |
| `sorted(it, key=, reverse=)` | Returns a new list; key is called once per element. | key takes EXACTLY ONE argument — that is what forces the closure. |
| `docstring position` | First statement of the body → __doc__ at def time. | POSITION makes it, not the quotes; absent is None. |
| `the five checks` | boundary / empty / one / outside / agree. | The mnemonic gives you the list, never the thinking. |

---

## S24 — Lists — Indexing and Slicing

*1.8 opened*

**Names**

| Name | What it does | The trap |
|---|---|---|
| `index operator []` | Takes a POSITION, returns the object there. | 0-based; the last valid index is len − 1. Length ≠ last index. |
| `negative index` | Counts backward from the end; -1 is last. | -len is the first; anything beyond raises. |
| `IndexError` | Raised when the position does not exist. | ONLY indexing raises it — slicing never does. |
| `slice [start:stop]` | Builds a NEW list. | HALF-OPEN — stops before stop; the same rule as range(). |
| `step [start:stop:step]` | How far to jump; negative walks backward. | l[::-1] is a reversed COPY, not a reversal in place. |
| `l[:]` | Full slice — the copy idiom. | Copies the REFERENCES, not the items — matters when nested. |
| `out-of-range slice` | Returns []. | SILENT — no crash, so out-of-range bugs hide. |
| `append vs extend` | One item at the end vs many items at the end; both in place. | Both return None; extend does not build a new list. |
| `insert(i, x) / remove(x)` | Puts x at position i / deletes the first occurrence of the VALUE. | remove takes a value, not an index. Both return None. |
| `pop()` | Removes the last item AND RETURNS IT. | The counterexample to the tell — it mutates but does NOT return None. |
| `the tell` | Returns None ⇒ mutating. | ONE-DIRECTIONAL — mutating does NOT imply returns None. |
| `the discriminator` | TYPE first, then the return value. | Immutable type ⇒ mutation impossible, so no method can do it. |
| `mila (the fifth check)` | Hold the PROMISE against the CODE, sentence by sentence. | The only check that looks at your own words instead of the input. |

---

## S25 — Recall Block — Eleven Promotions

*Closures, iterators, control flow re-tested*

**Names**

| Name | What it does | The trap |
|---|---|---|
| `closure — the nesting trap` | A function object binding a free variable into a cell. | NESTING ALONE IS NOT ENOUGH — no capture ⇒ __closure__ is None. |
| `free variable` | A name used, not defined locally, and not a parameter. | The thing that TRIGGERS the closure. |
| `list(it) on a partly consumed iterator` | Drains what is left into a new list. | You get only what's LEFT, not the whole sequence. |
| `__doc__` | The attribute holding the docstring. | It ALWAYS exists; an absent docstring ⇒ None, not AttributeError. |
| `pass` | A no-op placeholder. | The name suggests 'skip' — that is continue. |
| `break` | Ends the WHOLE loop. | Also suppresses loop else. |
| `loop else` | Runs if no break happened. | Nothing to do with if/else — read it as nobreak. |
| `ternary` | A if C else B — an EXPRESSION. | The MIDDLE is the condition; the value comes first. |
| `precedence vs associativity` | Rank between DIFFERENT operators vs direction within the SAME rank. | Precedence cannot break ties. ** is right-to-left; everything else left-to-right. |
| `the five checks (Hindi hook)` | boundary / khaali / ek / bahar / mila. | ek = exactly ONE; bahar covers TYPE as well as sign. |

---

## S26 — Tuples and Dicts

*1.8 — tuple in full, dict opened*

**Names**

| Name | What it does | The trap |
|---|---|---|
| `tuple` | Immutable ordered sequence; indexable, iterable. | Immutability is SHALLOW — a mutable object inside can still be mutated. |
| `the comma` | MAKES the tuple. | (5) is an int. (5,) is a tuple. Parens are grouping, not construction. |
| `t.count / t.index` | The ONLY two tuple methods; both report. | Anything that would change it cannot exist. Derive it from the type. |
| `unpacking` | low, high = t binds items to names left-to-right. | Count mismatch ⇒ ValueError, not TypeError — the type is fine, the count is wrong. |
| `multiple return` | return a, b builds ONE tuple. | A function never returns more than one object. |
| `sum(iterable)` | Totals an iterable of numbers; returns a new value. | Does not mutate. |
| `dict` | key → value; [] takes a KEY; no scan. | Keys are unique — assigning an existing key OVERWRITES, never duplicates. |
| `hashable` | A key's hash must be stable, so the key must be immutable. | The error says 'unhashable type', not 'immutable'. Immutability ⇏ uniqueness. |
| `d[k] vs d.get(k)` | Lookup that raises vs lookup that returns None. | .get MOVES THE CRASH AWAY FROM THE CAUSE. Use [] when a missing key is a bug. |
| `d.get(k, default)` | A fallback instead of None. | Only safe when absence is genuinely expected. |
| `in on a dict` | Tests KEYS. | Not values. Not pairs. |
| `for k in d` | Walks the KEYS. | Then d[k] does the lookup a SECOND time — use .items(). |
| `.keys() / .values() / .items()` | Keys / values / (key, value) TUPLES. | .items() is tuple unpacking in disguise. |
| `AttributeError` | The name after the dot is not on the object. | vs TypeError: there the operation exists but the type refuses it. |
| `KeyError` | The key is not in the dict. | vs IndexError (position) vs ValueError (value) — station 4's three siblings. |

---

## S27 — Sets, del, and Container Choice

*1.8 finished; the error hook gains station 0*

**Names**

| Name | What it does | The trap |
|---|---|---|
| `expression vs statement` | An expression evaluates to a VALUE; a statement DOES something and yields nothing. | Test it: can it go inside print(...)? d[k] = v and del d[k] are statements. |
| `SyntaxError` | Grammar broken; NOTHING ran. | Line 1 never executes either — that is the tell. |
| `TypeError vs SyntaxError` | TypeError: the operation is not defined for these types. | TypeError needs a RUNNING program; SyntaxError never gets that far. |
| `IndexError / KeyError / ValueError` | jagah / chaabi / cheez absent. | The brackets are IDENTICAL on a list and a dict — what's INSIDE decides. |
| `subscriptable` | Can be indexed with [ ]. | set is NOT; list/tuple/str/dict are. |
| `del d[k]` | Removes the pair. | A STATEMENT — hands back nothing; raises KeyError if absent. |
| `d.pop(k)` | Removes and RETURNS the value. | The counterexample to the returns-None tell, on a second type. |
| `d.clear()` | Empties the dict, returns None. | Leaves {} — empty, not gone; the SAME object. |
| `dict ordering` | Keys stay in FIRST-INSERTION order. | Ordered ≠ sorted; overwriting a value does NOT move the key. |
| `set` | Unique, unordered, hashable items. | {} is an empty DICT — use set(). |
| `set.add` | Adds; returns None. | Adding something already present is a SILENT no-op. |
| `remove vs discard` | Raise vs shrug when absent. | Pick by whether absence is a BUG — the spec decides, not temperament. |
| `\| & -` | Union / intersection / difference. | All build a NEW set; − is NOT symmetric. |
| `set order` | There is NO first element. | The same file printed three different orders in three runs. |
| `.keys()` | A VIEW of the keys. | Not a list — but it DOES support set operations directly. |
| `when-to-use-which container` | Ask: 'what am I going to ASK this container?' | Not 'what am I storing?' — that is the downstream half. |
| `list vs tuple` | GROWTH, not order. | Both are ordered; only one can grow. |
| `sentinel values` | Mark 'nothing here'. | Must be something the data can NEVER contain — None in a list of Nones is a bug. |

---

## S28 — Comprehensions, zip, f-strings

*1.9 opened; the S19 debt closed*

**Principles**

| Ask yourself | The answer |
|---|---|
| What is the master key that explains comprehensions? | Expression vs statement. It explains why comprehensions exist, why sum([… for …]) is legal, and why a for loop cannot live in an f-string's braces. |
| Written order vs execution order in a comprehension. | Iterable → var → gate → expression. The gate protects the expression BECAUSE it runs first. |
| When should you not use a comprehension? | When you are not building a container. A comprehension BUILDS one. |
| How does zip fail? | Silently — both of its failure modes. It never raises. Check lengths yourself. |
| Why does an exhausted iterator give [] instead of a crash? | list() catches StopIteration. |
| What is an f-string, mechanically? | Evaluate → str() → splice. The braces hold an EXPRESSION. |
| Is correct usage evidence of a model? | No. f-strings hid for 27 sessions precisely because you type them right. |

**Names**

| Name | What it does | The trap |
|---|---|---|
| `list comprehension` | An expression that builds a new list. | It is an EXPRESSION — that's the point, not the brevity. |
| `anatomy` | [EXPR for VAR in ITERABLE if COND] | Written order ≠ execution order (4→2→3→1). |
| `the filter` | A gate; failures never reach the expression. | It only protects you BECAUSE it runs first. |
| `comprehension scope` | Its own namespace, discarded at the end. | The variable DOES NOT EXIST afterwards ⇒ NameError. |
| `dict comprehension` | {KEY: VALUE for VAR in ITERABLE} | Braces AND colon — forgetting the braces is a SyntaxError. |
| `.items() in a comprehension` | Yields (key, value) tuples. | Needs TWO names in the VAR slot. |
| `zip` | Pairs parallel iterables; yields TUPLES. | It REMOVES THE INDEX — that's why you use it. |
| `zip truncation` | Stops at the SHORTEST. | Silent. No error. Ever. |
| `zip exhaustion` | A second pass gives []. | Silent — list() catches the StopIteration. |
| `f-string` | Evaluate → str() → splice. | No f ⇒ {x} is literal characters. |
| `format spec` | {value:.2f}, {v:8.2f}, {n:03d}, {s:10s} | The number is TOTAL WIDTH; text goes left, numbers go right. |

---

313 cards across 28 sessions.
