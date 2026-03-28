"""
RAG Document API
Capa: Entry Point
Version: 1.0.0
"""

import logging
from fastapi import FastAPI
from api.document_router import router as document_router
from api.search_router import router as search_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="RAG Document API",
    description="API para gestion de documentos con busqueda semantica",
    version="1.0.0",
)

app.include_router(document_router)
app.include_router(search_router)

@app.get("/health")
async def health():
    return {"status": "ok", "service": "rag-document-api"}
