from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate\

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.9)

# detailed prompt
template1 = ChatPromptTemplate(
    input_variables=["input"],
    template="explain about this {input} in detail?"
)

# summary prompt
template2 = ChatPromptTemplate(
    input_variables=["input"],
    template="explain about this {input} as a summary ?"
)
# without stroutputparser, the output will be in the form of a message object which contains the content and other metadata. By using stroutputparser, we can extract just the content of the message as a string, which is more convenient for further processing or displaying to the user.

prompt1=template1.invoke({"input": "india"})

result1=model.invoke(prompt1) # this will return a detailed explanation about india

prompt2=template2.invoke({"input": result1.content})

result2=model.invoke(prompt2) # this will return a summary of the detailed explanation about india

print(result1.content)



# stroutputparser will be used below

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)