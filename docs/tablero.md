# Tablero de estado — bcra-regulatory-kg

Actualizado al 17 de agosto de 2026 (semana del 10 al 17 de agosto; incluye
los dos commits del 08/08 posteriores al tablero anterior) — se actualiza por
laudo al cierre de cada semana; entre cierres, el estado real es `git log` +
`data/backlog/backlog.jsonl`.

Generado sobre HEAD `85d9fdba70621008e2e7c2f94677891d6250c46d` (working tree
limpio: `git status --porcelain` vacío al momento de generar, con la única
excepción de los tres archivos de esta unidad — este tablero, `docs/INDICE.md`
y `README.md` — y del archivo no rastreado `adjudicar.py`, ajeno a ella).
Todo número de este documento sale de parseo real; la fuente se cita junto a
cada bloque. Desde el tablero anterior (commit `f665d77`, 2026-08-07) hubo
**29** commits (`git rev-list --count f665d77..HEAD`).

Nomenclatura canónica de los grafos (`docs/nomenclatura_grafos.md`, commit
`237fb8f`): **KG-Base (`12c226e2`)**, **KG-Refinado (`26fac8b4`)**,
**KG-Reextraído (`8e2eadee`)**. Los alias históricos (`run_3`, `v3`, `v2`) se
citan solo entre paréntesis o cuando se transcribe un archivo o un commit.

---

## 1. Grafo vigente

- **Nombre canónico:** **KG-Refinado (`26fac8b4`)** — alias `v3`,
  `reensamblado_v3`; Gen. 2 del pipeline (extracción con esquema v2 +
  re-ensamblado + correcciones C1–C7).
- **Ruta:** `data/experiment/grafo_v2/reensamblado_v3/kg.json`.
- **Tamaño:** 4.469 nodos / 8.073 aristas
  (fuente: `python3 -c "import json; kg=json.load(open('data/experiment/grafo_v2/reensamblado_v3/kg.json')); print(len(kg['nodes']), len(kg['edges']))"`).
- **sha256 (post-C7, sin cambios desde el 2026-08-03):**
  `26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571`
  (fuente: `shasum -a 256 data/experiment/grafo_v2/reensamblado_v3/kg.json`;
  coincide con el sha aplicado que cierra
  `data/backlog/retests/C7_retest_2026-08-03.md` y con el que EV2 verifica al
  arrancar, `data/experiment/ev2_corrida/code/comun_ev2.py` dict `GRAFOS`).
- **Registro como vigente:** entrada explícita `GRAFOS_EXPLICITOS` en
  `app/main.py:193` (clave visible `v3_vigente`; promoción 2026-07-31,
  comentario en `app/main.py:186-192`).
- **KG-Reextraído NO fue promovido a vigente:** empató en fidelidad EV2 con
  KG-Refinado (§2) y no pasó por el circuito de promoción; la decisión queda
  para la primera release del pipeline completo (E4/E5, ver §5).
- **Últimas correcciones aplicadas** (fuente: `data/backlog/backlog.jsonl`,
  eventos `aplicacion`/`cambio_estado` con ts 2026-07-31 a 2026-08-03; sin
  correcciones nuevas desde entonces):
  - **BKL-0017** (C1) — restauración del criterio general 1.1 de Clasificación
    de Deudores; estado `verificado`; re-test 4/4 PASS
    (`data/backlog/retests/C1_retest_2026-07-31.md`).
  - **BKL-0006** (C2, opción A) — montos del punto 1.2 de Capitales Mínimos
    corregidos contra la tabla del PDF (bancos 5.000 / restantes 2.500);
    estado `verificado` (`data/backlog/retests/C2_retest_2026-07-31.md`).
  - **BKL-0007** — cerrada por referencia junto con C2; estado `verificado`.
  - **BKL-0023** (C3) — umbral propagado 2.500→5.000; estado `verificado`;
    re-test 4/4 (`data/backlog/retests/C3_retest_2026-08-02.md`); sha256
    posterior del kg `d673dd72…` (registrado en el commit `c51b96a`).
  - **BKL-0019** (C4) — aristas `subclase_de` promovidas desde cuarentena:
    de las 9 con padre sugerido en
    `data/experiment/grafo_v2/reensamblado_v3/cuarentena.json`, entraron
    **8** (bloque contiguo, `rol_fuente: cuarentena_laudada`); la novena
    (`Sujeto_propuesto_originante_acreedor_inicial`, DUDOSA: padre de nivel
    rol fuera del árbol de clases) quedó EXCLUIDA por laudo y DERIVADA a la
    decisión de modelado de BKL-0020 (evento `aplicacion` de BKL-0019 en
    `data/backlog/backlog.jsonl`); estado `verificado`; re-test 5/5
    (`data/backlog/retests/C4_retest_2026-08-02.md`); sha256 posterior del
    kg `0161be69…` (registrado en el commit `2c71e3f`).
  - **BKL-0004** (C5) — enumeración de niveles del 6.5 de Clasificación de
    Deudores restaurada: 9 nodos + 17 aristas (`rol_fuente:
    restauracion_manual`, cambio 100 % aditivo); estado `verificado`; re-test
    determinístico **32/32** (`data/backlog/retests/C5_retest_2026-08-02.md`);
    sha256 posterior `04a50081…`; corrida real RT-C5-1..RT-C5-5 con
    agente+juez: **5/5 correcta** (label `rt_c5_c6`, trazas juzgadas en
    `data/experiment/evaluacion/posthoc_run/traces/rt_c5_c6/`).
  - **BKL-0003** (C6) — salvedad mutuales/cooperativas del 1.1.2.5 de
    Protección de Usuarios: 1 nodo `Excepcion` + 2 aristas (`rol_fuente:
    restauracion_manual`, aditivo); estado `verificado` **en capa KG**;
    re-test determinístico **38/38**
    (`data/backlog/retests/C6_retest_2026-08-03.md`); sha256 posterior
    `fe5f6b69…`; corrida real RT-C6-1..RT-C6-4: **2/4** (incorrecta /
    correcta / parcial / correcta), con laudo de deslinde de capas: la capa
    KG cumplió (nodo presente, rank 1, `ver_nodo` byte-idéntico entre
    trazas); los residuos son de capa agente → altas BKL-0026 (generación) y
    BKL-0027 (navegación).
  - **BKL-0005** (C7) — calificadores del esquema del 7.1 de RegInf
    restaurados: edición de una sola `descripcion` de un solo nodo (cero
    nodos/aristas agregados); estado `verificado`; re-test determinístico
    **27/27** (`data/backlog/retests/C7_retest_2026-08-03.md`); sha256
    posterior `26fac8b4…` (= sha del vigente).
