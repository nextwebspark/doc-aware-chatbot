# Custom Chatbot with RAG (Retrieval-Augmented Generation)

This is a prototype for a customizable chatbot that uses LangChain and OpenAI's GPT model. Initially set up as a simple conversational agent with Streamlit, the project is designed to be extended into a sophisticated chatbot that leverages **Retrieval-Augmented Generation (RAG)** for answering questions based on specific documents.

## Features

- **Chatbot Core**: A simple conversational agent using OpenAI’s GPT model integrated through LangChain.
- **Streamlit Interface**: A web interface for interacting with the chatbot in real-time.
- **Conversation History**: Maintains a history of the conversation for context-aware responses.
- **Easy to Extend**: Modular design to easily integrate more advanced techniques like RAG in the future.

## Project Overview

1. **Initial Setup**: 
   - Simple chatbot using LangChain with OpenAI's GPT-3 model.
   - Streamlit web interface for interaction.
   
2. **Future Plans**:
   - Implement Retrieval-Augmented Generation (RAG) for document-based answers.
   - Integrate custom document databases or knowledge sources to make the chatbot aware of specific content.
   - Provide the option to upload documents and have the chatbot extract relevant information from them to answer questions.

## Setup Instructions

### Prerequisites
1. **Python 3.7+**
2. **OpenAI API Key**: You will need an OpenAI API key to interact with the GPT model. If you don't have one, sign up on [OpenAI's website](https://beta.openai.com/signup/).
3. **Dependencies**: Install the required Python libraries using the following command:

   ```bash
   pip install streamlit openai langchain
