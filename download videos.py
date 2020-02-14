
import youtube_dl as youtube_dl

Path = "C:/Users/Cipher/Desktop/mm/New folder"
Location = '%s \%(extractor)s-%(id)s-%(title)s.%(ext)s'.replace("%s ", Path)
ytdl_format_options = {
'outtmpl': Location
}

with youtube_dl.YoutubeDL(ytdl_format_options) as ydl:
     ydl.download(['https://www.youtube.com/watch?v=bNd5xfqVw1M'])
