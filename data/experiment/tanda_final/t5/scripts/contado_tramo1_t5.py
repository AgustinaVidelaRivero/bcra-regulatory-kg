"""B6.1, tanda final, T5, punto 8 (la columna del tablero del tramo 1): lo que se cuenta sin leer, con el mismo código de T3
(t3/scripts/contado_sin_leer_tf.py, copiado y adaptado: las mismas funciones), sobre los cuatro grafos del tramo 1, que T3 no contó:
KG-TandaFinal-Tramo1-r2b y su sin cola, y KG-Acumulado-Tandas0y1yTramo1-r2b y su sin cola. Corre desde la raíz de una COPIA del repo
(la del rsync del «seguí», con la entrada del acumulado de 60 armada por entrada_acumulado_60_t5.py). USD 0, sin API ni Neo4j.
Lo que cambia contra el de T3:
  - los grafos y sus rutas: el tramo 1, con los manifiestos de la raya (t3/prueba_raya_tramo1/manifiestos/, que rigen: FRENO T3, §2,
    punto 2); el acumulado de 60, con los suyos (t3/acumulado/manifiestos/) y su E0 y su entrada (t3/acumulado/);
  - sin el control contra la línea de base de la tanda 1 (el «seguí» de T5, punto 9: de la tanda 1 no se abren cifras); queda el control
    contra el re-sellado de la tanda 0;
  - la cola por estado y los otros estados van solo al NO_ABRIR_ (punto 9: ningún desglose por estado de E3): en la salida quedan la
    cola, las aceptadas (los tres estados juntos) y la cola por TO.
Uso (desde la raíz de la copia): python -B contado_tramo1_t5.py <copia> <salida.json> <salida NO_ABRIR.json>
"""
from __future__ import annotations

import ast
import collections
import hashlib
import importlib.util
import json
import sys
import types
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, OUT, OUT_NA = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3])
assert Path.cwd().resolve() == RAIZ and not (RAIZ / ".git").exists(), "correr desde la raíz de una copia del repo"
X = "data/experiment/reextraccion_v2"
A = "data/experiment/tanda_final/t3/acumulado"
T3 = "data/experiment/tanda_final/t3"
PR = "data/experiment/tanda_final/t3/prueba_raya_tramo1/manifiestos"


def cargar(nombre: str, ruta: Path):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nombre] = m
    spec.loader.exec_module(m)
    assert Path(m.__file__).resolve().is_relative_to(RAIZ)
    return m


RM = cargar("medicion_tablero_r2b_rs1_mesa", RAIZ / "data/experiment/resellado_t0/condicion_4/medicion_tablero_r2b_rs1_mesa.py")
assert Path(RM.RAIZ).resolve() == RAIZ
dc = json.loads((RAIZ / T3 / "salidas/doble_corrida_tf.json").read_text(encoding="utf-8"))["doble_corrida"]
GRAFOS = OrderedDict([
    ("tf_tramo1", {"nombre": "KG-TandaFinal-Tramo1-r2b", "ens": f"{X}/corpus_tanda_final/ens_tramo1_r2b", "dc": "tf_tramo1",
                   "manifiesto": f"{PR}/tanda_final_ens_tramo1_r2b_raya.json", "e0": f"{X}/e0_chunking/salida_tanda_final_r2b",
                   "salida": f"{X}/corpus_tanda_final/salida_r2b", "sin_cola": False}),
    ("tf_tramo1_sincola", {"nombre": "KG-TandaFinal-Tramo1-r2b-sincola", "ens": f"{X}/corpus_tanda_final/ens_tramo1_r2b_sincola",
                           "dc": "tf_tramo1_sincola", "manifiesto": f"{PR}/tanda_final_ens_tramo1_r2b_raya_sincola.json",
                           "e0": f"{X}/e0_chunking/salida_tanda_final_r2b", "salida": f"{X}/corpus_tanda_final/salida_r2b", "sin_cola": True}),
    ("acum60", {"nombre": "KG-Acumulado-Tandas0y1yTramo1-r2b", "ens": f"{A}/ens_60_tramo1_r2b", "dc": "acum60",
                "manifiesto": f"{A}/manifiestos/tanda_final_acumulado_ens_60_tramo1_r2b.json", "e0": f"{A}/e0_acumulado_60_r2b",
                "salida": f"{A}/entrada_acumulado_60_r2b", "sin_cola": False}),
    ("acum60_sincola", {"nombre": "KG-Acumulado-Tandas0y1yTramo1-r2b-sincola", "ens": f"{A}/ens_60_tramo1_r2b_sincola", "dc": "acum60_sincola",
                        "manifiesto": f"{A}/manifiestos/tanda_final_acumulado_ens_60_tramo1_r2b_sincola.json", "e0": f"{A}/e0_acumulado_60_r2b",
                        "salida": f"{A}/entrada_acumulado_60_r2b", "sin_cola": True})])
