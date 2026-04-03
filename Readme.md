
FAISS Knowledge-Based Chatbot

Overview
This project is a simple AI knowledge-based chatbot that retrieves relevant information from a predefined text knowledge base.

Instead of traditional keyword matching, the chatbot converts text into vector embeddings and uses similarity search to find the most relevant answer.

The chatbot is built using Python and provides a simple web interface where users can ask questions and receive relevant information from the stored knowledge base.

---

Features

Semantic search using embeddings
Fast similarity search using FAISS
Interactive web interface built with Streamlit
Simple knowledge base created using text data

---

Technologies Used

Python
FAISS (vector similarity search library)
Sentence Transformers (embedding model library)
Streamlit (Python web application framework)

---

How It Works

1. A small text knowledge base is created inside the project.

2. Each document in the knowledge base is converted into embeddings using a Sentence Transformer model.

3. The embeddings are stored in a FAISS vector index.

4. When a user asks a question, the query is also converted into an embedding.

5. FAISS searches the vector index to find the most similar documents.

6. The chatbot displays the most relevant knowledge to the user in the interface.

---

Demo Screenshot
https://github.com/Allure815/Faiss_Chatbot/blob/main/FAISS-ss.png

---

Demo Video
https://github.com/Allure815/Faiss_Chatbot/blob/main/Demo-FAISS.mp4

---

Installation

Install the required dependencies using:

pip install -r requirements.txt

---

Run the Project

First build the FAISS index:

python build_index.py

Then run the chatbot application:

streamlit run app.py

The chatbot will open automatically in your web browser.

---

Example Questions

You can ask questions such as:

What is Python?
What is SQL?
What is FAISS?
What is Streamlit?

The chatbot will retrieve the most relevant information from its knowledge base.


