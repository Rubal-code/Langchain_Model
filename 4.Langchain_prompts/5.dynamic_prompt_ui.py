from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()
st.header("Dynamic Prompt Example")

paper_input=st.selectbox("Select a research paper", options=["Bert","GAN","VAE"], key="paper")
style_input=st.selectbox("select the writing style", options=["formal","informal"], key="style")
length_input=st.slider("Select the length of the summary", min_value=50, max_value=500, value=100, step=50, key="length")

# prompt=PromptTemplate(
#     template="""
# Please summarize the research paper titled "{paper_input}" with the following specifications:

# Explanation Style: {style_input}  
# Explanation Length: {length_input}

# 1. Mathematical Details:
#    - Include relevant mathematical equations if present in the paper.
#    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.

# 2. Analogies:
#    - Use relatable analogies to simplify complex ideas.

# If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.

# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """,
# input_variables=["paper_input","style_input","length_input"]
# )

prompt=load_prompt("6_prompt_template.json")

final_prompt = prompt.format(paper_input=paper_input, style_input=style_input, length_input=length_input)
if st.button("Generate Summary"):
    model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5, max_tokens=length_input)
    response=model.invoke(final_prompt)
    st.write(response.content)