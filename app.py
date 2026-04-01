import streamlit as st
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load FAISS index
index = faiss.read_index("vectorstore/index.faiss")

# Load stored documents
with open("vectorstore/index.pkl", "rb") as f:
    documents = pickle.load(f)

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Search function
def search_docs(query, k=1):
    q_embedding = embed_model.encode([query])
    distances, indices = index.search(q_embedding, k)
    return [documents[i] for i in indices[0]]

# Streamlit UI
st.set_page_config(page_title="AI Knowledge Chatbot", page_icon="🤖")

st.title("🤖 My First AI Knowledge Chatbot")
st.write("Ask me anything from my knowledge base")

query = st.text_input("Enter your question")

if query:
    docs = search_docs(query)

    st.markdown("### 📚 Relevant Knowledge")

    for i, doc in enumerate(docs, 1):
        with st.expander(f"Result {i}"):
            st.write(doc)