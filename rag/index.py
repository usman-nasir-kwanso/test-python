from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()

pdf_path = (
    Path(__file__).parent
    / "Djermaya Solar PIM version 01 Final (2019-01-31) - Project Information Memorandum Sample for AI Team.pdf"
)
loader = PyPDFLoader(pdf_path)
docs = loader.load()
print(docs[2])

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
chunks = text_splitter.split_documents(docs)
print(chunks[0])

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# Embed the chunks
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = QdrantVectorStore.from_documents(
    chunks,
    embeddings_model,
    url="http://localhost:6333",
    collection_name="djermaya_solar",
)

print("Indexing complete")
