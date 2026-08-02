# Propuesta C3 — Umbral propagado de compañías financieras (rastro residual de la inversión del 1.2)

Entrada del backlog: **BKL-0023** (fuente: `verificador`, diagnóstico
`verificador_validado` — primera corrección de origen 100 %
diagnóstico-automático; el hallazgo lo produjo el verificador dentro de su
propio gate de validación, `docs/lectura_gate_u5.md` §3).
Formato: `.claude/skills/kg-refinement/references/formato_propuesta.md`.
Estado: PROPUESTA — la aplicación es otra unidad (Fase 2 de C3, post-laudo
y commit de la adjudicadora).

## El PDF como árbitro (re-verificado contra el PDF real, no contra C2)

`TO_capitales_minimos_actual.pdf`, **página 4**, punto **1.2. Exigencia
básica** ("Según la clase de entidad, serán las siguientes exigencias
básicas:"). La tabla, extraída **estructuralmente** (extract_tables, que
preserva columnas) en esta unidad, de nuevo, sobre el PDF de
`data/experiment/subset/`:

| Bancos | Restantes entidades (salvo Cajas de Crédito Cooperativas) |
|---|---|
| **5.000** | **2.500** |

(-En millones de pesos-)

Y a continuación, texto corrido de la misma página, verbatim:

> "Las compañías financieras que realicen, en forma directa, operaciones de
> comercio exterior deberán observar las exigencias establecidas para los
> bancos."

**Valor derivado correcto:** compañías financieras con comercio exterior
directo → exigencia de bancos → **5.000 millones de pesos** (tabla del 1.2).

Comando que reproduce ambas citas:
`python3 -c "import pdfplumber; p=pdfplumber.open('data/experiment/subset/TO_capitales_minimos_actual.pdf').pages[3]; [print(t) for t in p.extract_tables()]; print(p.extract_text())"`

## El nodo afectado (vigente `data/experiment/grafo_v2/reensamblado_v3/kg.json`, verbatim pre-corrección)

```json
{
  "id": "Restriccion_las_companias_financieras_que_realicen_en_forma_directa_operaciones_de_comercio__7bb7bb",
  "type": "Restriccion",
  "label": "Exigencia compañías financieras comercio exterior",
  "properties": {
    "descripcion": "Las compañías financieras que realicen, en forma directa, operaciones de comercio exterior deberán observar las exigencias establecidas para los bancos",
    "tipo": "limite_cuantitativo",
    "umbral": "2.500 millones de pesos"
  },
  "provenance": {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "Punto 1.2. Exigencia básica."
  },
  "provenances": [
    {
      "source_doc": "TO_capitales_minimos_actual.pdf",
      "location": "Punto 1.2. Exigencia básica."
    }
  ],
  "rol_fuente": "cuerpo"
}
```

La `descripcion` es **fiel al PDF** (coincide byte a byte con la oración
citada arriba, normalizando el salto de línea interno del PDF a espacio y
sin el punto final; verificado programáticamente en esta unidad). El defecto vive solo en
`properties.umbral`: porta **2.500** — el valor que la tabla linealizada
viciada (RX-10) asignaba a "bancos" al momento de la extracción — cuando el
árbitro fija bancos = **5.000**. Es un **valor derivado**: la referencia
textual "exigencias establecidas para los bancos" fue resuelta por el
extractor contra la tabla invertida y quedó horneada en un property de un
nodo ajeno a la tabla; por eso C2/BKL-0006 (corrección por enumeración de
ids de los dos nodos de la tabla) no lo alcanzó.

Aristas del nodo (**3**, verbatim por endpoints; ninguna cambia):

1. `…_7bb7bb --establecida_en--> TextoOrdenado_to_capitales_minimos_actual_pdf`
2. `…_7bb7bb --aplica_a--> Sujeto_compania_financiera`
3. `…_7bb7bb --limita--> Operacion_operaciones_comercio_exterior_cb4d13`

## Convención de identidad — opción A, sin remapeo (explícito)

Bajo la convención laudada en C2 (**opción A**: el id del nodo deriva del
slug de su `descripcion`), esta corrección **no toca el id**: cambia UN
property (`umbral`) y la `descripcion` queda **byte-idéntica** → el slug no
cambia → el id `…_7bb7bb` queda **intacto**. En consecuencia: **cero
remapeo de aristas**, cero ids nuevos, referencias históricas (traza del
gate U5, fichas, backlog) intactas. No es la opción B de C2 (ids
mentirosos): acá el id no porta monto alguno, así que conservarlo es
consistente con la opción A, no una excepción a ella.

