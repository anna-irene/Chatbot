# Simple Sentiment Chatbot 

A console-based chatbot written in Python that combines **intent matching** and **sentiment analysis**.  
This code is based on a project from the LinkedIn Learning course:  
**“Advanced Python Projects: Build AI Applications.”**

I made several improvements to optimize the code and add new features, while preserving the original structure.

---

##  Original Features (from course)

| Feature | Description |
|---------|-------------|
| **Intent Detection** | Responds to specific queries like business hours or return policy using keyword matching. |
| **Sentiment Analysis** | Uses `TextBlob` to determine the emotional tone of the user's message (positive, negative, or neutral) and respond accordingly. |

---

## My Enhancements

| Feature | What I added or improved |
|--------|---------------------------|
| **User Name Memory** | Greets the user by name and includes their name in all future responses. |
| **Colorful Console Output** | Integrated `colorama` to clearly distinguish chatbot messages (green) and user input (yellow). |
| **Bug Fix 1 – Flexible exit detection** | The chatbot used to quit **only** when the message was exactly “exit”, “bye”, or “quit”. It now exits when those words appear **anywhere** in the sentence (e.g., “Great bye”, “I have to quit now”). |
| **Bug Fix 2 – Syntax error in `intents` dictionary** | Added the missing commas between dictionary entries; without them the script raised a `SyntaxError`. |
| **Bug Fix 3 – Undefined `intent_data`** | Rewrote the intent-matching loop so `intent_data` is properly defined (`for intent_data in intents.values(): …`). Previously the code referenced `intent_data` before assignment, causing a `NameError`. |

---

##  Example Interaction

```bash
Chatbot: Hi! What's your name?
You: Anna
Chatbot: Hi Anna. How can I be of help today?
You: I'm really disappointed in my purchase
Chatbot: I'm so sorry to hear that, Anna. How can I help?
You: i want a refund
Chatbot: I'd be happy to help you with the return process. Let me transfer you to a live agent.
You: okay great bye
Chatbot: Thank you for chatting, anna. Have a great day!
```

## Install dependencies:
```bash
pip install textblob colorama
```

## Run the chatbot:
```bash
python chatbot.py
```

##  Credits

- **Course Inspiration**: [Advanced Python Projects: Build AI Applications](https://www.linkedin.com/learning/advanced-python-projects-build-ai-applications)
  <br>By: [Priya Mohan](https://www.linkedin.com/learning/instructors/priya-mohan)
