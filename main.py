from tkinter import *
from typing import Any
import screeninfo

# Global Variables
DEEP_RED = "#B51F09"
MAIN_RED = "#D73c37"
SOFT_RED = "#EE6146"
DEEP_YELLOW = "#DFBC5E"
SOFT_YELLOW = "#E6E0AE"
SW_WIDTH = 750   # Start Window Width
SW_HEIGHT = 400   # Start Window Height

# Get screen width and height
screen = screeninfo.get_monitors()[0]
screen_width = screen.width
screen_height = screen.height

# ___Start window setup___
class Window():
    def __init__(self):
        
        self.root.wm_title("Flashyee Cards")    # Window's titles
        self.root.wm_iconbitmap('images\zhong_favicon.ico')    # Favicon
        self.root.wm_minsize(width=750, height=400)   # Min/Max size of window when compressed
        self.root.wm_maxsize(width=750, height=400)

        self.root.resizable(False, False)    # Not resizable in (Width,Height)
        self.root.config(padx=10, pady=10)   # Padding around the border 

        # Start window launches front and is the topmost window
        self.root.attributes("-topmost", True)
        self.root.attributes("-topmost", False)

        # Centers start window
        x = (screen_width - SW_WIDTH) // 2
        y = (screen_height - SW_HEIGHT) // 2
        self.root.geometry("+{}+{}".format(x, y))

        # Coloring Format
        self.root.config(bg=SOFT_YELLOW)

        # create a frame inside the root window
        self.frame = Frame(self.root, bg="white", borderwidth=2)
        self.label1 = Label(self.frame, text="Label 1")
        self.label1.pack()
        self.label2 = Label(self.frame, text="Label 2")
        self.label2.pack()
        self.frame.pack()

        self.root.mainloop()

Window()




class Window():
    def __init__ (self,master):
        mainframe = tk.Frame(master)
        mainframe.pack(padx=10, payy=10, fill='both', expand=1)
        self.idex = 0

        self.frameList = [FirstWindow(mainframe), SecondWindow(mainframe)]
        self.frameList[1].forget()

        bottomframe = tk.Frame(master)
        bottomframe.pack(padx=10, payy=10)

    def changeWindow(self):
        self.index = (self.index + 1 ) % len(self.frameList)

root = tk.TK()
Window = MainWindow(root)
root.mainloop()