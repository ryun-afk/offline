import keyboard
import time

class KeyboardCapture:
    
    # properties
    hwnd = None
    move_forward = 'w'
    move_back = 's'
    move_left = 'a'
    move_right = 'd'
    keyboard_action = 'e'
    object_targeting = 'q'

    def __init__(self):
        self.hwnd = None

    def on_key_event(self,event):
        if event.event_type == keyboard.KEY_DOWN:
            print(f"Key {event.name} pressed")

    def record_keyboard(self):
        keyboard.on_press(self.on_key_event)
        keyboard.on_release(self.on_key_event)

    def send_key(self,key, delay = .1):
        keyboard.press(key)
        time.sleep(delay)
        keyboard.release(key)

        
