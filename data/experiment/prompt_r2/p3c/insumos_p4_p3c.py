"""
insumos_p4_p3c.py — U-PROMPT-R2, P3c-1 (USD 0, sin API): lo que el diseño de P3c toma de la salida guardada de P4.

Lee el crudo de los dos brazos de P4 (`p4/salida/resultados_p4.jsonl`) y su análisis (`p4/salida/analisis_p4.json`) y
cuenta, en el brazo nuevo:
  1. las omisiones `meta_normativo`, con dónde verifica su tramo: contra el texto propio (la verificación del
     análisis, `validador_r2.verificar_tramo`), contra el texto completo o, en un mini-chunk a mitad de oración, en el
     orden de lectura (P3b, h); y cuáles confirmó la autora como contenido normativo (revisión del 04/10/2026);
  2. las menciones de sujeto que no verifican (punto e);
  3. las relaciones de D5 (`condicion_de` de firma nueva) y D6 (`limita`) que el crudo emite y la validación de su
     brazo rechaza, por brazo (la corrección a de la revisión, aplicada a las dos dimensiones);
  4. la verificación del tramo de todas las omisiones del brazo nuevo, hoy (solo el texto propio,
     `validador_r2.py:1316`) y con la regla del punto g (la del tramo simple de la entidad: propio, completo y orden de
     lectura).

Escribe solo en --salida (insumos_p4_p3c.json). Sobre una copia del repo (regla l).
Uso (desde la raíz de la copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3c/insumos_p4_p3c.py \
      --e0-fuera DIR_E0R2_FUERA --salida DIR
  (DIR_E0R2_FUERA: la e0-r2 de ayccef, expaef, opefci y adrei que arma p4/e0_fuera_p4.py.)
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
import validador_r2 as V  # noqa: E402

P4 = AQUI.parent / "p4" / "salida"
E0_R2 = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_tanda0_r2"   # la de P4 (f8dedd4)
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
FUERA = ("ayccef", "expaef", "opefci", "adrei")
# Revisión de la autora (04/10/2026, corrección d): omisiones `meta_normativo` que son contenido normativo.
META_NORMATIVAS_AUTORA = ("adrei::S5", "ext::10.4.2.7", "expaef::2.2.6.5", "ctacte::4.2.1", "ctacte::5.1.2.2",
                          "cla::5.1.1::intro", "ctacte::8.3::intro", "ctacte::8.4::intro", "ext::13.4.8")
PRED = {"condicion_de_firma_nueva": "condicion_de", "destino_limita": "limita"}


def chunks(e0_fuera: Path) -> dict:
    out = {}
    for d, tos in ((E0_R2, TOS), (e0_fuera, FUERA)):
        for to in tos:
            for c in json.loads((d / f"chunks_{to}.json").read_text(encoding="utf-8")):
                out[c["id"]] = c
    return out


def donde(tramo: str, c: dict, pol) -> str:
    """Dónde verifica un tramo de omisión: propio, completo, orden_de_lectura o no."""
    if V.verificar_tramo(tramo, c.get("texto") or "", pol.holgura)[0] in ("exacta", "tokens"):
        return "propio"
    if V.verificar_tramo(tramo, V.texto_completo(c), pol.holgura)[0] in ("exacta", "tokens"):
        return "completo"
    if V._mini_a_mitad(c) and V.verificar_tramo(tramo, V.texto_en_orden_de_lectura(c), pol.holgura)[0] in (
            "exacta", "tokens"):
        return "orden_de_lectura"
    return "no"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--e0-fuera", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    pol = V.politica_default()
    ch = chunks(a.e0_fuera)
    res = {}
    for x in (P4 / "resultados_p4.jsonl").read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            res[r["chunk_id"]] = r
    filas = json.loads((P4 / "analisis_p4.json").read_text(encoding="utf-8"))["filas"]
    marcas = json.loads((P4 / "marcas_lectura_p4.json").read_text(encoding="utf-8"))["fichas"]

    meta, todas, hoy, con_g = [], Counter(), Counter(), Counter()
    menciones = []
    for cid in sorted(filas):
        c = ch[cid]
        for o in res[f"{cid}|nuevo"]["tool_input"].get("omisiones") or []:
            t = o.get("tramo")
            if not t:
                continue
            d = donde(t, c, pol)
            hoy["verifica" if d == "propio" else "no_verifica"] += 1
            con_g["verifica" if d != "no" else "no_verifica"] += 1
            con_g[f"donde:{d}"] += 1
            todas[o.get("categoria")] += 1
            if o.get("categoria") == "meta_normativo":
                meta.append({"chunk": cid, "grupo": filas[cid]["grupo"], "donde": d,
                             "normativa_autora": cid in META_NORMATIVAS_AUTORA, "tramo": t})
        for m in filas[cid]["hechos"]["nuevo"].get("menciones") or []:
            if m.get("verificada") not in ("exacta", "tokens"):
                menciones.append({"chunk": cid, "grupo": filas[cid]["grupo"], "mencion": m.get("mencion"),
                                  "verificada": m.get("verificada")})

    rechazadas = []
    for cid, dims in sorted(marcas.items()):
        for dim, pred in PRED.items():
            if dim not in dims:
                continue
            for brazo in ("sellado", "nuevo"):
                r = res[f"{cid}|{brazo}"]
                crudo = [x for x in r["tool_input"].get("relations") or [] if x.get("predicate") == pred]
                val = [x for x in r["validacion_e1"].get("relaciones") or [] if x.get("predicate") == pred]
                if len(crudo) != len(val):
                    rechazadas.append({
                        "chunk": cid, "grupo": filas[cid]["grupo"], "dimension": dim, "brazo": brazo,
                        "marca": dims[dim][brazo], "crudo": len(crudo), "validadas": len(val),
                        "rechazos": [z["motivo"] + ": " + z["detalle"] for z in r["validacion_e1"].get("rechazos") or []
                                     if f"({pred})" in z["detalle"] or f"--{pred}-->" in z["detalle"]]})

    cm = Counter(m["donde"] for m in meta)
    out = {
        "comando": "data/experiment/prompt_r2/p3c/insumos_p4_p3c.py --e0-fuera DIR --salida DIR",
        "fuentes": ["data/experiment/prompt_r2/p4/salida/resultados_p4.jsonl",
                    "data/experiment/prompt_r2/p4/salida/analisis_p4.json",
                    "data/experiment/prompt_r2/p4/salida/marcas_lectura_p4.json"],
        "meta_normativo": {
            "total": len(meta), "fichas": len({m["chunk"] for m in meta}), "por_donde": dict(sorted(cm.items())),
            "con_texto_propio": cm["propio"],
            "con_texto_propio_normativas_autora": sum(m["normativa_autora"] for m in meta if m["donde"] == "propio"),
            "sin_texto_propio_normativas_autora": sum(m["normativa_autora"] for m in meta if m["donde"] != "propio"),
            "filas": meta},
        "menciones_no_verificadas": {"total": len(menciones),
                                     "las_entidades": sum(str(m["mencion"]).lower() == "las entidades"
                                                          for m in menciones),
                                     "fichas": len({m["chunk"] for m in menciones}), "filas": menciones},
        "relaciones_d5_d6_rechazadas_por_el_validador": rechazadas,
        "omisiones_verificacion_del_tramo": {"por_categoria": dict(sorted(todas.items())),
                                             "hoy_solo_texto_propio": dict(hoy), "con_regla_g": dict(sorted(con_g.items()))},
    }
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "insumos_p4_p3c.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in out["meta_normativo"].items() if k != "filas"}, ensure_ascii=False))
    print(json.dumps({k: v for k, v in out["menciones_no_verificadas"].items() if k != "filas"}, ensure_ascii=False))
    print(json.dumps(out["omisiones_verificacion_del_tramo"], ensure_ascii=False))
    print(len(rechazadas), "relaciones de D5/D6 rechazadas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
