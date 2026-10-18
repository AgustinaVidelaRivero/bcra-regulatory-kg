"""Selftest de calibradores_v2_mesa.py (mesa, §141): casos sintéticos en una carpeta temporal, sin datos del grafo vigente.
Uso: python3 -I -B selftest_calibradores_v2_mesa.py <carpeta temporal>"""
import json
import random
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
AQUI = Path(__file__).resolve().parent
TMP = Path(sys.argv[1])
fallas = []


def ok(cond, que):
    print(("OK   " if cond else "FALLA") + " " + que)
    if not cond:
        fallas.append(que)


if TMP.exists():
    shutil.rmtree(TMP)
(TMP / "e0").mkdir(parents=True)
(TMP / "runner" / "d1").mkdir(parents=True)


def fila(k, **kw):
    base = {"to": "d1", "chunk_id": f"d1::{k}", "e0_sha256_completo": "0", "indice_relacion": 0, "punto": str(k), "predicado": "aplica_a",
            "mencion": "las entidades", "sujeto_mencion_modelo": None, "mencion_verificada": "exacta", "sujeto_id_modelo": "S_m",
            "regla_texto": None, "id_regla_texto": None, "criterios": [], "calificador": None, "resuelto_a": "S_m",
            "metodo_resolucion": "R4_sugerencia_modelo", "desacuerdo_regla_modelo": False, "catalogo_sha256": "c"}
    base.update(kw)
    return base


KW = {"E1": dict(metodo_resolucion="R1_label_exacto", resuelto_a="S_r"),
      "E2": dict(metodo_resolucion="R1_label_exacto", resuelto_a="S_r", desacuerdo_regla_modelo=True),
      "E3": dict(regla_texto="R3", id_regla_texto="S_m"), "E4": dict(regla_texto="R2_calificador", id_regla_texto="S_r", desacuerdo_regla_modelo=True),
      "E5": {}, "E6": dict(mencion_verificada="no")}
filas, k = [], 0
for est, n in (("E1", 70), ("E2", 60), ("E3", 70), ("E4", 90), ("E5", 70), ("E6", 75)):
    for _ in range(n):
        k += 1
        filas.append(fila(k, **KW[est]))
random.Random(3).shuffle(filas)
(TMP / "res.jsonl").write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in filas), encoding="utf-8")
(TMP / "e0" / "chunks_d1.json").write_text(json.dumps([{"id": f"d1::{i}", "texto": f"texto {i}", "herencia": []} for i in range(1, k + 1)]), encoding="utf-8")
(TMP / "cat.json").write_text(json.dumps({"sujetos": [{"id": "S_m", "label": "Bancos", "alias": [], "definicion": "d", "padre": None},
                                                      {"id": "S_r", "label": "Rol", "alias": [], "definicion": None, "padre": None}]}), encoding="utf-8")
(TMP / "rol.json").write_text(json.dumps({}), encoding="utf-8")
reg = lambda i: {"chunk_id": f"d1::{i}", "estado_e3": "NO_DEBE_COPIARSE", "validacion": {"entidades": [{"local_id": "e1", "type": "Obligacion",  # noqa: E731
                 "label": f"norma {i}", "properties": {}}], "relaciones": [{"indice_crudo": 0, "predicate": "aplica_a", "source": "e1", "sujeto_mencion": "x"}]}}
(TMP / "runner" / "d1" / "extracciones_finales_r2_d1.jsonl").write_text("".join(json.dumps(reg(i)) + "\n" for i in range(1, k + 1)), encoding="utf-8")
run = lambda script, *a: subprocess.run([sys.executable, "-I", "-B", str(AQUI / script), *a], capture_output=True, text=True)  # noqa: E731
r = run("planilla_desamb_mesa.py", "sortear", "--resolucion", str(TMP / "res.jsonl"), "--semilla", "prueba", "--salida", str(TMP / "s"))
ok(r.returncode == 0, "el sorteo sellado del diseño, sobre los datos sintéticos")
lst = json.loads((TMP / "s" / "lista_muestra.json").read_text(encoding="utf-8"))
base = ["--lista", str(TMP / "s" / "lista_muestra.json"), "--sello", str(TMP / "s" / "sello_muestra.json"), "--resolucion", str(TMP / "res.jsonl"),
        "--semilla", "prueba", "--salida", str(TMP / "c")]
