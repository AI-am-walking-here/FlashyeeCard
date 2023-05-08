from tkinter import *
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
start_window = Tk()
start_window.wm_title("Flashyee Cards")    # Window's titles
start_window.wm_iconbitmap('images\zhong_favicon.ico')    # Favicon
start_window.wm_minsize(width=750, height=400)   # Min/Max size of window when compressed
start_window.wm_maxsize(width=750, height=400)

start_window.resizable(False, False)    # Not resizable in (Width,Height)
start_window.config(padx=100, pady=200)   # Pading around the boarder 

# Start window launches front and is the topmost window
start_window.attributes("-topmost", True)
start_window.attributes("-topmost", False)

# Centers start window
x = (screen_width - SW_WIDTH) // 2
y = (screen_height - SW_HEIGHT) // 2
start_window.wm_geometry("+{}+{}".format(x, y))

# Coloring Format
start_window.config(bg=SOFT_YELLOW)

class Window():
    pass













start_window.mainloop()