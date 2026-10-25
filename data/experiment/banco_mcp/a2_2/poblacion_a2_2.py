#!/usr/bin/env python3
"""poblacion_a2_2.py — La población de N = 3 de A2.2 y la agregación de sus re-corridas (pre-registro FIRMADO, a78ead7b, §4):

  · el disparo: va a N = 3 un par (pregunta, brazo) cuyo veredicto del código en N = 1 es «parcial» (protocolo de EV2,
    `:104-108`; A-D8: una `requiere_adjudicacion` no dispara y se adjudica al final);
  · la auditoría: de los «correcto» de N = 1 de cada brazo, max(ceil(10 % · n), 1), con `random.Random("A22:auditoria:v1")
    .sample` sobre los ids ordenados y un generador nuevo por brazo (`ev2_encadenamiento/code/comun_enc.py:177-190`, con la
    semilla de A2.2; A-D7 y A-D10). Un brazo sin «correcto» no tiene auditoría;
  · la agregación de las tres re-corridas: `ev2_encadenamiento/code/agregacion_enc.py`, importado sin editar (mayoría, empate
    triple a parcial, la base no vota; con un voto `requiere_adjudicacion`, el par queda decidido solo si el resultado no depende
    de cómo se resuelva).
Los veredictos por par salen de los agregados ciegos del juez y de su tabla id opaco → (pregunta, brazo, repetición).

Uso:
  .venv/bin/python -B data/experiment/banco_mcp/a2_2/poblacion_a2_2.py --calcular      # después del juez de N = 1
Imprime solo cuántos pares y sesiones lleva la población, sin veredictos ni brazos.
"""
from __future__ import annotations

