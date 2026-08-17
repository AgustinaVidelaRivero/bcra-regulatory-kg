# Nomenclatura canónica de los tres grafos de EV2

Este documento fija los nombres con los que la prosa del proyecto (tesis,
informes, guiones, issues futuros) se refiere a los tres grafos medidos en
EV2. Es una capa de nombres SOBRE los artefactos sellados: ningún path, sha
ni commit cambia. Todo número lleva el comando o la ruta que lo reproduce,
corrido desde la raíz del repo; los shas están verificados en esta unidad
contra el working tree Y contra el commit de sellado de cada archivo.

Los nombres canónicos son un laudo de la autora; este documento los registra y
los ancla a los archivos.

---

## 1. Tabla canónica

| Nombre canónico | Alias históricos (repo y conversación) | Path exacto del `kg.json` | sha256 | Commit de sellado | Generación del pipeline |
|---|---|---|---|---|---|
| **KG-Base** | `run_3`, `run_3_ppf_core`, "baseline congelado", "ganador de la Fase 2.3", "PPF-core", `run3` (labels de dbs EV2: `ev2_base_run3`) | `data/experiment/run_3_ppf_core/kg.json` | `12c226e22b8fdc8f46999cae7f1eb808930e71f5dfe803f3a4f637a88348c410` | `58581b6` (2026-05-27, alta del run); seleccionado ganador en la corrida congelada de la Fase 2.3, commit `d56020e` (2026-06-23) | **Gen. 1** — Fase 2.2, estrategia 3 de 5 ("7 entidades core PPF": schema cerrado 7 entidades / 12 relaciones, extracción Haiku 4.5, resolución determinística); código en `data/experiment/run_3_ppf_core/code/{chunker,extract,assemble}.py` |
| **KG-Refinado** | `v3`, `reensamblado_v3`, "v3 vigente", "grafo vigente (de trabajo)", "re-ensamblado v3", "grafo v3" (labels EV2: `ev2_base_v3`) | `data/experiment/grafo_v2/reensamblado_v3/kg.json` — **OJO: vive bajo `grafo_v2/`** (ver §2) | `26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571` | `05984e1` (2026-08-03, C7 — último commit que toca el archivo; sha "post-C7" del tablero §1). Origen del linaje: `7faa03f` (2026-07-30, re-ensamblado v3, 4.458/8.044) + C1–C7 (`af75f70`, `a2e3bb8`, `c51b96a`, `2c71e3f`, `d9e7e9b`, `756d6ec`, `05984e1`) | **Gen. 2** — extracción con esquema v2 (`data/experiment/grafo_v2/code/extract.py`, caché `cache_v2/full`, 508 chunks) + **re-ensamblado** desde ese mismo caché (`assemble_v3.py` + `chunk_roles.py`, cero llamadas a API) + siete correcciones manuales C1–C7 con propuesta sellada y re-test. Pre-Enmienda 01. |
| **KG-Reextraído** | `v2`, `corpus_v2`, "v2-reextraído", "grafo v2 FINAL", "re-extracción v2", "reextraccion_v2" (labels EV2: `ev2_base_v2`) | `data/experiment/reextraccion_v2/corpus_v2/salida/kg.json` | `8e2eadee57b48e00ccb51ade9a953ba1469001fe089c45d97c4307ccf2725581` | `5273c0c` (2026-08-12, "GRAFO v2 FINAL (issue #9)") | **Gen. 3** — pipeline de re-extracción E0–E5 (`data/experiment/reextraccion_v2/{e0_chunking,e1_extractor,e2_reduce,e3_verificador,corpus_v2}/`), diseño `a8fa053` (2026-08-10), **con Enmienda 01** (diseño `baf5608`, implementación `d082812`, ambos 2026-08-11); desde los PDFs, sin heredar C1–C7. |

Verificación de shas (output de esta unidad, working tree):

```
$ shasum -a 256 data/experiment/run_3_ppf_core/kg.json data/experiment/grafo_v2/reensamblado_v3/kg.json data/experiment/reextraccion_v2/corpus_v2/salida/kg.json
12c226e22b8fdc8f46999cae7f1eb808930e71f5dfe803f3a4f637a88348c410  data/experiment/run_3_ppf_core/kg.json
26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571  data/experiment/grafo_v2/reensamblado_v3/kg.json
8e2eadee57b48e00ccb51ade9a953ba1469001fe089c45d97c4307ccf2725581  data/experiment/reextraccion_v2/corpus_v2/salida/kg.json
```

