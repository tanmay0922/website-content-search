from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks):
    texts = [chunk["content"] for chunk in chunks]
    embeddings = model.encode(texts, convert_to_tensor=True)
    for i, emb in enumerate(embeddings):
        chunks[i]["embedding"] = emb
    print(f"[DEBUG] Embedded {len(embeddings)} chunks")
    return chunks

def search_similar_chunks(query: str, embedded_chunks, top_k: int = 5):
    try:
        top_k = int(top_k)  # Force convert to int
        query_embedding = model.encode(query, convert_to_tensor=True)
        
        similarities = []
        for chunk in embedded_chunks:
            score = util.cos_sim(query_embedding, chunk["embedding"]).item()
            similarities.append((chunk, score))

        similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

        top_results = []
        for i in range(min(top_k, len(similarities))):
            chunk, score = similarities[i]
            top_results.append({
                "content": chunk["content"],
                "path": chunk["path"],
                "html": chunk.get("html", ""),
                "match_score": round(score, 4)
            })

        print(f"[DEBUG] Found {len(top_results)} similar chunks")
        return top_results

    except Exception as e:
        print(f"[ERROR] Similarity search failed: {e}")
        return []
