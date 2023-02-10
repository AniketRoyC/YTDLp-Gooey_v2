import tkinter as tk
from tkinter import ttk

from datetime import datetime
print('gooey_v2 - Aniket Roy C')
print(datetime.now()) # could use this to track time spent downloading.

# RANDOM LINKS
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html - tkinter 8.5 reference, includes ttk stuff
# https://www.pythontutorial.net/tkinter/tkinter-grid/ - explanation of grid stuff (including pictures!)


### WIDGET FUNCTIONS ===




### TTK STYLES







### WIDGETS

root = tk.Tk()
root.title('Gooey_v2 - GUI only')
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

    # The 'root' window is the one that is the so-called 'toplevel'.
    # It is best practice to add a frame within the 'root' and just have that inhabit the entire space.
    # mainframe is a frame in location (0,0) of 'root'
    # row and column 0 of 'root' have been set to resize automatically with the window. (see above)

#TODO add icon photo.
# titlebar_icon = tk.PhotoImage(Im "WEBall.png")
# root.iconphoto(True, titlebar_icon)

#=========================================================================
### MAINFRAME
mainframe = ttk.Frame(root, padding='10 10 10 10')
mainframe.grid(row=0, column=0, sticky=(tk.N, tk.E, tk.W, tk.S))

mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

## INITIAL OPTIONS LABELFRAME
# this labelframe is in (0,0) of 'mainframe'
InitOpts_labelframe = ttk.Labelframe(mainframe, text = 'Initial Options', padding='3 3 3 3')
InitOpts_labelframe.grid(column=0, row=0, sticky = (tk.N, tk.W, tk.E))

InitOpts_labelframe.columnconfigure(1, weight=6)

#URL entrybox label
URL_entry_label = ttk.Label(InitOpts_labelframe, text = 'Video URL: ')
URL_entry_label.grid(row=0, column=0)

#URL entrybox
URL = tk.StringVar()
URL_entry = ttk.Entry(InitOpts_labelframe, width = 25, textvariable=URL)
URL_entry.grid(row = 0, column= 1, sticky = (tk.N, tk.W, tk.E))
URL_entry.focus()


for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)


root.mainloop()
