# U-NOSEG-LIMITE — FRENO final (04/10/2026)

Unidad de diagnóstico de solo lectura, en una etapa. Mandato FIRMADO por la autora el 04/10/2026
(`docs/mandatos/UNOSEG_limite_no_segmentables.md`, firma en `966c2bc`, sha256 `5cad985f…`; el texto
del mandato que recibí es idéntico). HEAD al correr: `966c2bc`. Costo de API: USD 0; ninguna llamada a
la API; Neo4j no se usó. Ninguna salida se ejecutó: la decisión es de la autora.

Fuentes firmadas leídas en el commit de su firma (regla k):

| documento | commit | sha256 |
|---|---|---|
| adenda 2 al laudo B5.5 (§1 a §5 y firma) | `1ae387e` | `7baf6ee0fa4c…` (coincide con el mandato) |
| adenda 2, registros §6 y §7 (posteriores a la firma) | `074a712` | — (se citan como registro, no como texto firmado) |
| protocolo entre tandas | `a304b89` | `b23d37c5396a…` |
| L-ESQ-R2 | `4ef7650` | `66c4a1b9c5ed…` |
| adenda 1 al laudo B5.5 (segmentación universal) | `a06cdab` | — (leída por el motivo del §2.2) |

Los artefactos de esta carpeta se regeneran con los scripts de `code/` (comando en el docstring de cada
uno). Las entradas que vienen del scratchpad (roles por página, salida de e0-r2, comparación de R5,
health-check) quedan registradas con su sha256 dentro de cada JSON y van en el paquete de revisión.

---

## L1. El peso completo