Los mismos tres shas en el commit de sellado de cada archivo (idénticos al
working tree):

```
$ git show 58581b6:data/experiment/run_3_ppf_core/kg.json | shasum -a 256
12c226e22b8fdc8f46999cae7f1eb808930e71f5dfe803f3a4f637a88348c410  -
$ git show 05984e1:data/experiment/grafo_v2/reensamblado_v3/kg.json | shasum -a 256
26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571  -
$ git show 5273c0c:data/experiment/reextraccion_v2/corpus_v2/salida/kg.json | shasum -a 256
8e2eadee57b48e00ccb51ade9a953ba1469001fe089c45d97c4307ccf2725581  -
```

Los tres shas coinciden además con los que EV2 verifica obligatoriamente al
arrancar (`data/experiment/ev2_corrida/code/comun_ev2.py`, dict `GRAFOS`,
líneas 75–90) y con `data/experiment/ev2_corrida/censo/censo_resumen.json`
(clave `kg_sha256` por grafo). Commits por archivo:
`git log --format='%h %ad %s' --date=short -- <path>`.

**Cuarto grafo, fuera de EV2 pero con alias en colisión:**
`data/experiment/grafo_v2/kg.json` (3.872 nodos / 7.231 aristas, sha
`2c7487bb11c8dafee702a27d6558f1dc643f481bb6656ec5e19e3b11f9ae49c1`, commit
`11f0d4a`, 2026-07-26; medición sellada del escalón 1). No participa de EV2 y
NO recibe nombre canónico en esta tabla, pero importa porque en el escalón 1b
y en la pasada 1 intrínseca se lo llamó **"v2"** — el mismo alias que EV2 usa
para KG-Reextraído (§2). Cuando haga falta nombrarlo en prosa: "grafo_v2
(medición sellada del escalón 1, sha `2c7487bb`)".

## 2. Por qué los números confunden

Hay dos contadores independientes que usan la misma letra. El primero numera
el **linaje viejo** nacido de la extracción con esquema v2 (branch
`extraccion-schema-v2`, `data/experiment/grafo_v2/informes/U4_2026-07-18.md`
línea 7; "v2" ahí es el esquema, sucesor del de la Fase 2.2): `v2` es esa
extracción más su ensamblado original (`grafo_v2/kg.json`, commit `11f0d4a`)
y `v3` es el **re-ensamblado** del MISMO caché de extracción con otra lógica
de ensamblado (`reensamblado_v3/`, commit `7faa03f`: "misma extracción,
distinta lógica de ensamblado",
`data/experiment/grafo_v2/informes/reensamblado_v3_2026-07-29.md` §3) — v3
no re-extrajo nada, solo re-ensambló. Por eso KG-Refinado vive bajo
`grafo_v2/`: es hijo del caché de `grafo_v2`, no un directorio hermano. El
segundo contador numera **versiones del pipeline de re-extracción**, y
arranca de nuevo: `docs/diseno_reextraccion_v2.md` llama "chunker v1" (líneas
108 y 118) al chunker de TODO el linaje viejo (el documentado por RX-01 a
RX-08, es decir el que produjo tanto `grafo_v2` como `reensamblado_v3`) y
"re-extracción v2" al pipeline nuevo E0–E5 (commit `a8fa053`) que arranca
desde los PDFs; su producto se llamó `corpus_v2`. Resultado: el grafo MÁS
NUEVO (KG-Reextraído, 2026-08-12) lleva el número MENOR ("v2"), y el más
viejo de los dos refinados (KG-Refinado, 2026-07-30/08-03) lleva el mayor
("v3"); "v3" y "v2" no son términos comparables de una misma serie. Peor
aún, el alias "v2" cambió de referente en el tiempo: en
`docs/protocolo_escalon1b.md` líneas 8–9 y en
`data/experiment/metricas_intrinsecas/pasada1_resumen.md` "v2" es
`grafo_v2/kg.json`; en `data/experiment/ev2_corrida/code/comun_ev2.py` línea
76 y en toda la salida de EV2, "v2" es `corpus_v2/salida/kg.json`. Ningún
documento del repo está mal — cada uno es consistente consigo mismo — pero
leídos en secuencia inducen a error. Esta sección existe para que nadie más
pierda tiempo con esto: en prosa se usan los nombres canónicos de §1 y los
números quedan como alias de los paths.

