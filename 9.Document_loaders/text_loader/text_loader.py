import warnings
warnings.filterwarnings("ignore")
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader

load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Write a summary for the following poem - \n {poem}")
])

parser = StrOutputParser()
loader = TextLoader("9.Document_loaders/text_loader/cricket.txt", encoding="utf-8")
docs=loader.load()
print(docs)
print(type(docs))
print(len(docs))

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))