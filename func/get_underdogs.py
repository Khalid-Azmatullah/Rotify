def remove_duplicates_by_key(lst, key):
    seen = set()
    result = []
    for d in lst:
        value = d.get(key)
        if value not in seen:
            seen.add(value)
            result.append(d)
    return result

def load_underdogs():
    import json

    with open('logs/song.json', 'r', encoding='utf-8') as file:
        song_data = json.load(file)
    
    bottom_list = sorted(song_data, key=lambda x: x.get("views", None), reverse=False)
    seen = set()
    bottom_list = [d for d in bottom_list if tuple(sorted(d.items())) not in seen and not seen.add(tuple(sorted(d.items())))]
    bottom_list = remove_duplicates_by_key(bottom_list, 'url')


    bottom_list = bottom_list[:10]

    with open('logs/underdogs_songs.json', 'r', encoding='utf-8') as file:
        underdogs_song_data = json.load(file)
    
    new_underdogs_list = bottom_list + underdogs_song_data

    new_underdogs_list = sorted(new_underdogs_list, key=lambda x: x.get("views", None), reverse=False)
    seen = set()

    new_underdogs_list = [d for d in new_underdogs_list if tuple(sorted(d.items())) not in seen and not seen.add(tuple(sorted(d.items())))]
    new_underdogs_list = remove_duplicates_by_key(new_underdogs_list, 'url')

    new_underdogs_list = new_underdogs_list[:10]

    with open('logs/underdogs_songs.json', 'w', encoding='utf-8') as file:
        json.dump(new_underdogs_list, file, indent=4)