def remove_duplicates_by_key(lst, key):
    seen = set()
    result = []
    for d in lst:
        value = d.get(key)
        if value not in seen:
            seen.add(value)
            result.append(d)
    return result

def load_tops():
    import json

    with open('logs/song.json', 'r', encoding='utf-8') as file:
        song_data = json.load(file)
    
    top_list = sorted(song_data, key=lambda x: x.get("views", None), reverse=True)
    top_list = remove_duplicates_by_key(top_list, 'url')
    top_list = top_list[:10]

    with open('logs/tops_songs.json', 'r', encoding='utf-8') as file:
        top_song_data = json.load(file)
    
    new_top_list = top_list + top_song_data

    new_top_list = sorted(new_top_list, key=lambda x: x.get("views", None), reverse=True)
    new_top_list = remove_duplicates_by_key(new_top_list, 'url')

    new_top_list = new_top_list[:10]

    with open('logs/tops_songs.json', 'w', encoding='utf-8') as file:
        json.dump(new_top_list, file, indent=4)