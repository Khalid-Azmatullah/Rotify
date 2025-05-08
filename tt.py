from pytubefix import YouTube
import requests
from PIL import Image
from io import BytesIO

# Function to download and resize the thumbnail
def download_and_resize_thumbnail(video_url, sizes):
    # Fetch the YouTube video
    yt = YouTube(video_url)
    thumbnail_url = yt.thumbnail_url
    title= yt.title

    # Download the thumbnail image
    response = requests.get(thumbnail_url)
    if response.status_code != 200:
        print("Failed to retrieve the thumbnail.")
        return

    # Open the image using Pillow
    img = Image.open(BytesIO(response.content))

    # Prepare the artwork list
    artwork = []

    # Resize the image to each specified size and save
    for size in sizes:
        resized_img = img.copy()
        resized_img.thumbnail((size, size))
        filename = f'Cover/{title}_{size}x{size}.jpg'
        resized_img.save(filename, 'JPEG')
        artwork.append({
            'src': filename,
            'sizes': f'{size}x{size}',
            'type': 'image/jpeg'
        })
        print(f"Saved {filename}")

    return artwork

# Example usage
video_url = 'https://www.youtube.com/watch?v=2lAe1cqCOXo'  # Replace with your video URL
sizes = [96, 128, 192]
artwork = download_and_resize_thumbnail(video_url, sizes)
print(artwork)
