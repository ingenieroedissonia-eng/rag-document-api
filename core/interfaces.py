"""
Modulo: Interfaces
Capa: Core
Version: 1.0.0
"""
import logging
from abc import ABC, abstractmethod
from typing import List, Optional

from core.document import Document

logger = logging.getLogger(__name__)


class DocumentRepository(ABC):

    @abstractmethod
    def add(self, document: Document) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, document_id: str) -> Document:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[Document]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, document_id: str) -> None:
        raise NotImplementedError

    def save(self, document: Document) -> Document:
        self.add(document)
        return document

    def get(self, document_id: str) -> Optional[Document]:
        return self.get_by_id(document_id)

    def get_all(self) -> List[Document]:
        return self.list_all()
