from __future__ import unicode_literals
#спасибо папаша
import youtube_dl
x = input("  ССылка на видео:")
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #скачивание
    ydl.download([x])
    print("Видео успешно скачано!")
