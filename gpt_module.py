import openai
from dotenv import load_dotenv
import os
from config import GPT_MODEL # Import GPT model from config

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

def gpt_response(prompt, memory=None):
    if memory is None:
        memory = []
    
    messages = memory + [{"role": "user", "content": prompt}]
    
    try:
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=messages
        )
        reply = response.choices[0].message.content.strip()
        memory.append({"role": "assistant", "content": reply})
        return reply, memory
    except Exception as e:
        return f"An error occurred: {e}", memory