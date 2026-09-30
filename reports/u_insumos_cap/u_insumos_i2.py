"""U-INSUMOS-CAP, etapa I2 — recorrido del ejemplo del préstamo por componente (solo lectura).

El ejemplo es cla::5.1.1.1 → cla::3.7 sobre KG-Reextraído-r1 (0226e947…). Para cada
componente del pipeline, el script ubica el artefacto que contiene el paso del
ejemplo (ruta y línea, o índice/id), extrae un fragmento corto y computa el hecho
que el ejemplo muestra; si no hay artefacto, el componente queda NO ENCONTRADO.
No llama a la API, no usa Neo4j y no genera ningún artefacto del pipeline.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_insumos_cap/u_insumos_i2.py
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_insumos_cap/u_insumos_i2.py --out-dir <dir>

Salida: <out-dir>/recorrido_prestamo.md (por defecto, el directorio de este script).
Determinístico: sin fechas propias, sin rutas absolutas. La caché de reintentos de
E1 (e3_verificador/cache/e1_reintentos.db, fuera de git) se abre solo con
file:…?immutable=1; si no está, ese extracto queda NO ENCONTRADO.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[1]

REX = "data/experiment/reextraccion_v2"
CHUNKS_CLA = f"{REX}/e0_chunking/salida_enm01/chunks_cla.json"
CHUNKS_CLA_T0 = f"{REX}/e0_chunking/salida_tanda0/chunks_cla.json"
SAL = f"{REX}/corpus_v2/salida/cla"
E1 = f"{SAL}/extracciones_e1.jsonl"
VER = f"{SAL}/veredictos.jsonl"
FIN = f"{SAL}/finales.jsonl"
EXF = f"{SAL}/extracciones_finales_cla.jsonl"
GRAFO_CLA = f"{SAL}/grafo_cla.json"
REP_E2 = f"{SAL}/reporte_e2_cla.json"
RESUMEN_E3 = f"{SAL}/resumen_e3.json"
R1 = f"{REX}/corpus_v2/salida_r1"
KG = f"{R1}/kg.json"
E4_FILES = [f"{R1}/e4_propuestos.json", f"{R1}/e4_conflictos.json", f"{R1}/e4_texto_ordenado.json"]
E5 = f"{R1}/e5_esqueleto.json"
REMIS = f"{R1}/referencias_remisiones.json"
PROV = f"{R1}/provenance_verificacion.json"
DB_REINT = f"{REX}/e3_verificador/cache/e1_reintentos.db"
GITIGNORE_E3 = f"{REX}/e3_verificador/.gitignore"
R1_COMUN = f"{REX}/corpus_v2/r1_comun.py"
R1_REF = f"{REX}/corpus_v2/r1_referencias.py"
R1_E5 = f"{REX}/corpus_v2/r1_e5_esqueleto.py"
KG_T0DEV = f"{REX}/corpus_tanda0/ens_desarrollo/r1/kg.json"
UMED = "reports/u_med_ejemplo"
TRAZAS = [f"{UMED}/umed2_analista_paso4_traza_c{i}.json" for i in (1, 2, 3)]
ANALISIS = f"{UMED}/umed2_analista_paso4_analisis.json"
ANALISIS_CONSOLA = f"{UMED}/umed2_analista_paso4_analisis_consola.txt"
RESUMEN_AG = f"{UMED}/umed2_analista_paso4_resumen.json"
AGENTE_PY = f"{UMED}/umed2_analista_paso4_agente.py"
PASO2 = f"{UMED}/umed2_analista_paso2_resultado.json"
REGLA_A02 = "data/experiment/ev2_reporte/regla_atribucion.md"
SALIDAS_A02 = ["data/experiment/ev2_reporte/salida", "data/experiment/ev2_tanda0"]
UCITA_PY = "scripts/ucita2_indicadores.py"
UCITA_JSON = "reports/ucita2_indicadores.json"
FIG = "docs/tesis/figuras"
DATOS = f"{FIG}/ejemplo_prestamo_datos.json"
EXTRACTOR = f"{FIG}/extraer_datos_ejemplo_prestamo.py"
GEN = {
    "1.1": f"{FIG}/generar_figura_norma_a_grafo.py",
    "1.2": f"{FIG}/generar_figura_fragmentos_vs_grafo.py",
    "1.3": f"{FIG}/generar_figura_proceso_extraccion.py",
    "2.1": f"{FIG}/generar_figura_tripleta.py",
}
LEEME = {
    "1.1": f"{FIG}/LEEME_figura_norma_a_grafo.md",
    "1.2": f"{FIG}/LEEME_figura_fragmentos_vs_grafo.md",
    "1.3": f"{FIG}/LEEME_figura_proceso_extraccion.md",
    "2.1": f"{FIG}/LEEME_figura_tripleta.md",
}
KG_SHA = "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"
C511, C37 = "cla::5.1.1.1", "cla::3.7"
CMD = ("PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B "
       "reports/u_insumos_cap/u_insumos_i2.py")
LARGO_EXTRACTO = 170


# ---------------------------------------------------------------- utilidades

def ruta(rel: str) -> Path:
    return REPO / rel


def sha(rel: str) -> str:
    return hashlib.sha256(ruta(rel).read_bytes()).hexdigest()


def cargar(rel: str):
    return json.loads(ruta(rel).read_text(encoding="utf-8"))


def lineas(rel: str) -> list[str]:
    return ruta(rel).read_text(encoding="utf-8").splitlines()


def linea_de(rel: str, aguja: str, n: int = 1) -> int | None:
    """Número de línea (desde 1) de la n-ésima línea que contiene `aguja`."""
    k = 0
    for i, l in enumerate(lineas(rel), 1):
        if aguja in l:
            k += 1
            if k == n:
                return i
    return None


def jsonl_linea(rel: str, **filtro) -> tuple[int, dict]:
    """(línea, registro) del único registro jsonl que cumple el filtro."""
    hits = []
    for i, l in enumerate(lineas(rel), 1):
        if not l.strip():
            continue
        r = json.loads(l)
        if all(r.get(k) == v for k, v in filtro.items()):
            hits.append((i, r))
    if len(hits) != 1:
        raise SystemExit(f"{rel}: {filtro} da {len(hits)} registros")
    return hits[0]


def corto(s: str, n: int = LARGO_EXTRACTO) -> str:
    s = re.sub(r"\s+", " ", s.replace("-\n", "")).strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


def sn(b: bool) -> str:
    return "sí" if b else "no"


def cod(s: str) -> str:
    return f"`{s}`"


def ult(s: str) -> str:
    """Id abreviado por su sufijo (el id completo está en la sección de nodos)."""
    return "…" + s[-6:] if len(s) > 40 else s


def exigir(cond: bool, msg: str) -> None:
    """Guarda de las afirmaciones escritas como texto fijo en el .md."""
    if not cond:
        raise SystemExit(f"FRENO: no se cumple «{msg}»")


def prov_lista(x: dict) -> list[dict]:
    return ([x["provenance"]] if x.get("provenance") else []) + (x.get("provenances") or [])


# ---------------------------------------------------------------- recorrido

def recorrido() -> dict:
    datos = cargar(DATOS)
    nodos = datos["grafo"]["nodos"]
    ids = {k: v["id"] for k, v in nodos.items()}
    aristas = datos["grafo"]["aristas"]
    kg_bytes = ruta(KG).read_bytes()
    kg_sha = hashlib.sha256(kg_bytes).hexdigest()
    if kg_sha != KG_SHA or datos["fuentes"]["kg"]["sha256"] != KG_SHA:
        raise SystemExit("kg.json o el JSON del ejemplo no son de KG-Reextraído-r1")
    kg = json.loads(kg_bytes.decode("utf-8"))
    por_id = {n["id"]: n for n in kg["nodes"]}
    contenido = [ids[k] for k in ("operacion", "restriccion_monto", "restriccion_repago",
                                  "obligacion_3_7")]
    R: dict = {"comp": {}}

    # ------------------------------------------------ E0
    chunks = {c["id"]: c for c in cargar(CHUNKS_CLA)}
    c1, c3 = chunks[C511], chunks[C37]
    fuera_de_texto = {k: v for k, v in c1.items() if k not in ("texto", "herencia")}
    igual_t0 = sha(CHUNKS_CLA) == sha(CHUNKS_CLA_T0)
    her = [h["unidad_origen"] for h in c1["herencia"]]
    intro = next(h["texto"] for h in c1["herencia"] if h["unidad_origen"] == "5.1.1"
                 and h["tipo"] != "encabezado")
    R["comp"]["E0"] = {
        "estado": "ENCONTRADO",
        "artefactos": [f"{CHUNKS_CLA}:{linea_de(CHUNKS_CLA, chr(34) + 'id' + chr(34) + ': ' + chr(34) + C511 + chr(34))} (id {cod(C511)})",
                       f"{CHUNKS_CLA}:{linea_de(CHUNKS_CLA, chr(34) + 'id' + chr(34) + ': ' + chr(34) + C37 + chr(34))} (id {cod(C37)})"],
        "extracto": [f"{C511}: «{corto(c1['texto'])}»", f"{C37}: «{corto(c3['texto'])}»"],
        "hecho": (f"5.1.1.1 es una unidad propia ({c1['tipo']}, página {c1['paginas'][0]}, "
                  f"{c1['chars_propio']} caracteres) que hereda el encabezado y el intro de 5.1.1 "
                  f"(«{corto(intro, 80)}»); 3.7 es otra unidad ({c3['tipo']}, página "
                  f"{c3['paginas'][0]}). La remisión «punto 3.7.» está solo en `texto`: "
                  f"{'ningún' if '3.7' not in json.dumps(fuera_de_texto) else 'algún'} otro "
                  "campo del chunk la registra. Flags de tabla o fórmula en True en los dos "
                  f"chunks: {sum(bool(x['flags'][f]) for x in (c1, c3) for f in ('contenido_tabular', 'formula'))} de 4."),
        "control": f"chunks_cla.json de salida_enm01 y de salida_tanda0 byte-idénticos: {sn(igual_t0)}",
    }

    # ------------------------------------------------ E1
    l1, e1 = jsonl_linea(E1, chunk_id=C511)
    l3, e13 = jsonl_linea(E1, chunk_id=C37)
    ent1 = e1["tool_input_crudo"]["entities"]
    rel1 = e1["tool_input_crudo"]["relations"]
    val1 = e1["validacion"]

    def rel_txt(rels, ents):
        tipo = {e["local_id"]: e["type"] for e in ents}
        out = []
        for r in rels:
            dst = r.get("target") and tipo.get(r["target"]) or ("Sujeto(catálogo)" if r.get("sujeto_id") else "?")
            out.append(f"{tipo.get(r['source'], '?')} {r['predicate']} {dst}")
        return out

    rt1 = rel_txt(rel1, ent1)
    contenido1 = [e for e in ent1 if e["type"] != "TextoOrdenado"]
    exigir(sorted(r for r in rt1 if " aplica_a " in r) == ["Restriccion aplica_a Sujeto(catálogo)"] * 2,
           "el primer intento emite aplica_a desde las dos Restriccion")
    R["comp"]["E1"] = {
        "estado": "ENCONTRADO",
        "artefactos": [f"{E1}:{l1} ({cod(C511)}, primer intento)", f"{E1}:{l3} ({cod(C37)})",
                       f"{SAL}/resumen_e1.json → cliente.cache_stats.namespace = "
                       f"{cod(cargar(SAL + '/resumen_e1.json')['cliente']['cache_stats']['namespace'])}"],
        "extracto": [f"{e['type']} «{e['label']}»" for e in contenido1]
                    + [f"relaciones: {', '.join(rt1)}"]
                    + [f"validación: rechazos {len(val1['rechazos'])}, advertencias "
                       f"{[a['tipo'] for a in val1['advertencias']]}, métricas "
                       f"{val1['metricas']['entities_in']}→{val1['metricas']['entities_out']} entidades, "
                       f"{val1['metricas']['relations_in']}→{val1['metricas']['relations_out']} relaciones"],
        "hecho": (f"El primer intento sobre 5.1.1.1 emitió {len(contenido1)} entidades de contenido "
                  f"({', '.join(sorted(e['type'] for e in contenido1))}) y {len(rel1)} relaciones, "
                  f"con `aplica_a` desde las dos Restriccion; la validación aceptó "
                  f"{val1['metricas']['relations_out']} de {val1['metricas']['relations_in']} "
                  f"(advertencias: {len(val1['advertencias'])}). Sobre 3.7 emitió "
                  f"{', '.join(e['type'] for e in e13['tool_input_crudo']['entities'] if e['type'] != 'TextoOrdenado')} "
                  f"con {len(e13['tool_input_crudo']['relations'])} relaciones."),
    }

    # ------------------------------------------------ E3
    lv0, v0 = jsonl_linea(VER, chunk_id=C511, intento=0)
    lv1, v1 = jsonl_linea(VER, chunk_id=C511, intento=1)
    lv3, v3 = jsonl_linea(VER, chunk_id=C37, intento=0)
    lf1, f1 = jsonl_linea(FIN, chunk_id=C511)
    lf3, f3 = jsonl_linea(FIN, chunk_id=C37)
    vf = f1["validacion_final"]
    ent_f = vf["entidades"]
    rt_f = rel_txt(vf["relaciones"], ent_f)
    op0 = next(e["label"] for e in ent1 if e["type"] == "Operacion")
    opf = next(e["label"] for e in ent_f if e["type"] == "Operacion")
    frase = "se incluirán dentro de la cartera comercial"
    d0 = [frase in (e["properties"].get("descripcion") or "") for e in ent1 if e["type"] == "Restriccion"]
    df = [frase in (e["properties"].get("descripcion") or "") for e in ent_f if e["type"] == "Restriccion"]
    lim0 = sorted(r for r in rt1 if " limita " in r)
    limf = sorted(r for r in rt_f if " limita " in r)
    rech = vf["rechazos"]
    exigir(v0["faltantes"][0]["bloqueante"] is True, "el veredicto del intento 0 es bloqueante")
    exigir(not any(r["predicate"] == "aplica_a" for r in vf["relaciones"]),
           "la validación final de 5.1.1.1 no tiene aplica_a")
    exigir(len(rech) == 1 and rech[0]["motivo"] == "firma_invalida", "un único rechazo por firma")
    # crudo del reintento en la caché (fuera de git), solo lectura inmutable
    reint = None
    if ruta(DB_REINT).exists():
        con = sqlite3.connect(f"file:{ruta(DB_REINT)}?immutable=1", uri=True)
        filas = con.execute(
            "select c.key, c.created_at, c.model, c.raw_json, c.request_json from cache c "
            "join access_log a on a.key = c.key where a.run_label = ?",
            ("corpus_cla_reintentos_e1",)).fetchall()
        con.close()
        hits = [f for f in filas if C511 in f[4] or "Los créditos de esta clase que superen" in f[4]]
        if len(hits) == 1:
            key, creado, modelo, raw, _ = hits[0]
            tu = next(b["input"] for b in json.loads(raw)["content"] if b.get("type") == "tool_use")
            reint = {"key": key, "creado": creado, "modelo": modelo,
                     "aplica_a_operacion": any(r["predicate"] == "aplica_a" and r["source"] == "e1"
                                               for r in tu["relations"]),
                     "igual_a_validacion_final": sorted(e["label"] for e in tu["entities"])
                     == sorted(e["label"] for e in ent_f)}
    art_e3 = [f"{VER}:{lv0} (intento 0, {cod(v0['tool_input']['veredicto'])})",
              f"{VER}:{lv1} (intento 1, {cod(v1['tool_input']['veredicto'])})",
              f"{VER}:{lv3} ({cod(C37)}, {cod(v3['tool_input']['veredicto'])})",
              f"{FIN}:{lf1} (estado {cod(f1['estado'])}, reintentos {f1['n_reintentos']})",
              f"{FIN}:{lf3} ({cod(C37)}, estado {cod(f3['estado'])})"]
    if reint:
        art_e3.append(f"{DB_REINT}, fila de `cache` con key {cod(reint['key'][:16] + '…')} "
                      f"(created_at {reint['creado'][:19]}, {reint['modelo']}; archivo fuera de git, "
                      f"{GITIGNORE_E3}:1; leído con immutable=1)")
    else:
        art_e3.append(f"crudo del reintento: NO ENCONTRADO ({DB_REINT} ausente o sin la fila)")
    R["comp"]["E3"] = {
        "estado": "ENCONTRADO",
        "artefactos": art_e3,
        "extracto": [f"nota del veredicto (intento 0): «{corto(v0['faltantes'][0]['nota'], 400)}»",
                     f"severidad {v0['faltantes'][0]['severidad']}, bloqueante {sn(v0['faltantes'][0]['bloqueante'])}",
                     f"rechazo de la validación del reintento: {rech[0]['motivo']} «{rech[0]['detalle']}»"],
        "hecho": (f"E3 objetó el primer intento (bloqueante); tras {f1['n_reintentos']} reintento la "
                  f"re-verificación dio `{v1['tool_input']['veredicto']}`. El reintento cambió la "
                  f"etiqueta de la Operacion («{op0}» → «{opf}») y quitó «{frase}» de las "
                  f"descripciones de las Restriccion (presente en {sum(d0)} de {len(d0)} → {sum(df)} de "
                  f"{len(df)}); la forma quedó igual: {len(limf)} `limita` Restriccion→Operacion antes "
                  f"({len(lim0)}) y después ({len(limf)}, iguales: {sn(lim0 == limf)}). La validación del "
                  f"reintento rechazó `aplica_a` Operacion→Sujeto ({rech[0]['motivo']}), así que 5.1.1.1 "
                  f"queda sin `aplica_a`. 3.7 pasó sin reintento (`{f3['estado']}`)."
                  + (f" En la caché, el crudo del reintento trae ese `aplica_a`: "
                     f"{sn(reint['aplica_a_operacion'])}; mismas etiquetas que la validación final: "
                     f"{sn(reint['igual_a_validacion_final'])}." if reint else "")),
    }

    # ------------------------------------------------ extracción final
    lx1, x1 = jsonl_linea(EXF, chunk_id=C511)
    lx3, x3 = jsonl_linea(EXF, chunk_id=C37)
    rel3 = x3["validacion"]["relaciones"]
    suj3 = [r for r in rel3 if r["predicate"] == "aplica_a"]
    R["comp"]["extraccion_final"] = {
        "estado": "ENCONTRADO",
        "artefactos": [f"{EXF}:{lx1} ({cod(C511)}, estado_e3 {cod(x1['estado_e3'])})",
                       f"{EXF}:{lx3} ({cod(C37)}, estado_e3 {cod(x3['estado_e3'])})"],
        "extracto": [f"{C511}: " + ", ".join(rel_txt(x1["validacion"]["relaciones"],
                                                     x1["validacion"]["entidades"])),
                     f"{C37}: " + ", ".join(rel_txt(rel3, x3["validacion"]["entidades"]))],
        "hecho": (f"La validación guardada es la misma que `validacion_final` de finales.jsonl: "
                  f"{sn(x1['validacion'] == vf)}. 5.1.1.1 entra a E2 con "
                  f"{len([e for e in x1['validacion']['entidades'] if e['type'] != 'TextoOrdenado'])} "
                  f"nodos de contenido y {len(x1['validacion']['relaciones'])} relaciones, ninguna "
                  f"`aplica_a`; 3.7 entra con `aplica_a` al sujeto de catálogo "
                  f"{cod(suj3[0]['sujeto_id'])}, sin `sujeto_propuesto`."),
    }

    # ------------------------------------------------ E2
    gc = cargar(GRAFO_CLA)
    idx_n = {n["id"]: i for i, n in enumerate(gc["nodes"])}
    en_e2 = {k: idx_n.get(v) for k, v in ids.items()}
    idx_e = []
    for a in aristas:
        hit = [i for i, e in enumerate(gc["edges"])
               if e["source"] == ids[a["origen"]] and e["relation"] == a["relation"]
               and e["target"] == ids[a["destino"]]]
        idx_e.append((a["relation"], a["origen"], a["destino"], hit))
    rep = cargar(REP_E2)
    R["comp"]["E2"] = {
        "estado": "ENCONTRADO",
        "artefactos": [f"{GRAFO_CLA}: nodes " + ", ".join(f"[{i}]" for i in sorted(v for v in en_e2.values() if v is not None)),
                       f"{GRAFO_CLA}: edges " + ", ".join(f"[{h[0]}]" for _, _, _, h in idx_e if h),
                       f"{REP_E2} → `fanin`, `stats`, `edges_by_relation`",
                       f"{R1_COMUN}:{linea_de(R1_COMUN, 'def cargar_grafos_sellados')} (r1 lee grafo_<to>.json)"],
        "extracto": [f"{rel} {o} → {d}: " + (f"edges[{h[0]}]" if h else "ausente") for rel, o, d, h in idx_e]
                    + [f"fanin cla: {rep['fanin']['aceptados']} aceptados de {rep['fanin']['esperados']}; "
                       f"merges_exactos {rep['stats']['merges_exactos']}; aristas referencia en el grafo del TO: "
                       f"{rep['edges_by_relation'].get('referencia', 0)}"],
        "hecho": (f"E2 ya tiene los {sum(1 for v in en_e2.values() if v is not None)} nodos con los mismos "
                  f"ids que r1 y {sum(1 for *_, h in idx_e if h)} de las {len(idx_e)} aristas del ejemplo; "
                  "falta la `referencia`, que agrega r1."),
    }

    # ------------------------------------------------ E4
    e4_menciones = {}
    for f in E4_FILES:
        s = ruta(f).read_text(encoding="utf-8")
        e4_menciones[f] = sum(s.count(v) for v in list(ids.values()) + [C511, C37])
    t_o = cargar(f"{R1}/e4_texto_ordenado.json")
    exigir(all(n == 0 for n in e4_menciones.values()), "ningún id ni chunk del ejemplo en E4")
    exigir(len(suj3) == 1 and suj3[0].get("sujeto_propuesto") is None, "3.7 con sujeto de catálogo")
    R["comp"]["E4"] = {
        "estado": "NO ENCONTRADO",
        "artefactos": [f"{f}: {n} menciones de los 5 ids o de los 2 chunks" for f, n in e4_menciones.items()],
        "extracto": [f"e4_texto_ordenado.json → canonicos.cla = {cod(t_o['canonicos']['cla'])} "
                     "(destino de las `establecida_en` del punto; no es nodo del ejemplo)"],
        "hecho": ("Ningún nodo ni chunk del ejemplo pasa por E4: el sujeto es de catálogo (no hay "
                  "`sujeto_propuesto`) y ningún nodo del ejemplo figura en conflictos ni en "
                  "propuestos."),
    }

    # ------------------------------------------------ esqueleto
    S = ids["sujeto"]
    esq_suj, esq_cont = [], 0
    for i, e in enumerate(kg["edges"]):
        esq = any(p.get("rol_documental") == "esqueleto" for p in prov_lista(e))
        if esq and e["target"] == S:
            esq_suj.append((i, e["relation"], e["source"], (e.get("provenance") or {}).get("punto")))
        if esq and (e["source"] in contenido or e["target"] in contenido):
            esq_cont += 1
    e5 = cargar(E5)
    R["comp"]["esqueleto"] = {
        "estado": "ENCONTRADO",
        "artefactos": [f"{KG}: edges " + ", ".join(f"[{i}]" for i, *_ in esq_suj),
                       f"{E5} → `aristas_esqueleto_agregadas` = {e5['aristas_esqueleto_agregadas']} (total de r1)",
                       f"{R1_E5}:{linea_de(R1_E5, 'rol_documental')} (procedencia `esqueleto`)"],
        "extracto": [f"edges[{i}]: {src} {rel} {S} · punto «{pt}»" for i, rel, src, pt in esq_suj[:2]]
                    + ([f"… y {len(esq_suj) - 2} más con la misma forma"] if len(esq_suj) > 2 else []),
        "hecho": (f"El sujeto del ejemplo recibe {len(esq_suj)} aristas "
                  f"{', '.join(cod(r) for r in sorted({r for _, r, _, _ in esq_suj}))} del esqueleto, "
                  f"sin chunk; los cuatro nodos "
                  f"de contenido del ejemplo tienen {esq_cont} aristas de esqueleto."),
    }

    # ------------------------------------------------ referencias y procedencia r1
    remis = cargar(REMIS)
    rix = [(i, x) for i, x in enumerate(remis) if x["nodo"] in contenido
           and x["punto_origen"] in ("5.1.1.1", "3.7")]
    ref_kg = [(i, e) for i, e in enumerate(kg["edges"]) if e["relation"] == "referencia"
              and e["source"] in contenido]
    otros = [ids[k] for k in ("operacion", "restriccion_repago")]
    pv = cargar(PROV)
    pv_s = json.dumps(pv["inconsistencias"], ensure_ascii=False)
    pnodo = {k: (por_id[ids[k]].get("provenance") or {}) for k in ("restriccion_monto", "obligacion_3_7")}
    R["comp"]["referencias_y_procedencia_r1"] = {
        "estado": "ENCONTRADO",
        "artefactos": [f"{REMIS}: " + ", ".join(f"[{i}]" for i, _ in rix),
                       f"{KG}: edges " + ", ".join(f"[{i}] ({e.get('rol_fuente')})" for i, e in ref_kg),
                       f"{R1_REF}:{linea_de(R1_REF, 'def _texto')} (`_texto`: label + propiedades del nodo)",
                       f"{PROV} → `resumen`, `inconsistencias`"],
        "extracto": [f"[{i}] clase {x['clase']}, evidencia «{x['evidencia']}», destino "
                     f"{x['destinos'][0]['destino']} ({x['destinos'][0]['n_nodos']} nodo)" for i, x in rix]
                    + [f"procedencia de la restricción del monto: chunk {pnodo['restriccion_monto'].get('chunk_id')}, "
                       f"páginas {pnodo['restriccion_monto'].get('paginas')}, ancestros {pnodo['restriccion_monto'].get('ancestros')}"],
        "hecho": (f"El detector de r1 leyó la paráfrasis del nodo, no el texto de E0: {len(rix)} "
                  f"detecciones sobre `descripcion` y `umbral` de la restricción del monto, "
                  f"{len(ref_kg)} arista `referencia` en kg.json. La Operacion y la restricción del "
                  f"repago no tienen `referencia` "
                  f"({sum(1 for e in kg['edges'] if e['relation'] == 'referencia' and e['source'] in otros)}). "
                  f"provenance_verificacion: inconsistencias de estructura "
                  f"{pv['resumen']['inconsistencias_estructura']}; menciones de los ids del ejemplo en "
                  f"`inconsistencias`: {sum(pv_s.count(v) for v in contenido)}."),
    }

    # ------------------------------------------------ grafo final
    lin_nodos = {k: linea_de(KG, f'"id": "{v}"') for k, v in ids.items()}
    exigir(sorted(a["relation"] for a in aristas) == ["aplica_a", "limita", "limita", "referencia"],
           "las cuatro aristas del ejemplo son 2 limita, 1 aplica_a y 1 referencia")
    p2 = cargar(PASO2)
    R["comp"]["grafo_final"] = {
        "estado": "ENCONTRADO",
        "artefactos": [f"{KG}:{lin_nodos[k]} (nodo {k})" for k in ids]
                      + [f"{KG}: edges " + ", ".join(f"[{a['indice']}]" for a in aristas),
                         f"{PASO2} → `comparacion`"],
        "extracto": [f"edges[{a['indice']}]: {a['origen']} {a['relation']} {a['destino']}"
                     f" · rol_fuente {a['rol_fuente']} · chunk {a['chunk_id']}" for a in aristas],
        "hecho": (f"En r1 el ejemplo son {len(ids)} nodos y {len(aristas)} aristas: "
                  f"{sum(1 for a in aristas if a['relation'] == 'limita')} `limita` y 1 `aplica_a` de "
                  f"extracción, 1 `referencia` de r1. Las {p2['comparacion']['n_aristas_kg']} aristas "
                  f"incidentes a los nodos del ejemplo son iguales en kg.json y en Neo4j: "
                  f"{sn(p2['comparacion']['aristas_iguales_source_relation_target_orden_procedencia_runtime'])}."),
    }

    # ------------------------------------------------ agente
    an = cargar(ANALISIS)
    res = cargar(RESUMEN_AG)
    o37 = ids["obligacion_3_7"]
    vio37 = {c["corrida"]: [l["n"] for l in c["llamadas"] if l["tool"] == "ver_vecinos"
                            and any(o["id"] == o37 for o in l["objetivo_en_output"])] for c in an}
    secuencias = {c["corrida"]: [(l["tool"], json.dumps(l["input"], sort_keys=True)) for l in c["llamadas"]]
                  for c in an}
    iguales = len({json.dumps(v) for v in secuencias.values()}) == 1
    item3 = {}
    for c in an:
        m = re.search(r"\n3\. (.*?)(\n\n|\n\d\. |$)", c["respuesta"], re.S)
        item3[c["corrida"]] = corto(m.group(1), 300) if m else None
    exigir("deben ser clasificados en la cartera comercial" in item3[1]
           and all("no se incluyen en la cartera comercial" in item3[k] for k in (2, 3)),
           "el ítem 3 afirma la inclusión en la corrida 1 y la niega en las corridas 2 y 3")
    menciona = {k: [c["corrida"] for c in an if k in c["respuesta"].lower()]
                for k in ("repago", "micro", "ventas", "ley 24.467")}
    lin_abrio = [linea_de(ANALISIS_CONSOLA, "abrio 3.7: False", n) for n in (1, 2, 3)]
    exigir(all(c["abrio_nodo_5_1_1_1"] for c in an), "las tres corridas abren nodos de 5.1.1.1")
    R["comp"]["agente"] = {
        "estado": "ENCONTRADO",
        "artefactos": TRAZAS + [f"{ANALISIS} (corridas 1–3)",
                                f"{ANALISIS_CONSOLA}:" + ",".join(str(x) for x in lin_abrio)
                                + " («abrio 3.7: False»)",
                                f"{RESUMEN_AG} → `costo_total_usd` = {res['costo_total_usd']}"],
        "extracto": [f"corrida {k}, ítem 3 de la respuesta: «{v}»" for k, v in item3.items()],
        "hecho": (f"Tres corridas de {an[0]['tool_calls']} llamadas; secuencia idéntica en las tres: "
                  f"{sn(iguales)}. Abren nodos de 5.1.1.1 y ven la Obligacion del 3.7 como vecina por "
                  f"`referencia` en las llamadas {', '.join(map(str, vio37[1]))} (corrida 1), sin abrirla "
                  f"en ninguna corrida ({sum(not c['abrio_nodo_3_7'] for c in an)} de {len(an)}). "
                  f"Respuestas que mencionan el repago: {len(menciona['repago'])} de {len(an)}; que "
                  f"mencionan «Micro» o «ventas» (contenido del 3.7): "
                  f"{len(set(menciona['micro']) | set(menciona['ventas']))} de {len(an)}. El ítem 3 dice "
                  "que esos créditos van a la cartera comercial en la corrida 1 y que no se incluyen en "
                  "las corridas 2 y 3 (extracto). Citas: "
                  f"{', '.join(sorted({c2['location'] for c in an for c2 in c['citas']}))}."),
    }

    # ------------------------------------------------ juez
    claves_ver = 0
    for t in TRAZAS:
        s = ruta(t).read_text(encoding="utf-8")
        claves_ver += sum(s.count(f'"{k}"') for k in ("veredicto", "verdict", "veredicto_pregunta"))
    exigir(claves_ver == 0, "las trazas no tienen claves de veredicto")
    R["comp"]["juez"] = {
        "estado": "NO ENCONTRADO",
        "artefactos": [f"{AGENTE_PY}:{linea_de(AGENTE_PY, 'sin juez')} («sin juez»)",
                       f"claves de veredicto en las tres trazas: {claves_ver}"],
        "extracto": [],
        "hecho": "No hay veredicto del juez sobre ninguna de las tres respuestas.",
    }

    # ------------------------------------------------ A0.2
    menc_a02 = 0
    for d in SALIDAS_A02:
        for p in sorted(ruta(d).rglob("*")):
            if p.is_file() and p.suffix in (".json", ".jsonl", ".md", ".txt"):
                menc_a02 += p.read_text(encoding="utf-8", errors="replace").count("umed2")
    exigir(menc_a02 == 0, "ninguna salida de A0.2 menciona umed2")
    R["comp"]["atribucion_A0.2"] = {
        "estado": "NO ENCONTRADO",
        "artefactos": [f"{REGLA_A02}:{linea_de(REGLA_A02, 'Veredicto de referencia de cada traza')} "
                       "(la regla atribuye contra el veredicto de cada traza)",
                       f"menciones de «umed2» en {', '.join(SALIDAS_A02)}: {menc_a02}"],
        "extracto": [],
        "hecho": "La regla A0.2 pide el veredicto de la traza, que no existe; no se aplicó a estas trazas.",
    }

    # ------------------------------------------------ indicadores de cita
    uc = ruta(UCITA_JSON).read_text(encoding="utf-8").count("umed2")
    no_vistas = [c["citas_no_vistas_normalizadas"] for c in an]
    exigir(uc == 0, "los indicadores de cita no mencionan umed2")
    R["comp"]["indicadores_de_cita"] = {
        "estado": "NO ENCONTRADO",
        "artefactos": [f"{UCITA_PY}:{linea_de(UCITA_PY, 'determinísticos sobre las 112 trazas')} "
                       "(corre sobre las 112 trazas de EV2 de r1)",
                       f"{UCITA_JSON}: menciones de «umed2» = {uc}"],
        "extracto": [f"{ANALISIS} → `citas_no_vistas_normalizadas` = {no_vistas} (campo del harness, "
                     "no un indicador de U-CITA-2)"],
        "hecho": ("Los tres indicadores de cita no se computaron sobre estas trazas; el indicador 3 "
                  "necesita el ancla de una clave de EV2, que esta pregunta no tiene."),
    }

    # ------------------------------------------------ figuras
    t0 = cargar(KG_T0DEV)
    t0_nodos = []
    for n in t0["nodes"]:
        pp = {(p.get("chunk_id"), p.get("rol_documental")) for p in prov_lista(n)}
        for cid in (C511, C37):
            if (cid, "punto_propio") in pp and n["type"] not in ("Sujeto", "TextoOrdenado"):
                t0_nodos.append((cid, n["type"], n["label"], n["id"]))
    t0_ids = {x[3] for x in t0_nodos}
    t0_aristas = [(e["source"], e["relation"], e["target"]) for e in t0["edges"]
                  if e["source"] in t0_ids or e["target"] in t0_ids]
    t0_ref_511_37 = [a for a in t0_aristas if a[1] == "referencia"
                     and any(a[0] == x[3] and x[0] == C511 for x in t0_nodos)]
    t0_cond_sin = [x for x in t0_nodos if x[1] == "Condicion"
                   and not any(x[3] in (a[0], a[2]) for a in t0_aristas)]
    exigir(not any(x[1] == "Restriccion" for x in t0_nodos)
           and not any(a[1] == "limita" for a in t0_aristas),
           "en KG-Tanda0-Desarrollo-r1 no hay Restriccion ni limita del ejemplo")
    R["t0dev"] = {"sha": sha(KG_T0DEV), "nodos": sorted(t0_nodos),
                  "ref_511_37": len(t0_ref_511_37), "cond_sin_aristas": len(t0_cond_sin),
                  "aristas": len(t0_aristas)}
    R["datos"] = {"sha": sha(DATOS), "extractor_sha": sha(EXTRACTOR),
                  "extractor_lineas": {
                      "kg": linea_de(EXTRACTOR, "KG_SHA256 = "),
                      "kg_ruta": linea_de(EXTRACTOR, "KG_REL = "),
                      "chunks": linea_de(EXTRACTOR, "CHUNKS_CLA_REL = "),
                      "nodos": linea_de(EXTRACTOR, "NODOS = ["),
                      "aristas": linea_de(EXTRACTOR, "ARISTAS = ["),
                      "rangos": linea_de(EXTRACTOR, "RANGOS_ESPERADOS = "),
                      "paquete": linea_de(EXTRACTOR, "PAQUETE_SHA256 = ")}}
    R["gen"] = {
        "1.1": linea_de(GEN["1.1"], "def cargar_datos"),
        "1.2": linea_de(GEN["1.2"], "base.cargar_datos()"),
        "1.3": linea_de(GEN["1.3"], "KG_SHA256 = "),
        "2.1": linea_de(GEN["2.1"], "KG_SHA256 = "),
        "1.2_insumos": linea_de(GEN["1.2"], 'bf["sha256_insumos"]'),
    }
    R["leeme"] = {k: sha(v) for k, v in LEEME.items()}
    R["leeme_1_2_no_traza"] = linea_de(LEEME["1.2"], "no es la traza de una corrida del agente")
    R["kg_sha"] = kg_sha
    R["fuentes"] = {r: sha(r) for r in (
        CHUNKS_CLA, E1, VER, FIN, EXF, GRAFO_CLA, REP_E2, KG, E5, REMIS, PROV, KG_T0DEV,
        *TRAZAS, ANALISIS, RESUMEN_AG, PASO2, DATOS, EXTRACTOR, *GEN.values(), *LEEME.values())}
    return R


# ---------------------------------------------------------------- markdown

ORDEN = [("E0", "E0 (chunks)"), ("E1", "E1 (salida cruda y validación)"),
         ("E3", "E3 (veredicto y reintento)"), ("extraccion_final", "Extracción final"),
         ("E2", "E2"), ("E4", "E4"), ("esqueleto", "Esqueleto"),
         ("referencias_y_procedencia_r1", "Referencias y procedencia de r1"),
         ("grafo_final", "Grafo final"), ("agente", "Agente (trazas umed2)"),
         ("juez", "Juez"), ("atribucion_A0.2", "Atribución A0.2"),
         ("indicadores_de_cita", "Indicadores de cita")]


def md(R: dict) -> str:
    L: list[str] = []
    A = L.append
    C = R["comp"]
    A("# U-INSUMOS-CAP · I2 — Recorrido del ejemplo del préstamo por componente")
    A("")
    A("Insumo citable para el capítulo 4 (mesa de escritura). No es prosa de la tesis.")
    A("")
    A("Regenerar (desde la raíz del repo; doble corrida byte a byte idéntica):")
    A("")
    A("```bash")
    A(CMD)
    A("```")
    A("")
    A(f"Ejemplo: `{C511}` → `{C37}` sobre KG-Reextraído-r1 (`{R['kg_sha']}`). Pregunta: la de "
      f"`{DATOS}` → `pregunta`. Solo artefactos existentes: lo que no existe queda NO ENCONTRADO "
      "y no se genera. Los extractos son verbatim, con los saltos de línea como espacio, las "
      "palabras partidas por guion reunidas y cortados con «…».")
    A("")
    A("**Declaración (decisión 5 del mandato).** Después de la re-extracción de la tanda 0 "
      "(U-REEXT-T0), todos los datos de este recorrido quedan como datos de KG-Reextraído-r1: "
      "describen la corrida que produjo r1, no el pipeline vigente en ese momento.")
    A("")
    A("## 0. Tabla de componentes")
    A("")
    A("| componente | estado | artefacto principal |")
    A("|---|---|---|")
    for k, et in ORDEN:
        A(f"| {et} | {C[k]['estado']} | {C[k]['artefactos'][0]} |")
    A("")
    for n, (k, et) in enumerate(ORDEN, 1):
        c = C[k]
        A(f"## {n}. {et} — {c['estado']}")
        A("")
        A("Artefactos:")
        A("")
        for a in c["artefactos"]:
            A(f"- {a}")
        A("")
        if c["extracto"]:
            A("Extracto:")
            A("")
            for x in c["extracto"]:
                A(f"- {x}")
            A("")
        A(f"**Lo que muestra el ejemplo:** {c['hecho']}")
        if c.get("control"):
            A("")
            A(f"Control: {c['control']}.")
        A("")

    # dependencias con las figuras
    d = R["datos"]
    el = d["extractor_lineas"]
    t0 = R["t0dev"]
    A(f"## {len(ORDEN) + 1}. Dependencias con las figuras")
    A("")
    A(f"Las cuatro figuras del ejemplo leen `{DATOS}` (sha256 `{d['sha']}`), que escribe "
      f"`{EXTRACTOR}` (sha256 `{d['extractor_sha']}`). Las otras figuras de `{FIG}/` no usan el "
      "ejemplo. Los LEEME tienen cambios sin commit desde antes de esta unidad; se leyó el "
      "working tree (sha256 abajo).")
    A("")
    A("| figura | LEEME (sha256 del working tree) | datos del ejemplo que usa | candado |")
    A("|---|---|---|---|")
    A(f"| 1.1 norma a grafo | `{LEEME['1.1']}` (`{R['leeme']['1.1'][:12]}…`) | textos de 5.1.1, 5.1.1.1 y 3.7; "
      f"frase resaltada; 5 nodos; 4 aristas | `{GEN['1.1']}:{R['gen']['1.1']}` compara el sha de kg.json con el del JSON y "
      "cada nodo y arista contra kg.json |")
    A(f"| 1.2 fragmentos vs grafo | `{LEEME['1.2']}` (`{R['leeme']['1.2'][:12]}…`) | pregunta; textos; puestos "
      "2 y 1.523 y top-5 de BM25; nodos y aristas | `" + GEN["1.2"] + f":{R['gen']['1.2']}` importa la carga "
      f"de 1.1; con `--verificar-busqueda`, `:{R['gen']['1.2_insumos']}` exige el sha de los cinco "
      "chunks_*.json y los puestos |")
    A(f"| 1.3 proceso de extracción | `{LEEME['1.3']}` (`{R['leeme']['1.3'][:12]}…`) | 3 nodos (restricción "
      f"del monto, obligación del 3.7, operación); aristas 15772 y 15773 | `{GEN['1.3']}:{R['gen']['1.3']}` "
      "(KG_SHA256 fijo) |")
    A(f"| 2.1 tripleta | `{LEEME['2.1']}` (`{R['leeme']['2.1'][:12]}…`) | 2 nodos (restricción del monto, "
      f"operación); arista 15772 | `{GEN['2.1']}:{R['gen']['2.1']}` (KG_SHA256 fijo) |")
    A("")
    A("En el extractor, los candados son: el sha256 de r1 "
      f"(`{EXTRACTOR}:{el['kg']}`); la ruta de E0 `salida_enm01` (`:{el['chunks']}`); los nodos "
      f"buscados por tipo y etiqueta literal (`:{el['nodos']}`); las aristas por "
      f"(origen, relación, destino) (`:{el['aristas']}`); los puestos esperados de BM25 "
      f"(`:{el['rangos']}`); y el sha de los resultados de U-MED-EJEMPLO-2 (`:{el['paquete']}`).")
    A("")
    A("**Qué cambiaría después de U-REEXT-T0.** El mandato de U-REEXT-T0 es NO ENCONTRADO en "
      "`docs/mandatos/` al redactar esto; su alcance está en `docs/plan_tesis.md:399` (HEAD "
      "`ded3494`): E0 a E5 de los diez TOs con el prefijo nuevo, sobre el corpus congelado. Hechos:")
    A("")
    A(f"- Las figuras leen r1 por ruta y sha fijos (`{EXTRACTOR}:{el['kg_ruta']}-{el['kg']}`): "
      "U-REEXT-T0 no las cambia por sí mismo, porque r1 está sellado y no se reescribe. Para "
      "mostrar el grafo nuevo hay que re-apuntar el extractor; entonces fallan por diseño el "
      "candado de sha, la búsqueda por etiqueta literal y los índices de arista, que son salida "
      "de la extracción y del ensamblado de r1.")
    A(f"- El único grafo existente con el esquema congelado sobre esos dos puntos es "
      f"KG-Tanda0-Desarrollo-r1 (`{KG_T0DEV}`, `{t0['sha'][:12]}…`, prompt v3; no es U-REEXT-T0). "
      f"Allí los nodos de contenido son: "
      + "; ".join(f"{cid} {tipo} «{lab}»" for cid, tipo, lab, _ in t0["nodos"])
      + f". No hay Restriccion ni `limita`; aristas `referencia` de 5.1.1.1 hacia 3.7: "
        f"{t0['ref_511_37']}; Condicion del ejemplo sin ninguna arista: {t0['cond_sin_aristas']} de "
        f"{sum(1 for x in t0['nodos'] if x[1] == 'Condicion')}. Con ese grafo, las figuras 1.1, 1.3 y "
        "2.1 (Restriccion, `limita` y `referencia`) no se reproducen. Ya está registrado en "
        "`docs/laudo_release_r2_pipeline.md:332` (Condicion sin aristas) y `:334` (el ejemplo "
        "como test de la suite, que hoy daría «persiste» en ese grafo), en HEAD `ded3494`.")
    A("- Los textos y la búsqueda BM25 salen de los cinco chunks_*.json de `salida_enm01`, por "
      "ruta fija. Los puestos 2 y 1.523 dependen de los 1.763 fragmentos (idf y largo medio): "
      "si U-REEXT-T0 cambia algún fragmento de los cinco TOs y las figuras pasan a leer esa "
      "salida, los puestos se recalculan.")
    A("- Las trazas del agente, el Paso 2 y el Paso 3 de U-MED-EJEMPLO-2 son de r1 y no se "
      "rehacen. La figura 1.2 no dibuja una traza del agente: lo declara "
      f"`{LEEME['1.2']}:{R['leeme_1_2_no_traza']}` (working tree).")
    A("")
    A(f"## {len(ORDEN) + 2}. Fuentes (sha256)")
    A("")
    A("| archivo | sha256 |")
    A("|---|---|")
    for k, v in R["fuentes"].items():
        A(f"| `{k}` | `{v}` |")
    A("")
    A(f"La caché `{DB_REINT}` no está en git (`{GITIGNORE_E3}:1`) y cambia con corridas "
      "posteriores; se cita por la key de la fila, no por el sha del archivo.")
    A("")
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out-dir", default=str(AQUI))
    args = ap.parse_args()
    R = recorrido()
    salida = Path(args.out_dir) / "recorrido_prestamo.md"
    salida.write_text(md(R), encoding="utf-8")
    print("componentes:", {k: v["estado"] for k, v in R["comp"].items()})
    return 0


if __name__ == "__main__":
    sys.exit(main())
