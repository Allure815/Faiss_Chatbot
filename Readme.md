

**🤖 FAISS Semantic Search Chatbot**

A semantic knowledge-retrieval chatbot that finds answers by meaning, not keywords — built on Sentence Transformer embeddings and a FAISS vector index.

Built end-to-end: embedding generation → FAISS index construction → similarity-search retrieval → interactive Streamlit app.

---

**💡 Why This Matters**

Keyword search fails the moment a question is phrased differently from the source text. This project solves that by converting both the knowledge base and the user's query into dense vector embeddings, then retrieving the closest match by semantic similarity — the same core retrieval technique behind modern RAG (Retrieval-Augmented Generation) systems used in production AI search and support tools.

Input: a natural-language question → Output: the most semantically relevant document(s) from the knowledge base.

----


**⚙️ Key Features
**

🔍 Semantic search via all-MiniLM-L6-v2 sentence embeddings (no keyword matching)

⚡ Fast nearest-neighbor retrieval using a FAISS IndexFlatL2 vector index

🎨 Interactive Streamlit UI — ask a question, get ranked relevant results

🧩 Simple, extensible knowledge base structure — add documents and rebuild the index in seconds

---



**🧠 How It Works
**

-Each document in the knowledge base is embedded into a dense vector using a Sentence Transformer model

-Embeddings are indexed with FAISS for fast similarity search

-A user's question is embedded using the same model

-FAISS retrieves the nearest document vector(s) by L2 distance

-The most relevant document is returned and displayed in the UI


This is a retrieval system — it returns the most relevant stored knowledge directly, rather than generating a new answer with an LLM. That retrieval layer is exactly the foundation a generative RAG pipeline is built on top of.

----


🛠️ **Tech Stack**


Vector Search: FAISS

Embeddings: Sentence Transformers (all-MiniLM-L6-v2)

Interface: Streamlit

Language: Python

---



**Demo Screenshot**
https://github.com/Allure815/Faiss_Chatbot/blob/main/FAISS-ss.png

---

**Demo Video**
https://github.com/Allure815/Faiss_Chatbot/blob/main/Demo-FAISS.mp4

---


****▶️ Run It Locally**

bash# Clone
git clone https://github.com/Allure815/Faiss_Chatbot.git
cd Faiss_Chatbot

# Install dependencies
pip install -r requirements.txt

# Build the FAISS index
python build_index.py

# Launch the app
streamlit run app.py

------

The app opens automatically in your browser. Try questions like "What is Python?" or "What is FAISS?"

---


**🔭 What's Next**


Add an LLM generation layer on top of retrieval to turn this into a full RAG chatbot (answer synthesis, not just document lookup)
Expand the knowledge base beyond the current sample set and support ingesting PDFs/docs directly
Swap IndexFlatL2 for an approximate index (e.g. IndexIVFFlat) to scale to larger document collections
Add source citations in the UI so users see exactly which document an answer came from

-----


**Example Questions**

You can ask questions such as:

-What is Python?

-What is SQL?

-What is FAISS?

-What is Streamlit?


The chatbot will retrieve the most relevant information from its knowledge base.

-----

👤 Author

Heeral — https://github.com/Allure815/
---


