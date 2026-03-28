"""
RAG Document API - Document Router
Capa: API
Version: 1.0.0
"""

import logging
from abc import ABC, abstractmethod
from typing import List, Optional

from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, Field

from core.document import Document
from core.use_cases import AddDocument, AddDocumentRequest, DocumentRepository
from core.exceptions import ApplicationException, InvalidDocumentDataError
from infrastructure.in_memory_document_repository import InMemoryDocumentRepository

logger = logging.getLogger(__name__)


class DocumentCreateRequest(BaseModel):
    title: str = Field(..., min_length=1, description="Titulo del documento.")
    content: str = Field(..., min_length=1, description="Contenido del documento.")


class DocumentResponse(BaseModel):
    id: str
    title: str
    content: str


router = APIRouter(prefix="/documents", tags=["Documents"])

document_repository_instance = InMemoryDocumentRepository()


def get_document_repository() -> DocumentRepository:
    return document_repository_instance


def get_add_document_use_case(
    repo: DocumentRepository = Depends(get_document_repository)
) -> AddDocument:
    return AddDocument(document_repository=repo)


@router.post(
    "/",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo documento",
)
async def create_document_endpoint(
    document_data: DocumentCreateRequest,
    use_case: AddDocument = Depends(get_add_document_use_case),
) -> DocumentResponse:
    try:
        logger.info("Creando documento con titulo: %s", document_data.title)
        request = AddDocumentRequest(title=document_data.title, content=document_data.content)
        created = use_case.execute(request)
        logger.info("Documento creado con ID: %s", created.id)
        return DocumentResponse(id=created.id, title=created.title, content=created.content)
    except InvalidDocumentDataError as e:
        logger.warning("Datos invalidos: %s", e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except ApplicationException as e:
        logger.error("Error de aplicacion: %s", e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error("Error inesperado: %s", e, exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno.")
