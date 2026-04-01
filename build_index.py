import faiss
import pickle
import numpy as np
import os
from sentence_transformers import SentenceTransformer

# Correct documents (each topic separate)
documents = [
    "Python is a high-level programming language used for artificial intelligence, data science, and automation.",
    "SQL is a structured query language used to store, retrieve, and manage data in relational databases.",
    "FAISS is a vector database library developed by Facebook for fast similarity search and clustering of dense vectors.",
    "Streamlit is a Python framework that allows you to quickly build interactive web applications for machine learning projects."
]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert text to embeddings
embeddings = model.encode(documents)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Create vectorstore folder
os.makedirs("vectorstore", exist_ok=True)

# Save index
faiss.write_index(index, "vectorstore/index.faiss")

# Save documents
with open("vectorstore/index.pkl", "wb") as f:
    pickle.dump(documents, f)

print("Index built successfully!")