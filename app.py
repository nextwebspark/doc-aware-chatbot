# app.py

import streamlit as st
from chatLLMOpenAI import get_completion
from chatLLMLangChain import chat

# Initialize Streamlit UI
st.title("Chatbot Prototype")

# Display a text input box for user query
user_input = st.text_input("Ask me anything:")

if user_input:
    # Pass the user input to the llm_chain for processing
    response = get_completion(user_input)

    # Display the chatbot's response
    st.write("Assistant:", response)

if user_input:
    # Pass the user input to the llm_chain for processing
    response = chat.invoke(user_input)

    # Display the chatbot's response
    st.write("Assistant:", response.content)
