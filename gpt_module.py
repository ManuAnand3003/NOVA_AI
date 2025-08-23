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

def gpt_response(prompt, memory=None):
    if memory is None:
        memory = []
    
    # Gemini's chat history expects alternating roles.
    # OpenAI's messages can have consecutive user/assistant roles if not carefully managed.
    # We need to convert the existing memory to Gemini's format if it's not already.
    # For simplicity, let's assume 'memory' is already in a format compatible with Gemini's history
    # or that we'll build it correctly.
    
    # For Gemini, the history is a list of dicts with 'role' and 'parts'.
    # 'user' role for user input, 'model' role for AI responses.
    
    # Convert existing memory to Gemini format if necessary
    gemini_history = []
    for item in memory:
        if item["role"] == "user":
            gemini_history.append({"role": "user", "parts": [item["content"]]})
        elif item["role"] == "assistant":
            gemini_history.append({"role": "model", "parts": [item["content"]]})

    model = genai.GenerativeModel(GPT_MODEL)
    chat = model.start_chat(history=gemini_history)
    
    try:
        response = chat.send_message(prompt)
        reply = response.text.strip()
        
        # Append to memory in a consistent format (e.g., OpenAI-like for main.py compatibility)
        # Or, if main.py is updated to handle Gemini's format, this can be changed.
        # For now, let's keep it consistent with the original memory structure for main.py.
        memory.append({"role": "user", "content": prompt}) # Add user prompt to memory
        memory.append({"role": "assistant", "content": reply}) # Add AI response to memory
        
        return reply, memory
    except Exception as e:
        return f"An error occurred: {e}", memory