- **Hashes de referencia del `ver_nodo` de C6 (supersesión):** los vigentes,
  sellados en `data/backlog/retests/C6_retest_2026-08-03.md` (laudo de
  deslinde, commit `5b66d8b`), son
  `64bd825978953c4819dfa0850f1ff039d4b9bbbfa18fadfbc055822c6a6ab19e`
  (canónico: `json.dumps(obj, ensure_ascii=False, sort_keys=True)` sobre el
  output parseado) y
  `a5bb2d1fd7fc11eab4f6d23525efea0f3376c8c1981b1be50be268fba82e7667`
  (string crudo del output sin re-serializar), byte-idénticos entre RT-C6-1 y
  RT-C6-2. Cualquier hash de referencia previo citado para ese `ver_nodo` en
  material de sesión no versionado queda superseded: ningún otro hash de
  referencia figura en archivos del repo ni en la historia git (verificado en
  la actualización del 2026-08-07 por grep del prefijo previo y `git log -S`,
  ambos vacíos).

### 1.b Los tres grafos de EV2 (tabla canónica)

Fuente: `docs/nomenclatura_grafos.md` §1 (commit `237fb8f`); conteos por
`python3 -c "import json; kg=json.load(open('<path>')); print(len(kg['nodes']), len(kg['edges']))"`;
shas por `shasum -a 256 <path>` (verificados en esta actualización, idénticos
a los del commit de sellado de cada archivo).

| Nombre canónico | Alias | Path del `kg.json` | sha256 (corto) | Nodos / aristas | Commit de sellado | Generación del pipeline |
|---|---|---|---|---|---|---|
| **KG-Base** | `run_3`, `run_3_ppf_core`, baseline de la Fase 2.3 | `data/experiment/run_3_ppf_core/kg.json` | `12c226e2` | 4.050 / 6.634 | `58581b6` (alta); ganador de la corrida congelada, `d56020e` | Gen. 1 — Fase 2.2, estrategia 3/5 (7 entidades / 12 relaciones), Haiku 4.5 |
| **KG-Refinado** | `v3`, `reensamblado_v3`, vigente | `data/experiment/grafo_v2/reensamblado_v3/kg.json` | `26fac8b4` | 4.469 / 8.073 | `05984e1` (C7; origen `7faa03f` + C1–C7) | Gen. 2 — extracción esquema v2 + re-ensamblado + C1–C7; pre-Enmienda 01 |
| **KG-Reextraído** | `v2`, `corpus_v2`, "grafo v2 FINAL" | `data/experiment/reextraccion_v2/corpus_v2/salida/kg.json` | `8e2eadee` | 6.178 / 11.415 | `5273c0c` (2026-08-12) | Gen. 3 — pipeline E0–E3 con Enmienda 01, desde los PDFs, sin heredar C1–C7; E4/E5 no ejecutados |

Cuarto grafo con alias en colisión (fuera de EV2): `data/experiment/grafo_v2/kg.json`
(medición sellada del escalón 1, sha `2c7487bb`, 3.872 / 7.231) — se lo
nombra siempre por path + sha corto, nunca "v2" a secas (`docs/nomenclatura_grafos.md` §4).

## 2. Baselines y mediciones selladas

### 2.a Escalón 1b (EV1, material QUEMADO) e intrínsecas pasada 1

Fuente: `data/experiment/evaluacion_escalon1/corridas/resultados_1b_FINALES_2026-07-31.json`
(clave `primaria`):

| Grafo | EV1 (36 preguntas) |
|---|---|
| `grafo_v2` (medición sellada del escalón 1, sha `2c7487bb`) | 27/36 |
| KG-Refinado (linaje `reensamblado_v3`, medido en su estado previo a C1–C7; el vigente `26fac8b4` ya incluye las siete) | 29/36 |
| KG-Base (`12c226e2`, referencia) | 31/36 |

- Lectura sellada del 1b: `docs/lectura_escalon1b.md` (commit `e77b11f`). EV1
  quedó QUEMADO por completo (ídem, §5).
- **Pasada 1 intrínseca: HECHA** — descriptiva, sin umbrales, USD 0;
  **P-b (CRUX) CONFIRMADA** (v3 0.637730 > v2 0.600981 en M1)
  (fuente: `data/experiment/metricas_intrinsecas/pasada1_resumen.md`, tabla §1
  y fila P-b). **Umbrales de la pasada 2: PENDIENTES** (otra unidad y otro
  laudo, ídem y `docs/spec_evaluacion_intrinseca.md` §8).
