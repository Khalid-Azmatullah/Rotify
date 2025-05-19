import json

def remove_duplicates_by_key(lst, key, key_sec=None):
    if key_sec is None:
        seen = set()
        result = []
        for d in lst:
            value = d.get(key)
            if value not in seen:
                seen.add(value)
                result.append(d)
        return result
    else:
        seen = set()
        result = []
        for d in lst:
            value = (d.get(key), d.get(key_sec))
            if value not in seen:
                seen.add(value)
                result.append(d)
        return result

with open('logs/song.json', 'r', encoding='utf-8') as file:
    log = json.load(file)

log = remove_duplicates_by_key(log, "url")
log = remove_duplicates_by_key(log, "song_name", key_sec="artist_name")

with open('logs/song.json', 'w', encoding='utf-8') as file:
    json.dump(log, file,indent=4)