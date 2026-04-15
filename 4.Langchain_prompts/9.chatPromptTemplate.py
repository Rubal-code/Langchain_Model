# chatPromoteTemplate is used to create a prompt template for a chat-based model. It allows you to define the structure of the conversation and specify how the model should respond to different inputs. This is particularly useful for creating chatbots or conversational agents that need to maintain context and provide relevant responses based on user input. The ChatPromptTemplate can include placeholders for user input, system instructions, and other relevant information to guide the model's responses effectively.
from langchain_core.prompts import ChatPromptTemplate
# Define a chat prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that provides {length} answers."),
    ("human", "What is the capital of {country}?"),
    ("ai", "{response}")
])
prompt.invoke({"length": "concise", "country": "France", "response": "The capital of France is Paris."})
print(prompt)