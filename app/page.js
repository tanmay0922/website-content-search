"use client";
import { useState } from "react";

export default function Home() {
  const [url, setUrl] = useState("");
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/search", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url, query }),
      });

      const data = await response.json();
      console.log("[DEBUG] API returned:", data);
      setResults(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error("Error fetching results:", error);
      setResults([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-50 flex flex-col items-center justify-center px-4 py-10">
      <h1 className="text-4xl font-bold text-gray-900 mb-2 text-center">
        Website Content Search
      </h1>
      <p className="text-lg text-gray-600 mb-8 text-center">
        Search through website content with precision
      </p>

      <form
        onSubmit={handleSubmit}
        className="w-full max-w-2xl flex flex-col items-center"
      >
        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="https://example.com"
          className="w-full p-3 border border-gray-300 rounded-md text-gray-900 placeholder-gray-400 mb-4"
          required
        />
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search term"
          className="w-full p-3 border border-gray-300 rounded-md text-gray-900 placeholder-gray-400 mb-6"
          required
        />
        <button
          type="submit"
          className="w-full bg-blue-600 text-white font-medium py-3 rounded-md hover:bg-blue-700 transition"
        >
          {loading ? "Searching..." : "Search"}
        </button>
      </form>

      <h2 className="text-xl font-semibold text-gray-800 mt-10 mb-4">
        Search Results
      </h2>

      <div className="w-full max-w-2xl space-y-4">
        {results.length === 0 && !loading && (
          <p className="text-gray-500 text-center">No results found.</p>
        )}
        {results.map((item, index) => (
          <div
            key={index}
            className="bg-white border border-gray-200 rounded-lg shadow-sm p-5"
          >
            <h3 className="text-lg font-semibold text-gray-900">
              {item.content.slice(0, 100)}...
            </h3>
            <p className="text-sm text-gray-600 mt-1 mb-2">Path: {item.path}</p>
            <div className="flex items-center justify-between">
              <details>
                <summary className="text-blue-600 text-sm hover:underline font-medium cursor-pointer">
                  View HTML
                </summary>
                <pre className="bg-gray-100 p-2 mt-2 max-h-48 overflow-auto text-xs whitespace-pre-wrap">
                  {item.html}
                </pre>
              </details>
              <span className="bg-green-100 text-green-800 text-xs font-bold px-2.5 py-0.5 rounded">
                {Math.round(item.match_score * 100)}% match
              </span>
            </div>
          </div>
        ))}
      </div>
    </main>
  );
}