## 3. Diferencias técnicas (verificadas contra archivos)

### 3.a KG-Refinado vs KG-Reextraído: la Enmienda 01

- **Qué cambia.** La Enmienda 01 al diseño de la re-extracción convierte los
  bloques estructurales que E0 emitía solo como herencia (`chapeau_seccion`,
  `encabezado`, `intro`, `intersticial`, `cierre`) en **unidades de extracción
  de primera clase**: mini-chunks propios con id determinístico, sha propio y
  provenance de su unidad de origen (`docs/enmienda_01_diseno_reextraccion_v2.md`
  §2). Commit del diseño: `baf5608` (2026-08-11); commit de la implementación
  y mini-recalibración: `d082812` (2026-08-11); corpus completo: `5273c0c`
  (2026-08-12). KG-Refinado es anterior a todo esto: su extracción (Gen. 2)
  no tiene bloques estructurales como unidades — la prosa sin numerar
  dependía de que algún chunk hijo la extrajera de paso.
- **Motivación medida** (`docs/enmienda_01_diseno_reextraccion_v2.md` §1): en la
  calibración sobre Protección de Usuarios, 60 de 117 faltantes base
  verificaban SOLO en bloques heredados (51,3 %), y el feedback completo no
  los convertía (cola real 29,9 %). Predicciones y resultado
  (`data/experiment/reextraccion_v2/e3_verificador/salida/faseB_pro_enm01/analisis_enm01.json`):
  P1 confirmada — `faltantes_base_hijos_solo_en_prosa_heredada: 0` (familia
  60→0 por construcción); P2 refutada — `tasa_cola_sobre_verificadas: 0.2178`
  contra predicción `< 0.10`; P3 confirmada — `total_usd: 2.4823` contra
  referencia 2,87. La política de aceptación por severidad + guardia
  estructural (`recompute_politica_laudos.json`) baja la cola derivada a
  `0.0198` (2/101).
- **Conteos de nodos/aristas** (comando:
  `python3 -c "import json; [print(p, len(k['nodes']), len(k['edges'])) for p in ['data/experiment/grafo_v2/reensamblado_v3/kg.json','data/experiment/reextraccion_v2/corpus_v2/salida/kg.json'] for k in [json.load(open(p))]]"`):

  | Grafo | Nodos | Aristas | Tipos de nodo (conteo) | Tipos de relación |
  |---|---|---|---|---|
  | KG-Refinado | 4.469 | 8.073 | Obligacion 1.427, Operacion 1.209, Restriccion 841, Comunicacion 654, Excepcion 252, Sujeto 81, TextoOrdenado 5 | 16 |
  | KG-Reextraído | 6.178 | 11.415 | Obligacion 2.383, Operacion 1.837, Restriccion 1.318, Excepcion 506, Sujeto 93, Comunicacion 35, TextoOrdenado 6 | 11 |

  (Distribuciones por `type` y número de valores distintos de `relation`
  computados con `collections.Counter` sobre `nodes[*].type` y
  `edges[*].relation` de cada archivo; los conteos de KG-Reextraído coinciden
  con `data/experiment/reextraccion_v2/corpus_v2/salida/reporte_ensamblado.json`
  → `nodes_total`, `edges_total`, `nodes_by_type`.) KG-Refinado además porta
  `rol_fuente` por nodo (`{'cuerpo': 3811, 'tabla_norma_origen': 577,
  'esqueleto': 70, 'restauracion_manual': 11}`, tablero §6); KG-Reextraído no
  tiene esa clave.
