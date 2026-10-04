"""
escalon3_p3c.py — U-PROMPT-R2, P3c-1 (USD 0, sin API): diseño del tercer escalón del reintento por corte de E1
(transmisión por partes, solo con el perfil r2), agregado de la autora a P3c-1 del 04/10/2026.

El tercer escalón se dispara solo si el reintento de 16.384 tokens corta y la unidad no se puede partir
(`correr_e0.particionar_por_corte` devuelve None), o si corta una parte. Este script estima, sobre la E0 que lee
U-REEXT-T0 (`e0_chunking/salida_tanda0_r2b`, 2.439 unidades), qué unidades o partes llegarían a él, con la salida
proyectada como tokens por carácter de texto propio por tres razones:
  - 0,86: la mediana sellada de las 40 unidades de 3.000 caracteres o más de la tanda 0 (`p4/freno_p4.md`, e);
  - 1,175: la mediana del prefijo nuevo en las 6 unidades de ese tamaño de P4 (`p4/salida/analisis_p4.json`,
    `medicion_e`);
  - 1,498: el máximo de esas 6.
Para cada caso, el costo INCREMENTAL del tercer escalón: la llamada nueva (la salida proyectada, con el techo como
tope; la entrada sin caché con la calibración del mensaje de P1; el prefijo leído de la caché), su verificación en
E3 (cota: la extracción renderizada del tamaño de la salida de E1, más el texto propio) y, como cota alta, un
reintento del ratchet al techo. Los dos intentos cortados (8.192 y 16.384) ya los paga el pipeline de hoy.

Escribe solo en --salida (escalon3_p3c.json). Uso (desde la raíz de una copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3c/escalon3_p3c.py --hashes H --salida DIR
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

P3C = Path(__file__).resolve().parent
REPO = P3C.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REX / "e0_chunking"))
import correr_e0  # noqa: E402

E0_R2B = REX / "e0_chunking" / "salida_tanda0_r2b"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
CENSO_P1 = P3C.parent / "p1" / "salida" / "censo_p1.json"
GASTO_P4 = P3C.parent / "p4" / "salida" / "gasto_p4.json"
RAZONES = {"sellada_mediana_0_86": 0.86, "nuevo_mediana_1_175": 1.175, "nuevo_maximo_1_498": 1.498}
TECHO_2 = 16384
TECHO_3 = 40960                        # propuesta (diseno_p3c.md, §5b)
E1 = {"in": 1.00, "out": 5.00, "cr": 0.10}          # claude-haiku-4-5, USD por MTok
E3 = {"in": 2.00, "out": 10.00}                     # claude-sonnet-5, USD por MTok
E3_SALIDA_MAX = 4096                                # prompt_e3.MAX_OUTPUT_TOKENS
TOK_POR_CAR_TEXTO_E3 = 0.3                          # cota del texto propio en el mensaje de E3


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hashes", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    cal = json.loads(CENSO_P1.read_text(encoding="utf-8"))["calibracion"]["mensaje"]
    g = json.loads(GASTO_P4.read_text(encoding="utf-8"))
    h = json.loads(a.hashes.read_text(encoding="utf-8"))
    pref = round(h["borrador"]["caracteres"] * g["e1_nuevo"]["cache_stats"]["cache_write"]
                 / h["congelado"]["caracteres"])
    chunks = []
    for to in TOS:
        chunks += json.loads((E0_R2B / f"chunks_{to}.json").read_text(encoding="utf-8"))

    def costo(c: dict, salida: float) -> dict:
        ent = cal["a"] + cal["tokens_por_caracter"] * c["chars_completo"]
        llamada = (ent * E1["in"] + pref * E1["cr"] + min(salida, TECHO_3) * E1["out"]) / 1e6
        e3 = ((min(salida, TECHO_3) + TOK_POR_CAR_TEXTO_E3 * c["chars_propio"]) * E3["in"]
              + E3_SALIDA_MAX * E3["out"]) / 1e6
        ratchet = (ent * E1["in"] + pref * E1["cr"] + TECHO_3 * E1["out"]) / 1e6
        return {"llamada_usd": round(llamada, 4), "e3_usd": round(e3, 4), "ratchet_al_techo_usd": round(ratchet, 4)}

    out = {"comando": "data/experiment/prompt_r2/p3c/escalon3_p3c.py --hashes H --salida DIR",
           "e0": str(E0_R2B.relative_to(REPO)), "unidades": len(chunks), "techo_2": TECHO_2, "techo_3": TECHO_3,
           "prefijo_tokens_p3c_estimado": pref, "por_razon": {}}
    for nombre, r in RAZONES.items():
        casos = []
        for c in chunks:
            if r * c["chars_propio"] <= TECHO_2:
                continue
            partes, informe = correr_e0.particionar_por_corte(c)
            if partes is None:
                casos.append({"id": c["id"], "caso": "no_se_parte", "motivo": informe.get("motivo"),
                              "chars_propio": c["chars_propio"], "salida_proyectada": round(r * c["chars_propio"]),
                              "corta_en_el_techo_3": r * c["chars_propio"] > TECHO_3,
                              **costo(c, r * c["chars_propio"])})
                continue
            for p in partes:
                if r * p["chars_propio"] > TECHO_2:
                    casos.append({"id": p["id"], "caso": "parte_que_corta", "chars_propio": p["chars_propio"],
                                  "salida_proyectada": round(r * p["chars_propio"]),
                                  "corta_en_el_techo_3": r * p["chars_propio"] > TECHO_3,
                                  **costo(p, r * p["chars_propio"])})
        tot = {k: round(sum(x[k] for x in casos), 4) for k in ("llamada_usd", "e3_usd", "ratchet_al_techo_usd")}
        out["por_razon"][nombre] = {"razon": r, "casos": casos, "n": len(casos),
                                    "cortan_en_el_techo_3": sum(x["corta_en_el_techo_3"] for x in casos),
                                    "total_sin_ratchet_usd": round(tot["llamada_usd"] + tot["e3_usd"], 4),
                                    "total_con_ratchet_usd": round(sum(tot.values()), 4), **tot}
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "escalon3_p3c.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for k, v in out["por_razon"].items():
        print(k, v["n"], [(x["id"], x["caso"], x["salida_proyectada"]) for x in v["casos"]],
              "sin ratchet", v["total_sin_ratchet_usd"], "con ratchet", v["total_con_ratchet_usd"],
              "cortan en el techo 3:", v["cortan_en_el_techo_3"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
