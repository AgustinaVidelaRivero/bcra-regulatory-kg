# BCRA Regulatory Knowledge Graph

Proyecto Final de carrera — Ingeniería en Inteligencia Artificial, Universidad de San Andrés (UdeSA).

## Resumen

Este proyecto diseña, construye y evalúa un Knowledge Graph (KG) sobre la regulación del Banco Central de la República Argentina (BCRA), con énfasis en la calidad del modelado, la trazabilidad documental y el rigor de la evaluación de extracción. La utilidad del KG se demuestra a través de dos casos de uso aplicados:

1. Un sistema agéntico de explicabilidad que, dado un log de operaciones de un cliente o entidad, reconstruye la cadena causal de normas que justifica una restricción operativa específica.
2. Una comparación empírica entre arquitecturas KG-RAG y RAG tradicional sobre el mismo corpus, en términos de faithfulness, citation accuracy, costo y latencia.

## Pregunta de investigación

¿Un Knowledge Graph que modele explícitamente las entidades regulatorias del BCRA y sus relaciones causales habilita justificaciones operativas con mayor faithfulness y citation accuracy que sistemas RAG basados en embeddings densos sobre el mismo corpus?

## Estado

Mayo 2026 — completando el corpus regulatorio mediante scraping y diseñando el esquema del KG (RFC v0.2 en redacción). El schema preliminar v0.1 está archivado en [docs/schema/legacy/](docs/schema/legacy/) como referencia.

## Scope del corpus

Regulación pública del BCRA accesible desde el sitio oficial:

- **Textos Ordenados** vigentes e históricos (operatoria cambiaria, clasificación de deudores, capitales mínimos, garantías, tasas, protección al usuario, sistemas de pago, etc.).
- **Marco legal** asociado: Carta Orgánica del BCRA (Ley 24.144), Ley 19.359 (Régimen Penal Cambiario), Decreto 260/02, Decreto 609/19.
- **Comunicaciones A** (modificaciones normativas), rango post-cepo a partir de septiembre 2019.
- **Comunicaciones B** (aclaraciones interpretativas).
- **Documentos complementarios** linkeados desde páginas temáticas del BCRA.

Comunicaciones C (fe de erratas) y P (publicación administrativa) quedan fuera de scope por baja densidad informativa para el modelado del KG.

## Stack técnico

- Python 3.11+
- Scraping del corpus: `requests` + `pypdf` + `BeautifulSoup` con rate limiting global, manifiesto y checkpoint persistente.
- Extracción de tripletas: LLMs vía Anthropic SDK con structured outputs (a definir en RFC de schema v0.2).
- Construcción y análisis del grafo: a definir entre NetworkX (iteración rápida, alineado con el [cookbook de Anthropic sobre KG](https://platform.claude.com/cookbook/capabilities-knowledge-graph-guide)), RDFLib + Turtle (artefacto académico estándar) o un grafo nativo tipo Neo4j para queries multi-hop. Decisión a consensuar con mentor.
- Evaluación: precision/recall a nivel de tripleta contra gold standard manual, métricas estructurales del grafo, faithfulness y citation accuracy con RAGAS y FActScore sobre eval set curado.

## Estructura del repositorio

```text
bcra-regulatory-kg/
├── docs/
│   ├── schema/
│   │   └── legacy/    # Schemas previos archivados (v0.1)
│   └── literatura/    # Resúmenes de papers, comparativa cruzada y análisis de gaps
├── data/
│   ├── raw/       # PDFs y HTMLs descargados del BCRA + manifiesto + checkpoint (gitignored)
│   ├── processed/ # Texto extraído y limpio (gitignored)
│   └── kg/        # Knowledge graph en formato Turtle / JSON (gitignored)
├── notebooks/     # Exploración interactiva
├── src/
│   ├── scraper/    # Descarga de normativa del BCRA
│   ├── extraction/ # PDF → tripletas estructuradas
│   └── kg/         # Construcción, consulta y serialización del KG
├── scripts/       # Pipelines ejecutables (descarga, extracción, evaluación)
└── tests/         # Tests unitarios
```

## Uso del descargador

El script `scripts/download_bcra.py` modulariza la descarga del corpus en pasos B.1..B.9. Por defecto descarga el corpus BCRA completo:

```bash
python scripts/download_bcra.py B1   # TOs vigentes
python scripts/download_bcra.py B2   # Marco legal
python scripts/download_bcra.py B3   # TOs históricos
python scripts/download_bcra.py B4   # Comunicaciones A
python scripts/download_bcra.py B5   # Versiones tachado/negrita
python scripts/download_bcra.py B6   # Comunicaciones B
python scripts/download_bcra.py B9   # Documentos complementarios
```

Para restringir B4/B6/B7/B8 al subconjunto MULC (scope previo del proyecto):

```bash
python scripts/download_bcra.py B4 --mulc-only
```

Es idempotente: archivos ya descargados se saltean automáticamente.

## Setup

Requiere Python 3.11+.

```bash
git clone https://github.com/AgustinaVidelaRivero/bcra-regulatory-kg.git
cd bcra-regulatory-kg

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Mentores

- **Mentor:** Luciano del Corro (UdeSA)
- **Co-mentor:** Juan Wisznia (UdeSA)

## Autora

Agustina Videla Rivero — Ingeniería en Inteligencia Artificial, UdeSA.
