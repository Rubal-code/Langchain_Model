from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0,max_tokens=1000)
response=model.invoke("a roadmap to learn generative AI?")
print(response.content)