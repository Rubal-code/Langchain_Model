from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0,max_tokens=100)
response=model.invoke("write a poem on the stars")
print(response.content)

'''🌡️ What is temperature?

Temperature controls randomness (creativity) in the model’s output.

Think of it like:

🧊 Low temperature = safe, predictable
🔥 High temperature = creative, random'''