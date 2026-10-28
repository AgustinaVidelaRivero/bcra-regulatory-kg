"""selftest_armar_n7_v3_mesa.py — mesa, §312 (27/10/2026; el de la §299 con los casos de la decisión 9): el selftest de armar_n7_v3_mesa.py con análisis de
juguete y los archivos reales de N6 y del grafo evaluado (una copia del repo en HEAD 23559e51). Los casos 1 a 10 son los de la §299, con
la elección «sobre» las 30 y su clave dentro_de_V, como la escribe analizar_n6.py; los 11 a 13, la elección sobre las 26 sin FUERA_D9. Cada caso arma
un análisis con la forma de la salida de analizar_n6.py, con valores escritos a mano, y controla lo que N7 escribe o por qué frena.
  python3 -I -B selftest_armar_n7_v3_mesa.py <armar_n7_v3_mesa.py> <banco_mcp de la copia> <carpeta de trabajo nueva>
"""
import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path

SCRIPT, BANCO, TR = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
TR.mkdir(parents=True, exist_ok=False)
N6 = BANCO / "n6"
AGENTES = N6 / "config_agentes_n6.json"
CONFS = ("B", "T", "T-F1", "T-F2", "T-F3", "T-F4", "T-F5", "T-F6", "F1_bm25", "F1_hibrida")
sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731
res = []


def analisis(fid, elegibles, v30=0.02, al_tope=None, r9=None, entra_hibrida=True, elegida=None, orden=None, pasa=True):
    al_tope = al_tope or {}
    r9 = r9 or {}
    ops = {c: {"sesiones": 90 if c in ("B", "F1_bm25") else 30, "al_tope": al_tope.get(c, 0),
               "r9_medio_por_pregunta_usd": r9.get(c, 0.5)} for c in CONFS}
    fam = {f"T-F{k}": {"elegible": f"T-F{k}" in elegibles} for k in range(1, 7)}
    cands = [c for c in ("B", "T", "T-F1", "T-F2", "T-F3", "T-F4", "T-F5", "T-F6") if c in ("B", "T") or c in elegibles]
    mejor = max(fid[c] for c in cands)
    dentro = [c for c in cands if fid[c] >= mejor - v30 - 1e-12]
    orden_c = sorted(dentro, key=lambda c: (ops[c]["al_tope"], ops[c]["r9_medio_por_pregunta_usd"], -fid[c], c))
    el = {"sobre": "las 30", "candidatas": cands, "dentro_de_V": dentro, "orden_de_desempate": orden or orden_c,
          "elegida": elegida or orden_c[0],
          "caso_de_la_jerarquia": {"pasa": pasa}, "se_preregistra_asi": pasa}
    return {"medidas": {c: {"operativo": ops[c]} for c in CONFS},
            "regla": {"fidelidad_30": {c: fid[c] for c in fid}, "familias": fam, "V": {"30": {"V": v30}}, "eleccion": el,
                      "F1": {"entra_la_hibrida": entra_hibrida}}}


def analisis_d9(fid30, fid26, elegibles, v30, v26, al_tope26, r9_26, elegida=None):
    """Una elección con la forma de la decisión 9: sobre las 26, con V(26) y lo operativo de las 26 de las que quedan dentro de V."""
    a = analisis(fid30, elegibles, v30=v30)
    cands = [c for c in ("B", "T", "T-F1", "T-F2", "T-F3", "T-F4", "T-F5", "T-F6") if c in ("B", "T") or c in elegibles]
    mejor = max(fid26[c] for c in cands)
    dentro = [c for c in cands if fid26[c] >= mejor - v26 - 1e-12]
    orden = sorted(dentro, key=lambda c: (al_tope26.get(c, 0), r9_26.get(c, 0.5), -fid26[c], c))
    a["regla"]["fidelidad_sin_FUERA_D9"] = dict(fid26)
    a["regla"]["V_sin_FUERA_D9"] = {"30": {"V": v26}}
    a["regla"]["eleccion"] = {"sobre": "las 26 sin FUERA_D9 (decisión 9)", "candidatas": cands, "dentro_de_V": dentro,
                              "al_tope": {c: al_tope26.get(c, 0) for c in dentro}, "r9_medio_por_pregunta_usd": {c: r9_26.get(c, 0.5) for c in dentro},
                              "orden_de_desempate": orden, "elegida": elegida or orden[0], "caso_de_la_jerarquia": {"pasa": True},
                              "se_preregistra_asi": True, "con_las_30": a["regla"]["eleccion"]}
    return a


