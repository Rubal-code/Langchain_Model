from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "tell 5 points about {topic}?",
   
)

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({
    "topic": "Python programming language"
})
print(result)

chain.get_graph().print_ascii() # to visualize the chain structure