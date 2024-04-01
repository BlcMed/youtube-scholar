from googleapiclient.discovery import build
import os
from .manipulate_duration import parse_duration

API_KEY = os.getenv("API_KEY")


def search_playlist_by_name(name):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.search().list(
        q=name, part="snippet", type="playlist", maxResults=10
    )
    response = request.execute()
    return response["items"]


def filter_playlist_by_duration(playlist_id, min_duration=None, max_duration=None):
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

    if min_duration and total_duration < min_duration:
        return False
    if max_duration and total_duration > max_duration:
        return False

    def filter_playlist_by_language():
        pass

    def filter_playlist_by_accent():
        pass

    def filter_playlist_by_comments():
        pass

    return True


# Exemple usage:
# playlists = search_playlist_by_name("Java tutorial")
# for playlist in playlists:
#     playlist_id = playlist['id']['playlistId']
#     if filter_playlist_by_duration(playlist_id, min_duration=3600, max_duration=30000):
#         print(playlist['snippet']['title'])
