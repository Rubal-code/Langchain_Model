from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Static Prompt Example")

user_prompt=st.text_input("Enter your prompt here", key="prompt")

if st.button("generate response"):
    model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0,max_tokens=1000)
    response=model.invoke(user_prompt)
    st.write(response.content)
