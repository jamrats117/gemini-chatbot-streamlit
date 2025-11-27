import streamlit as st
from google import genai

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

st.title("🤖 Gemini Chatbot – Streamlit Cloud Demo")

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

if "history" not in st.session_state:
    st.session_state.history = []

# show chat
for role, msg in st.session_state.history:
    with st.chat_message(role):
        st.write(msg)

# input
user_msg = st.chat_input("ถามอะไรก็ได้…")

if user_msg:
    st.session_state.history.append(("user", user_msg))
    with st.chat_message("user"):
        st.write(user_msg)

    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=user_msg
    )

    bot_text = response.text
    st.session_state.history.append(("assistant", bot_text))

    with st.chat_message("assistant"):
        st.write(bot_text)
