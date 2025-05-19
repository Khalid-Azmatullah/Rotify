def format_duration(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}:{remaining_seconds:02}"

def build_search_card():
    import json
    with open(f'logs/tops_songs.json', 'r', encoding='utf-8') as file:
        top_songs = json.load(file)
    
    i = 0
    build = """"""
    for song in top_songs:
        i += 1
        card_template = f""" 
            <div class="song-item" data-id="{song['song_name']}">
                <span class="song-index">{i}</span>
                <div class="song-info">
                    <div class="song-title">{song['song_name']}</div>
                    <div class="song-artist">{song['artist_name']}</div>
                </div>
                <div class="song-duration">{format_duration(song['duration'])}</div>
            </div>"""
        build = build + card_template + '\n'

    return build
    
