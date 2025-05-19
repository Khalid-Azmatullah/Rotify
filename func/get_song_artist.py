def get_song_artist(video_title):
    import os
    from dotenv import load_dotenv
    import google.generativeai as genai
    import time

    load_dotenv()
    google_api_key = os.getenv('GOOGLE_API')

    time.sleep(4)
    genai.configure(api_key=google_api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    response = model.generate_content(f"""
        You are a music metadata assistant.  
        Given an input “Title” (which is ambiguous), identify the song’s official name and its primary artist.  
        Return your answer in the exact format:

        <song_name>-<artist_name>

        Example:
        Input: “Shape of You by Ed”  
        Output: “Shape of You-Ed Sheeran”

        Now process the following:
        Title: "{video_title}"
    """)

    song_metadata = response.text

    song_metadata = song_metadata.split('-')

    return song_metadata