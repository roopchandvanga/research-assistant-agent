from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import streamlit as st
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(model="gpt-4", temperature=0, api_key=OPENAI_API_KEY)

def infer_topic(text: str) -> str:
    prompt = f"""
    You are a research assistant. Given the abstract below, identify the main topic or research domain. 
    Be specific (e.g., "transformers in biomedical NLP" or "unsupervised graph learning for protein interaction").

    Abstract:
    {text}

    Topic:
    """
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content.strip()
