#main.py
import subprocess
from sentiment import analyze_sentiment
from gpt_module import gpt_response
from vision_module import analyze_image # Import the new vision module
from ai_generation_module import generate_text # Import the new AI generation module
import json
import os
import nlp_module

#load memory
def load_memory():
    if os.path.exists("memory.json"):
        with open("memory.json", "r") as f:
            return json.load(f)
    return {}

#save memory
def save_memory(memory):
    with open("memory.json", "w") as f:
        json.dump(memory, f)        

from config import DEFAULT_INPUT_MODE # Import default input mode from config

memory = load_memory()
if 'conversation' not in memory:
    memory['conversation'] = []

import speech_recognition as sr
from gtts import gTTS
import playsound
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "temp_voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, I didn't catch that. Could not request results from Google Speech Recognition service; {e}")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred during speech recognition: {e}")
        return ""

print("Hello!...I'm Nova, your personal AI assistant. What's your name?")
# speak("Hello! I'm Nova, your personal AI assistant. What's your name?")

# Get user name with voice/text fallback
try:
    user_name = listen()
    if not user_name:
        user_name = input("Enter your name (voice not detected): ")
except:
    user_name = input("Enter your name: ")

memory['user_name'] = user_name
save_memory(memory)

# speak(f"Nice to meet you, {user_name}! How can I assist you today?")
print(f"Nice to meet you, {user_name}! How can I assist you today?")

def get_user_input(user_name, current_mode):
    print(f"\nCurrent input mode: {current_mode.capitalize()}")
    print("Type 'switch mode' to change input mode.")
    if current_mode == 'voice':
        print("Listening...")
        user_input = listen()
        print(f"{user_name} (voice): {user_input}")
        if user_input.lower() == "switch mode":
            return "switch_mode_command", current_mode
        return user_input, current_mode
    else: # current_mode == 'text'
        user_input = input(f"{user_name}: ")
        if user_input.lower() == "switch mode":
            return "switch_mode_command", current_mode
        return user_input, current_mode

current_input_mode = DEFAULT_INPUT_MODE

while True:
    user_input, command = get_user_input(user_name, current_input_mode)

    if command == "switch_mode_command":
        print("\nAvailable Modes:")
        print("1. Voice Mode: Speak your commands and questions")
        print("2. Text Mode: Type your commands and questions")
        
        print("\nIntegrated Functionalities:")
        print("- Natural Language Processing: Understands common phrases and questions")
        print("- Calculator: Performs mathematical calculations")
        print("- Sentiment Analysis: Analyzes emotional tone in text")
        print("- Image Analysis: Describes image content (requires image path)")
        print("- AI Text Generation: Creates text based on prompts")
        print("- GPT Conversations: General AI-powered conversations")
        
        new_mode_choice = input("\nSwitch to (1) Voice or (2) Text? Enter choice (1/2): ")
        if new_mode_choice == '1':
            current_input_mode = 'voice'
            print("Switched to Voice input mode.")
        elif new_mode_choice == '2':
            current_input_mode = 'text'
            print("Switched to Text input mode.")
        else:
            print("Invalid choice. Staying in current mode.")
        continue

    # Use 'current_input_mode' for speak function
    # This 'choice' variable is used for the speak function at the end of the loop.
    # It's derived from current_input_mode to ensure consistency.
    choice = '1' if current_input_mode == 'voice' else '2'

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Nova: Goodbye! Have a great day!")
        break

    # Check NLP module for predefined responses
    nlp_response = nlp_module.chat_response(user_input)
    if nlp_response != "That's interesting! Let's talk more about it": # Check if it's a generic fallback
        print("Nova (NLP):", nlp_response)
        # if choice == '1':
        #     # speak(nlp_response)
        continue

    # Check if it's a calculation
    # Attempt to evaluate the expression, if it fails, it's not a calculation
    try:
        # A simple heuristic to check if it might be a calculation
        if any(char in user_input for char in "+-*/^%"):
            from calculator import evaluate_expression
            result = evaluate_expression(user_input)
            print("Nova (calculator):", result)
            # if choice == '1':
            #     # speak(result)
            continue
    except Exception:
        pass # Not a calculation, proceed to next checks


    # Check sentiment with more flexible triggers
    import re
    sentiment_patterns = [
        r"how do i feel",
        r"what's my mood",
        r"my sentiment",
        r"how am i feeling"
    ]
    if any(re.search(pattern, user_input.lower()) for pattern in sentiment_patterns):
        sentiment_result = analyze_sentiment(user_input)
        print("Nova (Sentiment):", sentiment_result)
        # if choice == '1':
        #     # speak(sentiment_result)
        continue

    # Check for image analysis request
    if "analyze image" in user_input.lower():
        image_path = input("Please provide the path to the image: ")
        vision_result = analyze_image(image_path)
        print("Nova (Vision):", vision_result)
        # if choice == '1':
        #     # speak(vision_result)
        continue


    # Check for AI generation request
    if "generate text" in user_input.lower():
        gen_prompt = input("What would you like me to generate text about? ")
        generated_content = generate_text(gen_prompt)
        print("Nova (AI Generation):", generated_content)
        # if choice == '1':
        #     # speak(generated_content)
        continue

    # GPT response with memory
    response, memory['conversation'] = gpt_response(user_input, memory.get('conversation'))
    save_memory(memory)
    print("Nova: ", response)
    # if choice == '1':
    #     # speak(response)