- **Residuales declarados.**
  - KG-Reextraído: 1.763 unidades E0; **1.683 aceptadas / 80 en cola humana**
    (1.757 verificadas por E3 = 1.678 aceptadas + 79 cola, más 6 de
    re-extracción dirigida = 5 aceptadas + 1 cola;
    `data/experiment/reextraccion_v2/corpus_v2/salida/estado_corpus.json` →
    `fases_cerradas.*:e3.resumen.estados` y `reextraccion_dirigida`);
    **975 residuales declarados** (faltantes de severidad media/baja
    aceptados por unidad: `python3 -c "import json; print(sum(len(json.loads(l).get('residuales',[])) for to in ['pro','cla','ric','cap','ext'] for l in open(f'data/experiment/reextraccion_v2/corpus_v2/salida/{to}/finales.jsonl')))"`
    → `975`; por TO: pro 41, cla 54, ric 89, cap 222, ext 569). Coincide con
    el mensaje del commit `5273c0c`.
  - KG-Refinado: los defectos del backlog RX que el re-ensamblado NO pudo
    mitigar porque quedaron congelados en el texto/`location` con que los
    chunks fueron a la API — RX-02, RX-03, RX-04, RX-05, RX-06, RX-09
    (`docs/tablero.md` §4; `data/experiment/grafo_v2/informes/reensamblado_v3_2026-07-29.md`
    §2); RX-01 y RX-07 mitigados en v3; RX-10 daño por instancia. Más la
    cuarentena de `reensamblado_v3/cuarentena.json` (11 propuestos en el
    re-ensamblado, `assemble_v3_report.json` → `cuarentena.propuestos`; 8
    promovidos por C4). Las 7 correcciones manuales C1–C7 son parches sobre
    este grafo, no sobre su pipeline.

### 3.b El trade-off medido en EV2: granularidad de puntos intermedios vs completitud estructural

Fuente: `data/experiment/ev2_corrida/censo/censo_resumen.json`,
`data/experiment/ev2_corrida/censo/ausencias_diagnostico.json` y
`data/experiment/ev2_corrida/navegabilidad/reporte_navegabilidad.md` (§7–§8).

- **Censo previo del eje sintético (64 casos por grafo, regla sellada: match
  exacto de punto, sin descendientes, contenedores > 10 anclas excluidos):**

  | Grafo | Presentes | Completos | Parciales | Ausentes | Contenedores excluidos |
  |---|---|---|---|---|---|
  | KG-Reextraído | 44 | 42 | 2 | 20 | 18 |
  | KG-Refinado | 64 | 64 | 0 | 0 | 20 |
  | KG-Base | 60 | 60 | 0 | 4 | 0 |