for g, cfg in GRAFOS.items():
    cfg["suite"] = f"{T3}/gate/e0_del_grafo/{g}/suite_perfil_r2.json"
ACEPTADOS = ("completo_ok_directo", "aceptado_con_residuales", "aceptado_tras_reintento")   # r0_f2_cifras_enmienda7.py:31
ID_V9 = "Sujeto_entidad_originante_de_transferencia"


def leer(p: str):
    return json.loads((RAIZ / p).read_text(encoding="utf-8"))


def lineas(p: Path) -> list:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


def sha(p: str) -> str:
    return hashlib.sha256((RAIZ / p).read_bytes()).hexdigest()


# ----------------------------------------------------------------- copias con la ruta de cada grafo (mismo código)
def suite_t3f(ruta: str, fixture: dict) -> dict:
    """RM.suite (medicion_tablero_r2b_rs1_mesa.py:590-611) con la ruta de la suite del grafo."""
    s = leer(ruta)
    estados = OrderedDict((it["id"], it["estado"]) for it in s["items"])
    part = s["parametros"]["particion"]
    ids46 = [i for i in estados if i not in part["items_r2"]]
    r1 = {k: (v["estado"] if isinstance(v, dict) else v) for k, v in fixture["estado_esperado"]["KG-Reextraido-r1"]["items"].items()}
    trans = Counter((r1.get(i), estados[i]) for i in ids46)
    return OrderedDict([
        ("kg_sha256", s["parametros"]["kg_sha256"]), ("resumen", s["resumen"]),
        ("particion_46", OrderedDict([("n", len(ids46)), ("estados", dict(sorted(Counter(estados[i] for i in ids46).items())))])),
        ("contra_entrada_r1", OrderedDict([
            ("transiciones_r1_a_r2a", {f"{a} -> {b}": n for (a, b), n in sorted(trans.items(), key=lambda x: (str(x[0][0]), x[0][1]))}),
            ("de_resuelto_a_persiste", sorted(i for i in ids46 if r1.get(i) == "resuelto" and estados[i] == "persiste")),
            ("de_resuelto_a_no_aplicable", sorted(i for i in ids46 if r1.get(i) == "resuelto" and estados[i] == "no_aplicable")),
            ("de_persiste_a_resuelto", sorted(i for i in ids46 if r1.get(i) == "persiste" and estados[i] == "resuelto"))])),
        ("regresion", {k: s["regresion"].get(k) for k in ("fixture_sha256", "estado_esperado_sha256", "parte", "entrada",
                                                          "n_regresiones", "coinciden", "sin_esperado", "nota")}),
        ("items", OrderedDict((it["id"], {"estado": it["estado"], "detalle": it["detalle"]}) for it in s["items"]
                              if it["id"] in ("EJ-cla-5.1.1.1", "BKL-0006", "BKL-0023", "T6", "E4-b", "LN-3", "LN-7")))])