- Nota de comparabilidad: la pasada 1 midió el v3 previo a las correcciones
  C1 a C7 (4.458 nodos / 8.044 aristas, `pasada1_resumen.md`
  cabecera); el vigente ya incluye las siete (4.469 / 8.073, §1).

### 2.b EV2 — CERRADO (commit de cierre `64de678`, 2026-08-17)

EV2 midió los tres grafos de §1.b con el mismo set sellado ANTES de toda
corrida (`9c44516`) y los mismos protocolos: la única variable fue el grafo.
Dos ejes ortogonales: **fidelidad** (40 preguntas generadas a ciegas contra
los PDFs, 164 criterios con cita verbatim, dosificación ext 16 / cap 8 /
cla 6 / ric 5 / pro 5) y **navegabilidad** (64 pares sintéticos literal /
anti-léxica). Reporte consolidado con recómputo determinístico:
`data/experiment/ev2_reporte/reporte_ev2.md` (commits `40603a9` + `85d9fdb`;
todo número se regenera con
`python3 -B data/experiment/ev2_reporte/code/recomputo_ev2.py`).

**Tabla definitiva de fidelidad** (40 preguntas por grafo; juez v1 congelado
N=3 ciego al grafo + adjudicación humana de 48 fichas / 200 criterios sobre
worksheet ciego sellado antes de adjudicar; fuente
`data/experiment/ev2_adjudicacion/adjudicacion_SOLO_MESA/cruce_definitivo_por_grafo_SOLO_MESA.md`
y `reporte_ev2.md` §2):

| Grafo | correcto | parcial | incorrecto | cobertura de criterios (sobre 164) | abstenciones (base) |
|---|---|---|---|---|---|
| KG-Base (`12c226e2`) | 3 | 20 | **17** | 56 (0,34) | 9/40 |
| KG-Refinado (`26fac8b4`) | 5 | 26 | 9 | 73 (0,45) | 4/40 |
| KG-Reextraído (`8e2eadee`) | 4 | 27 | 9 | 70 (0,43) | 7/40 |

Lectura: **ambos grafos del pipeline refinado reducen los incorrectos casi a
la mitad respecto del baseline (9 y 9 contra 17); el esquema v2 es el factor
común.** KG-Refinado y KG-Reextraído quedan en empate técnico (5/26/9 vs
4/27/9; cobertura 73 vs 70 sobre 164). Ningún grafo cubre la mitad de los
criterios que la norma establece. Las tres etapas de la tabla (base ciega →
pre-adjudicación post-§7 → definitiva) están en `reporte_ev2.md` §2.

**Validación del juez** (`reporte_ev2.md` §6): calibración sobre las 25 U6
adjudicadas 14/20 acuerdos + 5 a adjudicación, **3/3 incorrectas
detectadas** (`1a0ac5c`); muestra simétrica ciega de EV2 (12 fichas, 1
correcto + 3 parcial/incorrecto por grafo, semilla `adjudicacion-ev2-v1`):
**acuerdo exacto 11/12, acuerdo por criterio 52/53 (98,1 %)**,
sobre-acreditación 0/3, sub-acreditación 1/9 (el único desacuerdo va hacia
el rigor). 0 fugas de gold en 3.969 fragmentos auditados; 483/492 y 820/831
pares unánimes.

**Navegabilidad** (`data/experiment/ev2_corrida/navegabilidad/reporte_navegabilidad.md`,
commit `5b02d22`; replay determinístico 336/336 sin divergencias, USD 0):
recall consultada micro literal → anti-léxica **KG-Base 0,716 → 0,493
(60 casos presentes) / KG-Refinado 0,958 → 0,620 (64) / KG-Reextraído
0,396 → 0,271 (44)**; la brecha se confirma en los tres grafos y es la
comparación válida (dentro de cada grafo). Salvedad: KG-Refinado juega de
local — los pares se muestrearon de sus nodos. Censo de presencia
(`ev2_corrida/censo/censo_resumen.json`): 60/64/44 presentes, 4/0/20
ausencias; 15/23 anclas no resueltas de KG-Reextraído son granularidad de
ancla (el punto existe solo como sub-puntos), ninguna ausencia total; las 4
de KG-Base son ausencia total.

**Commits de cada etapa:** sello del set `9c44516` (2026-08-13) → corrida
del agente N=1 `bb89a8e` (456 trazas, USD 14,88) → pre-registro del método
de fidelidad `be8a84f` → navegabilidad `5b02d22` (+ fix `2c84069`) →
criterios de calibración U6 `2ac2fab` → calibración del juez `1a0ac5c` →
fidelidad base `b624865` (USD 4,34) → encadenamiento §7 `9044a04` (198
re-corridas + juez, USD 6,47 + 6,74) → worksheet ciego `03ebe83` →
adjudicación y cierre `64de678` → nomenclatura `237fb8f` → reporte
consolidado + regla de atribución `40603a9` → atribución de fallas
`85d9fdb`. **Costo total del período EV2: USD 35,62** (`reporte_ev2.md` §9,
archivo por línea).

**Mapa causal de fallas (U-A0 / A0.2, determinístico, USD 0; fuente
`data/experiment/ev2_reporte/salida/atribucion_fallas.md`, regla sellada
PRE-cómputo `data/experiment/ev2_reporte/regla_atribucion.md` en `40603a9`,
salida en `85d9fdb`; replay 120/120 base + 191/191 §7, doble corrida
byte-idéntica).** Cuatro clases con precedencia ausencia_kg → alcanzabilidad
→ vista_no_consultada → generacion, veredicto por traza de esa misma
respuesta, abstención como columna cruzada. Clase × grafo sobre las 120
trazas base (`atribucion_fallas.md` §1.a):

