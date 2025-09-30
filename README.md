#  Mon Cher Chat: Private Local LLM Chatbot 🐱🎀

## Project Overview

**Mon Cher Chat** is a prototype conversational chatbot designed to demonstrate secure, high-performance AI running entirely on local hardware. The system integrates the DeepSeek-R1 large language model (LLM), using Ollama as the local runtime environment and Streamlit to provide an interactive web interface

This setup highlights a practical and cost-effective approach to modern LLM deployment. By focusing on local execution and data privacy, it offers a solid framework for building secure, customized AI tools. This approach is particularly valuable for enterprise use cases that demand strict data privacy and regulatory compliance, such as internal knowledge management or confidential document processing. Additionally, it eliminates ongoing cloud service expenses and reduces latency, proving that powerful AI models can be run affordably and securely within an organization’s own infrastructure.

### 🔎 Technical Highlights

The Mon Cher Chat application is engineered for performance, privacy, and seamless operation through the following key components:

* **Secure Local Deployment:** The entire stack, from the **DeepSeek-R1:1.5b** model to the **Streamlit UI**, is configured for local execution, ensuring **100% data privacy** and eliminating dependency on external APIs or cloud providers.
* **Persistent Context & Memory:** Conversational memory management is implemented via `st.session_state` to maintain the full conversation history. This capability allows the model to generate **coherent, context-aware responses** over long, multi-turn dialogues.
* **High-Fidelity LLM Integration:** The system leverages **Ollama** and **LangChain** to efficiently manage the DeepSeek-R1 model, which is recognized for its advanced reasoning capabilities comparable to leading proprietary models.
* **Custom User Experience:** A responsive and modern chat interface was developed using Streamlit, complemented by custom styling, ensuring a polished and intuitive user experience.

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

