# Reporte consolidado de EV2 — fidelidad, navegabilidad, censo, juez y costos (U-A0 / A0.1)

Unidad U-A0 (plan de tesis §4, unidad 1; sub-tarea A0.1). Generado sobre HEAD
`237fb8f887b754a48e9882d48b37705e44f9f9e2` (A0.1 y A0.2 fase A) y completado
sobre HEAD `40603a99caf5842a2a994e0e1ae7376214e5a596` (A0.2 fase B, §12);
working tree limpio salvo esta unidad y el archivo previo no rastreado
`adjudicar.py`, ajeno a ella. USD 0: ninguna llamada a API.
Cero commits (los hace la autora).

**Todo número de este documento sale de un archivo commiteado y se recomputa
con un solo comando** (salida `salida/recomputo_ev2.json`, con la ruta del
insumo en cada bloque, y `salida/tablas_ev2.md` con las tablas largas):

```
python3 -B data/experiment/ev2_reporte/code/recomputo_ev2.py
```

El script verifica antes de computar los sha256 de los insumos que las
unidades previas ya sellaron (agregados base `9f1046c6…`, tabla opaca base
`e219b2fb…`, finales §7 `0c82e47a…`, agregados §7 `e7c8b5e1…`, tabla opaca §7
`629c4fb8…`, gold `1d587336…`, prompt del juez `fd446f8e…`) y el cuarteto
`data/experiment/evaluacion/{loader,harness,judge,llm_cache}.py` (4/4).
Corrida repetida ⇒ salida byte-idéntica (salvo `generado`; verificado).

**Nomenclatura canónica** (`docs/nomenclatura_grafos.md`, commit `237fb8f`):
**KG-Base (`12c226e2`)** = `run_3` (`data/experiment/run_3_ppf_core/kg.json`,
baseline congelado, Gen. 1); **KG-Refinado (`26fac8b4`)** = `v3`
(`data/experiment/grafo_v2/reensamblado_v3/kg.json`, vigente, Gen. 2 + C1–C7);
**KG-Reextraído (`8e2eadee`)** = `v2` (`data/experiment/reextraccion_v2/corpus_v2/salida/kg.json`,
Gen. 3, Enmienda 01). Las claves internas de los archivos EV2 (`run_3`/`v3`/`v2`,
labels `ev2_base_run3`/`ev2_base_v3`/`ev2_base_v2`) se citan solo entre
paréntesis o en comandos.

Cadena de commits que este reporte consolida: sello del set `9c44516` →
corrida del agente `bb89a8e` → pre-registro del método `be8a84f` →
navegabilidad `5b02d22` (+ fix `2c84069`) → criterios U6 `2ac2fab` →
calibración del juez `1a0ac5c` → fidelidad base `b624865` → encadenamiento §7
`9044a04` → worksheet ciego `03ebe83` → adjudicación y cierre `64de678` →
nomenclatura `237fb8f`.

---

## 1. Qué mide EV2 (una página)

- **Pregunta**: si la re-extracción con el pipeline v2 (KG-Reextraído) mejora
  la fidelidad y la navegabilidad respecto del vigente (KG-Refinado) y del
  baseline congelado (KG-Base), sobre un set sellado ANTES de toda corrida y
  con la única variable = el grafo (issue #10; `docs/diseno_ev2.md`;
  `docs/protocolo_corrida_ev2.md`).
- **Dos ejes ortogonales, sin mezcla.** *Fidelidad*: 40 preguntas generadas a
  ciegas contra los PDFs (territorio virgen, dosificación ext 16 / cap 8 /
  cla 6 / ric 5 / pro 5), gold = ancla normativa exacta + 164 criterios con
  cita verbatim (`data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json`).
  *Navegabilidad*: 64 samples aptos del pipeline de queries sintéticas, cada
  uno con par literal / anti-léxica (128 corridas por grafo antes de descontar
  ausencias), gold por anclas de provenance con resolución por grafo y censo
  previo (`data/experiment/exploracion/sinteticas/out/preguntas_faseB.json`).
- **Régimen** (protocolo §3, pre-declarado): N=1 base para todo; en fidelidad
  re-corrida N=3 del agente SI Y SOLO SI el veredicto base es `parcial`
  (mayoría; empate triple → parcial) + auditoría simétrica N=3 sobre el 10 %
  de los `correcto` (semilla `auditoria-ev2-v1`; con 3/4/2 correctos el 10 %
  redondea a 0 → laudo mínimo 1 por grafo). Orden `orden-ev2-v1`; anti-cache
  por label + db por repetición (0 cross-hits verificados en cada corrida).
- **Método de fidelidad** (`docs/preregistro_evaluacion_fidelidad_ev2.md`,
  `be8a84f`, sellado después de la corrida del agente y antes de leer respuesta
  alguna): juez `claude-sonnet-4-6` v1 congelado (prompt sha256 `fd446f8e…`),
  unidad = par (respuesta, criterio) ∈ {cumplido, no_cumplido, dudoso}, N=3
  modal, mapping en código (todos cumplido → correcto; cero → incorrecto;
  mezcla → parcial; dudoso/sin_consenso → requiere_adjudicacion), ceguera de
  grafo (ids opacos `EV2R-`/`EV2E-`, orden `juez-ev2-v1`), adjudicación humana
  de todo `requiere_adjudicacion` + muestra simétrica 10 %/10 % por grafo
  (semilla `adjudicacion-ev2-v1`), contra PDF y gold, con worksheet ciego
  sellado antes de adjudicar (`03ebe83`).
