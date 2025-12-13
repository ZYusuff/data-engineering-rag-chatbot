from fastapi import FastAPI
from data_models import Prompt, RagResponse
from constants import VECTOR_DATABASE_PATH
from rag import rag_agent
import lancedb
from typing import Dict

app = FastAPI()

def get_table():
    db = lancedb.connect(VECTOR_DATABASE_PATH)
    return db["transcripts"]


@app.post("/rag/query", response_model=RagResponse)
async def rag_query(prompt: Prompt):
    """RAG query endpoint"""
    try:
        result = await rag_agent.run(prompt.prompt)
        output = result.output

        return RagResponse(
            filename=output.filename,
            filepath=output.filepath,
            answer=output.answer,
        )
    
    except Exception as e:
        # Returnera ett kontrollerat fel istället för 500
        return RagResponse(
            filename="N/A",
            filepath="N/A",
            answer=f"Model error: {str(e)}"
        )