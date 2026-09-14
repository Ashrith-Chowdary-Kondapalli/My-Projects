# Project Notes

This page gives a little more context for the individual exercises in the repository.

## Command-line utilities

### `alarmclock.py`
Waits for a specified `HH:MM:SS` time and optionally plays a local audio file. The audio path is supplied by the user so the script does not depend on a machine-specific path.

### `monitor_app.py`
Displays basic local system information and scans TCP ports 1-1024 on `127.0.0.1`. It is intended for learning about sockets, threads, and terminal interfaces.

### `loopingsong.py`
Loads a local audio file with pygame and loops it until Ctrl+C is pressed.

## Beginner exercises

- `annoying_roomate.py` — simple list and loop practice.
- `avgOOP.py` — an experimental input/average exercise; it is kept as a learning artifact rather than presented as production code.
- `coffeeshop.py` — currently an empty starter file.
- `compoundinterestcalculator.py` — currently a starter file containing the exercise description.
- `shoopingcart.py` — early shopping-cart input/list exercise.
- `slotmachineOOP.py` — early object-oriented programming exercise using random symbols.
- `donate.py` — input validation and formatting exercise; it does not perform real payments.
- `validateuserexperience.py` — reusable name-validation example.

## API example

`openaitest.py` demonstrates a minimal OpenAI Responses API request. It expects credentials from the `OPENAI_API_KEY` environment variable and should never contain a hard-coded key.

## Public-release notes

Some exercises are deliberately preserved in their simple form so the repository remains a record of learning progress. When adding new projects, prefer:

1. A short module docstring.
2. Functions with clear names and type hints where useful.
3. A `main()` entry point for executable scripts.
4. A README section explaining dependencies and usage.
5. No secrets or machine-specific absolute paths.
6. Tests for non-trivial behavior.