- **Agente**: Haiku 4.5, temperatura 0, 3 tools (`buscar_nodos` /
  `ver_nodo` / `ver_vecinos`), máximo 15 tool calls; cuarteto congelado de
  `data/experiment/evaluacion/`.

## 2. Tabla definitiva de fidelidad por grafo (40 preguntas por grafo)

Fuente: `data/experiment/ev2_adjudicacion/adjudicacion/veredictos_definitivos_ciego.json`
cruzado con `data/experiment/ev2_fidelidad_eval/desanonimizacion/tabla_id_opaco.json`
(recómputo `salida/recomputo_ev2.json` → `fidelidad.definitiva_por_grafo`;
coincide 12/12 celdas con el cruce sellado
`data/experiment/ev2_adjudicacion/adjudicacion_SOLO_MESA/cruce_definitivo_por_grafo_SOLO_MESA.json`,
campo `definitiva_coincide_con_cruce_sellado: true`).

| Grafo | correcto | parcial | incorrecto | req. adj. |
|---|---|---|---|---|
| KG-Base (`12c226e2`) | 3 | 20 | 17 | 0 |
| KG-Refinado (`26fac8b4`) | 5 | 26 | 9 | 0 |
| KG-Reextraído (`8e2eadee`) | 4 | 27 | 9 | 0 |

**Vías por las que se llegó a cada veredicto definitivo** (mismo archivo,
`fidelidad.vias_por_grafo`; `juez_base` = veredicto del juez sobre la
respuesta base sin re-corrida; `adjudicacion_base` = heredado
`requiere_adjudicacion` de la base, adjudicado sobre la respuesta base;
`juez_enc` = agregado por par de las 3 re-corridas §7 decidido por el juez;
`adjudicacion_s7` = par de re-corridas con votos pendientes, resuelto por
adjudicación):

| Grafo | juez_base | adjudicacion_base | juez_enc | adjudicacion_s7 | total |
|---|---|---|---|---|---|
| KG-Base | 15 | 6 | 17 | 2 | 40 |
| KG-Refinado | 9 | 8 | 19 | 4 | 40 |
| KG-Reextraído | 9 | 7 | 21 | 3 | 40 |

Vía × veredicto (120 pares, `fidelidad.via_x_veredicto`): juez_base
{correcto 6, incorrecto 27}; adjudicacion_base {correcto 2, parcial 18,
incorrecto 1}; juez_enc {correcto 3, parcial 50, incorrecto 4};
adjudicacion_s7 {correcto 1, parcial 5, incorrecto 3}. Los 21 heredados se
resolvieron 2/18/1 y los 9 pendientes §7, 1/5/3.

**Las tres etapas de la misma tabla** (para trazabilidad; `fidelidad.base_ciega_por_grafo`
y `fidelidad.pre_adjudicacion_por_grafo`; coinciden con los cruces de mesa
declarados en `b624865` y `9044a04`):

| Grafo | base ciega (c/p/i/adj) | pre-adjudicación (post §7) | definitiva |
|---|---|---|---|
| KG-Base | 2 / 18 / 14 / 6 | 2 / 13 / 17 / 8 | 3 / 20 / 17 / 0 |
| KG-Refinado | 4 / 22 / 6 / 8 | 4 / 17 / 7 / 12 | 5 / 26 / 9 / 0 |
| KG-Reextraído | 3 / 23 / 7 / 7 | 3 / 20 / 7 / 10 | 4 / 27 / 9 / 0 |

Encadenamiento §7 que produce la columna del medio
(`data/experiment/ev2_encadenamiento/reporte/veredictos_finales_ciego.json`):
63 pares disparados por base `parcial` (KG-Base 18 / KG-Refinado 22 /
KG-Reextraído 23) + 3 de auditoría = 66 pares × 3 = 198 re-corridas; por
respuesta nueva parcial 148 / correcto 12 / incorrecto 14 /
requiere_adjudicacion 24; por par disparado parcial 49 / incorrecto 4 /
correcto 1 / requiere_adjudicacion 9 (vías: unánime 40, mayoría 2 de 3 7,
invariante con pendiente 7, pendiente 9); auditoría: 2 sin flip / 1 flip
descendente (tasa 1/3; re-corridas individuales no-correcto 3/9).

**Perfil por pregunta** (`fidelidad.perfiles_por_pregunta`, orden KG-Base /
KG-Refinado / KG-Reextraído): parcial/parcial/parcial 16;
incorrecto/incorrecto/incorrecto 7; incorrecto/parcial/parcial 6;
incorrecto/correcto/parcial 2; parcial/parcial/incorrecto 2; y 7 perfiles
con 1 pregunta cada uno (tabla T2 de `salida/tablas_ev2.md`). En 24 de 40
preguntas los tres grafos coinciden (16 + 7 + 1 correcto/correcto/correcto); en 9 el baseline es el único incorrecto.

