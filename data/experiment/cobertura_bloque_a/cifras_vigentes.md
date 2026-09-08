# Cifras vigentes de U-COB-A — hoja única para la mesa que escribe

Unidad U-COB-A (bloque A de B5.9), cerrada el 07/09/2026 en el commit `074a712`.
Varias de estas cifras cambiaron **hasta cuatro veces** durante la unidad. Esta hoja
es el registro de cuál es la vigente y por qué las otras dejaron de serlo: quien
escriba toma la de acá, no la primera que encuentre en un reporte.

---

## 0. Restricción que gobierna todo lo de abajo

**Las 77 unidades de prosa NO están en el grafo.** Se **midieron, adjudicaron y
listaron**; el ingreso es **acto del ensamblado de la tanda**, que además tiene que
**retirar tres aristas** (§4) y pasa por el `ensamblar_corpus.py` que U-ESQ-V3
modificó.

Lo escribible hoy es **«medido y adjudicado, pendiente de ingreso»**, con la cuenta.
**No** «se recuperó», **no** «el recurso creció», **no** «el grafo ahora incluye».

---

## 1. Cifras VIGENTES

| cifra | valor |
|---|---|
| unidades extraídas | **191** (77 prosa + 114 planilla) |
| alcance | **30 páginas · 9 documentos** |
| costo real | **USD 0,7399** sobre un tope de 4,00 |
| unidades con arista `aplica_a` | **12 de 77** |
| destinatarios identificados | **18 de 77 = 23,4 %** |
| recuperación | **66,7 % – 75,0 %** — medición sobre censo, con desempate conservador declarado que la sesga a la baja |
| aristas listadas para retiro | **3** (§4) |
| brazo planilla | **declarado y AFUERA** del recurso, con su medición, hacia el bloque B |

## 2. Cifras SUPERSEDED, con su motivo

| cifra | por qué dejó de ser vigente |
|---|---|
| 13 de 77 con `aplica_a` | previa al retiro de `ri_tii::p5.b9`, que pierde sus dos aristas |
| **76,5 %** de recuperación | etapa 1 — antes de revisar los 11 CONCORDANTE |
| **75,0 % como punto** | etapa 2 — tras los 11 (k=1), antes del censo de silencios |
| 17 y 16 destinatarios | etapas 1 y 2; hoy son **18** |
| 22,1 % y 20,8 % de piso | etapas 1 y 2; hoy **23,4 %** |
| etiqueta «cota superior» | el censo de las 42 cerró el denominador; la etiqueta correcta es **medición sobre censo**, y el desempate conservador la sesga **a la baja**, no a la alta |

## 3. Nota — la coincidencia 12/16 que puede confundir

El **75,0 % de la etapa 2** y el **extremo superior del intervalo** son ambos la
fracción **12/16**, y **no son la misma cosa**: los denominadores se componen
distinto.

- etapa 2: **16 = 17 − 1**, el destinatario retirado por la clase (B).
- extremo superior: **16 = 18 − 2**, las dos ambigüedades declaradas que *saldrían*
  del denominador si se resolvieran al revés.

Es un accidente aritmético. Citar «75,0 %» sin decir cuál de los dos es, mezcla una
cifra superseded con un extremo vigente.

## 4. Las tres aristas listadas para retiro

Ninguna unidad las retiró: la adjudicación **lista**, el ingreso es del ensamblado.
El gate de tanda 1 lleva su ítem con condición de cierre verificable.

1. `Operacion «Transferencias entre cuentas CVU mismo PSPCP»` → `Sujeto_pspcp`
2. la misma `Operacion` → `Sujeto_entidad_financiera`

   — ambas de **`ri_tii::p5.b9`**, unidad clase **(B)**: definición de código de
   partida («2010100 - De CVU a CVU dentro del mismo CBU recaudador») con `aplica_a`
   colgado encima.

3. `Operacion «Presentación de informaciones al BCRA»` → `Sujeto_pscpp`

   — de **`ri_pscpp::p1.b0`**: **arista (B) dentro de unidad (C)**. La unidad tiene
   destinatario legítimo y conserva sus otras cuatro aristas; ésta se construyó sobre
   el **título de la norma remitida**, no sobre el pasaje.

