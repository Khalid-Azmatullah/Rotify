from youtube_title_parse import get_artist_title
import os

directory = 'Songs'

# List all files (and directories) in the specified directory
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
files = [os.path.splitext(file)[0] for file in files]

for file in files:
    video_title = file
    print(video_title)
    artist, song = get_artist_title(video_title)
    print(song)
