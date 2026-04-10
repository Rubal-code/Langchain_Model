from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Initialize model
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    max_tokens=100
)
# create a dynamic question prompt template
prompt=PromptTemplate(
    input_variables=["topic"],
    template="What are the key concepts to understand about {topic}?"
)

# inject the values dynamically into the prompt template
final_prompt=prompt.format(topic="quantum computing")

response=model.invoke(final_prompt)
print(response.content)