## Verificación de especie (reporte al laudo; sin cambio propio)

Laudo vigente: `quimera`. Contra el catálogo cerrado de
`docs/spec_backlog_refinamiento.md` §2: `quimera` = "label de un punto con
description de otro, o nodos con contenido cruzado (ej.: CQN2-013;
**EV1-039**)". Calza: el property porta el valor de la **otra columna** de
la tabla (contenido cruzado entre nodos), y el ejemplo canónico de la
especie en el catálogo es EV1-039 — exactamente esta inversión del 1.2.
Alternativas evaluadas: `fabricacion` no calza (el valor existe en el PDF;
está mal emparejado, no inventado); `contenido_sin_subespecie` no calza (es
la especie provisional del intake automático y acá la sub-especie es
determinable). **Ninguna calza mejor; `quimera` se sostiene**, con el matiz
de que es la variante *derivada* de la quimera: el cruce no está en
label/descripcion sino en un property resuelto por referencia textual
contra la tabla viciada (la lección que motiva la precisión a RX-10).

```yaml
id_falla: "BKL-0023 (verificador validado, gate U5, caso EV1-039 en rama de lectura) — umbral derivado de la tabla del 1.2 invertida"
categoria_defecto: contenido_kg   # especie del backlog: quimera (laudada; verificación de catálogo arriba)
palanca: grafo/esquema
cambio_exacto: >
  En el nodo
  Restriccion_las_companias_financieras_que_realicen_en_forma_directa_operaciones_de_comercio__7bb7bb
  del grafo vigente (data/experiment/grafo_v2/reensamblado_v3/kg.json),
  reemplazar properties.umbral: "2.500 millones de pesos" →
  "5.000 millones de pesos". ÚNICO cambio en todo el grafo: descripcion,
  label, type, provenance(s), rol_fuente, id y las 3 aristas del nodo quedan
  byte-idénticos; ningún otro objeto se toca.
cita_pdf: >
  [TO_capitales_minimos_actual.pdf, página 4, punto 1.2 — tabla]: columnas
  "Bancos" | "Restantes entidades (salvo Cajas de Crédito Cooperativas)";
  fila de valores "-En millones de pesos-": 5.000 | 2.500. Texto siguiente:
  "Las compañías financieras que realicen, en forma directa, operaciones de
  comercio exterior deberán observar las exigencias establecidas para los
  bancos." Derivación: exigencia de bancos = 5.000 millones de pesos.
como_se_verificaria: >
  RE-TEST pre-especificado (PDF como árbitro, laudado como vía de cierre):
  (a) properties.umbral post-corrección coincide con el valor de la columna
  "Bancos" de la tabla estructural de la página 4 (5.000 millones de pesos);
  (b) descripcion e id del nodo byte-idénticos al pre;
  (c) cero cambios de conteos (4.459 nodos / 8.046 aristas) y cero cambios
  en todo otro objeto del grafo (diff estructural: el único delta es
  properties.umbral de …_7bb7bb);
  (d) shapes delta 0 (scripts/shapes_validator.py pre vs post).
  NOTA: el chunk del caché NO sirve como árbitro (porta la linealización
  viciada); el árbitro es el PDF.
categoria_riesgo: bajo
justificacion_riesgo: >
  Transcripción de un dato verificable contra un pasaje único e inequívoco
  del PDF (tabla del 1.2 + oración de compañías financieras), sin decisión
  de modelado: un solo property, un solo nodo, id intacto por convención ya
  laudada (opción A), cero remapeo. La derivación (compañías financieras →
  exigencia de bancos) está literal en el texto. Aplicación igualmente
  post-laudo: el circuito vigente exige propuesta commiteada antes de tocar
  el grafo.
```

## Barrido de propagación de la clase (familia 2.500 / 5.000 / 1.500 / 700)

Pregunta del barrido: ¿quedan otros nodos del vigente con valores de la
familia de las **dos tablas** de Capitales Mínimos horneados en properties?
Las dos tablas del PDF (ambas re-extraídas estructuralmente en esta unidad):

- **pág. 4, punto 1.2** (exigencia básica): Bancos **5.000** | Restantes
  entidades (salvo Cajas de Crédito Cooperativas) **2.500**.
