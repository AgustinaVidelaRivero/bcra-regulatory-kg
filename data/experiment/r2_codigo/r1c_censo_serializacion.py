"""U-R2-CODIGO, R1.c — censo y controles de la serialización de tablas e0-r2.

Lee la E0 legada de la tanda 0 (`e0_chunking/salida_tanda0/`, sellada) y una
salida e0-r2 (corrida sobre una copia del código) y escribe un JSON con:
  - V4: chunks sin tabla marcada idénticos a la legada (dict completo); chunks
    con tabla marcada y sin bloque, con texto y herencia idénticos salvo los
    bloques heredados; en todo chunk, el texto y la herencia legados se
    recuperan reemplazando cada bloque por las líneas de E0 de su tabla;
  - V1 a V3 por tabla serializada (las calcula correr_e0 y quedan en
    tablas_<to>.json) y su conteo;
  - tablas serializadas por modo, motivos de no serialización, celdas
    combinadas propagadas (agregado E), filas de subtítulo internas;
  - marca F: chunks con `contenido_tabular_residual` verdadero y falso;
  - modo posicional: si la primera fila del bloque es de encabezado (sin
    celdas numéricas ni de código), de modo que cada colN se asocie a su
    encabezado leyendo solo el bloque; lista de las que no;
  - ausencia del marcador de celda combinada en los textos y celdas legados.
USD 0, sin LLM, determinístico.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \\
    data/experiment/r2_codigo/r1c_censo_serializacion.py \\
    --e0-legada data/experiment/reextraccion_v2/e0_chunking/salida_tanda0 \\
    --e0-r2 <salida e0-r2> --out <json>
"""

from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path

RE_BLOQUE = re.compile(r"\[TABLA (\S+) \| [^\n]*\]\n.*?\n\[FIN TABLA \1\]", re.S)
RE_FILA = re.compile(r"^Fila (\d+): (.*)$")
RE_NUMERICO = re.compile(r"^(?=.*\d)[\d.,%()\-–/\s]+$")   # = e0_tablas.RE_NUMERICO
RE_CODIGO = re.compile(r"^\d{3}")                        # = correr_e0.RE_CODIGO_DATO
MARCADOR = ("⟨", "⟩")


def _cargar(d: Path, patron: str) -> dict:
    return {p.stem.split("_", 1)[1]: json.loads(p.read_text(encoding="utf-8"))
            for p in sorted(d.glob(patron))}


def _desbloquear(texto: str, lineas_de: dict[str, list[str]]) -> str:
    return RE_BLOQUE.sub(lambda m: "\n".join(lineas_de[m.group(1)]), texto)