**Definitivo × clasificación auxiliar del juez sobre la respuesta base**
(`fidelidad.auxiliar_base_x_definitivo_por_grafo`; abstención = la respuesta
declara no encontrar información; pre-registro §1, columna que no entra al
veredicto):

| Grafo | abstenciones (base) | abstención→incorrecto | contenido→incorrecto | contenido→parcial | contenido→correcto |
|---|---|---|---|---|---|
| KG-Base | 9 | 9 | 8 | 20 | 3 |
| KG-Refinado | 4 | 4 | 5 | 26 | 5 |
| KG-Reextraído | 7 | 6 (+1 →parcial por adjudicación) | 3 | 26 | 4 |

Toda abstención salvo una terminó `incorrecto`; el resto de los incorrectos
son respuestas con contenido — 8 en KG-Base, 5 en KG-Refinado, 3 en
KG-Reextraído (grounded ≠ correct: la respuesta cita el grafo y aun así
incumple todos los criterios). Por TO (`fidelidad.definitivo_por_to_y_grafo`,
tabla en el JSON): en `ext` (16 preguntas) KG-Base 0/8/8 contra 1/11/4 en los
dos refinados; en `ric` (5) KG-Base 3/1/1 es el mejor de los tres.

## 3. Cobertura por criterios (recomputada desde los veredictos definitivos)

Comando (misma corrida): `python3 -B data/experiment/ev2_reporte/code/recomputo_ev2.py`
→ `salida/recomputo_ev2.json` → `criterios.por_grafo` (por par en
`criterios.por_par` y tabla T3 de `salida/tablas_ev2.md`).

Regla declarada por esta unidad (no existe en archivos previos): la cobertura
de un par se cuenta sobre su **respuesta representativa** — la base (modales
del juez, o marcas humanas de la ficha si fue adjudicada) para las vías
`juez_base`/`adjudicacion_base`; para `juez_enc`/`adjudicacion_s7`, la
re-corrida de MENOR rep cuyo veredicto coincide con el definitivo del par
(la misma regla con la que el worksheet eligió qué respuesta llevar a la ficha,
`ev2_adjudicacion/checkpoint_sesion.md` decisión 2), con sus modales del juez
o sus marcas humanas según corresponda. El recómputo verifica que las marcas
son consistentes con el mapping §2 en los 120 pares
(`criterios.inconsistencias_con_mapping: []`).

| Grafo | criterios | cumplidos | no cumplidos | cobertura |
|---|---|---|---|---|
| KG-Base | 164 | 56 | 108 | 0,3415 |
| KG-Refinado | 164 | 73 | 91 | 0,4451 |
| KG-Reextraído | 164 | 70 | 94 | 0,4268 |

Cumplidos por vía (`criterios.por_grafo.*.cobertura_por_via`): KG-Base
juez_base 5/58, adjudicacion_base 13/26, juez_enc 35/72, adjudicacion_s7
3/8; KG-Refinado 11/34, 19/34, 39/82, 4/14; KG-Reextraído 4/33, 11/30, 49/88,
6/13. Lectura: la brecha KG-Base vs refinados en cobertura (0,34 vs 0,43–0,45)
es del mismo signo y magnitud relativa que la de incorrectos (17 vs 9); entre
KG-Refinado y KG-Reextraído la diferencia es de 3 criterios sobre 164.

## 4. Navegabilidad literal / anti-léxica (denominadores por grafo)

Fuente: `data/experiment/ev2_corrida/navegabilidad/agregados_navegabilidad.json`
(reporte de la unidad: `reporte_navegabilidad.md`, commit `5b02d22`; replay
determinístico 336/336 trazas sin divergencias, estándar y fuerte; USD 0).
Recall micro = anclas vistas|consultadas / anclas de la celda; brecha v-s-c =
anclas vistas en un `buscar_nodos` y jamás consultadas. **Denominadores
distintos por grafo** = casos presentes según el censo (§5): KG-Base 60,
KG-Refinado 64, KG-Reextraído 44 casos por variante; **los grafos no se
promedian entre sí ni se comparan sobre el mismo denominador**.

| Grafo | variante | n casos | n anclas | vistas | consultadas | brecha v-s-c | recall vista micro | recall consultada micro | recall consultada macro |
|---|---|---|---|---|---|---|---|---|---|
| KG-Base | literal | 60 | 67 | 61 | 48 | 13 | 0.9104 | 0.7164 | 0.7267 |
| KG-Base | anti-léxica | 60 | 67 | 53 | 33 | 20 | 0.7910 | 0.4925 | 0.5250 |
| KG-Refinado | literal | 64 | 71 | 71 | 68 | 3 | 1.0000 | 0.9577 | 0.9609 |
| KG-Refinado | anti-léxica | 64 | 71 | 60 | 44 | 17 | 0.8451 | 0.6197 | 0.6016 |
| KG-Reextraído | literal | 44 | 48 | 29 | 19 | 10 | 0.6042 | 0.3958 | 0.4205 |
| KG-Reextraído | anti-léxica | 44 | 48 | 22 | 13 | 9 | 0.4583 | 0.2708 | 0.2955 |

