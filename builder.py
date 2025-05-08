import json




with open('trac.json', 'r') as f:
    data = json.load(f)

favs = ["Bijlee Bijlee", "Excuses", "Jhol", "Jugnu", "Pal Pal", "Cheques", "WAVY"]
"""
<div class="card">
    <div class="card-body">
        <h3 class="card-title">Afusic - Pal Pal (Official Music Video) Prod. @AliSoomroMusic</h3>
        <p class="card-subtitle">Synthwave Collective</p>
        <a class="card-play-btn song_play" aria-label="Afusic - Pal Pal (Official Music Video) Prod. @AliSoomroMusic"><i class="fas fa-play-circle"></i></a>
    </div>
</div>
"""

card_favourite_p1 = """<div class="card">
    <div class="card-body">
        <h3 class="card-title">"""

card_favourite_p2 = """</h3>
        <p class="card-subtitle">"""

card_favourite_p3 = """</p>
        <a class="card-play-btn song_play" aria-label='"""

card_favourite_p4 = """'><i class="fas fa-play-circle"></i></a>
    </div>
</div>"""

fav_cards = """"""
for i in range(len(data)):
    if data[i]['title'] in favs:
        card = """"""
        card = card + card_favourite_p1 + data[i]['title'] + card_favourite_p2 + data[i]['artist'] + card_favourite_p3 + data[i]['title'] + card_favourite_p4 + '\n\n'
        fav_cards = fav_cards + card

print(fav_cards)