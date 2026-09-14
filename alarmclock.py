"""Simple command-line alarm clock with optional audio playback.

The alarm waits until the local clock matches the requested HH:MM:SS time.
If a sound file is supplied and pygame is installed, it plays the sound once.
"""

from __future__ import annotations

import argparse
import time
from datetime import datetime
from pathlib import Path


def set_alarm(alarm_time: str, sound_file: str | None = None) -> None:
    """Wait for *alarm_time* and optionally play *sound_file*.

    Args:
        alarm_time: Alarm time in ``HH:MM:SS`` 24-hour format.
        sound_file: Optional path to a local audio file supported by pygame.
    """
    try:
        datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError as exc:
        raise ValueError("alarm_time must use HH:MM:SS format") from exc

    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("WAKE UP!")
            if sound_file:
                play_sound(sound_file)
            return
        time.sleep(1)


def play_sound(sound_file: str) -> None:
    """Play a local audio file with pygame."""
    try:
        import pygame
    except ImportError as exc:
        raise RuntimeError("Install pygame to use alarm audio: pip install pygame") from exc

    path = Path(sound_file).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"Sound file not found: {path}")

    pygame.mixer.init()
    try:
        pygame.mixer.music.load(str(path))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.25)
    finally:
        pygame.mixer.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple command-line alarm.")
    parser.add_argument("alarm_time", help="Alarm time, e.g. 07:30:00")
    parser.add_argument("--sound", help="Optional local audio file to play")
    args = parser.parse_args()
    set_alarm(args.alarm_time, args.sound)