def m10_t3f(nombre: str) -> dict:
    """RM.m10 (:614-619) sobre las intrínsecas con la E0 con las partes (tanda_final/t3/intrinsecas_gen3/con_partes/)."""
    d = leer(f"{T3}/intrinsecas_gen3/con_partes/{nombre}.json")
    m = d["metricas"]["M10_chunks_mudos"]
    return OrderedDict([("valor", m["valor"]), ("numerador", m["numerador"]), ("denominador", m["denominador"]),
                        ("mudos", [x["chunk_id"] for x in m["notas"]["mudos_detalle"]]),
                        ("custodia", d["custodia"][0]["custodia"]), ("sha256_medido", d["custodia"][0]["sha256_medido"])])


def omisiones_t3f(kg: dict, tos: list, salida: str, ens: str, suite: str) -> dict:
    """RM.omisiones_r2b (:436-460) con la salida, el registro y la suite del grafo."""
    n_unid, n_om, sin_cat, sin_tramo, por_cat = 0, 0, 0, 0, Counter()
    for to in tos:
        for x in (RAIZ / salida / to / f"extracciones_finales_r2_{to}.jsonl").read_text(encoding="utf-8").splitlines():
            if not x.strip():
                continue
            r = json.loads(x)
            om = (r.get("validacion") or {}).get("omisiones") or []
            n_unid += bool(om)
            for o in om:
                n_om += 1
                por_cat[o.get("categoria")] += 1
                sin_cat += not o.get("categoria")
                sin_tramo += not o.get("tramo")
    reg = RAIZ / ens / "r2" / "omisiones.jsonl"
    filas = [json.loads(x) for x in reg.read_text(encoding="utf-8").splitlines() if x.strip()] if reg.exists() else None
    s = leer(suite)
    ln7 = next((it for it in s["items"] if it["id"] == "LN-7"), None)
    return OrderedDict([("unidades_con_omisiones", n_unid), ("omisiones", n_om), ("sin_categoria", sin_cat),
                        ("sin_tramo", sin_tramo), ("por_categoria", dict(sorted(por_cat.items(), key=lambda x: str(x[0])))),
                        ("registro_del_ensamblado_filas", None if filas is None else len(filas)),
                        ("ln7", None if ln7 is None else {"estado": ln7["estado"], "detalle": ln7["detalle"]})])


# ----------------------------------------------------------------- condiciones sin regla (como condiciones_sin_regla_rs1_mesa.py)
_src = (RAIZ / "reports/u_diag_cap3_grafo/scripts/udiag_e_aisladas.py").read_text(encoding="utf-8")
_nodos = [n for n in ast.parse(_src).body if (isinstance(n, ast.FunctionDef) and n.name in ("es_remision_r1", "medir")) or
          (isinstance(n, ast.Assign) and any(getattr(x, "id", "") == "NO_CONTENIDO" for x in n.targets))]
assert len(_nodos) == 3, "no encuentro las tres definiciones"
_ns = {"collections": collections}
exec(compile(ast.Module(body=_nodos, type_ignores=[]), "udiag_e_aisladas.py", "exec"), _ns)
medir_sin_regla = _ns["medir"]


# ----------------------------------------------------------------- vigilancias (4), (5), (8), (9) (como vigilancias_contables_rs1_mesa.py)
def docs_de(n: dict) -> frozenset:
    return frozenset(p.get("to") for p in (n.get("provenances") or []) if p.get("to"))


def vigilancias(kg: dict, tos: list, salida: str) -> dict:
    cnt = Counter()
    for n in kg["nodes"]:
        if n["type"] == "TextoOrdenado":
            for d in docs_de(n) or {"(sin to)"}:
                cnt[d] += 1
    v4 = {"por_to": dict(sorted(cnt.items())), "uno_por_to": set(cnt.values()) == {1} and set(cnt) == set(tos)}
    res = {to: json.loads((RAIZ / salida / to / "resumen_e1.json").read_text(encoding="utf-8")) for to in tos}
    v5 = {"tipo_obligacion_requisito_de_estructura": {to: res[to].get("tipo_obligacion_requisito_de_estructura") for to in tos},
          "tipo_obligacion_normalizados": {to: res[to].get("tipo_obligacion_normalizados") for to in tos}}
    v5["total"] = {k: sum(x or 0 for x in v.values()) for k, v in v5.items()}
    prop = sid = 0
    em = {}
    for to in tos:
        em[to] = 0
        for x in lineas(RAIZ / salida / to / f"extracciones_finales_{to}.jsonl"):
            for r in (x.get("validacion") or {}).get("relaciones") or []:
                if r.get("sujeto_propuesto"):
                    prop += 1
                elif r.get("sujeto_id"):
                    sid += 1
                if r.get("sujeto_id") == ID_V9:
                    em[to] += 1
    v8 = {"sujeto_propuesto": prop, "sujeto_id": sid, "tasa_pct": round(100 * prop / (prop + sid), 2) if prop + sid else None}
    v9 = {"emisiones_E1_por_to": em, "emisiones_E1_total": sum(em.values()),
          "aristas_en_kg": sum(1 for e in kg["edges"] if ID_V9 in (e["source"], e["target"]))}
    return OrderedDict([("4", v4), ("5", v5), ("8", v8), ("9", v9)])


