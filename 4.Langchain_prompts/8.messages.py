from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

# Create an instance of the Groq class
groq_model=ChatGroq(model="llama-3.3-70b-versatile",temperature=0,max_tokens=10000,timeout=None,max_retries=2)

messages=[
    SystemMessage(content="You are a helpful assistant that provides concise answers.",additional_kwargs={"role":"system"},response_format="text"),
    HumanMessage(content="What is the capital of France?")
]   
response = groq_model.invoke(messages)

messages.append(AIMessage(content=response.content))
print("Chat history:", messages)