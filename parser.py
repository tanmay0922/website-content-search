import requests
from bs4 import BeautifulSoup
from typing import List

def extract_and_split_text(url: str, chunk_size: int = 500) -> List[dict]:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove scripts and styles
        for tag in soup(['script', 'style', 'noscript']):
            tag.decompose()

        text = soup.get_text(separator=' ', strip=True)
        words = text.split()
        
        # Break text into chunks
        chunks = []
        for i in range(0, len(words), chunk_size):
            chunk_text = ' '.join(words[i:i+chunk_size])
            chunks.append({
                "content": chunk_text,
                "path": url,
                "html": ""  # Optionally add soup snippet or surrounding HTML
            })

        return chunks

    except Exception as e:
        print(f"[ERROR] Failed to extract content from {url}: {e}")
        return []
