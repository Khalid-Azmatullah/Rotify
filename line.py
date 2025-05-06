import os

folder_path = 'Songs copy'

trim_words = [
    'official video',
    'full video',
    'full video song',
    't-series',
    '(hd)',
    '(song)',
    'song by',
    '(official video)',
    '(live video)',
    '(full video)',
    '(video)',
    '(official music video)',
    'in cinemas',
    '(music video)',
    'music video',
    '()'
]


for filename in os.listdir(folder_path):
    if filename.endswith('.m4a'):
        old_path = os.path.join(folder_path, filename)
        for word in trim_words:
            if word in filename.lower():
                filename = filename.replace(word, '')
        new_filename = filename.strip().capitalize()
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)