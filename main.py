import cv2
import numpy as np
import os
from time import time
import pyautogui
import win32gui, win32ui, win32con
from windowcapture import WindowCapture

os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture()

loop_time = time()
while(True):

    screenshot = wincap.getScreenshot()

    cv2.imshow('Computer Vision', screenshot)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break


print('Done.')


