# Protocolo experimental — Diseño del schema del KG por comparación de 5 estrategias

**Objetivo del experimento:** determinar empíricamente qué estrategia de diseño de schema produce un Knowledge Graph más útil downstream, construyendo 5 KGs en paralelo (uno por estrategia) sobre un subset idéntico y evaluándolos después con preguntas complejas.

Este documento define el **terreno común**: el subset de documentos, el formato de salida obligatorio, las reglas de modelado no negociables, las métricas a reportar y la estructura de carpetas. Las 5 instancias paralelas trabajan contra este protocolo para que su output sea comparable.

---

## a) Identificación del subset experimental

Los 5 Textos Ordenados del subset, copiados a `data/experiment/subset/`:

| # | Nombre conceptual | Archivo | Págs | Tamaño | URL fuente (manifest) |
|---|---|---|---:|---:|---|
| 1 | Clasificación de Deudores | `TO_clasificacion_deudores_actual.pdf` | 60 | 2.1 MB | https://www.bcra.gob.ar/pdfs/texord/t-cladeu.pdf |
| 2 | Capitales Mínimos de las Entidades Financieras | `TO_capitales_minimos_actual.pdf` | 204 | 5.4 MB | https://www.bcra.gob.ar/pdfs/texord/t-capmin.pdf |
| 3 | Exterior y Cambios | `TO_exterior_cambios_actual.pdf` | 201 | 2.6 MB | https://www.bcra.gob.ar/Pdfs/Texord/t-excbio.pdf |
| 4 | Protección de los Usuarios de Servicios Financieros | `TO_proteccion_usuarios_servicios_financieros_actual.pdf` | 40 | 2.4 MB | https://www.bcra.gob.ar/pdfs/texord/t-pusf.pdf |
| 5 | RI Cont. Mensual — Exigencia e integración de capitales mínimos | `TO_regimen_informativo_contable_mensual_actual.pdf` | 59 | 2.2 MB | https://www.bcra.gob.ar/pdfs/texord/t-ri-cm.pdf |

### Justificación del subset

- **Diversidad temática.** Cubre 5 dominios regulatorios distintos: clasificación de deudores (riesgo crediticio), capitales mínimos (solvencia), exterior y cambios (operatoria cambiaria), protección al usuario (relación con el consumidor financiero), régimen informativo (reporte de las entidades al BCRA). Un schema que funcione bien debe modelar bien los 5.
- **Diversidad estructural.** 4 TOs son de Normativa General y 1 es de Régimen Informativo. Tienen estructura interna distinta: la Normativa General es texto narrativo-dispositivo organizado en secciones/puntos; el Régimen Informativo es más tabular/formulario (define campos, códigos, plazos de presentación). Un schema robusto debe manejar ambas formas.
- **Diversidad de tamaño.** De 40 páginas (Protección al Usuario) a 204 páginas (Capitales Mínimos). Un factor 5x que estresa la escalabilidad del pipeline de extracción de cada estrategia.
---

## b) Formato de salida obligatorio (no negociable)

Cada instancia serializa su KG como un único archivo `kg.json` con esta estructura mínima:

```json
{
  "nodes": [
    {
      "id": "<identificador único dentro del KG>",
      "type": "<tipo de entidad según el schema de la estrategia>",
      "label": "<etiqueta legible humana>",
      "properties": { "<clave>": "<valor>", "version": "<versión vigente>" },
      "provenance": {
        "source_doc": "<nombre del archivo PDF del subset>",
        "location": "<sección / punto / párrafo donde fue extraído>"
      }
    }
  ],
  "edges": [
    {
      "source": "<id del nodo origen>",
      "target": "<id del nodo destino>",
      "relation": "<tipo de relación según el schema de la estrategia>",
      "provenance": {
        "source_doc": "<nombre del archivo PDF del subset>",
        "location": "<sección / punto / párrafo donde fue extraído>"
      }
    }
  ]
}
```

**Reglas del formato:**
- `provenance` es **OBLIGATORIO** en cada nodo y en cada edge. Sin excepción. La provenance es propiedad del elemento del grafo, NO un nodo separado del grafo.
- `id` debe ser único dentro del KG. La convención de nombres del `id` la elige cada estrategia.
- `type` y `relation` toman valores del schema diseñado por cada estrategia — **esta es la variable del experimento, varía entre instancias**.
- `properties` es un diccionario libre; su contenido depende del schema de la estrategia. Debe incluir `version` cuando aplique (ver reglas de modelado).
- `label` es texto legible para humanos (sirve para inspección y evaluación).
- El JSON debe ser válido y parseable. Un solo archivo `kg.json` por instancia.

