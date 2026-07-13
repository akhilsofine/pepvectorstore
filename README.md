# 📚 ChromaDB Vector Store using LangChain & OpenAI

A simple project demonstrating how to build and interact with a **vector database** using **LangChain**, **ChromaDB**, and **OpenAI Embeddings**. This project showcases storing documents, performing semantic similarity search, filtering using metadata, updating documents, and deleting documents.

---

## 🚀 Features

- ✅ Create vector embeddings using OpenAI Embeddings
- ✅ Store documents in ChromaDB
- ✅ Semantic similarity search
- ✅ Similarity search with relevance scores
- ✅ Metadata filtering
- ✅ Retrieve documents using IDs
- ✅ Update existing documents
- ✅ Delete documents
- ✅ Persistent local vector database

---

## 🛠️ Tech Stack

- Python 3.13
- LangChain
- ChromaDB
- OpenAI Embeddings
- python-dotenv

---

## 📂 Project Structure

```
pepvectorstore/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── my_file_db/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/pepvectorstore.git
cd pepvectorstore
```

### 2. Create a virtual environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install langchain
pip install langchain-openai
pip install langchain-chroma
pip install chromadb
pip install python-dotenv
```

---

### 4. Create a .env file

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run

```bash
python main.py
```

---

# Project Workflow

### Step 1

Create sample documents using LangChain's `Document` class.

### Step 2

Generate embeddings using OpenAI's embedding model.

### Step 3

Store embeddings in a persistent ChromaDB collection.

### Step 4

Perform semantic similarity search.

Example:

```
Who among these is a physicist?
```

---

### Step 5

Retrieve similarity scores.

---

### Step 6

Filter documents using metadata.

Example:

```python
filter={"country":"India"}
```

---

### Step 7

Retrieve stored documents using IDs.

---

### Step 8

Update document information.

---

### Step 9

Delete documents from the vector database.

---

## 📌 Sample Documents

- Albert Einstein
- Mahatma Gandhi
- Marie Curie
- Leonardo da Vinci
- Martin Luther King Jr.

Each document contains metadata including:

- Country
- Field

---

## 📈 Example Queries

```
Who among these is a physicist?

Tell me about India's leader.

Which scientist worked on radioactivity?

Show artists from Italy.
```

---

## 💡 Learning Outcomes

This project demonstrates:

- Vector Embeddings
- Semantic Search
- Vector Databases
- Metadata Filtering
- Document CRUD Operations
- LangChain Integration
- ChromaDB Persistence
- OpenAI Embeddings

---

## 🔮 Future Improvements

- Streamlit UI
- PDF ingestion
- Multi-document upload
- Retrieval-Augmented Generation (RAG)
- Conversational chatbot
- Hybrid search
- Support for multiple embedding models

---

## 👨‍💻 Author

**Akhil Raj R**

GitHub: https://github.com/akhilsofine

---

## ⭐ If you found this project useful, consider giving it a star!
