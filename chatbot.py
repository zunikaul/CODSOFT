import random

def chatbot():
    print("CodBot: Hello!! I'm CodBot, your friendly chatbot. Type 'exit' to leave anytime.\n")

    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why don't programmers like nature? Too many bugs!",
        "Why did the computer show up late? It had a hard drive!"
    ]

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey", "yo"]:
            print("CodBot: Hi there! How can I help you today?")

        elif "your name" in user_input:
            print("CodBot: I'm CodBot, your chat amiga!")

        elif "how are you" in user_input or "how are you feeling" in user_input:
            print("CodBot: I'm feeling great! Thanks for asking. How are *you* feeling today?")

        elif user_input in ["i am fine", "i'm fine", "i am happy", "i'm happy"]:
            print("CodBot: That’s awesome to hear!")

        elif user_input in ["i am sad", "i'm sad", "feeling low", "not good"]:
            print("CodBot: I'm here for you. Want me to tell you a joke? (yes/no)")
            response = input("You: ").lower()
            if response == "yes":
                print("CodBot:", random.choice(jokes))
            elif response == "no":
                print("CodBot: No worries, I'm always here if you need me.")
            else:
                print("CodBot: I didn't get that, but I'm still here for you!")

        elif "joke" in user_input or "make me laugh" in user_input or "funny" in user_input:
            print("CodBot:", random.choice(jokes))

        elif user_input in ["exit", "bye", "quit"]:
            print("CodBot: Goodbye! It was nice chatting with you.")
            break

        else:
            print("CodBot: Hmm, I didn't get that. Try saying 'hi', 'i'm sad', or 'tell me a joke'!")

chatbot()
