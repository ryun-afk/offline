import numpy as np
import win32gui, win32ui, win32con, win32api
import cv2 as cv
from time import time

class Window:

    # properties
    hwnd = None
    w = 0
    h = 0
    image_original = None
    image_grayscale = None
    loop_time = 0

    def __init__(self, window_name):
        # find the handle for the window we want to capture
        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))
        self.loop_time = time()

    def print_fps(self):

        print('FPS {}'.format(1 / (time() - self.loop_time)))
        self.loop_time = time()
        
    def update_screen(self):

        self.get_window_size()
        self.get_window_image()

    def get_window_size(self):
        # get the window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # account for the window border and titlebar and cut them off
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        # images into actual screen positions
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y
    
    def get_window_image(self):
        # get the window image data
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (int(self.w), self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        # convert the raw data into a format opencv can read
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # free resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # drop the alpha channel, or cv.matchTemplate() will throw an error
        img = img[...,:3]
        img = np.ascontiguousarray(img)

        self.image_original = img
        self.image_grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    def debug(self, name = 'debug', image = None, resize_factor = .4):
        
        if image is None:
            image = self.image_original

        cv.imshow(name, cv.resize(image, (0, 0), fx=resize_factor, fy=resize_factor))

