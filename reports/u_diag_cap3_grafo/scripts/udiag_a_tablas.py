"""Tarea a: consolidación. Causa final de cada Excepcion sin `exceptua`/`exceptua_obligacion` saliente y de cada
Condicion sin `condicion_de` saliente (a9631a64 y e22fae1a), con la clase determinística de `udiag_a_casos.py` y,
para los casos que el código no decide, el código de la lectura (`lectura_a.json`). Cruce con la regla E
(`union_e.json`), controles de lectura con Wilson y cifras de la firma F.

Causas (despacho, tarea a.1):
  (i)   la regla está en otra unidad: por código (la unidad no extrajo ningún nodo de un tipo admisible como destino)
        o por lectura (I-ENC, en un bloque heredado; I-OTRA, fuera de la herencia);
  (ii)  la regla es una Operacion de la misma unidad: emitida y rechazada por firma, o no emitida (lectura II-OP);
  (iii) la relación se emitió y cayó por otro rechazo del validador: firma hacia otro tipo, o destino no emitido
        (`ref_colgante`);
  (iv)  nunca se emitió y la regla está en la unidad: IV-OMI (con nodo admisible) o IV-NOEXT (sin nodo admisible);
  (v)   otra: V-DEF (acota una definición) o V-OTRA.
Uso: PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B udiag_a_tablas.py
Escribe salida/tabla_a.json y salida/tabla_a.md.
"""
import collections
import json
import os

from udiag_comun import AQUI, wilson

OUT = os.path.join(AQUI, "salida")
CAUSA = {"I-ENC": "(i)", "I-OTRA": "(i)", "II-OP": "(ii)", "IV-OMI": "(iv)", "IV-NOEXT": "(iv)",
         "V-DEF": "(v)", "V-OTRA": "(v)"}
ORDEN = ("(i)", "(ii)", "(iii)", "(iv)", "(v)")


def leer(nombre, por_defecto=None):
    p = os.path.join(OUT, nombre)
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else por_defecto


def clasificar(c, lect, lect_i):
    k = c["clase_det"]
    if k == "I-SIN-NORMA-EN-LA-UNIDAD" and c["id"] in lect_i:
        cod = lect_i[c["id"]]
        return CAUSA[cod], f"lectura_grupo_sin_admisible:{cod}"
    if k == "II-OP-RECHAZADA":
        return "(ii)", "ii.emitida_rechazada_por_firma_hacia_Operacion"
    if k == "III-FIRMA":
        return "(iii)", "iii.firma_invalida:" + ";".join(c["firmas_rechazadas"])
    if k == "III-COLGANTE":
        return "(iii)", "iii.destino_no_emitido_ref_colgante"
    if k == "I-SIN-NORMA-EN-LA-UNIDAD":
        return "(i)", "i.por_codigo_sin_nodo_admisible_en_la_unidad"
    if k == "LEER":
        cod = lect[c["n"]]["codigo"]
        return CAUSA[cod], f"lectura:{cod}"
    raise ValueError(k)


