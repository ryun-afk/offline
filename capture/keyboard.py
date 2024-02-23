import keyboard

class KeyboardCapture:
    
    # properties
    hwnd = None

    def __init__(self):
        self.hwnd = None

    # Define a callback function to handle keyboard events
    def on_key_event(self,event):
        if event.event_type == keyboard.KEY_DOWN:
            print(f"Key {event.name} pressed")
        elif event.event_type == keyboard.KEY_UP:
            print(f"Key {event.name} released")

    def record_keyboard(self):
        # Register the callback function for keyboard events
        keyboard.on_press(self.on_key_event)
        keyboard.on_release(self.on_key_event)


