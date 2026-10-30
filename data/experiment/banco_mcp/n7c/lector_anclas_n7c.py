#!/usr/bin/env python3
"""lector_anclas_n7c.py — B2 de N7c: qué anclas consultó cada sesión, con el lector de la enmienda 1 de la atribución
(data/experiment/ev2_reporte/code/atribucion_fallas_nav.py, sin editarlo). Corre con un Python 3.12 o más nuevo (el lector
importa scripts/ucita2_indicadores_banco.py, que no compila con el 3.10 del .venv del repo) y recibe todo por la entrada
estándar.

CONSULTADA, por ancla (la regla de la enmienda, sobre el log R1 de la sesión, sin la re-ejecución de las v1):
  - por texto: el punto del ancla está entre los `textos` de atribucion_fallas_nav.leer_paso de alguna salida de las
    herramientas de navegación (ver_punto del punto, cuando muestra su texto; ver_descendientes, cuando el bloque del punto
    trae su texto);
  - por nodo: ver_nodo o ver_vecinos (las v1) con un nodo del ancla como su `id`, y una salida que no es de error. Los nodos
    del ancla son los de su punto en el índice por punto (`nodos` de puntos.json), sin los contenedores (los que portan más de
    resolucion.CONTENEDOR_MAX_ANCLAS claves y los `TextoOrdenado`), la regla del §2 de la enmienda.
La lectura del índice (el manifiesto de TOs del instrumento, los nodos de cada punto y los ids) es
atribucion_fallas_nav.cargar_lectura (modo «indice»: el índice por punto del grafo evaluado, con su E0 controlada por sha256);
las pruebas, con un índice de juguete sin E0, la arman igual (modo «juguete»).

Entrada (JSON por la entrada estándar):
  {"modo": "indice"|"juguete", "indice": <carpeta>, "sha256_manifiesto": <hex o null>, "repo": <raíz> (modo indice),
   "tos": [{"id", "archivo"}] y "secciones": {to: [...]} (modo juguete),
   "sesiones": [{"id", "anclas": ["to::punto", ...], "log": <log R1 o null>}]}
Salida (JSON por la salida estándar): por sesión, cuántas anclas, cuántas consultadas y si todas; ninguna clave ni texto.
Uso: <python 3.12> -I -B data/experiment/banco_mcp/n7c/lector_anclas_n7c.py < entrada.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / "data" / "experiment" / "ev2_reporte" / "code"))

import atribucion_fallas_nav as AFN  # noqa: E402  (la enmienda 1, sin editar)

V1_CONSULTA = ("ver_nodo", "ver_vecinos")


def lectura_juguete(e: dict) -> dict:
    d = Path(e["indice"])
    puntos = json.loads((d / "puntos.json").read_text(encoding="utf-8"))
    nodos = json.loads((d / "nodos.json").read_text(encoding="utf-8"))
    man = AFN.U.armar_manifiesto(e["tos"], {to: frozenset(v) for to, v in (e.get("secciones") or {}).items()})
    return {"man": man, "nodos_por_punto": {k: list(p["nodos"]) for k, p in puntos.items() if p["tipo"] != "to"},
            "ids": frozenset(nodos)}


def contenedores(indice: Path) -> set:
    nodos = json.loads((indice / "nodos.json").read_text(encoding="utf-8"))
    return {nid for nid, n in nodos.items() if len(n["puntos"]) > AFN.CONTENEDOR_MAX_ANCLAS
            or n["type"] in AFN.IP.TIPOS_FUERA_DE_PUNTO}


def main() -> int:
    if sys.version_info < (3, 12):
        raise SystemExit("ABORTO: el lector de la enmienda necesita Python 3.12 o más nuevo")
    e = json.loads(sys.stdin.read())
    indice = Path(e["indice"])
    lectura = (AFN.cargar_lectura(indice, e.get("sha256_manifiesto"), Path(e["repo"])) if e["modo"] == "indice"
               else lectura_juguete(e))
    fuera = contenedores(indice)
    out = {}
    for s in e["sesiones"]:
        claves = list(dict.fromkeys(AFN.clave_de_ancla(a) for a in s["anclas"]))
        nodos_de = {k: {n for n in lectura["nodos_por_punto"].get(k, ()) if n not in fuera} for k in claves}
        consultadas = set()
        llamadas = AFN.leer_log_r1(Path(s["log"]))["llamadas"] if s.get("log") and Path(s["log"]).is_file() else []
        for ll in llamadas:
            tool, salida = ll.get("tool"), ll.get("output_str")
            if not isinstance(salida, str):
                continue
            if tool in AFN.TOOLS_NAV:
                consultadas |= set(AFN.leer_paso(tool, salida, lectura)["textos"]) & set(claves)
            elif tool in V1_CONSULTA and not AFN.es_salida_de_error(tool, salida):
                nid = (ll.get("input") or {}).get("id")
                consultadas |= {k for k in claves if nid in nodos_de[k]}
        out[s["id"]] = {"anclas": len(claves), "consultadas": len(consultadas), "todas": len(consultadas) == len(claves),
                        "con_llamadas": bool(llamadas)}
    print(json.dumps({"sesiones": out, "lectura": "indice" if e["modo"] == "indice" else "juguete"}, ensure_ascii=False,
                     sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
