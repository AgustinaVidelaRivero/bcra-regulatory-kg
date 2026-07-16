# B1 — Verificación de arquitectura para el diseño de v7 (`ver_fuente`)

Fecha: 2026-07-16. SOLO LECTURA; única escritura: este archivo (zona gitignored). Sin
commits, sin API. **Solo hechos con evidencia** — sin propuesta de diseño.

## 1. El corpus en el repo

**Ruta:** `data/experiment/subset/` (READ-ONLY por regla del proyecto). Cinco PDFs reales
(no contenedores de imágenes):

```
$ file data/experiment/subset/*
TO_capitales_minimos_actual.pdf:                         PDF document, version 1.7 (zip deflate encoded)
TO_clasificacion_deudores_actual.pdf:                    PDF document, version 1.7 (zip deflate encoded)
TO_exterior_cambios_actual.pdf:                          PDF document, version 1.7 (zip deflate encoded)
TO_proteccion_usuarios_servicios_financieros_actual.pdf: PDF document, version 1.7 (zip deflate encoded)
TO_regimen_informativo_contable_mensual_actual.pdf:      PDF document, version 1.7 (zip deflate encoded)
```

| Documento | Bytes | Páginas | Chars de texto extraíble (pypdf) | Páginas casi-vacías |
|---|---|---|---|---|
| TO_capitales_minimos | 5.616.860 | 204 | 488.923 | 0 |
| TO_clasificacion_deudores | 2.192.648 | 60 | 137.220 | 0 |
| TO_exterior_cambios | 2.735.398 | 201 | 518.055 | 0 |
| TO_proteccion_usuarios | 2.502.846 | 40 | 95.074 | 0 |
| TO_regimen_informativo | 2.326.012 | 59 | 115.003 | 0 |
| **TOTAL** | ~15,4 MB | **564** | **1.354.275** | **0** |

**Todos tienen capa de texto extraíble completa** (cero páginas casi-vacías): no hay OCR ni
visión involucrados en ninguna lectura del corpus en este repo.

## 2. Cómo leyó el corpus el pipeline de extracción — y los artefactos intermedios

**El extractor de run_3** vive en `data/experiment/run_3_ppf_core/code/` (`chunker.py`,
`extract.py`, `schema.py`, `assemble.py`). Lee los PDFs con **pdfplumber** (texto directo;
docstring de `chunker.py`: "PDF → texto → chunks por punto numerado con MAX_CUT_DEPTH=2"),
corta SOLO en puntos de profundidad ≤2 y agrupa subpuntos en el chunk padre.

**LO MÁS VALIOSO — la capa de texto con anclaje a secciones EXISTE y está persistida:**
`data/experiment/run_3_ppf_core/code/cache/chunks_all.json` — **508 chunks, 1.324.841
chars** (≈98% de los 1,35M del texto pypdf), formato por chunk:

```json
{"chunk_id": "TO_capitales_minimos_actual.pdf::1.1", "doc": "TO_capitales_minimos_actual.pdf",
 "location": "Punto 1.1. Exigencia.", "text": "...", "char_count": 326}
```

Cobertura por documento: capitales 147 · clasificacion 65 · exterior 215 · proteccion 37 ·
regimen 44. Existen además los per-TO (`chunks_one_<doc>.json`) y `chunks_smoke.json`. Los
otros runs tienen sus propias capas de chunks (run_4: `code/cache/chunks/`; run_5:
`code/cache/chunks/*.json` — formatos propios de cada pipeline).

**La lectura del PDF en runtime del verificador** ya existe:
`data/experiment/evaluacion/pdf_locate.py` — `pdf_pages()` extrae texto por página con
**pypdf** (cacheado en memoria), `parse_point()` parsea "Punto X.Y"/"Sección N" de una
location, y `localize()` resuelve (source_doc, location) → pasaje, manejando cuerpo-vs-índice
por prose_score y devolviendo `localizacion_pdf=ok|fallida`. Es el backend de la tool
`leer_pasaje_pdf` del verificador (punto 4).

