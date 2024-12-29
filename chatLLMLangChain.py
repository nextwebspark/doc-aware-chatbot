from langchain.chat_models import ChatOpenAI

import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

llm_model=os.environ['OPENAI_API_MODEL']


chat = ChatOpenAI(temperature=0.0, model=llm_model)