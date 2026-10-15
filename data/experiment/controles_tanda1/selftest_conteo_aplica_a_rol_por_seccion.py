"""Selftest del conteo de aplica_a hacia el rol por sección: un grafo sintético con las cuentas conocidas. USD 0, sin datos reales.
Uso: python3 -I -B selftest_conteo_aplica_a_rol_por_seccion.py"""
import json, sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import conteo_aplica_a_rol_por_seccion as C  # noqa: E402

def nodo(i, t, cid, to="doc"):
    return {"id": i, "type": t, "provenance": {"to": to, "chunk_id": cid}}

def arista(s, t, cid, metodo="exacta"):
    return {"source": s, "target": t, "relation": "aplica_a", "metodo_resolucion": metodo, "provenance": {"chunk_id": cid}}

KG = {"nodes": [nodo("n1", "Obligacion", "doc::1.1"), nodo("n2", "Restriccion", "doc::1.2.1"), nodo("n3", "Potestad", "doc::3.1::intro"),
                nodo("n4", "Obligacion", "doc::3.2"), nodo("n5", "Obligacion", "doc::Sbloque1"), nodo("n6", "Operacion", "doc::3.3"),
                nodo("n7", "Obligacion", "doc::S2::chapeau_seccion"), nodo("n8", "Obligacion", "otro::1.1", to="otro"),
                {"id": "R", "type": "Sujeto"}, {"id": "X", "type": "Sujeto"}],
      "edges": [arista("n1", "R", "doc::1.1"), arista("n1", "X", "doc::1.1"), arista("n2", "X", "doc::1.2.1"),
                arista("n3", "R", "doc::3.1::intro", "derivada_de_alcance"), arista("n3", "R", "doc::3.1::intro"),
                arista("n6", "R", "doc::3.3"), arista("n7", "R", "doc::S2::chapeau_seccion"), arista("n8", "R", "otro::1.1"),
                {"source": "n4", "target": "R", "relation": "regula", "provenance": {"chunk_id": "doc::3.2"}}]}
casos = []
d = C.contar(KG, "doc", "R")
casos.append(("normas por sección", dict(d["normas_por_seccion"]) == {"1": 2, "2": 1, "3": 2, "bloques": 1}))
casos.append(("con aplica_a al rol", dict(d["normas_con_aplica_a_al_rol"]) == {"1": 1, "2": 1, "3": 1}))
casos.append(("solo a otro sujeto", dict(d["normas_con_aplica_a_solo_a_otro_sujeto"]) == {"1": 1}))
casos.append(("sin aplica_a (la otra relación no cuenta)", dict(d["normas_sin_aplica_a"]) == {"3": 1, "bloques": 1}))
casos.append(("aristas por método", {k: dict(v) for k, v in d["aristas_al_rol_por_seccion_y_metodo"].items()}
              == {"1": {"exacta": 1}, "2": {"exacta": 1}, "3": {"derivada_de_alcance": 1, "exacta": 1}}))
casos.append(("una Operacion no es norma", d["normas"] == 6))
casos.append(("otro documento no cuenta", d["totales"]["normas_con_aplica_a_al_rol"] == 3 and d["totales"]["aristas_al_rol"] == 4))
casos.append(("sección de los ids", [C.seccion(x) for x in ("doc::10.2", "doc::S11::chapeau_seccion", "doc::Sbloque3", "doc::D1A1::S0::x")]
              == ["10", "11", "bloques", "bloques"]))
with tempfile.TemporaryDirectory() as t:
    kg, out = Path(t) / "kg.json", Path(t) / "out.json"
    kg.write_text(json.dumps(KG), encoding="utf-8")
    rc = C.main(["--kg", str(kg), "--par", "doc:R", "--par", "otro:R", "--out", str(out)])
    o = json.loads(out.read_text(encoding="utf-8"))
    casos.append(("la línea de comandos", rc == 0 and [x["to"] for x in o["documentos"]] == ["doc", "otro"]
                  and o["documentos"][1]["totales"]["normas_con_aplica_a_al_rol"] == 1))
ok = sum(1 for _, v in casos if v)
for n, v in casos:
    print(("ok  " if v else "FAIL"), n)
print(f"{ok}/{len(casos)}")
sys.exit(0 if ok == len(casos) else 1)
