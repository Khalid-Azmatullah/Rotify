from func.gen import gen_card
from func.gen_search import build_search_card
import song_manager

full_build = """"""
print("Downloaded Songs Successfully!")
cards_build_sequence = ['favs', 'tops', 'underdogs']

for i in range(1, 4):
    print(i)
    with open(f'Build/default_build_{i}.txt', 'r', encoding='utf-8') as file:
        template = file.read()
    
    full_build = full_build + template + gen_card(cards_build_sequence[i-1]) + '\n'

with open(f'Build/default_build_4.txt', 'r', encoding='utf-8') as file:
    template = file.read()

full_build = full_build + template + build_search_card()

with open(f'Build/default_build_5.txt', 'r', encoding='utf-8') as file:
    template = file.read()

full_build = full_build + template

with open('temp.html', 'w', encoding='utf-8') as file:
    file.write(full_build)

trash = input('DEFAULT: Check `temp.html` and confirm with `Y`')

if trash == '':
    exit
elif trash == 'Y' or trash == 'y':
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(full_build)