# Resultado — Piloto de doble adjudicación sin-gold (U6)

Resultado del piloto pre-registrado en `docs/preregistro_piloto_singold_u6.md`
(sellado en commit 3e507c1) y su enmienda 01
(`docs/enmienda_01_preregistro_piloto_singold_u6.md`, commit e55388c).
Corrida: verificador v5.7 congelado, N=1 por caso, 13 casos síntoma-puro de U6,
label `singold_piloto_u6` (db homónima). Medición adjunta N=3 de RT-C6-1:
labels `rt_c6_n3_r{1,2,3}` (dbs homónimas separadas).

## 1. Resultado y rama laudada

El acuerdo quedó muy por debajo del umbral pre-registrado (capa ≥ 11/13):

- **Acuerdo de capa: 4/13** (lectura estricta — todas las primarias del
  verificador del mismo lado que mi primaria; ésta es la lectura oficial, por
  laudo). **6/13** bajo la lectura de sensibilidad que acepta que mi lado esté
  entre los lados de cualquiera de las primarias múltiples del verificador.
- **Acuerdo de causa fina: 4/13** (estricta) y **5/13** (sensibilidad).

**Rama que aplica, laudada: capa < 11/13 → Motor 3 NO validado; adjudicación
manual permanente; el régimen sin-gold queda declarado no validado en este
ciclo.** La rama es la misma bajo todas las lecturas, con la salvedad de la
enmienda 01: un acuerdo bajo admite dos lecturas no separables con n=13
(capacidad diagnóstica del verificador vs. menor contexto de entrada por
n_seen=0; ver §2).

Tabla completa de la corrida (verbatim del reporte de corrida; la adjudicación
humana es la sellada en el §2 del pre-registro, previa a toda corrida):

```
qid | verificador (primarias) | humana prim/sec | capa_estricta | capa_incluye | causa_todas | causa_alguna
U6-005 | navegación | completitud_kg/alcanzabilidad_kg | no | no | no | no
U6-007 | navegación | completitud_kg/alucinacion_agente | no | no | no | no
U6-008 | sin_defecto (sin_par; secundaria provenance_imprecisa) | alcanzabilidad_kg/— | no | no | no | no
U6-009 | navegación | estructural_kg/alcanzabilidad_kg | no | no | no | no
U6-012 | navegación | estructural_kg/navegación | no | no | SÍ | SÍ
U6-014 | completitud_kg | contenido_kg/provenance_imprecisa | SÍ | SÍ | no | no
U6-015 | alucinacion_agente + navegación | completitud_kg/— | no | no | no | no
U6-016 | completitud_kg | completitud_kg/alucinacion_agente | SÍ | SÍ | SÍ | SÍ
U6-018 | completitud_kg | contenido_kg/alucinacion_agente | SÍ | SÍ | no | no
U6-020 | contenido_kg + navegación | contenido_kg/navegación | no | SÍ | SÍ | SÍ
U6-022 | alucinacion_agente + completitud_kg | contenido_kg/alucinacion_agente | no | SÍ | no | SÍ
U6-024 | sin_defecto (sin_par) | completitud_kg/alucinacion_agente | no | no | no | no
U6-025 | completitud_kg | completitud_kg/alucinacion_agente | SÍ | SÍ | SÍ | SÍ

TOTALES: capa estricta 4/13 · capa incluye 6/13 · causa todas 4/13 · causa alguna 5/13
```

El manejo de primarias múltiples no estaba especificado en el pre-registro;
por eso reporto ambas lecturas y laudo la estricta como oficial (mixto cuenta
como desacuerdo). La rama resultante es idéntica bajo ambas.

## 2. Condición de corrida y su mitigación

La corrida operó con `n_seen = 0` (enmienda 01): los nodos vistos por el
agente no eran recuperables íntegros desde la base que consulta el mecanismo
de recuperación, y el verificador partió del fallback del builder sellado
("no se pudieron recuperar los nodos vistos; usá las tools").

La ambigüedad quedó mitigada porque el propio verificador dispone de
`ver_paso_completo` (`verificador.py:142-146`: re-ejecuta determinísticamente
el tool call del paso N de la trayectoria del agente y devuelve el output
íntegro) y de `leer_pasaje_pdf`, y las usó efectivamente en la corrida (§3):
todo lo que el agente vio era recuperable bajo demanda, paso por paso, y la
norma era consultable contra el PDF. La diferencia residual respecto de la
condición de calibración es recuperación bajo demanda vs. contexto servido
de entrada, y la declaro sin cuantificar.

## 3. Evidencia de investigación activa

