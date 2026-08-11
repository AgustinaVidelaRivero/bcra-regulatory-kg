# Informe E2 — Reduce en código + censo estructural (pipeline re-extracción v2)

Unidad E2 del pipeline v2 (diseño vinculante: `docs/diseno_reextraccion_v2.md`
§3-E2). Código puro, cero LLM, cero costo de API. Convierte las extracciones
por chunk de E1 en un grafo con ids determinísticos, con guarda de fan-in
antes de ensamblar y censo estructural contra el mapa de E0.

## 1. Qué hay acá

| Archivo | Qué es |
|---|---|
| `e2_lib.py` | Ensamblador (T1), guarda de fan-in (T2), censo estructural (T3) |
| `correr_e2.py` | CLI de corrida por TO; escribe `salida/` |
| `selftest_e2.py` | Selftest offline (T4): 31 checks, incluye la corrida real de pro |
| `salida/grafo_pro.json` | Mini-grafo de la calibración pro (358 nodos, 725 aristas) |
| `salida/fanin_pro.json` | Reporte de fan-in de la corrida real |
| `salida/censo_pro.json` | Censo estructural de pro contra E0 |
| `salida/reporte_e2_pro.json` | Reporte integral (conteos, dedup, conflictos, sha256) |

Reproduce todo:

```
cd data/experiment/reextraccion_v2/e2_reduce
python3 selftest_e2.py           # 31/31, offline
python3 correr_e2.py --to pro --extracciones ../e1_extractor/salida/faseB_pro/extracciones.jsonl
```

## 2. Decisiones de implementación

**Ids determinísticos (T1).** Uso la convención VIGENTE del re-ensamblado v3:
`entity_slug_v3` de `data/experiment/grafo_v2/code/assemble_v3.py` (líneas
95–129) — slug normalizado completo + sufijo sha1[:6] del slug entero, id
final `<Type>_<slug80>_<sha6>`. `assemble_v3.py` no es importable en este
entorno (su cadena de imports requiere el SDK de API), así que las tres
funciones están copiadas textuales en `e2_lib.py`; el selftest extrae las
originales por AST del fuente y verifica paridad salida-a-salida sobre 447
casos (10 de borde + las 437 entidades reales de pro). Si la copia diverge
del original, el selftest falla.

**Dedup EXACTO solamente.** Colisión = mismo type + mismo slug normalizado
completo (el sufijo sha del slug entero garantiza que solo contenido
idéntico-tras-normalizar colisiona; sin colisiones de prefijo por
truncamiento). Al mergear: provenances acumuladas con dedup exacto,
properties first-write-wins EN ORDEN DOCUMENTAL con todo conflicto
REGISTRADO en `reporte_e2_pro.json → conflictos_properties` (36 en pro, casi
todos variantes de `materia` del TextoOrdenado). La resolución con juicio es
de E4; acá no hay heurísticas.

**Determinismo por orden documental.** Los registros de E1 se procesan en el
orden de los chunks de E0 (orden documental), no en el orden de llegada del
jsonl. El selftest baraja el jsonl y verifica grafo bit-idéntico; la doble
corrida de `reducir()` da el mismo sha256.

**Guarda de fan-in (T2).** Esperados = ids de `chunks_{to}.json` de E0;
recibidos = registros del jsonl de E1. Estados: aceptado / rechazado
(contabilizado con motivo; no bloquea) / ausente. Además detecta chunk_ids
duplicados (precedente RX-01: el ensamblado v1/v2 descartó 102 resultados en
silencio por colisión de chunk_id) e inesperados. Ausentes, duplicados o
inesperados ⇒ `reducir()` aborta con `FanInError` ANTES de ensamblar y el CLI
persiste solo el reporte de fan-in; `--permitir-parcial` es la única vía de
ensamblar un set parcial y deja el reporte marcado `"parcial": true`.

**Censo estructural (T3).** Criterio: "nodo de contenido" = type fuera de
{TextoOrdenado, Sujeto} (BKL-0024 se detectó como "cero nodos de cuerpo";
contar el nodo TextoOrdenado — presente en casi todo chunk y dedupeado a un
nodo por documento — volvería vacuo el censo). Dos niveles:

