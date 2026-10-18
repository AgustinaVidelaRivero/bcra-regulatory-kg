"""Selftest de juez_desamb_mesa.py (mesa, §142 y §143): casos sintéticos en una carpeta temporal, sin datos del grafo vigente y SIN NINGUNA
LLAMADA A LA API (las corridas usan un cliente falso). Uso: python3 -I -B selftest_juez_desamb_mesa.py <carpeta temporal>"""
import argparse
import csv
import importlib.util
import inspect
import json
import random
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace

sys.dont_write_bytecode = True
AQUI = Path(__file__).resolve().parent
P4 = AQUI.parent / "parte4"
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
      "E5": {}, "E6": dict(mencion_verificada="no"), "E7": dict(metodo_resolucion="R2_id_slug", resuelto_a="S_r"),
      "E8": dict(metodo_resolucion="R2_calificador", resuelto_a="S_r"), "E9": dict(metodo_resolucion="R3", resuelto_a="S_r")}
filas, k = [], 0
for est, n in (("E1", 70), ("E2", 60), ("E3", 70), ("E4", 80), ("E5", 70), ("E6", 70), ("E7", 3), ("E8", 4), ("E9", 5)):
    for _ in range(n):
        k += 1
        filas.append(fila(k, **KW[est]))
random.Random(5).shuffle(filas)
(TMP / "res.jsonl").write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in filas), encoding="utf-8")
(TMP / "e0" / "chunks_d1.json").write_text(json.dumps([{"id": f"d1::{i}", "texto": f"texto {i}", "herencia": [{"unidad_origen": "S1", "texto": "encab"}]}
                                                       for i in range(1, k + 1)]), encoding="utf-8")
(TMP / "cat.json").write_text(json.dumps({"sujetos": [{"id": "S_m", "label": "Bancos", "alias": [], "definicion": "d", "padre": None},
                                                      {"id": "S_r", "label": "Rol", "alias": [], "definicion": None, "padre": None,
                                                       "rol": {"miembros": ["S_m"]}}]}), encoding="utf-8")
(TMP / "rol.json").write_text(json.dumps({"TO_d1.pdf": {"rol_id": "S_r", "label": "Rol"}}), encoding="utf-8")
reg = lambda i: {"chunk_id": f"d1::{i}", "estado_e3": "NO_DEBE_COPIARSE", "validacion": {"entidades": [{"local_id": "e1", "type": "Obligacion",  # noqa: E731
                 "label": f"norma {i}", "properties": {}}], "relaciones": [{"indice_crudo": 0, "predicate": "aplica_a", "source": "e1", "sujeto_mencion": "x"}]}}
(TMP / "runner" / "d1" / "extracciones_finales_r2_d1.jsonl").write_text("".join(json.dumps(reg(i)) + "\n" for i in range(1, k + 1)), encoding="utf-8")
run = lambda script, *a: subprocess.run([sys.executable, "-I", "-B", str(script), *a], capture_output=True, text=True)  # noqa: E731
PL, CAL, JZ = P4 / "planilla_desamb_mesa.py", P4 / "calibradores_v2_mesa.py", AQUI / "juez_desamb_mesa.py"
comunes = ["--e0", str(TMP / "e0"), "--salida-runner", str(TMP / "runner"), "--catalogo", str(TMP / "cat.json"), "--rol-por-to", str(TMP / "rol.json")]
assert run(PL, "sortear", "--resolucion", str(TMP / "res.jsonl"), "--semilla", "prueba", "--salida", str(TMP / "s")).returncode == 0
assert run(PL, "normas", "--lista", str(TMP / "s"), "--lista-resolucion", str(TMP / "res.jsonl"), "--salida-runner", str(TMP / "runner")).returncode == 0
r = run(PL, "planilla", "--lista", str(TMP / "s"), "--lista-resolucion", str(TMP / "res.jsonl"), *comunes, "--salida", str(TMP / "pl"))
assert r.returncode == 0, r.stderr
cb = ["--lista", str(TMP / "s" / "lista_muestra.json"), "--sello", str(TMP / "s" / "sello_muestra.json"), "--resolucion", str(TMP / "res.jsonl"),
      "--semilla", "prueba", "--salida", str(TMP / "c")]