FID = {"B": 0.50, "T": 0.70, "T-F1": 0.69, "T-F2": 0.60, "T-F3": 0.71, "T-F4": 0.55, "T-F5": 0.62, "T-F6": 0.66}


def correr(nombre, a, esperado, agentes=AGENTES, salida=None):
    pa = TR / f"{nombre}.json"
    pa.write_text(json.dumps(a), encoding="utf-8")
    s = salida or (TR / f"salida_{nombre}")
    r = subprocess.run([sys.executable, "-I", "-B", str(SCRIPT), "--analisis", str(pa), "--analisis-rel", f"juguete/{nombre}.json",
                        "--n6", str(N6), "--banco", str(BANCO), "--config-agentes", str(agentes), "--salida", str(s)],
                       capture_output=True, text=True)
    return r, s


def caso(nombre, ok, detalle=""):
    res.append((nombre, ok))
    print(f"{'OK  ' if ok else 'MAL '} {nombre}" + (f": {detalle}" if detalle else ""))


ag = json.loads(AGENTES.read_text(encoding="utf-8"))
bloque = {b["configuracion_n6"]: b["bloque_tools"] for b in ag["brazos"].values()}

# 1. T−F3 elegible y la mejor: la elegida lleva los ejemplos de la familia 6; la híbrida entra; nadie al tope
a1 = analisis(FID, {"T-F3", "T-F1"}, v30=0.005)
r, s = correr("t_f3", a1, 0)
reg = json.loads((s / "n7_configuracion_sellada.json").read_text(encoding="utf-8")) if r.returncode == 0 else {}
cfg = json.loads((s / "config_mcp_kg_n7_evaluado.json").read_text(encoding="utf-8")) if r.returncode == 0 else {}
ev = json.loads((BANCO / "mcp_kg" / "config_mcp_kg_nav_evaluado.json").read_text(encoding="utf-8"))
n6c = json.loads((N6 / "config_mcp_kg_n6_T-F3.json").read_text(encoding="utf-8"))
caso("1. elige T−F3, la mejor entre las elegibles (rc 0)", r.returncode == 0 and reg.get("brazo_grafo", {}).get("configuracion_n6") == "T-F3",
     r.stdout.strip()[:120])
caso("1. la config: las familias, la firma, el denso y la versión de N6; el grafo, el índice y los hubs del evaluado",
     cfg.get("familias") == n6c["familias"] and cfg.get("firma_tools") == n6c["firma_tools"] and cfg.get("denso") == n6c["denso"]
     and cfg.get("version") == n6c["version"] and cfg.get("grafo") == ev["grafo"] and cfg.get("indice_puntos") == ev["indice_puntos"]
     and cfg.get("sha256_manifiesto_indice") == ev["sha256_manifiesto_indice"] and cfg.get("hubs_esperados") == ev["hubs_esperados"]
     and cfg.get("kg_sha256_esperado") == ev["kg_sha256_esperado"])
mcp = json.loads((s / "mcp_kg_n7_evaluado.json").read_text(encoding="utf-8")) if r.returncode == 0 else {}
args = mcp.get("mcpServers", {}).get("kg", {}).get("args", [])
caso("1. el JSON de MCP: el servidor nuevo y la config de N7", any(x.endswith("servidor_mcp_kg_nav_cand.py") for x in args)
     and any(x.endswith("n7/config_mcp_kg_n7_evaluado.json") for x in args))
caso("1. el bloque de T−F3 y la plantilla de N6, byte a byte", r.returncode == 0 and (s / "bloque_tools_kg_n7.txt").read_bytes() ==
     (BANCO / bloque["T-F3"]).read_bytes() and (s / "plantilla_prompt_n7.txt").read_bytes() == (N6 / "plantilla_prompt_n6.txt").read_bytes())
