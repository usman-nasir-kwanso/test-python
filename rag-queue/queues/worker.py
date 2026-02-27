from openai import OpenAI
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings

load_dotenv()

openai_client = OpenAI()

# Vector Embedding Model
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = QdrantVectorStore.from_existing_collection(
    collection_name="djermaya_solar",
    embedding=embeddings_model,
    url="http://localhost:6333",
)


def process_query(query: str):
    print(f"Processing query: {query}")

    search_results = vectorstore.similarity_search(query=query)
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
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ],
    )

    answer = response.choices[0].message.content
    print(f"🤖 {answer}")
    return answer
