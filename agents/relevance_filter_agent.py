from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import streamlit as st
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]


llm = ChatOpenAI(model="gpt-4", temperature=0, api_key=OPENAI_API_KEY)

def is_relevant_to_query(abstract: str, query: str) -> bool:
    prompt = f"""
    You are a research assistant helping filter relevant academic papers.

    Query: "{query}"

    Below is an abstract from a paper. Your task is to determine whether this paper is actually relevant to the query topic.

    Respond with:
    - "yes, <reason>" if the paper is relevant
    - "no, <reason>" if it is not

    The reason should be **no more than 2 sentences**, and do not include any additional commentary or formatting.

    Abstract:
    {abstract}

    Answer:
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    content = response.content.strip().lower()

    if content.startswith("yes"):
        return {"relevant": True, "reason": content[4:].strip()}
    elif content.startswith("no"):
        return {"relevant": False, "reason": content[3:].strip()}
    else:
        return {"relevant": None, "reason": f"Unrecognized response: {content}"}
