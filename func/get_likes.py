def likes(url):
    from googleapiclient.discovery import build
    import os
    from dotenv import load_dotenv

    load_dotenv()
    google_api_key = os.getenv('YOUTUBE_API')

    video_id = url
    youtube = build('youtube', 'v3', developerKey=google_api_key)

    request = youtube.videos().list(
        part='statistics',
        id=video_id
    )
    response = request.execute()

    likes = response['items'][0]['statistics']['likeCount']

    return likes
