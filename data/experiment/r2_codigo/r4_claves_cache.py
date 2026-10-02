"""U-R2-CODIGO, R4.b — control nuevo de `BKL-0030`: con los perfiles existentes
(`produccion_dev` y `v3_b54`), la clave de caché de una muestra fija de
requests de E1 y de E3 es idéntica a la de hoy. Sin API. USD 0.

La clave es sha256(namespace + request canónico) (`llm_cache.compute_key` y
`canonical_request`). Este script arma los requests con el código del pipeline
de la raíz `--raiz-codigo` y lee los datos (E0, salidas de E1 y E3) del repo.
Se corre dos veces, con el código de hoy (el árbol de trabajo) y con el de HEAD
exportado (`git archive`), y las dos salidas tienen que ser byte a byte iguales.

Muestra, declarada antes de correr (semilla 20261002, `random.Random`, sobre
los chunk_id ordenados):
  - por perfil, 20 unidades de E0 para el primer intento de E1 y, de esas, las
    aceptadas por E1 para la primera verificación de E3;
  - los reintentos por corte de E1 de los tres casos del laudo de r2, §1.1
    (`cap::3.1.14.1`, `cap::4.2.1.2`, `cap::4.3.3.1`), con el techo de los
    perfiles existentes (en las salidas guardadas no hay registros con
    `reintento_corte`: en r1 cortaron sin reintento y en la tanda 0 la guarda
    del SDK rechazó el reintento);
  - 10 reintentos del ratchet de E3 (unidades de finales.jsonl con
    `n_reintentos`), con el request reconstruido como
    `runner_corpus.claves_reintentos_cache`.
Corridas: `produccion_dev` = KG-Reextraído (E0 `salida_enm01`, salidas en
`corpus_v2/salida`); `v3_b54` = tanda 0 (E0 `salida_tanda0`, salidas en
`corpus_tanda0/salida_dirigida`). Anclaje informativo: cuántas claves están en
las dbs de caché (solo lectura, immutable=1).

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/r4_claves_cache.py --out <json> \
      [--raiz-codigo <raíz con el código a usar; por defecto, el repo>]
"""

from __future__ import annotations

import argparse
import ast
import json
import random
import sqlite3
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SEMILLA = 20261002
N_E1 = 20
N_RATCHET = 10
CORRIDAS = {
    "produccion_dev": {"e0": "data/experiment/reextraccion_v2/e0_chunking/salida_enm01",
                       "salida": "data/experiment/reextraccion_v2/corpus_v2/salida",
                       "tos": ("pro", "cla", "ric", "cap", "ext")},
    "v3_b54": {"e0": "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0",
               "salida": "data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida",
               "tos": ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")},
}
DBS = {"e1": "data/experiment/reextraccion_v2/e1_extractor/cache/e1_extraccion.db",
       "e1_reintentos": "data/experiment/reextraccion_v2/e3_verificador/cache/e1_reintentos.db",
       "e3": "data/experiment/reextraccion_v2/e3_verificador/cache/e3_verificacion.db"}


def importar(raiz: Path):
    rex = raiz / "data" / "experiment" / "reextraccion_v2"
    for p in (raiz / "data" / "experiment" / "evaluacion", rex / "e2_reduce", rex / "e3_verificador",
              rex / "e1_extractor", rex):
        sys.path.insert(0, str(p))
    import llm_cache as lc
    import perfil_e1
    import cliente_e1
    import prompt_e3
    import cliente_e3
    import ratchet_e3
    import comun_e3
    arbol = ast.parse((rex / "corpus_v2" / "runner_corpus.py").read_text(encoding="utf-8"))
    k = {n.targets[0].id: ast.literal_eval(n.value) for n in arbol.body
         if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)
         and n.targets[0].id in ("MODEL_E1", "MODEL_E3", "MAX_TOKENS_REINTENTO")}
    return lc, perfil_e1, cliente_e1, prompt_e3, cliente_e3, ratchet_e3, comun_e3, k


def jsonl(p: Path) -> dict[str, dict]:
    out = {}
    if p.exists():
        for l in p.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l)
                out[r["chunk_id"]] = r
    return out


