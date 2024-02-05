import streamlit as st 
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Customize the layout
st.set_page_config(page_title="DOCAI", page_icon="🤖", layout="wide", )     
st.markdown(f"""
            <style>
            .stApp {{background-image: url("https://images.unsplash.com/photo-1509537257950-20f875b03669?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1469&q=80"); 
                     background-attachment: fixed;
                     background-size: cover}}
         </style>
         """, unsafe_allow_html=True)



st.title("📄 Document Conversation 🤖")
uploaded_files = st.sidebar.file_uploader(
    label="Upload PDF files", type=["pdf"], accept_multiple_files=True
)


msgs = StreamlitChatMessageHistory()
memory = ConversationBufferMemory(memory_key="chat_history", chat_memory=msgs, return_messages=True)


if len(msgs.messages) == 0 or st.sidebar.button("Clear message history"):
    msgs.clear()
    msgs.add_ai_message("How can I help you?")


avatars = {"human": "user", "ai": "assistant"}
for msg in msgs.messages:
    st.chat_message(avatars[msg.type]).write(msg.content)


if user_query := st.chat_input(placeholder="Ask me anything!"):
    st.chat_message("user").write(user_query)
    st.chat_message("assistant").write("sure")
    st.chat_message("user").write("or is it")

with st.chat_message("assistant"):
    placeholder = st.empty()
    full_response = ''
    for i in range(10)::
        full_response += str(i)
        placeholder.markdown(full_response)
    placeholder.markdown(full_response)
