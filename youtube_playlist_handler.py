# youtube_playlist_handler.py

from pytube import Playlist

def get_video_urls_from_playlist(playlist_url):
    """
    Takes a YouTube playlist URL and returns a list of video URLs.
    """
    try:
        playlist = Playlist(playlist_url)
        video_urls = playlist.video_urls
        print(f"Found {len(video_urls)} videos in the playlist.")
        return video_urls
    except Exception as e:
        print(f"Failed to get videos: {e}")
        return []
