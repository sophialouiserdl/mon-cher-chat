#  Mon Cher Chat: Private Local LLM Chatbot 🐱🎀

## Project Overview

[cite_start]**Mon Cher Chat** is a conversational chatbot prototype showcasing the capability to run a high-performance Large Language Model (LLM), **DeepSeek-R1** [cite: 29][cite_start], entirely on a local machine[cite: 2]. [cite_start]We use **Ollama** as the LLM runtime [cite: 5, 25] [cite_start]and **Streamlit** to build a friendly, interactive web interface[cite: 15, 149].

[cite_start]This project emphasizes **data privacy**[cite: 25], full **control over the AI environment**, and a lean, efficient architecture perfect for a technical portfolio.

### 🔎 Technical Highlights

* [cite_start]**Local-First Execution:** Ensures all conversations and data remain securely on your machine, eliminating the need for cloud dependencies or external API calls[cite: 25].
* [cite_start]**High-Performance LLM:** Utilizes the **DeepSeek-R1** open reasoning model [cite: 29][cite_start], known for its performance comparable to leading models, such as O3 and Gemini 2.5 Pro[cite: 29].
* [cite_start]**Conversational Memory:** Implements state management (`st.session_state`) [cite: 217] [cite_start]to maintain the full conversation history[cite: 18], allowing the AI to generate coherent, context-aware responses over long dialogues.
* [cite_start]**Custom Streamlit UI:** Features a responsive, modern chat interface developed quickly using Python[cite: 149].

## 🔎 Architecture and Technologies

| Category | Tool / Technology | Role in the Project |
| :--- | :--- | :--- |
| **LLM (Model)** | **DeepSeek-R1:1.5b** | [cite_start]The core model responsible for all response generation[cite: 31]. |
| **LLM Runtime** | **Ollama** | [cite_start]Manages, serves, and exposes the LLM via a local API endpoint[cite: 5]. |
| **Interface Web** | **Streamlit** | [cite_start]Python framework used for rapid front-end development[cite: 149]. |
| **Logic** | **Python 3.x + LangChain** | [cite_start]Primary language and framework for handling model communication, memory, and application logic[cite: 152]. |
| **Source Code** | `app.py` | The main script orchestrating the UI, memory, and the critical `llm.invoke()` calls. |

## 🔎 Setup and Installation Guide

[cite_start]To run this chatbot, you must have **Git** [cite: 24][cite_start], **Python**, and the **Ollama** application installed on your machine[cite: 5].

### Step 1: Configure Environment and LLM

1.  [cite_start]**Install Ollama** (if you haven't already)[cite: 5].
2.  **Download the DeepSeek-R1 model:**
    ```bash
    [cite_start]ollama pull deepseek-r1:1.5b [cite: 32]
    ```

### Step 2: Clone and Install Dependencies

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sophialouiserdl/mon-cher-chat-llm.git](https://github.com/sophialouiserdl/mon-cher-chat-llm.git)
    cd mon-cher-chat
    ```
2.  **Install Python dependencies** (from `requirements.txt`):
    ```bash
    pip install -r requirements.txt
    ```

### Step 3: Run the Chatbot

1.  Ensure the **Ollama** application is running in the background.
2.  Execute the Streamlit application:
    ```bash
    streamlit run app.py
    ```
The chat interface will automatically open in your web browser.

---

## ✅ Live Demonstration

[cite_start]The following screenshots illustrate the **Mon Cher Chat** interface, showcasing the custom design [cite: 274] and the DeepSeek-R1 model's conversational output.

<p align="center">
  <img src="assets/demo_chat.jpg" alt="Mon Cher Chat Chatbot Demonstration #1: Initial Interface" width="750"/>
</p>

<p align="center">
  <img src="assets/demo_chat2.jpg" alt="Mon Cher Chat Chatbot Demonstration #2: Conversation in progress" width="750"/>
</p>

<p align="center">
  <img src="assets/demo_chat3.jpg" alt="Mon Cher Chat Chatbot Demonstration #3: Conversational Memory" width="750"/>
</p>

---