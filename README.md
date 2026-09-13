# My Projects

A collection of small Python projects and learning exercises. The repository is intentionally varied: it contains beginner programming exercises, command-line utilities, object-oriented examples, audio experiments, and a small OpenAI API example.

## Projects

| File | Description | Extra setup |
| --- | --- | --- |
| `alarmclock.py` | Command-line alarm with optional audio playback | `pygame` for audio |
| `annoying_roomate.py` | Small beginner loop exercise | None |
| `avgOOP.py` | Experimental average-input exercise | None |
| `coffeeshop.py` | Placeholder learning exercise | None |
| `compoundinterestcalculator.py` | Starter exercise for compound-interest calculations | None |
| `donate.py` | Input/confirmation exercise for donation amounts | None |
| `loopingsong.py` | Loops a local audio file until interrupted | `pygame` |
| `monitor_app.py` | Terminal system monitor and localhost TCP port scanner | Python standard library |
| `openaitest.py` | Minimal OpenAI Responses API example | `openai` + API key |
| `shoopingcart.py` | Starter shopping-cart input exercise | None |
| `slotmachineOOP.py` | Slot-machine exercise demonstrating classes and randomness | None |
| `validateuserexperience.py` | Simple username validation exercise | None |

## Requirements

- Python 3.10+ recommended.
- Most scripts use only the Python standard library.
- Audio examples require `pygame`:

```bash
python -m pip install pygame
```

- The OpenAI example requires the official `openai` Python package:

```bash
python -m pip install openai
```

## Running a project

Run scripts from the repository root, for example:

```bash
python monitor_app.py
python alarmclock.py 07:30:00
python loopingsong.py way_down_we_go.mp3
```

### OpenAI example

Set your API key in the environment rather than putting it in source code:

```bash
export OPENAI_API_KEY="your-api-key"
python openaitest.py
```

On Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="your-api-key"
python openaitest.py
```

Never commit API keys, passwords, tokens, or other secrets to this repository.

## Audio files

The repository currently includes `way_down_we_go.mp3`, which is used by the audio examples. Only redistribute audio that you have permission to publish. If you do not have redistribution rights, remove the audio file and use your own local file instead.

## Network scanner safety

`monitor_app.py` scans **localhost only** (`127.0.0.1`) by default. Do not modify it to scan systems you do not own or have explicit permission to test.

## Project status

This repository is primarily a learning portfolio. Some files are intentionally simple or experimental rather than production-ready libraries. Contributions that improve correctness, documentation, tests, and code quality are welcome.

## License

No license has been selected yet. Until a license is added, normal copyright rules apply and others should not assume they have permission to reuse the code. Add a license if you want to grant explicit reuse rights.