- **Diagnóstico persistido de las ausencias** (`ausencias_diagnostico.json`,
  clave `nota`: "crudo=0 y desc>0 ⇒ el punto existe solo como sub-puntos
  (patrón de extracción por bloques); crudo=0 y desc=0 ⇒ el punto no está en el
  grafo en ninguna forma"). Conteo sobre `grafos.<g>.detalle`:
  - KG-Reextraído: 23 anclas no resueltas (20 casos ausentes + 3 anclas de 2
    casos parciales). De ellas, **15 con crudo=0 y desc>0** — el punto
    intermedio no existe como nodo propio pero sus sub-puntos sí (p. ej.
    `cap:2.6` con 31 descendientes, `cap:8.3` con 101, `ext:7.8` con 55); 6
    con crudo ≥ 1 y desc>0 y 2 con crudo=1 y desc=0 (en estos 8 el único
    nodo que porta el ancla no resolvió bajo la regla, lo que por la
    definición del censo solo ocurre si es un contenedor > 10 anclas —
    lectura mía de la regla, no un campo del archivo). **Ninguna** ausencia
    total (crudo=0 y desc=0).
  - KG-Base: 4 ausencias, las **4 con crudo=0 y desc=0** — el punto no está en
    el grafo en ninguna forma (EC-014, ED-007, ED-017, EE-003).
  - KG-Refinado: 0.
- **Lectura del trade-off.** KG-Reextraído gana completitud estructural (los
  bloques estructurales entran como unidades, 6.178/11.415 contra 4.469/8.073)
  y pierde granularidad de puntos intermedios: la extracción por bloques
  materializa los sub-puntos y deja sin nodo propio a 15 puntos contenedores
  que el gold usa como ancla, lo que el censo registra como ausencia (no como
  falla de navegación: protocolo `docs/protocolo_corrida_ev2.md` §2). KG-Refinado
  conserva los puntos intermedios como nodos (64/64 presentes) pero no tiene
  la prosa estructural sin numerar como unidad extraída (§3.a). Sobre los
  casos presentes de cada grafo, la métrica de navegabilidad literal da recall
  consultada micro **v3 0,9577 (64 casos) / run_3 0,7164 (60) / v2 0,3958
  (44)** y anti-léxica **0,6197 / 0,4925 / 0,2708**
  (`reporte_navegabilidad.md` §4; denominadores distintos por grafo, los
  grafos no se promedian entre sí).

### 3.c KG-Base vs ambos

- **Pipeline.** Gen. 1: estrategia 3 de la Fase 2.2 ("Run 3 — 7 entidades core
  PPF", `data/experiment/run_3_ppf_core/report.md` cabecera y `schema.md` §1):
  schema-based estricto, 7 tipos de entidad (`Obligacion`, `Restriccion`,
  `Excepcion`, `Operacion`, `Comunicacion`, `EntidadFinanciera`,
  `TextoOrdenado`) y 12 tipos de relación, extracción con Haiku 4.5 y
  resolución determinística. Conteos: **4.050 nodos / 6.634 aristas** (mismo
  comando de §3.a sobre `data/experiment/run_3_ppf_core/kg.json`); tipos:
  Obligacion 1.248, Operacion 892, Restriccion 818, Comunicacion 699,
  Excepcion 258, EntidadFinanciera 130, TextoOrdenado 5; 12 relaciones; sin
  `rol_fuente` ni `provenances` (solo `provenance` singular). Es el grafo
  ganador de la corrida congelada de la Fase 2.3 (`data/experiment/evaluacion/frozen_run/`,
  commit `d56020e`) y el baseline congelado que ninguna unidad posterior
  reabre (`docs/tablero.md`; `promocion_v3_2026-07-31.md` §3). En el escalón
  1b (EV1, 36 preguntas, material quemado) dio 31/36 contra 27/36 de
  `grafo_v2` y 29/36 de KG-Refinado
  (`data/experiment/evaluacion_escalon1/corridas/resultados_1b_FINALES_2026-07-31.json`
  → `primaria`).
- **Resultados EV2 definitivos** (commit `64de678`, 2026-08-17; archivo
  `data/experiment/ev2_adjudicacion/adjudicacion_SOLO_MESA/cruce_definitivo_por_grafo_SOLO_MESA.md`;
  40 preguntas de fidelidad por grafo, adjudicación humana cerrada, 0 pares
  pendientes):

  | Grafo | Correcto | Parcial | Incorrecto |
  |---|---|---|---|
  | KG-Base | 3 | 20 | 17 |
  | KG-Reextraído | 4 | 27 | 9 |
  | KG-Refinado | 5 | 26 | 9 |

  Lectura del commit de cierre: el baseline casi duplica los incorrectos de
  cualquiera de los dos refinados; KG-Reextraído y KG-Refinado quedan en
  empate técnico. En navegabilidad (§3.b) KG-Base tiene 4 ausencias totales
  (contenido no presente en ninguna forma) y recall consultada intermedia
  entre los otros dos.

## 4. Regla de uso

1. La prosa del proyecto — tesis, informes, guiones de reunión, issues
   futuros, actas — usa los nombres canónicos **KG-Base**, **KG-Refinado**,
   **KG-Reextraído**. Los alias de §1 se admiten solo entre paréntesis en la
   primera mención o cuando se cita literalmente un archivo, un label de db
   o un mensaje de commit que los usa.
2. Los paths del repo **JAMÁS se renombran**: `run_3_ppf_core/`,
   `grafo_v2/reensamblado_v3/`, `reextraccion_v2/corpus_v2/salida/` y sus
   `kg.json` son zonas selladas (`CLAUDE.md` §3); los shas y commits de §1
   son la identidad de cada grafo y este documento no la altera.
3. Todo documento nuevo que cite un grafo incluye `(nombre canónico, sha
   corto)` en la primera mención: **KG-Base (`12c226e2`)**, **KG-Refinado
   (`26fac8b4`)**, **KG-Reextraído (`8e2eadee`)**. Si en el futuro un grafo
   cambia de sha (p. ej. una corrección con propuesta sellada sobre el
   vigente), el nombre canónico se conserva y el sha corto de la mención lo
   distingue; la tabla de §1 se actualiza por laudo, nunca en silencio.
4. Cuando haya que referirse al cuarto grafo (`grafo_v2/kg.json`, medición
   sellada del escalón 1), se lo nombra por su path y sha corto (`2c7487bb`),
   nunca como "v2" a secas.