Comando: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/no_segmentables_limite/code/l1_peso.py`
(salidas `l1_peso.json` y `l1_peso.md`; fuentes `particion_152.json` `por_to` y `agregados`,
`conteos_b584.json` `roles_pagina`, `inventario_tos.csv`). Denominadores: 152 TOs, 6.757 páginas,
9.324 unidades de la partición; el script los controla contra `agregados`.

| clase | TOs | páginas | % pág. | unidades | % unid. | ficha | cuerpo | historial | índice |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 2 parciales | 2 | 2.413 | 35,7 | 46 | 0,5 | 2.175 | 238 | 0 | 0 |
| 12 no segmentables | 12 | 161 | 2,4 | 12 | 0,1 | 76 | 43 | 38 | 4 |
| los 14 | 14 | 2.574 | 38,1 | 58 | 0,6 | 2.251 | 281 | 38 | 4 |

Por TO (páginas; unidades; roles), de `l1_peso.md`: manual 2.037; 19; ficha 1.830, cuerpo 207 ·
ri2_pm 376; 27; ficha 345, cuerpo 31 · plandecuentas 77; 0; ficha 76, cuerpo 1 · optico 43; 1;
historial 38, índice 4, cuerpo 1 · ri_con 16 · ri_spi 11 · ri_tii 6 · ri_rem 2 · ri_chr, ri_fcem,
ri_itme, ri_pfmipyme, ri_pscpp y ri_pspii 1 cada uno (todas de cuerpo; ri_pspii con 2 unidades, los
demás con 1). Portada y tabla de origen: 0 en los 14. Las cifras del mandato se reproducen.

Páginas `ficha_registro` del universo: 2.281 = 1.830 (manual) + 345 (ri2_pm) + 76 (plandecuentas) +
27 (ri_laft) + 3 (ri_transpa). Dentro de TOs que entran a las tandas: ri_laft 27 y ri_transpa 3.

Volumen en unidades por alternativa (medido o NO MEDIDO):

| alternativa | unidades | fuente |
|---|--:|---|
| parte por punto de los 2 parciales | 42 (e0-r2: 42, mismos ids) | L2, `l2_regla_parciales.json` |
| las 4 unidades que cruzan fichas | 4 (texto propio 291.863 caracteres en e0-r2) | L2 |
| prosa del bloque A (nueve documentos) | 77 | U-COB-A, `chunks_a2.json`, campo `brazo` |
| planilla del bloque A | 114 (declarada y afuera, hacia el bloque B) | U-COB-A, `cifras_vigentes.md` §1 |
| ri_spi por su espina | NO MEDIDO (89 etiquetas terminales de letra y número, cota de lectura; 141 bloques en el censo de A.1) | L2, `censo_forma.json` |
| bloque B (fichas de los 2 parciales) | NO MEDIDO (plan `:730`: «~3.000 unidades» a densidad de prosa, extrapolado) | — |
| optico y plandecuentas | 0 (declarados referencia, adenda 2 §2) | — |
| texto por página al alcance del agente | 0 unidades; 161 páginas (o 2.397 con las de los parciales) | L3 |

---

## L2. Los 2 parciales con su parte por punto, y ri_spi

**Regla**, escrita antes de aplicarla: `l2_regla_parciales.md` (sha256 `14657c94…`, sellado a las
08:13 en el scratchpad, antes de correr `code/l2_parciales.py`). Una unidad es «por punto» si ninguna
página `ficha_registro` cae entre su primera y su última página; si cae alguna, «cruza fichas».
Control previo: los roles por página recomputados con `e0_lib` de HEAD dan 1.830 / 207 y 345 / 31.

**e0-r2 sobre los dos TOs y ri_spi**: `r5_escalera_particion.py --correr --tos manual,ri2_pm,ri_spi`
con el código de HEAD (`git archive 966c2bc`; el código de E0 no cambió desde `e1c9456`), en un espejo
del scratchpad armado copiando archivos (0 enlaces simbólicos) y con los PDF verificados contra
`manifest_pdfs.sha256`. Doble corrida en dos directorios: byte a byte iguales (`diff -rq` vacío).

| fuente | TO | unidades | por punto | páginas | caracteres | cruzan | páginas que listan | caracteres |
|---|---|--:|--:|--:|--:|--:|--:|--:|
| partición | manual | 19 | 17 | 6 | 8.638 | 2 | 202 | 283.502 |
| partición | ri2_pm | 27 | 25 | 10 | 16.931 | 2 | 24 | 19.893 |
| e0-r2 | manual | 19 | 17 | 6 | 8.595 | 2 | 202 | 272.377 |
| e0-r2 | ri2_pm | 27 | 25 | 10 | 16.763 | 2 | 24 | 19.486 |

Se reproduce el 42 / 4 del mandato: 16 páginas y 25.569 caracteres por punto; 226 páginas listadas y
303.395 caracteres en las que cruzan (partición). En e0-r2: 25.358 y 291.863 (pies y K). Las que
cruzan son `manual::2.3.2` (119 fichas dentro de su tramo), `manual::S2::cierre` (1.619),
`ri2_pm::2.2::intro` (18) y `ri2_pm::S5` (239).

Resto de e0-r2 (`l2_regla_parciales.json`, clave `e0r2`): ids iguales a la partición en los tres TOs
(19, 27, 1); sin `sub_chunking.json` ni `ids_desambiguados.json` (ninguna unidad terminal supera el
umbral C8; el cierre de 266.075 caracteres es un mini-chunk y la partición por tamaño no lo toca);
tablas: manual 11 (132 filas), ri2_pm 0, ri_spi 2 (14 filas); encabezados conservados por K: 15, 20 y
5. Diferencias de texto contra la partición, atribuidas con `--atribuir`: K 4, pies 2, pies y K 5,
tablas 1, «otra» 0. Health-check de E0 (`healthcheck_e0.py` en el espejo): manual `cid` (7 líneas,
páginas 7, 8, 9 y 1169), ri2_pm `cid` (27 líneas, página 250), ri_spi `paginas_sin_seccion`; ninguna
de esas páginas está entre las 16 de la parte por punto.

**Hallazgo: la herencia.** Siete de las 42 unidades por punto heredan texto de las que cruzan fichas:
`manual::2.1`, `2.2.1`, `2.2.2` y `2.3.1` llevan en su herencia el cierre de la sección 2 (253.303
caracteres cada una en e0-r2) y `ri2_pm::2.2.1` a `2.2.3` la intro de 2.2 (2.997 cada una); en total
1.022.203 caracteres. E1 imprime toda la herencia en el mensaje (`prompt_e1.py:466-478` en HEAD); E3
solo la de tipo `encabezado` (`comun_e3.py:111-133`).

**Qué exige el camino normal para la parte por punto.**
- Manifiesto: entradas de `manual` y `ri2_pm` con `rol_alcance` coherente con el catálogo (o `null`;
  `manifiesto_corpus.py:165-176`) y `nombres_remision` (`ensamblar_tanda0.py:589`). El manifiesto no
  tiene campo de alcance por unidad: `limitaciones_e0` existe solo con oráculo (`manifiesto_corpus.py:259-268`).
  Declarar «42 de 46» pide un campo nuevo y el filtro en el runner (código), o una salida de E0
  derivada con las 42 unidades (artefacto declarado). En los dos casos hay que recortar o declarar la
  herencia de las siete unidades.
- E1 a E4 y ensamblado: sin cambios de código para unidades por punto. `remite_a`: las menciones
  internas a puntos que viven en las unidades que cruzan quedarían «inexistente en E0» o sin nodos.
- Costo de referencia: 42 × USD 0,0202 ≈ USD 0,85 (`fca019d`, media por unidad del escenario central
  de r2b). Si la herencia no se recorta, E1 recibe además 1.022.203 caracteres: ≈ 303.000 a 337.500
  tokens de entrada (3,03 a 3,37 caracteres por token, `ev2_encadenamiento/estimacion/estimacion_fase_b.md:20`),
  ≈ USD 0,30 a 0,34 a USD 1 por millón (`cobertura_bloque_a/code/correr_a2.py:43`). ESTIMACIÓN NO VERIFICADA.

**Consecuencias.** El TO entra con 16 de sus 2.413 páginas. El grafo no puede declararlo adentro: el
nodo TextoOrdenado no tiene propiedad de alcance y agregarla es cambio de esquema (L-ESQ-R2 no la
prevé); la declaración vive en el manifiesto, el reporte del ensamblado y la tesis. B6.3 (a): extraer
no excluye (protocolo §7, «Efecto sobre el conjunto de evaluación»); los dos ya están entre los 137
(ninguno de los 14 está en `documentos_excluidos_esq.json`, que leí solo por sus ids); una pregunta
sobre las 2.397 páginas restantes no tiene respuesta en el grafo, y cómo lo trata el conjunto de B6.3
no lo leí (material de B6.3, prohibido). Tanda: son regímenes informativos, su fila es la tanda 3
(plan `:772`, que hoy excluye a ri2_pm por parcial); la tanda 1 los deja fuera de sus candidatos
(protocolo §7: «los 147 menos los 14 fuera, 133 TOs»).

**Por qué el protocolo los dejó enteros afuera — motivos escritos.**
- Protocolo §5 (`a304b89`): fila «fuera | 14 | 12 no segmentables y 2 parciales, declarados (`:738`)»,
  sin motivo propio. El protocolo no menciona la adenda 2, B5.9, los bloques A o B ni U-COB-A (grep
  sobre `git show a304b89:docs/protocolo_entre_tandas.md`, vacío).
- Partición (plan `:738`; `adjudicaciones_b584.json`, `d_parser_registro`): el material
  `ficha_registro` queda fuera del parseo de prosa. Es un motivo para las fichas, no para las 42.
- Adenda 1 al laudo B5.5 (`a06cdab`, §2.2): «El bloque RI sigue FUERA de la extracción hasta su ciclo
  propio» (ESQ-RI-1 a 4; ESQ-RI-3 sigue abierta, plan `:695`). Alcanza a los 53 RI, entre ellos los dos
  parciales y once de los doce. Un documento que la levante en forma explícita: NO ENCONTRADO (la
  adenda 2 extrae el bloque A, y la decisión D4 del protocolo crea la tanda 3 sin citarla).
- Diseño B5.9 (`1ae387e`, §0): lista las 46 unidades de los parciales como «(referencia) … 46 (sus
  preámbulos)», sin decidir sobre ellas.
- Un motivo escrito para dejar fuera la parte por punto de los parciales: NO ENCONTRADO.

**ri_spi.** e0-r2 lo deja igual que la partición: modo `sin_raiz`, 0 raíces, 1 chunk de 18.565
caracteres, `paginas_sin_seccion`. Su espina es de letra y número («APARTADO A», «A.1.», «A.1.1.»; 100
etiquetas distintas, 89 terminales, en las 11 páginas), que ninguna etapa de la escalera reconoce
(`correr_e0.py:965-993`: vigente, marcadores y sin raíz, todas por número). No entra por el camino
normal: necesita una regla de marcador de letra en E0, es decir, código de E0 con la guarda 1 de la
adenda 2 (no cambio sobre 1.763 / 762 / 6.340 / 9.266). Esta unidad no puede escribirlo. Pide una
unidad propia chica, de código, antes de la tanda en la que entre (decisión 2: el diagnóstico muestra
que la necesita).

---

## L3. Los 12 no segmentables con su texto al alcance del agente (diseño)

Volumen (`code/l3_volumen.py`, `l3_volumen.json`; tokens y USD son ESTIMACIÓN NO VERIFICADA con 3,03 a
3,37 caracteres por token y USD 1 por millón de entrada):

| conjunto | páginas | caracteres | mediana por página | tokens por página (mediana) | USD por página leída |
|---|--:|--:|--:|--:|--:|
| 12 no segmentables | 161 | 309.820 | 2.083 | 618 a 688 | ≈ 0,0006 a 0,0007 |
| nueve del bloque A | 30 | 35.865 | 1.078 | 320 a 356 | ≈ 0,0003 |
| fichas de los 2 parciales | 2.175 | 1.592.558 | 676 | 201 a 223 | ≈ 0,0002 |
| cuerpo entre fichas | 222 | 302.259 | 1.250 | 371 a 413 | ≈ 0,0004 |

| qué exige | hoy (ancla) | qué haría falta | unidad |
|---|---|---|---|
| texto por página con sha256 desde los PDF congelados | `e0_lib.extraer_lineas` por página; los PDF tienen sha en `escalado_prep/manifest_pdfs.sha256` | un artefacto versionado: texto y sha256 por página, doble corrida byte a byte | U-NAV-DISENO N5 |
| llegar a un documento que el grafo no nombra | KG-Tanda0-Diez-r2a tiene 10 TextoOrdenado; las 30 `remite_a` `to_entero` van a ellos | (i) índice de búsqueda fuera del grafo: `kg.json` no cambia; (ii) un nodo TextoOrdenado por documento: cambia el grafo y resolvería por nombre las citas a esos TOs (hoy 1 de las 189, L4) | N2 decide; recomiendo (i) |
| forma de la cita por página | el agente ve `{source_doc, location}` armado como «Punto X» o «Sección N» (`ev2_corrida/code/comun_ev2.py:134-145`); el harness junta dicts con esas claves (`harness.py:445-452`) | la herramienta devuelve `location: "Página N"` con `source_doc`; así entra a `seen_provenances` sin tocar el harness sellado | N5 |
| métrica de citas | `ucita2_indicadores.py:130-132`: solo «Punto …» o «Sección N» y `TO_…_actual.pdf`; lo demás es «no parseable» | forma «Página N» y existencia contra el número de páginas del PDF; la fidelidad (`_cita_fiel`, `harness.py:361-375`) ya compara la cadena normalizada | N5 |
| juez | `judge.py:163-166`: `cita_precision` ya admite «pagina»; `:180-181`: el juez no evalúa fidelidad de citas | nada | — |
| reporte aparte | no existe una marca de «respondida desde el texto» | una marca por respuesta: alguna cita con «Página N» de un documento sin nodos; tablas de fidelidad con y sin esas respuestas | N4, N6 |
| sistema por fragmentos | el índice vectorial lee los pasajes de E0 de los 5 de desarrollo, con sus páginas (`banco_mcp/mcp_vector/construir_indice.py`) | el mismo texto por página en su índice, o la asimetría declarada (N4: «lo que mejora la búsqueda se aplica igual al sistema por fragmentos») | N2, N7 |

**Si el grafo evaluado queda igual.** Con el índice fuera del grafo (i), `kg.json` no cambia un byte
en ninguna de las salidas 1 y 2 de L5; cambia el sistema evaluado (agente y herramientas), no el grafo.
Con un nodo por documento (ii), cambia.

**Párrafo propuesto para el borrador de U-NAV-DISENO** (texto para la autora; no edité el borrador):
«N2, herramienta 4 (texto fuente con su página): además del texto de la unidad, el texto por página de
los documentos que el grafo no extrae — los 12 no segmentables (161 páginas) y, si la autora lo
decide, las 2.397 páginas de ficha y de cuerpo entre fichas de los 2 parciales —, con su sha256 desde
los PDF congelados, por un índice de búsqueda fuera del grafo y sin nodos nuevos; la salida lleva
`source_doc` y `location: "Página N"`. N5: el artefacto de texto por página y la forma «Página N» en
`ucita2`. N6: la configuración «todas menos el texto por página» mide su aporte, y las respuestas con
alguna cita de página a un documento sin nodos se reportan aparte, como respondidas desde el texto.
N7: el pre-registro declara qué documentos están al alcance solo como texto, con su cifra en páginas,
y si el sistema por fragmentos recibe el mismo texto.»

---

## L4. Qué contienen las páginas excluidas

**Punto de partida (adjudicado).** Adenda 2: lectura a ciegas de 32 páginas, 23 prescriptivas y 9 de
referencia (§1, firmado); bloque A 14 leídas, 10 prescriptivas, una por documento y todas de prosa;
bloque B 18 leídas, 13 prescriptivas (§6, registro). Censo de forma de U-COB-A: 41 páginas de los diez
documentos con prescripción = 17 de prosa, 3 mixtas, 21 de planilla o ficha. U-COB-A: prosa adentro
con residuo declarado, planilla afuera hacia el bloque B, 3 aristas listadas para retiro (plan `:767`).
La lista de las 32 páginas leídas a ciegas: NO ENCONTRADO como archivo rastreado.

**Muestra.** Declarada antes de leer en `l4_declaracion_muestra.md` (sha256 `d39135d4…`, sellado a las
08:17), semilla 20261004, sorteada por `code/l4_muestra.py` (`l4_muestra.json`). Poblaciones: 1.830,
345, 222 (= 238 páginas de cuerpo menos las 16 por punto), 17, 43, 77 y 11; muestra 20, 10, 10, 10, 3,
3 y 3 = 59. Las diez del estrato 4 salieron todas de ri_con (14 de las 17 de la población son suyas).

**Planilla** `l4_planilla.csv` (lectura asistida, `revision_autora` vacía); conteos de `code/l4_conteos.py`:

| estrato | n | tabla de códigos | formulario o planilla | ficha con criterio | prosa normativa | historial o índice | prescribe sí / no |
|---|--:|--:|--:|--:|--:|--:|--:|
| ficha de manual | 20 | 0 | 0 | 20 | 0 | 0 | 13 / 7 |
| ficha de ri2_pm | 10 | 0 | 0 | 10 | 0 | 0 | 2 / 8 |
| cuerpo entre fichas | 10 | 1 | 0 | 9 | 0 | 0 | 9 / 1 |
| planilla de los nueve | 10 | 0 | 10 | 0 | 0 | 0 | 0 / 10 |
| optico | 3 | 0 | 0 | 0 | 0 | 3 | 0 / 3 |
| plandecuentas | 3 | 3 | 0 | 0 | 0 | 0 | 0 / 3 |
| ri_spi | 3 | 0 | 1 | 0 | 2 | 0 | 3 / 0 |
| total | 59 | 4 | 11 | 39 | 2 | 3 | 27 / 32 |

Lo que la muestra dice, en fracciones crudas: las páginas «de cuerpo entre fichas» son fichas con otro
formato en nueve de diez (la décima es una línea del plan de cuentas), así que las 4 unidades que
cruzan son material del bloque B y no prosa del cuerpo. En la ficha, «prescribe» es en general una
instrucción de imputación o valuación («se imputarán», «deberá constituirse»), no una obligación
sustantiva hacia el cliente. Las páginas de manual leídas llevan versiones de 1981 a 2008 y el título
del inventario es «RI - Manual de Cuentas vigente al 31/12/17»: si el documento rige hoy, NO VERIFICADO.
La planilla de ri_con no manda nada en las diez páginas leídas; ri_spi sí, en las tres.

**Preguntas** (`l4_preguntas_candidatas.json`, búsqueda en `l4_preguntas.json` sobre 143 TOs: 138
reconocidos plenos y 5 de desarrollo). 13 candidatas, 10 conservadas, 3 descartadas (Q05: la misma regla
está en prevmi y cajasc; Q12 y Q13, de forma). Conservadas: tres de ri_spi p. 3 (plazo de 5 días
hábiles para entregar la base de datos de seguimiento; periodicidad diaria; no rectificación), dos de
ri2_pm (valuación del platino, p. 166; títulos en garantía del BCRA, p. 88) y cinco de manual (p. 1893,
1874, 918, 694 y 1552), estas cinco con el aviso de vigencia de arriba. No son material de evaluación.

**Citas a los 14 desde las normas extraídas** (`code/l4_citas_189.py`, `l4_citas_189.md`). El 189 del
reporte de KG-Tanda0-Diez-r2a son pares únicos (chunk, evidencia): el registro tiene 195 filas con
esa causa, 6 repetidas. Por clase: 175 a otros TOs de los 152, 2 con el nombre deformado por la
extracción (cap y supcon), 8 anáforas («dicho ordenamiento»), 3 fuera de los 157 y **1 a uno de los
14**: optico, desde `docvig::3.6.1` («Sección 8. de las normas sobre “Presentación de informaciones
al Banco Central”»), y optico solo trae índice e historial, no el texto de esa sección. Desglose
por norma: 73 nombres distintos, en el `.md`. Complemento léxico (`code/l4_menciones_14.py`): en el
E0 de los diez TOs, «central de cheques rechazados» en 7 chunks de ctacte y el sistema SEPAIMPO en 5
de ext; nombran la central y el sistema, no los regímenes ri_chr y ri_spi.

---

## L5. Cómo y cuándo se cumple la adenda 2 en la release r2

**a. La parte por punto de los 2 parciales.** Recomiendo que entre por el camino normal con la tanda 3
(regímenes informativos), con el alcance declarado (42 de 46 unidades, 16 de 2.413 páginas) y la
herencia de las siete unidades recortada o declarada. Costo ≈ USD 0,85 (más ≈ 0,30 a 0,34 si la
herencia viaja; ESTIMACIÓN NO VERIFICADA). Exige un filtro de alcance (campo nuevo del manifiesto o
salida de E0 derivada) y una nota fechada al protocolo §5. Queda pendiente, como para toda la tanda 3,
el motivo de la adenda 1 §2.2.

**b. Las 4 unidades que cruzan fichas.** Van con el bloque B: por la muestra son fichas. El bloque B
pasa a declararse con 2.397 páginas (2.175 de ficha más 222 de cuerpo entre fichas), más la planilla
de los nueve que U-COB-A ya mandó ahí (114 unidades, 17 páginas).

**c. El bloque A con procedencia por página** (nueve documentos, 77 unidades de prosa, 13 páginas).
Lo que exige en la cadena (leído en HEAD, sin editar; verificado por mí sobre lo que mapeó un agente
de solo lectura):
1. E0: no hay vía de páginas (`correr_e0.py:965-993`; los ids y `paginas` salen del árbol de puntos,
   `e0_lib.py:1734-1740`). Hace falta una etapa o un emisor que produzca `chunks_<to>.json` y
   `estructura_<to>.json` por TO, con `chars_propio` y `sha256_*` (las 191 de `chunks_a2.json` no
   los tienen y son un solo archivo).
2. E1 con el prefijo de la release (r2b) y E3: el prompt imprime «Tipo de unidad: chunk de punto» y
   «Punto del chunk: p1.b0» (`prompt_e1.py:456-457`); U-COB-A corrió así y el literal no explicó el
   resultado (mensaje del commit `074a712`, punto (5), hipótesis (iii-b)). No hace falta cambiar el
   prefijo. Hay
   que re-extraer: el crudo de U-COB-A es del perfil `v3_b54`, no de la release. Costo ESTIMACIÓN NO
   VERIFICADA: USD 0,30 (por unidad de U-COB-A, solo E1) a 1,56 (77 × 0,0202, E1 y E3).
3. Procedencia: hoy `{to, archivo, punto, rol_documental}` con rol `punto_propio`
   (`validador_e1.py:228-233`, `pyd_r2/code/validador_r2.py:705-707`, `comun_e1.py:93-98`); hay que
   agregar `granularidad_procedencia` y la página. `Provenance` admite claves extra
   (`modelos_r2.py:407-412`; el mandato dice 405 a 410).
4. Ensamblado: toma las páginas del chunk si está en la salida de E0 (`ensamblar_tanda0.py:757-797`).
5. `remite_a`: `r1_referencias.unidades_e0` exige `estructura_<to>.json` (`r1_referencias.py:119-125`);
   una cita a «punto X» desde una unidad de página queda irresoluble (`:1054-1056`, `:1069`).
6. Validador, suite y shapes: S4 exige las cuatro claves sin formato (`shapes_validator.py:180`,
   `:373-396`), pasa; S31 lee `chunks_<to>.json` (`:1343-1392`); la suite (`regression_kg.py`) no tiene
   tests de unidades de página: hacen falta, entre ellos el retiro de las 3 aristas (plan `:767`).
7. Citas: «Punto p1.b0» no es parseable para `ucita2` (`:130-132`); hace falta la forma de página.
8. Guardas de la adenda 2: guarda 1 (no cambio) para el código de E0; guarda 3, el conteo «N de M»:
   en unidades, 77 de 9.391 (9.324 − 10 unidades degeneradas de los nueve + 77) si solo entra el
   bloque A; en elementos, NO MEDIDO.

**¿Antes del escalado o con la tanda 3?** Recomiendo con la tanda 3. Razones: el prefijo no cambia,
así que la regla de la ventana (plan `:741`) admite el cambio como release de código entre tandas (si
la procedencia nueva cuenta como «formato de salida de E1» lo decide la autora: el modelo no la
emite, la arma el validador en código, `validador_e1.py:228-233`); los
nueve son regímenes informativos como el resto de la tanda 3; el costo es chico en cualquier fecha; y
lo que sí cuesta es código (E0, procedencia, citas, tests) que antes de la tanda 1 entra en la ruta
crítica de U-REEXT-T0. Exige enmendar la adenda 2 §4, que dice «Bloque A antes del escalado»: cambia
una decisión firmada, no basta una nota. El §6 desacopla el calendario del bloque B, no el del A. Si la
autora prefiere cumplir el §4 tal como está, el bloque A tiene que entrar en el grafo de la tanda 1 con
la release r2 (el gate de la tanda 1 ya lo supone, plan `:767`), y las piezas 1 a 7 van antes.

**d. El bloque B, release posterior declarada** (adenda 2 §4): 2.397 páginas (2.175 de ficha + 222 de
cuerpo entre fichas) más la planilla de los nueve, con U-COB-B y sus guardas 4 a 6. Mientras tanto, su
texto puede quedar al alcance del agente por L3. Recomiendo decidirlo dentro de U-NAV-DISENO (N2 y
N6) y no por esta unidad.

**ri_spi**: por su espina, no por página (adenda 2 §7), con la unidad propia de código de E0 de L2,
antes de la tanda 3.

### Comparación de las salidas

| salida | costo | qué cambia de la cadena | grafo evaluado | antes de la tanda 1 | cifra que declara la tesis | adenda 2 (§2, §4) / protocolo (§5) |
|---|---|---|---|---|---|---|
| 1. exclusión total de los 14 | USD 0 | nada | no cambia | sí | 14 de 152 TOs fuera: 2.574 de 6.757 páginas, 58 de 9.324 unidades; prescripción en diez de los doce y en 13 de 18 fichas | contradice §2 y §4: exige enmienda a la adenda 2 con su motivo; el protocolo queda como está; el gate de `:767` y U-COB-A quedan sin destino (nota al plan) |
| 2. exclusión con la parte por punto adentro | ≈ USD 0,85 (+ 0,30 a 0,34 si viaja la herencia) | filtro de alcance; herencia de siete unidades | cambia: 2 TOs, 42 unidades | no, salvo nota al protocolo §5 y §7 | 2.558 páginas fuera (12 TOs enteros + 2.397 de los parciales) | sigue contradiciendo §2 y §4 por el bloque A: enmienda; protocolo §5: nota fechada |
| 3. la 1 o la 2 con el texto al alcance | USD 0 de extracción; herramienta en U-NAV-DISENO N5 (USD 0) y su medición en N6 | ninguna de extracción; herramienta nueva, `ucita2`, marca de respuesta, índice de fragmentos | `kg.json` igual con índice fuera del grafo; cambia el sistema evaluado | no (U-NAV-DISENO parte 2 es posterior a la tanda 1) | la de la 1 o la 2, más: «el texto de N páginas está al alcance del agente, sin nodos» | texto al alcance no es extracción: igual exige la enmienda de la 1 o la 2; protocolo: nota |
| 4a. prosa del bloque A antes del escalado | USD 0,30 a 1,56 (ESTIMACIÓN) + código | piezas 1 a 7 de L5 c | cambia: 9 TOs, 77 unidades de página | sí, si el código llega antes | 77 de 9.391 unidades con procedencia de página; planilla y bloque B declarados | cumple §2 y §4 para A; B queda como release posterior (§4); protocolo §5: nota fechada |
| 4b. prosa del bloque A con la tanda 3 | igual que 4a | igual que 4a, como release entre tandas | cambia, en la tanda 3 | no | igual que 4a | cumple §2; §4 pide enmienda de calendario; protocolo §5: nota fechada |

**Recomendación.** La salida 4b junto con (a), (b) y (d): parte por punto de los parciales y prosa del
bloque A con la tanda 3, ri_spi por su espina con una unidad propia antes de esa tanda, las cuatro
unidades que cruzan y la planilla con el bloque B, y el texto por página como decisión de U-NAV-DISENO.
Pide una enmienda a la adenda 2 §4 (calendario del bloque A) y una nota fechada al protocolo §5.
Queda abierta, para toda la tanda 3, la relación con la adenda 1 §2.2.

---

## Hallazgos para la autora

1. La herencia de la sección 2 de manual (253.303 caracteres por unidad) viajaría a E1 en cuatro
   unidades por punto (L2).
2. Las 4 unidades que cruzan fichas son fichas: el bloque B real tiene 2.397 páginas, no 2.175 (L4).
3. La adenda 1 §2.2 (`a06cdab`) deja fuera de la extracción a todo el bloque RI. No encontré un
   documento que la levante; la tanda 3 de D4 no la cita (L2).
4. El protocolo firmado no menciona la adenda 2 (L2).
5. De las 189 citas irresolubles, una apunta a los 14 (optico) (L4).
6. ri_spi necesita código de E0 propio; e0-r2 no lo segmenta (L2).
7. Vigencia de manual: el inventario lo titula «vigente al 31/12/17»; NO VERIFICADO si rige (L4).
8. Discrepancias menores con el mandato: `Provenance` está en las líneas 407 a 412, no 405 a 410;
   el 189 son pares únicos de 195 filas.

## Control

- Repo: sha256 de todos los archivos (sin `.git` ni `.venv`) antes (21.477, 08:08) y después
  (21.506). Además de los 25 archivos nuevos de esta carpeta, cambiaron archivos que no escribí: a las
  08:09 y 08:12, `docs/plan_tesis.md` y `docs/checklist_pre_escalado.md` (registran esta unidad como
  firmada y despachada y dan de alta U-DIAG-VINCULO), `docs/mandatos/UDIAG_vinculo.md` y
  `reports/u_diag_vinculo/` (nuevos); a las 08:40, el commit `92dc684` (U-R2-CODIGO-2 C1) con
  `data/experiment/r2_codigo2/`, que solo agrega esa carpeta y no cambia su contenido respecto de la
  línea de base; y tres `.DS_Store`. Ninguno toca E0, la partición, el ensamblado, los scripts ni las
  fuentes firmadas que usé; en el plan, la línea `:728` solo cambió el estado de este mandato.
- Ningún `.pyc` nuevo (línea de base de 2.424 entradas, igual al cierre).
- Los scripts de esta carpeta corridos dos veces seguidas dan salidas byte a byte iguales: 12 salidas
  generadas; la comparación cubrió los 17 archivos fuera de `code/`, entre ellos los 5 que no genera
  ningún script (este freno, la regla de L2, la declaración de L4, la planilla y las candidatas).
- Lecturas fuera de lo pedido: `documentos_excluidos_esq.json`, solo los ids, para el 137 → 123.
