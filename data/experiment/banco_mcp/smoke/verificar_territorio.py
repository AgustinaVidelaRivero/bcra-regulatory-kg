#!/usr/bin/env python3
"""verificar_territorio.py — Chequeo de territorio (principio 7) para las anclas de
las preguntas propias del banco (U-A2.0-banco). El territorio se quema POR ANCLA,
no por texto: una pregunta nueva sobre un ancla del gold de EV2 es material quemado.

Fuentes quemadas (se leen SOLO los campos de ancla; nunca las preguntas ni los
criterios):
  (a) gold de fidelidad EV2: exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json
      (`preguntas[*].gold.ancla`, forma "to:punto")
  (b) pares sintéticos de EV2 (navegabilidad): exploracion/sinteticas/out/
      preguntas_faseB.json (`registros[*].gold.anclas[*].{to,ancla}`; ruta
      FASEB_JSON de ev2_corrida/code/comun_ev2.py) y su población
      exploracion/sinteticas/out/samples.json (`samples[*].gold.anclas`)
  (c) pares v3 de la ablación: ablacion_retrieval/pares/pares_v3.json
      (`pares[*].gold.anclas[*].{to,ancla}`)

Criterio, por ancla candidata `to:p`:
  · solape EXACTO: `to:p` está en alguna fuente;
  · solape por PREFIJO de punto: existe `to:q` quemada con q == p, q prefijo de p
    (q + "." ⊂ p) o p prefijo de q (p + "." ⊂ q) — es decir, misma rama del
    punto en cualquiera de las dos direcciones.
Resultado: 0 solapes requeridos para usar el ancla. El mismo chequeo vale para
cualquier pregunta futura del banco.

Uso:
  python3 -B verificar_territorio.py [--preguntas preguntas_smoke.json] [--escribir]
  python3 -B verificar_territorio.py --candidatas        # lista anclas del KG libres de solape
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
EXPERIMENT_DIR = BANCO_DIR.parent
if str(BANCO_DIR) not in sys.path:
    sys.path.insert(0, str(BANCO_DIR))
from comun_banco import rel_repo, sha256_file  # noqa: E402

FUENTES = {
    "a_gold_fidelidad_ev2": EXPERIMENT_DIR / "exploracion" / "ev2_fidelidad" / "preguntas_ev2_fidelidad.json",
    "b_pares_sinteticos_ev2": EXPERIMENT_DIR / "exploracion" / "sinteticas" / "out" / "preguntas_faseB.json",
    "b_poblacion_sinteticas": EXPERIMENT_DIR / "exploracion" / "sinteticas" / "out" / "samples.json",
    "c_pares_v3_ablacion": EXPERIMENT_DIR / "ablacion_retrieval" / "pares" / "pares_v3.json",
}
KG = EXPERIMENT_DIR / "grafo_v2" / "reensamblado_v3" / "kg.json"
TO_DE_DOC = {"TO_capitales_minimos_actual.pdf": "cap", "TO_clasificacion_deudores_actual.pdf": "cla",
             "TO_exterior_cambios_actual.pdf": "ext", "TO_proteccion_usuarios_servicios_financieros_actual.pdf": "pro",
             "TO_regimen_informativo_contable_mensual_actual.pdf": "ric"}


def anclas_quemadas() -> dict[str, set[str]]:
    """Solo campos de ancla. No se lee ningún texto de pregunta."""
    out: dict[str, set[str]] = {}
    d = json.loads(FUENTES["a_gold_fidelidad_ev2"].read_text(encoding="utf-8"))
    out["a_gold_fidelidad_ev2"] = {a for p in d["preguntas"] for a in (p["gold"]["ancla"] or [])}
    d = json.loads(FUENTES["b_pares_sinteticos_ev2"].read_text(encoding="utf-8"))
    out["b_pares_sinteticos_ev2"] = {f"{a['to']}:{a['ancla']}" for r in d["registros"] for a in r["gold"]["anclas"]}
    d = json.loads(FUENTES["b_poblacion_sinteticas"].read_text(encoding="utf-8"))
    out["b_poblacion_sinteticas"] = {f"{a['to']}:{a['ancla']}" for r in d["samples"] for a in r["gold"]["anclas"]}
    d = json.loads(FUENTES["c_pares_v3_ablacion"].read_text(encoding="utf-8"))
    out["c_pares_v3_ablacion"] = {f"{a['to']}:{a['ancla']}" for r in d["pares"] for a in r["gold"]["anclas"]}
    return out


def solapes(ancla: str, quemadas: dict[str, set[str]]) -> dict:
    to, p = ancla.split(":", 1)
    res = {}
    for fuente, S in quemadas.items():
        exacto = ancla in S
        prefijo = sorted(q for q in S if q.startswith(to + ":") and q != ancla and
                         (q.split(":", 1)[1].startswith(p + ".") or p.startswith(q.split(":", 1)[1] + ".")))
        res[fuente] = {"exacto": exacto, "por_prefijo": prefijo}
    return res


def n_solapes(r: dict) -> int:
    return sum((1 if v["exacto"] else 0) + len(v["por_prefijo"]) for v in r.values())


def candidatas(quemadas, minimo_nodos=3, maximo_nodos=10) -> list[dict]:
    """Anclas del KG-Refinado (to:punto numérico) sin solape, con n nodos en [mín, máx]."""
    kg = json.loads(KG.read_text(encoding="utf-8"))
    cuenta: dict[str, set[str]] = {}
    for n in kg["nodes"]:
        for pv in n.get("provenances", []):
            to = TO_DE_DOC.get(pv.get("source_doc", ""))
            m = re.match(r"Punto\s+(\d+(?:\.\d+)*)\.?", pv.get("location", ""))
            if to and m:
                cuenta.setdefault(f"{to}:{m.group(1)}", set()).add(n["id"])
    out = []
    for a, ids in sorted(cuenta.items()):
        if minimo_nodos <= len(ids) <= maximo_nodos and n_solapes(solapes(a, quemadas)) == 0:
            out.append({"ancla": a, "n_nodos": len(ids)})
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--preguntas", type=Path, default=AQUI / "preguntas_smoke.json")
    ap.add_argument("--escribir", action="store_true", help="persiste `verificacion_territorio` en el archivo de preguntas")
    ap.add_argument("--candidatas", action="store_true")
    a = ap.parse_args()
    q = anclas_quemadas()
    resumen_fuentes = {k: {"ruta": rel_repo(FUENTES[k]), "sha256": sha256_file(FUENTES[k]), "n_anclas": len(v)} for k, v in q.items()}
    if a.candidatas:
        for c in candidatas(q):
            print(c)
        return 0
    d = json.loads(a.preguntas.read_text(encoding="utf-8"))
    filas = []
    for p in d["preguntas"]:
        for an in p["anclas"]:
            r = solapes(an, q)
            filas.append({"id": p["id"], "ancla": an, "n_solapes": n_solapes(r), "detalle": r})
    total = sum(f["n_solapes"] for f in filas)
    ver = {"generado": datetime.now().isoformat(timespec="seconds"), "criterio": "por ancla exacta y por prefijo de punto (ambas direcciones)",
           "fuentes": resumen_fuentes, "anclas_chequeadas": filas, "total_solapes": total, "PASS": total == 0}
    for f in filas:
        print(f"{f['id']} {f['ancla']}: solapes={f['n_solapes']}" + ("" if f["n_solapes"] == 0 else
              "  <- " + "; ".join(f"{k}: exacto={v['exacto']} prefijo={v['por_prefijo']}" for k, v in f["detalle"].items() if v["exacto"] or v["por_prefijo"])))
    print("TOTAL solapes:", total, "->", "PASS" if total == 0 else "FAIL")
    if a.escribir:
        d["verificacion_territorio"] = ver
        a.preguntas.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
