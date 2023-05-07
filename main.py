from tkinter import *
import screeninfo


# Global Variables
DEEP_RED = "#B51F09"
MAIN_RED = "#D73c37"
SOFT_RED = "#EE6146"
DEEP_YELLOW = "#DFBC5E"
SOFT_YELLOW = "#E6E0AE"

# Get screen width and height
screen = screeninfo.get_monitors()[0]
screen_width = screen.width
screen_height = screen.height

# ___Start window setup___
start_window = Tk()
start_window.wm_title("Flashyee Cards")    # Window's titles
start_window.wm_iconbitmap('images\zhong_favicon.ico')    # Favicon
start_window.wm_geometry("800x600")   # Size of the window at startup
start_window.wm_minsize(width=750, height=400)   # Minimum size of window when compressed
start_window.wm_maxsize(width=750, height=400)
start_window.resizable(False, False)    # Not resizable in (Width,Height)
start_window.config(padx=100, pady=200)   # Pading around the boarder 

# Start window launches front and is the topmost window
start_window.attributes("-topmost", True)
start_window.attributes("-topmost", False)

# Possible centering code, doesnt work well with the window startup geometry
x = (screen_width - start_window.winfo_reqwidth()) // 2
y = (screen_height - start_window.winfo_reqheight()) // 2
start_window.geometry("+{}+{}".format(x, y))


start_window.mainloop()