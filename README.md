# data-engineering-rag-chatbot

A Retrieval-Augmented Generation (RAG) chatbot built on YouTube transcript data, designed to support learning in data engineering.

# 🤖 The Data Engineer YouTube RAG Chatbot

Welcome to **The Data Engineer YouTube RAG Chatbot**!  
This project is a **Retrieval-Augmented Generation (RAG)** application that allows users to ask questions about **Data Engineering** and receive accurate, context-aware answers based on **AIengerinner YouTube video transcripts**.

The chatbot is designed with the personality of an enthusiastic and experienced data engineer, inspired by educational YouTubers. It combines modern AI tooling with a clean, production-oriented architecture — suitable for both academic evaluation and real-world use.

--- 

## Getting Started

Follow the steps below to set up and run the project locally.

### 1. Prerequisites

Make sure you have the following installed:

- **Python 3.12+**
- **Google Gemini API key** (used for embeddings and text generation)

---

### 2. Installation

Clone the repository and install dependencies using `uv`:

```bash
git clone <your-repo-url>
cd data-engineering-rag-chatbot
uv sync
```

### 3. Environment Variables

Create a .env file in the project root and add your API key:

```bash
GEMINI_API_KEY="your_api_key_here"
```
### 4. Ingest Data (Build the Knowledge Base)

Before running the chatbot, the YouTube transcripts must be processed and stored in the vector database.

This step:

- Converts .md files to clean .txt

- Splits text into chunks

- Generates embeddings

- Stores them in LanceDB

Run the ingestion script:

```bash
python backend/ingest_data.py
```

### 5. Run the Application localy

The application consists of a FastAPI backend and a Streamlit frontend. Start them in two separate terminals.

Terminal 1 – Backend (API):

```bash
uv run uvicorn api:app --reload
```

Terminal 2 – Frontend (UI):
```bash
streamlit run app.py
```

### Overview
The application follows a standard RAG architecture:

1. Data Ingestion
YouTube transcripts are cleaned, chunked, and embedded.

2. Vector Storage
LanceDB stores embeddings generated with gemini-embedding-001.

3. RAG Logic
PydanticAI retrieves relevant chunks and generates answers using structured outputs.

4. API Layer
FastAPI exposes the chatbot via a POST endpoint.

5. Frontend
Streamlit provides a simple chat interface.

6. Deployment
The API is deployed serverlessly using Azure Functions and consumed by Streamlit locally.

### Tech Stack

A selection of the main tools and technologies used:

LanceDB – Vector database

PydanticAI – Agent framework and structured outputs

Google Gemini – Large Language Model & embeddings

FastAPI – Backend API

Streamlit – Frontend user interface