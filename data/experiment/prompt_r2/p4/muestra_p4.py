"""
muestra_p4.py — U-PROMPT-R2, P4.a (USD 0, sin API): la muestra de la prueba pareada, con semilla declarada, y la
declaración de los chunks que cambian en la E0 de C2 de U-R2-CODIGO-2.

Grupos (mandato, decisión 19 y P4.a, con sus notas del 03 y 04/10/2026):
  - sorteo: 40 chunks de los diez TOs, 8 por estrato, con las definiciones de estrato del censo de P1
    (p1/censo_p1.py, `marcas`): con tabla serializada (flags.tablas_e0 de la e0-r2 de `f8dedd4`), con sujeto propuesto
    en el crudo guardado, con cuantía (reglas_comparacion.detectar_cuantias sobre el texto de la E0 legada), con
    omisiones_no_prosa en el crudo, y sin ninguna marca. Los estratos se sortean en ese orden, sin reposición entre
    ellos: random.Random(f"{SEMILLA}:{estrato}").sample(pool ordenado, 8);
  - fijos (9): los cinco casos de control, `cla::5.1.1::intro` y los tres ítems de `cap::8.5`;
  - F1 (8): los chunks de las cinco fichas y los tres incisos de `adrei::4.3.1`;
  - listas de excepciones (8): de las cinco listas elegidas por lectura (estrato_listas_excepciones.md), uno por lista
    y uno más en cada una de las tres listas de ext, que son las más largas; dentro de cada lista,
    random.Random(f"{SEMILLA}:lista:{contenedor}").shuffle de los ítems no leídos antes, en orden, y se toman los
    primeros; un ítem que la lectura descarta (no es un caso de la excepción) se reemplaza por el siguiente;
  - fuera de muestra (8): dos por TO de ayccef, expaef, opefci y adrei, de los chunks de su E0 (e0_fuera_p4.py) fuera
    de F1: random.Random(f"{SEMILLA}:fuera:{to}").sample(pool ordenado, 2);
  - pata de E3 (4): `ctacte::8.3::intro`, `ctacte::8.4::intro`, `ctacte::6.4.7::intro` y `adrei::4.3.1::intro`.
Del sorteo se excluyen los fijos, las listas, la pata de E3 y los chunks sin crudo válido (error en E1), o que no
están en las dos E0 de la tanda 0.

Escribe solo en --salida (muestra_p4.json). Uso (desde la raíz de una COPIA del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p4/muestra_p4.py --e0-fuera DIR --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
import reglas_comparacion as RC  # noqa: E402

SEMILLA = "U-PROMPT-R2:P4:2026-10-04"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
FUERA = ("ayccef", "expaef", "opefci", "adrei")
CRUDO = REX / "corpus_tanda0" / "salida_dirigida"
E0_LEG = REX / "e0_chunking" / "salida_tanda0"
E0_R2 = REX / "e0_chunking" / "salida_tanda0_r2"
E0_R2B = REX / "e0_chunking" / "salida_tanda0_r2b"
ESTRATOS = ("con_tabla_serializada", "con_sujeto_propuesto", "con_cuantia", "con_omisiones_no_prosa", "sin_marca")
FIJOS = ("cap::1.2", "ric::9.2.1", "cla::5.1.1.1", "pro::1.1.2.5", "cap::6.2.2.6", "cla::5.1.1::intro",
         "cap::8.5.1", "cap::8.5.2", "cap::8.5.3")
F1 = ("ayccef::4.2.7.2", "expaef::6.6.2", "ayccef::3.4.1", "expaef::1.1.2.5", "adrei::4.3.1::intro",
      "adrei::4.3.1.1", "adrei::4.3.1.2", "adrei::4.3.1.3")
PATA_E3 = ("ctacte::8.3::intro", "ctacte::8.4::intro", "ctacte::6.4.7::intro", "adrei::4.3.1::intro")
# Listas de excepciones elegidas por lectura (estrato_listas_excepciones.md): contenedor → ítems a tomar.
LISTAS = {"ext::3.5.6::intro": 2, "ext::13.4::intro": 2, "ext::3.3.3::intro": 2, "ctacte::6.2::intro": 1,
          "ctacte::5.1.2::intro": 1}
# Lecturas anteriores: lo que se leyó al escribir la regla f (U-DIAG-VINCULO y P3b-1) y la lectura de P3b-2.
LEIDOS = ("reports/u_diag_vinculo/anexo_u_diag_vinculo.md", "reports/u_diag_vinculo/reporte.md",
          "reports/u_diag_vinculo/salidas/lectura_precision.md", "reports/u_diag_vinculo/salidas/muestra_precision_fichas.md",
          "reports/u_diag_vinculo/salidas/censo_anuncios.txt", "reports/u_diag_vinculo/regla_deteccion.md",
          "data/experiment/prompt_r2/p3b/diseno_p3b.md", "data/experiment/prompt_r2/freno_p3b1.md",
          "data/experiment/prompt_r2/p3b/salida/lado_a_lado_p3b.md",
          "data/experiment/prompt_r2/p3b/salida/mensaje_p3b_lado_a_lado.md",
          "data/experiment/prompt_r2/p3b2/lectura_copia_nota.md")
# Ítems descartados por la lectura (no son casos de la excepción), con su razón: se completa al leer.
DESCARTADOS: dict[str, str] = {}


def jl_last_wins(p: Path) -> dict:
    out = {}
    for x in p.read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            out[r["chunk_id"]] = r
    return out


def chunks(d: Path, to: str) -> dict:
    return {c["id"]: c for c in json.loads((d / f"chunks_{to}.json").read_text(encoding="utf-8"))}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--e0-fuera", type=Path, required=True, help="directorio de trabajo de e0_fuera_p4.py")
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    sal.mkdir(parents=True, exist_ok=True)

    leg, r2, r2b, crudo = {}, {}, {}, {}
    for to in TOS:
        leg.update(chunks(E0_LEG, to))
        r2.update(chunks(E0_R2, to))
        r2b.update(chunks(E0_R2B, to))
        crudo.update(jl_last_wins(CRUDO / to / "extracciones_e1.jsonl"))
    validos = {cid for cid, r in crudo.items() if r.get("error") is None and r.get("tool_input_crudo") is not None
               and cid in leg and cid in r2}
    for cid in FIJOS + PATA_E3[:3]:
        assert cid in validos, f"{cid}: sin crudo válido o fuera de alguna E0"

    # ---- listas de excepciones ----
    censo = json.loads((REPO / "reports/u_diag_vinculo/salidas/censo_anuncios.json").read_text(encoding="utf-8"))
    cont = {c["id"]: c for c in censo["contenedores_tanda0"]}
    mencion = set()
    for f in LEIDOS:
        mencion |= set(re.findall(r"\b([a-z]{2,8}::[0-9S][0-9.]*[0-9](?:::[a-z]+)?)", (REPO / f).read_text(encoding="utf-8")))
    listas, elegidos_listas = {}, []
    for cont_id, k in LISTAS.items():
        items = [cid for u in cont[cont_id]["hijos"] for cid in cont[cont_id]["chunks_hijos"][u]]
        pool = [cid for cid in items if cid in validos and cid not in mencion and cid not in FIJOS]
        orden = sorted(pool)
        random.Random(f"{SEMILLA}:lista:{cont_id}").shuffle(orden)
        tomados = [cid for cid in orden if cid not in DESCARTADOS][:k]
        listas[cont_id] = {"clausula": cont[cont_id]["texto"], "items": items, "no_leidos_antes": sorted(pool),
                           "orden_sorteado": orden, "tomados": tomados,
                           "descartados": {c: DESCARTADOS[c] for c in orden if c in DESCARTADOS}}
        elegidos_listas += tomados

    # ---- sorteo por estratos (definiciones del censo de P1) ----
    excl = set(FIJOS) | set(PATA_E3) | set(elegidos_listas)
    marcas = {}
    for cid in sorted(validos):
        ti = crudo[cid].get("tool_input_crudo") or {}
        m = {"con_tabla_serializada": any(x.get("serializada") for x in (r2[cid].get("flags") or {}).get("tablas_e0") or []),
             "con_sujeto_propuesto": any(isinstance(x, dict) and x.get("sujeto_propuesto")
                                         for x in ti.get("relations") or []),
             "con_cuantia": bool(RC.detectar_cuantias(leg[cid].get("texto") or "")),
             "con_omisiones_no_prosa": bool(ti.get("omisiones_no_prosa"))}
        m["sin_marca"] = not any(m.values())
        marcas[cid] = m
    sorteo, elegidos = {}, set()
    for e in ESTRATOS:
        pool = sorted(cid for cid, m in marcas.items() if m[e] and cid not in excl and cid not in elegidos)
        s = random.Random(f"{SEMILLA}:{e}").sample(pool, 8)
        sorteo[e] = {"pool": len(pool), "elegidos": s}
        elegidos |= set(s)

    # ---- fuera de muestra ----
    w = a.e0_fuera.resolve()
    fuera = {}
    for to in FUERA:
        cl, cr = chunks(w / "e0_legada", to), chunks(w / "e0_r2", to)
        pool = sorted(cid for cid in cl if cid in cr and cid not in F1)
        fuera[to] = random.Random(f"{SEMILLA}:fuera:{to}").sample(pool, 2)
        assert all(c in cl and c in cr for c in F1 if c.startswith(to + "::")), f"F1 de {to} fuera de su E0"

    # ---- E0 de C2: ric cambia en salida_tanda0_r2b ----
    nuevos_r2b = sorted(set(r2b) - set(r2))
    cambiados_r2b = sorted(cid for cid in set(r2b) & set(r2)
                           if (r2b[cid].get("texto"), r2b[cid].get("herencia")) != (r2[cid].get("texto"), r2[cid].get("herencia")))
    todos = ([c for e in ESTRATOS for c in sorteo[e]["elegidos"]] + list(FIJOS) + list(F1) + elegidos_listas
             + [c for to in FUERA for c in fuera[to]] + list(PATA_E3[:3]))
    res = {"semilla": SEMILLA, "comando": "data/experiment/prompt_r2/p4/muestra_p4.py --e0-fuera DIR --salida DIR",
           "e0": {"legada": str(E0_LEG.relative_to(REPO)), "r2": str(E0_R2.relative_to(REPO)),
                  "fuera_de_muestra": "e0_fuera_p4.py, fuera del repo"},
           "sorteo": sorteo, "marcas_de_los_sorteados": {c: marcas[c] for e in ESTRATOS for c in sorteo[e]["elegidos"]},
           "fijos": list(FIJOS), "f1": list(F1), "listas_excepciones": listas, "fuera_de_muestra": fuera,
           "pata_e3": list(PATA_E3),
           "e0_c2": {"nuevos_en_r2b": nuevos_r2b, "cambiados_en_r2b": cambiados_r2b,
                     "en_la_muestra": sorted(set(todos) & (set(nuevos_r2b) | set(cambiados_r2b)))},
           "conteos": {"sorteo": sum(len(sorteo[e]["elegidos"]) for e in ESTRATOS), "fijos": len(FIJOS), "f1": len(F1),
                       "listas": len(elegidos_listas), "fuera_de_muestra": sum(len(v) for v in fuera.values()),
                       "pata_e3_solo": 3, "chunks_distintos": len(set(todos))}}
    txt = json.dumps(res, ensure_ascii=False, indent=1) + "\n"
    (sal / "muestra_p4.json").write_text(txt, encoding="utf-8")
    print(json.dumps(res["conteos"], ensure_ascii=False), hashlib.sha256(txt.encode()).hexdigest()[:12])
    print(json.dumps({"sorteo": {e: sorteo[e] for e in ESTRATOS}, "listas": {k: v["tomados"] for k, v in listas.items()},
                      "fuera": fuera, "e0_c2": res["e0_c2"]}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
