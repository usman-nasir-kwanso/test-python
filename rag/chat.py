from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

openai_client = OpenAI()
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = QdrantVectorStore.from_existing_collection(
    collection_name="djermaya_solar",
    embedding=embeddings_model,
    url="http://localhost:6333",
)

user_query = input("Enter your question: ")

search_results = vectorstore.similarity_search(query=user_query)

context = "\n\n".join(
    [
        f"Page Content: {result.page_content}\n"
        f"Page Number: {result.metadata['page_label']}\n"
        f"File Location: {result.metadata['source']}"
        for result in search_results
    ]
)

SYSTEM_PROMPT = f"""
You are a helpful AI Assistant who answers user query based on the available
context retrieved from a PDF file along with page_contents and page number.

You should only answer the user based on the following context and navigate the
user to open the right page number to know more.

Context:
{context}
"""

response = openai_client.chat.completions.create(
    model="gpt-5.2",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ],
)

print(f"🤖 {response.choices[0].message.content}")
