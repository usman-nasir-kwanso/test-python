export interface UploadResponse {
  document_id: string;
  filename: string;
  chunks_indexed: number;
  status: string;
}

export interface Citation {
  document_id: string;
  filename?: string | null;
  chunk_index: number;
  source?: string | null;
  page?: number | null;
  score: number;
  snippet: string;
}

export interface ChatResponse {
  answer: string;
  citations: Citation[];
  retrieved_chunks_count: number;
}

export interface ApiError {
  error: string;
  details: string;
}