# ----------------------------------------------------------------- la cola
def cola(tos: list, salida: str, ens: str, sin_cola: bool, kg: dict) -> dict:
    ult = {}
    for to in tos:
        for r in lineas(RAIZ / salida / to / "finales.jsonl"):
            ult[r["chunk_id"]] = r
    estados = Counter(r["estado"] for r in ult.values())
    en_cola = Counter({k: v for k, v in estados.items() if str(k).startswith("cola_humana")})
    acept = sum(v for k, v in estados.items() if k in ACEPTADOS)
    otros = {k: v for k, v in estados.items() if k not in ACEPTADOS and not str(k).startswith("cola_humana")}
    assert not any(str(k).startswith(("aceptado", "completo")) for k in otros), "un estado de aceptación fuera de ACEPTADOS"
    cola_ids = sorted(c for c, r in ult.items() if str(r["estado"]).startswith("cola_humana"))
    rep = leer(f"{ens}/r2/reporte_ensamblado_r2.json")
    desc = rep.get("cola_descartada_por_to") or {}
    return OrderedDict([
        ("unidades_en_finales", len(ult)), ("aceptadas_los_tres_estados_juntos", acept), ("cola", sum(en_cola.values())),
        ("cola_por_estado", dict(sorted(en_cola.items()))), ("otros_estados", dict(sorted(otros.items()))),
        ("cola_por_to", dict(sorted(Counter(c.split("::")[0] for c in cola_ids).items()))),
        ("grafo", OrderedDict([("con_cola", rep.get("con_cola")),
                               ("descartadas_por_el_ensamblado_sin_cola", sum(v["n"] for v in desc.values()) if sin_cola else None),
                               ("nodos_con_la_marca", sum(1 for n in kg["nodes"] if (n.get("properties") or {}).get("cola_humana") == "true")),
                               ("aristas_con_la_marca", sum(1 for e in kg["edges"] if (e.get("properties") or {}).get("cola_humana") == "true"))]))])


# ================================================================= medición
enums = leer(RM.ENUMS)
fixture = leer(RM.FIXTURE)
out = OrderedDict([("insumos", OrderedDict()), ("grafos", OrderedDict())])
na = OrderedDict([("nota", "B6.1, tanda final, T5, punto 8: las cuentas bajo el cegamiento de U-MED-VERIF (punto 9 del «seguí»), de los "
                           "grafos del tramo 1. No se abren; el FRENO da solo el sha256 del NO_ABRIR_ de T5, que las junta."),
                  ("grafos", OrderedDict())])
