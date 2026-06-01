from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

prompt1=PromptTemplate(
    template="discuss about the {topic} in detail?",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="what are the advantages of {text}?",
    input_variables=["text"]
)

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

parser = StrOutputParser()

chain = prompt1 | model | parser | RunnableLambda(lambda x: {"text": x}) | prompt2 | model | parser

result = chain.invoke({
    "topic": "Python programming language"
})
print(result)
