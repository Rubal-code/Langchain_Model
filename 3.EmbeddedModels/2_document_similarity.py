from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

document=[
    "virat kohli is the best batsman in the world",
    "jasprit bumrah is the best bowler in the world",
    "mumbai is the financial capital of the India",
    "pune is the cultural capital of the India",
    "shane warne is the best spinner in the world",
]
query="who is the best batsman in the world ?"
# embedding the document and query
document_embedding=embedding.embed_documents(document)
query_embedding=embedding.embed_query(query)
# calculating the cosine similarity between the query and document
scores=cosine_similarity([query_embedding], document_embedding)[0] # always pass 2d array to cosine_similarity function query_embedding is 1d array so we need to pass it as 2d array by wrapping it in a list

index,score=sorted(list(enumerate(scores)), key=lambda x:x[1])[-1] # it will print the index and score of each document
print("Query:", query)
print("Most similar document:", document[index])    
print("Similarity score:", score)