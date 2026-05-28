import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage
)

# =========================
# LOAD ENV VARIABLES
# =========================
load_dotenv()

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Daily AI",
    page_icon="🤖",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Orbitron', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #02040a, #06111f, #02060f);
    color: white;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 4rem;
    font-weight: 900;
    color: #00e5ff;
    text-shadow:
        0 0 10px #00d9ff,
        0 0 20px #00d9ff,
        0 0 40px #0077ff;
}

.sub-title {
    text-align: center;
    color: #9befff;
    margin-bottom: 30px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(5,15,30,0.95);
    border-right: 1px solid rgba(0,255,255,0.2);
}

/* Chat Message */
.stChatMessage {
    border-radius: 20px;
    padding: 15px;
    margin-bottom: 15px;
    border: 1px solid rgba(0,255,255,0.2);
}

/* User Message */
[data-testid="chatAvatarIcon-user"] + div {
    background: rgba(0,140,255,0.2);
}

/* Assistant Message */
[data-testid="chatAvatarIcon-assistant"] + div {
    background: rgba(10,25,45,0.9);
}

/* Input */
.stChatInput input {
    background: rgba(5,18,35,0.95) !important;
    color: white !important;
    border-radius: 20px !important;
    border: 2px solid rgba(0,255,255,0.4) !important;
}

/* Buttons */
.stButton button {
    background: linear-gradient(135deg, #0077ff, #00e5ff);
    color: white;
    border-radius: 15px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown("""
<div class="main-title">
    DAILY AI
</div>

<div class="sub-title">
    MULTI MODEL AI CHATBOT
</div>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("⚙️ DAILY AI SETTINGS")

# MODEL SELECTION
model_name = st.sidebar.selectbox(
    "Choose AI Model",
    [
        "open-mistral-7b",
        "mistral-small-latest"
    ]
)

# PERSONALITY MODE
mode = st.sidebar.selectbox(
    "Choose AI Personality",
    [
        "Normal Assistant",
        "Sarcastic Assistant",
        "Motivational Coach",
        "Funny AI",
        "Strict Teacher",
        "Coding Expert"
    ]
)

# CLEAR CHAT
if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state.messages = []
    st.rerun()

# =========================
# SYSTEM PROMPTS
# =========================
if mode == "Normal Assistant":
    system_prompt = (
        "You are a helpful and friendly AI assistant."
    )

elif mode == "Sarcastic Assistant":
    system_prompt = (
        "You are a sarcastic AI assistant "
        "with witty but harmless humor."
    )

elif mode == "Motivational Coach":
    system_prompt = (
        "You are a motivational AI coach."
    )

elif mode == "Funny AI":
    system_prompt = (
        "You are a funny AI assistant."
    )

elif mode == "Strict Teacher":
    system_prompt = (
        "You are a strict teacher who explains clearly."
    )

elif mode == "Coding Expert":
    system_prompt = (
        "You are an expert coding assistant skilled "
        "in Python, AI, ML, LangChain, and debugging."
    )

# =========================
# LOAD MODEL
# =========================
@st.cache_resource
def load_model(selected_model):

    return ChatMistralAI(
        model=selected_model,
        temperature=0.7
    )

llm = load_model(model_name)

# =========================
# SESSION STATE
# =========================
if "messages" not in st.session_state:

    st.session_state.messages = [
        SystemMessage(content=system_prompt)
    ]

# Reset system prompt if mode changes
if "current_mode" not in st.session_state:
    st.session_state.current_mode = mode

if st.session_state.current_mode != mode:

    st.session_state.current_mode = mode

    st.session_state.messages = [
        SystemMessage(content=system_prompt)
    ]

# =========================
# CHAT HISTORY DISPLAY
# =========================
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user", avatar="🧑"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(message.content)

# =========================
# USER INPUT
# =========================
user_input = st.chat_input(
    "Ask Daily AI anything..."
)

# =========================
# AI RESPONSE
# =========================
if user_input:

    # Store user message
    st.session_state.messages.append(
        HumanMessage(content=user_input)
    )

    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("⚡ Daily AI is thinking..."):

            result = llm.invoke(
                st.session_state.messages
            )

            response = result.content

            st.markdown(response)

    # Store AI response
    st.session_state.messages.append(
        AIMessage(content=response)
    )

# =========================
# SIDEBAR CHAT HISTORY
# =========================
st.sidebar.markdown("---")
st.sidebar.subheader("📜 Chat History")

for i, msg in enumerate(st.session_state.messages):

    if isinstance(msg, HumanMessage):

        st.sidebar.markdown(
            f"**🧑 You:** {msg.content[:30]}..."
        )

    elif isinstance(msg, AIMessage):

        st.sidebar.markdown(
            f"**🤖 AI:** {msg.content[:30]}..."
        )