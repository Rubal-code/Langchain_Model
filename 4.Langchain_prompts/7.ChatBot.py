from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage  

load_dotenv()
# Create an instance of the Groq class
groq_model=ChatGroq(model="llama-3.3-70b-versatile",temperature=0,max_tokens=10000,timeout=None,max_retries=2)
chat_history = []
messages=[
    SystemMessage(content="You are a helpful assistant that provides concise answers.",additional_kwargs={"role":"system"},response_format="text")
]

while True:
    user_input = input("enter the query: ")
    chat_history.append(HumanMessage(content=user_input, additional_kwargs={"role": "user"}, response_format="text"))
    if user_input.lower() in ["exit","quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response = groq_model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content, additional_kwargs={"role": "assistant"}, response_format="text"))
    print("Chatbot response:", response.content)
print("Chat history:", chat_history)