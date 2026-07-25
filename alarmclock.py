import time
import datetime as dt
import pygame


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "Python\\learnings\\way_down_we_go.mp3"
    is_runing = True

    while is_runing:
          current_time = dt.datetime.now().strftime("%H:%M:%S")
          print(current_time)

          if current_time == alarm_time:
                print("WAKE UP! 😴")

                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                      time.sleep(1)

                is_runing = False

          time.sleep(1)

if __name__ == "__main__":
        alarm_time = input("Enter the alarm time: ")
        set_alarm(alarm_time)