Brecha literal − anti-léxica (mismo denominador dentro de cada grafo;
`navegabilidad.por_grafo.*.brecha_literal_menos_antilexica`): recall
consultada micro KG-Base 0.2239, KG-Refinado 0.3380, KG-Reextraído 0.1250.
Cohortes etiquetadas y jamás promediadas (`cohorte_nucleo_limpio_EE` /
`cohorte_dirigida_EA_ED`): en el núcleo limpio E-E, recall consultada micro
literal/anti-léxica KG-Base 0.80/0.60 (10 casos), KG-Refinado 1.00/0.36 (11),
KG-Reextraído 0.57/0.29 (7 presentes de 11 aptos).

**Salvedad (a) — KG-Refinado juega de local.** Los 64 samples del eje
sintético se muestrearon del propio KG-Refinado (`samples.json`: "contra el
v3 vigente (sha 26fac8b4…)", `data/experiment/exploracion/ev2_sellado/manifest_ev2.txt`;
`docs/diseno_queries_sinteticas.md`): sus anclas gold provienen de nodos de
ese grafo, por lo que su presencia 64/64 y buena parte de su recall literal
(1.0000 vista) son en parte por construcción, y la variante anti-léxica se
diseñó contra el léxico de SUS nodos. La comparación de navegabilidad entre
grafos hereda ese sesgo a favor de KG-Refinado; la comparación válida dentro
de cada grafo es literal vs anti-léxica (que es el número central de la
unidad y se confirma en los tres).

## 5. Censo de presencia y diagnóstico de ausencias

Fuente: `data/experiment/ev2_corrida/censo/censo_resumen.json` y
`censo/ausencias_diagnostico.json` (commit `bb89a8e`; regla sellada
`resolucion.AnclaIndex`: match exacto de punto, sin descendientes,
contenedores > 10 anclas excluidos). 64 casos por grafo; ausencia = ninguna
ancla del caso resuelve; se excluye de navegabilidad y se reporta como dato de
fidelidad (protocolo §2).

| Grafo | presentes | completos | parciales | ausentes | contenedores excluidos | provenances sin parsear |
|---|---|---|---|---|---|---|
| KG-Base | 60 | 60 | 0 | 4 | 0 | 0 |
| KG-Refinado | 64 | 64 | 0 | 0 | 20 | 1 |
| KG-Reextraído | 44 | 42 | 2 | 20 | 18 | 0 |

Diagnóstico de las anclas no resueltas (`navegabilidad.ausencias.*.diagnostico`
del recómputo; detalle por ancla en tabla T4 de `salida/tablas_ev2.md`;
nota del archivo: crudo=0 y desc>0 ⇒ el punto existe solo como sub-puntos;
crudo=0 y desc=0 ⇒ el punto no está en el grafo en ninguna forma):

- **KG-Base**: 4 anclas no resueltas (EC-014 `cap:6.8`, ED-007 `cla:9.1`,
  ED-017, EE-003), las **4 con crudo=0 y desc=0** — ausencia total del
  contenido.
- **KG-Refinado**: 0.
- **KG-Reextraído**: 23 anclas no resueltas (20 casos ausentes + 3 anclas de
  2 casos parciales: EA-005 `ext:3.13`/`ext:4.6`, EA-016 `cap:2.6`). **15 con
  crudo=0 y desc>0** — el punto intermedio no existe como nodo propio pero sus
  sub-puntos sí (p. ej. `cap:2.6` con 31 descendientes); 6 con crudo≥1 y
  desc>0 y 2 con crudo≥1 y desc=0 (el único portador del ancla no resuelve
  bajo la regla, lo que por definición del censo solo ocurre si es un
  contenedor > 10 anclas — lectura de la regla, no un campo del archivo);
  **ninguna ausencia total**.

**Salvedad (d) — 15/23 de las ausencias de KG-Reextraído son granularidad de
ancla**, no falta de contenido: la extracción por bloques de la Enmienda 01
materializa los sub-puntos y deja sin nodo propio a puntos contenedores que el
gold usa como ancla exacta (`docs/nomenclatura_grafos.md` §3.b; trade-off
granularidad de puntos intermedios vs completitud estructural, 6.178/11.415
nodos/aristas contra 4.469/8.073). Con la regla sellada del censo esas 15
cuentan como ausencia (y los casos salen del denominador de navegabilidad de
KG-Reextraído: 44 en vez de 64); con `incluir_descendientes=True` resolverían.
La regla no se cambió: la ausencia se reporta con este diagnóstico al lado.

## 6. Validación del juez

