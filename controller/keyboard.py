import win32api, win32con
import threading

class Controller:

    # properties
    hwnd = None
    mouse_position = (0,0)


    # constructor
    def __init__(self, hwnd):
        self.hwnd = hwnd