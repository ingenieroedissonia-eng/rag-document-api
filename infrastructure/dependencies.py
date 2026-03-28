"""
Modulo: Dependencies
Capa: Infrastructure
Version: 1.0.0
"""
import logging

from core.search_use_case import SearchDocuments
from infrastructure.in_memory_document_repository import InMemoryDocumentRepository

logger = logging.getLogger(__name__)

_repository_instance = InMemoryDocumentRepository()


def get_search_use_case() -> SearchDocuments:
    return SearchDocuments(document_repository=_repository_instance)
