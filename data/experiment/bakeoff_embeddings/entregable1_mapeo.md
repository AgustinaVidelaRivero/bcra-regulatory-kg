# U-A2.0b-bakeoff — Entregable 1: mapeo gold → chunk

Unidad de apoyo al laudo de embeddings. Costo de API: USD 0 (ninguna llamada).
Escrituras: solo en el scratchpad de la sesión. Repo intacto, branch `main`.

## 1. Regla de mapeo (declarada antes de aplicarla)

Texto íntegro en `regla_mapeo_declarada.md`,
sha256 `60cd41a2d605c4148c19601b26ffa17b326026b88035c7a45c84d80306601428`.
Se selló antes de correr el script; el script la lee para hashearla y no la
modifica. Resumen operativo:

- **(a) primaria**: chunks con `to` igual y `unidad` exactamente igual al
  ancla. Incluye los `mini_chunk` (`intro`/`cierre`) de esa misma unidad.
- **(b) descendientes**: SOLO si (a) devuelve 0 chunks — chunks cuya `unidad`
  empieza con `ancla + "."`. Fundamento: el mismo fenómeno que el censo de
  EV2 registró como granularidad de ancla
  (`data/experiment/ev2_corrida/censo/ausencias_diagnostico.json`: "crudo=0 y
  desc>0 => el punto existe solo como sub-puntos").
- Gold del par = unión sobre sus anclas. Gold del caso = gold del par (las
  dos variantes comparten gold). 100 casos = 50 pares × 2 variantes.
- **Ambiguo** = caso mapeado con |gold| > 10. El corte 10 se toma de la regla
  sellada del censo de EV2 ("contenedores >10 anclas excluidos"). Marca, no
  excluye.

Dos hechos estructurales que la regla contempla y conviene tener presentes:
`unidad` no es clave única (1.703 unidades para 1.763 chunks: 58 unidades con
2 chunks, 1 con 3), por lo que el mapeo es ancla → CONJUNTO; y existen
unidades no numéricas (`S2`…`S15`, secciones sin puntos) que ningún ancla del
gold alcanza.

Reproduce todo lo que sigue:

```
python3 mapeo_gold_chunk.py
```

## 2. Conteos

Universo: 1.763 chunks E0 (cap 462, cla 143, ext 973, pro 101, ric 84);
50 pares, 53 anclas (47 pares con 1 ancla, 3 con 2), 37 anclas distintas.

| conteo | casos (de 100) | pares (de 50) |
|---|---|---|
| mapean a ≥1 chunk bajo **(a) sola** | **78** | 39 |
| mapean a ≥1 chunk bajo **(a)+(b)** | **100** | 50 |
| no mapean bajo (a)+(b) | **0** | 0 |
| ambiguos (|gold| > 10) | **18** | 9 |
| parcialmente resueltos (1 de 2 anclas) | **0** | 0 |

Anclas distintas: 28 resueltas por (a), 9 por (b), 0 sin resolver.

Distribución de |gold| por par bajo (a)+(b):

| |gold| | 1 | 2 | 4 | 7 | 8 | 16 | 17 | 18 | 19 | 25 | 27 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| pares | 34 | 3 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 4 |

Anclas que entraron por (b), con su fan-out: `ext:3.11` 16, `ext:10.4` 27
(en 4 pares), `cap:2.6` 7, `cap:2.11` 8, `ext:7.8` 18 (en 2 pares),
`ext:14.5` 4, `cap:5.2` 16, `ext:10.6` 8, `ext:10.2` 25.

**El umbral del mandato se supera: 100 ≥ 80.**

## 3. Ambigüedad: qué la produce

Los 18 casos ambiguos (9 pares) son todos casos de vía (b): el ancla es un
punto contenedor sin chunk propio y su contenido se reparte entre 16 y 27
descendientes. Ejemplos: `ext:10.4` (27 chunks, 4 pares), `ext:10.2` (25),
`ext:7.8` (18). En estos casos recall@k responde "¿cayó algún chunk del
bloque?" y no "¿recuperó el pasaje que contiene la respuesta?": con 27 chunks
gold sobre 1.763 pasajes, recall@10 es una prueba considerablemente más
blanda que con 1 chunk gold. No se excluyen — se reportan marcados, y en el
entregable 3 la métrica debería reportarse también restringida al subconjunto
no ambiguo.

## 4. Tres ejemplos completos (gold → chunk_id → primeras líneas)

Salida íntegra en `ejemplos_mapeo.txt`. Resumen:

**ED-002 — vía (a) sobre `punto_terminal`, caso limpio.**
Literal: "¿Cómo se clasifica, dentro de las operaciones cambiarias, la
financiación de importaciones argentinas de servicios?"
Gold `ext:13.6` → `ext::13.6` (`punto_terminal`, 1.917 chars, p.174):
"13.6. Líneas de crédito de entidades financieras aplicadas a la financiación
de importaciones de servicios. / La entidad financiera tendrá acceso al
mercado de cambios…". |gold| = 1.

**EE-017 — vía (b), contenedor sin chunk propio, fan-out 25.**
Literal: "¿Qué debe permitir verificar el sistema SEPAIMPO en relación con
pagos de importaciones efectuados antes del registro de ingreso aduanero de
los bienes?"
Gold `ext:10.2` → 25 chunks, entre ellos `ext::10.2.1.1` ("10.2.1.1. Pagos de
importaciones que cuentan con registro de ingreso aduanero.", 78 chars) y
`ext::10.2.1::cierre` ("En este último caso, los pagos cursados quedarán
sujetos a un seguimiento para verificar que se efectúe el registro de ingreso
aduanero…", 190 chars). |gold| = 25, ambiguo.

**EA-013 — vía (b), fan-out 27.**
Literal: "En el marco de pagos anticipados de importaciones, ¿qué excepción se
aplica al plazo general de 90 días corridos desde el acceso al mercado de
cambios cuando la nacionalización de los bienes requiere un plazo mayor al
normal?"
Gold `ext:10.4` → 27 chunks (`ext::10.4.1.1` … `ext::10.4.5`). |gold| = 27,
ambiguo.

## 5. Hallazgo que motiva el freno (no lo detecta el umbral)

El umbral cuenta cardinalidad, no adecuación. Aplicada la regla, **18 de las
28 anclas de vía (a) resuelven a un único `mini_chunk` de rol `intro`**: el
arranque de prosa del punto contenedor, mientras el contenido sustantivo vive
en descendientes que la cláusula "(b) solo si (a) da 0" excluye por
construcción. Detalle (ancla → chars propios del gold → descendientes
excluidos):

```
ext:4.8     26 chars   19 descendientes excluidos
ext:7.11    27           24
ext:4.6     46           11
ext:3.17    58           23
ext:7.10    76           15
ext:3.15    83            8
ext:2.6     94           10
ext:10.11  304           12
ext:3.5    395           38
ext:11.2   483            9
cap:6.3    630            4
cap:6.10   922            8
cap:8.5    945 (2 chunks) 3
ext:10.5  1067           10
cap:4.2   1160            7
cap:6.2   1177           17
cap:3.1   1392           48
cap:8.6   3295 (2 chunks) 3
```

A nivel par: **26 de 50 tienen un gold compuesto solo por `mini_chunk`**.

Caso testigo, íntegro en `ejemplo_patologia_intro.txt` — **EA-002**:
pregunta literal "Cuando una entidad financiera local otorga una financiación,
¿qué obligación de seguimiento condiciona esa operación hasta su cancelación
total?"; gold `ext:7.10` → `ext::7.10::intro`, cuyo texto propio COMPLETO es
`'del régimen de fomento de inversión para las exportaciones (Decreto
234/21).'`. Los 15 descendientes de 7.10 quedan fuera. Ningún modelo de
embeddings puede recuperar ese fragmento para esa pregunta, y si lo hiciera
no sería por la razón correcta. (Observación adicional, sin adjudicar: en este
par el `location_ejemplo` del gold ya venía mezclado —"Punto 7.10. 9.1.7.
Aportes de inversión extranjera directa…"—; si el ancla misma es adecuada es
material sellado de A1.3 y no lo juzgo acá.)

Consecuencia: con la regla tal como está declarada, hasta 52 de los 100 casos
se medirían contra un gold que no contiene la respuesta. Eso es exactamente
lo que el freno del mandato existe para evitar ("una medición sobre gold mal
mapeado no vale nada"), aunque el criterio numérico del freno no lo capture.

## 6. Las tres variantes, medidas (`variantes_regla.txt`)

| | R1 (declarada) | R2 (exacta + descendientes si no hay `punto_terminal` propio) | R3 (exacta ∪ descendientes siempre) |
|---|---|---|---|
| casos mapeados | 100/100 | 100/100 | 100/100 |
| mediana \|gold\| | 1 | 11 | 11 |
| media \|gold\| | 5,4 | 15,2 | 15,2 |
| máx \|gold\| | 27 | 49 | 49 |
| pares ambiguos (>10) | 9 | 27 | 27 |
| pares con gold solo-`mini_chunk` | 26 | 0 | 0 |

R2 y R3 dan resultados idénticos sobre este material (todo ancla con
`punto_terminal` propio es terminal y no tiene descendientes), así que la
decisión real es R1 vs R2.

El intercambio es explícito y no lo resuelve un criterio técnico neutro:
R1 mantiene el gold chico y exigente (mediana 1) pero con 26 pares cuyo gold
es un fragmento de encabezado; R2 elimina esa patología pero infla el gold
(mediana 11, 27 pares ambiguos) y vuelve el recall@10 considerablemente más
blando. Una tercera opción posible —restringir el bake-off a los pares de
gold unívoco y bien formado— reduce el material y hay que decidir a cuánto.

**No propongo ganador de regla: es laudo de la autora.** Lo que aporto es la
medición de las tres.

## 7. Estado

Entregables 2, 3 y 4 NO iniciados. No se descargó ningún modelo ni se tocó el
caché de HuggingFace. Checkpoint en
`checkpoint_U-A2.0b-bakeoff.md`.
