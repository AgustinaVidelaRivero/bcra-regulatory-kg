"""Mesa, §139 (17/10/2026), U-MED-DESAMB, regla candidata O1, PROPUESTA sin aplicar: el vínculo «mismo acto» entre dos Operacion
distintas del mismo documento con la misma clave de texto (la de entity_slug_r2, fase r2b, sin el punto), solo si sus puntos están
conectados por remite_a (en cualquier sentido) o comparten el encabezado padre de E0 (el último de `ancestros`). No une nodos: cada
uno queda en su punto. No escribe en el grafo: devuelve la lista de vínculos (la población del sorteo de O1) y, aparte, las aristas que
agregaría la opción de la arista (relation «mismo_acto», rol_fuente «derivada_mismo_acto»), que hoy no admite el esquema
(modelos_r2.PREDICADOS_DERIVADOS = ("remite_a",), pyd_r2/code/modelos_r2.py:165) ni las shapes (scripts/shapes_validator.py:1129-1135).
Uso: python3 -I -B mismo_acto_o1_mesa.py --e2lib <dir de e2_lib.py> --kg <kg.json> --salida <dir>"""
import argparse
import hashlib
import importlib.util
import itertools
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
AQUI = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("tamanos_desamb_mesa", str(AQUI.parent / "parte2" / "tamanos_desamb_mesa.py"))
T = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(T)


def vinculos_mismo_acto(E, kg):
    R = T.remisiones(kg["edges"])
    PAD = T.padres(kg["nodes"])
    grupos = {}
    for n in kg["nodes"]:
        if n["type"] != "Operacion":
            continue
        for to, punto in T.ocurrencias(n):
            k = E.entity_slug_r2(n, {"to": to, "punto": ""}, fase="r2b")
            grupos.setdefault((to, k), []).append((punto, n["id"]))
    out = []
    for (to, k), occ in sorted(grupos.items()):
        for (pa, a), (pb, b) in itertools.combinations(sorted(set(occ)), 2):
            if a == b or pa == pb:
                continue                     # el mismo nodo (perfil r2a) o el mismo punto: no es un vínculo entre nodos
            rem = (to, pa, pb) in R or (to, pb, pa) in R
            pad = PAD.get((to, pa)) is not None and PAD.get((to, pa)) == PAD.get((to, pb))
            if rem or pad:
                out.append({"to": to, "a": a, "b": b, "punto_a": pa, "punto_b": pb,
                            "criterio": "remite_a_y_padre" if rem and pad else "remite_a" if rem else "mismo_padre"})
    return out


def aristas_opcion_arista(vinculos):
    return [{"source": v["a"], "target": v["b"], "relation": "mismo_acto", "rol_fuente": "derivada_mismo_acto",
             "properties": {"criterio": v["criterio"], "puntos": [v["punto_a"], v["punto_b"]]}} for v in vinculos]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--e2lib", required=True)
    ap.add_argument("--kg", required=True)
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()
    E = T.cargar_e2lib(a.e2lib)
    b = Path(a.kg).read_bytes()
    kg = json.loads(b)
    v = vinculos_mismo_acto(E, kg)
    S = Path(a.salida)
    S.mkdir(parents=True, exist_ok=True)
    (S / "vinculos_o1.json").write_text(json.dumps(v, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (S / "aristas_mismo_acto_opcion_arista.json").write_text(json.dumps(aristas_opcion_arista(v), ensure_ascii=False, indent=1) + "\n",
                                                              encoding="utf-8")
    por = {}
    for x in v:
        por[x["criterio"]] = por.get(x["criterio"], 0) + 1
    print(f"O1 sobre kg {hashlib.sha256(b).hexdigest()[:8]}: {len(v)} vínculos entre nodos distintos, por criterio {por}")


if __name__ == "__main__":
    main()
