"""
Modulo: Exceptions
Capa: Core
Version: 1.0.0
"""
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class ApplicationException(Exception):

    def __init__(self, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.context = context or {}
        logger.debug("ApplicationException raised: %s, Context: %s", self.message, self.context)

    def __str__(self) -> str:
        if self.context:
            return f"{self.message} (Context: {self.context})"
        return self.message


class DocumentNotFound(ApplicationException):

    def __init__(self, document_id: str, message: Optional[str] = None) -> None:
        final_message = message or f"Document with ID '{document_id}' not found."
        context = {"document_id": document_id}
        super().__init__(message=final_message, context=context)
        self.document_id = document_id
        logger.warning("DocumentNotFound: No document found for ID %s", self.document_id)


class DocumentRepositoryError(ApplicationException):

    def __init__(self, message: str) -> None:
        super().__init__(message=message)
        logger.error("DocumentRepositoryError: %s", message)


class InvalidDocumentDataError(ApplicationException):

    def __init__(self, message: str) -> None:
        super().__init__(message=message)
        logger.warning("InvalidDocumentDataError: %s", message)


class EmbeddingGenerationError(ApplicationException):

    def __init__(self, message: str) -> None:
        super().__init__(message=message)
        logger.error("EmbeddingGenerationError: %s", message)


class SimilarityCalculationError(ApplicationException):

    def __init__(self, message: str) -> None:
        super().__init__(message=message)
        logger.error("SimilarityCalculationError: %s", message)


class InvalidQueryError(ApplicationException):

    def __init__(self, message: str) -> None:
        super().__init__(message=message)
        logger.warning("InvalidQueryError: %s", message)


class DocumentNotFoundError(ApplicationException):

    def __init__(self, message: str) -> None:
        super().__init__(message=message)
        logger.warning("DocumentNotFoundError: %s", message)


class DocumentNotFoundException(DocumentNotFound):

    def __init__(self, document_id: str, message: str = None) -> None:
        super().__init__(document_id=document_id, message=message)


class RepositoryException(DocumentRepositoryError):

    def __init__(self, message: str) -> None:
        super().__init__(message=message)


class EmptyQueryError(InvalidQueryError):

    def __init__(self, message: str) -> None:
        super().__init__(message=message)


class SearchServiceError(DocumentRepositoryError):

    def __init__(self, message: str) -> None:
        super().__init__(message=message)


class QueryEmptyError(InvalidQueryError):

    def __init__(self, message: str) -> None:
        super().__init__(message=message)


class SearchError(DocumentRepositoryError):

    def __init__(self, message: str) -> None:
        super().__init__(message=message)