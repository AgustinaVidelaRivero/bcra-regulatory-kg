"""N7c, C2-bis: la pregunta del humo de B2, elegida y escrita por código. La regla: de las preguntas de N3 de tipo
`varios_puntos` y subtipo `remision`, la primera por id con todas sus anclas en la sección de la primera (la regla de B1,
n7c/c1/b1_n7c.py, «El techo en N3»: cada ancla que no es la primera está entre los puntos que la sección de N7c lista dentro de
su tope, para el punto de la primera). NavegadorRel de la copia sobre el Neo4j de B6.3, solo en lectura (cada sesión con acceso
de lectura y sin notificaciones, y cada consulta controlada contra las palabras de escritura de Cypher), con el índice por punto
de la config de N7c. La huella del Neo4j, antes y después.
Escribe la pregunta elegida, tal cual está en N3, en <salida de la pregunta> (un archivo nuevo, fuera del repo y del paquete de
revisión), y en <salida.json> solo cuentas y el sha256 de ese archivo. No imprime ninguna pregunta, ningún criterio, ningún
ancla y ningún id.
Uso: NEO4J_URI=bolt://127.0.0.1:47687 <python del .venv> -B elegir_pregunta_humo_n7c.py <raiz de la copia> <preguntas_N3.json>
     <salida de la pregunta> <salida.json>
"""
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, PREG, HUMO, SALIDA = (Path(x).resolve() for x in sys.argv[1:5])
BANCO = RAIZ / "data" / "experiment" / "banco_mcp"
for _p in (BANCO / "mcp_kg", BANCO / "b63" / "v2" / "b2", RAIZ / "data" / "experiment" / "neo4j"):
    sys.path.insert(0, str(_p))

import neo4j  # noqa: E402
import familias_nav_rel as FNR  # noqa: E402
import control_neo4j_b63 as CNB  # noqa: E402
from conexion import abrir_driver  # noqa: E402
from grafos import GRAFOS  # noqa: E402

SHA_N3 = "6a92d18145e4957f39a0b87d9193a38ca592128c6e248fac0b8d1c9ecd82613b"
HUELLA_B63 = "2645da6d01795d520f3c4ab5e237050c530238061f849cd7d1e0170be9223463"
ESCRITURA = re.compile(r"\b(CREATE|MERGE|SET|DELETE|DETACH|REMOVE|DROP|LOAD\s+CSV|FOREACH)\b|CALL\s+(?!\{)", re.I)
CAMPOS_NEO4J = ("ok", "kg_meta_sha256", "n_nodos", "n_aristas", "huella_estado", "huella_contenido")


class SesionLectura:
    def __init__(self, s, consultas: Counter):
        self.s, self.consultas = s, consultas

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.s.close()
        return False

    def run(self, cypher, **params):
        if ESCRITURA.search(cypher):
            raise SystemExit("ABORTO: una consulta con una palabra de escritura")
        self.consultas["n"] += 1
        return self.s.run(cypher, **params)


class DriverLectura:
    def __init__(self, d):
        self.d, self.consultas = d, Counter()

    def session(self, **kw):
        return SesionLectura(self.d.session(default_access_mode=neo4j.READ_ACCESS, notifications_min_severity="OFF", **kw),
                             self.consultas)

    def close(self):
        self.d.close()


def main() -> int:
    if HUMO.exists():
        raise SystemExit("ABORTO: el archivo de la pregunta del humo tiene que ser nuevo")
    res = {"unidad": "N7c, C2-bis: la pregunta del humo de B2 (solo cuentas)"}
    res["neo4j_antes"] = {k: v for k, v in CNB.estado(HUELLA_B63).items() if k in CAMPOS_NEO4J}
    if not res["neo4j_antes"]["ok"]:
        raise SystemExit("ABORTO: el Neo4j de B6.3 no da su huella")
    b = PREG.read_bytes()
    if hashlib.sha256(b).hexdigest() != SHA_N3:
        raise SystemExit("ABORTO: las preguntas de N3 no dan su sha256")
    n3 = json.loads(b)
    P = sorted(n3["preguntas"], key=lambda p: p["id"])
    cfg = json.loads((BANCO / "n7c" / "config_mcp_kg_n7c_evaluado.json").read_text(encoding="utf-8"))
    drv = DriverLectura(abrir_driver())
    try:
        nav = FNR.NavegadorRel(drv, GRAFOS[cfg["grafo"]]["label"], (BANCO / "mcp_kg" / cfg["indice_puntos"]).resolve(),
                               sha256_manifiesto=cfg["sha256_manifiesto_indice"], hubs_esperados=cfg["hubs_esperados"])

        def clave(a: dict):
            return nav.resolver_punto(f"{a['to']}::{re.sub(r'[.]+$', '', a['punto'].strip())}")

        cuenta, elegida, posicion = Counter(), None, None
        for p in P:
            if p["tipo"] != "varios_puntos" or p.get("subtipo") != "remision":
                continue
            cuenta["de_remision"] += 1
            cl = [clave(a) for a in p["gold"]["anclas"]]
            primero, otras = cl[0], sorted({c for c in cl[1:] if c != cl[0]}, key=str)
            if primero is None or not otras or None in otras:
                cuenta["sin_primero_en_el_indice_o_sin_otras"] += 1
                continue
            vista = [f[0] for f in nav.relacionados(primero)][:FNR.TOPE_RELACIONADOS]
            if all(c in vista for c in otras):
                cuenta["con_todas_en_la_seccion"] += 1
                if elegida is None:
                    elegida, posicion = p, cuenta["de_remision"]
        res["remision"] = dict(sorted(cuenta.items()))
        res["la_regla_da_una_pregunta"] = elegida is not None
        res["posicion_entre_las_de_remision_por_id"] = posicion
        res["consultas_al_neo4j"] = drv.consultas["n"]
    finally:
        drv.close()
    if elegida is None:
        raise SystemExit("FRENO: la regla no da ninguna pregunta")
    HUMO.parent.mkdir(parents=True, exist_ok=True)
    HUMO.write_text(json.dumps({"version": n3.get("version", 1),
                                "unidad": "N7c, humo de B2: la pregunta del humo, tal cual en N3 "
                                          "(n7c/c2bis/elegir_pregunta_humo_n7c.py)",
                                "preguntas": [elegida]}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    res["sha256_archivo_de_la_pregunta"] = hashlib.sha256(HUMO.read_bytes()).hexdigest()
    res["anclas_de_la_pregunta"] = len(elegida["gold"]["anclas"])
    res["criterios_de_la_pregunta"] = len(elegida["gold"]["criterios"])
    res["neo4j_despues"] = {k: v for k, v in CNB.estado(HUELLA_B63).items() if k in CAMPOS_NEO4J}
    res["neo4j_igual"] = res["neo4j_antes"] == res["neo4j_despues"]
    SALIDA.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: res[k] for k in ("remision", "la_regla_da_una_pregunta", "posicion_entre_las_de_remision_por_id",
                                          "anclas_de_la_pregunta", "criterios_de_la_pregunta",
                                          "sha256_archivo_de_la_pregunta", "consultas_al_neo4j", "neo4j_igual")},
                     ensure_ascii=False))
    return 0 if res["neo4j_igual"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
