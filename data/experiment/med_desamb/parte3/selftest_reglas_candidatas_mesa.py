"""Selftest del código preparado de S1, S2 y C1 (mesa, §139). Sin API y sin escribir en el clon.
Corre la misma batería con el código de HEAD y con el parchado, cada uno en su propio proceso, y controla:
  1. con los parámetros nuevos en su defecto, el parchado da exactamente lo de HEAD (resolver_relaciones_r2, reresolver_registro,
     decidir sobre las 3.108 filas de resolución de r2a y la guarda entre documentos);
  2. con S1, S2 o C1 encendidos, cambia solo lo que la regla dice, caso por caso.
La copia parchada se ejecuta con el __file__ de su original en el clon, para que sus rutas resuelvan ahí.
Uso: python3 -I -B selftest_reglas_candidatas_mesa.py <clon>"""
import importlib.util
import json
import subprocess
import sys
import types
from copy import deepcopy
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PREP = AQUI / "codigo_preparado"
REL = {"r1_e4": "data/experiment/reextraccion_v2/corpus_v2/r1_e4.py",
       "r1_invariantes": "data/experiment/reextraccion_v2/corpus_v2/r1_invariantes.py",
       "reresolver_catalogo": "data/experiment/reresolucion_catalogo/reresolver_catalogo.py"}
ALCANCE = "TO_exterior_cambios_actual.pdf"
ROL = "Sujeto_rol_entidad_autorizada_exterior"


def cargar(nombre, CL, variante):
    """El módulo de HEAD (del clon) o el parchado (del paquete), ejecutado con el __file__ del clon; queda en sys.modules."""
    ruta = Path(CL) / REL[nombre]
    src = ruta.read_text(encoding="utf-8") if variante == "head" else (PREP / f"{nombre}_con_reglas_candidatas.py").read_text(encoding="utf-8")
    m = types.ModuleType(nombre)
    m.__file__ = str(ruta)
    sys.modules[nombre] = m
    exec(compile(src, str(ruta), "exec"), m.__dict__)
    return m


def rel(i, mencion, nivel, modelo, punto="3.1"):
    return {"predicate": "aplica_a", "source": f"e{i}", "target": None, "sujeto_mencion": mencion, "mencion_verificada": nivel,
            "sujeto_id_modelo": modelo, "padre_sugerido": None, "indice_crudo": i, "punto": punto}


CASOS = [  # (nombre, archivo, mención, nivel, modelo)
    ("c1_R1_con_desacuerdo", ALCANCE, "los bancos", "exacta", "Sujeto_entidad_financiera"),
    ("c2_R3_contra_modelo", ALCANCE, "las entidades", "exacta", "Sujeto_banco"),
    ("c3_R3_mismo_id", ALCANCE, "las entidades", "exacta", ROL),
    ("c4_calificador_contra_modelo", ALCANCE, "las agencias de cambio autorizadas", "exacta", "Sujeto_entidad_cambiaria"),
    ("c5_mencion_no_verificada", ALCANCE, "los operadores habilitados", "no", "Sujeto_banco"),
    ("c6_sin_regla_verificada", ALCANCE, "quienes operen", "exacta", "Sujeto_banco"),
    ("c7_parte_A_sin_alcance", "TO_sin_alcance_de_prueba.pdf", "las entidades", "exacta", "Sujeto_banco"),
    ("c8_R3_sin_modelo", ALCANCE, "las entidades", "exacta", None),
    ("c9_tokens_contra_modelo", ALCANCE, "las entidades", "tokens", "Sujeto_banco"),
]


