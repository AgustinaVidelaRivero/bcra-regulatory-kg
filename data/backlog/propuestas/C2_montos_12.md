# Propuesta C2 — Montos invertidos de la tabla del 1.2 de Capitales Mínimos

Entrada del backlog: **BKL-0006** (fusionada: EV1-039/quimera + RX-10 post-1b).
Formato: `.claude/skills/kg-refinement/references/formato_propuesta.md`.
Estado: PROPUESTA — presenta DOS opciones de aplicación **sin elegir** (la
elección es de la adjudicadora); la aplicación es otra unidad.

## El PDF como árbitro

`TO_capitales_minimos_actual.pdf`, **página 4**, punto **1.2. Exigencia
básica** ("Según la clase de entidad, serán las siguientes exigencias
básicas:"). La tabla, extraída **estructuralmente** (extract_tables, que
preserva columnas):

| Bancos | Restantes entidades (salvo Cajas de Crédito Cooperativas) |
|---|---|
| **5.000** | **2.500** |

(-En millones de pesos-)

Y a continuación, texto corrido: "Las compañías financieras que realicen, en
forma directa, operaciones de comercio exterior deberán observar las
exigencias establecidas para los bancos."

**Evidencia de que la linealización la cruzó** — el mismo pasaje en el texto
plano del chunk del caché (`TO_capitales_minimos_actual.pdf::1.2`, 343 chars):
«Restantes entidades / Bancos / (salvo Cajas de Crédito Cooperativas) / -En
millones de pesos- / 5.000 2.500 / …» — encabezados en un orden, valores en
otro (RX-10). El extractor emparejó según esa linealización.

**Correspondencia correcta (del PDF): Bancos ↔ 5.000 · Restantes entidades
(salvo Cajas de Crédito Cooperativas) ↔ 2.500.**

**Hallazgo adicional de la misma linealización (sub-decisión para el laudo):**
en la tabla real el paréntesis "(salvo Cajas de Crédito Cooperativas)"
califica a **Restantes entidades**, no a Bancos. Los nodos de v3 lo adjuntan a
Bancos, y existe además
`Excepcion_cajas_de_credito_cooperativas_estan_exceptuadas_de_la_exigencia_basica_de_bancos_c19412`*
construida sobre esa lectura. Esta propuesta lo deja registrado; su corrección
puede laudarse junto con C2 o como entrada aparte.
(*id verificable en v3 por prefijo `Excepcion_cajas_de_credito_cooperativas`.)

```yaml
id_falla: "BKL-0006 (EV1-039 quimera + RX-10) — tabla del 1.2 cruzada"
categoria_defecto: contenido_kg   # especie del backlog: quimera (valores cruzados entre nodos)
palanca: grafo/esquema
cambio_exacto: >
  Corregir la correspondencia entidad-monto en los dos nodos de v3 según la
  tabla del PDF (Bancos 5.000; Restantes entidades 2.500), bajo UNA de las dos
  opciones de abajo (A o B, a laudar). En ambas opciones el contenido final es:
    - nodo "bancos":      label/descripcion "Bancos (…) deberán observar
      exigencia básica de 5.000 millones de pesos", properties.monto?=5.000
    - nodo "restantes":   label/descripcion "Restantes entidades (salvo Cajas
      de Crédito Cooperativas) deberán observar exigencia básica de 2.500
      millones de pesos", properties.monto?=2.500
cita_pdf: >
  [TO_capitales_minimos_actual.pdf, página 4, punto 1.2 — tabla]: columnas
  "Bancos" | "Restantes entidades (salvo Cajas de Crédito Cooperativas)";
  fila de valores "-En millones de pesos-": 5.000 | 2.500. Texto siguiente:
  "Las compañías financieras que realicen, en forma directa, operaciones de
  comercio exterior deberán observar las exigencias establecidas para los
  bancos."
como_se_verificaria: >
  RE-TEST pre-especificado (PDF como árbitro): (1) la correspondencia
  entidad-monto post-corrección coincide con la tabla estructural extraída de
  la página 4 (Bancos 5.000 / Restantes 2.500); (2) no-regresión referencial:
  cero aristas colgantes — todo source/target de las aristas listadas abajo
  resuelve a un nodo existente; (3) si se lauda la opción A, verificación de
  que ningún otro nodo/arista del grafo referencia los ids viejos.
  NOTA: el chunk del caché NO sirve como árbitro (porta la linealización
  viciada); el árbitro es el PDF.
categoria_riesgo: alto
justificacion_riesgo: >
  El dato numérico es inequívoco en el PDF, pero la corrección exige decisión
  de modelado (renombrar ids con remapeo de aristas, o ids mentirosos) y toca
  un caso con antecedente de medición (EV1-039); "ante la duda → alto".
```