**Calibración** (`data/experiment/ev2_juez/calibracion/registro_calibracion.md`
+ `out_app/acuerdo_juez_humana.json`, commit `1a0ac5c`; fuente exclusiva:
las 25 preguntas U6 adjudicadas humanamente, respuestas de la sesión de la app
que la adjudicación usó; material EV2 no abierto): por pregunta **14 acuerdos
+ 6 desacuerdos + 5 requiere_adjudicacion (14/20 sobre las decididas)**;
matriz humano→juez correcto→{correcto 1, parcial 5, req.adj. 1},
parcial→{parcial 10, incorrecto 1, req.adj. 4}, incorrecto→incorrecto 3
(**3/3 incorrectas detectadas**); por criterio, humana incorrecta → 13/13
no_cumplido, humana correcta → 11/21 cumplido; no-determinismo 87/92 pares
unánimes, 0 sin_consenso. Los 6 desacuerdos son de etiqueta (5/6 de vara:
criterio no preguntado o cláusula de cierre; declarados y no corregidos; no
aplicables a EV2, donde vara y gold coinciden por construcción). Iteración
v1.1 (un calibrador contra la fuga de gold de U6-001 c3) DESCARTADA por
aceptación pre-declarada no cumplida (3/91 pares cambian modal). Prompt v1
congelado `fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455`.
Limitaciones documentadas: fuga de gold al fragmento (benigna: siempre
`dudoso` → adjudicación), rigor formal en fronteras de equivalencia,
consistencia interna no medida, brecha de vara U6.

**Muestra simétrica §6 sobre EV2** (`data/experiment/ev2_adjudicacion/adjudicacion/reporte_muestra_simetrica.json`,
commit `64de678`; 12 fichas = 1 correcto + 3 parcial/incorrecto por grafo,
semilla `adjudicacion-ev2-v1`, adjudicadas a ciegas): **acuerdo exacto 11/12**;
dirección A (juez correcto / humana no) **0/3**; dirección B (juez
parcial-incorrecto / humana correcto) **1/9**; desacuerdo de grado
parcial↔incorrecto 0; **acuerdo por criterio 52/53 (98,1 %)**. Por grafo
(`cruce_definitivo_por_grafo_SOLO_MESA.json` → `cruce_muestra_por_grafo`):
KG-Base 3/4, KG-Refinado 4/4, KG-Reextraído 4/4. La muestra mide la tasa de
error del juez y NO reemplaza su veredicto en esos pares (laudo). El único
desacuerdo (ADJ-182df261: juez parcial, humana correcto, 4/5 criterios) es
sub-acreditación: el sentido del error del instrumento es hacia el rigor.

**No-determinismo en EV2** (recómputo `juez.no_determinismo_*` sobre los
agregados): base 483/492 pares unánimes, 0 sin_consenso, 22 modales dudoso;
§7 820/831 unánimes, 0 sin_consenso, 26 dudoso. Los 37 criterios que el juez
dejó dudosos y llegaron a ficha se resolvieron 20 cumplido / 17 no_cumplido
(`veredictos_definitivos_ciego.json` → `resueltos_dudosos`). Auditoría
mecánica de fragmentos: base 1.476 fragmentos = 673 null / 792 verbatim /
0 fuga_gold / 11 no_verbatim (concatenaciones de piezas presentes);
§7 2.493 fragmentos = 933 null / 1.516 verbatim / 0 fuga_gold / 44 no_verbatim
(`reporte_ciego.md`, `reporte_final_ciego.md`).

## 7. Salvedades obligatorias

- **(a) KG-Refinado juega de local en navegabilidad** — §4: los pares
  literal/anti-léxica se muestrearon de KG-Refinado; presencia 64/64 y recall
  literal 1.0 son en parte por construcción; comparación válida = literal vs
  anti-léxica dentro de cada grafo.
- **(b) Sello `9c44516` posterior al grafo `5273c0c`.** El commit de sellado
  del set (eje de fidelidad + protocolo + manifest) es del 2026-08-13 18:33
  y el grafo KG-Reextraído final del 2026-08-12 12:22 (`git log --format='%h %ad' --date=iso`).
  Argumento de aislamiento del registro de generación
  (`data/experiment/exploracion/ev2_fidelidad/registro_generacion_ev2_fidelidad.md`
  §1, fecha de generación 2026-08-10, sha256 `d62673b0…` en el manifest): la
  instancia generadora leyó EXCLUSIVAMENTE los 5 PDFs, el mapa de territorio
  quemado (solo anclas), el protocolo U6, el diseño EV2 y `validar_anclas.py`;
  "no se abrió kg.json, nada bajo sinteticas/, posthoc_run/, el backlog, ni
  ningún eval set previo. La generación no vio ningún output del pipeline v2".
  Las tres piezas del eje sintético ya estaban commiteadas el 2026-08-10
  (`5ceb816`, antes del grafo). El sello llegó tarde por no haber salido el
  commit único al cierre de los issues #3/#4 (nota del propio commit:
  "sello efectivo 2026-08-13 … ninguna corrida ejecutada antes de este sello,
  pre-registro válido"), y la primera corrida es `bb89a8e` (2026-08-14). El
  set no pudo mirar el grafo; el retraso es de registro, no de aislamiento.
- **(c) N=3 del agente solo para parciales — sesgo alcista igual para los
  tres grafos.** Protocolo §3: re-correr solo los no-correctos "solo puede
  subir el nivel absoluto"; al ser la regla idéntica para los tres, la
  comparación queda limpia y el nivel absoluto se reporta con esta salvedad.
  La auditoría simétrica midió el sesgo contrario: flip descendente 1/3 de
  los correctos re-corridos (3 pares, mínimo 1 por grafo por laudo). Efecto
  observado del encadenamiento sobre la tabla (§2): pasa 63 parciales base a
  49 parcial / 4 incorrecto / 1 correcto / 9 a adjudicación — la re-corrida
  bajó más de lo que subió, y los incorrectos de KG-Base pasaron de 14 a 17.
