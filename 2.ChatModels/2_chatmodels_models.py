from langchain_groq import ChatGroq
from dotenv import load_dotenv     # used to load environment variables from .env file


load_dotenv()
# Create an instance of the Groq class
groq_model=ChatGroq(model="llama-3.3-70b-versatile",temperature=0,max_tokens=100,timeout=None,max_retries=2)
response = groq_model.invoke("What is the capital of France?")
print(response.content)