def gen_card(type):
    import json

    card_template = ["""<div class="card">
        <div class="card-body">
            <h3 class="card-title">""", """</h3>
            <p class="card-subtitle">""", """</p>
            <a class="card-play-btn song_play" aria-label='""", """'><i class="fas fa-play-circle"></i></a>
        </div>
    </div>"""]

    with open(f'logs/{type}_songs.json', 'r', encoding='utf-8') as file:
        songs = json.load(file)

    build = """"""
    for song in songs:
        card = card_template[0] + song['song_name'] + card_template[1] + song['artist_name'] + card_template[2] + song['song_name'] + card_template[3]
        build = build + '\n' + card

    return build