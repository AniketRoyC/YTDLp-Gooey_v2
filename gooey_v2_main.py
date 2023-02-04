import yt_dlp
#https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp
# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
import json

from tkinter import *
from tkinter import ttk
# https://tkdocs.com/tutorial/index.html

from datetime import datetime
print(datetime.now()) #going to use this to track time spent downloading.

root = Tk() #base window
root.title('Gooey_v2 - Main')

mainframe = ttk.Frame(root, padding = '3 3 12 12') #main frame in the 'root' window
mainframe.grid(column = 0, row = 0, sticky=(N,W,E,S)) #grid within the main frame

#expand the frame to fill any extra space on re-size:
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
label = Label(text="Hello, Tkinter")



#INPUT - URL Entry
URL_label = ttk.Label(mainframe, text = "Video URL")
URL_label.grid(column = 1, row = 1, sticky = W, padx = 5, pady = 5)

URL = StringVar()
URL_entry = ttk.Entry(mainframe, width = 25, textvariable = URL)
URL_entry.grid(column = 2, row = 1, sticky = (W,E), padx = 5, pady = 5)

URL_entry.focus()


root.mainloop()


#Padding every widget at once (if no custom padding is needed)
# for child in mainframe.winfo_children(): 
#     child.grid_configure(padx=5, pady=5)



# YOUTUBE DL STUFF, DEAL WITH THIS ONCE THE GUI EXISTS


# # https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L180
# ydl_opts = {


# }
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     info = ydl.extract_info(URL, download=False)

#     # ℹ️ ydl.sanitize_info makes the info json-serializable
#     print(json.dumps(ydl.sanitize_info(info)))