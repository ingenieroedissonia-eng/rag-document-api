# RAG Document API

API REST para gestión de documentos con búsqueda semántica, construida con FastAPI y desplegada en Google Cloud Run.

## Descripción

RAG Document API permite almacenar documentos y realizar búsquedas semánticas sobre su contenido. Construida con Clean Architecture y principios SOLID.

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/documents/` | Crear un nuevo documento |
| GET | `/search/?q=texto` | Búsqueda semántica de documentos |
| GET | `/health` | Estado del servicio |

## Demo en producción

**Swagger UI:** https://rag-document-api-247946064488.us-central1.run.app/docs

## Stack

- Python 3.12
- FastAPI
- Google Cloud Run
- Clean Architecture

## Uso

### Crear un documento
```bash
curl -X POST https://rag-document-api-247946064488.us-central1.run.app/documents/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Mi documento", "content": "Contenido del documento"}'
```

### Buscar documentos
```bash
curl "https://rag-document-api-247946064488.us-central1.run.app/search/?q=contenido"
```

## Desarrollado por

Edisson A.G.C. — Ingeniería IA Aplicada al Comercio