Los 13 casos tuvieron entre 6 y 19 tool calls del verificador (mediana 12),
con uso de `ver_paso_completo` en 12/13 casos y de `leer_pasaje_pdf` en
13/13: el desacuerdo del §1 no se explica por diagnóstico sin evidencia.

Desglose por caso (del reporte de corrida, verbatim; se reproduce desde las
salidas crudas persistidas bajo el label `singold_piloto_u6`):

```
qid | n_tools | ver_paso_completo | leer_pasaje_pdf | buscar_nodos | ver_nodo | ver_vecinos
U6-005 | 12 | 1 | 2 | 4 | 4 | 1
U6-007 | 14 | 4 | 1 | 6 | 3 | 0
U6-008 | 16 | 2 | 7 | 2 | 3 | 2
U6-009 | 12 | 0 | 4 | 5 | 3 | 0
U6-012 | 19 | 1 | 6 | 7 | 4 | 1
U6-014 | 9 | 2 | 1 | 5 | 1 | 0
U6-015 | 17 | 3 | 5 | 6 | 3 | 0
U6-016 | 7 | 1 | 1 | 4 | 1 | 0
U6-018 | 12 | 3 | 1 | 4 | 3 | 1
U6-020 | 11 | 2 | 4 | 1 | 4 | 0
U6-022 | 12 | 1 | 3 | 4 | 4 | 0
U6-024 | 6 | 3 | 1 | 0 | 2 | 0
U6-025 | 16 | 2 | 6 | 6 | 2 | 0
```

El único caso sin `ver_paso_completo` es U6-009, que compensó con 4 llamadas
a `leer_pasaje_pdf`.

## 4. Naturaleza de la divergencia

El piloto mide acuerdo entre adjudicadores, no verdad causal. Mi adjudicación
separa hechos verificados mecánicamente (existencia/ausencia de nodos y
contenidos, confirmada por desempates determinísticos sobre `kg.json` y
anclas contra el PDF) de la atribución de capa, que es interpretativa.

El patrón dominante de desacuerdo (5/13 casos: U6-005, U6-007, U6-009,
U6-012, U6-015 — los desacuerdos de capa bajo la lectura de sensibilidad
donde el verificador atribuyó navegación y mi primaria es de capa KG) es
KG↔navegación: casos donde ambas descripciones fácticas son simultáneamente
ciertas (el contenido existe en el grafo Y el agente no lo alcanzó) y la
taxonomía v5.7 fuerza la elección de un lado. La frontera entre capas es el
lugar exacto donde dos adjudicadores informados divergen, lo que constituye
un hallazgo sobre la taxonomía, no (solo) sobre el verificador.

Excepción objetiva: los dos `sin_defecto` del verificador (U6-008, U6-024)
recayeron sobre respuestas demostrablemente incorrectas contra la norma
anclada — se registran como observación de calibración, sin cambio en v5.7
(congelada).

Las atribuciones causales quedan como predicciones refutables: la inyección
del backend full-text (issue #5) y la re-extracción (issue #9) funcionarán
como árbitro causal caso por caso — si la intervención predicha por mi
diagnóstico hace pasar el caso, la atribución era correcta.

## 5. Resultado adjunto — N=3 de RT-C6-1

La medición N=3 de RT-C6-1 (issue #2) dio **incorrecta / incorrecta /
incorrecta → veredicto modal: incorrecta (3/3)**. Labels `rt_c6_n3_r1`,
`rt_c6_n3_r2`, `rt_c6_n3_r3`, cada rep en su db separada, con cero
cross-hits de caché (0 hits de agente y 0 de juez en los summaries de las
tres reps). La inversión de generación es sistemática. El evento
correspondiente queda asentado en BKL-0026 (`data/backlog/backlog.jsonl`).

## 6. Consumo

Consumo real de la sesión API: **USD 18,37** (piloto 18,28 + N=3 0,09),
contra una estimación central de USD 20. En tokens: 3.111.580 de entrada
(51,9% del tope laudado de 6M) y 108.814 de salida (54,4% del tope de 200K),
según el log de corrida persistido con el label `singold_piloto_u6`. El
costo de las tres reps N=3 se reproduce de los summaries de los labels
`rt_c6_n3_r{1,2,3}` (0,036217 + 0,034166 + 0,024117 USD).

## 7. Próximo paso pre-declarado

Análisis aparte de los 5 casos con atribución de fuente (U6-001, U6-003,
U6-010, U6-011, U6-019), con la pregunta: ¿el acuerdo mejora cuando el
síntoma insinúa la familia causal? No requiere corrida nueva de agente —
los casos ya tienen traza; requiere solo corrida del verificador sobre esos
5 (decisión de gasto de la autora, ~5/13 del costo del piloto).
