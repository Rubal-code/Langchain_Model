from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text="Delhi is the capital of the India"
doc=[
    "delhi is the capital of the India",
    "paris is the capital of the France",
    "london is the capital of the UK",
]

vector=embedding.embed_query(text)
print(str(vector))

vector1=embedding.embed_documents(doc)
print(str(vector1))