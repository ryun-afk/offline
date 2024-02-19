import win32gui

def get_active_windows():
    active_windows = []

    # Callback function to enumerate windows
    def enum_windows(hwnd, lParam):
        # Check if the window is visible and has a title
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowTextLength(hwnd) > 0:
            # Get the title of the window
            window_title = win32gui.GetWindowText(hwnd)
            # Append the window handle and title to the list of active windows
            active_windows.append((hwnd, window_title))
        return True

    # Enumerate all top-level windows
    win32gui.EnumWindows(enum_windows, 0)

    return active_windows

# Get a list of active windows
active_windows = get_active_windows()

# Print the list of active windows along with their titles
print("List of Active Windows:")
for hwnd, title in active_windows:
    print(f"Window handle: {hwnd}, Title: {title}")
