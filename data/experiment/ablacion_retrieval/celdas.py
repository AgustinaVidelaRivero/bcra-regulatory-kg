"""
celdas.py — Las CUATRO celdas de la ablación factorial 2×2 sobre KG-Refinado,
construidas por import desde las piezas selladas y escritas a `celdas/` con su
sha256 (pre-registro §1). Cero API, cero Neo4j: acá solo se arman los TEXTOS que
verá el modelo (prompt del sistema + specs de tools) y la declaración del backend
de cada tool por celda; A1.4 los carga desde estos JSON y aborta si su sha no
coincide con el sellado en `preregistro_ablacion.md`.

Factores (cada uno es un PAQUETE {función + spec + línea de prompt}, nunca tres
factores sueltos — laudo de cierre de U-A1.2):

  R = retriever de `buscar_nodos`:
      booleano = `Neo4jIndex(modo='paridad').buscar_nodos` (réplica byte-idéntica
                 del `GraphIndex.buscar_nodos` del harness, 322/322 en A1.1)
                 + spec `harness.TOOLS['buscar_nodos']` + línea 1 del prompt harness.
      bm25     = `Neo4jIndex(modo='fulltext').buscar_nodos` (= `ToolsV2.buscar_nodos_v2`)
                 + spec `specs_tools_v2.json['buscar_nodos']` + línea 1 del prompt v2.
  T = tools de navegación (`ver_vecinos`; `ver_nodo` es byte-idéntico en todas):
      v1 = `Neo4jIndex.ver_vecinos(id, direccion)` (byte-idéntico al harness)
           + spec `harness.TOOLS['ver_vecinos']` + línea 3 del prompt harness.
      v2 = `ToolsV2.ver_vecinos_v2(id, relacion, pagina, por_pagina)`
           + spec `specs_tools_v2.json['ver_vecinos']` + línea 3 del prompt v2.

Invariantes verificados acá (fallan ruidosamente):
  - {booleano, v1} == harness VERBATIM (prompt y TOOLS byte a byte);
  - {bm25, v2}     == paquete sellado de A1.2 VERBATIM (SYSTEM_PROMPT_V2_PROPUESTO
                      y TOOLS_V2 byte a byte);
  - las dos líneas de prompt son EXACTAMENTE `agente_v2._REEMPLAZOS_PROMPT`
    (importadas, no re-tipeadas), aplicadas de a una por factor;
  - `ver_nodo` es idéntica en harness.TOOLS y TOOLS_V2;
  - el orden de las specs es el del harness (buscar_nodos, ver_nodo, ver_vecinos).

Uso:  python3 -B celdas.py         (escribe celdas/celda_*.json y celdas/manifest_celdas.json)
      python3 -B celdas.py --check (recomputa y compara contra lo escrito; exit 1 si difiere)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun_ablacion import (CELDAS_DIR, KG_REFINADO_SHA256, PIEZAS_SELLADAS,  # noqa: E402
                            rel_repo, verificar_piezas)

from harness import (MAX_TOKENS, MAX_TOOL_CALLS, MODEL, SYSTEM_PROMPT,  # noqa: E402
                     TEMPERATURE, TOOLS)
from agente_v2 import _REEMPLAZOS_PROMPT, SYSTEM_PROMPT_V2_PROPUESTO  # noqa: E402
from tools_v2 import (LIMITE_DEFAULT, POR_PAGINA_DEFAULT, POR_PAGINA_MAX,  # noqa: E402
                      TOOLS_V2)
from indices import ANALYZER, CAMPOS_FULLTEXT  # noqa: E402  (neo4j, A1.1)

GRAFO = "KG_Refinado"          # clave de neo4j/grafos.py (nombre canónico KG-Refinado)

# id de celda -> (retriever, tools)
CELDAS = {
    "C00_booleano_v1": ("booleano", "v1"),   # CONTROL: harness verbatim
    "C10_bm25_v1":     ("bm25", "v1"),
    "C01_booleano_v2": ("booleano", "v2"),
    "C11_bm25_v2":     ("bm25", "v2"),       # paquete sellado de A1.2 verbatim
}
ORDEN_CELDAS = list(CELDAS)      # orden de corrida pre-registrado (§4)


def _sha_texto(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _sha_json(obj) -> str:
    return _sha_texto(json.dumps(obj, ensure_ascii=False, sort_keys=True))


def _por_nombre(specs: list) -> dict:
    return {s["name"]: s for s in specs}


def _aplicar(prompt: str, reemplazo: tuple[str, str]) -> str:
    """Aplica UNA sustitución de agente_v2._REEMPLAZOS_PROMPT (misma regla que
    agente_v2._prompt_propuesto: el patrón debe aparecer exactamente una vez)."""
    viejo, nuevo = (x.replace("\\\n", "") for x in reemplazo)
    n = prompt.count(viejo)
    if n != 1:
        raise RuntimeError(f"la frase esperada aparece {n} veces: {viejo!r}")
    return prompt.replace(viejo, nuevo)


def construir_celda(celda_id: str) -> dict:
    retriever, tools = CELDAS[celda_id]
    v1, v2 = _por_nombre(TOOLS), _por_nombre(TOOLS_V2)
    assert list(v1) == ["buscar_nodos", "ver_nodo", "ver_vecinos"] == list(v2)
    assert v1["ver_nodo"] == v2["ver_nodo"], "ver_nodo debería ser idéntica v1/v2"

    prompt = SYSTEM_PROMPT
    if retriever == "bm25":
        prompt = _aplicar(prompt, _REEMPLAZOS_PROMPT[0])   # línea buscar_nodos
    if tools == "v2":
        prompt = _aplicar(prompt, _REEMPLAZOS_PROMPT[1])   # línea ver_vecinos

    specs = [
        (v2 if retriever == "bm25" else v1)["buscar_nodos"],
        v1["ver_nodo"],
        (v2 if tools == "v2" else v1)["ver_vecinos"],
    ]
    backend = {
        "grafo": GRAFO,
        "kg_sha256": KG_REFINADO_SHA256,
        "buscar_nodos": ("Neo4jIndex(driver, grafo='KG_Refinado', modo='paridad').buscar_nodos(consulta, limite)"
                         if retriever == "booleano" else
                         "Neo4jIndex(driver, grafo='KG_Refinado', modo='fulltext').buscar_nodos(consulta, limite)"
                         "  [= ToolsV2.buscar_nodos_v2]"),
        "ver_nodo": "Neo4jIndex.ver_nodo(id)  [byte-idéntico al harness en ambos modos]",
        "ver_vecinos": ("Neo4jIndex.ver_vecinos(id, direccion='ambas')  [byte-idéntico al harness]"
                        if tools == "v1" else
                        "ToolsV2.ver_vecinos_v2(id, relacion=None, pagina=1, por_pagina=40)"),
        "clase_agente_A1_4": ("subclase de agente_v2.GraphAgentV2 con system_prompt/tools de ESTA celda "
                              "y _run_tool despachando según 'buscar_nodos'/'ver_vecinos' de arriba; "
                              "ask = copia verificada del harness (2 sustituciones)"),
        "replay_A1_4": ("celdas v1: metrica.evaluar_por_anclas con index=Neo4jIndex(modo) sin cambios; "
                        "celdas v2: mismo evaluar_por_anclas con re-ejecutor v2-aware inyectado por atributo "
                        "de módulo (metrica._reejecutar_step) — metrica.py no se edita"),
    }
    celda = {
        "celda_id": celda_id,
        "retriever": retriever,
        "tools": tools,
        "es_control": celda_id == "C00_booleano_v1",
        "es_paquete_A1_2_verbatim": celda_id == "C11_bm25_v2",
        "modelo_agente": {"model": MODEL, "temperature": TEMPERATURE, "max_tokens": MAX_TOKENS,
                          "max_tool_calls": MAX_TOOL_CALLS},
        "retriever_config": {
            "booleano": {"campos": ["label", "id"], "score": "|tokens(consulta) ∩ tokens(label+id)|",
                         "orden": "(-score, len(label), id)", "limite_default": LIMITE_DEFAULT,
                         "clamp_limite": "1..50; no entero -> 10"},
            "bm25": {"campos": CAMPOS_FULLTEXT, "analyzer": ANALYZER,
                     "score": "BM25 Lucene (db.index.fulltext.queryNodes), score no expuesto",
                     "orden": "score DESC, size(label) ASC, id ASC",
                     "limite_default": LIMITE_DEFAULT, "clamp_limite": "1..50; no entero -> 10",
                     "indice": "nodos_fulltext_kg_refinado (uno por grafo)"},
        }[retriever],
        "ver_vecinos_config": {
            "v1": {"firma": "(id, direccion='ambas')", "ventana": 40, "paginacion": False,
                   "filtro_relacion": False},
            "v2": {"firma": "(id, relacion=None, pagina=1, por_pagina=40)",
                   "por_pagina_default": POR_PAGINA_DEFAULT, "por_pagina_max": POR_PAGINA_MAX,
                   "bidireccional_siempre": True, "paginacion": "offset sobre r.orden",
                   "filtro_relacion": True},
        }[tools],
        "backend": backend,
        "system_prompt": prompt,
        "system_prompt_sha256": _sha_texto(prompt),
        "tools_specs": specs,
        "tools_specs_sha256": _sha_json(specs),
    }
    return celda


def construir_todas() -> dict[str, dict]:
    celdas = {cid: construir_celda(cid) for cid in ORDEN_CELDAS}
    # Invariantes de esquina (verbatim)
    c00, c11 = celdas["C00_booleano_v1"], celdas["C11_bm25_v2"]
    assert c00["system_prompt"] == SYSTEM_PROMPT
    assert c00["tools_specs"] == TOOLS
    assert c11["system_prompt"] == SYSTEM_PROMPT_V2_PROPUESTO
    assert c11["tools_specs"] == TOOLS_V2
    # Los 4 prompts y los 4 juegos de specs son distintos entre sí
    assert len({c["system_prompt_sha256"] for c in celdas.values()}) == 4
    assert len({c["tools_specs_sha256"] for c in celdas.values()}) == 4
    return celdas


def manifest(celdas: dict[str, dict]) -> dict:
    return {
        "unidad": "U-A1.3",
        "grafo": {"clave": GRAFO, "nombre_canonico": "KG-Refinado", "kg_sha256": KG_REFINADO_SHA256},
        "orden_celdas": ORDEN_CELDAS,
        "piezas_selladas": {n: {"path": rel_repo(p), "sha256": s} for n, (p, s) in PIEZAS_SELLADAS.items()},
        "harness_system_prompt_sha256": _sha_texto(SYSTEM_PROMPT),
        "harness_tools_sha256": _sha_json(TOOLS),
        "prompt_v2_propuesto_sha256": _sha_texto(SYSTEM_PROMPT_V2_PROPUESTO),
        "tools_v2_sha256": _sha_json(TOOLS_V2),
        "lineas_prompt_A1_2": [
            {"factor": "retriever(bm25)", "vieja": _REEMPLAZOS_PROMPT[0][0].replace("\\\n", ""),
             "nueva": _REEMPLAZOS_PROMPT[0][1].replace("\\\n", "")},
            {"factor": "tools(v2)", "vieja": _REEMPLAZOS_PROMPT[1][0].replace("\\\n", ""),
             "nueva": _REEMPLAZOS_PROMPT[1][1].replace("\\\n", "")},
        ],
        "celdas": {
            cid: {"retriever": c["retriever"], "tools": c["tools"],
                  "system_prompt_sha256": c["system_prompt_sha256"],
                  "tools_specs_sha256": c["tools_specs_sha256"],
                  "archivo": f"celdas/celda_{cid}.json"}
            for cid, c in celdas.items()
        },
    }


def escribir(celdas: dict[str, dict]) -> dict:
    CELDAS_DIR.mkdir(parents=True, exist_ok=True)
    for cid, c in celdas.items():
        with (CELDAS_DIR / f"celda_{cid}.json").open("w", encoding="utf-8") as f:
            json.dump(c, f, ensure_ascii=False, indent=1)
    m = manifest(celdas)
    for cid in m["celdas"]:
        m["celdas"][cid]["archivo_sha256"] = hashlib.sha256(
            (CELDAS_DIR / f"celda_{cid}.json").read_bytes()).hexdigest()
    with (CELDAS_DIR / "manifest_celdas.json").open("w", encoding="utf-8") as f:
        json.dump(m, f, ensure_ascii=False, indent=1)
    return m


def check() -> int:
    """Recomputa desde las piezas y compara con lo escrito en celdas/."""
    celdas = construir_todas()
    ok = True
    for cid, c in celdas.items():
        p = CELDAS_DIR / f"celda_{cid}.json"
        if not p.exists():
            print(f"FALTA {p}"); ok = False; continue
        with p.open(encoding="utf-8") as f:
            escrito = json.load(f)
        mismo = (escrito["system_prompt"] == c["system_prompt"]
                 and escrito["tools_specs"] == c["tools_specs"]
                 and escrito["backend"] == c["backend"])
        print(f"  {'OK ' if mismo else 'DIF'} {cid}  prompt {c['system_prompt_sha256'][:12]}…  "
              f"specs {c['tools_specs_sha256'][:12]}…")
        ok = ok and mismo
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    print("piezas selladas:")
    verificar_piezas()
    if args.check:
        return check()
    celdas = construir_todas()
    m = escribir(celdas)
    print("\nceldas escritas en", rel_repo(CELDAS_DIR))
    for cid, info in m["celdas"].items():
        print(f"  {cid:18s} R={info['retriever']:8s} T={info['tools']}  prompt {info['system_prompt_sha256'][:16]}…  "
              f"specs {info['tools_specs_sha256'][:16]}…  archivo {info['archivo_sha256'][:16]}…")
    print(f"harness prompt {m['harness_system_prompt_sha256'][:16]}… == C00 ; "
          f"v2 propuesto {m['prompt_v2_propuesto_sha256'][:16]}… == C11")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
