import yt_dlp
    #https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp
    # ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions

##=========================================================================
ytdl_AUDonly = {
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '192',
}



# https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L180
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [],
     #TODO add a way for user to specify ffmpeg location '--ffmpeg-location'
}
# https://www.youtube.com/watch?v=dQw4w9WgXcQ
def run_ytdl():
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # info = ydl.extract_info(URL, download=False)

        # # ℹ️ ydl.sanitize_info makes the info json-serializable
        # print(json.dumps(ydl.sanitize_info(info)))
        ydl.download([URL])

URL = input('Enter a video URL here::\n')
if input('Extract audio only? (y/n)::\n') == 'y':
    ydl_opts['postprocessors'] = [ytdl_AUDonly]
else:
    Aud_only = False


run_ytdl()