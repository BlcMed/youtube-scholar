from googleapiclient.discovery import build
import os

API_KEY = os.getenv("API_KEY")


def get_likes_views_info(playlist_id):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.playlistItems().list(
        part="snippet", playlistId=playlist_id, maxResults=50
    )
    response = request.execute()

    videos_info = []
    total_likes = 0
    total_views = 0

    for item in response["items"]:
        video_id = item["snippet"]["resourceId"]["videoId"]
        video_response = youtube.videos().list(part="statistics", id=video_id).execute()
        statistics = video_response["items"][0]["statistics"]
        likes = int(statistics.get("likeCount", 0))
        views = int(statistics.get("viewCount", 0))
        total_likes += likes
        total_views += views
        videos_info.append({"video_id": video_id, "likes": likes, "views": views})

    videos_info.sort(key=lambda x: x["likes"] / x["views"], reverse=True)
    top_videos = videos_info[:3]  # Return top 3 videos with highest likes/views ratio

    if total_views > 0:
        average_ratio = total_likes / total_views
    else:
        average_ratio = 0

    return top_videos, average_ratio


# Example usage:
# playlist_id = "YOUR_PLAYLIST_ID"
# top_videos, average_ratio = get_likes_views_info(playlist_id)
# print("Top 3 videos with highest likes/views ratio:")
# for video in top_videos:
#     print(f"Video ID: {video['video_id']}, Likes: {video['likes']}, Views: {video['views']}")
# print("Average likes/views ratio for all videos in the playlist:", average_ratio)
