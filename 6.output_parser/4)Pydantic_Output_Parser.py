from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

class Person(BaseModel):
    name: str = Field(description="person name")
    age: int = Field(description="person age")
    country: str = Field(description="person country")

parser = PydanticOutputParser(pydantic_object=Person)

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

prompt = ChatPromptTemplate.from_template(
    """
    Extract the information from the text.

    {format_instructions}

    Text:
    {input}
    """
)

chain = (
    prompt.partial(
        format_instructions=parser.get_format_instructions()
    )
    | model
    | parser
)

result = chain.invoke({
    "input": "My name is John. I am 25 years old and I live in USA."
})

print(result)