def claves_db(rel: str, ns: str) -> set | None:
    p = REPO / rel
    if not p.exists():
        return None
    con = sqlite3.connect("file:" + str(p.resolve()) + "?mode=ro&immutable=1", uri=True)
    try:
        return {k for (k,) in con.execute("SELECT key FROM cache WHERE namespace = ?", (ns,))}
    finally:
        con.close()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--raiz-codigo", type=Path, default=REPO)
    a = ap.parse_args()
    lc, perfil_e1, cliente_e1, prompt_e3, cliente_e3, ratchet_e3, comun_e3, k = importar(a.raiz_codigo.resolve())
    clave = lambda ns, kw: lc.compute_key(ns, lc.canonical_request(kw))  # noqa: E731
    out: dict = {"semilla": SEMILLA, "constantes": {**k, "MAX_TOKENS_REINTENTO_CORTE": cliente_e1.MAX_TOKENS_REINTENTO_CORTE},
                 "perfiles": {}}
    anclaje: dict = {}
    for nombre, cfg in CORRIDAS.items():
        pf = perfil_e1.perfil(nombre)
        ns1 = cliente_e1.namespace_e1(prefijo_hash=pf.prefijo_hash_para_namespace)
        ns3 = cliente_e3.namespace_e3()
        chunks = {c["id"]: c for to in cfg["tos"]
                  for c in json.loads((REPO / cfg["e0"] / f"chunks_{to}.json").read_text(encoding="utf-8"))}
        unidades = {c["unidad"] for c in chunks.values()}
        regs, fin, ver = {}, {}, {}
        for to in cfg["tos"]:
            regs.update(jsonl(REPO / cfg["salida"] / to / "extracciones_e1.jsonl"))
            fin.update(jsonl(REPO / cfg["salida"] / to / "finales.jsonl"))
            p = REPO / cfg["salida"] / to / "veredictos.jsonl"
            for l in p.read_text(encoding="utf-8").splitlines() if p.exists() else []:
                r = json.loads(l)
                if r["fase"] == "verificacion":
                    ver[r["chunk_id"]] = r
        rnd = random.Random(SEMILLA)
        muestra = sorted(rnd.sample(sorted(chunks), N_E1))
        build = lambda c, **kw: pf.build_request_kwargs(c, model=k["MODEL_E1"], **kw)  # noqa: E731
        e1 = {cid: clave(ns1, build(chunks[cid])) for cid in muestra}
        e3 = {cid: clave(ns3, prompt_e3.build_request_kwargs(chunks[cid], regs[cid]["validacion"], model=k["MODEL_E3"]))
              for cid in muestra if cid in regs and comun_e3.chunk_aceptado(regs[cid])}
        cortes = ["cap::3.1.14.1", "cap::4.2.1.2", "cap::4.3.3.1"]
        e1c = {cid: clave(ns1, {**build(chunks[cid]), "max_tokens": cliente_e1.MAX_TOKENS_REINTENTO_CORTE})
               for cid in cortes}
        con_ratchet = sorted(cid for cid, f in fin.items() if f.get("n_reintentos") and cid in chunks and cid in ver)
        muestra_r = sorted(rnd.sample(con_ratchet, min(N_RATCHET, len(con_ratchet))))
        rat = {}
        for cid in muestra_r:
            ev = ratchet_e3.evaluar_veredicto(ver[cid]["tool_input"], chunks[cid], unidades)
            kw = ratchet_e3.build_reextraccion_kwargs(chunks[cid], ev["bloqueantes_utilizables"], model=k["MODEL_E1"],
                                                      intento=1, max_tokens_reintento=k["MAX_TOKENS_REINTENTO"],
                                                      perfil=None if nombre == "produccion_dev" else pf)
            rat[cid] = clave(ns1, kw)
        out["perfiles"][nombre] = {"namespace_e1": ns1, "namespace_e3": ns3, "e1_primer_intento": e1,
                                   "e3_verificacion": e3, "e1_reintento_corte": e1c, "e3_reintento_ratchet": rat}
        db1, dbr, db3 = claves_db(DBS["e1"], ns1), claves_db(DBS["e1_reintentos"], ns1), claves_db(DBS["e3"], ns3)
        anclaje[nombre] = {
            "e1_primer_intento_en_db": None if db1 is None else sum(v in db1 for v in e1.values()),
            "e1_reintento_corte_en_db": None if db1 is None else sum(v in db1 for v in e1c.values()),
            "e3_verificacion_en_db": None if db3 is None else sum(v in db3 for v in e3.values()),
            "e3_reintento_ratchet_en_db": None if dbr is None else sum(v in dbr for v in rat.values()),
            "tamanos": {"e1": len(e1), "e3": len(e3), "cortes": len(e1c), "ratchet": len(rat)}}
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(anclaje, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
