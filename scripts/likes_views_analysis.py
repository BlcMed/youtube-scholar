from googleapiclient.discovery import build
import os

API_KEY = os.getenv("API_KEY")


def get_likes_views_info(playlist_id):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    playlist_info_request = youtube.playlists().list(part="snippet", id=playlist_id)
    playlist_info_response = playlist_info_request.execute()

    playlist_title = playlist_info_response["items"][0]["snippet"]["title"]

    playlist_items_request = youtube.playlistItems().list(
        part="snippet", playlistId=playlist_id, maxResults=50
    )
    playlist_items_response = playlist_items_request.execute()

    videos_info = []
    total_likes = 0
    total_views = 0

    for item in playlist_items_response["items"]:
        video_id = item["snippet"]["resourceId"]["videoId"]
        video_title = item["snippet"]["title"]
        video_response = (
            youtube.videos().list(part="statistics,snippet", id=video_id).execute()
        )
        statistics = video_response["items"][0]["statistics"]
        snippet = video_response["items"][0]["snippet"]
        likes = int(statistics.get("likeCount", 0))
        views = int(statistics.get("viewCount", 0))
        total_likes += likes
        total_views += views
        videos_info.append(
            {
                "video_id": video_id,
                "video_title": video_title,
                "likes": likes,
                "views": views,
            }
        )

    videos_info.sort(key=lambda x: x["likes"] / x["views"], reverse=True)
    top_videos = videos_info[:3]  # Return top 3 videos with highest likes/views ratio

    if total_views > 0:
        average_ratio = total_likes / total_views
    else:
        average_ratio = 0

    return playlist_title, top_videos, average_ratio


# Example usage:
# playlist_id = "YOUR_PLAYLIST_ID"
# top_videos, average_ratio = get_likes_views_info(playlist_id)
# print("Top 3 videos with highest likes/views ratio:")
# for video in top_videos:
#     print(f"Video ID: {video['video_id']}, Likes: {video['likes']}, Views: {video['views']}")
# print("Average likes/views ratio for all videos in the playlist:", average_ratio)
