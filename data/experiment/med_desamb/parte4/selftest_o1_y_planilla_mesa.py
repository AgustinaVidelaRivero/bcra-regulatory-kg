"""Selftest de mismo_acto_o1_mesa.py y planilla_desamb_mesa.py (mesa, §139 y §140): casos sintéticos en una carpeta temporal, sin datos
del grafo vigente. Uso: python3 -I -B selftest_o1_y_planilla_mesa.py <dir de e2_lib.py> <carpeta temporal>"""
import importlib.util
import json
import random
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
AQUI = Path(__file__).resolve().parent
E2LIB, TMP = sys.argv[1], Path(sys.argv[2])
fallas = []


def ok(cond, que):
    print(("OK   " if cond else "FALLA") + " " + que)
    if not cond:
        fallas.append(que)


def mod(nombre, ruta):
    s = importlib.util.spec_from_file_location(nombre, str(ruta))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


O1 = mod("o1", AQUI.parent / "parte3" / "mismo_acto_o1_mesa.py")
E = O1.T.cargar_e2lib(E2LIB)


def prov(to, punto, anc):
    return {"to": to, "punto": punto, "chunk_id": f"{to}::{punto}", "rol_documental": "punto_propio", "ancestros": anc}


def op(i, label, to, punto, anc):
    p = prov(to, punto, anc)
    return {"id": i, "type": "Operacion", "label": label, "properties": {"tipo": "t", "descripcion": f"desc {i}"}, "provenance": p, "provenances": [p]}


def rem(to, a, b):
    p = prov(to, a, [])
    return {"source": "x", "target": "y", "relation": "remite_a", "provenance": p, "provenances": [p], "properties": {"alcance": "interna", "destino": f"{to}::{b}"}}


# --- O1 ---
merged = op("u", "Canje", "d1", "7.1", ["S7", "7"])
merged["provenances"].append(prov("d1", "7.2", ["S7", "7"]))
kg = {"nodes": [op("t1", "Transferencia", "d1", "2.1", ["S2", "2"]), op("t2", "Transferencia", "d1", "5.1", ["S5", "5"]),
                op("c1", "Cesión", "d1", "1.1", ["S1", "1"]), op("c2", "Cesión", "d1", "1.2", ["S1", "1"]), op("c3", "Cesión", "d1", "3.4", ["S3", "3"]),
                op("p1", "Pase", "d1", "4.1", ["S4", "4"]), op("p2", "Pase", "d1", "6.1", ["S6", "6"]), op("p3", "Pase", "d2", "4.1", ["S4", "4"]), merged],
      "edges": [rem("d1", "5.1", "2.1")]}
v = O1.vinculos_mismo_acto(E, kg)
ok(sorted((x["a"], x["b"], x["criterio"]) for x in v) == [("c1", "c2", "mismo_padre"), ("t1", "t2", "remite_a")],
   f"O1: solo Cesión 1.1–1.2 (mismo padre) y Transferencia 2.1–5.1 (remite_a, en el otro sentido); ni 3.4, ni Pase, ni otro documento, ni el nodo de r2a en dos puntos ({v})")
ar = O1.aristas_opcion_arista(v)
ok(all(a["relation"] == "mismo_acto" and a["rol_fuente"] == "derivada_mismo_acto" for a in ar) and len(ar) == 2, "O1: la opción arista, una por vínculo, con su marca")

# --- planilla (diseño firmado el 17/10/2026, §140) ---
if TMP.exists():
    shutil.rmtree(TMP)
(TMP / "e0").mkdir(parents=True)
(TMP / "runner" / "d1").mkdir(parents=True)
filas = []
def fila(to, k, **kw):
    base = {"to": to, "chunk_id": f"{to}::{k}", "e0_sha256_completo": "0", "indice_relacion": 0, "punto": str(k), "predicado": "aplica_a",
            "mencion": "las entidades", "sujeto_mencion_modelo": None, "mencion_verificada": "exacta", "sujeto_id_modelo": "S_m",
            "regla_texto": None, "id_regla_texto": None, "criterios": [], "calificador": None, "resuelto_a": "S_m",
            "metodo_resolucion": "R4_sugerencia_modelo", "desacuerdo_regla_modelo": False, "catalogo_sha256": "c"}
    base.update(kw)
    return base
k = 0
KW = {"E1": dict(metodo_resolucion="R1_label_exacto", resuelto_a="S_r"),
      "E2": dict(metodo_resolucion="R1_label_exacto", resuelto_a="S_r", desacuerdo_regla_modelo=True),
      "E3": dict(regla_texto="R3", id_regla_texto="S_m"), "E4": dict(regla_texto="R2_calificador", id_regla_texto="S_r", desacuerdo_regla_modelo=True),
      "E5": {}, "E6": dict(mencion_verificada="no"), "E8": dict(metodo_resolucion="R2_calificador", resuelto_a="S_r")}
