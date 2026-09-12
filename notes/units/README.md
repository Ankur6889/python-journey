# Unit notes — Layer 0 / Python Core

One file per curriculum unit. Each file is a self-contained reference for that
unit: every concept covered in the course so far, with runnable code and the
output it produces. No self-tests, no session history — those live in
`notes/session_<N>_notes.md`.

| Unit | File | Status in the course |
|---|---|---|
| 1.1 How Python Runs Code | [unit_1_01_how_python_runs.md](unit_1_01_how_python_runs.md) | closed |
| 1.2 Variables, Name Binding, the Object Model | [unit_1_02_names_and_objects.md](unit_1_02_names_and_objects.md) | closed |
| 1.3 Data Types — the Five Primitives | [unit_1_03_data_types.md](unit_1_03_data_types.md) | closed |
| 1.4 Mutability vs Immutability | [unit_1_04_mutability.md](unit_1_04_mutability.md) | closed |
| 1.5 Operators and Expressions | [unit_1_05_operators.md](unit_1_05_operators.md) | closed |
| 1.6 Control Flow | [unit_1_06_control_flow.md](unit_1_06_control_flow.md) | closed |
| 1.7 Functions | [unit_1_07_functions.md](unit_1_07_functions.md) | closed |
| 1.8 Data Structures | [unit_1_08_data_structures.md](unit_1_08_data_structures.md) | closed |
| 1.9 Error Handling and Exceptions | [unit_1_09_exceptions.md](unit_1_09_exceptions.md) | taught in full |
| 1.10 Modules, Packages, Imports | [unit_1_10_modules_and_imports.md](unit_1_10_modules_and_imports.md) | taught in full |
| 1.11 File Handling | [unit_1_11_file_handling.md](unit_1_11_file_handling.md) | taught in full |
| 1.12 OOP | — | not started |
| 1.13 Python Internals | — | not started |

Conventions used in every file:

- Code blocks are complete and runnable as shown. Output follows in its own
  block, or as `# ->` comments on the line.
- Memory addresses printed by `id()` differ on every run; only "same or
  different within one run" carries meaning.
- The course runs on **Python 3.12 (CPython)**. A few facts are version-gated
  and say so.
- A "trap" is the specific way a construct is commonly misread. They are
  written next to the construct, not collected at the end.
