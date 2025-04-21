# youtube_transcript_extractor.py
"""
This module extracts the transcript from a given YouTube video URL.
We use youtube-transcript-api for this.
"""

from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(youtube_url):
    """
    Extracts the video ID from a YouTube URL.
    """
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", youtube_url)
    if video_id_match:
        return video_id_match.group(1)
    else:
        raise ValueError("Invalid YouTube URL format.")

def get_transcript(youtube_url, language='en'):
    """
    Retrieves the transcript for a given YouTube video.
    Returns the full transcript as a single string.
    """
    try:
        video_id = extract_video_id(youtube_url)
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])

        full_transcript = "\n".join([item['text'] for item in transcript_list])
        return full_transcript

    except Exception as e:
        print(f"[ERROR] Failed to get transcript: {e}")
        return None

# Test script (only runs if this file is executed directly)
if __name__ == "__main__":
    test_url = input("Enter a YouTube video URL: ")
    transcript = get_transcript(test_url)
    if transcript:
        print("\n[TRANSCRIPT]\n", transcript)
