from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import os
import requests
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Load environment variables
HF_API_TOKEN = os.getenv("HF_API_TOKEN")


# FastAPI App
app = FastAPI()

# Paths to local document and vector DB
DOC_PATH = "data/doc.md"
INDEX_PATH = "vectorstore/document_index.faiss"
CHUNKS_PATH = "vectorstore/document_chunks.pkl"

class QuestionRequest(BaseModel):
    question: str

# Index local document into FAISS
def index_document(path: str):
    os.makedirs("vectorstore", exist_ok=True)
    with open(path, "r") as f:
        text = f.read()

    chunks = text.split("\n\n")
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = embedder.encode(chunks)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)
    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(chunks, f)

# Retrieve context for a given query
def retrieve_context(query: str, k=3) -> str:
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    index = faiss.read_index(INDEX_PATH)
    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)

    query_vec = embedder.encode([query])
    _, I = index.search(query_vec, k)
    return "\n\n".join([chunks[i] for i in I[0]])

# Genrate with llama
def generate_with_llama(prompt: str) -> str:
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant for a personal portfolio website. You're a great promoter"},
            {"role": "user", "content": prompt}

        ],
        "max_tokens" :1000,
        "model" : "meta-llama/Meta-Llama-3.1-405B-Instruct"
    }
    try:
        response = requests.post(
            "https://router.huggingface.co/nebius/v1/chat/completions",
            headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print("llama fallback failed:", e)
        return "Sorry, I couldn't generate an answer."

@app.post("/ask")
def ask_question(request: QuestionRequest):
    # Index if missing
    if not os.path.exists(INDEX_PATH) or not os.path.exists(CHUNKS_PATH):
        index_document(DOC_PATH)

    context = retrieve_context(request.question)
    prompt = f"Context:\n{context}\n\nQuestion: {request.question}"

    response = generate_with_llama(prompt)
    return {"answer": response}


# CLI for local testing
if __name__ == "__main__":
    query = input("Ask something: ")

    if not os.path.exists(INDEX_PATH) or not os.path.exists(CHUNKS_PATH):
        print("Index not found. Indexing document...")
        index_document(DOC_PATH)

    context = retrieve_context(query)
    prompt = f"Context:\n{context}\n\nQuestion: {query}"

    response = generate_with_llama(prompt)
    if response:
        print("\nAnswer:", response.strip())
    else:
        print ("No return from llama")
