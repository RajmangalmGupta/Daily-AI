from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# ---------------- LOAD ENV ----------------
load_dotenv()

# ---------------- INITIALIZE MODEL ----------------
llm = ChatMistralAI(
    model="open-mistral-7b",
    temperature=0.7,
)

# ---------------- AI MODES ----------------
print("\n========== CHOOSE YOUR AI MODE ==========\n")

print("1. Normal Assistant")
print("2. Sarcastic Assistant")
print("3. Motivational Coach")
print("4. Funny AI")
print("5. Strict Teacher")
print("6. Coding Expert")

mode = input("\nEnter mode number: ")

# ---------------- SYSTEM PROMPTS ----------------
if mode == "1":
    system_message = "You are a helpful and friendly AI assistant."

elif mode == "2":
    system_message = (
        "You are a sarcastic AI assistant. "
        "You respond with witty sarcasm but remain harmless."
    )

elif mode == "3":
    system_message = (
        "You are a motivational AI coach who inspires users "
        "to work hard and stay disciplined."
    )

elif mode == "4":
    system_message = (
        "You are a funny AI assistant who tells jokes "
        "and responds humorously."
    )

elif mode == "5":
    system_message = (
        "You are a strict teacher who explains concepts "
        "clearly and pushes students to improve."
    )

elif mode == "6":
    system_message = (
        "You are an expert AI coding assistant skilled in "
        "Python, AI, ML, LangChain, and debugging."
    )

else:
    print("\nInvalid mode selected. Defaulting to Normal.\n")

    system_message = (
        "You are a helpful and friendly AI assistant."
    )

# ---------------- CHAT START ----------------
print("\n------------------------------------------")
print("🤖 Welcome to the AI Chatbot!")
print("Type 'exit' to quit.")
print("------------------------------------------\n")

# ---------------- MESSAGE HISTORY ----------------
messages = [
    SystemMessage(content=system_message)
]

# ---------------- CHAT LOOP ----------------
while True:

    prompt = input("You: ")

    # Exit condition
    if prompt.lower() == "exit":
        print("\n👋 Goodbye!\n")
        break

    # Add user message
    messages.append(HumanMessage(content=prompt))

    # Get AI response
    result = llm.invoke(messages)

    # Store AI response
    messages.append(
        AIMessage(content=result.content)
    )

    # Print response
    print(f"\n🤖 Chatbot: {result.content}\n")