## 3. Censo de provenances (run_3) + contraste run_2/run_4

Sobre el `kg.json` congelado de run_3 (vía loader): **4.050 nodos, 4.050 con provenance
(100%), 4.064 provenances totales.** Formatos del campo `location` (regex + frecuencia + 5
ejemplos verbatim en el output pegado abajo):

| Patrón | Regex | Frecuencia |
|---|---|---|
| `punto_multinivel` | `^Punto\s+\d+(\.\d+)+\.` | **3.642 (89,6%)** |
| `punto_un_nivel` | `^Punto\s+\d+\.(?!\d)` | **422 (10,4%)** |
| sección / página / encabezado / otros | — | **0 (0,0%)** |

**Parseabilidad mecánica a (documento, punto/sección): 4.064/4.064 = 100,0%** con el parser
ya existente (`pdf_locate.parse_point`). Ejemplos verbatim y el caso sucio observado
("Punto 1.1. “A” 2136 1. 1° Según Com. …" — parsea igual a punto 1.1) en el output:

```
[punto_multinivel] 3642 (89.6%)
    "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    "Punto 1.2. Exigencia básica."
    "Punto 1.3. Integración."
    "Punto 1.4. Incumplimientos."
    "Punto 10.1. Disposiciones generales."
[punto_un_nivel] 422 (10.4%)
    "Punto 12. 8028. (parte 2)" ... "(parte 6)"
parseables con pdf_locate.parse_point: 4064/4064 (100.0%)
```

**Contraste multi-esquema (3 ejemplos verbatim por run):**

- **run_2:** `"Encabezado"` · `"Sección 1 > Punto 2.1"` · `"Sección 2 > Sección 2 — preámbulo"`
  (formato jerárquico "Sección > Punto"; incluye locations no-punto como "Encabezado").
- **run_4:** `"p.1-5 / Punto 1.1.1"` · `"p.9-11 / Punto 2.3.1.1, inciso vii y ss."` ·
  `"p.12-14 / Punto 2.3.2.2 y siguientes"` (rango de páginas + punto, con sufijos textuales).

