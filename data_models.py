from pydantic import BaseModel, Field
from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector
from dotenv import load_dotenv 

load_dotenv()

embedding_model = get_registry().get("gemini-text").create(name="gemini-embedding-001")

EMBEDDING_DIM = 3072

class Transcript(LanceModel):
    """Represents a transcript for Kokchun's youtube video with its corresponding embeddings"""
    doc_id: str
    filepath: str
    filename: str = Field(description="file name without extension")
    content: str = embedding_model.SourceField()
    embedding: Vector(EMBEDDING_DIM) = embedding_model.VectorField()

class Prompt(BaseModel):
    prompt: str = Field(description="prompt from user")

class RagResponse(BaseModel):
    filename: str = Field(description="filename of the retrieved file without suffix")
    filepath: str = Field(description="absolute path to the retrieved file")
    answer: str = Field(description="answer based on the retrieved file")