caso("1. fragmentos con la híbrida, su config y su bloque de N6", reg.get("F1", {}).get("principal_de_fragmentos") == "hibrida" and
     (s / "bloque_tools_fragmentos_n7.txt").read_bytes() == (BANCO / bloque["F1_hibrida"]).read_bytes() and
     reg["brazo_fragmentos"]["principal"]["sha256"] == sha((BANCO / "mcp_vector/config_fragmentos_hibrida_evaluado_r2b.json").read_bytes()))
caso("1. R5 queda en 30, 32 y 1,80", reg.get("R5", {}).get("sube") is False and reg["R5"]["valores"]["max_turns"] == 32)
caso("1. los ejemplos de la familia 6 en fragmentos, pendientes", len(reg.get("pendiente", [])) == 1)
r2, s2 = correr("t_f3_otra_vez", a1, 0)
caso("1. dos corridas, los mismos bytes en todo lo que escribe", r2.returncode == 0 and sorted(p.name for p in s.iterdir()) ==
     sorted(p.name for p in s2.iterdir()) and all((s / p.name).read_bytes() == (s2 / p.name).read_bytes() for p in s.iterdir()
                                                    if p.name != "n7_configuracion_sellada.json")
     and json.loads((s / "n7_configuracion_sellada.json").read_text())["brazo_grafo"] ==
     json.loads((s2 / "n7_configuracion_sellada.json").read_text())["brazo_grafo"])

# 2. B, con BM25: sin familias, no carga el codificador, sin pendiente
f2 = dict(FID, B=0.75)
r, s = correr("b", analisis(f2, set(), v30=0.01, entra_hibrida=False), 0)
reg = json.loads((s / "n7_configuracion_sellada.json").read_text(encoding="utf-8")) if r.returncode == 0 else {}
caso("2. elige B: sin familias, sin codificador, sin pendiente, fragmentos con BM25", r.returncode == 0 and
     reg["brazo_grafo"]["familias"] == [] and reg["brazo_grafo"]["carga_el_codificador"] is False and not reg["pendiente"]
     and reg["F1"]["principal_de_fragmentos"] == "bm25" and (s / "bloque_tools_fragmentos_n7.txt").read_bytes() ==
     (BANCO / bloque["F1_bm25"]).read_bytes(), r.stdout.strip()[:100])

# 3. T−F6: el bloque de B, sin pendiente
f3 = dict(FID, **{"T-F6": 0.80})
r, s = correr("t_f6", analisis(f3, {"T-F6"}, v30=0.01), 0)
reg = json.loads((s / "n7_configuracion_sellada.json").read_text(encoding="utf-8")) if r.returncode == 0 else {}
caso("3. elige T−F6: su bloque es el de B y no lleva los ejemplos", r.returncode == 0 and not reg["pendiente"] and
     (s / "bloque_tools_kg_n7.txt").read_bytes() == (BANCO / bloque["T-F6"]).read_bytes() and bloque["T-F6"] == bloque["B"])

# 4. el desempate dentro de V(30): T y T−F3 empatan; T−F3 llega más veces al tope, gana T
r, s = correr("desempate", analisis(FID, {"T-F3"}, v30=0.02, al_tope={"T-F3": 1}), 0)
reg = json.loads((s / "n7_configuracion_sellada.json").read_text(encoding="utf-8")) if r.returncode == 0 else {}
caso("4. dentro de V(30), gana la que llega menos al tope", reg.get("brazo_grafo", {}).get("configuracion_n6") == "T")

# 5. R5 sube: 2 de 30 al tope en la elegida (6,7 %)
r, s = correr("r5", analisis(FID, {"T-F3"}, v30=0.005, al_tope={"T-F3": 2}), 0)
reg = json.loads((s / "n7_configuracion_sellada.json").read_text(encoding="utf-8")) if r.returncode == 0 else {}
caso("5. más del 5 % al tope: R5 sube a 45, 47 y 3,30", reg.get("R5", {}).get("sube") is True and reg["R5"]["valores"] ==
     {"tope_tool_calls_prompt": 45, "max_turns": 47, "max_budget_usd": 3.30})
r, s = correr("r5_justo", analisis(FID, {"T-F3"}, v30=0.005, al_tope={"F1_bm25": 4}, entra_hibrida=False), 0)
reg = json.loads((s / "n7_configuracion_sellada.json").read_text(encoding="utf-8")) if r.returncode == 0 else {}
caso("5. 4 de 90 en fragmentos (4,4 %): no sube", reg.get("R5", {}).get("sube") is False)