- *Nivel chunk (terminal):* toda unidad chunkeada por E0 debe tener ≥1 nodo
  de contenido anclado a su punto propio. Las ausencias se diagnostican
  cruzando fan-in (rechazo E1), flags de E0 (tabular/fórmula) y el aporte por
  chunk (¿ancló solo a la herencia? ¿extrajo solo meta?).
- *Nivel mapa (oráculo):* toda unidad de `censo_oraculo.json`
  (coincidencias ∪ solo_mapa ∪ solo_parser) debe quedar cubierta por anclaje
  exacto o descendiente. Las unidades que E0 ya reconcilió como limitación
  conocida están en el registro `LIMITACIONES_E0` de `e2_lib.py` con su
  diagnóstico ex ante citado de `e0_chunking/salida/censo_oraculo.md`; las de
  clase granularidad se dan por reconciliadas solo si sus unidades del parser
  están cubiertas; ric 4.4 es ausencia real conocida (ver §4). Las ausencias
  se reportan — jamás se inventa estructura para taparlas.

## 3. Corrida real (calibración pro, 88 chunks)

Fan-in: **88 esperados = 87 aceptados + 1 rechazado contabilizado
(`pro::3.1.1.2`, `entities_o_relations_invalidos`, el rechazo a nivel chunk
ya registrado por el validador de E1), 0 ausentes, 0 duplicados, 0
inesperados** → apto para ensamblar sin flag.

Grafo (`salida/grafo_pro.json`, sha256 `113bafd32bb7…` completo en el
reporte): **358 nodos, 725 aristas**.

- Nodos: 207 Obligacion, 81 Operacion, 45 Restriccion, 13 Excepcion,
  9 Sujeto (materializados del catálogo por referencia de `sujeto_id`),
  2 Comunicacion, 1 TextoOrdenado.
- Conservación de entidades: 437 aceptadas por E1 = 349 nodos creados + 88
  merges exactos (86 del TextoOrdenado que dedupea a 1 nodo con 87
  provenances, 2 de contenido).
- Conservación de aristas: 729 relaciones aceptadas por E1 = 725 aristas +
  1 provenance acumulada + 3 repeticiones exactas contabilizadas + 0
  rechazos. Re-validación E2 de firmas contra la matriz y de refs: **0
  rechazos nuevos** (E1 ya había validado).
- Dedup de contenido aplicado (los únicos 2 casos, verificables en el
  reporte): (i) la obligación de informar comisión de préstamos hipotecarios
  UVA/dólar MEP, repetida casi textual en 2.3.1.1 y 2.4.1 → 1 nodo con ambas
  provenances; (ii) una obligación idéntica anclada al chapeau S3 desde los
  chunks 3.1.3 y 3.1.4 → 1 nodo (provenance única: a granularidad punto ambas
  citas son la misma, S3/herencia_encabezado). Cero fusiones con juicio.
- Cuarentena de sujetos propuestos: 0 (consistente con `resumen_faseB.json`).

## 4. Censo de pro contra E0

- **Nivel mapa: 17/17 unidades cubiertas, 0 ausencias** (pro reconcilia
  exacto con el oráculo; no aplica ninguna limitación conocida).
- **Nivel chunk: 81/88 cubiertas, 7 ausencias diagnosticadas** (ninguna
  inventada, todas en `salida/censo_pro.json`):
  - `3.1.1.2` — chunk rechazado en fan-in E1 (`entities_o_relations_invalidos`).
    Única ausencia causada por rechazo.
  - `1.1.2.1/.2/.3/.4/.6` — extracción solo-meta: el extractor emitió
    únicamente el nodo TextoOrdenado. Son los sub-puntos de la enumeración de
    sujetos obligados, cuyo contenido normativo es la definición de sujetos —
    y el esquema v2 prohíbe crear entidades para sujetos (catálogo cerrado).
    Ausencia esperable por diseño del esquema, pero queda flaggeada para el
    juicio de E3 (nótese que 1.1.2.5 — la salvedad de mutuales/cooperativas,
    BKL-0003 — SÍ tiene contenido extraído y no figura como ausencia).
  - `3.2.3.8` — contenido anclado SOLO a la herencia: 1 obligación en el
    chapeau 3.2.3 y 0 nodos en el punto propio (candidato a E3).

