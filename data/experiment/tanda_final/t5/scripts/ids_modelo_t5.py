"""B6.1, tanda final, T5, punto 5: los ids de modelo que devolvió la API, por etapa, para los 98 TOs. Usa sin cambios
t2/freno_modelo_t2.py (importado; su sha256 se controla): copia las tres bases del runner (E1, los reintentos de E1 de la fase de E3 y
E3) a <trabajo>, fuera del repo, y en la copia cruza `access_log` (run_label corpus_<TO>_e1, _reintentos_e1 y _e3) con `cache.model`,
que es el id de la respuesta.
  - E1: el conjunto de ids y cuántas llamadas devolvió cada uno (las de E1 no son reintentos de E3).
  - Los reintentos de E1 de la fase de E3 y E3: solo el conjunto de ids. Cuántas llamadas son cuenta los reintentos de E3 (cegamiento de
    U-MED-VERIF): esas cuentas van solo a <NO_ABRIR.json>, que no se abre.
  - Contra lo esperado: el pre-registro de la tanda final, §2 (E1 frena si una llamada devuelve otro id que claude-haiku-4-5-20251001; E3
    usa claude-sonnet-5) y el freno por modelo de T2 (OK, con esos dos ids). El manifiesto de la extracción no nombra ids de modelo.
Solo lee el repo; escribe <salida.json>, <NO_ABRIR.json> y la copia de las bases en <trabajo>.
Uso: python3 -I -B ids_modelo_t5.py <raíz> <trabajo> <salida.json> <NO_ABRIR.json>
"""
import hashlib
import importlib.util
import json
import sqlite3
import sys
from pathlib import Path

sys.dont_write_bytecode = True
R, W, OUT, OUT_NA = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3]), Path(sys.argv[4])
FM = R / "data/experiment/tanda_final/t2/freno_modelo_t2.py"
assert hashlib.sha256(FM.read_bytes()).hexdigest() == "35ee2094d28454f9c2bdd0ce52e5305226bbf833413eba2bfe4bb8ac9d4d43b4"
spec = importlib.util.spec_from_file_location("freno_modelo_t2", FM)
fm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fm)
assert not W.is_relative_to(R), "la copia de las bases va fuera del repo"
tramos = json.loads((R / "data/experiment/tanda_final/preregistro/tramos_tanda_final.json").read_text(encoding="utf-8"))
tos = list(tramos["tramo_1_tos"]) + list(tramos["tramo_2_tos"])
assert len(tos) == 98
copias = fm.copiar_bases(R, W)
ids, cuentas = {}, {}
for nombre, db in copias.items():
    etiquetas = [fm.ETIQUETA[nombre].format(t) for t in tos]
    marcas = ",".join("?" * len(etiquetas))
    con = sqlite3.connect(str(db))
    try:
        filas = con.execute(f"SELECT c.model, COUNT(*) FROM access_log a JOIN cache c ON c.key = a.key "
                            f"WHERE a.run_label IN ({marcas}) GROUP BY c.model ORDER BY c.model", etiquetas).fetchall()
    finally:
        con.close()
    ids[nombre] = [m for m, _ in filas]
    cuentas[nombre] = {m: n for m, n in filas}
esperado = {"e1": [fm.ID_E1], "e1_reintentos": [fm.ID_E1], "e3": ["claude-sonnet-5"]}
res = {"tos": len(tos),
       "e1": {"ids": ids["e1"], "llamadas_por_id": cuentas["e1"], "esperado": esperado["e1"], "igual": ids["e1"] == esperado["e1"]},
       "e1_reintentos_de_la_fase_de_e3": {"ids": ids["e1_reintentos"], "esperado": esperado["e1_reintentos"],
                                          "igual": ids["e1_reintentos"] in (esperado["e1_reintentos"], []),
                                          "cuantas_llamadas": "en el NO_ABRIR_ (cuenta los reintentos de E3)"},
       "e3": {"ids": ids["e3"], "esperado": esperado["e3"], "igual": ids["e3"] == esperado["e3"],
              "cuantas_llamadas": "en el NO_ABRIR_ (cuenta los reintentos de E3)"},
       "freno_por_modelo_de_T2": "OK, con claude-haiku-4-5-20251001 en E1 y claude-sonnet-5 en E3 (t2/FRENO_T2.md, resultado)",
       "manifiesto": "no nombra ids de modelo; los esperados salen del pre-registro de la tanda final, §2"}
res["todo_igual_a_lo_esperado"] = all(res[k]["igual"] for k in ("e1", "e1_reintentos_de_la_fase_de_e3", "e3"))
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
OUT_NA.write_text(json.dumps({"llamadas_por_id": {"e1_reintentos_de_la_fase_de_e3": cuentas["e1_reintentos"], "e3": cuentas["e3"]}},
                             ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: (v["ids"] if isinstance(v, dict) and "ids" in v else v) for k, v in res.items()}, ensure_ascii=False))
print("e1, llamadas por id:", res["e1"]["llamadas_por_id"])
