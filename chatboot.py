
import random
import nltk
from nltk.tokenize import word_tokenize
from datetime import datetime

nltk.download("punkt", quiet=True)

responses = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! Welcome.",
        "Hey! Nice to meet you."
    ],
    "thanks": [
        "You're welcome!",
        "Happy to help!"
    ],
    "bye": [
        "Goodbye!",
        "See you again!"
    ],
    "help": [
        "I can answer basic questions and chat with you."
    ]
}

intents = {
    "greeting": ["hello","hi","hii","hey","good","morning","evening"],
    "thanks": ["thanks","thank","thankyou"],
    "bye": ["bye","goodbye"],
    "help": ["help","support"]
}

def get_response(message):
    text = message.lower()
    words = word_tokenize(text)

    for intent, keywords in intents.items():
        if any(word in keywords for word in words):
            return random.choice(responses[intent])

    if "time" in words:
        return f"Current time is {datetime.now().strftime('%I:%M %p')}"

    if "date" in words:
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}"

    if "name" in words:
        return "I'm AI Assistant created using Python, Flask and NLTK."

    return "I'm still learning. Could you ask that in another way?"