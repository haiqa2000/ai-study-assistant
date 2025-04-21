# youtube_playlist_handler.py
"""
This module extracts video URLs from a YouTube playlist.
"""

from pytube import Playlist
import re

def get_video_urls_from_playlist(playlist_url):
    """
    Takes a YouTube playlist URL and returns a list of video URLs.
    
    Parameters:
    - playlist_url (str): URL of the YouTube playlist
    
    Returns:
    - list: List of video URLs in the playlist
    """
    # Validate playlist URL format
    if not re.match(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/playlist\?list=', playlist_url):
        raise ValueError("Invalid YouTube playlist URL format. URL should be in the format: https://www.youtube.com/playlist?list=PLAYLIST_ID")
    
    try:
        playlist = Playlist(playlist_url)
        
        # Sometimes pytube needs this workaround to correctly parse playlist URLs
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        
        video_urls = list(playlist.video_urls)
        
        if not video_urls:
            print("[WARNING] No videos found in the playlist. Check if the playlist is private or empty.")
            return []
            
        print(f"[INFO] Found {len(video_urls)} videos in the playlist: '{playlist.title}'")
        return video_urls
        
    except Exception as e:
        print(f"[ERROR] Failed to get videos from playlist: {e}")
        return []

# Test script (only runs if this file is executed directly)
if __name__ == "__main__":
    test_playlist_url = input("Enter a YouTube playlist URL: ")
    videos = get_video_urls_from_playlist(test_playlist_url)
    
    if videos:
        print("\n[VIDEOS IN PLAYLIST]")
        for i, url in enumerate(videos, 1):
            print(f"{i}. {url}")
    else:
        print("[ERROR] Could not extract videos from playlist.")