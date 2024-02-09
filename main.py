import cv2
import numpy as np
import os
import pyautogui

os.chdir(os.path.dirname(os.path.abspath(__file__)))

while(True):

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = screenshot[:, :, ::-1].copy()

    cv2.imshow('Computer Vision', screenshot)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

print('Done.')


