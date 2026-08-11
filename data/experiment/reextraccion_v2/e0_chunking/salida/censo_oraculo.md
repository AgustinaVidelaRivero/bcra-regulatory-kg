# Censo E0 contra el oráculo (mapa de territorio) — reconciliación diagnosticada

Oráculo: inventario de unidades por TO de
`data/experiment/exploracion/mapa_territorio_quemado_5TOs_5sets.json`
(solo su lista de unidades: `quemadas_enteras ∪ quemadas_parcialmente ∪
disponibles`; su información de quemado es irrelevante para la extracción).
Unidad del mapa: punto x.y del índice, o sección sin puntos (`S<n>`).
Inventario del parser agregado a esa granularidad:
`inventario_nivel_mapa()` de `e0_lib.py`; datos crudos en `censo_oraculo.json`.

Regla de esta reconciliación (mandato T3): el mapa NO es verdad absoluta; las
discrepancias se reportan con diagnóstico, no se "arreglan" torciendo el parser.

| TO  | unidades parser | unidades mapa | coinciden | solo mapa | solo parser |
|-----|----|----|----|----|----|
| cap | 63 | 54 | 51 | 3  | 12 |
| cla | 35 | 35 | 35 | 0  | 0  |
| ext | 124| 116| 115| 1  | 9  |
| pro | 17 | 17 | 17 | 0  | 0  |
| ric | 27 | 24 | 20 | 4  | 7  |

## cla y pro: reconciliación exacta (35/35 y 17/17)

Sin discrepancias en ninguna dirección.

## cap: 51/54 — 1 familia de discrepancia (granularidad del índice)

- **Solo mapa: S10, S11, S12** / **solo parser: 10.1–10.3, 11.1–11.6,
  12.1–12.3.** Son la MISMA discrepancia vista de ambos lados: el índice de cap
  anuncia las Secciones 10 (Agentes de calificación externa ECAI), 11 (Otras
  disposiciones) y 12 (Disposiciones transitorias) sin desglosar puntos, y el
  mapa (que hereda la granularidad del índice) las registra como unidades `S`.
  El cuerpo SÍ tiene puntos numerados bajo esas secciones (verificable:
  `estructura_cap.json`, secciones 10–12). **Diagnóstico: limitación del mapa**
  (heredada del índice del propio TO); el parser produce las unidades reales.
  Consistencia interna: las mismas 12 unidades aparecen en
  `divergencias_indice_cuerpo.json` como `en_cuerpo_sin_anunciar` de cap.

## ext: 115/116 — 1 familia de discrepancia (granularidad del índice)

- **Solo mapa: S1** / **solo parser: 1.1–1.9.** Ídem cap: el índice de ext
  anuncia la Sección 1 (Disposiciones generales) sin desglosar; el cuerpo tiene
  1.1–1.9 (p.7, `estructura_ext.json`). **Diagnóstico: limitación del mapa.**

## ric: 20/24 — 4 discrepancias de 3 clases distintas

- **Solo mapa: 3.2.** El índice anuncia "3.2. Modelo de información"; el cuerpo
  lo rinde como **3.1.4 Modelo de información** (p.8). Es la divergencia
  documental conocida de la Sección 3 (test T4-d) y aparece en
  `divergencias_indice_cuerpo.json` como el ÚNICO `anunciado_sin_cuerpo` de los
  5 TOs. **Diagnóstico: divergencia real del documento fuente**, capturada por
  ambos instrumentos: el mapa registra lo anunciado, el parser lo que existe.
  No se fabricó ningún chunk 3.2.
- **Solo mapa: 4.4.** El cuerpo NO contiene un header "4.4.": tras los cuadros
  de 4.3 (p.16–17) aparecen directamente "4.4.3. Riesgo de cambio" y "4.4.4.
  Riesgo de posiciones en opciones" (p.18), huérfanos de su padre. El parser
  los rechaza (`padre_4.4_no_abierto`, registrados en
  `estructura_ric.json → rechazos_header`) y su contenido queda como prosa del
  punto abierto precedente — no se fabrica un 4.4 inexistente. Nota: el índice
  de ric tampoco anuncia 4.4 (solo llega a 4.2); la unidad 4.4 del mapa
  proviene de sus fuentes de anclas, no del índice. **Diagnóstico: defecto del
  documento fuente** (label del padre ausente), visible en el reporte de
  rechazos; ni el mapa ni el parser lo pueden resolver sin inventar estructura.
- **Solo mapa: S1, S12** / **solo parser: 1.1, 1.2, 12.1–12.4.** Granularidad
  del índice, misma clase que cap/ext. El cuerpo tiene 1.1/1.2 (p.3) y
  12.1–12.4 (p.57–58). **Diagnóstico: limitación del mapa.**
- **Solo parser: 6.3.** "6.3. Límites mínimos:" existe en el cuerpo (p.34) y ni
  el índice ni el mapa lo anuncian. **Diagnóstico: limitación del mapa**
  (heredada del índice; el índice de ric solo anuncia 6.1 y 6.2).

## Conclusión

No hay ninguna discrepancia atribuible a una limitación del parser. Las
discrepancias se agrupan en tres clases: (1) granularidad del índice heredada
por el mapa — 5 secciones sin desglosar (cap S10–S12, ext S1, ric S1/S12) cuyo
cuerpo sí tiene puntos, más ric 6.3 no anunciado; (2) divergencia real del
documento fuente capturada por ambos instrumentos — ric 3.2 anunciado y rendido
como 3.1.4; (3) defecto del documento fuente reportado sin fabricar estructura
— ric 4.4 sin label propio con 4.4.3/4.4.4 huérfanos. Reproduce:
`python3 correr_e0.py` y comparar `salida/censo_oraculo.json`.
