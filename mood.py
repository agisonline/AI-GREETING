# Basic AI Mood Detector without emojis

def detect_mood(message):
    message = message.lower()

    if "happy" in message or "good" in message or "great" in message:
        return "You sound happy!"
    elif "sad" in message or "bad" in message or "upset" in message:
        return "I'm sorry you're feeling sad."
    elif "angry" in message or "mad" in message:
        return "You seem angry. Want to talk about it?"
    else:
        return "I'm not sure how you're feeling."

def chat():
    print("MoodBot: Hello! How are you feeling? (type 'bye' to exit)")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("MoodBot: Goodbye! Take care.")
            break

        response = detect_mood(user_input)
        print("MoodBot:", response)

# Start the bot
chat()
