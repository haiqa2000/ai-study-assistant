# main.py
"""
Main controller script for the AI Study Assistant.
Handles user input, extracts content, calls OpenAI, and displays results.
"""

import os
from pdf_text_extractor import extract_text_from_pdf
from youtube_transcript_extractor import extract_transcript
from openai_prompt_handler import generate_study_material
from youtube_playlist_handler import get_video_urls_from_playlist

def display_menu():
    """
    Displays the main menu and gets user selection.
    """
    print("\n📚 AI Study Assistant 📚")
    print("1. Extract from PDF eBook/Notes")
    print("2. Extract from YouTube Video")
    print("3. Process YouTube Playlist")
    print("4. Exit")
    choice = input("Select an option (1-4): ")
    return choice.strip()

def choose_material_type():
    """
    Lets user choose the type of study material to generate.
    """
    print("\nWhat do you want to generate?")
    print("1. Notes")
    print("2. Flashcards")
    print("3. Formula Sheet")
    print("4. Question Bank")
    type_choice = input("Select (1-4): ")
    material_map = {
        "1": "notes",
        "2": "flashcards",
        "3": "formula sheet",
        "4": "question bank"
    }
    return material_map.get(type_choice.strip(), "notes")

def save_to_file(output_text, file_name):
    """
    Saves the generated content to a text file.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(output_text)
    print(f"\n[INFO] Content saved to {file_name}")

def process_content(content_text, source_identifier=""):
    """
    Process extracted content and generate study materials
    """
    if not content_text:
        print("[ERROR] No content extracted. Try again.")
        return

    material_type = choose_material_type()
    print("\n[INFO] Generating AI-powered study material. Please wait...")

    result = generate_study_material(content_text, material_type)

    if result:
        print(f"\n[RESULT — {material_type.upper()}]\n")
        print(result[:3000])  # Limit display length for readability

        # Ask user if they want to save
        save = input("\nDo you want to save this to a text file? (y/n): ").lower()
        if save == "y":
            if source_identifier:
                default_filename = f"{material_type.replace(' ', '_')}_{source_identifier}"
                file_name = input(f"Enter a file name (default: {default_filename}): ") or default_filename
                if not file_name.endswith(".txt"):
                    file_name += ".txt"
            else:
                file_name = input("Enter a file name (without extension): ") + ".txt"
            save_to_file(result, file_name)
    else:
        print("[ERROR] AI generation failed. Try again.")

def main():
    while True:
        user_choice = display_menu()

        if user_choice == "1":
            pdf_path = input("\nEnter the full path to your PDF file: ").strip()
            try:
                content_text = extract_text_from_pdf(pdf_path)
                process_content(content_text, os.path.basename(pdf_path).replace(".pdf", ""))
            except FileNotFoundError as e:
                print(f"[ERROR] {e}")
            except Exception as e:
                print(f"[ERROR] An unexpected error occurred: {e}")

        elif user_choice == "2":
            video_url = input("\nEnter the YouTube video URL: ").strip()
            try:
                content_text = extract_transcript(video_url)
                if content_text:
                    video_id = video_url.split("v=")[-1][:11]  # Extract video ID for filename
                    process_content(content_text, video_id)
            except Exception as e:
                print(f"[ERROR] Failed to process video: {e}")

        elif user_choice == "3":
            playlist_url = input("\nEnter YouTube playlist URL: ").strip()
            try:
                video_urls = get_video_urls_from_playlist(playlist_url)
                
                if not video_urls:
                    print("[ERROR] No videos found in playlist or invalid playlist URL.")
                    continue
                
                print(f"[INFO] Found {len(video_urls)} videos in the playlist.")
                process_all = input("Process all videos? (y/n): ").lower() == "y"
                
                material_type = choose_material_type() if process_all else None
                
                for i, video_url in enumerate(video_urls):
                    print(f"\n[INFO] Processing video {i+1}/{len(video_urls)}: {video_url}")
                    
                    if not process_all:
                        process_this = input(f"Process this video? (y/n): ").lower() == "y"
                        if not process_this:
                            continue
                    
                    transcript_text = extract_transcript(video_url)
                    if transcript_text:
                        video_id = video_url.split("v=")[-1][:11]
                        
                        if process_all:
                            result = generate_study_material(transcript_text, material_type)
                            if result:
                                file_name = f"{material_type.replace(' ', '_')}_{video_id}.txt"
                                save_to_file(result, file_name)
                                print(f"[INFO] Saved {material_type} for video {i+1}")
                        else:
                            process_content(transcript_text, video_id)
                    else:
                        print(f"[WARNING] Could not extract transcript for video {i+1}")
            
            except Exception as e:
                print(f"[ERROR] Failed to process playlist: {e}")

        elif user_choice == "4":
            print("\nExiting program. Goodbye! 👋")
            break

        else:
            print("[WARNING] Invalid choice. Try again.")

if __name__ == "__main__":
    main()