def trabajador(CL, variante):
    sys.dont_write_bytecode = True
    for p in ("data/experiment/reextraccion_v2/corpus_v2", "data/experiment/reextraccion_v2/e2_reduce"):
        sys.path.insert(0, str(Path(CL) / p))
    E4 = cargar("r1_e4", CL, variante)
    cat = E4.catalogo_r2()
    idx, rpt = cat["indice"], cat["rol_por_to"]
    vers = {"catalogo_sha256": cat["catalogo_sha256"]}
    out = {}
    regs = [{"chunk_id": f"x::{k}", "to": "x", "archivo": a, "e0_sha256_completo": "0",
             "validacion": {"entidades": [{"local_id": f"e{k}", "type": "Obligacion", "label": "n"}],
                            "relaciones": [rel(k, m, nv, mo)]}} for k, (_, a, m, nv, mo) in enumerate(CASOS)]
    combos = [{}] if variante == "head" else [{}, {"s1": False, "s2": False}, {"s1": True}, {"s2": True}, {"s1": True, "s2": True}]
    for kw in combos:
        rr = deepcopy(regs)
        res = E4.resolver_relaciones_r2(rr, idx, rpt, vers, parte_a=True, **kw)
        out["resolver:" + json.dumps(kw, sort_keys=True)] = {"res": res, "relaciones_mutadas": [r["validacion"]["relaciones"] for r in rr]}
    filas = [{"estado": "cuarentena", "to": "x", "chunk_id": "x::0", "indice_relacion": 0, "mencion": "las entidades",
              "mencion_verificada": "exacta", "sujeto_id_modelo": "Sujeto_banco", "padre_sugerido": None, "calificador": None},
             {"estado": "cuarentena", "to": "x", "chunk_id": "x::1", "indice_relacion": 1, "mencion": "los operadores habilitados",
              "mencion_verificada": "no", "sujeto_id_modelo": "Sujeto_banco", "padre_sugerido": None, "calificador": None}]
    for kw in combos:
        out["reresolver:" + json.dumps(kw, sort_keys=True)] = E4.reresolver_registro(deepcopy(filas), idx, rpt, {"x": ALCANCE}, "sha_prueba", **kw)
    # decidir sobre las filas reales de r2a (grafo de prueba): solo igualdad HEAD/parchado y cuántas cambian con S1 o S2
    sys.modules["r1_e4"] = E4
    RC = cargar("reresolver_catalogo", CL, variante)
    pref = E4._prefijos(idx)
    filas_r2a = [json.loads(l) for l in open(Path(CL) / "data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2a/r2/resolucion_sujetos.jsonl",
                                             encoding="utf-8") if l.strip()]
    archivo = {"ext": ALCANCE, "cap": "TO_capitales_minimos_actual.pdf", "pro": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
               "ric": "TO_regimen_informativo_contable_mensual_actual.pdf", "cla": "TO_clasificacion_deudores_actual.pdf"}
    for kw in combos:
        out["decidir_r2a:" + json.dumps(kw, sort_keys=True)] = [
            RC.decidir(f, None, idx, pref, (rpt.get(archivo[f["to"]]) or {}).get("rol_id"), False, **kw) for f in filas_r2a]
    # la guarda entre documentos, con C1
    INV = cargar("r1_invariantes", CL, variante)
    tos = list(INV.C.TOS_ORDEN)

    def com(i, cod, label):
        return {"id": i, "type": "Comunicacion", "label": label, "properties": {"codigo": cod, "tipo": "A"},
                "provenances": [{"to": None, "punto": "1"}]}

    def to_g(to, coms):
        pv = {"to": to, "punto": "1", "chunk_id": f"{to}::1"}   # I5 pide `provenance` y `provenances` no vacío
        t = {"id": f"TextoOrdenado_{to}", "type": "TextoOrdenado", "label": to, "properties": {}, "provenance": pv, "provenances": [pv]}
        ns = [t] + [dict(c, provenance=pv, provenances=[pv]) for c in coms]
        return {"nodes": ns, "edges": [{"source": t["id"], "relation": "referencia", "target": c["id"], "provenance": pv,
                                        "provenances": [pv]} for c in coms]}
    grafos = {tos[0]: to_g(tos[0], [com("Comunicacion_a_6847", "A-6847", "Com. A 6847")]),
              tos[1]: to_g(tos[1], [com("Comunicacion_comunicacion_a_6847", "Comunicación A 6847", "Comunicación A 6847")]),
              tos[2]: to_g(tos[2], [com("Comunicacion_a_6847", "A-6847", "A 6847")]),
              tos[3]: to_g(tos[3], [com("Comunicacion_a_sin_especificar", "A-<sin especificar>", "Com. A —")]),
              tos[4]: to_g(tos[4], [com("Comunicacion_a_sin_especificar", "A-<sin especificar>", "Com. A —")])}
    sys.path.insert(0, str(AQUI.parent / "parte2"))
    spec = importlib.util.spec_from_file_location("tam", str(AQUI.parent / "parte2" / "tamanos_desamb_mesa.py"))
    T = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(T)
    guardas = {"{}": {}} if variante == "head" else {"{}": {}, "none": {"codigo_comunicacion": None},
                                                     "c1": {"codigo_comunicacion": T.codigo_normalizado}}
    for nombre_g, kw in guardas.items():
        m = INV.merge_grafos_guardado(deepcopy(grafos), **kw)
        kg = {"nodes": m["nodes"], "edges": m["edges"]}
        inv = INV.verificar_invariantes(kg, m["grafos_pre_merge"], merges_nodo=len(m["merges_cross_to"]),
                                        merges_arista=INV.merges_arista_de(m["grafos_pre_merge"], kg["edges"]))
        clave = "guarda:" + nombre_g
        out[clave] = {"kg": kg, "adjudicacion": m["adjudicacion_cross_to"], "conflictos": m["conflictos"],
                      "uniones_c1": m.get("uniones_c1"), "invariantes_ok": inv["ok"], "invariantes_fallos": inv.get("fallos")}
    print(json.dumps(out, ensure_ascii=False, sort_keys=True, default=str))