| Grafo | ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto |
|---|---|---|---|---|---|
| KG-Base | 6 | 11 | 3 | **17** | 3 |
| KG-Refinado | 4 | 6 | 1 | **25** | 4 |
| KG-Reextraído | 9 | 1 | 5 | **21** | 4 |

Hallazgos H1–H7 (`atribucion_fallas.md` §5): **H1** el empate 9-9 esconde
perfiles de falla distintos — KG-Refinado falla por navegación con el ancla
presente (5/9 de sus incorrectos definitivos: 4 alcanzabilidad + 1 vista),
KG-Reextraído por granularidad de ancla (4/9 ausencia_kg, 3 de ellas con el
contenido presente solo en sub-puntos) más generación (3/9); **H2** KG-Base
falla por navegación (10/17) y tiene 6 anclas de fidelidad totalmente
ausentes; **H3** la generación es la clase modal en los tres grafos (17 / 25
/ 21) — grounded ≠ correct cuantificado; **H4** ausencia_kg es ausencia total
en KG-Base/KG-Refinado (6/6, 4/4) y granularidad en KG-Reextraído (8/10 +
2 contenedor; sensibilidad informativa con descendientes: 9 → 6 generacion +
2 alcanzabilidad + 1 ausencia); **H5** generación × abstención = nodo-ancla
cáscara (encabezado o puntero sin el contenido pedido), limitación declarada
de la clase, material del sub-diagnóstico A0.3; **H6** las 191 re-corridas
§7 replican el perfil base; **H7** instrumento verificado. **Techo de
retrieval dimensionado** (alcanzabilidad + vista_no_consultada, trazas base):
**14 / 7 / 6**.

**Estado del juez de fidelidad EV2:** prompt **v1 congelado**
(`data/experiment/ev2_juez/prompt_juez_v1.md`, sha256
`fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455`), mapping
en código (`ev2_juez/mapping.py`, tests 20/20), calibración CERRADA en
`1a0ac5c` (iteración v1.1 descartada por aceptación pre-declarada no
cumplida — candado de ajuste). Cuatro limitaciones documentadas en
`data/experiment/ev2_juez/calibracion/registro_calibracion.md` §8: fuga de
gold al fragmento (benigna: siempre `dudoso` → adjudicación), rigor formal
en fronteras de equivalencia, consistencia interna no medida, brecha de vara
en U6 (no aplicable a EV2). Gasto de la calibración USD 3,18.

**Desvíos declarados del período EV2** (los 8 de `reporte_ev2.md` §8, todos
registrados en archivos):
1. `9c44516` — sello efectivo 2026-08-13, un día posterior al grafo
   `5273c0c`; aislamiento documentado en el registro de generación (el set
   no vio ningún output del pipeline v2).
2. `bb89a8e` — recuperación de 5 casos de KG-Reextraído por corte de red
   (misma db, N=1 efectivo); EA-013::literal en KG-Base con error 400
   permanente del harness congelado (traza completa, métrica computable).
3. `5b02d22` — corrige la transcripción de las ausencias de KG-Base del
   reporte de fase A; `2c84069` retira symlinks con rutas locales.
4. `2ac2fab`/`1a0ac5c` — pasada 1 de calibración sobre trazas B2 (fuente
   equivocada), conservada y rotulada NO VÁLIDA; v1.1 descartada.
5. `b624865` — commit tardío respecto del cierre de la unidad, detectado por
   la unidad §7 (trabajó sobre archivos sellados por sha en disco).
6. `9044a04` — auditoría 10 % redondea a 0 → laudo mínimo 1 por grafo; regla
   de agregación con votos pendientes ratificada por laudo.
7. `03ebe83` — votos ADJ pendientes 17 (no 24 como decía el mandato); fichas
   compartidas por textos idénticos.
8. `237fb8f` — colisión del alias "v2" resuelta por nomenclatura canónica.

## 3. Backlog de nodos

Fuente: `data/backlog/backlog.jsonl` (71 líneas, 27 ids únicos; sin eventos
nuevos desde el commit `24432a4`, 2026-08-07). Regla del estado efectivo por
id: se recorre el archivo en orden y (i) todo evento con la clave `estado` no
vacía fija el estado; (ii) la clave `estado_retriage` — propia de los eventos
`retriage_v3` y DISTINTA de `estado` — fija el estado solo cuando vale
`resuelta_por_v3`; su otro valor (`vigente_sin_cambios`) no modifica nada;
(iii) los eventos sin ninguna de las dos claves (p. ej. `nota`) tampoco
modifican. Comando que implementa la regla tal cual y devuelve la tabla:
`python3 -c "import json,collections; est={}; [est.__setitem__(o['id'], o['estado'] if o.get('estado') else 'resuelta_por_v3') for o in map(json.loads, open('data/backlog/backlog.jsonl')) if o.get('estado') or o.get('estado_retriage')=='resuelta_por_v3']; print(len(est), dict(collections.Counter(est.values())))"`
→ `27 {'resuelta_por_v3': 2, 'verificado': 10, 'triaged': 15}` (recontado en
esta actualización: idéntico al tablero anterior).

| Estado | Cantidad | Ids |
|---|---|---|
| `verificado` | 10 | BKL-0003..0007, 0017, 0019, 0023, 0026, 0027 |
| `resuelta_por_v3` (retriage) | 2 | BKL-0001, BKL-0002 |
| `triaged` vigentes | 15 | BKL-0008..0016, 0018, 0020..0022, 0024, 0025 |

Sin aplicaciones nuevas en el período: la semana se dedicó a la
re-extracción y a EV2. La priorización de las 15 `triaged` queda pendiente
de laudo; su tratamiento previsto pasa del parche manual a la corrección en
el pipeline (§5).

