from langchain_openai import ChatOpenAI
from dotenv import load_dotenv     # used to load environment variables from .env file
load_dotenv()   
# Create an instance of the ChatOpenAI class
chat_model=ChatOpenAI(model="gpt-3.5-turbo-instruct")

response = chat_model.invoke("What is the capital of France?")
print(response.content)