def principal(CL):
    corr = lambda v: json.loads(subprocess.run([sys.executable, "-I", "-B", __file__, CL, v], capture_output=True, text=True, check=True).stdout)  # noqa: E731
    H, P = corr("head"), corr("parchado")
    fallas = []

    def ok(cond, que):
        print(("OK   " if cond else "FALLA") + " " + que)
        if not cond:
            fallas.append(que)
    for pref in ("resolver:", "reresolver:", "decidir_r2a:"):
        h = H[pref + "{}"]
        for kw in ("{}", json.dumps({"s1": False, "s2": False}, sort_keys=True)):
            ok(P[pref + kw] == h, f"{pref} con {kw}: el parchado da exactamente lo de HEAD")
    ok(H["guarda:{}"]["invariantes_ok"], "el caso sintético de la guarda pasa I1-I5 con el código de HEAD")
    ok(P["guarda:{}"] == H["guarda:{}"] and P["guarda:none"] == H["guarda:{}"],
       "guarda sin C1: el parchado da exactamente lo de HEAD (kg, adjudicación y conflictos)")
    base = {f["indice_relacion"]: f for f in H["resolver:{}"]["res"]["resolucion"]}

    def cambios(kw):
        res = {f["indice_relacion"]: f for f in P["resolver:" + json.dumps(kw, sort_keys=True)]["res"]["resolucion"]}
        return {CASOS[i][0]: (base[i]["metodo_resolucion"], base[i]["resuelto_a"], res[i]["metodo_resolucion"], res[i]["resuelto_a"],
                              res[i].get("regla_candidata")) for i in base if (base[i]["metodo_resolucion"], base[i]["resuelto_a"]) !=
                (res[i]["metodo_resolucion"], res[i]["resuelto_a"])}
    print("  HEAD, por caso:", {CASOS[i][0]: (f["metodo_resolucion"], f["resuelto_a"]) for i, f in base.items()})
    c1 = cambios({"s1": True})
    ok(set(c1) == {"c2_R3_contra_modelo", "c4_calificador_contra_modelo", "c9_tokens_contra_modelo"}
       and c1["c2_R3_contra_modelo"][2:] == ("R3", ROL, "S1") and c1["c4_calificador_contra_modelo"][2] == "R2_calificador",
       f"S1 cambia solo R3 y el calificador contra el modelo (también con mención por tokens): {c1}")
    c2 = cambios({"s2": True})
    ok(set(c2) == {"c5_mencion_no_verificada"} and c2["c5_mencion_no_verificada"][2:] == ("cuarentena", None, "S2"),
       f"S2 manda a cuarentena solo la sugerencia sin mención verificada: {c2}")
    c12 = cambios({"s1": True, "s2": True})
    ok(set(c12) == set(c1) | set(c2), "S1 y S2 juntas: la unión de las dos, sin otra diferencia")
    reg2 = P['resolver:{"s2": true}']["res"]["registro"]
    ok(any(r["motivo"] == "mencion_no_verificada" and r["sujeto_id_modelo"] == "Sujeto_banco" for r in reg2),
       "S2: la fila del registro guarda la sugerencia del modelo, como la parte A")
    rr_h = H["reresolver:{}"]["filas"]
    rr_1 = P['reresolver:{"s1": true}']["filas"]
    rr_2 = P['reresolver:{"s2": true}']["filas"]
    ok(rr_h[0]["metodo"] == "R4_sugerencia_modelo" and rr_1[0]["metodo"] == "R3" and rr_1[0]["resuelto_a"] == ROL,
       f"reresolver con S1: la fila que HEAD resuelve por R4 la resuelve R3 ({rr_h[0].get('metodo')} → {rr_1[0].get('metodo')})")
    ok(rr_h[1]["metodo"] == "R4_sugerencia_modelo" and rr_2[1]["estado"] == "cuarentena" and "metodo" not in rr_2[1],
       "reresolver con S2: la sugerencia sin mención verificada sigue en cuarentena (HEAD la resuelve por R4)")
    dh = H["decidir_r2a:{}"]
    for kw in ({"s1": True}, {"s2": True}):
        dp = P["decidir_r2a:" + json.dumps(kw, sort_keys=True)]
        n = sum(1 for a, b in zip(dh, dp) if a != b)
        print(f"  r2a (grafo de prueba), decidir con {kw}: cambian {n} de {len(dh)} filas")
    g = P["guarda:c1"]
    ids = sorted(n["id"] for n in g["kg"]["nodes"] if n["type"] == "Comunicacion")
    ok(ids == ["Comunicacion_a_6847", "Comunicacion_a_sin_especificar", "Comunicacion_a_sin_especificar__ext"],
       f"C1: A 6847 de tres documentos queda en un nodo; los marcadores, separados como siempre ({ids})")
    ok([a["id"] for a in g["adjudicacion"]] == ["Comunicacion_a_sin_especificar"] and len(g["uniones_c1"]) == 1
       and len(g["uniones_c1"][0]["nodos"]) == 3, "C1: la colisión de A 6847 no va a la adjudicación; queda en uniones_c1 con sus 3 nodos")
    ok(any(c["property"] == "label" for c in g["conflictos"]) and any(c["property"] == "codigo" for c in g["conflictos"]),
       "C1: las diferencias de label y de código quedan como conflictos del merge sellado")
    refs = [e for e in g["kg"]["edges"] if e["relation"] == "referencia" and e["target"] == "Comunicacion_a_6847"]
    ok(len(refs) == 3 and g["invariantes_ok"], f"C1: las 3 aristas referencia apuntan al nodo unido; invariantes I1-I5 OK ({len(refs)})")
    print("FALLAS:", len(fallas))
    return 1 if fallas else 0


if __name__ == "__main__":
    if len(sys.argv) == 3:
        trabajador(sys.argv[1], sys.argv[2])
    else:
        raise SystemExit(principal(sys.argv[1]))