assert run(CAL, "sortear", *cb).returncode == 0
assert run(CAL, "normas", "--salida", str(TMP / "c"), "--resolucion", str(TMP / "res.jsonl"), "--salida-runner", str(TMP / "runner")).returncode == 0
r = run(CAL, "planilla", "--salida", str(TMP / "c"), "--resolucion", str(TMP / "res.jsonl"), *comunes, "--planilla", str(TMP / "pc"), "--clave", str(TMP / "kc"))
assert r.returncode == 0, r.stderr
# la hoja de la autora de la lectura, con una marca que no puede aparecer en ningún pedido
claveL = json.loads((TMP / "pl" / "CLAVE_aparte_no_abrir_antes_de_cerrar_la_lectura.json").read_text(encoding="utf-8"))
salt = sorted(c["item"] for c in claveL if c["grupo"] == "calibracion")
(TMP / "saltear.txt").write_text("encabezado\n\n" + ", ".join(salt) + "\n", encoding="utf-8")
with open(TMP / "hoja_lectura.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["item", "letra", "entrada_id", "etiqueta", "clase", "nota"])
    for c in claveL:
        for e in c["entradas"]:
            w.writerow([c["item"], e["letra"], e["id"], "", "" if c["grupo"] == "calibracion" else ("correcta" if e["de"] != "regla_texto" else "incorrecta"),
                        "MARCA_DE_LA_AUTORA_QUE_EL_JUEZ_NO_VE"])
J = ["--salida", str(TMP / "j")]
r = run(JZ, "preparar", "--lista", str(TMP / "s" / "lista_muestra.json"), "--sello", str(TMP / "s" / "sello_muestra.json"), "--resolucion", str(TMP / "res.jsonl"),
        "--planilla-lectura", str(TMP / "pl" / "planilla_lectura.json"), "--clave-planilla", str(TMP / "pl" / "CLAVE_aparte_no_abrir_antes_de_cerrar_la_lectura.json"),
        "--planilla-calibradores", str(TMP / "pc" / "planilla_calibradores.json"), *comunes, *J, "--clave", str(TMP / "kj"))
ok(r.returncode == 0, f"preparar ({r.stdout.strip()[:220]} {r.stderr[-300:]})")
items = json.loads((TMP / "j" / "items_juez.json").read_text(encoding="utf-8"))["items"]
mapa = json.loads((TMP / "kj" / "mapa_items_juez.json").read_text(encoding="utf-8"))
lst = json.loads((TMP / "s" / "lista_muestra.json").read_text(encoding="utf-8"))
n_juez = sum(1 for x in lst["lista"] if x["grupo"] == "juez")
ok(sum(1 for m in mapa if "lectura" in m["grupos"]) == 52 and sum(1 for m in mapa if "juez" in m["grupos"]) == n_juez,
   f"los ítems: las 52 de la lectura y los {n_juez} de la muestra del juez, una fila que está en las dos se juzga una vez ({len(items)} distintos)")
pl_items = {h["item"]: h for h in json.loads((TMP / "pl" / "planilla_lectura.json").read_text(encoding="utf-8"))["items"]}
ok(all(h == pl_items[h["item"]] for h in items if h["item"].startswith("D")), "las 52 van tal cual las ve la autora en su planilla")
r = run(JZ, "seco", *J, "--planilla-calibradores", str(TMP / "pc" / "planilla_calibradores.json"))
ok(r.returncode == 0, f"la prueba en seco ({r.stdout.strip()[:260]} {r.stderr[-300:]})")
res = json.loads((TMP / "j" / "resumen_prueba_en_seco_juez.json").read_text(encoding="utf-8"))
ok(res["pedidos"] == 3 * len(items) and all(v for k2, v in res["controles"].items() if k2 != "sdk_importado") and not res["controles"]["sdk_importado"],
   f"en seco: {res['pedidos']} pedidos armados, 3 por ítem, sin importar el SDK; prefijos distintos por repetición; relleno marcado")
sys.path.insert(0, str(AQUI))
spec = importlib.util.spec_from_file_location("juez", str(JZ))
JM = importlib.util.module_from_spec(spec)
spec.loader.exec_module(JM)
anexo = (TMP / "j" / "anexo_juez.md").read_text(encoding="utf-8").rstrip("\n")
cal = json.loads((TMP / "pc" / "planilla_calibradores.json").read_text(encoding="utf-8"))
pls = JM._plantilla(anexo, JM._bloque_calibradores(cal["items"]))
todos = "".join(json.dumps(JM.pedido(JM.prompt_sistema(pls, 1), h), ensure_ascii=False) for h in items)
ok("MARCA_DE_LA_AUTORA_QUE_EL_JUEZ_NO_VE" not in todos and "NO_DEBE_COPIARSE" not in todos, "ningún pedido trae una clasificación de la autora de las 52 ni estado_e3")
ok(not any(f"## {h['item']}" in todos for h in items) and "## Ítem" in todos, "el juez no ve el número del ítem (ni D ni J)")
ok(all(w not in todos for w in ("metodo_resolucion", "R4_sugerencia", "regla_texto", "estrato", "desacuerdo")), "ni la vía ni el estrato")
src = {n: inspect.getsource(getattr(JM, n)) for n in ("preparar", "seco", "calibradores", "humo", "correr", "_corrida", "_llamar", "pedido")}
ok(not any("hoja_lectura" in s for s in src.values()) and "hoja_lectura" in inspect.getsource(JM.evaluar),
   "solo «evaluar», después de las corridas, lee la hoja de la autora de las 52")
ok("Rol; sus miembros" not in anexo and "Es un rol; sus miembros: Bancos" in anexo and "Es el alcance de: TO_d1.pdf" in anexo, "el anexo de las entradas va en el prefijo, con los miembros y el alcance")
props = JM.HERRAMIENTA["input_schema"]["properties"]["entradas"]["items"]
ok(list(props["properties"]) == ["letra", "porque", "clase"] and props["required"] == ["letra", "porque", "clase"],
   "la herramienta: los campos en el orden letra, porque y clase (§143)")
ok("cita, entre comillas, las palabras del texto que identifican al sujeto" in props["properties"]["porque"]["description"],
   "el porqué cita las palabras del texto que identifican al sujeto")
for frase in ("no se ajusta sin una decisión de la autora", "ningún ajuste se justifica mirando las clasificaciones de la autora", "68 de 78",
              "sin segunda vuelta", "requiere_adjudicacion", "En cada entrada va primero `porque`",
              "cita, entre comillas, las palabras del texto que identifican al sujeto"):
    ok(frase in JM.PLANTILLA, f"el prompt dice: «{frase}»")
# los calibradores: frena si la hoja está incompleta; carga si está completa
hoja_c = TMP / "pc" / "hoja_calibradores.csv"
filas_c = list(csv.DictReader(open(hoja_c, encoding="utf-8")))
r = run(JZ, "calibradores", *J, "--planilla-calibradores", str(TMP / "pc" / "planilla_calibradores.json"), "--hoja-calibradores", str(hoja_c))
ok(r.returncode != 0 and "no tiene clase" in (r.stdout + r.stderr), "con la hoja de los calibradores vacía, la carga frena")
with open(hoja_c, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(filas_c[0].keys()), lineterminator="\n")
    w.writeheader()
    for x in filas_c:
        w.writerow({**x, "clase": "generica", "nota": f"porqué de prueba {x['item']}{x['letra']}"})
r = run(JZ, "calibradores", *J, "--planilla-calibradores", str(TMP / "pc" / "planilla_calibradores.json"), "--hoja-calibradores", str(hoja_c))
plc = (TMP / "j" / "plantilla_con_calibradores.md").read_text(encoding="utf-8") if r.returncode == 0 else ""
ok(r.returncode == 0 and "porqué de prueba" in plc and JM.MARCA_RELLENO not in plc and plc.count("### Ejemplo") == 12 and "### Ejemplo K" not in plc
   and "porqué: porqué de prueba" in plc and plc.index("porqué: porqué de prueba") < plc.index("clase **generica**"),
   "con la hoja completa, los 12 ejemplos resueltos (caso, clase y porqué) entran al prompt, sin su número K")
# los controles de la corrida
sello_ok = TMP / "sello_lectura.json"
sello_ok.write_text(json.dumps({"sellado": "2026-10-21 12:00:00 -0300"}), encoding="utf-8")
sello_tarde = TMP / "sello_lectura_tarde.json"
sello_tarde.write_text(json.dumps({"sellado": "2026-10-21 18:30:00 -0300"}), encoding="utf-8")
base_a = dict(salida=str(TMP / "j"), autorizacion="12:00:00 del 24/10", sello_lectura=str(sello_ok), sello_tanda_final="abcdef12", repo=str(TMP / "repo_falso"))
dentro = datetime(2026, 10, 24, 12, 0, tzinfo=timezone(timedelta(hours=-3)))
ok(JM.controles_de_corrida(argparse.Namespace(**base_a), ahora=dentro, ps="") == [], "con todo en regla, los controles pasan")
casos = [("sin la autorización", dict(autorizacion=None), {}), ("con la lectura cerrada tarde", dict(sello_lectura=str(sello_tarde)), {}),
         ("sin el sello de la tanda final", dict(sello_tanda_final=None), {}), ("después del 27/10", {}, dict(ahora=datetime(2026, 10, 28, 9, 0, tzinfo=timezone.utc))),
         ("con una extracción corriendo", {}, dict(ps="/x/.venv/bin/python -B data/experiment/tanda1/t2/lanzar_t2.py --trabajo-bases y")),
         ("con la salida dentro del repo", dict(repo=str(TMP)), {})]
for que, cambio, kw in casos:
    f = JM.controles_de_corrida(argparse.Namespace(**{**base_a, **cambio}), **{"ahora": dentro, "ps": "", **kw})
    ok(len(f) >= 1, f"frena {que}: {f}")
print("  aviso: el control real de procesos ve hoy", len(JM.procesos_de_extraccion()), "procesos de extracción (con T2 corriendo, la humo frenaría)")


class Falso:
    """Un cliente sin red: devuelve una clasificación por cada letra del ítem. `malas` = cuántas salidas mal formadas devuelve primero."""
    def __init__(self, malas=0):
        self.llamadas, self.malas = 0, malas
        self.messages = self

    def create(self, **kw):
        self.llamadas += 1
        txt = kw["messages"][0]["content"]
        letras = [l.split("**")[1].rstrip(".") for l in txt.split("\n") if l.startswith("- **") and l[4:5].isalpha() and l[5:7] == ".*"]
        u = SimpleNamespace(input_tokens=900, output_tokens=150, cache_creation_input_tokens=0, cache_read_input_tokens=12000)
        if self.malas > 0:
            self.malas -= 1
            return SimpleNamespace(content=[SimpleNamespace(type="text", text="sin herramienta")], usage=u, stop_reason="end_turn")
        ent = [{"letra": L, "porque": "«las entidades»: x", "clase": "correcta"} for L in letras]
        return SimpleNamespace(content=[SimpleNamespace(type="tool_use", name="clasificar", input={"entradas": ent})], usage=u, stop_reason="tool_use")


fc = Falso()
a = argparse.Namespace(**base_a, cliente_de_prueba=fc, ps_de_prueba="")
JM.humo(a)
reg_h = [json.loads(l) for l in open(TMP / "j" / "registro_humo.jsonl", encoding="utf-8")]
ok(fc.llamadas == 5 and len(reg_h) == 5 and all(x["valida"] for x in reg_h), "la humo hace 5 llamadas (cliente falso) y las registra con su uso")
g = json.loads((TMP / "j" / "presupuesto_juez.json").read_text())["gasto_usd"]
ok(abs(g - 5 * JM.costo_de({"input_tokens": 900, "output_tokens": 150, "cache_read_input_tokens": 12000})) < 1e-9, f"la cuenta propia suma el costo real de cada llamada ({g:.6f})")
try:
    JM.humo(argparse.Namespace(**base_a, cliente_de_prueba=Falso(), ps_de_prueba="lanzar_t2.py corriendo"))
    ok(False, "con una extracción corriendo, la humo no llama")
except SystemExit as e:
    ok("extracción corriendo" in str(e), "con una extracción corriendo, la humo no llama a la API")
(TMP / "j" / "presupuesto_juez.json").write_text(json.dumps({"gasto_usd": 39.999, "tope_usd": 40}), encoding="utf-8")
try:
    JM.humo(argparse.Namespace(**base_a, cliente_de_prueba=Falso(), ps_de_prueba=""))
    ok(False, "el tope frena")
except SystemExit as e:
    ok("tope" in str(e), "cerca del tope, frena antes de la llamada")
(TMP / "j" / "presupuesto_juez.json").unlink()
h0 = next(h for h in items if h["item"].startswith("J"))
s0 = JM.prompt_sistema((TMP / "j" / "plantilla_con_calibradores.md").read_text(encoding="utf-8"), 1)
pr = JM.Presupuesto(TMP / "j" / "p2.json")
ok(JM._llamar(Falso(malas=1), pr, TMP / "j" / "r2.jsonl", s0, h0, 1, "t") is not None, "una salida mal formada se reintenta una vez")
ok(JM._llamar(Falso(malas=2), pr, TMP / "j" / "r3.jsonl", s0, h0, 1, "t") is None, "dos mal formadas: esa repetición no vota")
ok(JM.modal(["correcta", "correcta", "incorrecta"]) == "correcta" and JM.modal(["correcta", "generica", "incorrecta"]) is None
   and JM.modal(["requiere_adjudicacion"] * 3) is None and JM.modal([]) is None, "el modal: 2 de 3; sin moda o con «requiere_adjudicacion», a la autora")
ac = JM.acuerdo({("D1", "A"): "correcta", ("D2", "A"): "incorrecta", ("D3", "A"): None}, {("D1", "A"): "correcta", ("D2", "A"): "no_decidible", ("D3", "A"): "incorrecta"})
ok(ac["acuerdan"] == 2 and ac["n"] == 3 and not ac["valido"], "el acuerdo binario: la adjudicación pendiente del juez cuenta como desacuerdo")
JM.correr(argparse.Namespace(**base_a, cliente_de_prueba=Falso(), ps_de_prueba=""))
r = run(JZ, "evaluar", *J, "--mapa", str(TMP / "kj" / "mapa_items_juez.json"), "--hoja-lectura", str(TMP / "hoja_lectura.csv"), "--saltear", str(TMP / "saltear.txt"))
ev = json.loads((TMP / "j" / "evaluacion_juez.json").read_text(encoding="utf-8")) if r.returncode == 0 else {}
ok(r.returncode == 0 and ev["acuerdo"]["n"] == 78, f"evaluar: el acuerdo sobre las 78 clasificaciones ({r.stdout.strip()} {r.stderr[-200:]})")
ok(ev.get("acuerdo", {}).get("acuerdan") == 78 - 26 and not ev["la_cifra_se_usa"] and ev["cifra"] is None,
   "con el juez diciendo «correcta» a todo, las 26 entradas de la regla en E4 difieren: 52 de 78, la cifra no se usa")
# la cifra principal y la de las reglas aplicadas (decisión 7 con el cambio del §143), con votos armados a mano
votos = {}
for m in mapa:
    for e in m["entradas"]:
        votos[f"{m['item']}|{e['letra']}"] = ["incorrecta" if e["de"] == "regla_texto" else "correcta"] * 3
(TMP / "j" / "votos_juez.json").write_text(json.dumps(votos), encoding="utf-8")
ev_args = [*J, "--mapa", str(TMP / "kj" / "mapa_items_juez.json"), "--hoja-lectura", str(TMP / "hoja_lectura.csv"), "--saltear", str(TMP / "saltear.txt")]
r = run(JZ, "evaluar", *ev_args)
ev = json.loads((TMP / "j" / "evaluacion_juez.json").read_text(encoding="utf-8"))
ok(ev["acuerdo"]["acuerdan"] == 78 and ev["la_cifra_se_usa"] and ev["cifra_con_las_reglas_aplicadas_descriptiva"] is None,
   "con 78 de 78, la cifra principal se usa; sin S1 ni S2, no hay cifra con reglas")
pe = ev["cifra"]["criterio"]["por_estrato"]
ok(pe["E4"]["aciertos"] == pe["E4"]["n"], "la cifra principal usa la entrada que está hoy en rs1 (en E4, la del modelo)")
r = run(JZ, "evaluar", *ev_args, "--s1-paso", "--s2-paso")
ev = json.loads((TMP / "j" / "evaluacion_juez.json").read_text(encoding="utf-8"))
cr = ev["cifra_con_las_reglas_aplicadas_descriptiva"]
ok(cr is not None and cr["cifra"]["criterio"]["por_estrato"]["E4"]["aciertos"] == 0 and "E6" not in cr["cifra"]["criterio"]["por_estrato"]
   and cr["a_cuarentena_por_S2"] == 200, "con S1 y S2: en E4 vale la entrada de la regla (de la misma corrida) y E6 sale a cuarentena")
ok(ev["cifra"]["criterio"]["por_estrato"]["E4"]["aciertos"] == ev["cifra"]["criterio"]["por_estrato"]["E4"]["n"], "la cifra principal no cambia con las reglas")
shutil.rmtree(TMP)
print("FALLAS:", len(fallas))
sys.exit(1 if fallas else 0)
