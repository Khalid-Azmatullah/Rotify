import os
from dotenv import load_dotenv
import time
import json

load_dotenv()
google_api_key = os.getenv('GOOGLE_API')

import google.generativeai as genai
genai.configure(api_key=google_api_key)

model = genai.GenerativeModel('gemini-2.0-flash-lite')
start_time = time.time()

directory = 'Songs'
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
files = [os.path.splitext(file)[0] for file in files]

tracks = []
i = 0
for file_index in range(len(files)):
    if file_index > (15 + 15*i) and time.time() - (start_time + 60*i) < 60:
        print('waiting')
        time.sleep(61 - time.time() + start_time)
        i+=1
        start_time = time.time()
    response = model.generate_content(f'The following is a title of a youtube video, you MUST reply with its EXACT song name and artist name is the format: <song_name> / <artist_name>. DO NOT USE ANY OTHER FORMAT OTHER THAN THIS. This is the file: {files[file_index]}')
    print(response.text, '\n')
    song_name = response.text.split('/')[0].strip()
    artist = response.text.split('/')[1].strip()
    os.rename(f'Songs/{files[file_index]}.m4a', f'Songs/{song_name}.m4a')
    tracks.append(
        {
            'src': f'Songs/{song_name}.m4a',
            'title': song_name,
            'artist': artist
        }
    )
    with open('trac.json', 'w+') as f:
        json.dump(tracks, f, indent=4)
