import streamlit as st
from langchain_ollama import ChatOllama

## Comando input p/ ser um componente ao enviar as dúvidas e entende-lo com usuario humano 
## e plotar no chat msg. Invocando a LLM.

llm = ChatOllama(model='deepseek-r1:1.5b', 
                base_url='http://localhost:11434')

st.set_page_config(page_title='Chat DeepSeek', layout='centered')
st.title('Teste com DeepSeek')

in_message = st.chat_input ('Send your question:')
if in_message:
    chat = st.chat_message('human')
    chat.markdown(in_message)
    response = llm.invoke(in_message)
    chat = st.chat_message('ia')
    chat.markdown(response.content)
