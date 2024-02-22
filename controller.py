import win32api, win32con
import threading

class Controller:

    # properties
    keyboard = None
    mouse = None
    mouse_position = (0,0)


    # constructor
    def __init__(self):
        self.keyboard = None