# 6 a 10. los frenos, sin escribir nada
for nombre, a, rc in (("jerarquia", analisis(FID, {"T-F3"}, v30=0.005, pasa=False), 11),
                      ("otra_elegida", analisis(FID, {"T-F3"}, v30=0.005, elegida="T", orden=["T", "T-F3"]), 10),
                      ("f1_sin_decidir", analisis(FID, {"T-F3"}, v30=0.005, entra_hibrida=None), 12)):
    r, s = correr(nombre, a, rc)
    caso(f"freno {rc}: {nombre}, sin escribir nada", r.returncode == rc and not s.exists(), r.stdout.strip()[:90])
r, s = correr("ya_existe", a1, 14, salida=TR / "salida_t_f3")
caso("freno 14: la salida ya existe", r.returncode == 14)
ag2 = copy.deepcopy(ag)
for b in ag2["brazos"].values():
    if b["configuracion_n6"] == "T-F3":
        b["carga_codificador"] = False
pag = TR / "agentes_juguete.json"
pag.write_text(json.dumps(ag2), encoding="utf-8")
r, s = correr("carga_distinta", a1, 15, agentes=pag)
caso("freno 15: la config de agentes dice otra cosa sobre el codificador", r.returncode == 15 and not s.exists())

# 11 a 13. la decisión 9: la elección sobre las 26, con V(26) y lo operativo de las 26
F26 = dict(FID, **{"T-F3": 0.60, "T-F6": 0.75})
a11 = analisis_d9(FID, F26, {"T-F3", "T-F6"}, v30=0.005, v26=0.01, al_tope26={}, r9_26={"T-F6": 0.2})
r, s = correr("d9", a11, 0)
reg = json.loads((s / "n7_configuracion_sellada.json").read_text(encoding="utf-8")) if r.returncode == 0 else {}
caso("11. sobre las 26: elige T−F6 (la mejor sin FUERA_D9) y no T−F3 (la mejor sobre las 30)", r.returncode == 0
     and reg["brazo_grafo"]["configuracion_n6"] == "T-F6" and reg["regla_N4_5"]["otra_vez"]["sobre"].startswith("las 26")
     and reg["regla_N4_5"]["del_analisis"]["dentro_de_V"] == reg["regla_N4_5"]["otra_vez"]["dentro_de_V"], r.stdout.strip()[:90])
F26b = dict(FID, **{"T-F3": 0.745, "T-F6": 0.75})
a12 = analisis_d9(FID, F26b, {"T-F3", "T-F6"}, v30=0.005, v26=0.01, al_tope26={}, r9_26={"T-F6": 0.6, "T-F3": 0.3})
r, s = correr("d9_desempate", a12, 0)
reg = json.loads((s / "n7_configuracion_sellada.json").read_text(encoding="utf-8")) if r.returncode == 0 else {}
caso("12. sobre las 26, dentro de V(26): gana la más barata con el R9 de las 26", reg.get("brazo_grafo", {}).get("configuracion_n6") == "T-F3")
a13 = analisis_d9(FID, F26, {"T-F3", "T-F6"}, v30=0.005, v26=0.01, al_tope26={}, r9_26={"T-F6": 0.2}, elegida="T-F3")
r, s = correr("d9_otra", a13, 10)
caso("13. freno 10: sobre las 26, el análisis dice otra elegida, sin escribir nada", r.returncode == 10 and not s.exists(), r.stdout.strip()[:90])
a14 = analisis_d9(FID, F26, {"T-F3", "T-F6"}, v30=0.005, v26=0.01, al_tope26={}, r9_26={"T-F6": 0.2})
del a14["regla"]["eleccion"]["al_tope"]["T-F6"]
r, s = correr("d9_sin_operativo", a14, 10)
caso("13. freno 10: sobre las 26, sin lo operativo de una de las de dentro de V", r.returncode == 10 and not s.exists(), r.stdout.strip()[:90])
print(f"RESULTADO: {sum(ok for _, ok in res)} de {len(res)}")
sys.exit(0 if all(ok for _, ok in res) else 1)
