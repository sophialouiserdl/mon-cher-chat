import streamlit as st
from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage, AIMessage

# Configura LLM DeepSeek
llm = ChatOllama(
    model='deepseek-r1:1.5b', 
    base_url='http://localhost:11434'
)

# Configuração da página
st.set_page_config(page_title="Mon Cher Chat", layout="centered")

# Inicializa mensagens
if "messages" not in st.session_state:
    st.session_state["messages"] = []

messages = st.session_state["messages"]

#  CSS para interface
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Kaushan+Script&display=swap');

.stApp {
    background-color: #ff8fb1;
}

/* Título */
.title {
    font-family: 'Kaushan Script', cursive;
    font-size: 48px;
    text-align: center;
    color: #2c2c2c;
    margin-bottom: -10px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #4a0c2e;
    margin-bottom: 20px;
}

/* Chat container */
.chat-frame {
    width: 90%;
    max-width: 750px;
    margin: auto;
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding-bottom: 20px;
}

/* Balõezinhos de mensagem */
.chat-message {
    padding: 12px 18px;
    border-radius: 20px;
    max-width: 70%;
    word-wrap: break-word;
    font-size: 16px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.1);
}

.chat-message.human {
    background-color: #ffe1eb;
    align-self: flex-start;
    border-top-left-radius: 0;
}

.chat-message.ai {
    background-color: #fce4ff;
    align-self: flex-end;
    border-top-right-radius: 0;
}

.message-container {
    display: flex;
    align-items: flex-end;
    gap: 8px;
}

.message-container.human {
    justify-content: flex-start;
}

.message-container.ai {
    justify-content: flex-end;
    flex-direction: row-reverse;
}

.avatar {
    font-size: 24px;
}
</style>
""", unsafe_allow_html=True)

# Título
st.markdown("<div class='title'>Mon Cher Chat</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Lumie welcomes you with love 💕</div>", unsafe_allow_html=True)

# Container de mensagens
chat_container = st.container()

# Entrada do usuário
user_input = st.chat_input("Type your message for Lumie...")

if user_input:
    # Armazena a pergunta do usuário
    messages.append(("human", user_input))
    
    # Prepara histórico para DeepSeek-R1
    chat_history = []
    for sender, content in messages:
        if sender == "human":
            chat_history.append(HumanMessage(content=content))
        elif sender == "ai":
            chat_history.append(AIMessage(content=content))
    
    # Chamada que retorna apenas a resposta final (corrigir, continua pensando)
    response = llm.predict_messages(chat_history)
    messages.append(("ai", response.content))

# Renderiza mensagens
with chat_container:
    st.markdown("<div class='chat-frame'>", unsafe_allow_html=True)
    for sender, msg in messages:
        if sender == "human":
            st.markdown(f"""
                <div class="message-container human">
                    <div class="avatar">👤</div>
                    <div class="chat-message human">{msg}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="message-container ai">
                    <div class="avatar">😺🎀</div>
                    <div class="chat-message ai">{msg}</div>
                </div>
            """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

