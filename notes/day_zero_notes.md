# DAY ZERO NOTES — Onboarding

**Topics: systems thinking · happy path vs failure cases · atomicity · distributed
systems (ROS2 mapping) · tutorial hell · AI tools as amplifiers**

No Python here. This is the mindset and the vocabulary the rest of the course
leans on.

---

## FULL TEACHING

### 1. Systems thinking

Describe how an ATM works and it decomposes into components: card reading,
identity verification, server communication, balance checking, dispensing,
session management. That is a *system*, not a machine.

**Systems thinking** = seeing how independent components interact to produce a
larger behaviour. Every program is a system: functions, classes, modules, APIs,
databases are all components that talk to each other.

The two questions to always ask: **what are the parts, and how do they talk to
each other?**

### 2. Happy path vs failure cases

The obvious description of any system covers only the **happy path** —
everything goes right. The real work is what happens when the network drops
mid-transaction.

Juniors write for the happy path. Seniors obsess over failure cases. That gap is
almost the whole difference between buggy and reliable software.

The standing checklist for any system:

| Question | Why it matters |
|---|---|
| What if the network fails? | External dependencies always fail eventually |
| What if the user inputs bad data? | Users will always surprise you |
| What if this runs twice simultaneously? | Concurrency bugs are hard to debug |
| What if storage is full? | Resources are always finite |
| What if the response takes too long? | Timeouts need explicit handling |

### 3. Atomicity

"Dispense the money, then signal the bank to deduct" leaves a dangerous gap:
what if the cash goes out but the deduction never lands?

**Atomicity**: a set of operations must either ALL succeed or ALL fail. No
acceptable in-between state. If one step fails, everything rolls back as if
nothing happened.

| Domain | Atomic operation | Why it matters |
|---|---|---|
| Banking | Debit + credit must both happen | Money can't vanish in transit |
| Databases | All rows updated or none | Data stays consistent |
| AI training | Checkpoint save must be complete | Corrupted checkpoints break training |
| ROS2 | Command sent + acknowledged | Robot acts on confirmed state only |

To be implemented in code later, at databases and error handling.

### 4. Distributed systems thinking — the ROS2 mapping

The ROS2 vocabulary already describes a classic distributed architecture:

| ROS2 concept | General equivalent | What it does |
|---|---|---|
| Node | Microservice / module | Independent logical unit |
| Topic (pub/sub) | Message queue / event stream | One-way async data flow |
| Service | API (request/response) | Ask for something, get an answer |
| Action | API with progress callbacks | Long task with a feedback loop |

PyTorch training pipelines, FastAPI backends and LLM serving use these same
patterns. The ROS2 background is a real head start.

### 5. Tutorial hell and shiny object syndrome

The pattern: when friction shows up mid-course, the brain seeks relief by
jumping to new material. It feels like progress; it is a reset back to
the comfortable beginner zone.

The antidote: **friction is the learning.** The moment it gets hard is exactly
the moment to stay.

The mechanism against it: a **Curiosity Parking Lot**. Anything out of scope gets
written down and visited at the right time — never mid-session, never by jumping
ship.

### 6. AI tools as amplifiers, not crutches

Powerful only for someone who already knows what good code looks like. Used too
early they generate code you cannot evaluate, debug, or improve.

| Stage | Use AI for | Never use AI for |
|---|---|---|
| Beginner (now) | Explaining errors, concepts | Writing your assignments |
| Intermediate | Code review, alternatives | First drafts of solutions |
| Advanced | Boilerplate, navigation | Architectural decisions |

---

## KEY MENTAL MODELS

- Every program you will ever write is a system.
- Failure cases are the engineering; the happy path is the easy half.
- Atomicity is all-or-nothing, and it recurs everywhere — banking, databases,
  distributed systems, AI pipelines.
- Friction is the signal to stay, not to leave.
- The people who build things like LLMs think differently: they break every
  problem into smaller problems, and ask *why does this work*, not just *how do I
  make it work*. They are comfortable sitting with confusion.

> "You're not learning to type Python. You're learning to think like an engineer."

---

## WHAT'S COMING NEXT — SESSION 1

Setup required first: VS Code, Python 3.12+ with PATH checked, the Python +
Pylance extensions, and `python --version` confirmed in a terminal.

Topic: how Python thinks — what happens when you run a script, how Python stores
things in memory, what the interpreter actually does.
