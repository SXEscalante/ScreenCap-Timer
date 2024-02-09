import cv2
import numpy as np
import win32gui, win32ui, win32con

class WindowCapture:
    w = 0
    h = 0

    def __init__(self):
        self.w = 1920
        self.h = 1080
    

    def getScreenshot(self):

        #hwnd = win32gui.FindWindow(None, windowname)
        hwnd = None
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0),(self.w, self.h) , dcObj, (0, 0), win32con.SRCCOPY)

        #Save Screenshot
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        #Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img = img[...,:3]

        img = np.ascontiguousarray(img)

        return img

