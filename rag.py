from pydantic_ai import Agent
from data_models import RagResponse, Transcript, Prompt
import lancedb
from constants import VECTOR_DATABASE_PATH

# Koppla till vector database
vector_db = lancedb.connect(VECTOR_DATABASE_PATH)

# Skapa RAG-agent
rag_agent = Agent(
    model="google-gla:gemini-2.5-flash", 
    retries=2,
    system_prompt=( # Generated through LLMs
        "You are Kokchun's data-engineering assistant. Be friendly, slightly nerdy, and explain concepts clearly.",
        "Always answer based on the retrieved knowledge, but you can mix in your expertise to make the answer more coherent.",
        "Don't hallucinate; rather say you can't answer it if the user prompts outside of the retrieved knowledge.",
        "Keep answers clear and concise, max 6 sentences.",
        "Also describe which file you have used as source.",
    ), 
    output_type=RagResponse,
)


@rag_agent.tool_plain
def retrieve_top_documents(query: str, top_results: int = 3) -> str:
    """
    Retrieve top_results closest matching documents from the vector database.
    """
    table = vector_db["transcripts"] 
    results = table.search(query=query).limit(top_results).to_list()

    if not results:
        return "No documents found for your query."

    # Bygg en sträng med de hämtade resultaten
    retrieved_texts = []
    for doc in results:
        retrieved_texts.append(
            f"Filename: {doc['filename']}\nFilepath: {doc['filepath']}\nContent: {doc['content']}\n"
        )

    return "\n---\n".join(retrieved_texts)