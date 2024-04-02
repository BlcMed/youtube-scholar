from googleapiclient.discovery import build
import os
from .manipulate_duration import parse_duration
from .language_analysis import detect_language_from_text

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
    return True


def get_most_used_language(playlist_id):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.playlistItems().list(
        part="snippet", playlistId=playlist_id, maxResults=50
    )
    response = request.execute()

    language_count = {}
    total_videos = 0

    for item in response["items"]:
        video_id = item["snippet"]["resourceId"]["videoId"]
        video_response = youtube.videos().list(part="snippet", id=video_id).execute()
        video_snippet = video_response["items"][0]["snippet"]
        video_title = video_snippet.get("title", "")
        video_description = video_snippet.get("description", "")
        video_text = f"{video_title} {video_description}"

        # Detect language from video text
        detected_language = detect_language_from_text(video_text)

        if detected_language:
            total_videos += 1
            if detected_language in language_count:
                language_count[detected_language] += 1
            else:
                language_count[detected_language] = 1

    if total_videos == 0:
        return None

    most_used_language = max(language_count, key=language_count.get)
    return most_used_language


def filter_playlist_by_language(playlist_id, target_language=None):
    most_used_language = get_most_used_language(playlist_id)
    if not most_used_language:
        return False
    return most_used_language == target_language


def filter_playlist_by_accent():
    pass


def filter_playlist_by_comments():
    pass


# exemple usage for get_most_used_language
# playlist_id = "PLL6RiAl2WHXEU04zFYyWrUGV_fqGG4TuR"
# most_used_language = get_most_used_language(playlist_id)
# if most_used_language:
#     print(f"The most used language in the playlist is {most_used_language}.")
# else:
#     print("No language detected in the playlist.")
