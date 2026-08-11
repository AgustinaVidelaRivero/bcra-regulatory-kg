# Informe de unidad — E0: chunking estructural determinístico (issue #9)

Primera unidad de implementación del pipeline de re-extracción v2. Diseño
vinculante: `docs/diseno_reextraccion_v2.md` §3-E0. Cero llamadas a APIs de
LLM: todo el código es determinístico puro. Ningún archivo preexistente del
repo fue modificado; todo lo nuevo vive bajo
`data/experiment/reextraccion_v2/e0_chunking/`.

## 1. Insumos (solo lectura)

Los 5 PDFs de `data/experiment/subset/` (reproduce:
`shasum -a 256 data/experiment/subset/*.pdf`):

| sha256 | archivo |
|---|---|
| `f6ab71be7783c4192e67c13ee84f1fc585c6ae5e05aa074961c9c59429280bb8` | TO_capitales_minimos_actual.pdf |
| `6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2` | TO_clasificacion_deudores_actual.pdf |
| `baea7264918877da132acca5f7ec6df1a3a33fd5be77109b90360a3d586bc130` | TO_exterior_cambios_actual.pdf |
| `48564cc714daa9a8c8bbd7115dfe006307ca7cb1c3d78b106c52555fe75a12ec` | TO_proteccion_usuarios_servicios_financieros_actual.pdf |
| `754c888ae6034f63eb04991c5cad441435b6bf6f8e8fb3669fd2bb279c3b35d5` | TO_regimen_informativo_contable_mensual_actual.pdf |

Oráculo de reconciliación (T3): inventario de unidades por TO de
`data/experiment/exploracion/mapa_territorio_quemado_5TOs_5sets.json` (solo su
lista de unidades; su información de quemado no participa).

## 2. Arquitectura implementada

Código: `e0_lib.py` (parser + chunker + censo + cobertura), `correr_e0.py`
(driver), `selftest_e0.py` (determinismo + cobertura + tests de aceptación).
Salida: `salida/*.json` + `salida/censo_oraculo.md`.

### 2.1 Extracción de líneas con posición (la señal estructural central)

`pdfplumber.extract_words` agrupadas en líneas por coordenada vertical
(±2 pt); cada línea conserva su **columna x0**. La indentación es la señal que
el chunker v1 nunca usó y la que resuelve el problema central del diseño:
anclar la prosa sin numerar a su contenedor. Evidencia de calibración (ext
p.14): los cierres sin numerar del 2.7 corren en x0=104,9 — la columna de
texto del nivel 2 — mientras la continuación de un 2.7.x corre en 140,3; en
texto plano ambas son indistinguibles.

### 2.2 Roles de página

`portada` (antes del índice) · `indice` (marcador `-Índice-` y variantes, más
continuación sin marcador: página que sigue a una de índice con ≥2 líneas
`Sección N.` — caso ric p.2) · `tabla_norma_origen` (contiene `NORMA DE
ORIGEN`) · `historial` (desde la página que anuncia el historial de
Comunicaciones de la norma, pegajoso) · `cuerpo` (resto). Los roles no-cuerpo
quedan fuera del universo de chunking y de cobertura, contados por TO en
`conteos.json → roles_pagina`.

### 2.3 Encabezados y pies de página

Por página de cuerpo se descartan (con registro individual en
`estructura_<to>.json → accounting`): título del TO en mayúsculas, línea
`B.C.R.A.` (a veces fusionada con la línea corrida de sección: `B.C.R.A.
Sección 3. …`), la línea corrida `Sección N. …` (capturada como metadata: es
la que abre secciones), la cola envuelta del título de sección (renglón a
≤16 pt del anterior que no arranca con numeración — la condición de numeración
evita comerse el primer punto de la página, defecto detectado en ric p.28), y
el pie `Vigencia:` / `Versión: … Página N` / fecha.

### 2.4 Validación de headers de punto (anti RX-03)

Un candidato `x.y.z…` (con o sin punto final: el BCRA omite el punto en
labels como `13.4.1 el pago…`, ext p.172) solo abre punto si pasa CINCO
guardas, cada rechazo registrado con su motivo:

1. **Raíz ≤ 30** (mata citas de Comunicaciones y montos).
2. **Resto no vacío** — una numeración sola (`9.3.13.`) es referencia envuelta;
   este caso, aceptado, bloqueaba los 13 puntos reales de ext 9.3.
