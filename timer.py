import time
import cv2
import keyboard
from playsound import playsound

class Timer:

    @staticmethod
    def startTimer():
        cancelTimer = False
        seconds = 0
        minutes = 0

        while cancelTimer == False:
            if seconds < 10:
                print(f"{minutes}:0{seconds}") 
            else:
                print(f"{minutes}:{seconds}") 

            if keyboard.is_pressed("p"):
                cancelTimer = True

            if minutes > 0 and minutes < 11:
                if seconds == 0 or seconds == 30:
                    playsound("duck-quack.mp3", block=False)

            time.sleep(1)

            if seconds == 59:
                seconds = 0
                minutes += 1
            else:
                seconds += 1

    

