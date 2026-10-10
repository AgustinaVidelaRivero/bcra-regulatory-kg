"""U-OMISIONES-COD, O2 — las medidas sobre la tanda 0 con el código nuevo (nota del 09/10/2026 al pie de la v7, punto 2):
por grafo r2b (diez y desarrollo, con y sin cola), lo que cuenta cada grupo, leído del reporte del ensamblado, de los
registros y del grafo. Solo lee. Uso: python -B medidas_tanda0_O2.py --grafo nombre=<dir r2> [...] --out <json>"""
import argparse, json, sys
from collections import Counter, OrderedDict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import medir_h_i as HI  # noqa: E402

def jl(p):
    return [json.loads(x) for x in Path(p).read_text(encoding="utf-8").splitlines() if x.strip()]

def condiciones(kg):
    def rf(e): return e.get("rol_fuente") or (e.get("properties") or {}).get("rol_fuente")
    tipo = {n["id"]: n["type"] for n in kg["nodes"]}
    cont, cd, grado = set(), set(), Counter()
    for e in kg["edges"]:
        grado[e["source"]] += 1; grado[e["target"]] += 1
        if not (e["relation"] in ("establecida_en", "remite_a") or (e["relation"] == "referencia" and rf(e) == "referencia_cruzada")):
            cont |= {e["source"], e["target"]}
        if e["relation"] == "condicion_de":
            cd.add(e["source"])
    c = [i for i, t in tipo.items() if t == "Condicion"]
    ais = [i for i in tipo if grado[i] == 0]
    return {"condicion": len(c), "sin_arista_de_contenido": sum(1 for i in c if i not in cont),
            "sin_condicion_de_saliente": sum(1 for i in c if i not in cd), "aislados": len(ais),
            "aislados_por_tipo": dict(Counter(tipo[i] for i in ais))}

ap = argparse.ArgumentParser(); ap.add_argument("--grafo", action="append", required=True); ap.add_argument("--out", type=Path, required=True)
a = ap.parse_args(); res = OrderedDict()
for x in a.grafo:
    nom, d = x.split("=", 1); d = Path(d)
    r = json.loads((d / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
    kg = json.loads((d / "kg.json").read_text(encoding="utf-8"))
    u = r["umbrales"]
    com = [n for n in kg["nodes"] if n["type"] == "Comunicacion"]
    ra = [e for e in kg["edges"] if e["relation"] == "remite_a"]
    nav = HI.navegacion(kg)
    res[nom] = OrderedDict([
        ("sha256_kg", r["sha256_kg"]), ("nodos", r["nodes_total"]), ("aristas", r["edges_total"]),
        ("A_omisiones", r["omisiones"]), ("A_supuestos_en_norma", r["supuestos_en_norma"]),
        ("B_resolucion", {"por_metodo": r["resolucion_sujetos"]["por_metodo"],
                          "desacuerdos_regla_modelo": r["resolucion_sujetos"]["desacuerdos_regla_modelo"],
                          "registro_no_mapeados": {k: r["registro_no_mapeados"][k] for k in ("filas", "por_estado")},
                          "sujetos_propuestos": sum(1 for n in kg["nodes"] if n["type"] == "Sujeto"
                                                    and n["properties"].get("nivel") == "propuesto")}),
        ("C_base", {k: u[k] for k in ("base_del_validador", "base_no_resuelta_por_motivo", "base_por_origen")}),
        ("L_tramo_de_e1", {k: v for k, v in u["tramo_de_e1"].items() if k != "conservan_la_cuantia"}),
        ("L_conservan_la_cuantia", u["tramo_de_e1"].get("conservan_la_cuantia", [])),
        ("G_r", r["procedencia_g_r"]),
        ("H_comunicacion", {"total": len(com), "por_tipo": dict(Counter(str(n["properties"].get("tipo")) for n in com)),
                            "con_tipo_no_derivable": sum(1 for n in com if (n.get("properties_no_definidas") or {}).get("tipo_no_derivable")),
                            "sin_tratar": sum(1 for n in com if not n["properties"].get("tipo")
                                              and not (n.get("properties_no_definidas") or {}).get("tipo_no_derivable"))}),
        ("I_condiciones_sin_regla", condiciones(kg)),
        ("J_remite_a", {"aristas": len(ra), "procedencia_sin_tramo_con_la_marca": sum(
            1 for e in ra if e["provenance"].get("tramo") is None and e["provenance"].get("tramo_verificado") == "ausente"),
                        "procedencia_sin_tramo_sin_la_marca": sum(1 for e in ra if e["provenance"].get("tramo") is None
                                                                  and e["provenance"].get("tramo_verificado") != "ausente")}),
        ("K_irresolubles_por_causa", r["remite_a"]["irresolubles_por_causa"]),
        ("h_aristas_por_origen", r["aristas_por_origen"]),
        ("i_ventana_del_agente", {"con_remite_a": nav["ventana_del_agente_con_remite_a"]["n"],
                                  "sin_remite_a": nav["ventana_del_agente_sin_remite_a"]["n"],
                                  "referencia_v6_solo_remite_a": nav["grado_total_solo_remite_a"]["n"],
                                  "referencia_v6_sin_remite_a": nav["grado_total_sin_remite_a"]["n"],
                                  "lista_con_remite_a": [y["id"] for y in nav["ventana_del_agente_con_remite_a"]["lista"]],
                                  "lista_sin_remite_a": [y["id"] for y in nav["ventana_del_agente_sin_remite_a"]["lista"]]}),
        ("validacion_modelos_r2", {k: r["validacion_modelos_r2"][k] for k in ("nodos_fuera_del_modelo", "aristas_fuera_del_modelo")}),
        ("doble_corrida_byte_identica", r["doble_corrida_byte_identica"])])
a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for nom, v in res.items():
    print(nom, v["sha256_kg"][:8], "| A", v["A_omisiones"]["tramo_en_heredado"]["filas"], v["A_omisiones"]["revisar"]["filas"], v["A_omisiones"]["texto_propio_entero"]["filas"], v["A_supuestos_en_norma"]["entidades"],
          "| C", v["C_base"]["base_del_validador"], "| L", v["L_tramo_de_e1"], "| G-r", {k: v["G_r"][k] for k in ("cambia_el_punto", "solo_el_rol")},
          "| H", v["H_comunicacion"]["con_tipo_no_derivable"], v["H_comunicacion"]["sin_tratar"], "| I", v["I_condiciones_sin_regla"]["sin_arista_de_contenido"], v["I_condiciones_sin_regla"]["condicion"],
          "| J", v["J_remite_a"], "| K", v["K_irresolubles_por_causa"].get("destino_en_unidad_excluida"), v["K_irresolubles_por_causa"].get("punto_sin_nodos"),
          "| h", v["h_aristas_por_origen"], "| i", v["i_ventana_del_agente"]["con_remite_a"], v["i_ventana_del_agente"]["sin_remite_a"])
