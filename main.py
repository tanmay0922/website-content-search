from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from parser import extract_and_split_text
from vector_db import embed_chunks, search_similar_chunks

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchRequest(BaseModel):
    url: str
    query: str

class SearchResult(BaseModel):
    content: str
    path: str
    html: str
    match_score: float

@app.post("/search", response_model=List[SearchResult])
async def search(request: SearchRequest):
    url = request.url
    query = request.query
    print(f"[INFO] Received search request for URL: {url} and query: '{query}'")

    try:
        chunks = extract_and_split_text(url)
        print(f"[DEBUG] Extracted {len(chunks)} chunks")
        if not chunks:
            raise HTTPException(status_code=400, detail="No content extracted.")

        embedded_chunks = embed_chunks(chunks)
        print(f"[DEBUG] Embedded {len(embedded_chunks)} chunks")

        results = search_similar_chunks(query, embedded_chunks, top_k=5)
        print(f"[DEBUG] Final results to return:")
        for res in results:
            print(f" - {res['match_score']}: {res['content'][:50]}...")

        return results

    except Exception as e:
        print(f"[ERROR] {str(e)}")
        raise HTTPException(status_code=500, detail="Error processing request.")