for g, cfg in GRAFOS.items():
    kgp, repp = f"{cfg['ens']}/r2/kg.json", f"{cfg['ens']}/r2/reporte_ensamblado_r2.json"
    esperado = dc[cfg["dc"]]["kg_sha256"][0]
    if sha(kgp) != esperado:
        raise SystemExit(f"FRENO: {g} no da su sha256")
    kg, rep = leer(kgp), leer(repp)
    tos = RM.tos_de(cfg["manifiesto"])
    RM.E0_R2, RM.SALIDA_R2B = cfg["e0"], cfg["salida"]
    unidades = sum(len(cs) for cs in RM.chunks_de(cfg["e0"], tos).values())
    out["insumos"][g] = {"kg": kgp, "kg_sha256": esperado, "reporte": repp, "reporte_sha256": sha(repp),
                         "manifiesto": cfg["manifiesto"], "e0": cfg["e0"], "salida": cfg["salida"], "tos": len(tos)}
    f = OrderedDict()
    f["tos"] = tos
    f["unidades_e0_r2b"] = unidades
    f["f49_obs10"] = RM.obs10(kg, unidades, ("derivada_de_procedencia",))
    f["f50_obs11"] = RM.obs11(kg, rep)
    f["f51_remisiones_por_origen"] = RM.remisiones_por_origen(kg)
    f["f52_aislados"] = RM.aislados(kg)
    f["f52_condiciones_sin_regla"] = medir_sin_regla(kg)
    f["f53_falsas_parafrasis"] = RM.falsas_parafrasis(kg) if "cap" in tos else "no aplica: el grafo no tiene cap"
    f["f54_f55_suite"] = suite_t3f(cfg["suite"], fixture)
    f["f61_m10"] = m10_t3f(cfg["nombre"])
    f["f62_cap_1_2"] = RM.cap_1_2(kg) if "cap" in tos else "no aplica: el grafo no tiene cap"
    f["f63_tablas"] = (RM.tablas(kg) if all(t in tos for t in ("cap", "ric", "ext", "ctacte", "polcre"))
                       else "no aplica: el grafo no tiene los TOs de las citas de D2 ni de las unidades de U-UMBRAL")
    v = RM.valores_fuera_de_lista(kg, enums)
    pnd = v.pop("properties_no_definidas")
    f["f64_valores_fuera_de_lista"] = v
    f["f64_properties_no_definidas"] = "en NO_ABRIR_conteos_t3.json: cuenta copia_nota_e3 (cegamiento) y la marca de L-04"
    f["f65_sujetos"] = RM.sujetos(kg, rep)
    f["f67_cuantias"] = RM.cuantias(kg, "umbrales")
    f["f67_mismo_criterio_con_campo_heredado"] = RM.cuantias(kg, "heredado")
    f["f67_limites_relativos_s18"] = RM.limites_relativos(kg)
    f["f68_omisiones"] = omisiones_t3f(kg, tos, cfg["salida"], cfg["ens"], cfg["suite"])
    f["f69_crudo_reintento"] = "en NO_ABRIR_conteos_t3.json (cegamiento: usa los reintentos de E3)"
    f["f70_colisiones_e0_r2"] = RM.colisiones(tos)
    f["f71_no_verificadas_e3"] = RM.no_verificadas(kg)
    f["f73_pies_e0_r2"] = RM.pies(cfg["e0"], tos)
    f["f74_frecuencia"] = RM.frecuencia(kg, rep)
    f["vigilancias"] = vigilancias(kg, tos, cfg["salida"])
    f["cola"] = cola(tos, cfg["salida"], cfg["ens"], cfg["sin_cola"], kg)
    estados_e3 = OrderedDict((k, f["cola"].pop(k)) for k in ("cola_por_estado", "otros_estados"))
    out["grafos"][g] = f
    n = OrderedDict()
    n["f64_properties_no_definidas"] = pnd
    n["f69_crudo_reintento"] = RM.crudo_reintento(rep)
    n["f69_crudo_reintento_en_la_salida"] = RM.crudo_reintento_salida(tos)
    n["cola_por_estado_y_otros_estados"] = estados_e3
    na["grafos"][g] = n
out["f66_catalogo"] = RM.catalogo()
out["f72_lineas_mayusculas"] = ("no medido: la fila lee r1k_encabezados_descartados_e0r2.json, medido sobre la E0 legada de la tanda 0; "
                                "la tanda final no tiene E0 legada")

