# RAG Document API

REST API for document management with semantic search, built with FastAPI and deployed on Google Cloud Run.

## Description

RAG Document API allows storing documents and performing semantic searches on their content. Built with Clean Architecture and SOLID principles.

## Live Demo

**Swagger UI:** https://rag-document-api-247946064488.us-central1.run.app/docs

## Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| POST | `/documents/` | Create a new document |
| GET | `/search/?q=text` | Semantic search over documents |
| GET | `/health` | Service health check |

## Stack

- Python 3.12
- FastAPI
- Google Cloud Run
- Clean Architecture
- Semantic Search

## Usage

### Create a document
```bash
curl -X POST https://rag-document-api-247946064488.us-central1.run.app/documents/ \
  -H "Content-Type: application/json" \
  -d '{"title": "My document", "content": "Document content here"}'
```

### Search documents
```bash
curl "https://rag-document-api-247946064488.us-central1.run.app/search/?q=content"
```

## Built by

Edisson A.G.C. — AI Engineering Applied to Commerce
