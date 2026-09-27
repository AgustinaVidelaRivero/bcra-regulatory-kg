#!/usr/bin/env python3
"""sonda_T1_T7_cuatro_grafos_UB21.py — U-B2.1 fase 1 (re-diagnóstico), pieza e.

Corre, SIN EDITARLOS NI COPIARLOS, los tests T1–T7 de r1
(data/experiment/reextraccion_v2/corpus_v2/r1_tests.py::correr_tests, que
delega T1–T3 en ensamblar_corpus.tests_respuesta_conocida) y las invariantes
I3–I5 de r1_invariantes.verificar_invariantes (con grafos_pre=None: I1 e I2
se omiten porque exigen los grafos pre-merge, que solo existen para la cadena
r1) sobre los cuatro grafos de la decisión 4 del mandato. Verifica los sha256
antes de correr y compara contra los resultados sellados de r1
(salida_r1/tests_respuesta_conocida_r1.json) y de KG-Reextraído
(salida/tests_respuesta_conocida.json).

Solo lectura; imprime por stdout. Corre desde la raíz del repo:
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python3 reports/revision_UB21_diag/sonda_T1_T7_cuatro_grafos_UB21.py
(r1_tests importa schema.py de grafo_v2/code, que requiere pydantic: usar el
intérprete del .venv.)
"""
import sys
sys.dont_write_bytecode = True

import hashlib
import json
import traceback
from collections import Counter
from pathlib import Path

RAIZ = Path.cwd()
CORPUS_V2 = RAIZ / "data" / "experiment" / "reextraccion_v2" / "corpus_v2"
sys.path.insert(0, str(CORPUS_V2))

import r1_comun as C            # noqa: E402  (importado, no editado)
import r1_tests as T            # noqa: E402
import r1_invariantes as INV    # noqa: E402
import ensamblar_corpus as EC   # noqa: E402

GRAFOS = [
    ("KG-Base", "data/experiment/run_3_ppf_core/kg.json",
     "12c226e22b8fdc8f46999cae7f1eb808930e71f5dfe803f3a4f637a88348c410"),
    ("KG-Refinado", "data/experiment/grafo_v2/reensamblado_v3/kg.json",
     "26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571"),
    ("KG-Reextraido", "data/experiment/reextraccion_v2/corpus_v2/salida/kg.json",
     "8e2eadee57b48e00ccb51ade9a953ba1469001fe089c45d97c4307ccf2725581"),
    ("KG-Reextraido-r1", "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json",
     "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"),
]
MUESTRA30 = CORPUS_V2 / "salida_r1" / "referencias_muestra30_inspeccionada_A2.json"
SELLADO_R1 = CORPUS_V2 / "salida_r1" / "tests_respuesta_conocida_r1.json"
SELLADO_V2 = CORPUS_V2 / "salida" / "tests_respuesta_conocida.json"
ORDEN_TESTS = ["T1_bkl0024_ext_3_9", "T2_clausula_125", "T3_pro_1_1_2_5_salvedad",
               "T4_esqueleto_paridad_kg_refinado", "T5_referencias_muestra30",
               "T6_texto_ordenado_5", "T7_cuarentena_sin_padre_inventado"]


def sha256_path(p: str) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def resumen(nombre: str, r: dict) -> str:
    """Una línea compacta por test con los conteos que sostienen el pass."""
    if nombre.startswith("T1"):
        return (f"anclados_3_9={r['nodos_anclados_3_9']} puntos={r['puntos']} "
                f"con_usd_200={len(r['nodos_con_usd_200'])}")
    if nombre.startswith("T2"):
        return (f"nodos_separados_ext={r['n_nodos_separados_ext']} "
                f"puntos_distintos={r['puntos_distintos']}")
    if nombre.startswith("T3"):
        return (f"anclados_1_1_2_5={r['nodos_anclados']} con_salvedad={len(r['nodos_con_salvedad'])} "
                f"de_los_cuales_excepcion={r['de_los_cuales_excepcion']}")
    if nombre.startswith("T4"):
        return (f"esqueleto_esperados={r['nodos_esqueleto_esperados']} faltan_nodos={len(r['faltan_nodos'])} "
                f"aristas_esqueleto_en_grafo={r['aristas_esqueleto_r1']} faltan_triplas={len(r['faltan_triplas'])}")
    if nombre.startswith("T5"):
        pres = Counter(f["presente"] for f in r["fallas"])
        return f"n_muestra={r['n_muestra']} fallas={len(r['fallas'])} (presente_con_otra_evidencia={pres.get(True, 0)}, ausente={pres.get(False, 0)})"
    if nombre.startswith("T6"):
        return f"n={r['n']} ids={r['ids']}"
    if nombre.startswith("T7"):
        motivos = Counter(m.split(" a ")[0].split(" ")[0] if m.startswith("padre_sugerido") else m
                          for _, m in r["malos"])
        return (f"propuestos={r['n_propuestos']} aristas_padre_sugerido={r['n_padre_sugerido']} "
                f"malos={len(r['malos'])} {dict(motivos)} fuera_catalogo_no_propuestos={len(r['sujetos_fuera_catalogo_no_propuestos'])}")
    return ""


