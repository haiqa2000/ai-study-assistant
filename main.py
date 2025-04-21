# main.py
"""
Main controller script for the AI Study Assistant.
Handles user input, extracts content, calls OpenAI, and displays results.
"""

import os
from pdf_text_extractor import extract_text_from_pdf
from youtube_transcript_extractor import extract_transcript
from openai_prompt_handler import generate_study_material

def display_menu():
    """
    Displays the main menu and gets user selection.
    """
    print("\n📚 AI Study Assistant 📚")
    print("1. Extract from PDF eBook/Notes")
    print("2. Extract from YouTube Video")
    print("3. Exit")
    choice = input("Select an option (1-3): ")
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

def main():
    while True:
        user_choice = display_menu()

        if user_choice == "1":
            pdf_path = input("\nEnter the full path to your PDF file: ").strip()
            content_text = extract_text_from_pdf(pdf_path)

        elif user_choice == "2":
            video_url = input("\nEnter the YouTube video URL: ").strip()
            content_text = extract_transcript(video_url)

        elif user_choice == "3":
            print("\nExiting program. Goodbye! 👋")
            break

        else:
            print("[WARNING] Invalid choice. Try again.")
            continue

        if not content_text:
            print("[ERROR] No content extracted. Try again.")
            continue

        material_type = choose_material_type()
        print("\n[INFO] Generating AI-powered study material. Please wait...")

        result = generate_study_material(content_text, material_type)

        if result:
            print(f"\n[RESULT — {material_type.upper()}]\n")
            print(result[:3000])  # Limit display length for readability

            # Ask user if they want to save
            save = input("\nDo you want to save this to a text file? (y/n): ").lower()
            if save == "y":
                file_name = input("Enter a file name (without extension): ") + ".txt"
                save_to_file(result, file_name)
        else:
            print("[ERROR] AI generation failed. Try again.")

if __name__ == "__main__":
    main()
