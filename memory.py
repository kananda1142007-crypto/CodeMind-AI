
import streamlit as st
from hindsight_client import Hindsight

BANK_ID = "codemind-ai"

def get_client():
    return Hindsight(
        base_url=st.secrets["HINDSIGHT_BASE_URL"],
        api_key=st.secrets["HINDSIGHT_API_KEY"]
    )

def save_memory(content):
    with get_client() as client:
        client.retain(
            bank_id=BANK_ID,
            content=content
        )
    return "Memory saved successfully!"

def recall_memory(query):
    with get_client() as client:
        result = client.recall(
            bank_id=BANK_ID,
            query=query
        )
        return [item.text for item in result.results]