**Cruce con limitaciones conocidas de E0 (mandato):** el registro
`LIMITACIONES_E0` cubre las 8 unidades solo-mapa de `censo_oraculo.json`
(cap S10–S12, ext S1, ric 3.2/4.4/S1/S12). El caso **ric 4.4.x** queda
verificado por selftest (checks 19–21): el censo de ric lo lista como
*ausencia conocida ex ante* citando la explicación de E0
(`censo_oraculo.md` §ric): el cuerpo NO contiene un header "4.4."; 4.4.3 y
4.4.4 aparecen huérfanos de su padre y el parser los rechaza
(`padre_4.4_no_abierto`, registrado en `estructura_ric.json →
rechazos_header`), quedando su contenido como prosa del punto abierto
precedente — defecto del documento fuente; no se fabrica un 4.4 inexistente.
Esto es el test conceptual BKL-0024 operando: la ausencia se detecta contra
el mapa y se reporta con diagnóstico, nunca se rellena.

## 5. Selftest (T4)

`python3 selftest_e2.py` → **31/31**, offline. Cobertura: paridad AST de la
convención de ids contra `assemble_v3.py` (447 casos); determinismo (doble
corrida + jsonl barajado + sha256 end-to-end); fixtures de colisión exacta,
no-fusión de contenido distinto, ref rota, firma inválida re-validada,
set parcial (aborta sin flag / marca `parcial` con flag), chunk_id duplicado
(RX-01), chunk inesperado, rechazado-no-bloquea, sujeto propuesto en
cuarentena; censo con ausencia diagnosticada y no inventada; ric 4.4 con
cita ex ante; e integración real sobre pro (fan-in 88=87+1, conservación de
entidades y aristas, 0 rechazos E2, ids únicos sin refs rotas, diagnósticos
del censo).

## 6. Límites de esta unidad

- El grafo de pro es el mini-grafo de calibración de la fase B de E1, no una
  medición: sirve como test de integración de E2 y como insumo de la
  calibración de E3.
- E2 no jerarquiza sujetos (esqueleto del catálogo completo y jerarquía
  subclase_de/miembro_de: etapa de anclas E5) ni resuelve variación
  cross-chunk (E4). Los 36 conflictos de properties registrados son insumo de
  E4.
- La provenance es a granularidad punto (principio 2.e): dos chunks que
  anclan contenido idéntico al mismo punto heredado rinden una sola cita (el
  caso (ii) del §3).

---

## Enmienda 01 (2026-08-11) — mapa ampliado con mini-chunks

Sin lógica nueva de ensamblado (§2.c de la enmienda): los ids de E2 ya son
función del contenido y la provenance. Cambios mínimos:

- `cargar_chunks_e0`/`cargar_censo_oraculo`/`reducir` ganan `e0_dir`
  (default: la salida sellada — los tests sellados no cambian); el CLI gana
  `--e0-dir` y `--sufijo` para la corrida enm01 sin pisar la sellada.
- El aporte por chunk clasifica `rol_documental = bloque_<rol>` como
  contenido PROPIO (el bloque ES el texto propio del mini).
- Censo nivel chunk: los mini-chunks comparten `unidad` con su punto de
  origen, así que su cobertura se mide por el aporte propio del chunk id (no
  por el punto, que otro chunk pudo cubrir); un mini solo-meta es ausencia
  con diagnóstico propio.

**Corrida enm01** (`python3 correr_e2.py --to pro --extracciones
../e1_extractor/salida/faseB_pro_enm01/extracciones.jsonl --e0-dir
../e0_chunking/salida_enm01 --sufijo _enm01`): fan-in 101 = 101 aceptados +
0 rechazados/ausentes/duplicados; grafo `salida/grafo_pro_enm01.json` con
370 nodos / 718 aristas (sha256 bbdf9caa41be…); conservación exacta
(464 entidades in = 362 nodos de contenido+meta + 102 merges; 720 relaciones
in = 718 aristas + 2 prov acumuladas + 0 rechazos E2). Censo nivel chunk
95/101 (6 ausencias solo-meta diagnosticadas: 1.1.2.x sujetos-enumeración y
3.2.3.7/8 — mismas clases que la corrida sellada; ningún mini en ausencia);
nivel mapa 17/17.

**Selftest ampliado: 35/35 PASS** (31 previos re-pasados + 4 de mini-chunks:
fan-in con mini esperado, aporte bloque_*, cobertura por chunk id, ausencia
de mini solo-meta diagnosticada).