r = run("calibradores_v2_mesa.py", "sortear", *base)
ok(r.returncode == 0, f"sortear los calibradores nuevos ({r.stdout.strip()[:200]} {r.stderr[-200:]})")
l2 = json.loads((TMP / "c" / "lista_calibradores_v2.json").read_text(encoding="utf-8"))
r2 = run("calibradores_v2_mesa.py", "sortear", *base[:-1], str(TMP / "c2"))
ok((TMP / "c" / "lista_calibradores_v2.json").read_bytes() == (TMP / "c2" / "lista_calibradores_v2.json").read_bytes(), "dos veces: la misma lista, byte a byte")
cuenta = {e: sum(1 for x in l2["lista"] if x["estrato_de_la_fila"] == e) for e in ("E4", "E6", "E2")}
ok(cuenta == {"E4": 5, "E6": 5, "E2": 2} and len(l2["lista"]) == 12, f"5 de E4, 5 de E6 y 2 de E2 ({cuenta})")
fuera = {tuple(x["clave"]) for x in lst["lista"] if x["grupo"] in ("lectura", "juez")}
ok(not fuera & {tuple(x["clave"]) for x in l2["lista"]}, "ningún calibrador nuevo es de la lectura ni de la muestra del juez")
orden = lambda f: tuple(f"{x:09d}" if isinstance(x, int) else str(x) for x in (f["to"], f["chunk_id"], f["indice_relacion"], f["predicado"]))  # noqa: E731
import importlib.util  # noqa: E402
_s = importlib.util.spec_from_file_location("tam", str(AQUI.parent / "parte2" / "tamanos_desamb_mesa.py"))
TT = importlib.util.module_from_spec(_s)
_s.loader.exec_module(TT)
pool = sorted([f for f in filas if TT.estrato(f) == "E4" and (f["to"], f["chunk_id"], f["indice_relacion"], f["predicado"]) not in fuera], key=orden)
esperado = random.Random("prueba:calibracion2:E4").sample(pool, 5)
ok([x["clave"] for x in l2["lista"] if x["estrato_de_la_fila"] == "E4"] == [[f["to"], f["chunk_id"], f["indice_relacion"], f["predicado"]] for f in esperado],
   "E4: random.Random(f\"{semilla}:calibracion2:E4\").sample sobre las filas ordenadas, sin la lectura ni el juez")
pb = ["--salida", str(TMP / "c"), "--resolucion", str(TMP / "res.jsonl"), "--salida-runner", str(TMP / "runner")]
pp = ["planilla", *pb, "--e0", str(TMP / "e0"), "--catalogo", str(TMP / "cat.json"), "--rol-por-to", str(TMP / "rol.json"),
      "--planilla", str(TMP / "pl"), "--clave", str(TMP / "k")]
r = run("calibradores_v2_mesa.py", *pp)
ok(r.returncode != 0, "sin el control de normas, la planilla de los calibradores frena")
r = run("calibradores_v2_mesa.py", "normas", *pb)
ok(r.returncode == 0, f"control de normas OK ({r.stdout.strip()})")
r = run("calibradores_v2_mesa.py", *pp)
ok(r.returncode == 0, f"la planilla de los calibradores ({r.stdout.strip()[:160]} {r.stderr[-200:]})")
md = (TMP / "pl" / "planilla_calibradores.md").read_text(encoding="utf-8")
csvt = (TMP / "pl" / "hoja_calibradores.csv").read_text(encoding="utf-8")
cl = json.loads((TMP / "k" / "CLAVE_calibradores_v2.json").read_text(encoding="utf-8"))
items = md[md.index("\n## K"):] + csvt
ok("calibradores" in md[:md.index("\n## K")] and md.count("\n## K") == 12, "dice que son calibradores, 12 ítems K01 a K12")
ok(not any(w in items for w in ("metodo_resolucion", "R4_sugerencia", "regla_texto", "estrato", "desacuerdo", "\"E4\"", "\"E2\"", "NO_DEBE_COPIARSE")),
   "los ítems no dicen la vía ni el estrato, ni copian estado_e3")
ok(csvt.splitlines()[0] == "item,letra,entrada_id,etiqueta,clase,nota" and len(csvt.splitlines()) - 1 == sum(len(c["entradas"]) for c in cl),
   "la hoja tiene la columna nota y una fila por entrada")
ok(all(sorted(e["de"] for e in c["entradas"]) == ["modelo", "regla_texto"] for c in cl if c["estrato_de_la_fila"] == "E4"),
   "E4: las dos entradas, la del modelo y la de la regla, solo en la clave")
p = TMP / "c" / "lista_calibradores_v2.json"
p.write_text(p.read_text(encoding="utf-8").replace("\"E4\"", "\"E4 \"", 1), encoding="utf-8")
r = run("calibradores_v2_mesa.py", "normas", *pb)
ok(r.returncode != 0 and "no es la sellada" in (r.stdout + r.stderr), "si la lista de los calibradores cambia después del sello, frena")
q = TMP / "s" / "lista_muestra.json"
q.write_text(q.read_text(encoding="utf-8") + " ", encoding="utf-8")
r = run("calibradores_v2_mesa.py", "sortear", *base[:-1], str(TMP / "c3"))
ok(r.returncode != 0 and "no es la sellada" in (r.stdout + r.stderr), "si la lista sellada del diseño cambia, el sorteo nuevo frena")
shutil.rmtree(TMP)
print("FALLAS:", len(fallas))
sys.exit(1 if fallas else 0)
