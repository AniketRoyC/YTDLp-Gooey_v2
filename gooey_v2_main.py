#IMPORTS==================================================================
    # import yt_dlp
    # #https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp
    # # ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
    # import json

from tkinter import *
from tkinter import ttk
# https://tkdocs.com/tutorial/index.html

from datetime import datetime
print('gooey_v2 - Aniket Roy C')
print(datetime.now()) #going to use this to track time spent downloading.

#=========================================================================
    # #Logger for intercepting output:
    # class MyLogger(object):
    #     def debug(self, msg):
    #         pass

    #     def warning(self, msg):
    #         pass

    #     def error(self, msg):
    #         print(msg)

    # def my_hook(d):
    #     if d['status'] == 'finished':
    #         print('Done downloading, now converting ...')

##=========================================================================
    # ytdl_AUDonly = {
    #     'key': 'FFmpegExtractAudio',
    #     'preferredcodec': 'mp3',
    #     'preferredquality': '192',
    # }

    # # https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L180
    # ydl_opts = {
    #     'format': 'bestaudio/best',
    #     'postprocessors': [],
    #     'logger' : MyLogger(),
    #     'progress_hooks' : [my_hook],
    # }
# WIDGET FUNCTIONS =======================================================
def RUN_button_func():
    print('Button pressed:: run_ytdl')
# WISHFUL THINKING:
    # UPDATE POSTPROCESSOR ARGUMENTS
    # UPDATE YTDL OPTIONS
    # RUN YTDL

    #     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #         # info = ydl.extract_info(URL, download=False)

    #         # # ℹ️ ydl.sanitize_info makes the info json-serializable
    #         # print(json.dumps(ydl.sanitize_info(info)))
    #         ydl.download([URL])

def XAUD_changed(): #runs every time the "Audio Only" checkbox is toggled
# WISHFUL THINKING:
# SWITCHES POSPTORCESSOR OPTIONS BETWEEN AUDIO AND VIDEO VERSIONS
# SWITCHES YTDL OPTIONS BETWEEN AUDIO AND VIDEO VERSIONS

    #ydl_opts['postprocessors'] = ytdl_AUDonly
    if XAUD.get():print('Checkbox:: Audio-only enabled')
    else: print('Checkbox:: Audio-only disabled')

# WIDGETS ================================================================
root = Tk() #base window
root.title('Gooey_v2 - Main')

#expand the frame to fill any extra space on re-size:
root.columnconfigure([1,2], weight = 1, )
root.rowconfigure(0, weight = 1)
root.configure(background='blue')
#https://stackoverflow.com/questions/54476511/setting-background-color-of-a-tkinter-ttk-frame


mainframe = ttk.Frame(root, padding = '3 3 12 12') #main frame in the 'root' window

mainframe.grid(column = 0, row = 0, sticky=(N,W,E,S)) #grid within the main frame



#INPUT - URL Entry
URL_label = ttk.Label(mainframe, text = 'Video URL:')
URL_label.grid(column = 1, row = 1, sticky = W)

URL = StringVar()
URL_entry = ttk.Entry(mainframe, width = 25, textvariable = URL)
URL_entry.grid(column = 2, row = 1, sticky = (W,E))
URL_entry.focus()

#EXTRACT AUDIO - Checkbox for Audio Only
XAUD = IntVar()
XAUD_check = ttk.Checkbutton(mainframe, text = 'Download Audio Only',
                            variable = XAUD, command=XAUD_changed,
                            onvalue = 1, offvalue = 0)
XAUD_check.grid(column = 3,row = 1, sticky = E)


#RUN - Button to run ytdlp
RUN_button = ttk.Button(mainframe, text = 'Run ytdlp', command = RUN_button_func)
RUN_button.grid(column = 6, row = 30, sticky = W)
    #TODO - make this the bottom button always.


#FORMATTING-BY-FRAME =====================================================
#Padding every widget at once (if no custom padding is needed)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()