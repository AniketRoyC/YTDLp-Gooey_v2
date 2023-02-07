import yt_dlp
    #https://github.com/yt-dlp/yt-dlp#embedding-yt-dlp
    # ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')

##=========================================================================
ytdl_AUDonly = {
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '192',
    #TODO add a way for user to specify ffmpeg location '--ffmpeg-location'
}
ytdl_regular = {
    'key': 'FFmpegVideoConvertor',
    "preferedformat" : "mp4",
    #TODO add a way for user to specify ffmpeg location '--ffmpeg-location'
}


# https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L180
ydl_opts = {
    'postprocessors': [],
     'progress_hooks' : [my_hook]
}
# https://www.youtube.com/watch?v=jslGE6p0nj4 using this link for testing.
def run_ytdl():
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # info = ydl.extract_info(URL, download=False)

        # # ℹ️ ydl.sanitize_info makes the info json-serializable
        # print(json.dumps(ydl.sanitize_info(info)))
        ydl.download([URL])

URL = input('Enter a video URL here::\n')
if input('Extract audio only? (y/n)::\n') == 'y':
    ydl_opts['postprocessors'] = [ytdl_AUDonly]
    print('Using Audio Only Postprocessor Arguments...')
else:
    ydl_opts['postprocessors'] = [ytdl_regular]
    print('Using Regular PostProcessor Arguments...')

if input('Start with (B)est formats or (D)efault yt-dlp formats?::\n ') == 'B':
    ydl_opts['format'] = 'bv*+ba/b'
        #https://github.com/yt-dlp/yt-dlp/blob/7aefd19afed357c80743405ec2ace2148cba42e3/yt_dlp/YoutubeDL.py#L209
else:
    pass

run_ytdl()