"""
ejemplos_mensaje_r2.py — U-PROMPT-R2, P1 (USD 0): mensajes de usuario de E1 de
borrador (perfil r2b) y NOTA de E3, sellados al lado de los nuevos, para una
selección fija de chunks que cubre cada rama del bloque de tablas:
  - cap::1.2: tabla serializada simple (la tabla invertida de BKL-0006);
  - ric::9.2.1: dos tablas serializadas, una posicional (el cuadro de códigos de D2);
  - cap::6.2.2.6: tabla posicional con celdas combinadas sin propagar (aviso);
  - cap::4.2.1.2: tablas serializadas y una no serializada (residual verdadero);
  - ric::S2: tabla detectada y no serializada (residual verdadero, sin bloque);
  - cap::2.13: marcada solo por la heurística legada (clave residual ausente);
  - ric::11.2.3: bloque heredado de su mini-chunk;
  - cla::5.1.1.1: sin tabla (el ejemplo de la tesis);
  - ctacte::2.3.4.1: ítem de una lista cuyo encabezado está en la línea de título (F1-A);
  - ext::4.8.6::intro y ext::4.8.6.1: encabezado con una condición que vale para cada ítem (tipo (ii)), con la
    NOTA de E3 de los encabezados de lista, y uno de sus ítems;
y una demostración de la lista de tablas forzadas a residual: cap::6.2.2.6 con
cap::tabla037 en la lista (en código; el prefijo no cambia).
Lee la E0 legada (mensaje sellado) y la e0-r2 versionada en f8dedd4 (mensaje
nuevo). Escribe data/experiment/prompt_r2/p1/salida/ejemplos_mensaje_r2.md.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p1/ejemplos_mensaje_r2.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

P1 = Path(__file__).resolve().parent
REPO = P1.parents[3]
for p in ("data/experiment/b54_catalogo_v3/code", "data/experiment/esq/code",
          "data/experiment/reextraccion_v2/e1_extractor"):
    sys.path.insert(0, str(REPO / p))
sys.path.insert(0, str(P1))
import comun_e1  # noqa: E402
import perfil_e1  # noqa: E402
import mensaje_r2_borrador as MB  # noqa: E402

CASOS = ("cap::1.2", "ric::9.2.1", "cap::6.2.2.6", "cap::4.2.1.2", "ric::S2", "cap::2.13", "ric::11.2.3",
         "cla::5.1.1.1", "ctacte::2.3.4.1", "ext::4.8.6::intro", "ext::4.8.6.1")
E0LG = REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0"
E0R2 = REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2"


def chunk(d: Path, cid: str) -> dict:
    to = cid.split("::")[0]
    x = json.loads((d / f"chunks_{to}.json").read_text(encoding="utf-8"))
    return next(c for c in (x if isinstance(x, list) else x.get("chunks", [])) if c["id"] == cid)


def main() -> None:
    pf = perfil_e1.perfil("v3_b54")
    out = ["# Ejemplos del mensaje de E1 y de la NOTA de E3 (borrador r2b)\n",
           "Generado por `p1/ejemplos_mensaje_r2.py`. El sellado sale de `perfil_e1.perfil('v3_b54')` sobre la E0 "
           "legada; el nuevo, de `p1/mensaje_r2_borrador.py` sobre la E0 e0-r2 (`f8dedd4`).\n"]
    for cid in CASOS:
        lg, r2 = chunk(E0LG, cid), chunk(E0R2, cid)
        out.append(f"## {cid}\n")
        out.append("Mensaje de E1, sellado:\n\n```text\n" + pf.build_user_message(lg) + "\n```\n")
        out.append("Mensaje de E1, nuevo:\n\n```text\n"
                   + MB.build_user_message_r2(r2, pf.rol_por_to, comun_e1.puntos_admitidos, comun_e1.es_mini_chunk)
                   + "\n```\n")
        n_lg = MB.nota_e3_sellada(lg)
        n_r2 = " ".join(x for x in (MB.nota_e3_r2(r2), MB.nota_e3_encabezado_r2(r2)) if x) or None
        out.append(f"NOTA de E3, sellada: {n_lg or '(sin NOTA)'}\n")
        out.append(f"NOTA de E3, nueva: {n_r2 or '(sin NOTA)'}" + (" (igual)" if n_lg == n_r2 else "") + "\n")
    forz = frozenset({"cap::tabla037"})
    r2 = chunk(E0R2, "cap::6.2.2.6")
    out.append("## cap::6.2.2.6 con `cap::tabla037` en la lista de tablas forzadas a residual (demostración)\n")
    out.append("Mensaje de E1, nuevo, con la tabla forzada:\n\n```text\n"
               + MB.build_user_message_r2(r2, pf.rol_por_to, comun_e1.puntos_admitidos, comun_e1.es_mini_chunk,
                                          forzadas=forz) + "\n```\n")
    out.append(f"NOTA de E3, nueva, con la tabla forzada: {MB.nota_e3_r2(r2, forzadas=forz) or '(sin NOTA)'}\n")
    (P1 / "salida" / "ejemplos_mensaje_r2.md").write_text("\n".join(out), encoding="utf-8")
    print(f"{len(CASOS)} casos")


if __name__ == "__main__":
    main()
