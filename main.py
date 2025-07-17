#main.py  
from nlp_module import chat_response
from calculator import evalualate_expression
from sentiment import analyze_sentiment
import json
import os

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

memory=load_memory()

print("Hello!...I'm Nova , your personal AI assistant. What's your name?")
user_name=input("Enter your name: ")
memory['user_name'] = user_name
save_memory(memory)

print(f"Nice to meet you, {user_name}! How can I assist you today?")

while True:
    user_input=input(f"{user_name}: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Nova: Goodbye! Have a great day!")
        break

    #check if its a calculation
    if any(char in user_input for char in "+-*/^%"):
        result = evalualate_expression(user_input)
        print("Nova (calculator):", result)
        continue

    # check sentiment
    if "how do i feel" in user_input.lower():
        print("Nova (Sentiment):", analyze_sentiment(user_input))
        continue

    #NLP response
    print("Nova: ",chat_response(user_input))