---

## c) Reglas de modelado comunes (no negociables — aplican a las 5 estrategias)

1. **Los nodos representan entidades regulatorias REALES.** Una restricción operativa específica, una operación, una entidad financiera, una obligación, un concepto definido. NO representan la jerarquía documental. `"Punto 3.16.3.4"` NO es un nodo: es información que va en `provenance.location`. (Regla del mentor.)

2. **La versión es un ATRIBUTO del nodo**, no una estructura aparte. Se modela como `properties.version`. La versión vigente es la principal. Si se modela una versión histórica, es un nodo adicional con un valor de `version` distinto. NO sobre-modelar el versionado con estructuras complejas (nada de nodos "Versión", nada de árboles de revisión). Para este experimento, basta con la versión vigente.

3. **El contenido del KG sale del Texto Ordenado.** El subset son 5 TOs y el KG se construye sobre ellos. NO se usan Comunicaciones A como fuente de contenido. (Las Comunicaciones A son metadata satelital — útiles como diff histórico — no fuente de contenido del KG. Ver `project_scope_kg_source` en memoria.)

4. **Cada instancia documenta su schema en su propio `schema.md`.** Las entidades y relaciones del schema PUEDEN variar entre estrategias — esa es justamente la variable que el experimento mide. Lo que NO varía: el formato JSON de la sección (b) y las reglas de modelado de esta sección (c).

---

## d) Métricas que cada instancia reporta en su `report.md`

Toda instancia reporta, como mínimo:

| Métrica | Definición |
|---|---|
| Tiempo de construcción | Tiempo total: extracción de tripletas + ensamblaje del grafo. |
| Costo | Tokens consumidos y USD aproximado, si usó LLM. |
| Nodos por tipo | Conteo de nodos desglosado por cada tipo de entidad del schema. |
| Edges por tipo | Conteo de edges desglosado por cada tipo de relación del schema. |
| Densidad del grafo | edges / nodes. |
| Tipos de entidad | Nº de tipos de entidad únicos definidos en el schema. |
| Tipos de relación | Nº de tipos de relación únicos definidos en el schema. |
| Cobertura | Porcentaje aproximado de cada uno de los 5 TOs que generó al menos una tripleta (estimación, no censo exacto). |

**La evaluación downstream con preguntas complejas NO se hace en esta fase.** Se hace en la FASE 2.3, comparando los 5 KGs entre sí. Ninguna instancia evalúa su propio KG.

---

## e) Estructura de carpetas del experimento

```
data/experiment/
├── subset/                  Los 5 PDFs (ya copiados — sección a).
├── run_1_cookbook/          Run 1 — estrategia "Cookbook de Anthropic".
│   ├── schema.md            Documentación del schema diseñado.
│   ├── kg.json              KG serializado (formato sección b).
│   └── report.md            Métricas (sección d).
├── run_2_papers/            Run 2 — estrategia "Papers del estado del arte".
├── run_3_ppf_core/          Run 3 — estrategia "7 entidades core de la PPF".
├── run_4_schema_light/      Run 4 — estrategia "schema-light puro".
└── run_5_hybrid/            Run 5 — estrategia "híbrido core + emergente".
```

Cada carpeta `run_X_*/` contiene exactamente 3 archivos: `schema.md`, `kg.json`, `report.md`. Las carpetas se crean vacías en esta fase; las instancias paralelas las llenan. Cada instancia escribe SOLO dentro de su carpeta asignada.

---

## Resumen del flujo del experimento

1. **FASE 2.1 (esta).** Preparación del terreno común: subset, protocolo, template. — *completada con este documento.*
2. **FASE 2.2.** Se lanzan 5 instancias paralelas de Claude Code. Cada una recibe el `experiment_instance_template.md` con su `[ESTRATEGIA]` insertada. Cada una diseña su schema, construye su KG sobre el subset y reporta métricas.
3. **FASE 2.3.** Evaluación comparativa: se corren preguntas complejas contra los 5 KGs y se mide cuál estrategia produjo el schema más útil downstream.
