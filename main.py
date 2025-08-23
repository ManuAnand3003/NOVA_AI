#main.py
import subprocess
from sentiment import analyze_sentiment
from gpt_module import gpt_response
from vision_module import analyze_image # Import the new vision module
from ai_generation_module import generate_text # Import the new AI generation module
import json
import os
import nlp_module


# Load user-specific memory
def load_memory(user_name):
    filename = f"user_{user_name}.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {"interests": [], "conversation": []}

# Save user-specific memory
def save_memory(user_name, memory):
    filename = f"user_{user_name}.json"
    with open(filename, "w") as f:
        json.dump(memory, f)

from config import DEFAULT_INPUT_MODE # Import default input mode from config



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

# Load or create user-specific memory
memory = load_memory(user_name)
memory['user_name'] = user_name
save_memory(user_name, memory)

# speak(f"Nice to meet you, {user_name}! How can I assist you today?")
print(f"Nice to meet you, {user_name}! How can I assist you today?")

# List of available functions/services
AVAILABLE_FUNCTIONS = [
    "chat",
    "image analysis",
    "image generation",
    "audio conversation",
    "sentiment analysis",
    "calculator",
    "AI text generation"
]


def show_available_functions():
    print("\nCurrent available functions/services:")
    for func in AVAILABLE_FUNCTIONS:
        print(f"- {func}")
    print("Type the name of the function/service you want to use.")

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
    show_available_functions()
    selected_function = input("\nEnter the function/service you want to use (or type 'exit' to quit): ")
    selected_function_clean = selected_function.strip().lower()
    # Map user input to available functions (case/space insensitive)
    function_map = {func.lower(): func for func in AVAILABLE_FUNCTIONS}

    if selected_function_clean in ["exit", "quit", "bye"]:
        print("Nova: Goodbye! Have a great day!")
        break

    # Optionally allow mode switching
    if selected_function_clean == "switch mode":
        print("\nAvailable Modes:")
        print("1. Voice Mode: Speak your commands and questions")
        print("2. Text Mode: Type your commands and questions")
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

    # Get user input for the selected function
    if selected_function_clean == "chat":
        user_input, _ = get_user_input(user_name, current_input_mode)
        # Sentiment analysis integration
        sentiment_result = analyze_sentiment(user_input)
        print(f"Sentiment: {sentiment_result}")
        response, memory['conversation'] = gpt_response(user_input, memory.get('conversation'))
        save_memory(user_name, memory)
        print("Nova: ", response)
    elif selected_function_clean == "image analysis":
        image_path = input("Please provide the path to the image: ")
        vision_result = analyze_image(image_path)
        print("Nova (Vision):", vision_result)
    elif selected_function_clean == "image generation":
        from image_generation import generate_image
        prompt = input("Enter a prompt to generate an image: ")
        output_path = input("Enter output file name (or press Enter for 'generated_image.png'): ").strip()
        if not output_path:
            output_path = "generated_image.png"
        print("Generating image, please wait...")
        result_path = generate_image(prompt, output_path)
        print(f"Image generated and saved to {result_path}")
    elif selected_function_clean == "audio conversation":
        user_input = listen()
        print(f"{user_name} (voice): {user_input}")
        response, memory['conversation'] = gpt_response(user_input, memory.get('conversation'))
        save_memory(user_name, memory)
        print("Nova: ", response)
    elif selected_function_clean == "sentiment analysis":
        user_input = input("Enter text to analyze sentiment: ")
        sentiment_result = analyze_sentiment(user_input)
        print("Nova (Sentiment):", sentiment_result)
    elif selected_function_clean == "calculator":
        user_input = input("Enter calculation: ")
        from calculator import evaluate_expression
        result = evaluate_expression(user_input)
        print("Nova (calculator):", result)
    elif selected_function_clean == "ai text generation":
        gen_prompt = input("What would you like me to generate text about? ")
        generated_content = generate_text(gen_prompt)
        print("Nova (AI Generation):", generated_content)
    else:
        print("Invalid function/service. Please choose from the available options.")