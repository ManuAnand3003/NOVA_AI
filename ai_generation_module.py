# ai_generation_module.py
import google.generativeai as genai
from dotenv import load_dotenv
import os
from config import GPT_MODEL # Import GPT model from config

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY") # Assuming GOOGLE_API_KEY for Gemini

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

genai.configure(api_key=api_key)

def generate_text(prompt, model=GPT_MODEL):
    """
    Generates text based on a given prompt using the Gemini API.
    This can be extended for image generation or other creative tasks.
    """
    try:
        model = genai.GenerativeModel(model)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"An error occurred during AI generation: {e}"

if __name__ == "__main__":
    # Example usage
    print("Generating a short story about a robot cat...")
    story_prompt = "Write a very short, whimsical story about a robot cat who loves to chase laser pointers, but only on Tuesdays."
    generated_story = generate_text(story_prompt)
    print("\nGenerated Story:")
    print(generated_story)