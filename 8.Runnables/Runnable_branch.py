from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

parser = StrOutputParser()

tweet_prompt = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)

linkedin_prompt = PromptTemplate(
    template="Generate a LinkedIn post about {topic}",
    input_variables=["topic"]
)

tweet_chain = tweet_prompt | model | parser

linkedin_chain = linkedin_prompt | model | parser

branch_chain = RunnableBranch(
    (
        lambda x: x["topic"].lower() == "cricket",
        tweet_chain
    ),
    linkedin_chain
)

print(branch_chain.invoke({"topic": "cricket"}))