"""U-R2-CODIGO, R1.b — prototipo del formato de serialización de tablas.

Propuesta para el FRENO intermedio de R1 (decisión 4 del mandato): NO es la
implementación. Lee una salida de E0 versión e0-r2 (tablas_<to>.json y
chunks_<to>.json, que hoy solo marcan) y, para cada tabla marcada, decide si
se serializa y arma su bloque con el formato de
`r1b_propuesta_formato_tablas.md`. Escribe:
  --out-json   bloques por tabla, motivo de no serialización, modo y tamaños;
  --out-ej     texto de los chunks de ejemplo antes y después (sustitución de
               la corrida contigua de líneas de E0 de cada tabla).
USD 0, sin LLM, determinístico.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \\
    data/experiment/r2_codigo/r1b_prototipo_formato.py --e0-r2 <salida e0-r2> \\
    --out-json <json> --out-ej <txt> cap::1.2 cap::2.12.2.5 ric::9.2.1 cap::6.2.1.1
"""

from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path

RE_NUMERICO = re.compile(r"^(?=.*\d)[\d.,%()\-–/\s]+$")   # = e0_tablas.RE_NUMERICO
RE_CODIGO = re.compile(r"^\d{3}")                        # = e0_lib, primer_codigo
MAX_FILAS_ENCABEZADO = 4                                  # = e0_tablas.MAX_FILAS_ZONA_ENCABEZADO
SEP_PAR = " | "
SEP_CLAVE = " = "


def _tx(c) -> str:
    return (c or "").strip()


def celda(c) -> str:
    """Una celda multilínea se escribe en una línea: fragmentos unidos por un
    espacio (no se des-silabea: «gradua- ción» queda como está)."""
    return " ".join(f.strip() for f in _tx(c).split("\n") if f.strip())


def es_dato(c) -> bool:
    t = _tx(c)
    return bool(t) and bool(RE_NUMERICO.match(t) or RE_CODIGO.match(t))


def multilinea_numerica(c) -> bool:
    fr = [f.strip() for f in _tx(c).split("\n") if f.strip()]
    return len(fr) >= 2 and all(RE_NUMERICO.match(f) for f in fr)


def filas_de(t: dict) -> list[list]:
    """Filas de la tabla lógica; en los segmentos de continuación se omiten
    las filas que e0_tablas marcó como encabezado repetido (R-COSTURA)."""
    out = []
    for si, s in enumerate(t["segmentos"]):
        rep = set(s.get("filas_encabezado_repetido") or [])
        out.extend(f for fi, f in enumerate(s["filas"]) if not (si > 0 and fi in rep))
    return out


def motivo_no_serializada(t: dict) -> str | None:
    celdas = [c for s in t["segmentos"] for f in s["filas"] for c in f]
    lineas = [l["texto"] for s in t["segmentos"] for l in s["lineas_e0"]]
    ch = lambda xs: collections.Counter(x for s in xs for x in (s or "") if not x.isspace())
    if t["estado"] != "parseada":
        return "declarada_por_e0_tablas:" + ",".join(t["causas"])
    if any(s["verificacion"]["chars_perdidos"] for s in t["segmentos"]):
        return "r_verif_con_perdida"
    if sum((ch(lineas) - ch(celdas)).values()):
        return "lineas_e0_no_contenidas_en_celdas"
    if any(multilinea_numerica(c) for c in celdas):
        return "filas_colapsadas"
    if any("|" in _tx(c) for c in celdas):
        return "separador_en_celda"
    if len(t["chunks"]) != 1:
        return "mas_de_un_chunk"
    return None


