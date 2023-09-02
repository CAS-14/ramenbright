from tkinter import messagebox as tkmb
import os
import random

import ramenbright

RAMEN_DIR = os.path.join(os.path.expanduser("~"), ".anyramen")

def run():
    if not os.path.isdir(RAMEN_DIR):
        tkmb.showerror(title="No directory!", message="You must create a directory .anyramen in your home directory, and put images in it!")

    else:
        ramen_files = [filename for filename in os.listdir(RAMEN_DIR) if os.path.isfile(os.path.join(RAMEN_DIR, filename))]
        if not ramen_files:
            tkmb.showerror(title="No files!", message="Directory .anyramen detected, but no images in it! Please fix this!")

        else:
            ramenbright.VERSION += "a1"
            ramenbright.RAMEN_FILE = random.choice(ramen_files)
            ramenbright.main()