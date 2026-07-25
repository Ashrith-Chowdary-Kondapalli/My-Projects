import os
import pygame
import time

sound_file = os.path.join(os.path.dirname(__file__), "way_down_we_go.mp3")

pygame.mixer.init()
try:
    pygame.mixer.music.load(sound_file)
except pygame.error as e:
    raise SystemExit(f"Could not load sound file: {sound_file}\n{e}")

pygame.mixer.music.play(loops=-1)
print("Playing looped audio. Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping playback...")
    pygame.mixer.music.stop()
    pygame.mixer.quit()