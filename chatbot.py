"""
Project 1: Rule-Based AI Chatbot
DecodeLabs Internship 

A simple rule-based chatbot that uses if-else / dictionary logic
to respond to predefined user inputs. This project demonstrates
control flow, decision-making logic, and basic AI concepts.
"""

# 1.Knowledge Base (Intents)

responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What's up?",
    "hey": "Hey! Nice to see you.",
    "how are you": "I'm just your friendly rule-based chatbot, but I'm doing great! How about you?",
    "your name": "I'm a simple rule-based chatbot built for DecodeLabs Project 1.",
    "who made you": "I was built as part of the DecodeLabs AI Internship program by Ms.Sabaoon :)",
    "help": "I can chat about basic things. Try saying hello, or ask me about Sabaoon!",
    "who is sabaoon": "Sabaoon is a BS Computer Science Graduate and She loves to explore new technologies!",
    "what can you do": "Right now, I can only respond to a few fixed messages. I'm rule-based, not a learning AI yet!",
    "thank you": "You're welcome!",
    "thanks": "No problem, happy to help. See you later!",
}

EXIT_COMMANDS = ["bye", "exit", "quit"]


def get_response(user_input: str) -> str:
    #2.Look up a cleaned user input in the knowledge base.
    return responses.get(user_input, "I do not understand. Can you rephrase that?")


def chat():
    print("Chatbot: Hello Pookie! I'm a rule-based chatbot.Remember to type: 'bye' or 'exit' to end the chat.\n")

    while True:
        raw_input_text = input("You: ")

        # 3.Sanitization: normalize case & remove extra whitespace
        clean_input = raw_input_text.lower().strip()

        # 4.Exit condition
        if clean_input in EXIT_COMMANDS:
            print("Chatbot: Goodbye! Have a nice day. \U0001F44B")
            break

        # 5.Fallback & lookup handled in one place
        reply = get_response(clean_input)
        print("Chatbot:", reply)


if __name__ == "__main__":
    chat()
