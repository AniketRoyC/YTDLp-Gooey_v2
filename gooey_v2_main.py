import yt_dlp
#https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp
# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
import json

from tkinter import *
from tkinter import ttk
# https://tkdocs.com/tutorial/index.html

from datetime import datetime
print(datetime.now()) #going to use this to track time spent downloading.

root = Tk()
label = Label(text="Hello, Tkinter")

root.title('Gooey_v2')

root.mainloop()




# YOUTUBE DL STUFF, DEAL WITH THIS ONCE THE GUI EXISTS
# label.pack()
# URL = input('Enter video URL::\n')


# # https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L180
# ydl_opts = {


# }
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     info = ydl.extract_info(URL, download=False)

#     # ℹ️ ydl.sanitize_info makes the info json-serializable
#     print(json.dumps(ydl.sanitize_info(info)))