---

## 5. Mapeo bloque A ↔ los doce no segmentables (tabla cruda)

Recomputado contra `data/experiment/segmentacion_84/b584_particion/particion_152.json`,
clase `no_segmentable_declarado`. **Conteo por documento, sin resumir:**

| documento | páginas | unidades | ¿en los nueve? |
|---|--:|--:|---|
| `optico` | 43 | 1 | NO |
| `plandecuentas` | 77 | **0** | NO |
| `ri_chr` | 1 | 1 | SÍ |
| `ri_con` | 16 | 1 | SÍ |
| `ri_fcem` | 1 | 1 | SÍ |
| `ri_itme` | 1 | 1 | SÍ |
| `ri_pfmipyme` | 1 | 1 | SÍ |
| `ri_pscpp` | 1 | 1 | SÍ |
| `ri_pspii` | 1 | **2** | SÍ |
| `ri_rem` | 2 | 1 | SÍ |
| `ri_spi` | 11 | 1 | NO |
| `ri_tii` | 6 | 1 | SÍ |
| **TOTAL 12** | **161** | **12** | |

**«Una unidad degenerada por documento» es FALSO y está medido**: `plandecuentas`
aporta **0** y `ri_pspii` aporta **2**. Los otros diez, una cada uno.

### 5.a Los cuatro controles, que cierran

| conjunto | docs | páginas | unidades |
|---|--:|--:|--:|
| nueve (bloque A) | 9 | **30** | **10** |
| fuera | 3 | **131** | **2** |
| control | 12 | 30 + 131 = **161** ✓ | 10 + 2 = **12** ✓ |

Los dos totales coinciden con el agregado declarado por el propio artefacto
(`no_segmentable_declarado`: 12 TOs, 161 páginas, 12 unidades).

### 5.b Identidad de las 30 páginas — la bisagra del párrafo

Verificado **a nivel de número de página, documento por documento, contra tres
artefactos**: el conteo de `particion_152.json`, la lista de páginas del censo de
forma, y las páginas reales de los chunks enviados al modelo (`chunks_a2.json`). Los
tres coinciden, y en los nueve casos son `1..N` sin huecos — de modo que la
coincidencia es de **conjuntos**, no de totales.

**A.2 extrajo exactamente el material no segmentable de esos nueve documentos,
completo y sin sobrante.**

### 5.c Las tres exclusiones, cada una por una causa distinta

La asimetría importa y va al párrafo: **dos salen porque no prescriben; uno sale
aunque prescribe.**

- **`optico`** (43 pág · `categoria: no-RI` · 0 pág de ficha) — fuera por
  **contenido**: la lectura a ciegas lo adjudicó **referencia pura**, uno de los dos
  únicos con densidad deóntica 0,000 en las tres variantes. Adenda 2 al laudo B5.5,
  cuerpo firmado.
- **`plandecuentas`** (77 pág · `categoria: RI` · **76** pág de ficha) — fuera por
  **dos causas acumuladas**: referencia pura por la misma lectura, **y** material
  ficha en 76 de sus 77 páginas, razón por la cual la enmienda 1 resuelve su caso sin
  pasar por la herencia del bloque B. Único de los doce con **0** unidades
  degeneradas.
- **`ri_spi`** (11 pág · `categoria: RI` · 0 pág de ficha) — fuera por **forma, no
  por contenido**: **tiene espina** y el parser vigente no la reconoce (numera el
  71 % de sus bloques), así que darle procedencia de página degradaría granularidad
  real. Queda declarado **caso propio** — el tercer destino de la ampliación. Adenda 2
  §7, post-firma. **Es el único de los tres que sí contiene material prescriptivo.**

---

## 6. Los siete sellos de la unidad

Todos anteriores a la medición que gobiernan, y todos en el repo desde `074a712`:
`prerregistro_A2.md` (v1) · `prerregistro_A2_v2.md` · `prerregistro_A2_v3.md` ·
`prerregistro_A2_v4.md` (vigente al correr) · `criterio_destinatario.md` ·
`adenda_criterio_concordantes.md` · `declaracion_censo_silencios.md`.
Sus sha256 completos están enumerados en el mensaje de `074a712`.
