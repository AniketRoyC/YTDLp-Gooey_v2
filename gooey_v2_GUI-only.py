import tkinter as tk
from tkinter import ttk

from datetime import datetime

# RANDOM LINKS
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html - tkinter 8.5 reference, includes ttk stuff
# https://www.pythontutorial.net/tkinter/tkinter-grid/ - explanation of grid stuff (including pictures!)
# https://python-forum.io/thread-755.html - pretty detailed tutorial on a forum, including screenshots, etc.
# https://stackoverflow.com/questions/3316882/how-do-i-get-a-string-format-of-the-current-date-time-in-python - python date-time basic stuff
### MISC
date_string = '{:%Y-%m-%d}'.format(datetime.now())


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
URL_entry.grid(row = 0, column= 1, columnspan=5, sticky = (tk.N, tk.W, tk.E))
URL_entry.focus()


for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

## RUN BUTTON LABELFRAME
#this labelframe is always the bottom of 'mainframe'
RunButton_labelframe = ttk.LabelFrame(mainframe, padding = '3 3 3 3')
RunButton_labelframe.grid(column = 0, row = 100, sticky=(tk.S, tk.W, tk.E))

RunButton_labelframe.columnconfigure(1, weight=1)

#RUN - Button to run ytdlp
RUN_button = ttk.Button(RunButton_labelframe, text = 'Run ytdlp')#, command = RUN_button_func)
RUN_button.grid(column = 1, row = 0, sticky = (tk.E, tk.S, tk.N))
 
#BOTTOMTEXT - other info to throw in for the culture.
RUN_label_text = '(Badly) made by Aniket Roy C | ' + str(date_string)
RUN_label = ttk.Label(RunButton_labelframe, text = RUN_label_text )
RUN_label.grid(column = 0, row = 0, sticky = (tk.W, tk.S, tk.N))


root.mainloop()
