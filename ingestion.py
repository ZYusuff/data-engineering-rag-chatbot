# ingestion.py (i roten)
import lancedb
from constants import VECTOR_DATABASE_PATH, DATA_PATH
from data_models import Transcript
from pathlib import Path
import time


def setup_vector_db(path):
    vector_db = lancedb.connect(uri = path)
    vector_db.create_table("transcripts", schema=Transcript, exist_ok=True)
    return vector_db


def ingest_docs_to_vector_db(table):
    files = list(DATA_PATH.glob("*.md"))
    if not files:
        print(f"No .md files found in {DATA_PATH}")
        return
    
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        doc_id = file.stem

        # delete old version if exists
        table.delete(f"doc_id = '{doc_id}'")

        # Insert without embedding → LanceDB handles it
        table.add([
            {
                "doc_id": doc_id,
                "filepath": str(file),
                "filename": file.stem,
                "content": content
            }
        ])

        print(table.to_pandas()["filename"])
        time.sleep(30)


if __name__ == "__main__":
    vector_db = setup_vector_db(VECTOR_DATABASE_PATH)
    ingest_docs_to_vector_db(vector_db["transcripts"])

