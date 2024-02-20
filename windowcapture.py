import cv2 as cv
import numpy as np
import win32gui, win32ui, win32con, win32api
from time import time


class WindowCapture:

    # properties
    w = 0
    h = 0
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0
    loop_time = 0

    # constructor
    def __init__(self, window_name):
        # find the handle for the window we want to capture
        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))
            #--add pop up for error--

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

        # set the cropped coordinates offset so we can translate screenshot
        # images into actual screen positions
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

        # starting timer
        loop_time = time()

    def print_fps(self):
        print('FPS {}'.format(1 / (time() - self.loop_time)))
        self.loop_time = time()

    # uses win32 to refresh computer vision
    def update_screenshot(self):

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

        # make image C_CONTIGUOUS to avoid errors that look like:
        #   File ... in draw_rectangles
        #   TypeError: an integer is required (got type tuple)
        # see the discussion here:
        # https://github.com/opencv/opencv/issues/14866#issuecomment-580207109
        img = np.ascontiguousarray(img)

        return img

    # filter images to save memory
    def filter_image(self,img):
        image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        image = cv.GaussianBlur(image, (7,7), 0)
        return image

    # display computer vision for debugging
    def show_image(self, name = 'Computer Vision',img = None, resize_factor = .5,):
        image = cv.resize(img, (0, 0), fx=resize_factor, fy=resize_factor)
        cv.imshow(name, image)

    # draw points
    def draw_points(self, image = None, points = (0,0), marker_color = (0, 255, 0)):
        img = image
        marker_type = cv.MARKER_CROSS
        for (x, y) in points:
            # Draw the center point
            cv.drawMarker(img, (x, y), color = marker_color, markerType = marker_type, markerSize=20, thickness=1)
        return image