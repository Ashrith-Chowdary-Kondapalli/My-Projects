"""Play a local audio file continuously until interrupted."""

from __future__ import annotations

import argparse
import time
from pathlib import Path


def play_loop(sound_file: str) -> None:
    """Play *sound_file* repeatedly until Ctrl+C is pressed."""
    try:
        import pygame
    except ImportError as exc:
        raise RuntimeError("Install pygame first: pip install pygame") from exc

    path = Path(sound_file).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"Audio file not found: {path}")

    pygame.mixer.init()
    try:
        pygame.mixer.music.load(str(path))
        pygame.mixer.music.play(loops=-1)
        print("Playing looped audio. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping playback...")
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Loop an audio file until interrupted.")
    parser.add_argument("sound_file", nargs="?", default="way_down_we_go.mp3")
    args = parser.parse_args()
    play_loop(args.sound_file)