- **pág. 177, punto 12.1** (transitoria 01/06/24–31/12/24): Bancos
  **1.500** | Restantes entidades (salvo Cajas de Crédito Cooperativas)
  **700** — misma linealización desordenada en el texto plano ("Restantes
  entidades / Bancos / Período (salvo …)").

Método: escaneo recursivo de TODAS las properties (cualquier campo,
anidamiento incluido) de los 4.459 nodos del vigente, con regex que cubre
los formatos numéricos 2.500/2,500/2 500/2500 (ídem 5.000, 1.500) y 700
como número aislado (lookarounds que excluyen sub-cadenas de números
mayores). Script: `barrido_propagacion_c3.py` (corrido desde scratchpad
temporal; reproducible con el comando del pie). Cada coincidencia se
adjudicó contra el PDF real (páginas citadas por fila).

**Resultado: 10 coincidencias en 7 nodos únicos.**

| Nodo | Campo | Valor (extracto) | Veredicto |
|---|---|---|---|
| `Restriccion_bancos_deberan_observar_exigencia_basica_de_5_000_millones_de_pesos_380229` | `properties.descripcion` | "… exigencia básica de 5.000 millones de pesos" | **correcto** — PDF pág. 4, col. Bancos = 5.000 (nodo post-C2) |
| `…_380229` | `properties.umbral` | "5.000 millones de pesos" | **correcto** — ídem |
| `Restriccion_restantes_entidades_salvo_cajas_de_credito_cooperativas_deberan_observar_exigenc_7b4b77` | `properties.descripcion` | "… exigencia básica de 2.500 millones de pesos" | **correcto** — PDF pág. 4, col. Restantes = 2.500 (nodo post-C2) |
| `…_7b4b77` | `properties.umbral` | "2.500 millones de pesos" | **correcto** — ídem |
| `Restriccion_las_companias_financieras_que_realicen_en_forma_directa_operaciones_de_comercio__7bb7bb` | `properties.umbral` | "2.500 millones de pesos" | **rastro de inversión** — PDF pág. 4: bancos = 5.000; ya de alta como BKL-0023 (objeto de esta propuesta) |
| `Restriccion_minimo_20_dias_para_conjuntos_neteo_grande_83fd71` | `properties.description` | "… supere las 5.000 en cualquier momento del trimestre …" | **correcto** — PDF pág. 76 (punto 4.2), verbatim; es conteo de operaciones, no monto en pesos |
| `Excepcion_no_se_aplicara_el_plazo_minimo_de_veinte_dias_habiles_para_el_calculo_del_period_d2d648` | `properties.descripcion` | "… más de 5.000 operaciones …" | **correcto** — PDF pág. 89 (punto 4.3), verbatim |
| `Restriccion_exclusion_de_extension_por_cantidad_de_operaciones_9f5f83` | `properties.description` | "La sola existencia de 5.000 operaciones o más …" | **correcto** — PDF pág. 95 (punto 4.3), verbatim |
| `Obligacion_desde_el_01_06_24_y_hasta_el_31_12_24_correspondera_que_tales_entidades_en_funci_9f9564` | `properties.descripcion` | "… Bancos 1.500 millones de pesos; …" | **correcto** — PDF pág. 177, tabla del 12.1, col. Bancos = 1.500 (emparejamiento correcto pese a la misma linealización; consistente con la precisión 31-07 de RX-10) |
| `…_9f9564` | `properties.descripcion` | "… Restantes entidades (salvo Cajas de Crédito Cooperativas) 700 millones de pesos." | **correcto** — PDF pág. 177, col. Restantes = 700 |

Chequeo complementario (fuera del alcance mandado, USD 0): mismo regex sobre
`label` e `id` de los 4.459 nodos — solo los labels/ids de los dos nodos
post-C2 (montos correctos por re-test C2) y un falso positivo del sufijo
hash `…_e5f700` (el "700" es parte del hash del id, no un monto; descartado).

**Candidatas de alta nuevas: NINGUNA.** El único rastro de inversión del
barrido es `…_7bb7bb`, ya de alta como BKL-0023. No hay filas
"no adjudicable con el PDF a mano". (Regla del mandato: todo rastro nuevo
habría quedado listado para laudo, sin alta propia.)

Reproduce: `python3 barrido_propagacion_c3.py data/experiment/grafo_v2/reensamblado_v3/kg.json`
(script en el scratchpad de la sesión; salida íntegra pegada en el reporte
de la unidad).
