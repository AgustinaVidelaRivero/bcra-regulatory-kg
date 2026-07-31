# Propuesta C1 — Restauración del criterio general 1.1 de Clasificación de Deudores

Entrada del backlog: **BKL-0017** (con BKL-0007/EV1-015 como antecedente).
Formato: `.claude/skills/kg-refinement/references/formato_propuesta.md`.
Estado: PROPUESTA — la aplicación es otra unidad, post-aprobación explícita.

```yaml
id_falla: "BKL-0017 (candidata b del re-triage) / antecedente BKL-0007 (EV1-015, modificada_por_v3)"
categoria_defecto: completitud_kg   # especie del backlog: ausencia (el texto no existe en ningún nodo de v3)
palanca: grafo/esquema
cambio_exacto: >
  Crear en reensamblado_v3/kg.json el nodo nuevo:
    id: "Obligacion_los_clientes_de_la_entidad_tanto_residentes_en_el_pais_de_los_sectores_publico_y_e1946e"
        (convención de ids de v3: slug completo de la descripción truncado a 80
        + sufijo sha1[:6] del slug completo; verificado inexistente en v3)
    type: "Obligacion"
    label: "Criterio general de clasificación de deudores: clientes que deben ser clasificados"
    properties:
      descripcion: "Los clientes de la entidad (tanto residentes en el país, de
        los sectores público y privado, financieros y no financieros, como
        residentes en el exterior), por las financiaciones comprendidas, deberán
        ser clasificados desde el punto de vista de la calidad de los obligados
        en orden al cumplimiento de sus compromisos y/o las posibilidades que a
        este efecto se les asigne sobre la base de una evaluación de su
        situación particular."
      tipo: "criterio_general"
    provenance: {source_doc: "TO_clasificacion_deudores_actual.pdf",
                 location: "Sección 1. Deudores comprendidos. Punto 1.1. Criterio general."}
    provenances: [ (la misma) ]
    rol_fuente: "restauracion_manual"   # trazable: no proviene del pipeline de extracción
  Aristas mínimas propuestas (endpoints existentes de v3, verbatim):
    1. (nodo nuevo) --establecida_en--> "TextoOrdenado_to_clasificacion_deudores_actual_pdf"
    2. (nodo nuevo) --aplica_a--> "Sujeto_rol_obligado_a_clasificar_clasificacion"
cita_pdf: >
  [TO_clasificacion_deudores_actual.pdf, página 4, Sección 1. Deudores
  comprendidos, punto 1.1. Criterio general — verbatim]: "Los clientes de la
  entidad (tanto residentes en el país, de los sectores público y privado,
  financieros y no financieros, como residentes en el exterior), por las
  financiaciones comprendidas, deberán ser clasificados desde el punto de vista
  de la calidad de los obligados en orden al cumplimiento de sus compromisos
  y/o las posibilidades que a este efecto se les asigne sobre la base de una
  evaluación de su situación particular."
como_se_verificaria: >
  RE-TEST pre-especificado (chunk-contra-PDF): (1) releer la página 4 del PDF y
  confirmar que properties.descripcion coincide literalmente con el punto 1.1
  (sin agregar ni quitar cláusulas; los guiones de corte de línea del PDF se
  normalizan); (2) confirmar que la provenance del nodo dice Sección 1 / punto
  1.1 (la CORRECTA del PDF) y NO la del nodo v2 de origen; (3) verificar que
  las 2 aristas existen y sus endpoints resuelven (cero colgantes); (4) réplica
  del índice: las 3 queries de la verificación de alcanzabilidad devuelven el
  nodo dentro del corte de 10.
categoria_riesgo: alto
justificacion_riesgo: >
  Aplicando el criterio fijo: aunque la descripción es transcripción literal de
  un pasaje único del PDF, la propuesta CREA estructura nueva (un nodo y dos
  aristas) y fija una provenance por juicio — "creación de estructura nueva
  (aristas, tipos)" está enumerada como alto → revisión humana.
```

## Nota obligatoria de provenance (RX-02)

El nodo v2 portador (`Obligacion_clasificar_deudores_por_calidad`) tenía la
provenance **desplazada**: apuntaba a "Punto 10.4. Proveedores de servicios de
créditos entre particulares…" — el punto de OTRO tema donde el chunk mixto
(`clasificacion::10.4`, índice→cuerpo) lo dejó anclado. **Esta propuesta
restaura el contenido con la provenance correcta leída del PDF (Sección 1,
punto 1.1, página 4) y NO copia la provenance del nodo v2.** El chunk 10.4 del
caché y el nodo v2 quedan como evidencia de contexto; el ancla de la
restauración es el PDF.

## Verificación de alcanzabilidad léxica (medida, índice replicado)

Réplica del `GraphIndex` real sobre v3 + el nodo propuesto agregado EN MEMORIA
(el kg.json no se tocó); 3 queries plausibles:

| Query | Rank del nodo (corte 10) |
|---|---|
| "criterio general clasificación deudores" | **1** |
| "qué clientes deben ser clasificados" | **1** |
| "clasificación residentes en el exterior" | **3** |

(El label propuesto se eligió con estas mediciones: la variante corta
"Criterio general de clasificación de deudores" dejaba la segunda query fuera
del top-10 — ranks 1/None/2; la variante combinada cubre las tres.)

## Qué NO hace esta propuesta

No re-extrae el chunk 10.4, no toca el nodo v2 (grafo sellado), no agrega más
aristas que las 2 mínimas (cualquier enriquecimiento adicional es otra
propuesta). La elección final de label/aristas y la aprobación son de la
adjudicadora.