def main() -> int:
    print("sonda_T1_T7_cuatro_grafos_UB21 — T1–T7 (r1_tests.correr_tests) + I3–I5 (r1_invariantes.verificar_invariantes)")
    print(f"r1_tests.py      sha256 {sha256_path(str(CORPUS_V2 / 'r1_tests.py'))}")
    print(f"r1_invariantes.py sha256 {sha256_path(str(CORPUS_V2 / 'r1_invariantes.py'))}")
    print(f"muestra30 (T5)   sha256 {sha256_path(str(MUESTRA30))}  {MUESTRA30.relative_to(RAIZ)}")
    muestra = json.loads(MUESTRA30.read_text(encoding="utf-8"))
    sellado_r1 = json.loads(SELLADO_R1.read_text(encoding="utf-8"))
    sellado_v2 = json.loads(SELLADO_V2.read_text(encoding="utf-8"))
    resultados = {}
    for nombre, ruta, sha_esp in GRAFOS:
        sha = sha256_path(ruta)
        print()
        print(f"===== {nombre}  {ruta}")
        print(f"sha256 {sha}  -> {'OK' if sha == sha_esp else 'DIFIERE de ' + sha_esp}")
        if sha != sha_esp:
            print("  FRENO: sha distinto del declarado en el mandato; no se corre.")
            return 1
        kg = json.loads(Path(ruta).read_text(encoding="utf-8"))
        res = {"sha256": sha, "tests": {}, "invariantes": None, "excepcion": None}
        try:
            tests = T.correr_tests(kg, muestra)
        except Exception:                      # noqa: BLE001 — se reporta, no se oculta
            res["excepcion"] = traceback.format_exc().strip().splitlines()[-1]
            print(f"  EXCEPCION en correr_tests: {res['excepcion']}")
            print("  (se corren T1–T3 por separado con ensamblar_corpus.tests_respuesta_conocida)")
            tests = EC.tests_respuesta_conocida(kg)
        for k in ORDEN_TESTS:
            if k in tests:
                r = tests[k]
                res["tests"][k] = {"pass": bool(r["pass"]), "resumen": resumen(k, r)}
                print(f"  {k:36s} {'PASS' if r['pass'] else 'FAIL'}  {resumen(k, r)}")
            else:
                res["tests"][k] = {"pass": None, "resumen": "no corrido (excepcion arriba)"}
                print(f"  {k:36s} ----  no corrido")
        inv = INV.verificar_invariantes(kg)     # grafos_pre=None -> I1/I2 omitidas
        res["invariantes"] = {k: inv[k] for k in ("nodes", "edges", "aristas_colgantes",
                                                   "nodos_sin_provenance", "aristas_sin_provenance", "ok")}
        res["invariantes"]["fallos"] = [f[:90] for f in inv["fallos"]]
        i3 = not any(f.startswith("I3") for f in inv["fallos"])
        i4 = not any(f.startswith("I4") for f in inv["fallos"])
        i5 = not any(f.startswith("I5") for f in inv["fallos"])
        print(f"  I1/I2 conservacion                    N/A   (exigen grafos pre-merge: solo cadena r1)")
        print(f"  I3 unicidad ids/triplas               {'PASS' if i3 else 'FAIL'}  nodes={inv['nodes']} edges={inv['edges']}")
        print(f"  I4 cero colgantes                     {'PASS' if i4 else 'FAIL'}  colgantes={inv['aristas_colgantes']}")
        print(f"  I5 provenance en todo nodo/arista     {'PASS' if i5 else 'FAIL'}  nodos_sin={inv['nodos_sin_provenance']} aristas_sin={inv['aristas_sin_provenance']}")
        for f in inv["fallos"]:
            print(f"     fallo: {f[:110]}")
        resultados[nombre] = res

    print()
    print("===== Comparacion contra los sellados")
    r1 = resultados["KG-Reextraido-r1"]
    ok_r1 = all(r1["tests"][k]["pass"] == sellado_r1[k]["pass"] for k in ORDEN_TESTS)
    print(f"r1 vs salida_r1/tests_respuesta_conocida_r1.json (pass por test): {'IDENTICO' if ok_r1 else 'DIFIERE'}")
    # Igualdad completa del dict de r1 (no solo el pass): recomputo byte a byte.
    kg_r1 = json.loads(Path(GRAFOS[3][1]).read_text(encoding="utf-8"))
    completo_r1 = T.correr_tests(kg_r1, muestra)
    ident = json.dumps(completo_r1, ensure_ascii=False, sort_keys=True) == json.dumps(sellado_r1, ensure_ascii=False, sort_keys=True)
    print(f"r1 recomputado == sellado (dict completo, json canonico): {ident}")
    v2 = resultados["KG-Reextraido"]
    ok_v2 = all(v2["tests"][k]["pass"] == sellado_v2[k]["pass"] for k in ORDEN_TESTS[:3])
    print(f"KG-Reextraido T1–T3 vs salida/tests_respuesta_conocida.json: {'IDENTICO' if ok_v2 else 'DIFIERE'}")

    print()
    print("===== Matriz pass (T1–T7, I3–I5) por grafo")
    cab = "test".ljust(36) + "".join(n.ljust(18) for n, _, _ in GRAFOS)
    print(cab)
    for k in ORDEN_TESTS:
        fila = k.ljust(36)
        for n, _, _ in GRAFOS:
            p = resultados[n]["tests"][k]["pass"]
            fila += ("PASS" if p else ("FAIL" if p is False else "----")).ljust(18)
        print(fila)
    for inv_k, etiqueta in (("I3", "I3_unicidad"), ("I4", "I4_colgantes"), ("I5", "I5_provenance")):
        fila = etiqueta.ljust(36)
        for n, _, _ in GRAFOS:
            fallos = resultados[n]["invariantes"]["fallos"]
            fila += ("FAIL" if any(f.startswith(inv_k) for f in fallos) else "PASS").ljust(18)
        print(fila)
    canon = json.dumps(resultados, ensure_ascii=False, sort_keys=True)
    print()
    print(f"sha256 del JSON canonico de resultados (determinismo): {hashlib.sha256(canon.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
