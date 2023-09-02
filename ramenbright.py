import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import shutil
import os

MONITOR_INDEX = 0
MIN_BRIGHTNESS_SCALE = 1

VERSION = "1.0.1"

RAMEN_FILE = os.path.join(os.path.dirname(__file__), "ramen.jpg")

class App(tk.Tk):
    def __init__(self, monitor_name: str, current_brightness: float = 1.0):
        super().__init__()
        self.title(f"RamenBright {VERSION} by CAS")
        self.resizable(0, 0)

        self.monitor_name = monitor_name

        self.slider = ttk.Scale(self, from_=MIN_BRIGHTNESS_SCALE, to=20, command=self.set_brightness)
        self.slider.set(int(current_brightness * 20))
        
        ramen_image = Image.open(RAMEN_FILE)
        ramen_image = ramen_image.resize((200, 200))
        ramen_image_tk = ImageTk.PhotoImage(ramen_image)

        label_min = ttk.Label(self, text="0%")
        label_max = ttk.Label(self, text="100%")
        self.label_brightness = ttk.Label(self, text=f"Brightness: {int(current_brightness * 100)}%")
        label_ramen = ttk.Label(self, image=ramen_image_tk)

        label_ramen.grid(row=1, column=4, rowspan=2, padx=(0, 50), pady=20)
        label_min.grid(row=1, column=1, padx=(50, 0))
        self.slider.grid(row=1, column=2, padx=5)
        label_max.grid(row=1, column=3, padx=(0, 20))
        self.label_brightness.grid(row=2, column=1, columnspan=3)

    def set_brightness(self, *args):
        new_brightness = self.slider.get() / 20
        subprocess.getoutput(f"xrandr --output {self.monitor_name} --brightness {new_brightness}")
        self.label_brightness.config(text=f"Brightness: {int(new_brightness * 100)}%")

def main():
    if shutil.which("xrandr") and subprocess.getoutput("xrandr"):
        brightness = float(subprocess.getoutput("xrandr --verbose | grep rightness").strip().split(": ")[1])
        if brightness is None:
            brightness = 1.0

        monitors = subprocess.getoutput("xrandr --listmonitors").splitlines()[1:]
        monitor_name = monitors[MONITOR_INDEX].strip().split()[-1]
        
        app = App(monitor_name, brightness)
        app.mainloop()
    
    else:
        print("You must have xrandr installed (sudo apt install x11-server-utils) to use this program.")

if __name__ == "__main__":
    main()