from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
# Create an instance of the Groq class
groq_model=ChatGroq(model="llama-3.3-70b-versatile",temperature=0,max_tokens=10000,timeout=None,max_retries=2)
chat_history = []

while True:
    user_input = input("enter the query: ")
    chat_history.append({"role": "user", "content": user_input})
    if user_input.lower() in ["exit","quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response = groq_model.invoke(chat_history)
    chat_history.append({"role": "assistant", "content": response.content})
    print("Chatbot response:", response.content)
print("Chat history:", chat_history)