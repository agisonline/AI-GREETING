import random

# List of greetings the bot can recognize
greetings = ["hi", "hello", "hey", "hola", "howdy"]

# Possible bot responses
responses = [
    "Hello! How can I help you today?",
    "Hi there! Nice to meet you!",
    "Hey! What can I do for you?",
    "Howdy! How’s your day going?"
]

def get_response(user_input):
    user_input = user_input.lower()
    for word in greetings:
        if word in user_input:
            return random.choice(responses)
    return "I'm not sure what you mean. Try saying hello!"

# Main chat loop
def chat():
    print("🤖 Smart AI Bot: Type 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("🤖 Smart AI Bot: Goodbye! Have a great day!")
            break
        print("🤖 Smart AI Bot:", get_response(user_input))

# Run the bot
chat()