- **(d) Ausencias de KG-Reextraído: 15/23 son granularidad de ancla** — §5.

## 8. Desvíos declarados del período (todos registrados en archivos)

1. `9c44516`: sello efectivo 2026-08-13, posterior al grafo (salvedad b).
2. `bb89a8e`: recuperación de 5 casos de KG-Reextraído por corte de red
   (misma db, replay bajo `/bin/zsh`, N=1 efectivo; `resumen_ev2_base_v2.json`
   muestra 1.005 hits de caché de esa recuperación); EA-013::literal en
   KG-Base con error 400 permanente del harness congelado (traza completa de
   5 steps, métrica computable; ratificado). Censo previo con 20/0/4 ausencias.
3. `5b02d22`: corrige la transcripción de las ausencias de KG-Base del reporte
   de fase A (censo commiteado como fuente); `2c84069` retira symlinks con
   rutas locales del repo (desvío de convención del commit anterior).
4. `2ac2fab`/`1a0ac5c`: la pasada 1 de calibración juzgó las trazas B2 y no
   las respuestas adjudicadas (4/25 idénticas) — error de fuente detectado,
   pasada conservada y rotulada NO VÁLIDA (`ev2_juez/out/NOTA_fuente_respuestas_pasada1.md`),
   gasto contado; iteración v1.1 descartada por aceptación no cumplida
   (candado de ajuste). Gasto total de la calibración USD 3,18.
5. `b624865`: commit tardío respecto del cierre de la unidad, detectado por la
   unidad §7 (que trabajó sobre los archivos en disco sellados por sha en
   `ev2_encadenamiento/sellos/sellos_inicio_faseA.txt`; ninguna corrida
   dependió del contenido sin sellar). 11 fragmentos no_verbatim del juez
   (concatenaciones), 0 fugas de gold.
6. `9044a04`: auditoría 10 % redondea a 0 con 3/4/2 correctos → laudo mínimo
   1 por grafo; regla de agregación con votos `requiere_adjudicacion`
   (decidido solo si invariante) declarada por la unidad y ratificada por
   laudo; el juez tuvo 60 hits intra-db esperados por textos idénticos entre
   re-corridas (534 llamadas pagadas de 594).
7. `03ebe83`: los votos ADJ pendientes eran 17, no 24 como decía el mandato
   (7 viven en pares invariantes); fichas compartidas por textos idénticos
   (17 votos → 15 fichas); muestra §6 no reemplaza veredictos; heredado
   adjudicado no dispara re-corridas §3.
8. `237fb8f`: colisión de alias "v2" (grafo del escalón 1 vs KG-Reextraído)
   resuelta por nomenclatura canónica; ningún archivo estaba mal, leídos en
   secuencia inducían a error.

## 9. Costos del período EV2 (archivo exacto por línea)

Fuente de cada línea: `salida/recomputo_ev2.json` → `costos.lineas`
(archivo y campo citados por fila). Las pasadas inválida y descartada de la
calibración cuentan como gasto real.

| Unidad | Componente | USD | Archivo (campo) |
|---|---|---|---|
| ev2_corrida (agente base N=1) | `ev2_base_v2` (128 casos) | 4,1971 | `ev2_corrida/trazas/ev2_base_v2/resumen_ev2_base_v2.json` (`costo_usd`) |
| ev2_corrida | `ev2_base_v3` (168 casos) | 5,0955 | `…/ev2_base_v3/resumen_ev2_base_v3.json` (`costo_usd`) |
| ev2_corrida | `ev2_base_run3` (160 casos) | 5,5886 | `…/ev2_base_run3/resumen_ev2_base_run3.json` (`costo_usd`) |
| ev2_juez (calibración) | pasada 1 sobre trazas B2 — NO VÁLIDA | 1,0262 | `ev2_juez/out/resumen_corrida.json` (`gasto_real.usd`) |
| ev2_juez | pasada válida v1 (fuente app) | 1,0101 | `ev2_juez/out_app/resumen_corrida.json` |
| ev2_juez | iteración v1.1 — DESCARTADA | 1,1461 | `ev2_juez/out_app_v11/resumen_corrida.json` |
| ev2_fidelidad_eval | juez v1 N=3, 360 llamadas | 4,3405 | `ev2_fidelidad_eval/out/resumen_corrida.json` (`gasto_real.usd`) |
| ev2_encadenamiento | agente, 198 re-corridas | 6,4732 | `ev2_encadenamiento/reporte/resumen_agente.json` (`gasto_dbs.total.usd`) |
| ev2_encadenamiento | juez v1 N=3, 594 llamadas (534 pagadas) | 6,7441 | `ev2_encadenamiento/juez_out/resumen_corrida_juez.json` (`gasto_real.usd`) |
| navegabilidad, adjudicación, esta unidad | offline | 0 | — |
| **Total EV2** | | **35,62** | suma de `costos.lineas` |

