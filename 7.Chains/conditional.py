from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableBranch
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

positive_chain=(ChatPromptTemplate.from_template("write a thank you response for the following message: {message}") | model)

negative_chain=(ChatPromptTemplate.from_template("write an apology response to the following message: {message}") | model)

neutral_chain=(ChatPromptTemplate.from_template("write a neutral response to the following message: {message}") | model)

branch=RunnableBranch(
    (
        lambda x: "good product" in x["message"].lower(),
        positive_chain
    ),
    (
        lambda x: "bad product" in x["message"].lower(),
        negative_chain
    ),
        neutral_chain


)
parser=StrOutputParser()

chain=branch | parser
result= chain.invoke({
    "message": "I recently bought your product and it is a good product."
})
print(result)