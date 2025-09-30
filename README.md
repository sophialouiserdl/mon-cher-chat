#  Mon Cher Chat: Private Local LLM Chatbot 🐈🎀

## Project Overview

**Mon Cher Chat** is a conversational chatbot prototype showcasing the capability to run a high-performance Large Language Model (LLM), **DeepSeek-R1**, entirely on a local machine. We use **Ollama** as the LLM runtime and **Streamlit** to build a friendly, interactive web interface.

This project emphasizes **data privacy**, full **control over the AI environment**, and a lean, efficient architecture perfect for a technical portfolio.

### 🔎 Technical Highlights

* **Local-First Execution:** Ensures all conversations and data remain securely on your machine, eliminating the need for cloud dependencies or external API calls.
* **High-Performance LLM:** Utilizes the **DeepSeek-R1** open reasoning model, known for its performance comparable to leading models, such as O3 and Gemini 2.5 Pro.
* **Conversational Memory:** Implements state management (`st.session_state`) to maintain the full conversation history, allowing the AI to generate coherent, context-aware responses over long dialogues.
* **Custom Streamlit UI:** Features a responsive, modern chat interface developed quickly using Python.

## 🔎 Architecture and Technologies

| Category | Tool / Technology | Role in the Project |
| :--- | :--- | :--- |
| **LLM (Model)** | **DeepSeek-R1:1.5b** | The core model responsible for all response generation. |
| **LLM Runtime** | **Ollama** | Manages, serves, and exposes the LLM via a local API endpoint. |
| **Interface Web** | **Streamlit** | Python framework used for rapid front-end development. |
| **Logic** | **Python 3.x + LangChain** | Primary language and framework for handling model communication, memory, and application logic. |
| **Source Code** | `app.py` | The main script orchestrating the UI, memory, and the critical `llm.invoke()` calls. |

## 🔎 Setup and Installation Guide

To run this chatbot, you must have **Git**, **Python**, and the **Ollama** application installed on your machine.

### Step 1: Configure Environment and LLM

1.  **Install Ollama** (if you haven't already).
2.  **Download the DeepSeek-R1 model:**
    ```bash
    ollama pull deepseek-r1:1.5b
    ```

### Step 2: Clone and Install Dependencies

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sophialouiserdl/mon-cher-chat.git](https://github.com/sophialouiserdl/mon-cher-chat.git)
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

## 🟢 Live Demonstration

The following screenshots illustrate the **Mon Cher Chat** interface, showcasing the custom design and the DeepSeek-R1 model's conversational output.

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