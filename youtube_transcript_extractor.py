# youtube_transcript_extractor.py
"""
This module extracts the transcript from a given YouTube video URL.
We use youtube-transcript-api for this.
"""

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import re

def extract_video_id(youtube_url):
    """
    Extracts the video ID from a YouTube URL.
    
    Parameters:
    - youtube_url (str): YouTube video URL
    
    Returns:
    - str: YouTube video ID
    """
    # Handle different YouTube URL formats
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*",  # Standard and shortened URLs
        r"(?:embed\/)([0-9A-Za-z_-]{11})",  # Embed URLs
        r"(?:youtu\.be\/)([0-9A-Za-z_-]{11})"  # Short URLs
    ]
    
    for pattern in patterns:
        match = re.search(pattern, youtube_url)
        if match:
            return match.group(1)
    
    raise ValueError("Invalid YouTube URL format. Could not extract video ID.")

def extract_transcript(youtube_url, languages=['en']):
    """
    Retrieves the transcript for a given YouTube video.
    Returns the full transcript as a single string.
    
    Parameters:
    - youtube_url (str): YouTube video URL
    - languages (list): List of language codes to try, in order of preference
    
    Returns:
    - str: Full transcript as a string
    """
    try:
        video_id = extract_video_id(youtube_url)
        
        # Try to get transcript in any of the provided languages
        transcript_list = None
        for lang in languages:
            try:
                transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
                print(f"[INFO] Transcript found in language: {lang}")
                break
            except (NoTranscriptFound, TranscriptsDisabled) as e:
                continue
                
        if transcript_list is None:
            # Try one more time with auto-generated transcripts
            try:
                transcript_list = YouTubeTranscriptApi.list_transcripts(video_id).find_generated_transcript(languages)
                print("[INFO] Using auto-generated transcript")
            except Exception:
                print("[ERROR] No transcript available for this video.")
                return None

        # Join all transcript parts into one text
        full_transcript = "\n".join([item['text'] for item in transcript_list])
        return full_transcript

    except TranscriptsDisabled:
        print("[ERROR] Transcripts are disabled for this video.")
        return None
    except Exception as e:
        print(f"[ERROR] Failed to get transcript: {e}")
        return None

# Test script (only runs if this file is executed directly)
if __name__ == "__main__":
    test_url = input("Enter a YouTube video URL: ")
    transcript = extract_transcript(test_url)
    if transcript:
        print("\n[TRANSCRIPT]\n", transcript[:500], "...\n")  # Show first 500 chars
    else:
        print("[ERROR] Could not extract transcript.")