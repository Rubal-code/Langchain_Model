from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a Linkedin post about {topic}",
    input_variables=["topic"]
)

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet": prompt1 | model | parser,
    "linkedin": prompt2 | model | parser
})

result = parallel_chain.invoke({"topic": "AI"})

print(result)