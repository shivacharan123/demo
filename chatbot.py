
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"] = "true"

#creating chatbot 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a great helpful assistant. please provide respons to the user quastion"),
        ("user","Question:{question}")
    ]
)
#streamlit frame

st.title("Langchain Demo With llama2")
input_text = st.text_input("Ask me anything you want")

llm = Ollama(model="llama2", temperature=0)
ouput_parser = StrOutputParser()

chain = prompt | llm | ouput_parser

if input_text:
    response = chain.invoke({"question":input_text})
    st.write(response)