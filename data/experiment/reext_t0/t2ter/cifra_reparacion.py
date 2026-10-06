"""U-REEXT-T0, T2-ter (decisión 5 de la autora sobre el FRENO T2-bis): la cifra de la reparación para la tesis y para
T5, tomada del resumen de E1 de cada TO (resumen_e1.json: reintentos_forma y reparadas_forma), y su control contra los
registros de E1 (extracciones_e1.jsonl, última versión).

Con el perfil r2b, cada unidad con reintento por forma aporta un primer intento mal formado; las que tienen segundo
reintento, además el del primer reintento; y las que quedan agotadas o reparadas, además la última. Entonces:
  salidas mal formadas = |unidades| + |con_segundo_reintento| + |agotados| + |reparadas|.

USD 0, sin red. Lee solo las salidas que se le pasan (copias).
Uso: python -B cifra_reparacion.py --estado NOMBRE=DIR_SALIDA_R2B [--estado ...] --out OUT
"""
import argparse
import json
from pathlib import Path

TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
ap = argparse.ArgumentParser()
ap.add_argument("--estado", action="append", required=True)
ap.add_argument("--out", type=Path, required=True)
a = ap.parse_args()


def last_wins(p: Path) -> dict:
    out = {}
    for x in p.read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            out[r["chunk_id"]] = r
    return out


res = {}
for e in a.estado:
    nombre, d = e.split("=", 1)
    S = Path(d)
    u, seg, ago, rep = [], [], [], []
    mal_reg, por_intento = 0, {"primer_intento": 0, "-rforma1": 0, "-rforma2": 0}
    for to in TOS:
        r1 = json.loads((S / to / "resumen_e1.json").read_text(encoding="utf-8"))
        rf = r1.get("reintentos_forma") or {}
        u += rf.get("unidades", []); seg += rf.get("con_segundo_reintento", []); ago += rf.get("agotados", [])
        rep += (r1.get("reparadas_forma") or {}).get("unidades", [])
        for cid, r in last_wins(S / to / "extracciones_e1.jsonl").items():
            f = r.get("reintento_forma")
            if not f:
                continue
            seg_ = "reintento_2" in f
            ultima_mal = r.get("error") == "salida_mal_formada_tras_reintento" or "reparacion_forma" in r
            por_intento["primer_intento"] += 1
            por_intento["-rforma1"] += 1 if (seg_ or ultima_mal) else 0
            por_intento["-rforma2"] += 1 if (seg_ and ultima_mal) else 0
            mal_reg += 1 + (1 if seg_ else 0) + (1 if ultima_mal else 0)
    unidades_vivas = set(u)
    res[nombre] = {"unidades_con_reintento_por_forma": len(u), "con_segundo_reintento": len(seg),
                   "agotadas_sin_validacion": len(ago), "reparadas": len(rep),
                   "resueltas_por_un_reintento": len(unidades_vivas - set(ago) - set(rep)),
                   "salidas_mal_formadas_segun_el_resumen": len(u) + len(seg) + len(ago) + len(rep),
                   "salidas_mal_formadas_segun_los_registros": mal_reg, "por_intento_segun_los_registros": por_intento,
                   "unidades": {"reparadas": sorted(rep), "agotadas": sorted(ago), "con_segundo_reintento": sorted(seg)}}
a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
for k, v in res.items():
    print(k, json.dumps({x: y for x, y in v.items() if x != "unidades"}, ensure_ascii=False))
