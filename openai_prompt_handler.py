# openai_prompt_handler.py
"""
This module interacts with the OpenAI API.
It sends structured prompts to generate notes, flashcards, formula sheets, etc.
"""

from openai import OpenAI
from config import OPENAI_API_KEY

# Initialize OpenAI client with key from config file
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_study_material(content_text, material_type="notes"):
    """
    Sends a prompt to OpenAI API to generate study material from provided content.
    
    Parameters:
    - content_text (str): Text input (from PDF or YouTube transcript)
    - material_type (str): Type of material to generate: 'notes', 'flashcards', 'formula sheet', 'question bank'
    
    Returns:
    - response_text (str): AI-generated content
    """

    # Check if content is too short
    if not content_text or len(content_text) < 20:
        return "Insufficient content to generate study material."

    # Define different prompt templates based on material type
    prompt_templates = {
        "notes": f"Convert the following content into well-organized, concise study notes:\n\n{content_text}",
        
        "flashcards": f"Create at least 10 flashcards from the following content. Write them in 'Question: ... Answer: ...' format:\n\n{content_text}",
        
        "formula sheet": f"Extract all important formulas from the following content and list them clearly under appropriate headings:\n\n{content_text}",
        
        "question bank": f"Generate at least 10 multiple-choice and short-answer questions based on the following content. Provide answers too:\n\n{content_text}"
    }

    # Get the appropriate prompt for the requested material type
    prompt = prompt_templates.get(material_type.lower(), prompt_templates["notes"])

    try:
        # Call OpenAI API with our prompt using the updated client format
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert academic content generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,  # Slight creativity, but mostly accurate
            max_tokens=2000   # Maximum length of generated response
        )

        response_text = response.choices[0].message.content
        return response_text.strip()

    except Exception as e:
        print(f"[ERROR] OpenAI API call failed: {e}")
        return None


# Test script (only runs if this file is executed directly)
if __name__ == "__main__":
    test_content = input("Enter a short content sample: ")
    material_type = input("Choose type (notes / flashcards / formula sheet / question bank): ").strip().lower()

    result = generate_study_material(test_content, material_type)
    print(f"\n[GENERATED {material_type.upper()}]\n")
    print(result)