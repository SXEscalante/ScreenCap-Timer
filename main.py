import cv2
import numpy as np
import os
import pyautogui
import win32gui, win32ui, win32con

from timer import Timer
from time import time
from playsound import playsound
from windowcapture import WindowCapture
from vision import findClickPositions
 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture()

loop_time = time()
start = False


while(start == False):
    screenshot = wincap.getScreenshot()

    # cv2.imshow('Computer Vision', screenshot)
    if findClickPositions('DotaStart.jpg', screenshot, 0.98, 'default') == True:
        start = True

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        start = True

cv2.destroyAllWindows()
Timer.startTimer()


