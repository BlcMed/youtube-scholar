from flask import Flask, render_template, request
from playlist_search import search_playlist_by_name, filter_playlist_by_duration
from likes_views_analysis import get_likes_views_info
from get_playlist_duration import get_playlist_duration

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/results", methods=["POST"])
def results():
    query_type = request.form["query_type"]
    if query_type == "duration":
        playlist_id = request.form["playlist_id"]
        total_duration = get_playlist_duration(playlist_id)
        return render_template(
            "results.html", query_type=query_type, total_duration=total_duration
        )
    elif query_type == "search":
        tutorial_name = request.form["tutorial_name"]

        min_hours = int(request.form["min_hours"])
        min_minutes = int(request.form["min_minutes"])
        max_hours = int(request.form["max_hours"])
        max_minutes = int(request.form["max_minutes"])

        min_duration = min_hours * 3600 + min_minutes * 60
        max_duration = max_hours * 3600 + max_minutes * 60

        # Search for playlists containing the tutorial name
        playlists = search_playlist_by_name(tutorial_name)

        # Filter playlists based on duration
        filtered_playlists = []
        for playlist in playlists:
            playlist_id = playlist["id"]["playlistId"]
            if (
                not min_duration
                or filter_playlist_by_duration(playlist_id, min_duration=min_duration)
            ) and (
                not max_duration
                or filter_playlist_by_duration(playlist_id, max_duration=max_duration)
            ):
                filtered_playlists.append(playlist_id)

        if not filtered_playlists:
            return render_template(
                "results.html",
                query_type=query_type,
                playlists=[],
                message="No playlists found matching the criteria.",
            )

        # Get likes/views info for each filtered playlist
        playlist_likes_views_info = []
        for playlist_id in filtered_playlists:
            top_videos, average_ratio = get_likes_views_info(playlist_id)
            duration = get_playlist_duration(playlist_id)  # Fetch duration of playlist
            playlist_likes_views_info.append(
                {
                    "playlist_id": playlist_id,
                    "top_videos": top_videos,
                    "average_ratio": average_ratio,
                    "duration": duration,
                }
            )

        # Sort playlists by average ratio of likes/views
        playlist_likes_views_info.sort(key=lambda x: x["average_ratio"], reverse=True)

        # Prepare playlist data for rendering
        playlists_data = []
        for playlist_info in playlist_likes_views_info:
            playlist_data = {
                "playlist_id": playlist_info["playlist_id"],
                "link": f"https://www.youtube.com/playlist?list={playlist_info['playlist_id']}",
                "top_videos": playlist_info["top_videos"],
                "duration": playlist_info["duration"],
                "likes_ratio": round(playlist_info["average_ratio"] * 100, 2),
            }
            playlists_data.append(playlist_data)

        return render_template(
            "results.html", query_type=query_type, playlists=playlists_data
        )


if __name__ == "__main__":
    app.run(debug=True)