# control: las mismas funciones sobre el diez re-sellado reproducen la medición del re-sellado
base = leer("data/experiment/resellado_t0/condicion_4/medicion_tablero_r2b_rs1.json")["diez"]
T0d = f"{X}/corpus_tanda0/ens_diez_r2b_rs1"
kg0, rep0 = leer(f"{T0d}/r2/kg.json"), leer(f"{T0d}/r2/reporte_ensamblado_r2.json")
RM.E0_R2, RM.SALIDA_R2B = f"{X}/e0_chunking/salida_tanda0_r2b", f"{X}/corpus_tanda0/salida_r2b"
u0 = sum(len(cs) for cs in RM.chunks_de(RM.E0_R2, base["tos"]).values())
v0 = RM.valores_fuera_de_lista(kg0, enums)
v0.pop("properties_no_definidas")
vb = dict(base["f64_valores_fuera_de_lista"])
vb.pop("properties_no_definidas", None)
ctrl = OrderedDict([
    ("f49_obs10", RM.obs10(kg0, u0, ("derivada_de_procedencia",)) == base["f49_obs10"]),
    ("f50_obs11", RM.obs11(kg0, rep0) == base["f50_obs11"]),
    ("f51_remisiones_por_origen", RM.remisiones_por_origen(kg0) == base["f51_remisiones_por_origen"]),
    ("f52_aislados", RM.aislados(kg0) == base["f52_aislados"]),
    ("f53_falsas_parafrasis", RM.falsas_parafrasis(kg0) == base["f53_falsas_parafrasis"]),
    ("f64_valores_fuera_de_lista_sin_pnd", json.loads(json.dumps(v0)) == json.loads(json.dumps(vb))),
    ("f65_sujetos", json.loads(json.dumps(RM.sujetos(kg0, rep0))) == json.loads(json.dumps(base["f65_sujetos"]))),
    ("f67_cuantias", RM.cuantias(kg0, "umbrales") == base["f67_cuantias"]),
    ("f71_no_verificadas_e3", RM.no_verificadas(kg0) == base["f71_no_verificadas_e3"]),
    ("f73_pies_e0_r2", RM.pies(RM.E0_R2, base["tos"]) == base["f73_pies_e0_r2"]),
    ("f74_frecuencia", json.loads(json.dumps(RM.frecuencia(kg0, rep0))) == json.loads(json.dumps(base["f74_frecuencia"])))])
out["control_contra_el_re_sellado"] = {"grafo": "KG-Tanda0-Diez-r2b-rs1", "base": "resellado_t0/condicion_4/medicion_tablero_r2b_rs1.json",
                                       "iguales": ctrl, "todos": all(ctrl.values())}

# el catálogo al cierre
RR = cargar("r2_1_medicion", RAIZ / "data/experiment/reresolucion_catalogo/r2_1_medicion.py")
RR.ENSAMBLADOS = OrderedDict((g, f"{c['ens']}/r2") for g, c in GRAFOS.items())
um = RR.medir_umbral()
out["catalogo_al_cierre"] = OrderedDict(
    (g, OrderedDict([("filas_registro", u["filas_registro"]), ("cuarentena", u["cuarentena"]),
                     ("verificadas_en_cuarentena", u["verificadas_en_cuarentena"]), ("claves", u["claves"]),
                     ("claves_con_2_unidades_o_mas", u["claves_con_2_unidades_o_mas"]),
                     ("n_claves_con_2_unidades_o_mas", len(u["claves_con_2_unidades_o_mas"])),
                     ("claves_con_3_unidades_o_mas", u["claves_con_3_unidades_o_mas"]),
                     ("claves_en_2_tos_o_mas", u["claves_en_2_tos_o_mas"])])) for g, u in um.items())

out["control_contra_la_linea_de_base_de_la_tanda_1"] = ("no se corre en T5: el «seguí», punto 9, veda las cifras de la tanda 1 "
                                                       "(el de T3 lo corrió, FRENO T3, §6)")
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
OUT_NA.write_text(json.dumps(na, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
print("escrito:", OUT.name, hashlib.sha256(OUT.read_bytes()).hexdigest())
print("escrito (sin abrir):", OUT_NA.name, hashlib.sha256(OUT_NA.read_bytes()).hexdigest())
print("control contra el re-sellado:", out["control_contra_el_re_sellado"]["iguales"])
