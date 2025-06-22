from textblob import TextBlob
from colorama import Fore, Style, init
init(autoreset=True)

intents = {
    "hours": {
        "keywords": ["hours", "open", "close"],
        "response": "We are open from 9 to 5, Monday to Friday."
    },
    "return": {
        "keywords": ["refund", "money back", "return"],
        "response": "I'd be happy to help you with the return process. Let me transfer you to a live agent."
    }
}

def get_response(message,name):
    message = message.lower()
    
    for intent_data in intents.values():
        if any(word in message for word in intent_data["keywords"]):
            return intent_data["response"]
    
    sentiment = TextBlob(message).sentiment.polarity
    if sentiment > 0:
        return f"That's so great to hear, {name}!"
    elif sentiment < 0:
        return f"I'm so sorry to hear that, {name}. How can I help?"
    else:
        return f"I see. Can you tell me more about that, {name}?"

def chat():
    print(Fore.GREEN+"Chatbot: Hi whats your name?")
    user_name=input(Fore.YELLOW+"You:").strip()
    print(Fore.GREEN+f"Chatbot:Hi {user_name}. how can i be of help today?")
    while (user_message := input(Fore.YELLOW+"You: ").strip().lower()):
      if any(word  in user_message for word in ["exit", "quit", "bye"]):
        print(Fore.GREEN+f"Chatbot: Thank you for chatting, {user_name}. Have a great day!")
        break
      else:
        print(Fore.GREEN+f"\nChatbot: {get_response(user_message,user_name)}")

if __name__ == "__main__":
    chat()
