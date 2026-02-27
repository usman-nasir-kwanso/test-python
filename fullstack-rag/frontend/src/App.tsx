import { FormEvent, useState } from "react";
import { askQuestion, uploadDocument } from "./api";
import type { Citation } from "./types";
import "./styles.css";

type Message = {
  role: "user" | "assistant";
  text: string;
  citations?: Citation[];
};

export default function App() {
  const [file, setFile] = useState<File | null>(null);
  const [documentId, setDocumentId] = useState<string | null>(null);
  const [uploadStatus, setUploadStatus] = useState<string>("");
  const [question, setQuestion] = useState<string>("");
  const [loading, setLoading] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  const [error, setError] = useState<string>("");

  const onUpload = async (e: FormEvent) => {
    e.preventDefault();
    if (!file) {
      setError("Please choose a file first.");
      return;
    }
    setError("");
    setUploadStatus("Uploading and indexing...");
    try {
      const result = await uploadDocument(file);
      setDocumentId(result.document_id);
      setUploadStatus(
        `Indexed ${result.filename} (${result.chunks_indexed} chunks). Document ID: ${result.document_id}`
      );
    } catch (err) {
      setUploadStatus("");
      setError(err instanceof Error ? err.message : "Upload failed.");
    }
  };

  const onAsk = async (e: FormEvent) => {
    e.preventDefault();
    if (!question.trim()) {
      return;
    }
    setError("");
    setLoading(true);
    const userText = question.trim();
    setQuestion("");
    setMessages((prev) => [...prev, { role: "user", text: userText }]);

    try {
      const result = await askQuestion(userText, documentId);
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: result.answer, citations: result.citations },
      ]);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Chat request failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="app">
      <h1>Document Chat (FastAPI + React)</h1>

      <section className="panel">
        <h2>1) Upload Document</h2>
        <form onSubmit={onUpload} className="row">
          <input
            type="file"
            accept=".pdf,.txt"
            onChange={(e) => setFile(e.target.files?.[0] ?? null)}
          />
          <button type="submit">Upload & Index</button>
        </form>
        {uploadStatus && <p className="success">{uploadStatus}</p>}
      </section>

      <section className="panel">
        <h2>2) Ask Questions</h2>
        <form onSubmit={onAsk} className="row">
          <input
            type="text"
            placeholder="Ask a question about your uploaded document..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            disabled={loading}
          />
          <button type="submit" disabled={loading}>
            {loading ? "Asking..." : "Ask"}
          </button>
        </form>

        <div className="chat">
          {messages.map((msg, idx) => (
            <article key={idx} className={`bubble ${msg.role}`}>
              <strong>{msg.role === "user" ? "You" : "Assistant"}:</strong>
              <p>{msg.text}</p>
              {msg.citations && msg.citations.length > 0 && (
                <details>
                  <summary>Sources ({msg.citations.length})</summary>
                  <ul>
                    {msg.citations.map((citation, cidx) => (
                      <li key={`${idx}-${cidx}`}>
                        <strong>{citation.filename || "document"}</strong> · chunk{" "}
                        {citation.chunk_index} · score {citation.score.toFixed(3)}
                        <br />
                        <small>{citation.snippet}</small>
                      </li>
                    ))}
                  </ul>
                </details>
              )}
            </article>
          ))}
        </div>
      </section>

      {error && <p className="error">Error: {error}</p>}
    </main>
  );
}