3. **Sección**: el primer componente es la sección corriente de la página.
4. **Secuencia**: el padre está abierto en la pila y el último componente
   supera al último hermano. Los saltos se aceptan y REPORTAN
   (`saltos_numeracion`); los duplicados se rechazan.
5. **Columna + forma**: los hermanos comparten columna de label (±3 pt) y el
   primer hijo corre en la columna de texto del padre. Como las columnas
   DERIVAN entre páginas (páginas de Comunicaciones con márgenes distintos:
   deriva medida de hasta 34 pt, ric 11.2 en x0=42,6 vs hermanos en 76,6), la
   columna incompatible no rechaza sola: se acepta con aviso si el resto tiene
   forma de título (mayúscula/comilla inicial), o si es un ítem de lista en
   minúscula en contexto de lista (línea previa terminando en `:` o `;` —
   labels reales en minúscula medidos: ext 10.11.x, 13.3.1, 13.4.x, 8.5.14.x).
   Las referencias cruzadas a inicio de renglón ("en el marco de…", "de las
   citadas normas…") no cumplen ninguna de las dos condiciones.

### 2.5 Anclaje de prosa por indentación

La prosa se anexa al punto abierto más profundo, SALVO que su x0 coincida
(±3 pt) con la columna de texto de un ancestro estricto: entonces cierra los
puntos más profundos y se ancla al ancestro (cierres e intersticiales — el
mecanismo "chapeau perdido" de U6). El re-anclaje exige forma de prosa
(≥55 chars y sin fronteras de columna): las filas de tabla pueden caer por
azar en la columna de un ancestro y cerrarían puntos a mitad de tabla (caso
medido: tabla de aforos de cap p.108 en x0=103,3, que cerraba 5.3.2 y perdía
5.3.2.4–5.3.2.5).

### 2.6 Chunker

Chunk = **punto terminal** (sin hijos) o **sección sin puntos** (`S<n>`, caso
ric S2 / pro S5). Texto propio: línea de label + segmentos propios. Herencia:
por cada ancestro, de la sección hacia abajo — título (`encabezado`), chapeau
de sección, intros, intersticiales y cierres — cada tramo con provenance
propia (tipo, unidad de origen, páginas). Ids `to::unidad`, únicos por
construcción (un solo cuerpo, duplicados rechazados por secuencia).
`sha256_propio` (texto propio) y `sha256_completo` (herencia + propio) por
chunk.

### 2.7 Detección de tablas y fórmulas (solo flag, sin tratamiento)

`contenido_tabular`: ≥3 líneas con ≥2 fronteras de columna (huecos >15 pt), o
≥5 sumando las de 1 frontera con último token numérico (filas
'concepto … ponderador') o primer token código (≥3 dígitos, filas 'código
partida descripción'), o marcador lexical `Cuadro N`. `formula`: línea con
`=`, `donde:` aislado, o anuncio "…siguiente expresión:". Cada flag guarda su
evidencia (líneas disparadoras) en el chunk.

## 3. Conteos por TO

| TO | páginas (cuerpo/índice/tabla/historial/portada) | secciones | chunks | tabular | fórmula | mediana chars propio | mediana chars completo | rechazos | saltos | avisos deriva |
|----|----|----|----|----|----|----|----|----|----|----|
| cap | 204 (175/2/9/17/1) | 12 | 401 | 12 | 19 | 409 | 1.246 | 43 | 0 | 30 |
| cla | 60 (40/2/6/11/1) | 10 | 127 | 0 | 0 | 314 | 898 | 4 | 0 | 3 |
| ext | 201 (178/5/7/10/1) | 15 | 783 | 1 | 0 | 295 | 1.206 | 66 | 1 | 3 |
| pro | 40 (31/1/2/5/1) | 5 | 88 | 0 | 0 | 384 | 843,5 | 3 | 0 | 1 |
| ric | 59 (57/2/0/0/0) | 12 | 78 | 16 | 23 | 638 | 770,5 | 18 | 2 | 21 |

Total: **1.477 chunks** = 1.475 puntos terminales (401+127+783+87+77) + 2
secciones sin puntos (pro S5 "Sanciones…" y ric S2 "Entidades comprendidas").
"Completo" = herencia + propio. Reproduce: `python3 correr_e0.py` →
`salida/conteos.json`.

## 4. Divergencias índice↔cuerpo (T1, ambas direcciones)

El índice se parsea por separado (`indice_<to>.json`) y NO gobierna ningún
corte. `divergencias_indice_cuerpo.json`:

- **anunciado_sin_cuerpo**: ric 3.2 "Modelo de información" (el cuerpo lo
  rinde como 3.1.4, p.8 — la divergencia conocida de la Sección 3, T4-d).
  Único caso en los 5 TOs.
- **en_cuerpo_sin_anunciar**: cap 10.1–10.3, 11.1–11.6, 12.1–12.3 (el índice
  no desglosa las secciones 10–12); ext 1.1–1.9 (ídem Sección 1); ric 1.1,
  1.2, 4.3, 4.5, 6.3, 12.1–12.4. cla y pro: cero divergencias.
- **titulos_distintos** (bonus del contraste): cla 7.4 (índice dice
  "Superintendencia de Entidades Financieras y Cambiarias", cuerpo abrevia
  "SEFyC…"), ext 5.2 (errata del índice: "Tipo de cambo minorista" vs cuerpo
  "cambio"), ric 4.2 y 6.2 (singular/plural).

## 5. Censo contra el oráculo (T3)

Reconciliación completa con diagnóstico por discrepancia en
`salida/censo_oraculo.md`. Resumen: cla 35/35 y pro 17/17 exactos; cap 51/54,
ext 115/116, ric 20/24 — ninguna discrepancia atribuible al parser: 5
secciones sin desglosar por el índice (el mapa hereda esa granularidad; el
cuerpo tiene los puntos), 1 divergencia documental real (ric 3.2→3.1.4) y 1
defecto del documento fuente (ric 4.4 sin label propio; 4.4.3/4.4.4 huérfanos
rechazados con registro, no fabricados).

## 6. Tests de aceptación (T4) — evidencia

Automatizados en `selftest_e0.py` (corrida: 30/30 PASS).

**(a) ext 3.9 entero (BKL-0024).** Chunks `3.9.1`–`3.9.5` presentes (p.33);
"USD 200" en el texto propio de 3.9.1: «conjunto de los conceptos señalados,
el equivalente a USD 200 (dólares». 3.9 no es chunk terminal: su título, su
intro ("Las entidades podrán dar acceso…") y su cierre ("En todos los casos,
la entidad deberá obtener evidencia…") viajan como herencia de los cinco.

**(b) Herencia de chapeau.** ext 7.6: el encabezado sin numerar (1.144 chars)
viaja en la herencia de los 8 chunks 7.6.x, con el plazo verbatim: «ingresar
las divisas dentro de los 20 (veinte) días hábiles de la fecha de puesta a
disposición» (U6-007). ext 2.7: los DOS párrafos de cierre sin numerar (638
chars: cómputo a los límites mensuales + declaración jurada) viajan como tramo
`cierre` en la herencia de 2.7.1–2.7.4 (U6-001).

**(c) cla 1.1, cla 4.5, ext 9.2 — CONTRADICCIÓN DEL MANDATO REPORTADA.** El
mandato esperaba verlos como divergencia "anunciado sin cuerpo". El cuerpo SÍ
los contiene: `1.1. Criterio general.` (cla p.4, x0=76,6), `4.5. Deudores que
no deben ser objeto de clasificación.` (cla p.15), `9.2. Entidad nominada por
el exportador.` (ext p.123) — labels verificados contra el PDF crudo. La
expectativa proviene de RX-04 (`docs/backlog_reextraccion.md`), que describe
el output del chunker v1 — "Su texto está en el corpus (…) pero no existe como
pasaje con nombre" — no el PDF. Por regla d del circuito, mandan los archivos:
E0 los produce como chunks reales (454 / 285 / 1.500 chars propios), que es
exactamente el comportamiento que RX-04 pedía del chunker nuevo. No se fabricó
ningún chunk vacío.

**(d) ric Sección 3.** `3.2` es el único `anunciado_sin_cuerpo` del corpus y
el cuerpo lo rinde como chunk `3.1.4 Modelo de información` (flaggeado
tabular). Capturado exactamente como divergencia, sin fabricar un 3.2.

**(e) Tablas.** Flags por TO: cap 12, ric 16, ext 1, cla 0, pro 0. Los cuadros
exigidos salen flaggeados: cap `2.12.2.4` (tabla de calificaciones AAA…B-),
cap `2.13` (CCF, el cuadro de U6-012), ric `3.1.4` y `7.2` (cuadros de
partidas código/concepto). Tres ejemplos con evidencia en
`chunks_cap.json`/`chunks_ric.json → flags.evidencia_tabular`:
cap 2.12.2.4 («AAA A+ BBB+ BB+»), ric 7.2 («Cuadro 7.2.1.», «60100000
Disminución de la exigencia…»), ric 3.1.4 (filas de partidas con código).

## 7. Selftest (T5) — 30/30 PASS

1. **Determinismo**: pipeline corrido DOS veces → 19/19 archivos de salida con
   sha256 idénticos.
2. **Cero pérdida de texto**: universo = líneas de contenido de páginas de rol
   cuerpo, tras descontar el accounting línea-por-línea de encabezados/pies
   (cada descarte registrado con su texto y página). Método: recorrido del
   árbol contando cada línea por identidad de objeto — toda línea pertenece a
   exactamente un nodo (label o segmento; los tramos de herencia son
   proyecciones de los segmentos de ancestros, no copias contadas). Resultado:
   cap 6.311/6.311, cla 1.249/1.249, ext 6.500/6.500, pro 1.052/1.052,
   ric 1.760/1.760; 0 duplicadas y 0 huérfanas en los 5.
3. **T4 automatizados**: los 5 casos de §6.

## 8. Limitaciones conocidas (documentadas, no silenciosas)

- **ric 4.4**: sin label en el cuerpo (ni `4.4.` ni `4.4.1.` ni `4.4.2.`
  existen como línea en todo el PDF; la única mención previa es la referencia
  "4.4.1.- se consignarán…" dentro de la prosa de 4.3.1.1, p.14). Los labels
  huérfanos `4.4.3. Riesgo de cambio` (p.18, top 143,6) y `4.4.4. Riesgo de
  posiciones en opciones` (p.18, top 407,4) se rechazan
  (`padre_4.4_no_abierto`) y **su contenido normativo completo —ambos títulos
  más sus cuadros de partidas (553100/xx/M…, 554100/xx…)— queda como texto
  PROPIO (continuación) del chunk `ric::4.3.3`** (que abarca p.15–18,
  4.499 chars, e incluye además el 4.3 duplicado de p.16 y la tabla apaisada
  de p.17). **Ancla imprecisa conocida**: el contenido de 4.4.x está presente
  y ningún carácter se pierde, pero viaja bajo provenance 4.3.3. A resolver:
  decisión pendiente de laudo entre (i) tratarlo en E1 con instrucción al
  extractor sobre labels huérfanos embebidos, o (ii) iterar el parser con una
  regla de recuperación de huérfanos que fabrique el padre 4.4 vacío — opción
  hoy descartada por la regla de no fabricar estructura.
- **ric 11.2.1/11.2.2**: existen solo como títulos de cuadros ("Cuadro
  11.2.1. b)") dentro del contenido de 11.2 → viajan como herencia de 11.2.3,
  no como chunks propios. Salto 0→3 reportado.
- **ext 14.5.4–14.5.6**: ausentes del documento fuente (14.5.3 → 14.5.7 en el
  flujo de p.181–182); salto reportado.
- **Numeración duplicada del fuente**: ric repite `4.3` (p.14 normas / p.16
  modelos) y `10.1.4.3` (dos códigos distintos, p.44); ext repite el párrafo
  de `3.16.4` en p.60–61. Política: el primero gana, los repetidos quedan como
  prosa del punto abierto y en el registro de rechazos.
- **Riesgo residual de falsos headers**: una referencia envuelta que sea
  sucesor exacto del hermano abierto, con mayúscula inicial o en contexto de
  lista, pasaría las guardas. Los avisos (`aceptado_con_columna_derivada`: 57
  en total, `aceptado_lista_minuscula`: 1) hacen auditable esa frontera.
- **Guiones de corte de línea**: el texto conserva la linealización cruda del
  PDF (con guiones de silabeo); des-silabear es decisión de E1, no de E0.

## 9. Reproducción

```
cd data/experiment/reextraccion_v2/e0_chunking
python3 correr_e0.py          # regenera salida/
python3 selftest_e0.py        # 2 corridas + cobertura + T4 (30 checks)
```

## 10. Corrección post-calibración (2026-08-11): dos reglas de principio

**Motivo.** La calibración de E1 sobre pro expuso un defecto de costura del
chunking: los acápites `vii)`–`x)` de `pro::2.3.1.1` (p.9) salían como
segmentos intersticiales de 2.3.1 —herencia de los CUATRO chunks 2.3.1.x— en
vez de texto propio de 2.3.1.1. Causa raíz: la deriva de columnas de la p.9
hace que los marcadores corran en x0=133,3 = text_col de 2.3.1 (mientras los
acápites `i)`–`vi)` de p.7–8 corren fuera de tolerancia), y el re-anclaje de
§2.5 los subía al padre. Junto con eso, había fronteras de segmento que caían
en palabras partidas por guion de fin de línea. Ambos defectos se corrigen por
regla general (no por parche del caso), como post-procesamiento del árbol: el
parseo de §2.4–2.5 no cambió.

**Regla 1 — continuidad de enumeración en costuras**
(`e0_lib.aplicar_continuidad_enumeracion`). Un segmento intersticial cuyo
primer marcador de enumeración continúa la secuencia con la que termina el
texto propio del hermano terminal inmediatamente anterior se reasigna como
continuación de ese propio; las líneas envueltas del ítem (sin marcador, en
columna más profunda que la del marcador) lo siguen. Detector de secuencias:
marcadores line-initial `vii)` / `h)` / `3)` / `(ii)` (minúsculas con
paréntesis de cierre — única forma de acápite de los 5 TOs); familias romano
canónico 1–39, letra a–z, número 1–99; la ambigüedad (`i` es romano 1 y letra
9) se resuelve exigiendo una familia común donde el candidato sea sucesor
inmediato del último marcador del propio. Límites documentados: solo
intersticiales (los `cierre` —enumeraciones nuevas del padre, arrancan en
`i)`: ext 3.16.2, 4.3.2, 14.2.1, 14.4— quedan fuera por diseño); solo hermano
anterior terminal; enumeraciones anidadas hacen que el último marcador sea el
interno (falla hacia NO reasignar); estilos `a.` / `I)` / `1.-` no cubiertos
(no aparecen como acápites en el corpus). Un marcador que no sucede corta la
cadena del hueco.

Resultado: **8 segmentos (12 líneas) reasignados, todos `pro 2.3.1 →
2.3.1.1`** — exactamente el caso conocido; cap/cla/ext/ric: 0. Evidencia
completa por reasignación (página, x0, motivo, primera línea) en
`salida/correcciones.json → pro.reasignaciones_continuidad`.

**Regla 2 — cero cortes intra-palabra**
(`e0_lib.corregir_fronteras_intra_palabra`). Ninguna frontera de segmento
puede caer en palabra partida por guion: la frontera se corre línea por línea
(la línea que cierra la palabra se mueve al segmento que terminaba partido)
hasta punto fijo; el donante vacío se elimina. Solo se corrige DÓNDE cae la
frontera; el des-silabeo sigue siendo decisión de E1 (§8). Detector
(`e0_lib._clasificar_frontera`): última línea termina en letra+guion, y la
línea documental siguiente existe, no es label, está en la misma sección,
tiene forma de prosa (sin fronteras de columna) y arranca en minúscula (el
silabeo del BCRA continúa siempre en minúscula). Los guards son sobre la
línea SIGUIENTE — la línea partida no se filtra por sus propias fronteras de
columna, porque los renglones de definición de fórmula (`RM: … en la Sec-` →
`ción 6.`, cap 8.5) las tienen y su continuación es genuina. Exclusiones
auditadas (41 en total, listadas en `correcciones.json →
fronteras_intra_palabra.sospechosas_excluidas`, solo cap y ric): filas de
rating `AA- A- BBB- B-` y encabezados `-En millones de pesos-` (la línea
siguiente arranca en dígito o mayúscula), subíndices de fórmula (`K` +
`SA`/`A`/`R`, cap 3.1.11.2), cierres de aparte `-…-` seguidos de mayúscula, y
celdas de cuadros de partidas cuya sílaba continúa DENTRO de la fila
siguiente (`23100000 nancieras…`, ric 6.2) — irresolubles moviendo fronteras:
son la linealización de tablas ya delegada a E1 (§8). Todas las exclusiones
son intra-nodo y ninguna cae en la última frontera de un nodo: no cruzan
chunks.

Resultado (antes → después, por TO): cap 200→0, cla 10→0, ext 0→0, pro 23→0,
ric 37→0 (**270 fronteras eliminadas, 345 líneas corridas** — las corridas
superan a las fronteras por cascadas de líneas que también terminaban
partidas). Las 345 corridas fueron **todas intra-nodo** (`mismo_nodo: true` en
`correcciones.json`): el texto propio concatenado de los chunks no cambió por
esta regla; donde la frontera corrida vació un tramo o fusionó tramos
adyacentes de un mismo ancestro (cierres del 8.5 de cap), el texto completo
heredado tampoco cambia — solo la partición en tramos.

**Impacto total sobre la salida** (reproduce: comparar `salida/` contra la
copia pre-corrección del paquete de revisión): mismos 1.477 ids de chunk;
`sha256_propio` cambia SOLO en `pro::2.3.1.1` (3.888 → 4.764 chars, ahora
cierra en «cio de que se trate.»); `sha256_completo` cambia solo en
`pro::2.3.1.{1,2,3,4}` (la herencia de 2.3.1.2–2.3.1.4 pierde los 8 tramos
intersticiales); censo contra el oráculo, cobertura (cero pérdida, mismas
líneas: 6.311/1.249/6.500/1.052/1.760), divergencias índice↔cuerpo y medianas
de §3: idénticos a la corrida original. `conteos.json` agrega cuatro campos
por TO (`reasignaciones_continuidad`, `fronteras_intra_palabra_antes/despues`,
`lineas_corridas_por_frontera`); `salida/correcciones.json` es archivo nuevo.

**ric 4.4 re-chequeado con la regla 1**: sin cambio, tal como se esperaba —
no hay continuidad de lista en esa costura (el propio de 4.3.3 no termina en
enumeración y los labels huérfanos `4.4.3.`/`4.4.4.` no son marcadores de
acápite), y además el contenido viaja como texto propio (continuación) de
4.3.3, no como intersticial, fuera del alcance de la regla. Cero
reasignaciones en ric; la limitación de §8 sigue vigente, pendiente de laudo.

**Selftest ampliado: 42/42 PASS** (los 30 checks originales re-pasados —
determinismo 20/20 archivos, cobertura, T4 a–e— más 12 nuevos: acápites en el
propio de 2.3.1.1 y herencia limpia de 2.3.1.2–4, toda reasignación es el
caso conocido, fronteras después = 0 en los 5 TOs, ric sin reasignaciones y
4.4.x aún en 4.3.3). Reproduce: `python3 selftest_e0.py`.

---

## Enmienda 01 (2026-08-11) — mini-chunks como unidades de extracción

Implementación de `docs/enmienda_01_diseno_reextraccion_v2.md` §2.a. La
corrida enmendada vive en `salida_enm01/` (la calibración sellada `salida/`
queda intacta; los chunks terminales de `salida_enm01/` son byte-idénticos a
los sellados — solo se AGREGAN mini-chunks, interleaved en orden documental).

**Criterio de materialización adoptado (letra de §2.a, agrupado):** los
tramos `encabezado` son línea de título pura en los 5 TOs (387/387) y nunca
materializan; los segmentos de prosa (intro/intersticial/cierre/chapeau) no
contienen la línea de label y materializan siempre que su texto normalizado
no sea vacío. Los segmentos contiguos del mismo rol de una unidad se funden
en UN mini-chunk (intro/cierre/chapeau son contiguos por construcción; evita
fragmentar fórmulas partidas por columna); intersticiales: uno por segmento
con `::<n>`. La heurística de escala de la enmienda (una línea ≤140 ≈ título)
se DESCARTÓ como criterio: excluiría intros normativos de una línea (caso
pro 2.7, «deberán contar con sendos hipervínculos…»). Invariante: todo bloque
de prosa de ancestro con texto no vacío tiene exactamente un responsable.

**Resultado: 286 mini-chunks** (estimación de la enmienda: 284) — intro 218,
cierre 57, chapeau_seccion 8, intersticial 3; por TO: cap 61, cla 16,
ext 190, **pro 13** (== estimación), ric 6. El «encabezado de 1.144 chars del
7.6 de ext» de §6.b es tipo `intro` en la salida real y materializa como
`ext::7.6::intro`. 10 mini-chunks de ≤15 chars normalizados (colas de título
envueltas, marcas 'n1') quedan medidos como costo del criterio; sus
extracciones vacías se diagnostican en el censo de E2.

Id: `<to>::<unidad_origen>::<rol>[::<n>]`; sha256 propio del bloque;
provenance (`unidad`) = unidad de origen; herencia del mini = SOLO los tramos
encabezado de su cadena. `conteos.json` suma `mini_chunks` y
`mini_chunks_por_rol`; el censo-oráculo no cambia (mismo inventario x.y).

Reproduce: `python3 correr_e0.py --salida salida_enm01`.
**Selftest ampliado: 57/57 PASS** (los 42 previos + 15 de mini-chunks:
determinismo vía sha de archivos, criterio, ids, herencia de títulos,
interleaving, conteos). `python3 selftest_e0.py`.
