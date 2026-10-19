"""
conteos_t2.py — B6.1, tanda final, T2: el desglose que el cegamiento de U-MED-VERIF no deja mirar (pre-registro firmado
de la tanda final, §4.1; pre-registro de la tanda 1, §7; despacho de T1 de la tanda final, punto 1.5). Es el de la tanda 1
(data/experiment/tanda1/t2/conteos_t2.py), con las rutas de la tanda final y sin otro cambio. USD 0, sin red.

Escribe en `data/experiment/tanda_final/t2/NO_ABRIR_conteos_reextracciones_tanda_final.json` (o en --out), por TO y en
total:
  - el desglose por estado de E3 (último expediente de cada unidad en finales.jsonl);
  - la distribución de `n_reintentos`;
  - los renglones de `reintentos_e3.jsonl` y de `copias_nota_e3.jsonl`;
  - las `marcas_e3` (reporte_e2_r2_<to>.json, stats.p3b.unidades_con_marca_e3; reext_t0/t2_contadores.py:215-223);
  - el gasto de E3 partido en el del verificador y el de los reintentos de E1 (resumen_e3.json, cliente_e3 y
    cliente_e1_reintentos, gasto_usd_real).
Imprime solo el sha256 del archivo y, para la vigilancia que usa esas cuentas, OK o FRENO:
  - integridad_e3: todo estado de finales.jsonl está en ratchet_e3.ESTADOS y, en cada TO con la fase de E3 cerrada,
    toda unidad aceptada en E1 tiene su expediente.
Las cifras de cierre que usan estas cuentas esperan al sello del diseño de U-MED-VERIF.

Uso: <python> -B conteos_t2.py --repo <raíz> [--salida <salida del runner>] [--out <json>]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
MANIFIESTO_REL = "data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json"
SALIDA_REL = "data/experiment/reextraccion_v2/corpus_tanda_final/salida_r2b"
OUT_REL = "data/experiment/tanda_final/t2/NO_ABRIR_conteos_reextracciones_tanda_final.json"
PARTICIONADA = "particionada_por_corte"


def last_wins(p: Path) -> dict[str, dict]:
    out = {}
    if p.exists():
        for x in p.read_text(encoding="utf-8").splitlines():
            if x.strip():
                r = json.loads(x)
                out[r["chunk_id"]] = r
    return out


def renglones(p: Path) -> int:
    return sum(1 for x in p.read_text(encoding="utf-8").splitlines() if x.strip()) if p.exists() else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--salida", type=Path, default=None)
    ap.add_argument("--out", type=Path, default=None)
    a = ap.parse_args()
    repo = a.repo.resolve()
    sys.path.insert(0, str(repo / "data" / "experiment" / "reextraccion_v2" / "e3_verificador"))
    sys.path.insert(0, str(repo / "data" / "experiment" / "evaluacion"))
    import ratchet_e3                       # noqa: PLC0415 — solo ESTADOS
    salida = (a.salida or repo / SALIDA_REL).resolve()
    out = (a.out or repo / OUT_REL).resolve()
    man = json.loads((repo / MANIFIESTO_REL).read_text(encoding="utf-8"))
    estado = json.loads((salida / "estado_corpus.json").read_text(encoding="utf-8")) \
        if (salida / "estado_corpus.json").exists() else {"fases_cerradas": {}}
    por_to, tot_estados, tot_nr, integridad = {}, Counter(), Counter(), []
    tot = Counter()
    for to in man["orden_corrida"]:
        tdir = salida / to
        fin = last_wins(tdir / "finales.jsonl")
        e1 = last_wins(tdir / "extracciones_e1.jsonl")
        estados = Counter(r["estado"] for r in fin.values())
        nr = Counter(str(r.get("n_reintentos")) for r in fin.values())
        rep = tdir / f"reporte_e2_r2_{to}.json"
        marcas = (json.loads(rep.read_text(encoding="utf-8"))["stats"].get("p3b") or {}).get("unidades_con_marca_e3") \
            if rep.exists() else None
        r3p = tdir / "resumen_e3.json"
        r3 = json.loads(r3p.read_text(encoding="utf-8")) if r3p.exists() else {}
        fuera = sorted(set(estados) - set(ratchet_e3.ESTADOS))
        sin_exp = []
        if f"{to}:e3" in estado["fases_cerradas"]:
            sin_exp = sorted(cid for cid, r in e1.items() if r.get("error") is None and cid not in fin)
        integridad.append(not fuera and not sin_exp)
        por_to[to] = {"estados_e3": dict(sorted(estados.items())), "n_reintentos": dict(sorted(nr.items())),
                      "renglones_reintentos_e3": renglones(tdir / "reintentos_e3.jsonl"),
                      "renglones_copias_nota_e3": renglones(tdir / "copias_nota_e3.jsonl"),
                      "marcas_e3": marcas,
                      "gasto_verificador_e3_usd": (r3.get("cliente_e3") or {}).get("gasto_usd_real"),
                      "gasto_reintentos_e1_usd": (r3.get("cliente_e1_reintentos") or {}).get("gasto_usd_real"),
                      "estados_fuera_del_vocabulario": fuera, "aceptadas_en_e1_sin_expediente": sin_exp}
        tot_estados.update(estados)
        tot_nr.update(nr)
        tot["renglones_reintentos_e3"] += por_to[to]["renglones_reintentos_e3"]
        tot["renglones_copias_nota_e3"] += por_to[to]["renglones_copias_nota_e3"]
    res = {"salida": str(salida.relative_to(repo)) if salida.is_relative_to(repo) else "<salida fuera del repo>",
           "por_to": por_to, "total": {"estados_e3": dict(sorted(tot_estados.items())),
                                       "n_reintentos": dict(sorted(tot_nr.items())), **tot}}
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("sha256", hashlib.sha256(out.read_bytes()).hexdigest())
    print("vigilancia integridad_e3:", "OK" if all(integridad) else "FRENO")
    return 0


if __name__ == "__main__":
    sys.exit(main())
