import os
import pandas as pd
from googleapiclient.discovery import build
from datetime import timedelta

# Replace with your own API key
API_KEY = 'YOUR_YOUTUBE_DATA_API_KEY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
PLAYLIST_ID = 'PLIg1dOXc_acbdJo-AE5RXpIM_rvwrerwR'  # Replace with your playlist ID

def get_video_details(youtube, playlist_id):
    videos = []
    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50
    )
    response = request.execute()

    while request:
        video_ids = []
        for item in response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            video_ids.append(video_id)

        video_details = youtube.videos().list(
            part='contentDetails,snippet',
            id=','.join(video_ids)
        ).execute()

        for item in video_details['items']:
            duration = item['contentDetails']['duration']
            title = item['snippet']['title']
            description = item['snippet']['description']
            video_id = item['id']
            
            # Convert ISO 8601 duration to a more readable format
            duration_readable = convert_duration(duration)
            
            # Create video link
            video_link = f'https://www.youtube.com/watch?v={video_id}'
            
            videos.append({
                'Video ID': video_id,
                'Title': title,
                'Description': description,
                'Duration': duration_readable,
                'Link': video_link
            })

        request = youtube.playlistItems().list_next(request, response)
        if request:
            response = request.execute()

    return videos

def convert_duration(duration):
    # Example: PT1H2M34S (1 hour, 2 minutes, 34 seconds)
    time_parts = duration.replace('PT', '').replace('H', ':').replace('M', ':').replace('S', '').split(':')
    
    # Convert parts to integer and handle missing values (e.g., no hours)
    time_parts = [int(part) if part else 0 for part in time_parts]
    
    # Create timedelta
    if len(time_parts) == 3:
        return str(timedelta(hours=time_parts[0], minutes=time_parts[1], seconds=time_parts[2]))
    elif len(time_parts) == 2:
        return str(timedelta(minutes=time_parts[0], seconds=time_parts[1]))
    else:
        return str(timedelta(seconds=time_parts[0]))

def save_to_excel(videos, filename='youtube_playlist.xlsx'):
    df = pd.DataFrame(videos)
    df.to_excel(filename, index=False)
    print(f'File saved as {filename}')

def main():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    videos = get_video_details(youtube, PLAYLIST_ID)
    save_to_excel(videos)

if __name__ == '__main__':
    main()
