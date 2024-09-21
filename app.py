import streamlit as st
import chatbot_lib as cbl

st.set_page_config(page_title="Company Info Chatbot")
st.title("Company Info Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

chat_container = st.container()

input_text = st.chat_input("Ask about the company")

if input_text:
    cbl.chat_with_model(message_history=st.session_state.chat_history, new_text=input_text)

for message in st.session_state.chat_history:
    with chat_container.chat_message(message.role):
        st.markdown(message.text)