## Los dos nodos afectados y TODAS sus aristas (v3, verbatim)

`Restriccion_bancos_salvo_cajas_de_credito_cooperativas_deberan_observar_exigencia_basica_de__2d3063`
(description actual: "Bancos (salvo Cajas de Crédito Cooperativas) deberán
observar exigencia básica de **2.500** millones de pesos") — **4 aristas**:

1. `…_2d3063 --establecida_en--> TextoOrdenado_to_capitales_minimos_actual_pdf`
2. `Excepcion_cajas_de_credito_cooperativas_estan_exceptuadas_de_la_exigencia_basica_de_bancos_c19412 --exceptua--> …_2d3063`
3. `…_2d3063 --aplica_a--> Sujeto_banco`
4. `…_2d3063 --limita--> Operacion_operaciones_comercio_exterior_cb4d13`

`Restriccion_restantes_entidades_deberan_observar_exigencia_basica_de_5_000_millones_de_pesos_50658f`
(description actual: "Restantes entidades deberán observar exigencia básica de
**5.000** millones de pesos") — **2 aristas**:

1. `…_50658f --establecida_en--> TextoOrdenado_to_capitales_minimos_actual_pdf`
2. `…_50658f --aplica_a--> Sujeto_rol_alcance_capmin`

## Opción A — Renombrar ids (id honesto, remapeo total)

Los montos viven **en el id además de la description** (el id v3 deriva del
slug de la descripción). Corregir description y regenerar ids con la
convención v3:

- `…bancos…exigencia_basica_de__2d3063` → id nuevo derivado de "Bancos (salvo
  Cajas de Crédito Cooperativas) deberán observar exigencia básica de 5.000
  millones de pesos" (o de la variante sin el paréntesis si se lauda la
  sub-decisión).
- `…restantes_entidades…de_5_000_millones_de_pesos_50658f` → id nuevo derivado
  de "Restantes entidades deberán observar exigencia básica de 2.500 millones
  de pesos".

Remapeo verbatim requerido: las **6 aristas** listadas arriba (4 + 2)
reescriben su endpoint al id nuevo. Análisis mecánico: 6 aristas afectadas en
total; ningún otro objeto del grafo referencia esos ids (verificado: solo esas
aristas los tocan). Riesgo referencial: bajo en volumen (6 reescrituras) pero
introduce ids nuevos que ninguna traza/ficha histórica menciona — las
referencias EXTERNAS al grafo (fichas del 1b, expediente, mapeo) quedan
apuntando a ids que ya no existen (aceptable si se registra el mapeo
viejo→nuevo en el evento de aplicación).

## Opción B — Conservar ids, corregir solo label/description/properties

Se corrigen description/label (y `properties` de monto si aplica) dejando los
ids como están. Costo explícito: **ids mentirosos** — el id del nodo
"restantes" seguiría diciendo `…de_5_000_millones_de_pesos…` con una
description que dice 2.500 (y viceversa el sufijo hash deja de corresponder
al slug de la description). El índice léxico de `buscar_nodos` indexa label
**e id**: el id viejo seguiría matcheando queries por "5.000" hacia el nodo
de 2.500 — riesgo de confusión léxica permanente, documentado. Ventaja: cero
remapeo, referencias históricas intactas.

**Sin elección acá: la opción la lauda la adjudicadora.**