def main():
    casos = leer("casos_a.json")
    lect = {x["caso"]: x for x in leer("lectura_a.json")}
    leidos = [c for c in casos["diez"] if c["clase_det"] == "LEER"]
    for k, c in enumerate(leidos, 1):
        c["n"] = k
    # el grupo sin nodo admisible en la unidad, leído entero: control (1) más el resto (dos partes)
    lect_i = {}
    for m, l, clave in (("muestra_control_i.json", "lectura_control_i.json", "control"),
                        ("muestra_resto_i.json", "lectura_resto_i_parte1.json", "resto"),
                        ("muestra_resto_i.json", "lectura_resto_i_parte2.json", "resto")):
        mm, ll = leer(m, []), leer(l, [])
        ids = {x[clave]: x["id"] for x in mm}
        for x in ll:
            lect_i[ids[x[clave]]] = x["codigo"]
    out_lect_i = len(lect_i)
    for c in casos["diez"]:
        c["causa"], c["sub"] = clasificar(c, lect, lect_i)
    union = leer("union_e.json")
    res_e = {nombre: {f["id"]: f for f in union[nombre]["filas"]} for nombre in ("diez", "sincola")}
    ids_s = set(casos["ids_sincola"])
    out = {"fuentes_sha256": casos["kg_sha256"], "grupo_sin_admisible_leidos": out_lect_i}
    for nombre in ("diez", "sincola"):
        cs = [c for c in casos["diez"] if nombre == "diez" or c["id"] in ids_s]
        g = {}
        for t in ("Excepcion", "Condicion"):
            ct = [c for c in cs if c["type"] == t]
            g[t] = {
                "total": len(ct),
                "por_causa": {k: sum(1 for c in ct if c["causa"] == k) for k in ORDEN},
                "por_subcausa": dict(collections.Counter(c["sub"] for c in ct).most_common()),
                "por_causa_y_tipo_de_unidad": {k: dict(collections.Counter(
                    c["tipo_unidad"] for c in ct if c["causa"] == k).most_common()) for k in ORDEN},
                "por_tipo_de_unidad": dict(collections.Counter(c["tipo_unidad"] for c in ct).most_common()),
                "por_to": dict(collections.Counter(c["to"] for c in ct).most_common()),
                "por_causa_y_to": {k: dict(collections.Counter(c["to"] for c in ct if c["causa"] == k).most_common())
                                   for k in ORDEN},
                "relacion_emitida_en_otro_intento": sum(1 for c in ct if c["emitida_en_otro_intento"]),
                "con_origen_en_una_unidad_de_la_cola": sum(1 for c in ct if any(o["en_cola"] for o in c["origenes"])),
                "regla_E_en_los_items": {f"{k}|{r}": v for (k, r), v in collections.Counter(
                    (c["causa"], res_e[nombre][c["id"]]["resultado"]) for c in ct if c["id"] in res_e[nombre]
                ).most_common()},
            }
            assert sum(g[t]["por_causa"].values()) == g[t]["total"]
        out[nombre] = g
    # controles de lectura
    lu = leer("lectura_union_e.json")
    if lu:
        juicios = [x["juicio"] for x in lu["lecturas"]]
        ok = sum(j == "correcta" for j in juicios)
        out["lectura_union_e"] = {"n": len(juicios), "por_juicio": dict(collections.Counter(juicios)),
                                  "correctas_wilson": [ok, wilson(ok, len(juicios))],
                                  "correctas_o_dudosas_wilson": [ok + juicios.count("dudosa"),
                                                                 wilson(ok + juicios.count("dudosa"), len(juicios))],
                                  "piso_l_esq_r2_6_3": "0,75 (con 30, 28 correctas)"}
    rl = leer("relectura_25_sesion.json")
    if rl:
        g = lambda x: CAUSA[x]
        ex = sum(x["codigo"] == lect[x["caso"]]["codigo"] for x in rl)
        ca = sum(g(x["codigo"]) == g(lect[x["caso"]]["codigo"]) for x in rl)
        out["relectura_concordancia"] = {"n": len(rl), "mismo_codigo": [ex, wilson(ex, len(rl))],
                                         "misma_causa": [ca, wilson(ca, len(rl))]}
    ci = leer("lectura_control_i.json")
    if ci:
        conf = sum(CAUSA.get(x["codigo"], "?") == "(i)" for x in ci)
        out["control_i_por_codigo"] = {"n": len(ci), "por_codigo": dict(collections.Counter(x["codigo"] for x in ci)),
                                       "confirma_i_wilson": [conf, wilson(conf, len(ci))]}
    li = [x for nombre in ("lectura_control_i.json", "lectura_resto_i_parte1.json", "lectura_resto_i_parte2.json")
          for x in leer(nombre, [])]
    if li:
        conf = sum(CAUSA.get(x["codigo"]) == "(i)" for x in li)
        out["grupo_sin_admisible_lectura_entera"] = {"n": len(li), "por_codigo": dict(collections.Counter(
            x["codigo"] for x in li).most_common()), "confirma_i": conf}
    gr = leer("lectura_g_r_22.json")
    if gr:
        out["lectura_g_r_22"] = {"coherentes_wilson": [gr["coherentes"], wilson(gr["coherentes"], gr["n"])]}
    cf = leer("lectura_control_f.json")
    if cf:
        js = [x["juicio"] for x in cf]
        ok = js.count("correcta")
        out["control_f_41"] = {"n": len(js), "por_juicio": dict(collections.Counter(js)),
                               "correctas_wilson": [ok, wilson(ok, len(js))],
                               "mejor_destino_de_las_incorrectas": dict(collections.Counter(
                                   (x.get("mejor_destino") or "null").split(" ")[0] if x["juicio"] != "correcta" else "-"
                                   for x in cf).most_common())}
    ff = leer("firma_f.json")
    out["firma_f"] = ff["resumen"]
    out["firma_f"]["solo_exceptua"] = {
        "rechazos": sum(1 for f in ff["filas"] if f["predicado"] == "exceptua"),
        "nodos_excepcion": len({f["excepcion"] for f in ff["filas"] if f["predicado"] == "exceptua"}),
        "unidades": len({f["chunk_id"] for f in ff["filas"] if f["predicado"] == "exceptua"}),
        "unidades_por_to": dict(collections.Counter(c.split("::")[0] for c in sorted({
            f["chunk_id"] for f in ff["filas"] if f["predicado"] == "exceptua"})).most_common())}
    out["regla_e"] = {nombre: union[nombre]["resumen"] for nombre in ("diez", "sincola")}
    json.dump(out, open(os.path.join(OUT, "tabla_a.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # tabla en markdown
    lin = ["# Tarea a: Excepcion y Condicion sin unir a su regla, por causa", "",
           "Fuente: `tabla_a.json` (este script). a9631a64 (diez) y e22fae1a (sin cola).", ""]
    for nombre in ("diez", "sincola"):
        for t in ("Excepcion", "Condicion"):
            g = out[nombre][t]
            lin += [f"## {nombre}: {t} ({g['total']})", "",
                    "| causa | " + " | ".join(ORDEN) + " | total |", "|---|" + "---:|" * (len(ORDEN) + 1),
                    "| nodos | " + " | ".join(str(g["por_causa"][k]) for k in ORDEN) + f" | {g['total']} |", ""]
            tus = sorted(g["por_tipo_de_unidad"], key=lambda x: -g["por_tipo_de_unidad"][x])
            lin += ["| tipo de unidad | " + " | ".join(ORDEN) + " | total |", "|---|" + "---:|" * (len(ORDEN) + 1)]
            for tu in tus:
                lin.append(f"| {tu} | " + " | ".join(str(g["por_causa_y_tipo_de_unidad"][k].get(tu, 0)) for k in ORDEN)
                           + f" | {g['por_tipo_de_unidad'][tu]} |")
            lin += ["", "| TO | " + " | ".join(ORDEN) + " | total |", "|---|" + "---:|" * (len(ORDEN) + 1)]
            for to in g["por_to"]:
                lin.append(f"| {to} | " + " | ".join(str(g["por_causa_y_to"][k].get(to, 0)) for k in ORDEN)
                           + f" | {g['por_to'][to]} |")
            lin += ["", "Subcausas: " + "; ".join(f"{k} {v}" for k, v in g["por_subcausa"].items()), ""]
    open(os.path.join(OUT, "tabla_a.md"), "w", encoding="utf-8").write("\n".join(lin))
    for nombre in ("diez", "sincola"):
        print(nombre, {t: out[nombre][t]["por_causa"] for t in ("Excepcion", "Condicion")})
    print(json.dumps({k: out[k] for k in out if k.startswith(("lectura", "relectura", "control"))}, ensure_ascii=False))


if __name__ == "__main__":
    main()
