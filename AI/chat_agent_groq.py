import os
import httpx
from dotenv import load_dotenv
from groq import Groq

# Load your GROQ_API_KEY from .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Groq client with SSL bypass
client = Groq(api_key=api_key, http_client=httpx.Client(verify=False))

# Initialize message history
conversation = [
    {"role": "system", "content": "You are a helpful and conversational assistant."}
]

def chat():
    print("🧠 Groq Chat Agent (type 'exit' to quit)")
    while True:
        user_input = input("👤 You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # Append user message
        conversation.append({"role": "user", "content": user_input})

        # Get response from Groq
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=conversation
        )
        reply = response.choices[0].message.content.strip()

        # Print and save assistant message
        print(f"🤖 Groq: {reply}\n")
        conversation.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    chat()
