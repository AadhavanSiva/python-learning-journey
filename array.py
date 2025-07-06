responses = {
    ("hello", "hi", "hey"): "Hello! How can I help you?",
    ("what's your name", "name", "who are you"): "I'm your friendly Python bot.",
    ("how are you", "how's it going", "how do you do"): "I'm doing great, thanks for asking!",
    ("bye", "goodbye", "see you"): "Goodbye!"
}

def smart_ai_agent():
    print("Hi! I'm your AI assistant. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        matched = False

        for keywords, response in responses.items():
            if user_input in keywords:
                print("AI:", response)
                matched = True
                if user_input in ("bye", "goodbye", "see you"):
                    return
                break

        if not matched:
            print("AI: I'm not sure how to respond to that.")

smart_ai_agent()