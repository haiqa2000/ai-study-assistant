# config.py
"""
This config file loads sensitive keys from your local .env file.
We use python-dotenv for safe key management.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# YouTube API key (if you plan to use YouTube Data API — optional for now)
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Check if keys loaded successfully
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found! Please check your .env file.")

print("[CONFIG] API keys loaded successfully.")
