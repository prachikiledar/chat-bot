import streamlit as st
import os
from google.generativeai import chat

# Load secrets from .env
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Generative AI
chat.api_key = GOOGLE_API_KEY

# Streamlit App
st.set_page_config(page_title="AI Query App")
st.title("AI Query Application")

query = st.text_input("Enter your query:")
if st.button("Submit"):
    response = chat.chat(query)
    st.write("Response:", response["text"])
