from googleapiclient.discovery import build
import os
from .manipulate_duration import parse_duration, format_duration

API_KEY = os.getenv("API_KEY")


def get_playlist_duration(playlist_id):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.playlistItems().list(
        part="contentDetails", playlistId=playlist_id, maxResults=50
    )
    response = request.execute()

    total_duration = 0
    for item in response["items"]:
        video_id = item["contentDetails"]["videoId"]
        video_response = (
            youtube.videos().list(part="contentDetails", id=video_id).execute()
        )
        duration = video_response["items"][0]["contentDetails"]["duration"]
        total_duration += parse_duration(duration)

    return format_duration(total_duration)