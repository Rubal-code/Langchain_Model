from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv     # used to load environment variables from .env file
import os
load_dotenv(dotenv_path="../.env")
print("API KEY:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))


llm=HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model=ChatHuggingFace(llm=llm)

result=model.invoke("what is the capital of India ?")

print(result.content)