**Intake de la app** (`data/backlog/intake/cola_intake.jsonl`; el archivo es
un log de eventos por caso, se cuenta por caso y no por línea):
`python3 -c "import json; est={}; [est.__setitem__(x['caso_id'], x['estado']) for x in map(json.loads, open('data/backlog/intake/cola_intake.jsonl'))]; print(len(est), sum(1 for v in est.values() if v=='pendiente_de_triage'))"`
→ `3 0`: **3 casos, 0 pendientes de triage** (2 `adjudicado` — uno derivó en
BKL-0024 —, 1 `descartado` → BKL-0025; eventos del 2026-08-02). El tablero
anterior contaba líneas (6, 3 pendientes): la corrección es de conteo, no de
estado.

Notas (sin cambios desde el 2026-08-07):
- **BKL-0026** (alta 2026-08-05, laudo commit `5b66d8b`) — defecto de capa
  generación, especie `alucinacion_agente` (casilla existente de la
  taxonomía v5.7): paráfrasis de verbatim sintácticamente ambiguo que
  invierte la norma con el nodo correcto presente en contexto (contraste
  RT-C6-1 vs RT-C6-2, `ver_nodo` byte-idéntico). La medición N=3 de RT-C6-1
  dio **incorrecta 3/3** (labels `rt_c6_n3_r{1,2,3}`, dbs separadas, 0 hits
  de caché): el flag "n=1 — sistematicidad NO confirmada" fue **retirado**
  (evento del 2026-08-07 en `backlog.jsonl`); el defecto es sistemático y
  reproducible con retrieval perfecto. Estado `verificado`, `aplicado_en`
  null (defecto de agente, no del grafo). EV2 lo replica a escala: la
  generación es la clase modal de fallas en los tres grafos (§2.b, H3).
- **BKL-0027** (alta 2026-08-05, mismo laudo) — defecto de capa navegación,
  especie `navegación` (casilla existente de la taxonomía v5.7): asimetría
  direccional de `ver_vecinos` en roles alcanzables solo por aristas
  entrantes (RT-C6-3); pariente directo de BKL-0022. Estado `verificado`
  con flag n=1 (sin medición de sistematicidad programada), `aplicado_en`
  null.
- **BKL-0024 y BKL-0025** — altas de `app_feedback` (especie `ausencia`),
  `triaged` el 2026-08-02.
- **BKL-0022** queda `triaged`: su orfandad léxica está mitigada por
  navegación tras C4, pero esa navegabilidad es orden-dependiente bajo la
  ventana de 40 de `ver_vecinos` (fragilidad registrada en el evento `nota`
  del 2026-08-02); el fix durable queda diferido a la migración de backend
  (§5).
- **BKL-0020** acumuló la arista pendiente de C4 (la DUDOSA de
  `Sujeto_propuesto_originante_acreedor_inicial`), de modo que sus dos
  originantes son hoy una sola decisión de modelado.

## 4. Backlog RX (instrumento) y re-extracción