def bloque(t: dict) -> tuple[str, str]:
    filas = filas_de(t)
    n_cols = max(len(f) for f in filas)
    i_dato = next((i for i, f in enumerate(filas) if any(es_dato(c) for c in f)), None)
    zona = (filas[:i_dato] if i_dato is not None and 1 <= i_dato <= MAX_FILAS_ENCABEZADO
            else [])
    rotulos, enc_filas = [], []
    for f in zona:
        if _tx(f[0]) and all(c is None for c in f[1:]):
            rotulos.append(celda(f[0]))
        else:
            enc_filas.append(f)
    simple = (bool(enc_filas)
              and not any(c is None for f in enc_filas for c in f)
              and not any(SEP_CLAVE in celda(c) for f in enc_filas for c in f))
    enc = [""] * n_cols
    if simple:
        for f in enc_filas:
            for k, c in enumerate(f):
                if _tx(c):
                    enc[k] = (enc[k] + " " + celda(c)).strip()
    modo = "columnas" if simple else "posicional"
    pags = ", ".join(str(p) for p in sorted({s["pagina"] for s in t["segmentos"]}))
    origen = "e0_tablas" if t["origen"] == "e0_tablas" else "R-TC2"
    ls = [f"[TABLA {t['id']} | página {pags} | {origen} | {modo}]"]
    if simple:
        ls.extend(f"Rótulo: {r}" for r in rotulos)
        ls.append("Columnas: " + SEP_PAR.join(e or f"col{k + 1}" for k, e in enumerate(enc)))
        datos = filas[len(zona):]
    else:
        datos = filas
    datos = [f for f in datos if any(_tx(c) for c in f)]
    for i, f in enumerate(datos, start=1):
        pares = [f"{(enc[k] if simple and enc[k] else f'col{k + 1}')}{SEP_CLAVE}{celda(c)}"
                 for k, c in enumerate(f) if _tx(c)]
        ls.append(f"Fila {i}: " + SEP_PAR.join(pares))
    ls.append(f"[FIN TABLA {t['id']}]")
    return "\n".join(ls), modo


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--e0-r2", required=True)
    ap.add_argument("--out-json", required=True)
    ap.add_argument("--out-ej", required=True)
    ap.add_argument("ejemplos", nargs="*")
    a = ap.parse_args()
    sal = Path(a.e0_r2)
    res = []
    tablas_por_chunk: dict[str, list[dict]] = collections.defaultdict(list)
    for f in sorted(sal.glob("tablas_*.json")):
        for t in json.loads(f.read_text(encoding="utf-8"))["tablas"]:
            if not t.get("marca"):
                continue
            m = motivo_no_serializada(t)
            b, modo = bloque(t) if m is None else (None, None)
            lineas = [l["texto"] for s in t["segmentos"] for l in s["lineas_e0"]]
            res.append({"tabla": t["id"], "chunks": t["chunks"], "origen": t["origen"],
                        "motivo_no_serializada": m, "modo": modo,
                        "chars_lineas_e0": len("\n".join(lineas)),
                        "chars_bloque": len(b) if b else None, "bloque": b})
            for cid in t["chunks"]:
                tablas_por_chunk[cid].append({"t": t, "bloque": b, "lineas": lineas})
    ser = [r for r in res if r["bloque"]]
    resumen = {
        "tablas_marcadas": len(res),
        "serializadas": len(ser),
        "no_serializadas_por_motivo": dict(sorted(collections.Counter(
            r["motivo_no_serializada"] for r in res if not r["bloque"]).items())),
        "por_modo": {m: {"tablas": sum(1 for r in ser if r["modo"] == m),
                         "chars_lineas_e0": sum(r["chars_lineas_e0"] for r in ser if r["modo"] == m),
                         "chars_bloques": sum(r["chars_bloque"] for r in ser if r["modo"] == m)}
                     for m in ("columnas", "posicional")},
        "chunks_con_texto_propio_cambiado": sorted({r["chunks"][0] for r in ser}),
    }
    Path(a.out_json).write_text(json.dumps({"resumen": resumen, "tablas": res},
                                           ensure_ascii=False, indent=1) + "\n",
                                encoding="utf-8")
    partes = []
    for cid in a.ejemplos:
        to = cid.split("::")[0]
        ch = {c["id"]: c for c in json.loads((sal / f"chunks_{to}.json").read_text(
            encoding="utf-8"))}[cid]
        nuevo = ch["texto"].split("\n")
        for x in tablas_por_chunk[cid]:
            if not x["bloque"]:
                continue
            run = x["lineas"]
            for i in range(len(nuevo) - len(run) + 1):
                if nuevo[i:i + len(run)] == run:
                    nuevo[i:i + len(run)] = x["bloque"].split("\n")
                    break
            else:
                raise SystemExit(f"{x['t']['id']}: líneas no contiguas en {cid}")
        partes.append(f"===== {cid} — ANTES (E0 legada)\n{ch['texto']}\n\n"
                      f"===== {cid} — DESPUÉS (formato propuesto)\n" + "\n".join(nuevo) + "\n")
    Path(a.out_ej).write_text("\n".join(partes), encoding="utf-8")


if __name__ == "__main__":
    main()
