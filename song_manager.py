"""
SONG_MANAGER.PY

Beta build for Rotify Music logs. More robust solution to original downloader.py 

Playlists:
https://youtube.com/playlist?list=PLttkmJc3m9Muf1yJ_1nGqCxBrhEJZPvFh&si=pk4kw5G099uPSCOg
https://youtube.com/playlist?list=PLttkmJc3m9Mvd8HjlcMplqzs1j9Fyo88I&si=s64quuoqGPluzkk-

Urls:
https://youtu.be/8of5w7RgcTc?si=pZjOHZ_d_S25mQEz 
https://youtu.be/Y2lWEVyO-qE?si=HAJoclIRpBd2ERD2
https://youtu.be/NwdQx2P_ytk?si=9es2RcKDFF02Q3-b
https://youtu.be/vX2cDW8LUWk?si=lZsSYwGBcg4J2xYZ
https://youtu.be/0pWsCiBvLOk?si=T7nkRhkd-uCx9GBn
https://youtu.be/-2RAq5o5pwc?si=thQk8MKQvDIjUeFc
https://youtu.be/AKH6ZNSnWOA?si=KeCHfK_Ob3BAwQTB
https://youtu.be/4tywp83zkmk?si=tKH2b6ovj1G7tDoa
https://youtu.be/XTp5jaRU3Ws?si=7L9Agj05RsK5fjfF
"""

"""
STEPS:

=> Load all the Url(s) for the songs or Playists in the new-arc.txt file.
=> Make sure all the links are valid Youtube originating urls.
=> Run song_manager.py, this adds the song(s) to the running directory.
"""

"""
Import Dependencies:

=> func.check_link
=> pytubefix
=> pytubefix.cli
=> json
=> func.rem_dup
=> pytubefix.exceptions
=> func.clear_cache
=> func.get_song_artist
=> re
=> func.get_favs
=> func.get_tops
=> func.get_underdogs
=> func.get_likes
"""

from func.check_link import check_if_playlist
from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress
import json
from func.rem_dup import remove_duplicates
from pytubefix.exceptions import VideoUnavailable
from func.clear_cache import clear_cache
from func.get_song_artist import get_song_artist
import re
from func.get_favs import load_favs
from func.get_tops import load_tops
from func.get_underdogs import load_underdogs
from func.get_likes import likes

# GET URL(S)
with open('new-arc.txt', 'r', encoding='utf-8') as file:
    link_list = file.readlines()

parsed_link_list = []
for link_s in link_list:
    val = check_if_playlist(link_s)
    if val:
        p = Playlist(link_s)
        for url in p.video_urls:
            parsed_link_list.append(url)
    elif not val:
        parsed_link_list.append(link_s)
    else:
        print(f'Rejected: {link_s}')

parsed_link_list = remove_duplicates(parsed_link_list)

with open('logs/url-log.json', 'r', encoding='utf-8') as file:
    link_log = json.load(file)

parsed_link_list = [link for link in parsed_link_list if YouTube(link).video_id not in link_log]

log = link_log + [YouTube(id).video_id for id in parsed_link_list]

with open('logs/url-log.json', 'w', encoding='utf-8') as file:
    json.dump(log, file,indent=4)


# DOWNLOAD SONGS
profile_s = []
# print(parsed_link_list)
lent = len(parsed_link_list)
i = 0
for url in  parsed_link_list:
    i += 1
    build_bod = {
        "url": "https://youtu.be/XXXXXXXXXXX?si=x0x0x0x0x0x0x0x0",
        "title": "Olympus - The Morning Benders",
        "duration": 180,
        "song_name": "Olympus",
        "artist_name": "The Morning Benders" ,
        "views": 100000000,
        "ratio": 0.5
    }



    try:
        yt = YouTube(url, on_progress_callback=on_progress)
    except VideoUnavailable:
        continue

    build_bod['url'] = yt.video_id

    build_bod["title"] = yt.title
    build_bod["duration"] = yt.length
    build_bod["views"] = yt.views
    build_bod["ratio"] = (int(likes(yt.video_id)) / (yt.views))

    song_metadata = get_song_artist(yt.title)

    build_bod["song_name"] = re.sub(r"^[#%&{}\[\]\|\\<>?:;!'\"@+=\$~]" , '', song_metadata[0])
    build_bod["artist_name"] = song_metadata[1].splitlines()[0]

    ys = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    ys.download(output_path="Songs", filename=f'{build_bod["song_name"]}.m4a')
    print(f'Downloaded: {build_bod['song_name']}')
    print(f'Remaining: {i}/{lent}')

    profile_s.append(build_bod)

with open('logs/song.json', 'r', encoding='utf-8') as file:
    song_s_metadata = json.load(file)

song_s_metadata_new = song_s_metadata + profile_s

with open('logs/song.json', 'w', encoding='utf-8') as file:
    json.dump(song_s_metadata_new, file, indent=4)

load_favs()
print('Loaded Favourite Songs')
load_tops()
print('Loaded Top Songs')
load_underdogs()
print('Loaded Underdogs')

clear_cache()