# BCRA Regulatory Knowledge Graph

Proyecto Final de carrera — Ingeniería en Inteligencia Artificial, Universidad de San Andrés (UdeSA).

## Resumen

Este proyecto explora si organizar la documentación normativa del Banco Central de la República Argentina (BCRA) como un *knowledge graph* mejora la fidelidad y reduce las alucinaciones de un sistema *Retrieval-Augmented Generation* (RAG) asistivo, comparado contra retrieval por embeddings tradicional, en el contexto de justificación normativa de decisiones automatizadas de credit scoring.

## Pregunta de investigación

¿Un sistema GraphRAG sobre un knowledge graph del corpus normativo del BCRA produce justificaciones de decisiones de credit scoring con mayor fidelidad y *citation accuracy* que un sistema vector-RAG tradicional?

## Estado

Etapa de diseño — modelado del schema y exploración del corpus normativo.

## Stack técnico

- Python 3.11+
- [RDFLib](https://rdflib.readthedocs.io/) para manipulación de RDF/Turtle/SPARQL
- Servidor SPARQL: TBD (Apache Jena Fuseki / GraphDB / Neo4j con n10s)

## Estructura del repositorio

```text
bcra-regulatory-kg/
├── docs/
│   ├── schema/    # Diseño y diagramas de la ontología
├── data/
│   ├── raw/       # PDFs descargados del BCRA (gitignored)
│   ├── processed/ # Texto extraído y limpio (gitignored)
│   └── kg/        # Knowledge graph en formato Turtle
├── notebooks/     # Exploración interactiva
├── src/
│   ├── scraper/    # Descarga de normativa del BCRA
│   ├── extraction/ # PDF → texto estructurado
│   └── kg/         # Construcción y consulta del KG
├── scripts/       # Scripts ejecutables (descarga, pipelines)
└── tests/         # Tests unitarios
```

## Setup

Requiere Python 3.11+.

```bash
# Clonar el repo
git clone https://github.com/AgustinaVidelaRivero/bcra-regulatory-kg.git
cd bcra-regulatory-kg

# Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## Mentores

- **Mentor:** Luciano del Corro (UdeSA)
- **Co-mentor:** Juan Wisznia (UdeSA)

## Autora

Agustina Videla Rivero — Ingeniería en Inteligencia Artificial, UdeSA.
