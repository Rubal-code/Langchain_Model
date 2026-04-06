from langchain_openai import OpenAI
from dotenv import load_dotenv     # used to load environment variables from .env file

load_dotenv()
# Create an instance of the OpenAI class
llm=OpenAI(model="gpt-3.5-turbo-instruct")
# test the model by asking a question
response=llm.invoke("What is the capital of France?")
print(response)

