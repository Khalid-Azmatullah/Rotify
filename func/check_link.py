def check_if_playlist(url):
    if url.startswith('https://youtu.be/'):
        return False
    elif url.startswith('https://youtube.com/playlist?'):
        return True
    else:
        return 0