for est, n in (("E1", 70), ("E3", 70), ("E4", 40), ("E5", 70), ("E6", 10), ("E2", 5), ("E8", 3)):
    for _ in range(n):
        k += 1
        filas.append(fila("d1", k, **KW[est]))
random.Random(7).shuffle(filas)
(TMP / "res.jsonl").write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in filas), encoding="utf-8")
(TMP / "e0" / "chunks_d1.json").write_text(json.dumps([{"id": f"d1::{i}", "texto": f"texto {i}", "herencia": [{"unidad_origen": "S1", "texto": "encabezado"}]}
                                                       for i in range(1, k + 1)]), encoding="utf-8")
(TMP / "cat.json").write_text(json.dumps({"sujetos": [{"id": "S_m", "label": "Bancos", "alias": ["banco"], "definicion": "d", "padre": "S_x"},
                                                      {"id": "S_r", "label": "Rol", "alias": [], "definicion": None, "padre": None}]}), encoding="utf-8")
(TMP / "rol.json").write_text(json.dumps({"TO_d1.pdf": {"rol_id": "S_rol", "label": "rol de d1", "miembros_labels": ["Bancos"]}}), encoding="utf-8")
def reg(i, sin=None):
    return {"chunk_id": f"d1::{i}", "estado_e3": "NO_DEBE_COPIARSE", "validacion": {"entidades": [{"local_id": "e1", "type": "Obligacion",
            "label": f"norma {i}", "properties": {"descripcion": f"desc {i}"}}], "relaciones": [{"indice_crudo": 0, "predicate": "aplica_a",
            "source": "e1", "sujeto_mencion": "las entidades"}]}}
(TMP / "runner" / "d1" / "extracciones_finales_r2_d1.jsonl").write_text("".join(json.dumps(reg(i)) + "\n" for i in range(1, k + 1)), encoding="utf-8")
PL = AQUI / "planilla_desamb_mesa.py"
corr = lambda *a: subprocess.run([sys.executable, "-I", "-B", str(PL), *a], capture_output=True, text=True)  # noqa: E731
r = corr("sortear", "--resolucion", str(TMP / "res.jsonl"), "--semilla", "prueba", "--salida", str(TMP / "s1"))
ok(r.returncode == 0, f"sortear corre ({r.stdout.strip()[:200]} {r.stderr[-200:]})")
r2 = corr("sortear", "--resolucion", str(TMP / "res.jsonl"), "--semilla", "prueba", "--salida", str(TMP / "s2"))
ok((TMP / "s1" / "lista_muestra.json").read_bytes() == (TMP / "s2" / "lista_muestra.json").read_bytes(), "sortear dos veces: la misma lista, byte a byte")
lst = json.loads((TMP / "s1" / "lista_muestra.json").read_text(encoding="utf-8"))
d = lst["declarado"]
ok((d["E4"]["n"], d["E6"]["n"], d["E6"]["censo"], d["E1"]["n"], d["E3"]["n"], d["E5"]["n"], d["calibracion"]["n"]) == (26, 10, True, 4, 3, 3, 12),
   f"tamaños: E4 26, E6 censo, control fijo 4/3/3, calibración 12 ({ {k2: (v2['n'], v2['N']) for k2, v2 in d.items()} })")
ok(d["juez:E1"]["n"] == 50 and d["juez:E8"]["censo"] and d["juez:E4"]["N"] == 40 - sum(1 for x in lst["lista"] if x["grupo"] == "calibracion" and x["estrato_de_la_fila"] == "E4"),
   "juez: 50 por estrato, censo donde no llega, sin los calibradores")
T = O1.T
orden = sorted([f for f in filas if T.estrato(f) == "E4"], key=lambda f: tuple(f"{x:09d}" if isinstance(x, int) else str(x) for x in (f["to"], f["chunk_id"], f["indice_relacion"], f["predicado"])))
esperado = random.Random("prueba:E4").sample(orden, 26)
ok([x["clave"] for x in lst["lista"] if x["estrato"] == "E4"] == [[f["to"], f["chunk_id"], f["indice_relacion"], f["predicado"]] for f in esperado],
   "E4: random.Random(f\"{semilla}:{estrato}\").sample sobre las filas ordenadas")
