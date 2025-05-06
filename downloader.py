from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix import Playlist
import os

urls = ["https://youtu.be/8of5w7RgcTc?si=pZjOHZ_d_S25mQEz", 
        "https://youtu.be/Y2lWEVyO-qE?si=HAJoclIRpBd2ERD2", 
        "https://youtu.be/NwdQx2P_ytk?si=9es2RcKDFF02Q3-b", 
        "https://youtu.be/vX2cDW8LUWk?si=lZsSYwGBcg4J2xYZ", 
        "https://youtu.be/0pWsCiBvLOk?si=T7nkRhkd-uCx9GBn", 
        "https://youtu.be/-2RAq5o5pwc?si=thQk8MKQvDIjUeFc", 
        "https://youtu.be/AKH6ZNSnWOA?si=KeCHfK_Ob3BAwQTB", 
        "https://youtu.be/4tywp83zkmk?si=tKH2b6ovj1G7tDoa",
        "https://youtu.be/XTp5jaRU3Ws?si=7L9Agj05RsK5fjfF"  
    ]


# playlist_url = "https://youtube.com/playlist?list=PLttkmJc3m9Muf1yJ_1nGqCxBrhEJZPvFh&si=pk4kw5G099uPSCOg"

# # Initialize the Playlist object
# playlist = Playlist(playlist_url)

# # Download audio from each video in the playlist
# for video in playlist.videos:
#     video.register_on_progress_callback(on_progress)
#     audio_stream = video.streams.filter(only_audio=True).order_by('abr').desc().first()
#     audio_stream.download(output_path="Songs")




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
    audio_list= audio_list + '{ src:"' + file + '", title:"' + os.path.splitext(file)[0] + '", artist:"Unkown"}, '

files = [os.path.splitext(file)[0] for file in files]

# print(files)

builder_list = ['s1.txt', 's3.txt', 's5.txt']
build =[]
for tst in builder_list:
    with open(f'builder/{tst}', 'r') as f:
        build.append(f.read())



menu = ''
for song in files:
    menu = menu + '<div class="menuitem" id="' + song + '">' + song + '</div> \n'

# print(build[0])
full_build = build[0] + menu + build[1] + audio_list + build[2]

with open('index0.html', '+w', encoding='utf-8') as f:
    f.writelines(full_build)



    

