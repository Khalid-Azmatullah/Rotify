from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=5Eqb_-j3FDA"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
ys.download(output_path="Songs")