Fuente: `docs/backlog_reextraccion.md` (último commit `6cca6c9`, 2026-08-02).
El backlog RX fue la spec y la batería de pruebas de la re-extracción v2
(issue #8); la re-extracción ya se ejecutó (abajo) y el cierre formal de cada
entrada con evidencia del pipeline nuevo es una unidad pendiente del carril
de escritura (§5). Estado por entrada tal como está escrito en el archivo:

- **RX-01** — `chunk_id` ambiguo (81 ids / 183 chunks): mitigado en v3; fix de raíz pendiente.
- **RX-02** — location desplazada por coalescing (21 chunks / 26.308 chars): no mitigable en ensamblado.
- **RX-03** — falsos headers por referencias cruzadas (17 chunks / 47.813 chars): no mitigable; reproducibilidad DECLARADA.
- **RX-04** — 3 puntos sin articulado propio (clasificación 1.1 y 4.5, exterior 9.2): no mitigable.
- **RX-05** — 13 chunks con roles documentales mezclados: no mitigable; unidad de conteo DECLARADA.
- **RX-06** — 51 chunks partidos por `HARD_CAP_CHARS`: no mitigable; daño sin cuantificar (falta gold por chunk).
- **RX-07** — extracción del índice pagada (48 chunks): mitigada en v3; con precisión sellada del chunk mixto `clasificacion_deudores::10.4`.
- **RX-08** — 25 nodos cáscara heredados del índice: registro, no acción; se resuelve con RX-04.
- **RX-09** — preámbulos descartados (1.207 chars): impacto despreciable; listado para declarar cobertura 100%.
- **RX-10** — tablas linealizadas dentro del articulado: daño POR INSTANCIA, no sistemático; la instancia conocida (montos 1.2) ya corregida vía BKL-0006; toda tabla numérica requiere verificación individual.

**Re-extracción v2 (issue #9) — EJECUTADA; estado final:**
- Diseño `docs/diseno_reextraccion_v2.md` (`a8fa053`, 2026-08-10): pipeline
  E0–E5 (chunking estructural con herencia, extractor con prefijo cacheado,
  reduce determinístico, verificador de completitud en contexto fresco,
  E4 resolución de variación, E5 esqueleto). Calibración E0→E3 sobre `pro`:
  E1 `cd76991` (87/88 chunks, USD 0,73), E2 `8d0fac4` (mini-grafo 358/725,
  paridad de ids 447/447), E0 corregido + E3 `e287fe3` (detección gold 8/8
  en ciego, cola real 29,9 %).
- **Enmienda 01** (`docs/enmienda_01_diseno_reextraccion_v2.md`, `baf5608`;
  implementación `d082812`, 2026-08-11): bloques estructurales como unidades
  de extracción de primera clase, con predicciones refutables — **P1
  confirmada** (faltantes solo-en-herencia 60→0 por construcción), **P2
  refutada y publicada** (cola medida 21,8 % contra <10 % pre-declarado),
  **P3 confirmada** (USD 2,48 < 2,87); política de aceptación por severidad
  + guardia estructural → cola derivada 2,0 %, 45 residuales declarados.
- **KG-Reextraído (`8e2eadee`) final** (`5273c0c`, 2026-08-12): corpus de 5
  TOs completo, 6.178 nodos / 11.415 aristas, 1.683/1.763 unidades aceptadas
  (80 en cola con expediente, 975 residuales declarados como pasivo), tests
  de respuesta conocida 3/3 PASS (BKL-0024, 125 %, 1.1.2.5), re-extracción
  dirigida 5/6 recuperadas (`cap::4.2.1.2` queda como caso testigo del
  límite single-shot), **USD 32,97** de tope 48,50
  (`data/experiment/reextraccion_v2/corpus_v2/salida/estado_corpus.json`).
  **E4/E5 no ejecutados** (`docs/diseno_reextraccion_v2.md`, definidos y no
  corridos): KG-Reextraído es el grafo del pipeline E0–E3 sin resolución de
  variación ni esqueleto de clases.
- Resultado en EV2: §2.b (empate técnico con KG-Refinado; trade-off
  completitud estructural vs granularidad de ancla, `docs/nomenclatura_grafos.md` §3.b).

## 5. Cola de unidades y líneas de trabajo

**La cola vigente de unidades es el plan de tesis de la autora** — documento
de trabajo por carriles (medición / grafo y pipeline / escritura y
gobernanza), NO commiteado a la fecha de este tablero; se referencia sin
detallar. Cada unidad ejecutada cita el plan por id en su mandato y propone
su actualización al frenar; los bloques del plan se abren como issues del
repo. Este tablero registra el estado de las líneas de trabajo que la cola
anterior enumeraba:

- **U5 (re-calibración del verificador): HECHA** — gate U5 pasado y
  verificador validado-en-familia v2/v3 (`docs/lectura_gate_u5.md`, commit
  `f5bfb2c`; Motor 3 habilitado como diagnóstico automático con laudo
  humano). **Piloto sin-gold U6 (2026-08-07): Motor 3 NO validado como
  adjudicador sin humano** — acuerdo de capa 4/13 (estricta; 6/13 en
  sensibilidad) contra umbral pre-registrado ≥ 11/13; adjudicación manual
  permanente (`docs/resultado_piloto_singold_u6.md` §1). **Análisis de 5
  casos con atribución de fuente (2026-08-08, `d0bf8bf` + `87a431c`, cierra
  issue #1): sin señal** — acuerdo de capa 1/5 (estricta) / 2/5
  (sensibilidad); el patrón KG↔agente se sostiene en ambas cohortes
  (`docs/resultado_analisis_5_atribucion_u6.md` §1).
- **Resto del backlog de nodos (§3):** 15 `triaged`, sin aplicaciones
  nuevas; el tratamiento previsto migra del parche manual a la corrección
  en el pipeline con regression suite (plan de tesis).
- **Matriz de `scripts/shapes_validator.py` a esquema v2:** pendiente desde
  julio (sin cambios).
- **U6 — exploración dirigida: EJECUTADA Y ADJUDICADA** (corrida
  `u6_exploracion`, 25 casos; adjudicación humana sellada 7 correctas / 15
  parciales / 3 incorrectas, `data/experiment/exploracion/adjudicacion/u6_adjudicacion_humana.jsonl`,
  commit `b337152`). Las 25 U6 fueron además la fuente de calibración del
  juez de fidelidad EV2 (criterios `2ac2fab`, calibración `1a0ac5c`) y sus
  25 anclas se incorporaron al mapa de territorio quemado (`63cc420`:
  disponibles 167→143). Motor 2 operativo (`scripts/adaptador_sesiones.py`,
  commit `0d5fd10`); cola de intake 3 casos / 0 pendientes (§3).
- **Canal de abstenciones-aprobadas (candidata):** sin novedades
  (`docs/protocolo_gate_u5.md` §7, `docs/lectura_gate_u5.md` §5).
- **EV2 por generación ciega: HECHO Y CERRADO** (§2.b). Diseño `7c21053`,
  queries sintéticas `e40bbb9` + `a611ed2` + `5ceb816` (98 samples, 64
  aptos, USD 2,20), sello `9c44516`, cierre `64de678`.
- **Re-extracción única: HECHA** (§4; KG-Reextraído `5273c0c`). El cierre
  del backlog RX con evidencia del pipeline nuevo y la primera release del
  pipeline completo (E4/E5, referencias cruzadas, provenance rica) son
  unidades del plan.
- **Migración Neo4j** (`docs/decision_backend_grafo.md`): **backend
  experimental ejecutado y mergeado, NO inyectado** (commit `c26cb9b`;
  `data/experiment/neo4j/README.md`): carga verificada 4.469/8.073 exactos,
  índice full-text Lucene analyzer `spanish` sobre label+descripcion,
  adaptador `Neo4jIndex` con paridad exacta en `ver_nodo`/`ver_vecinos`
  (10/10 y 10/10) y divergencia esperada en `buscar_nodos`, benchmark de
  latencia (~2 ms de mediana full-text). El pipeline de evaluación sigue
  usando el `GraphIndex` in-memory; la inyección y la ablación de retrieval
  (estructura del grafo vs algoritmo de búsqueda) son unidades del plan
  (issue #5). El techo de retrieval de EV2 (14 / 7 / 6, §2.b) es el número
  que esa ablación debe mover.
- **Escalado del corpus — prep de fase A HECHA** (`111ed19`, 2026-08-13,
  USD 0; `data/experiment/escalado_prep/resumen_escalado.md`): inventario de
  **152 TOs** congelados por sha256 (6.757 páginas), E0 seco 152/152 con
  paridad exacta contra el subset sellado (1.763/1.763 unidades), **8.010
  unidades de extracción** visibles; veredicto **68 TOs digeribles / 84
  necesitan reglas** (62 de ellos con cero unidades: E0 no engancha su
  estructura; RI 0/53 digeribles); proyección **USD 155,70** sobre lo
  visible (banda 130–179) y **~USD 269** de techo sobre ~13.800 unidades
  (E1+E3, sin E2 ni reintentos); los 68 digeribles solos: 2.009 páginas,
  6.340 unidades, USD 123,24. Catálogo de sujetos: presión de fusión
  cross-TO medida por proxy léxico (no adjudicación). **Laudo D5 (qué corpus
  se escala) PENDIENTE** (`resumen_escalado.md` §6); prerrequisitos de
  endurecimiento del pipeline y análisis de costos (issue #6) son unidades
  del plan (issue #11).
- **Comparación KG-RAG vs RAG tradicional** (pregunta de investigación,
  `README.md`; issue #12): pendiente; habilitada por EV2 cerrado y por el
  mapa causal de fallas (§2.b).

## 6. Laudos abiertos

- Cierre de la pasada 2 — laudo de M7 CERRADO (2026-08-02): `restauracion_manual` cuenta como rol normativo (fuera del numerador de M7); `esqueleto` también queda fuera del numerador (nodos sin chunk de origen); ambos integran el denominador. Declarado en la fila M7 de `docs/spec_evaluacion_intrinseca.md`. El bloqueante de la pasada 2 por este punto queda LEVANTADO. **M7 vigente: 577/4.469** — numerador = 577 nodos `tabla_norma_origen` (cero `indice`); los **11** nodos `restauracion_manual` del vigente (BKL-0017, los 9 de BKL-0004 y el de BKL-0003, según la fila M7 de la spec) quedan fuera del numerador, igual que los 70 `esqueleto`; ambos integran el denominador (recomputado: `python3 -c "import json,collections; kg=json.load(open('data/experiment/grafo_v2/reensamblado_v3/kg.json')); print(dict(collections.Counter(n.get('rol_fuente') for n in kg['nodes'])))"` → `{'esqueleto': 70, 'cuerpo': 3811, 'tabla_norma_origen': 577, 'restauracion_manual': 11}`). Los umbrales de la pasada 2 siguen pendientes de laudo (§2.a).
- **Indexación de lecturas en `docs/INDICE.md`: CERRADO en esta actualización
  (2026-08-17)** — `docs/lectura_escalon1b.md` y las lecturas, pre-registros
  y protocolos del período (EV2, re-extracción, juez, U-A0, nomenclatura)
  quedaron indexados (verificación: `grep -n "lectura_escalon1b\|reporte_ev2\|nomenclatura_grafos" docs/INDICE.md`
  no vacío).
- **Laudo D5 — corpus a escalar:** pendiente
  (`data/experiment/escalado_prep/resumen_escalado.md` §6): los 152 TOs son
  el universo publicado, no el corpus elegido; los 84 «necesitan reglas» no
  tienen decisión (excluir / escribir reglas / segunda vuelta).
- **Experimento de memoria de sesiones** (candidatas: Graphiti — sinergia
  Neo4j —, TencentDB-Agent-Memory modo solo-artefactos, cognee; gbrain
  descartado): condición post-U5 CUMPLIDA; pendiente laudo de arranque y
  timebox.

## 7. Disciplinas activas

- **Pre-registro con válvula:** protocolo o vara sellada ANTES de toda corrida; desvíos por válvula documentada, nunca ajuste silencioso (los 8 desvíos del período EV2 están enumerados en §2.b).
- **Material quemado:** EV1/CQ/CQN/CQN2 no se reutilizan como re-test ni objetivo. Las 25 anclas de U6 están en el mapa de territorio quemado (`63cc420`).
- **Un commit por corrección:** cada arreglo del grafo con su evento en `backlog.jsonl` y su SHA.
- **Verificación contra archivos:** todo dato de estado sale de archivos del repo, nunca de memoria.
- **Blind eval generation para EV2:** las preguntas nuevas se generaron a ciegas contra los PDFs, sin ver los grafos (registro de generación en el manifest sellado `9c44516`).
- **Nomenclatura canónica de grafos:** KG-Base / KG-Refinado / KG-Reextraído con sha corto en primera mención (`docs/nomenclatura_grafos.md` §4); los paths jamás se renombran.

## 8. Hitos

- **Semana 27/07–02/08:** escalón 1b medido y adjudicado (v2 27/36 → v3 29/36;
  el defecto de ensamblado explicaba la mitad del gap contra run_3); inversión
  P-b confirmada (pasada 1 intrínseca); v3 promovido a vigente; circuito de
  refinamiento estrenado (C1 restauración 1.1, C2 montos 1.2; 3/22 entradas
  cerradas); biblioteca ampliada (playbook fichado, KARMA como 09, mapa de
  incorporación); CLAUDE.md + tablero. Commits 1–14 de la semana.
- **2026-08-02:** gate U5 pasado (cero silenciosos + 3/4, cuarto en rama de
  lectura), verificador validado-en-familia v2/v3, Motor 3 habilitado
  (diagnóstico automático, laudo humano), USD 23,22 (`docs/lectura_gate_u5.md`).
  Además: **C3 y C4 aplicadas y verificadas** (re-tests 4/4 y 5/5,
  `data/backlog/retests/C{3,4}_retest_2026-08-02.md`); **adaptador de
  sesiones (D1) construido** — Motor 2 operativo
  (`scripts/adaptador_sesiones.py`, commit `0d5fd10`); **INFRA-2** (reglas
  g/h del circuito de trabajo, commit `1ef98cf`). Commits de la semana
  27/07–02/08: **30**
  (fuente: `git rev-list --count --since=2026-07-27 HEAD`).
- **Semana 03/08–07/08:**
  - **C5, C6 y C7 aplicadas y verificadas** (re-tests determinísticos 32/32,
    38/38 y 27/27: `data/backlog/retests/C5_retest_2026-08-02.md`,
    `C6_retest_2026-08-03.md` y `C7_retest_2026-08-03.md`); grafo vigente en
    4.469/8.073, sha256 `26fac8b4…` (§1).
  - **Corrida real `rt_c5_c6`** (agente+juez, 9 preguntas, USD 0,40 —
    `summary_rt_c5_c6_reensamblado_v3.json`): **C5 5/5, C6 2/4**; laudo de
    deslinde de capas (capa KG cumplida; residuos de capa agente) → altas
    **BKL-0026** (generación) y **BKL-0027** (navegación), commit `5b66d8b`.
  - **U6 — exploración dirigida:** corrida `u6_exploracion` de 25 casos;
    adjudicación humana sellada **7 correctas / 15 parciales / 3
    incorrectas** (commit `b337152`).
  - **Piloto sin-gold U6** (pre-registrado, commits `3e507c1` + `e55388c`):
    **Motor 3 NO validado** — acuerdo de capa 4/13 (estricta) contra umbral
    ≥ 11/13; adjudicación manual permanente. Consumo USD 18,37
    (`docs/resultado_piloto_singold_u6.md`, commit `24432a4`).
  - **N=3 de RT-C6-1:** incorrecta **3/3** (labels `rt_c6_n3_r{1,2,3}`,
    0 hits de caché) — flag n=1 de BKL-0026 retirado (evento 2026-08-07 en
    `backlog.jsonl`).
  - **Backend Neo4j experimental completo y mergeado, no inyectado**
    (commit `c26cb9b`, `data/experiment/neo4j/README.md`).
- **08/08–09/08:** análisis pre-registrado de 5 casos U6 con atribución de
  fuente (`d0bf8bf` pre-registro, `87a431c` resultado): **sin señal** (1/5
  estricta), patrón KG↔agente sostenido; fe de erratas de trazabilidad de
  las notas U6; cierra issue #1.
- **Semana 10/08–17/08** (27 commits, `git rev-list --count 87a431c..HEAD`;
  con los 2 del 08/08 son los 29 desde el tablero previo,
  `git rev-list --count f665d77..HEAD`):
  - **Diseños sellados (10/08):** re-extracción v2 E0–E5 (`a8fa053`, issue
    #8), queries sintéticas (`e40bbb9`, issue #3), EV2 de dos ejes con
    cohortes núcleo-limpio/dirigida (`7c21053`, issue #4); mapa de
    territorio 5 sets con las 25 anclas U6 quemadas (`63cc420`).
  - **Queries sintéticas fase A+B** (`a611ed2`, `5ceb816`): 98 samples
    estratificados, 64/98 pares aptos, USD 2,20.
  - **Pipeline de re-extracción calibrado sobre `pro`** (E1 `cd76991`, E2
    `8d0fac4`, E0 corregido + E3 `e287fe3`) → **Enmienda 01** (`baf5608` +
    `d082812`: P1 confirmada, P2 refutada y publicada, P3 confirmada) →
    **KG-Reextraído (`8e2eadee`) final** (`5273c0c`, 12/08): 6.178/11.415,
    tests 3/3, USD 32,97 (§4).
  - **Sello de EV2** (`9c44516`, 13/08): 40 preguntas / 164 criterios +
    protocolo de corrida + manifest sha256 6/6.
  - **Prep del escalado fase A** (`111ed19`, 13/08, USD 0): 152 TOs, 8.010
    unidades, 68 digeribles / 84 necesitan reglas, proyección USD 155,70 /
    ~269 techo; D5 pendiente (§5).
  - **Corrida EV2 y evaluación** (14–17/08): agente N=1 sobre los tres grafos
    (`bb89a8e`, 456 trazas, USD 14,88); pre-registro del método de fidelidad
    (`be8a84f`); navegabilidad determinística 336/336 (`5b02d22`, +
    `2c84069`); criterios U6 (`2ac2fab`) y **juez v1 congelado**
    (`1a0ac5c`, USD 3,18); fidelidad base (`b624865`, USD 4,34);
    encadenamiento §7 (`9044a04`, USD 13,21); worksheet ciego (`03ebe83`);
    **EV2 CERRADO** (`64de678`): KG-Base 3/20/17, KG-Refinado 5/26/9,
    KG-Reextraído 4/27/9; juez 11/12 y 52/53 contra adjudicación humana.
  - **Nomenclatura canónica** (`237fb8f`) y **U-A0** — reporte consolidado
    EV2 (USD 35,62 recomputados) + regla de atribución sellada pre-cómputo
    (`40603a9`) + atribución determinística de fallas H1–H7 (`85d9fdb`):
    perfiles de falla distintos en el 9-9, generación clase modal 17/25/21,
    techo de retrieval 14/7/6 (§2.b).
