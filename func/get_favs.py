def remove_duplicates_by_key(lst, key):
    seen = set()
    result = []
    for d in lst:
        value = d.get(key)
        if value not in seen:
            seen.add(value)
            result.append(d)
    return result

def load_favs():
    import json

    with open('logs/song.json', 'r', encoding='utf-8') as file:
        song_data = json.load(file)
    
    fav_list = sorted(song_data, key=lambda x: x.get("ratio", None), reverse=True)
    seen = set()

    fav_list = [d for d in fav_list if tuple(sorted(d.items())) not in seen and not seen.add(tuple(sorted(d.items())))]
    fav_list = remove_duplicates_by_key(fav_list, 'url')

    fav_list = fav_list[:10]

    with open('logs/favs_songs.json', 'r', encoding='utf-8') as file:
        fav_song_data = json.load(file)
    
    new_fav_list = fav_list + fav_song_data

    new_fav_list = sorted(new_fav_list, key=lambda x: x.get("ratio", None), reverse=True)
    seen = set()

    new_fav_list = [d for d in new_fav_list if tuple(sorted(d.items())) not in seen and not seen.add(tuple(sorted(d.items())))]
    new_fav_list = remove_duplicates_by_key(new_fav_list, 'url')

    new_fav_list = new_fav_list[:10]

    with open('logs/favs_songs.json', 'w', encoding='utf-8') as file:
        json.dump(new_fav_list, file, indent=4)