def _igual_desbloqueado(c: dict, v: dict, lineas_de: dict[str, list[str]]) -> bool:
    """El chunk e0-r2 `c`, con cada bloque reemplazado por las líneas de E0 de
    su tabla, es igual al legado `v`: texto; herencia unida (un tramo absorbido
    entero por un bloque no figura en e0-r2, así que los tramos de `c` son una
    subsecuencia de los de `v`); y metadatos (salvo los tamaños y sha, que se
    derivan del texto, y los flags, que se comparan aparte)."""
    derivados = ("texto", "herencia", "flags", "chars_propio", "chars_completo",
                 "sha256_propio", "sha256_completo")
    meta = lambda h: (h["tipo"], h["unidad_origen"], h["paginas"])   # noqa: E731
    it = iter([meta(h) for h in v["herencia"]])
    subsecuencia = all(m in it for m in (meta(h) for h in c["herencia"]))
    return (_desbloquear(c["texto"], lineas_de) == v["texto"]
            and _desbloquear("\n".join(h["texto"] for h in c["herencia"]), lineas_de)
            == "\n".join(h["texto"] for h in v["herencia"])
            and subsecuencia
            and {k: x for k, x in c.items() if k not in derivados}
            == {k: x for k, x in v.items() if k not in derivados})


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--e0-legada", required=True)
    ap.add_argument("--e0-r2", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    leg = _cargar(Path(a.e0_legada), "chunks_*.json")
    r2 = _cargar(Path(a.e0_r2), "chunks_*.json")
    tablas = _cargar(Path(a.e0_r2), "tablas_*.json")

    lineas_de: dict[str, list[str]] = {}
    ser_por_tabla: dict[str, dict] = {}
    motivos = collections.Counter()
    por_modo = collections.Counter()
    chars = collections.Counter()
    propagadas, tablas_con_prop, subtitulos, tablas_con_sub = 0, [], 0, []
    sin_propagar = 0
    verif_fallidas = []
    posicional_sin_encabezado = []
    posicional_ok = 0
    marcador_en_celdas = 0
    for to in sorted(tablas):
        for t in tablas[to]["tablas"]:
            for s in t["segmentos"]:
                for f in s["filas"]:
                    for c in f:
                        if c and any(m in c for m in MARCADOR):
                            marcador_en_celdas += 1
            ser = t["serializacion"]
            if not t["marca"]:
                continue
            if not ser["serializada"]:
                motivos[ser["motivo"]] += 1
                continue
            lineas_de[t["id"]] = [l["texto"] for s in t["segmentos"] for l in s["lineas_e0"]]
            ser_por_tabla[t["id"]] = ser
            por_modo[ser["modo"]] += 1
            chars[ser["modo"] + "_e0"] += ser["chars_lineas_e0"]
            chars[ser["modo"] + "_bloque"] += ser["chars_bloque"]
            if ser["celdas_propagadas"]:
                propagadas += ser["celdas_propagadas"]
                tablas_con_prop.append({"tabla": t["id"], "celdas": ser["celdas_propagadas"]})
            sin_propagar += ser["celdas_combinadas_sin_propagar"]
            if ser["filas_subtitulo"]:
                subtitulos += ser["filas_subtitulo"]
                tablas_con_sub.append({"tabla": t["id"], "filas": ser["filas_subtitulo"]})
            if not (ser["v1"]["ok"] and ser["v2_r_verif_sin_perdida"]
                    and ser["v3_e0_en_celdas"] and ser["v3_e0_en_bloque"]):
                verif_fallidas.append(t["id"])
            if ser["modo"] == "posicional":
                fila1 = next(RE_FILA.match(l) for l in ser["bloque"].split("\n") if RE_FILA.match(l))
                valores = [p.split(" = ", 1)[1] for p in fila1.group(2).split(" | ")]
                if any(RE_NUMERICO.match(v) or RE_CODIGO.match(v) for v in valores):
                    posicional_sin_encabezado.append({"tabla": t["id"], "chunk": t["chunks"][0],
                                                      "fila_1": fila1.group(2)[:200]})
                else:
                    posicional_ok += 1

    v4_identicos = v4_sin_bloque_ok = v4_desbloqueo_ok = v4_solo_heredado_ok = 0
    v4_fallos = []
    residual = {"con_residual": [], "sin_residual": []}
    marcador_en_legada = 0
    for to in sorted(r2):
        cl = {c["id"]: c for c in leg[to]}
        if [c["id"] for c in leg[to]] != [c["id"] for c in r2[to]]:
            v4_fallos.append({"to": to, "falla": "ids"})
        for c in leg[to]:
            textos = [c["texto"]] + [h["texto"] for h in c["herencia"]]
            if any(m in x for x in textos for m in MARCADOR):
                marcador_en_legada += 1
        for c in r2[to]:
            v = cl[c["id"]]
            f = c["flags"]
            if "tablas_e0" not in f:
                if c == v:
                    v4_identicos += 1
                elif _igual_desbloqueado(c, v, lineas_de) and c["flags"] == v["flags"]:
                    v4_solo_heredado_ok += 1
                else:
                    v4_fallos.append({"chunk": c["id"], "falla": "chunk_sin_tabla_distinto"})
                continue
            clave = "con_residual" if f["contenido_tabular_residual"] else "sin_residual"
            residual[clave].append(c["id"])
            tiene_bloque = any(e["serializada"] for e in f["tablas_e0"])
            if not tiene_bloque and c["texto"] == v["texto"]:
                v4_sin_bloque_ok += 1
            fl = {k: x for k, x in f.items() if k not in ("contenido_tabular", "tablas_e0",
                                                          "contenido_tabular_residual")}
            fl_v = {k: x for k, x in v["flags"].items() if k != "contenido_tabular"}
            if _igual_desbloqueado(c, v, lineas_de) and fl == fl_v and f["contenido_tabular"]:
                v4_desbloqueo_ok += 1
            else:
                v4_fallos.append({"chunk": c["id"], "falla": "desbloqueo"})
    heredados = sorted({c["id"] for to in r2 for c in r2[to]
                        if any(RE_BLOQUE.search(h["texto"]) for h in c["herencia"])})
    marcadas = sum(1 for to in tablas for t in tablas[to]["tablas"] if t["marca"])
    out = {
        "unidad": "U-R2-CODIGO", "etapa": "R1.c",
        "chunks_total": sum(len(v) for v in r2.values()),
        "tablas_marcadas": marcadas,
        "tablas_serializadas": len(ser_por_tabla),
        "serializadas_por_modo": dict(sorted(por_modo.items())),
        "caracteres_por_modo": dict(sorted(chars.items())),
        "no_serializadas_por_motivo": dict(sorted(motivos.items())),
        "verificacion_v1_v3_fallidas": verif_fallidas,
        "combinadas_celdas_propagadas": propagadas,
        "combinadas_tablas": tablas_con_prop,
        "combinadas_sin_propagar_por_origen": sin_propagar,
        "filas_subtitulo_internas": subtitulos,
        "filas_subtitulo_tablas": tablas_con_sub,
        "posicional_con_encabezado_en_el_bloque": posicional_ok,
        "posicional_sin_encabezado_en_el_bloque": posicional_sin_encabezado,
        "v4_chunks_sin_tabla_identicos": v4_identicos,
        "v4_chunks_sin_tabla_solo_bloque_heredado": v4_solo_heredado_ok,
        "v4_chunks_con_tabla_sin_bloque_texto_identico": v4_sin_bloque_ok,
        "v4_chunks_con_tabla_desbloqueo_igual_a_legada": v4_desbloqueo_ok,
        "v4_fallos": v4_fallos,
        "chunks_con_bloque_heredado": heredados,
        "residual": {k: {"n": len(v), "chunks": v} for k, v in residual.items()},
        "marcador_en_textos_legados": marcador_en_legada,
        "marcador_en_celdas": marcador_en_celdas,
    }
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                           encoding="utf-8")


if __name__ == "__main__":
    main()
