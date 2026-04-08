import streamlit as st
from Chatbot import get_response, set_mode

st.title("🤖 Mood based Chatbot")

# Mood selector in sidebar
mood_options = {"😊 Helpful": 1, "😠 Angry": 2, "😢 Sad": 3}
selected_label = st.sidebar.selectbox("Select Mood", list(mood_options.keys()))
selected_mode = mood_options[selected_label]

# Re-initialize memory when mood changes
if st.session_state.get("current_mode") != selected_mode:
    st.session_state["current_mode"] = selected_mode
    st.session_state["chat_history"] = []
    set_mode(selected_mode)

for role, content in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(content)

user_input = st.chat_input("You:")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_response(user_input)
        st.markdown(response)

    st.session_state.chat_history.append(("assistant", response))