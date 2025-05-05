from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

urls = ["https://youtu.be/XTp5jaRU3Ws?si=7L9Agj05RsK5fjfF"]

for url in urls:
    yt = YouTube(url, on_progress_callback=on_progress)
    
    print(yt.title)

    ys = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    ys.download(output_path="Songs")

directory = 'Songs'

# List all files (and directories) in the specified directory
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

audio_list = ''
for file in files:
    audio_list= audio_list + f'\'{file}\','

files = [os.path.splitext(file)[0] for file in files]

print(files)

builder_list = ['s1.txt', 's3.txt', 's5.txt']
build =[]
for tst in builder_list:
    with open(f'builder/{tst}', 'r') as f:
        build.append(f.read())



menu = ''
for song in files:
    menu = menu + '<div class="menuitem" id="#' + song + '">' + song + '</div> \n'

print(build[0])
full_build = build[0] + menu + build[1] + audio_list + build[2]

with open('index0.html', '+w') as f:
    f.writelines(full_build)



    