Fuera del total, por ser unidades previas al sello: queries sintéticas fase B
USD 2,20 (commit `5ceb816`), generación ciega del eje de fidelidad (sin costo
de API en el repo), re-extracción del grafo USD 32,97 (commit `5273c0c`).
Los USD 14,88 de la corrida del agente coinciden con el "gasto real desde
dbs" del commit `bb89a8e` (tope 18,50).

## 10. Lectura consolidada (hallazgos, cada uno con su número)

1. **El baseline casi duplica los incorrectos de cualquiera de los dos
   refinados** (17 vs 9 y 9; §2) y tiene la menor cobertura de criterios
   (0,34 vs 0,45 / 0,43; §3). Su desventaja se concentra en `ext` (0/8/8
   contra 1/11/4) y en las abstenciones (9 de sus 17 incorrectos son
   respuestas que declaran no encontrar la información; §2), consistente
   con sus 4 ausencias totales de contenido en el censo (§5) y su recall
   consultada intermedio (§4).
2. **KG-Refinado y KG-Reextraído están en empate técnico en fidelidad**:
   5/26/9 vs 4/27/9, cobertura 73 vs 70 criterios sobre 164, misma cantidad de
   incorrectos (9-9) con composición distinta (KG-Refinado 4 abstenciones +
   5 con contenido; KG-Reextraído 6 abstenciones + 3 con contenido). La
   atribución determinística por traza (§12, H1) muestra que esos 9-9 son
   perfiles distintos: navegación con ancla presente en KG-Refinado,
   granularidad de ancla + generación en KG-Reextraído.
3. **La brecha literal vs anti-léxica se confirma en los tres grafos** (recall
   consultada micro cae 0.22 / 0.34 / 0.13; §4): la navegación depende del
   léxico de la pregunta; KG-Refinado, con presencia total, es el que más
   pierde en anti-léxica en el núcleo limpio (1.00 → 0.36).
4. **KG-Reextraído gana completitud estructural y pierde granularidad de
   ancla** (§5, salvedad d): 20 casos ausentes bajo la regla del censo, 15/23
   anclas por granularidad, 0 ausencias totales; sobre sus 44 presentes su
   recall consultada es el más bajo (0.40 literal). Con la salvedad (a), la
   navegabilidad no permite ordenar KG-Reextraído contra KG-Refinado; la
   fidelidad, sí, y da empate.
5. **El instrumento se sostiene**: juez v1 congelado, 3/3 incorrectas
   detectadas en calibración, 11/12 de acuerdo exacto y 52/53 por criterio en
   la muestra simétrica ciega de EV2, 0 sobre-acreditación, sub-acreditación
   1/9, 0 fugas de gold en 3.969 fragmentos auditados de EV2 (1.476 base +
   2.493 en §7),
   483/492 y 820/831 pares unánimes (§6). El nivel absoluto es conservador
   (el error del juez va hacia el rigor) y comparable entre grafos.
6. **Todo el período costó USD 35,62** (§9), 0 cross-hits de caché en todas
   las corridas con repeticiones, replay 336/336 en navegabilidad.

## 11. Propuesta de texto de cierre del issue #10 (lo cierra la autora)

> **Cerrado.** EV2 corrió sobre los tres grafos con el mismo set sellado
> (`9c44516`) y los mismos protocolos; la única variable fue el grafo.
> Resultado definitivo de fidelidad (40 preguntas por grafo, juez v1
> congelado N=3 ciego al grafo + adjudicación humana de 48 fichas / 200
> criterios; `64de678`): **KG-Base (`12c226e2`) 3 correctas / 20 parciales /
> 17 incorrectas; KG-Refinado (`26fac8b4`) 5 / 26 / 9; KG-Reextraído
> (`8e2eadee`) 4 / 27 / 9** — el baseline casi duplica los incorrectos de
> cualquiera de los dos refinados; KG-Refinado y KG-Reextraído quedan en
> empate técnico. Cobertura de criterios 56 / 73 / 70 sobre 164. Navegabilidad
> (replay determinístico 336/336, `5b02d22`): la brecha literal vs anti-léxica
> se confirma en los tres grafos (recall consultada micro KG-Base 0.716→0.493,
> KG-Refinado 0.958→0.620, KG-Reextraído 0.396→0.271, sobre 60/64/44 casos
> presentes); censo 60/64/44 presentes con 4/0/20 ausencias (15/23 de las de
> KG-Reextraído por granularidad de ancla, ninguna total). Validación del juez:
> calibración U6 14/20 + 3/3 incorrectas detectadas; muestra simétrica ciega
> 11/12 exacto, 52/53 por criterio, 0 sobre-acreditación. Salvedades:
> KG-Refinado juega de local en navegabilidad; el sello llegó un día después
> del grafo con aislamiento documentado en el registro de generación; N=3 solo
> para parciales (sesgo alcista compartido). Costo del período USD 35,62.
> Reporte consolidado con recómputo: `data/experiment/ev2_reporte/reporte_ev2.md`
> (commits `bb89a8e`, `5b02d22`, `1a0ac5c`, `b624865`, `9044a04`, `03ebe83`,
> `64de678`, `237fb8f`). Atribución determinística de fallas por traza (A0.2,
> regla `40603a9`): los 9-9 incorrectos de los refinados son perfiles distintos
> — KG-Refinado navegación con ancla presente (5/9), KG-Reextraído granularidad
> de ancla (4/9) + generación (3/9); KG-Base navegación (10/17)
> (`data/experiment/ev2_reporte/salida/atribucion_fallas.md`).

