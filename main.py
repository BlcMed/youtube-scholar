from playlist_search import search_playlist_by_name, filter_playlist_by_duration
from likes_views_analysis import get_likes_views_info

def main():
    # Input tutorial name and duration filter
    tutorial_name = input("Enter the name of the tutorial: ")
    duration_filter = int(input("Enter the duration filter in seconds (optional, 0 for no filter): "))

    # Search for playlists containing the tutorial name
    playlists = search_playlist_by_name(tutorial_name)

    # Filter playlists based on duration
    filtered_playlists = []
    for playlist in playlists:
        playlist_id = playlist['id']['playlistId']
        if not duration_filter or filter_playlist_by_duration(playlist_id, max_duration=duration_filter):
            filtered_playlists.append(playlist_id)

    if not filtered_playlists:
        print("No playlists found matching the criteria.")
        return

    # Get likes/views info for each filtered playlist
    playlist_likes_views_info = []
    for playlist_id in filtered_playlists:
        _, average_ratio = get_likes_views_info(playlist_id)
        playlist_likes_views_info.append({'playlist_id': playlist_id, 'average_ratio': average_ratio})

    # Sort playlists by average ratio of likes/views
    playlist_likes_views_info.sort(key=lambda x: x['average_ratio'], reverse=True)

    # Print links of playlists with highest average ratio of likes/views
    print("Playlists with the highest average ratio of likes/views:")
    for playlist_info in playlist_likes_views_info[:3]:
        playlist_link = f"https://www.youtube.com/playlist?list={playlist_info['playlist_id']}"
        print(playlist_link)

if __name__ == "__main__":
    main()
