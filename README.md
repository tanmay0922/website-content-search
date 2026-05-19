# Website Content Search

A semantic search engine for web content — submit any URL and a query to find the most relevant sections of that page using NLP embeddings and cosine similarity.

## Features

- **Web Extraction** — fetches and parses any URL using BeautifulSoup
- **Smart Chunking** — splits content into 500-token segments for precise matching
- **Semantic Search** — generates embeddings via SentenceTransformers, ranks by cosine similarity
- **Full-stack** — Next.js frontend with TailwindCSS, FastAPI Python backend
- **Contextual Results** — returns ranked snippets with surrounding context

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js + TailwindCSS |
| Backend | FastAPI (Python) |
| NLP | SentenceTransformers |
| Parsing | BeautifulSoup + Requests |
| Language | JavaScript (48%) + Python (47%) |

## Getting Started

```bash
git clone https://github.com/tanmay0922/website-content-search.git
cd website-content-search

# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

## How It Works

```
URL Input → Fetch Page → Parse HTML → Chunk Text (500 tokens)
                                              ↓
Query Input → Embed Query → Compare vs Chunk Embeddings → Rank by Cosine Similarity → Return Top Results
```

## Author

**Tanmay Upadhyay** — [GitHub](https://github.com/tanmay0922) · [LinkedIn](https://www.linkedin.com/in/tanmay-upadhyay-0b884b203/) · [Portfolio](https://tanmay0922.github.io)
