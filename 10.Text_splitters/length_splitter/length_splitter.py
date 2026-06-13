from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('bank_clerk_resume.pdf')

docs=loader.load()

splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0 , separator='\n')

result = splitter.split_documents(docs)

print(result[0].content)