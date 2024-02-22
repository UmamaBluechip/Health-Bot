import streamlit as st
from transformers import pipeline

pipe = pipeline("text-generation", model="mistralai/Mixtral-8x7B-Instruct-v0.1")


prompt_input = (
    "The conversation between human and AI medical assistant.\n"
    "[|Human|] {input}\n"
    "[|AI|]"
)

# Chat history
chat_history = st.session_state.chat_history = []

# Input and Button
user_input = st.text_input("Ask me anything about health:")
if st.button("Ask"):

    # Generate response
    def generate_response(prompt):
        sentence = prompt.format_map({'input': user_input})
        response = pipe(sentence, max_length=500, num_return_sequences=1)
        return response

    # Update chat history and display response
    chat_history.append(f"[Human]: {user_input}")
    chat_history.append(f"[AI]: {generate_response(prompt_input)}")
    st.empty().write("\n".join(chat_history))
    st.text_input.empty()

