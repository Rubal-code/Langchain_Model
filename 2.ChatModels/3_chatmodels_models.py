from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv     # used to load environment variables from .env file

load_dotenv()
# Create an instance of the Google Generative AI class
google_model=ChatGoogleGenerativeAI(model='gemini-2.0-flash')
result=google_model.invoke("What is the capital of France?")
print(result.content)


# paid api