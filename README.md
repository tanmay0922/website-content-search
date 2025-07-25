# 🌐 Website Content Search Tool

A powerful full-stack application that lets users **search website content** semantically. Enter a URL, extract content intelligently, chunk and embed it, then perform semantic search using Sentence Transformers – all in one seamless UI.

---

## 🚀 Features

- 🔗 Extracts content from a webpage using `BeautifulSoup`
- 📄 Splits content into 500-token chunks for efficient search
- 🧠 Embeds content using `SentenceTransformers`
- 🔍 Performs semantic similarity search for user queries
- 🧰 Built with **FastAPI** (Backend) & **Next.js + TailwindCSS** (Frontend)

---

## 🧱 Tech Stack

| Layer     | Technology               |
|-----------|--------------------------|
| Frontend  | Next.js, TailwindCSS     |
| Backend   | FastAPI, Python          |
| NLP       | SentenceTransformers     |
| Parsing   | BeautifulSoup, Requests  |
| State     | React Hooks              |

---

## 📁 Project Structure

website-content-search/
│
├── backend/ # FastAPI backend

│ ├── main.py # API endpoints

│ ├── chunker.py # Tokenizer + chunk logic

│ ├── parser.py # HTML parsing

│ ├── vector_db.py # In-memory embedding + search

│ └── requirements.txt # Python dependencies

│
├── frontend/ # Next.js frontend

│ ├── app/ # Components, pages

│ ├── public/ # Icons and static files

│ ├── tailwind.config.js

│ ├── postcss.config.js

│ ├── package.json

│ └── next.config.mjs

│
├── .gitignore
└── README.md


---

## ⚙️ Setup Instructions

### 🐍 Backend (FastAPI)

1. Navigate to backend folder:
2. 
   cd backend
   
2.Create virtual environment:

python -m venv venv

source venv/bin/activate  # or venv\Scripts\activate on Windows

3.Install dependencies:

pip install -r requirements.txt

4.Start FastAPI server:

uvicorn main:app --reload
🌐 Frontend (Next.js)

1.Navigate to frontend folder:
cd frontend

2.Install dependencies:

npm install

3.Run the development server:

npm run dev

4.Open in browser: http://localhost:3000


🔍 How It Works
1.User enters a website URL and a query.

2.Backend fetches and parses the website using BeautifulSoup.

3.Text is split into meaningful 500-token chunks.

4.Chunks are embedded using a transformer model.

5.Query is embedded and matched against chunks using cosine similarity.

6.Results are ranked and displayed with context.