(`pdf_locate.parse_point` ya contempla el formato de run_2 — su comentario cita "run_2 cita
'Sección 3 > Punto 3.6'" y prefiere el Punto sobre la Sección.)

## 4. La superficie del instrumento (tools del verificador)

**Definición** (en `data/experiment/evaluacion/verificador.py`):

- Las 3 tools de grafo vienen de `harness.TOOLS` (import en verificador.py:47).
- `LEER_PASAJE_PDF_TOOL`: schema en **líneas 119-141** (name en la 122; inputs
  `source_doc` + `location`: "'Punto X.Y', 'Sección N' o 'p. N'").
- `VER_PASO_COMPLETO_TOOL`: schema en **líneas 142-155** (name en la 142).
- **`VERIF_TOOLS = list(TOOLS) + [LEER_PASAJE_PDF_TOOL, VER_PASO_COMPLETO_TOOL]` —
  línea 156.** Se pasa a la API en la **línea 853** (`tools=VERIF_TOOLS`).

**Despacho** — `VerificadorAgente._run_tool`, **líneas 803-814**: if-chain por nombre
(`buscar_nodos`/`ver_nodo`/`ver_vecinos` → GraphIndex; `leer_pasaje_pdf` →
`_leer_pasaje_pdf` (definida en la línea 159, backend `pdf_locate.localize`);
`ver_paso_completo` → `self._ver_paso_completo`, líneas 816-837).

**Referencias a las tools en el prompt del verificador** (`system_prompt()`, línea 425, con
el texto en las constantes previas): **líneas 253-254** (checklist de cierre: leer_pasaje_pdf
por pata, ver_nodo antes de citar), **línea 276** (uso de ver_paso_completo en la prueba de
pertinencia), **líneas 288-293** (catálogo de herramientas: las 3 de grafo con la advertencia
del índice, leer_pasaje_pdf, ver_paso_completo).

**Puntos de cambio para agregar una tool nueva (hechos, sin implementar):**

1. Constante nueva con el schema JSON de la tool + sumarla a `VERIF_TOOLS` (línea 156).
2. Rama nueva en `_run_tool` (líneas 803-814) con su backend.
3. Texto del prompt: catálogo de herramientas (288-293) y, si cambia el método, el checklist
   (253-254) — **el prompt es parte del instrumento congelado**: tocarlo es nueva versión.
4. **La caché** (`llm_cache.py`): la key incluye `tools` — agregar una tool cambia TODAS las
   keys → namespace nuevo de facto; consistente con "v7 exige instrumento nuevo y
   calibración con material fresco".
5. El contrato de salida y los detectores no referencian tools por nombre salvo
   `tool_calls_usadas` (conteo agregado) — sin cambios estructurales ahí.

## 5. Tamaños para presupuestar

- **Texto del corpus:** 1.354.275 chars (pypdf, por página) ≈ **~340K tokens** (4 chars/token
  aprox — coincide con los ~338K tokens de contenido que registró la Fase 2.2 en CLAUDE.md).
  Por documento: tabla del punto 1. La capa de chunks de run_3: 1.324.841 chars en 508
  chunks (~2,6K chars promedio).
- **Nodos con provenance en run_3:** 4.050/4.050 (4.064 provenances).
- **Costo por caso medido (referencia, citado de las lecturas — no recalculado):** gate #2
  ≈ 1,16M input/caso (5,80M/5, `docs/lectura_gate2_AB.md` + extracción); piloto ≈ 0,84M/caso
  (4.179.672/5, `docs/lectura_piloto_v6.md` §1); validación ≈ 0,74M/caso (5.896.712/8,
  `docs/lectura_validacion_v61.md` §1). Régimen N=3 en todos.

## Comandos y outputs completos

El código del relevamiento (pypdf/loader/pdf_locate, solo lectura) y su output íntegro:

```
== 1/5: PDFs — páginas y texto extraíble (pypdf, mecanismo de pdf_locate) ==
  TO_capitales_minimos_actual.pdf: 204 páginas · 488,923 chars de texto extraído · páginas casi-vacías: 0
  TO_clasificacion_deudores_actual.pdf: 60 páginas · 137,220 chars · 0
  TO_exterior_cambios_actual.pdf: 201 páginas · 518,055 chars · 0
  TO_proteccion_usuarios_servicios_financieros_actual.pdf: 40 páginas · 95,074 chars · 0
  TO_regimen_informativo_contable_mensual_actual.pdf: 59 páginas · 115,003 chars · 0
  TOTAL corpus (texto pypdf): 1,354,275 chars (~338,568 tokens aprox)

== 2: capa de chunks de run_3 ==
  chunks_all.json: 508 chunks · chars totales: 1,324,841
    capitales 147 · clasificacion 65 · exterior 215 · proteccion 37 · regimen 44
  formato location: 'Punto 1.1. Exigencia.' etc.

== 3: censo run_3 ==
  nodos: 4050 · con provenance: 4050 · provenances totales: 4064
  punto_multinivel 3642 (89.6%) · punto_un_nivel 422 (10.4%) · otros 0
  parseables con pdf_locate.parse_point: 4064/4064 (100.0%)

== 3b: contraste ==
  run_2: ['Encabezado', 'Sección 1 > Punto 2.1', 'Sección 2 > Sección 2 — preámbulo']
  run_4: ['p.1-5 / Punto 1.1.1', 'p.9-11 / Punto 2.3.1.1, inciso vii y ss.', 'p.12-14 / Punto 2.3.2.2 y siguientes']
```

---

*Fin de B1. Hechos para el documento de diseño de v7; sin propuesta de diseño. Frenado para
revisión.*
