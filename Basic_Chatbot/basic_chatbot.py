"""
CodeAlpha Python Internship - Task 4
Basic Rule-Based Chatbot

A simple chatbot that responds to predefined user inputs like greetings,
questions, and farewells using if-elif logic.

Author: Anam Shaheen
"""


def get_response(user_input):
    """Return a chatbot response based on the user's input."""
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you today?"

    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How about you?"

    elif user_input in ["what is your name", "what's your name"]:
        return "I'm a simple chatbot built for the CodeAlpha internship."

    elif user_input in ["what can you do"]:
        return "I can chat with you about basic things like greetings and farewells!"

    elif user_input in ["thank you", "thanks"]:
        return "You're welcome!"

    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I didn't understand that. Could you try rephrasing?"


def chat():
    print("=" * 40)
    print("Simple Chatbot - Type 'bye' to exit")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ")
        response = get_response(user_input)
        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    chat()
