from langchain_groq import ChatGroq
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Initialize model
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3   # lower = more structured & reliable output
)

# Define schema
schema = [
    ResponseSchema(name="name", description="the name of the person"),
    ResponseSchema(name="age", description="the age of the person"),
    ResponseSchema(name="country", description="the country of the person")
]

# Create parser
parser = StructuredOutputParser.from_response_schemas(schema)

# Create prompt
template = ChatPromptTemplate.from_template(
    "Extract the name, age and country from this text:\n"
    "{input}\n\n"
    "{format_instructions}"
)

# Inject format instructions
prompt = template.partial(
    format_instructions=parser.get_format_instructions()
)

# Chain
chain = prompt | model | parser

# Run
result = chain.invoke({
    "input": "my name is john, i am 25 years old and i am from USA"
})

print(result)