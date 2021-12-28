import sys
v = sys.version

if "2.7" in v:
    from Tkinter import *
else:
    from tkinter import *

root = Tk("Text Editor")

root.mainloop()
