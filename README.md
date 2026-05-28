# 🤖 Daily AI — Multi Model AI Chatbot

Daily AI is a futuristic AI chatbot built using:

* Python
* Streamlit
* LangChain
* Mistral AI API

The chatbot supports:

* Multiple AI personalities
* Multiple Mistral models
* Chat history
* Futuristic cyberpunk UI
* Real-time conversations

---

# 🚀 Features

## ✅ AI Personalities

Choose different chatbot behaviors:

* Normal Assistant
* Sarcastic Assistant
* Motivational Coach
* Funny AI
* Strict Teacher
* Coding Expert

---

## ✅ Multiple Models

Supports:

* `open-mistral-7b`
* `mistral-small-latest`

---

## ✅ Chat History

* Stores conversation history
* Displays previous chats in sidebar
* Session-based memory

---

## ✅ Futuristic UI

Includes:

* Neon cyberpunk design
* Glassmorphism
* Animated effects
* Custom chat bubbles

---

# 📂 Project Structure

```bash
Generative_AI/
│
├── chatmodels/
│   ├── UIchatbot.py
│
├── .env
├── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
```

---

## 2️⃣ Move into Project Folder

```bash
cd Generative_AI
```

---

## 3️⃣ Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv .venv
```

### Windows

```bash
python -m venv .venv
```

---

## 4️⃣ Activate Virtual Environment

### Mac/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install streamlit
pip install langchain-mistralai
pip install python-dotenv
```

OR

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

Example:

```env
MISTRAL_API_KEY=your_api_key_here
```

Get API key from:
https://console.mistral.ai

---

# ▶️ Running the Application

Run the Streamlit app:

```bash
streamlit run /Users/yourname/Desktop/Generative_AI/chatmodels/UIchatbot.py
```

OR

Move into the folder:

```bash
cd chatmodels
streamlit run UIchatbot.py
```

---

# 🖥️ Local URL

After running successfully:

```bash
Local URL: http://localhost:8501
```

Open it in your browser.

---

# 🧠 Technologies Used

| Technology | Purpose               |
| ---------- | --------------------- |
| Python     | Backend               |
| Streamlit  | Web UI                |
| LangChain  | LLM Framework         |
| Mistral AI | AI Model API          |
| dotenv     | Environment Variables |

---

# 📦 Required Packages

```txt
streamlit
langchain-mistralai
python-dotenv
```

---

# 📌 Future Improvements

* Voice Assistant
* Speech-to-Text
* Text-to-Speech
* File Upload
* RAG Integration
* PDF Chat
* Database Memory
* Multi-Agent System
* Authentication System

---

# 🛠️ Troubleshooting

## Error: File does not exist

Use full file path:

```bash
streamlit run /full/path/UIchatbot.py
```

---

## Error: Missing ScriptRunContext

You are running Streamlit incorrectly.

❌ Wrong:

```bash
python UIchatbot.py
```

✅ Correct:

```bash
streamlit run UIchatbot.py
```

---

# 👨‍💻 Author

Built by Raj Gupta 🚀

---

# ⭐ If You Like This Project

Give it a star on GitHub ⭐
