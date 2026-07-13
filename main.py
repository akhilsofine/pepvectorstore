from dotenv import load_dotenv
import os

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# ---------------------------
# Load API Key
# ---------------------------
load_dotenv()

print("API Key Loaded:", os.getenv("OPENAI_API_KEY")[:10] + "...")

# ---------------------------
# Create Documents
# ---------------------------

docs = [
    Document(
        page_content="Albert Einstein was a theoretical physicist known for developing the theory of relativity.",
        metadata={"field": "Physics", "country": "Germany"},
    ),
    Document(
        page_content="Mahatma Gandhi was a leader of India's non-violent independence movement.",
        metadata={"field": "Politics", "country": "India"},
    ),
    Document(
        page_content="Marie Curie pioneered research on radioactivity.",
        metadata={"field": "Chemistry", "country": "Poland"},
    ),
    Document(
        page_content="Leonardo da Vinci was a Renaissance artist and inventor.",
        metadata={"field": "Art", "country": "Italy"},
    ),
    Document(
        page_content="Martin Luther King Jr. fought for civil rights using non-violence.",
        metadata={"field": "Civil Rights", "country": "USA"},
    ),
]

# ---------------------------
# Create Vector Store
# ---------------------------

vector_store = Chroma(
    collection_name="sample",
    embedding_function=OpenAIEmbeddings(),
    persist_directory="my_file_db",
)

# ---------------------------
# Add Documents
# ---------------------------

ids = vector_store.add_documents(docs)

print("\nGenerated IDs:")
print(ids)

# ---------------------------
# View all stored documents
# ---------------------------

print("\nAll Documents:")
print(vector_store.get())

# ---------------------------
# Similarity Search
# ---------------------------

print("\nSimilarity Search:")

results = vector_store.similarity_search(
    query="Who among these is a physicist?",
    k=2,
)

for doc in results:
    print(doc.page_content)

# ---------------------------
# Similarity Search with Score
# ---------------------------

print("\nSimilarity Search with Scores:")

results = vector_store.similarity_search_with_score(
    query="Who among these is a physicist?",
    k=2,
)

for doc, score in results:
    print("\nScore:", score)
    print(doc.page_content)

# ---------------------------
# Metadata Filter Search
# ---------------------------

print("\nMetadata Filter:")

results = vector_store.similarity_search_with_score(
    query="leader",
    filter={"country": "India"},
)

for doc, score in results:
    print(score)
    print(doc.page_content)

# ---------------------------
# Retrieve Document by ID
# ---------------------------

print("\nRetrieve First Document:")

result = vector_store.get(ids=[ids[0]])

print(result)

# ---------------------------
# Update Document
# ---------------------------

updated_doc = Document(
    page_content="Albert Einstein revolutionized physics with relativity and contributed to quantum mechanics.",
    metadata={
        "field": "Physics",
        "country": "Germany",
        "updated": True,
    },
)

vector_store.delete(ids=[ids[0]])

vector_store.add_documents(
    [updated_doc],
    ids=[ids[0]],
)

print("\nUpdated Document:")

print(vector_store.get(ids=[ids[0]]))

# ---------------------------
# Delete Document
# ---------------------------

vector_store.delete(ids=[ids[4]])

print("\nRemaining Documents:")

print(vector_store.get())