lc = [tuple(x["clave"]) for x in lst["lista"] if x["grupo"] in ("lectura", "calibracion")]
ok(len(lc) == len(set(lc)) == 58, "lectura y calibración, disjuntas (58 filas distintas en el caso sintético)")
cal = {tuple(x["clave"]) for x in lst["lista"] if x["grupo"] == "calibracion"}
ok(not cal & {tuple(x["clave"]) for x in lst["lista"] if x["grupo"] == "juez"}, "la muestra del juez no incluye ningún calibrador")
base = ["--lista", str(TMP / "s1"), "--lista-resolucion", str(TMP / "res.jsonl"), "--salida-runner", str(TMP / "runner")]
argsP = ["planilla"] + base + ["--e0", str(TMP / "e0"), "--catalogo", str(TMP / "cat.json"), "--rol-por-to", str(TMP / "rol.json"), "--salida", str(TMP / "p")]
r = corr(*argsP)
ok(r.returncode != 0 and "control de normas" in (r.stdout + r.stderr), "sin el control de normas, la planilla frena")
r = corr("normas", *base)
ok(r.returncode == 0 and json.loads((TMP / "s1" / "control_normas.json").read_text())["ok"], f"control de normas en OK con el registro completo ({r.stdout.strip()})")
r = corr(*argsP)
ok(r.returncode == 0, f"planilla corre ({r.stdout.strip()[:200]} {r.stderr[-300:]})")
pl = json.loads((TMP / "p" / "planilla_lectura.json").read_text(encoding="utf-8"))
cl = json.loads((TMP / "p" / "CLAVE_aparte_no_abrir_antes_de_cerrar_la_lectura.json").read_text(encoding="utf-8"))
md = (TMP / "p" / "planilla_lectura.md").read_text(encoding="utf-8")
csvt = (TMP / "p" / "hoja_clases.csv").read_text(encoding="utf-8")
items_md = md[md.index("\n## D"):]          # la cabecera dice que hay 12 calibradores mezclados; los ítems no dicen cuáles
todo = items_md + csvt + json.dumps(pl, ensure_ascii=False)
print("  palabras vedadas encontradas:", [w for w in ("metodo_resolucion", "R4_sugerencia", "regla_texto", "estrato", "calibra", "\"E4\"", "desacuerdo", "NO_DEBE_COPIARSE") if w in todo])
ok(not any(w in todo for w in ("metodo_resolucion", "R4_sugerencia", "regla_texto", "estrato", "calibra", "\"E4\"", "desacuerdo", "NO_DEBE_COPIARSE")),
   "la planilla (md, csv y json) no dice la vía, el estrato, qué ítem es calibrador, ni copia estado_e3")
grupos = [c["grupo"] for c in cl]
ok(len(cl) == 58 and grupos.count("calibracion") == 12 and "calibracion" in grupos[:29], "los 12 calibradores van mezclados (no todos al final)")
e4 = [c for c in cl if c["estrato_de_la_fila"] == "E4"]
ok(all(sorted(e["de"] for e in c["entradas"]) == ["modelo", "regla_texto"] for c in e4) and len({tuple(e["de"] for e in c["entradas"]) for c in e4}) == 2,
   "E4: las dos entradas, en orden sorteado que varía entre ítems")
filas_csv = csvt.strip().split("\n")[1:]
ok(len(filas_csv) == sum(len(c["entradas"]) for c in cl) and md.count("\n## D") == 58, "el csv tiene una fila por entrada y el md un ítem por sección")
hoja = {h["item"]: h for h in pl["items"]}
ok(all(hoja[c["item"]]["entradas"][j]["id"] == c["entradas"][j]["id"] for c in cl for j in range(len(c["entradas"]))), "la clave y la planilla coinciden letra por letra")
ok(all(h["norma"]["etiqueta"] == f"norma {h['punto']}" for h in pl["items"]), "la norma sale del registro validado, la de cada relación")
# un registro que falta frena el control
lineas = (TMP / "runner" / "d1" / "extracciones_finales_r2_d1.jsonl").read_text(encoding="utf-8").splitlines()
falta = next(h["punto"] for h in pl["items"])
(TMP / "runner" / "d1" / "extracciones_finales_r2_d1.jsonl").write_text("".join(l + "\n" for l in lineas if f'"d1::{falta}"' not in l), encoding="utf-8")
r = corr("normas", *base)
ok(r.returncode != 0 and not json.loads((TMP / "s1" / "control_normas.json").read_text())["ok"], "si falta el registro de una norma, el control da FRENO")
r = corr(*argsP[:-1], str(TMP / "p2"))
ok(r.returncode != 0, "y con el control en FRENO, no hay planilla")
# el sello frena si la lista cambia
pth = TMP / "s1" / "lista_muestra.json"
pth.write_text(pth.read_text(encoding="utf-8").replace("\"E4\"", "\"E4 \"", 1), encoding="utf-8")
r = corr("normas", *base)
ok(r.returncode != 0 and "no es la sellada" in (r.stdout + r.stderr), "si la lista cambia después del sello, todo frena")
shutil.rmtree(TMP)
print("FALLAS:", len(fallas))
sys.exit(1 if fallas else 0)