import argparse
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
for _p in (str(AQUI), str(AQUI.parents[1] / "ev2_encadenamiento" / "code")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import comun_a2_2 as K                        # noqa: E402
import agregacion_enc as AG                   # noqa: E402  (EV2: solo import)

DISPARADOR = "parcial"


def veredictos_por_par(juez_dir: Path, etapa: str) -> dict:
    """{(qid, brazo, rep): agregado} desde agregados_<etapa>_ciego.json y la tabla de desanonimización de la etapa."""
    agg = json.loads((juez_dir / etapa / f"agregados_{etapa}_ciego.json").read_text(encoding="utf-8"))
    tab = json.loads((juez_dir / etapa / "desanonimizacion_SOLO_MESA" / f"tabla_id_opaco_{etapa}_SOLO_MESA.json")
                     .read_text(encoding="utf-8"))
    fila = {f["id_opaco"]: f for f in tab["filas"]}
    out = {}
    for a in agg["agregados"]:
        f = fila[a["id_opaco"]]
        k = (f["qid"], f["brazo"], f["rep"])
        if k in out:
            raise K.FrenoA22("un par (pregunta, brazo, repetición) con dos respuestas agregadas")
        out[k] = a
    return out


def muestra_auditoria(correctos_por_brazo: dict[str, list[str]], semilla: str = K.SEMILLA_AUDITORIA) -> dict[str, list[str]]:
    """max(ceil(10 % · n), 1) de los ids «correcto» de cada brazo, random.Random(semilla).sample sobre los ids ordenados, con un
    generador nuevo por brazo: la muestra de un brazo no depende de la de otro (comun_enc.py:177-190)."""
    out = {}
    for b in sorted(correctos_por_brazo):
        ids = sorted(correctos_por_brazo[b])
        if not ids:
            out[b] = []
            continue
        k = max(math.ceil(K.FRACCION_AUDITORIA * len(ids)), K.MINIMO_AUDITORIA)
        out[b] = sorted(random.Random(semilla).sample(ids, k))
    return out


def derivar(veredictos_n1: dict, preguntas_ids: list[str]) -> dict:
    """La población de N = 3 desde los veredictos de N = 1: [{qid, brazo, tipo}] y las cuentas por brazo."""
    base = {(q, b): veredictos_n1[(q, b, 1)]["veredicto_pregunta"] for (q, b, r) in veredictos_n1 if r == 1}
    parciales = sorted((q, b) for (q, b), v in base.items() if v == DISPARADOR)
    correctos = {b: [q for (q, bb), v in base.items() if bb == b and v == "correcto"] for b in K.BRAZOS}
    aud = muestra_auditoria(correctos)
    pares = [{"qid": q, "brazo": b, "tipo": "parcial_disparado"} for q, b in parciales]
    pares += [{"qid": q, "brazo": b, "tipo": "auditoria_correcto"} for b in K.BRAZOS for q in aud[b]]
    pares.sort(key=lambda p: (p["brazo"], p["qid"]))
    sin_veredicto = sorted((q, b) for q in preguntas_ids for b in K.BRAZOS if (q, b) not in base)
    return {"regla": {"disparador": f"veredicto del código de N = 1 == '{DISPARADOR}' (protocolo de EV2, :104-108; A-D8)",
                      "auditoria": (f"max(ceil({K.FRACCION_AUDITORIA} · n), {K.MINIMO_AUDITORIA}) de los 'correcto' por brazo, "
                                    f"random.Random('{K.SEMILLA_AUDITORIA}').sample sobre los ids ordenados, un generador "
                                    "por brazo (comun_enc.py:177-190; A-D7 y A-D10)"),
                      "re_corridas": "tres sesiones nuevas por par (r2, r3 y r4); la base no vota (§4)"},
            "distribucion_n1_por_brazo": {b: dict(Counter(v for (q, bb), v in base.items() if bb == b)) for b in K.BRAZOS},
            "n_parciales_por_brazo": {b: sum(1 for q, bb in parciales if bb == b) for b in K.BRAZOS},
            "n_correctos_por_brazo": {b: len(correctos[b]) for b in K.BRAZOS},
            "n_auditoria_por_brazo": {b: len(aud[b]) for b in K.BRAZOS},
            "P_por_brazo": {b: sum(1 for p in pares if p["brazo"] == b) for b in K.BRAZOS},
            "pares_sin_veredicto_n1": [{"qid": q, "brazo": b} for q, b in sin_veredicto],
            "n_pares": len(pares), "n_sesiones_recorridas": len(pares) * len(K.REPS_RECORRIDA), "pares": pares}


def agregar_recorridas(poblacion: dict, veredictos_rc: dict) -> dict:
    """El veredicto final de cada par de la población: agregacion_enc.detalle_par sobre los tres votos (r2, r3, r4)."""
    finales, incompletos = [], []
    for p in poblacion["pares"]:
        votos = [veredictos_rc.get((p["qid"], p["brazo"], r)) for r in K.REPS_RECORRIDA]
        if any(v is None for v in votos):
            incompletos.append(p | {"reps_sin_veredicto": [r for r, v in zip(K.REPS_RECORRIDA, votos) if v is None]})
            continue
        det = AG.detalle_par([v["veredicto_pregunta"] for v in votos])
        base = "correcto" if p["tipo"] == "auditoria_correcto" else DISPARADOR
        finales.append(p | {"votos": det["votos"], "final": det["final"], "via": det["via"],
                            "flip_descendente": AG.flip_descendente(base, det["final"])})
    return {"regla": AG.__doc__.strip().splitlines()[0], "n_pares": len(poblacion["pares"]), "n_agregados": len(finales),
            "n_incompletos": len(incompletos), "pares": finales, "incompletos": incompletos}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--calcular", action="store_true", required=True)
    ap.add_argument("--preguntas", type=Path, default=K.EV2_PATH)
    ap.add_argument("--sha-preguntas", default=K.EV2_SHA256)
    ap.add_argument("--real", action=argparse.BooleanOptionalAction, default=True)
    ap.add_argument("--juez-dir", type=Path, default=K.JUEZ_DIR)
    ap.add_argument("--salida", type=Path, default=K.POBLACION)
    a = ap.parse_args(argv)
    try:
        preguntas = K.cargar_preguntas(a.preguntas, a.sha_preguntas, real=a.real)
        res = json.loads((a.juez_dir / "n1" / "resumen_juez_n1.json").read_text(encoding="utf-8"))
        if res.get("FRENO_JUEZ") or "corrida" not in res:
            raise K.FrenoA22("el juez de N = 1 no terminó: la población espera a que pase por todas sus respuestas")
        # Una respuesta con una salida mal formada del juez no tiene veredicto: no dispara y queda en pares_sin_veredicto_n1.
        pob = derivar(veredictos_por_par(a.juez_dir, "n1"), sorted(preguntas))
    except (K.FrenoA22, FileNotFoundError) as e:
        print("FRENO DE PRECONDICIÓN DE LA POBLACIÓN:", e)
        return 5
    pob["fuente"] = {"agregados": K.rel_repo(a.juez_dir / "n1" / "agregados_n1_ciego.json"),
                     "sha256_agregados": K.sha256_file(a.juez_dir / "n1" / "agregados_n1_ciego.json"),
                     "agregacion_enc_sha256": K.sha256_file(Path(AG.__file__))}
    a.salida.parent.mkdir(parents=True, exist_ok=True)
    nuevo = json.dumps(pob, ensure_ascii=False, indent=1) + "\n"
    if a.salida.exists() and a.salida.read_text(encoding="utf-8") != nuevo:
        print("FRENO: la población ya existe y difiere de la recomputada")
        return 5
    a.salida.write_text(nuevo, encoding="utf-8")
    print(f"población de N = 3: {pob['n_pares']} pares, {pob['n_sesiones_recorridas']} sesiones de re-corrida")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
