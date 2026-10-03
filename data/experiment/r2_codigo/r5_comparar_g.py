"""U-R2-CODIGO, ajuste B antes de R5 — cambios de resolución de la regla (g)
entre versiones del detector de remisiones. USD 0.

Dos modos:
  --tabla: con el código de `--raiz` (una copia del repo con la versión a
     medir de r1_referencias.py y r3d_remisiones.py; nunca el repo), arma la
     tabla de resolución de cada mención de norma: en desarrollo y en diez,
     las citas del detector del perfil r2 sobre el texto de e0-r2
     (`--e0-r2`), y en la partición, las menciones de cada chunk de
     `segmentacion_84/b584_particion` sobre su texto (tramos heredados de la
     unidad y texto propio, unidos, como en la comparación de R4). Clave de
     una mención: chunk, puntos, secciones y posición de la evidencia en el
     texto normalizado (la evidencia puede cambiar entre versiones).
  --comparar A B [C]: cambios de resolución de B frente a A en cada sentido
     (resuelta → irresoluble, irresoluble → resuelta, otro TO), con la vía de
     la regla (g) de la versión nueva («igualdad», «prefijo», «comienzo»); con
     C, además, para las citas que pasaron de resueltas en A a irresolubles en
     B (las 41 de la partición entre la (g) anterior y la de R4), su estado
     en C y por qué vía.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/r5_comparar_g.py --tabla \\
      --raiz <copia> --e0-r2 <dir> --out <json>
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/r5_comparar_g.py --comparar \\
      <tabla_A> <tabla_B> [<tabla_C>] --out <json>
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

CLASES = ("externa", "externa_anaforica", "interna")


def _clave(chunk: str, texto_norm: str, men: dict) -> str:
    pos = texto_norm.find(men["evidencia"])
    return "|".join([chunk, ",".join(men.get("puntos") or []), ",".join(men.get("secciones") or []), str(pos)])


def tabla(raiz: Path, e0_r2: Path) -> dict:
    if (raiz / ".git").exists():
        raise SystemExit("--raiz no puede ser el repo (tiene .git): la medición corre sobre una copia")
    for p in (raiz / "data/experiment/r2_codigo", raiz / "data/experiment/reextraccion_v2/corpus_v2",
              raiz / "data/experiment/reextraccion_v2", raiz / "data/experiment/grafo_v2/code"):
        sys.path.insert(0, str(p))
    import r1_referencias as REF  # noqa: PLC0415  versión de --raiz
    import r3d_remisiones as D  # noqa: PLC0415
    assert Path(REF.__file__).resolve().is_relative_to(raiz.resolve()) and D.REF is REF
    out = {"r1_referencias": str(Path(REF.__file__).resolve()), "r3d_remisiones": str(Path(D.__file__).resolve())}
    for ens in ("desarrollo", "diez"):
        with D.redirigido(ens):
            kg, base, sellados = D.cargar(ens)
            r = D.correr(base, D.emisores(), reglas=REF.REGLAS_R2, chunks_e0_r2=D.chunks_e0_r2(e0_r2))
            filas = {}
            for c in r["registro"]:
                if c["clase"] not in CLASES:
                    continue
                k = "|".join([c.get("chunk_id") or "", c.get("atribucion") or "", c["evidencia"],
                              ",".join(c["puntos"]), ",".join(c["secciones"])])
                filas[k] = {"clase": c["clase"], "to_destino": c["to_destino"], "norma": c.get("norma_nombrada"),
                            "via": c.get("via_norma"), "destinos": sorted(d["destino"] for d in c["destinos"]),
                            "causas": sorted(x["causa"] for x in c["irresolubles"])}
            out[ens] = filas
    part = {}
    P = raiz / "data/experiment/segmentacion_84/b584_particion"
    ids = sorted({r["id"] for r in csv.DictReader(REF.INVENTARIO_TITULOS.open(encoding="utf-8"))}
                 | {"cap", "cla", "ext", "pro", "ric"})
    REF.TITULOS_TOS = REF.titulos_de_inventario(ids)
    for d in sorted(x for x in P.iterdir() if x.is_dir()):
        f = d / f"chunks_{d.name}.json"
        if not f.exists():
            continue
        for ch in json.loads(f.read_text(encoding="utf-8")):
            t = REF.normalizar_e0("\n".join([h["texto"] for h in ch.get("herencia", []) if h["unidad_origen"] == ch.get("unidad")]
                                            + [ch.get("texto") or ""]), True)[0]
            for m in REF.detectar_menciones_r2(t, d.name, REF.REGLAS_R2):
                if m["clase"] not in CLASES:
                    continue
                part[_clave(ch["id"], t, m)] = {"clase": m["clase"], "to_destino": m["to_destino"],
                                                "norma": m.get("norma_nombrada"), "via": m.get("via_norma"),
                                                "evidencia": m["evidencia"], "causa": m.get("causa_irresoluble")}
    out["particion"] = part
    return out


def _estado(f: dict | None) -> str | None:
    if f is None:
        return None
    return "resuelta" if f.get("to_destino") else "irresoluble"


def comparar(a: dict, b: dict, c: dict | None = None) -> dict:
    res = {}
    for parte in ("desarrollo", "diez", "particion"):
        A, B = a[parte], b[parte]
        filas, cuenta = [], Counter()
        for k in sorted(set(A) & set(B)):
            ea, eb = _estado(A[k]), _estado(B[k])
            if ea == eb and A[k].get("to_destino") == B[k].get("to_destino"):
                continue
            sentido = (f"{ea}_a_{eb}" if ea != eb else "otro_to")
            cuenta[sentido] += 1
            filas.append({"sentido": sentido, "clave": k, "norma_antes": A[k].get("norma"), "norma_despues": B[k].get("norma"),
                          "antes": A[k].get("to_destino"), "despues": B[k].get("to_destino"), "via_despues": B[k].get("via"),
                          "clase_antes": A[k].get("clase"), "clase_despues": B[k].get("clase")})
        res[parte] = {"conteo": dict(sorted(cuenta.items())), "menciones_solo_en_A": len(set(A) - set(B)),
                      "menciones_solo_en_B": len(set(B) - set(A)), "filas": filas}
        if c is not None:
            C = c[parte]
            perdidas = [x for x in filas if x["sentido"] == "resuelta_a_irresoluble"]
            seguimiento = []
            for x in perdidas:
                fc = C.get(x["clave"])
                seguimiento.append({**x, "en_C": _estado(fc), "to_C": (fc or {}).get("to_destino"), "via_C": (fc or {}).get("via"),
                                    "norma_C": (fc or {}).get("norma"),
                                    "igual_que_antes": (fc or {}).get("to_destino") == x["antes"]})
            res[parte]["resueltas_en_A_irresolubles_en_B"] = {
                "n": len(perdidas),
                "en_C": dict(sorted(Counter(str(s["en_C"]) for s in seguimiento).items())),
                "vuelven_a_resolver_por_via": dict(sorted(Counter(str(s["via_C"]) for s in seguimiento if s["en_C"] == "resuelta").items())),
                "vuelven_al_mismo_to": sum(1 for s in seguimiento if s["en_C"] == "resuelta" and s["igual_que_antes"]),
                "filas": seguimiento}
    return res


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tabla", action="store_true")
    ap.add_argument("--raiz", type=Path)
    ap.add_argument("--e0-r2", type=Path, dest="e0_r2")
    ap.add_argument("--comparar", nargs="+", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    if a.tabla:
        r = tabla(a.raiz, a.e0_r2)
    else:
        ts = [json.loads(p.read_text(encoding="utf-8")) for p in a.comparar]
        r = comparar(*ts)
    a.out.write_text(json.dumps(r, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
