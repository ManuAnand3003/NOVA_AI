#nlp_module.py

def chat_response(text):
    text = text.lower()
    if "your name" in text:
        return "I'm Nova, your multifunctional personal AI assistant, who is still in early stages of development."
    elif "hello" in text or "hi" in text:
        return "Hello there! How can I assist you today?"
    elif "help" in text:
        return "Sure! I can help with calculations, sentiment analysis, and general questions. What do you need?"
    else:
        return "That's interesting! Let's talk more about it"