## 12. A0.2 — atribución determinística de fallas (Fase B, tras el laudo `40603a9`)

Regla ratificada: `regla_atribucion.md` (sha256 `20040e94…`, commit `40603a9`;
precedencia ausencia_kg → generacion → vista_no_consultada → alcanzabilidad,
veredicto de ESA traza, solo ancla primaria). Salida completa:
`salida/atribucion_fallas.{json,md}` + `salida/atribucion_por_traza.md`
(comando: `.venv/bin/python -B data/experiment/ev2_reporte/code/atribucion_fallas.py --correr --incluir-enc --sensibilidad-descendientes`).
Replay 120/120 (base) y 191/191 (§7) estándar y fuerte OK; sha256 de los tres
grafos verificados; **doble corrida byte-idéntica** salvo `generado` (json, md
y por_traza; sha256 sin `generado` `b2c357cc…` / `561381d7…` / `38b3d2dd…`).
USD 0.

**Clase × grafo, 120 trazas base** (`atribucion_fallas.md` §1.a; veredicto de
esa respuesta = juez base + adjudicación de los 21 heredados):

| Grafo | ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto (no atribuible) |
|---|---|---|---|---|---|
| KG-Base | 6 | 11 | 3 | 17 | 3 |
| KG-Refinado | 4 | 6 | 1 | 25 | 4 |
| KG-Reextraído | 9 | 1 | 5 | 21 | 4 |

**Clase × grafo × veredicto DEFINITIVO** (120 pares, traza representativa del
veredicto — regla ratificada; `atribucion_fallas.md` §3.a), incorrectos /
parciales (ausencia / alcanzabilidad / vista_no_consultada / generacion):
KG-Base 4/8/2/3 y 2/3/0/15; KG-Refinado 2/4/1/2 y 2/3/0/21; KG-Reextraído
4/1/1/3 y 6/0/3/18.

**Criterios no cumplidos × clase** (`atribucion_fallas.md`, tabla de
criterios de §1): la clase generacion tiene la tasa de no cumplidos más baja
en los tres grafos (0,50 / 0,48 / 0,59); ausencia_kg 0,75 / 0,78 / 0,72;
alcanzabilidad 0,88 / 0,76 / 0,75. Columna cruzada abstención (§1.c):
generacion × abstención 1 / 2 / 4.

**Hallazgos** (H1–H7 en `atribucion_fallas.md` §5, cada uno con las tablas
que lo sostienen): **H1** los 9-9 incorrectos de KG-Refinado y KG-Reextraído
esconden perfiles distintos — KG-Refinado falla por navegación con el ancla
presente (4 alcanzabilidad + 1 vista de 9) y KG-Reextraído por granularidad de
ancla (4 ausencia_kg, 3 de ellas con el punto presente solo como sub-puntos) y
generación (3); **H2** KG-Base falla por navegación (10/17 incorrectos) y
tiene 6 anclas de fidelidad totalmente ausentes; **H3** la generación es la
clase dominante de los parciales en los tres grafos (grounded ≠ correct);
**H4** ausencia_kg es ausencia total en KG-Base/KG-Refinado (6/6, 4/4) y
granularidad en KG-Reextraído (8/10 + 2 contenedor; sensibilidad informativa
con descendientes: 9 → 6 generacion + 2 alcanzabilidad + 1 ausencia); **H5**
generacion × abstención = nodo-ancla cáscara (encabezado/puntero) —
limitación declarada de la clase, material del verificador causal; **H6** las
191 re-corridas §7 replican el perfil base; **H7** instrumento verificado.

Adición declarada de la Fase B (a ratificar): el flag
`--sensibilidad-descendientes` (§4.b de `atribucion_fallas.md`) es un análisis
INFORMATIVO fuera de la regla ratificada, sobre las trazas base con clase
ausencia_kg; no reemplaza la clase primaria ni toca `regla_atribucion.md`.

## 13. Reproducción y convenciones

```
python3 -B data/experiment/ev2_reporte/code/recomputo_ev2.py          # todos los números de §2–§6 y §9
.venv/bin/python -B data/experiment/ev2_reporte/code/atribucion_fallas.py --selftest   # A0.2 fase A (24/24)
.venv/bin/python -B data/experiment/ev2_reporte/code/atribucion_fallas.py --correr --incluir-enc --sensibilidad-descendientes   # A0.2 fase B
```

Los shas de los grafos se re-verifican en cada corrida del módulo de
atribución (`comun_ev2.verificar_grafos`) y los de los insumos y el cuarteto
en `comun_reporte.verificar_sellos`. Grep de convenciones (nombres de personas
y referencias a mensajes) al cierre de la unidad: en el reporte de la sesión.
