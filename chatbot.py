# chatbot.py
import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey 👋"],
    "ev": ["Electric vehicles are eco-friendly and cost-efficient."],
    "range": ["Electric range depends on battery capacity and make."],
    "tesla": ["Tesla is a leading EV manufacturer known for innovation."],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I don’t have an answer for that yet 🤖"
