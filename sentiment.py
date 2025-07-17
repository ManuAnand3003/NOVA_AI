#sentiment.py

from textblob import TextBlob

def analyze_sentiment(text):
    blob=TextBlob(text)
    polarity=blob.sentiment.polarity
    if polarity > 0:
        return "You seem to be in a positive mood!"
    elif polarity < 0:
        return "You might be feeling down. I'm here to support you."
    else:
        return "Hmmm...I can't quite tell how you're feeling."