# Extended Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower().strip()  # Normalize input
    
    # Greetings
    if user_input in ["hello", "hi", "hey", "good morning", "good evening"]:
        return "Hello there! "
    
    # Asking about wellbeing
    elif user_input in ["how are you", "how are you doing", "how's it going"]:
        return "I'm doing great, thanks for asking! How about you?"
    
    # Responding to thanks
    elif user_input in ["thank you", "thanks"]:
        return "You're welcome! "
    
    # Exit command
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a nice day! "
    
    # Default reply
    else:
        return "Hmm, I’m not sure how to respond to that yet ."

# Main program loop
def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot . Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        if user_input.lower() in ["bye", "goodbye", "see you"]:
            break

# Run chatbot
chatbot()
