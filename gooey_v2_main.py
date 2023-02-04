#IMPORTS==================================================================
import yt_dlp
#https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp
# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
import json

from tkinter import *
from tkinter import ttk
# https://tkdocs.com/tutorial/index.html

from datetime import datetime
print(datetime.now()) #going to use this to track time spent downloading.

#=========================================================================
#Logger for intercepting output:
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

##=========================================================================
vibecheck = {
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '192',
}



# https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L180
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [],
    'logger' : MyLogger(),
    'progress_hooks' : [my_hook],
}





def run_ytdl():
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # info = ydl.extract_info(URL, download=False)

        # # ℹ️ ydl.sanitize_info makes the info json-serializable
        # print(json.dumps(ydl.sanitize_info(info)))
        ydl.download([URL])

def XAUD_changed():
    ydl_opts['postprocessors'] = vibecheck



root = Tk() #base window
root.title('Gooey_v2 - Main')

mainframe = ttk.Frame(root, padding = '3 3 12 12') #main frame in the 'root' window
mainframe.grid(column = 0, row = 0, sticky=(N,W,E,S)) #grid within the main frame

#expand the frame to fill any extra space on re-size:
root.columnconfigure([1,2], weight = 1)
root.rowconfigure(0, weight = 1)





#INPUT - URL Entry
URL_label = ttk.Label(mainframe, text = 'Video URL:')
URL_label.grid(column = 1, row = 1, sticky = W)

URL = StringVar()
URL_entry = ttk.Entry(mainframe, width = 25, textvariable = URL)
URL_entry.grid(column = 2, row = 1, sticky = (W,E))
URL_entry.focus()

#EXTRACT AUDIO - Checkbox for Audio Only
XAUD = StringVar()
XAUD_check = ttk.Checkbutton(mainframe, text = 'Audio Only',
                            variable = XAUD, command=XAUD_changed,
                            onvalue = 'XAUD_on', offvalue = 'XAUD_off')
XAUD_check.grid(column = 3,row = 1, sticky = E)


#RUN - Button to run ytdlp
RUN_button = ttk.Button(mainframe, text = 'Run ytdlp', command = run_ytdl)
RUN_button.grid(column = 3, row = 3, sticky = W)


#Padding every widget at once (if no custom padding is needed)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()