"""
freno_t1_cifras.py — B6.1, tanda final, T1: todas las cifras y tablas del FRENO T1, desde los archivos que las respaldan
(pre-registro firmado de la tanda final, §7: «toda cifra del FRENO sale por script»). USD 0, sin API. Solo lee; escribe
--md y --json. No abre ningún NO_ABRIR_.

Fuentes (todas relativas a --repo):
  - la versión derivada de T1 y las cifras del pre-registro (data/experiment/tanda_final/preregistro/);
  - data/experiment/tanda_final/t1/: e0/, manifiesto/, entradas/, seco/, ensamblado/, pruebas_t2/, estimaciones/, la
    consulta de deprecaciones y sha256_para_T2.txt;
  - el manifiesto de la tanda final y su alternativa con el reparto.
Uso: python3 -I -B freno_t1_cifras.py --repo <raíz> --md <salida.md> --json <salida.json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from decimal import Decimal
from pathlib import Path

sys.dont_write_bytecode = True
T1 = "data/experiment/tanda_final/t1"
PRE = "data/experiment/tanda_final/preregistro"
MAN = "data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--md", type=Path, required=True)
    ap.add_argument("--json", type=Path, required=True)
    a = ap.parse_args()
    r = a.repo.resolve()
    leer = lambda rel: json.loads((r / rel).read_text(encoding="utf-8"))  # noqa: E731
    sha = lambda rel: hashlib.sha256((r / rel).read_bytes()).hexdigest()  # noqa: E731
    md: list[str] = []
    out: dict = {}

    def tabla(titulo: str, cab: list[str], filas: list[list]) -> None:
        md.append(f"\n### {titulo}\n")
        md.append("| " + " | ".join(cab) + " |")
        md.append("|" + "|".join("---" for _ in cab) + "|")
        for f in filas:
            md.append("| " + " | ".join(str(x) for x in f) + " |")

    # 1. la versión derivada de T1
    h = leer(f"{PRE}/preregistro_tanda_final_derivada_T1.huecos.json")
    cif = leer(f"{PRE}/salida_cifras_preregistro_tanda_final.json")
    out["derivada"] = {"md_sha256": sha(f"{PRE}/preregistro_tanda_final_derivada_T1.md"),
                       "huecos_sha256": sha(f"{PRE}/preregistro_tanda_final_derivada_T1.huecos.json"),
                       "cifras_fuente": h["cifras"]["fuente"], "cifras_sha256": h["cifras"]["sha256"],
                       "documentos_fuera": cif["documentos_fuera"], "costo": cif["costo"],
                       "tramos": {k: {x: v[x] for x in ("tos", "unidades")} for k, v in cif["tramos"].items()},
                       "bases_control_entre_tramos": cif["bases_control_entre_tramos"]}
    c = cif["costo"]
    tabla("1. Las cifras con las que corre la tanda (versión derivada de T1, sección final)", ["cifra", "valor"],
          [["documentos fuera", cif["documentos_fuera"] or "ninguno"], ["U", c["U"]], ["tarifa", c["tarifa"]],
           ["estimado (U × tarifa)", c["estimado"]], ["tope (derivada, 2 decimales)", c["tope"]],
           ["tramo 1: estimado", c["tramo_1_estimado"]], ["tramo 2: estimado", c["tramo_2_estimado"]]]
          + [[f"{k}: TOs y unidades", f"{v['tos']} y {v['unidades']}"] for k, v in out["derivada"]["tramos"].items()]
          + [[f"base del control: {k}", v] for k, v in cif["bases_control_entre_tramos"].items()
             if k.startswith(("umbral", "base", "costo"))])

    # 2. la E0
    cc, c152, c98 = (leer(f"{T1}/e0/{n}") for n in ("control_codigo_raiz_t1.json", "control_e0_152_t1.json",
                                                    "control_e0_98_t1.json"))
    hc = leer(f"{T1}/e0/comparacion_resumen_hc_t1.json")
    rhc = leer(f"{T1}/e0/resumen_healthcheck_tanda_final_t1.json")
    ag = {n: v["igual"] for n, v in c98["agregados"].items()}
    out["e0"] = {"codigo": {n: v["igual"] for n, v in cc["codigo"].items()}, "c152": {k: c152[k] for k in
                 ("esperados", "iguales", "tos", "unidades")}, "por_to": f"{c98['por_to_iguales']} de {c98['por_to_esperados']}",
                 "corridas_98": [c98["archivos_corrida_1"], c98["archivos_corrida_2"], c98["corridas_98_iguales"]],
                 "agregados": ag, "primer_nivel": c98["primer_nivel"], "unidades": c98["unidades"],
                 "pdfs": c98["pdfs_iguales"], "hc": {"verde": hc["verde"], "diferencias": hc["n_diferencias"],
                 "resumen_sha256": hc["resumen_sha256"], "referencia_sha256": hc["referencia_sha256"],
                 "hc_sha256": rhc["hc_sha256"], "veredictos": rhc["veredictos"]}}
    tabla("2. La E0 de los 98 con el código del gate", ["control", "resultado"],
          [["código de la raíz contra S0-6b", f"{sum(out['e0']['codigo'].values())} de {len(cc['codigo'])} ({cc['veredicto']})"],
           ["los 152 contra el manifiesto de S0-6b", f"{c152['iguales']} de {c152['esperados']}, {c152['tos']} TOs, {c152['unidades']} unidades ({c152['veredicto']})"],
           ["las dos corridas de los 98", f"{c98['archivos_corrida_1']} y {c98['archivos_corrida_2']} archivos, iguales: {c98['corridas_98_iguales']}"],
           ["archivos por TO contra S0-6b", out["e0"]["por_to"]],
           ["agregados contra los 152 restringidos", f"{sum(ag.values())} de {len(ag)} iguales ({', '.join(n for n, v in c98['agregados'].items() if not v.get('en_los_98'))} falta y el restringido da vacío)" if any(not v.get("en_los_98") for v in c98["agregados"].values()) else f"{sum(ag.values())} de {len(ag)} iguales"],
           ["version_e0.json", c98["version_e0_igual"]], ["primer nivel", f"{c98['primer_nivel']} archivos, faltan {len(c98['faltan'])}, sobran {len(c98['sobran'])}"],
           ["unidades", f"{c98['unidades']} (cada TO con su unidades_por_to: {c98['unidades_ok']})"],
           ["PDF contra S1-ter (dos carpetas)", f"{c98['pdfs_iguales']} de {2 * c98['n_tos']}"],
           ["control de salud", f"verde: {hc['verde']}; diferencias con S2c: {hc['n_diferencias']}; veredictos {rhc['veredictos']}"]])

    # 3. el manifiesto
    ip, ir, ic = (leer(f"{T1}/manifiesto/{n}") for n in ("info_armado_plano.json", "info_armado_reparto_alternativa.json",
                                                        "info_armado_contra_perfil_anterior_a3.json"))
    m = leer(MAN)
    mr = leer(f"{T1}/manifiesto/tanda_final_98tos_r2b_reparto_alternativa.json")
    est1 = leer(f"{T1}/seco/estimado_por_to_t1.json")["por_to"]
    out["manifiesto"] = {"sha256": sha(MAN), "reparto_sha256": sha(f"{T1}/manifiesto/tanda_final_98tos_r2b_reparto_alternativa.json"),
                         "contra_sha256": sha(f"{T1}/manifiesto/tanda_final_98tos_r2b_contra_perfil_anterior_a3.json"),
                         "plano": ip, "reparto": ir, "contra": {k: ic[k] for k in ("con_alcance", "sin_alcance")}}
    tabla("3. El manifiesto (plano, en el repo) y la alternativa con el reparto", ["cifra", "plano (repo)", "reparto (alternativa)"],
          [["sha256", sha(MAN)[:16] + "…", out["manifiesto"]["reparto_sha256"][:16] + "…"],
           ["TOs y unidades", f"{ip['tos']} y {ip['unidades']}", f"{ir['tos']} y {ir['unidades']}"],
           ["estimado total", ip["estimado_total_usd"], ir["estimado_total_usd"]],
           ["tramo 1", ip["tramo_1_estimado_usd"], ir["tramo_1_estimado_usd"]],
           ["tramo 2", ip["tramo_2_estimado_usd"], ir["tramo_2_estimado_usd"]],
           ["U × tarifa + 0,209440 (A3)", ip["u_por_tarifa_mas_lineas_a3_usd"], ir["u_por_tarifa_mas_lineas_a3_usd"]],
           ["diferencia", ip["diferencia_contra_u_por_tarifa_mas_lineas_a3"], ir["diferencia_contra_u_por_tarifa_mas_lineas_a3"]],
           ["líneas de A3 por documento, sumadas", ip["lineas_a3_por_documento_sumadas_usd"], ir["lineas_a3_por_documento_sumadas_usd"]],
           ["resto del reparto", ip["resto_del_reparto_usd"], f"{ir['resto_del_reparto_usd']} (al e3 de {ir['resto_al_e3_de']})"],
           ["tope", f"{ip['tope_usd']} (exacto {ip['tope_exacto']})", ir["tope_usd"]],
           ["con alcance / sin alcance", f"{ip['con_alcance']} / {len(ip['sin_alcance'])}", f"{ir['con_alcance']} / {len(ir['sin_alcance'])}"],
           ["chars_completo de la E0", ip["chars_completo"], ir["chars_completo"]],
           ["tramo 1: proporción de las unidades y de los caracteres",
            f"{round(100 * sum(est1[t]['unidades_e0'] for t in m['orden_corrida'][:30]) / ip['unidades'], 1)} % y "
            f"{round(100 * sum(est1[t]['chars_completo'] for t in m['orden_corrida'][:30]) / ip['chars_completo'], 1)} %", "igual"],
           ["checkpoint_cada", m["limites"]["checkpoint_cada"], mr["limites"]["checkpoint_cada"]],
           ["archivos de la E0 en los sellos", m["sellos"]["e0"]["archivos"], mr["sellos"]["e0"]["archivos"]]])
    md.append("\n`orden_corrida`, tramo 1: " + ", ".join(m["orden_corrida"][:30]) + ".")
    md.append("\n`orden_corrida`, tramo 2: " + ", ".join(m["orden_corrida"][30:]) + ".")
    md.append(f"\nSin alcance declarado (rol_alcance null): {', '.join(ip['sin_alcance'])}.")

    # 4. el control de entradas
    ce = leer(f"{T1}/entradas/control_entradas_t1.json")
    sc = leer(f"{T1}/entradas/resumen_sin_cuentas_t1.json")
    out["entradas"] = {"veredicto": ce["veredicto"], "controles": {k: v["ok"] for k, v in ce["controles"].items()},
                       "selftest_sin_cuentas": {k: v for k, v in sc.items() if k != "salidas"}}
    i = ce["controles"]["i_mensajes_e1_contra_la_base_de_a3"]["por_tanda"]
    tabla("4. El control de entradas", ["control", "OK"], [[k, v["ok"]] for k, v in ce["controles"].items()]
          + [["veredicto", ce["veredicto"]],
             ["mensajes, tanda 0", f"{i['tanda0']['iguales']} de {i['tanda0']['unidades_copia']} iguales a la base de A3"],
             ["mensajes, tanda 1", f"{i['tanda1']['iguales']} de {i['tanda1']['unidades_copia']} iguales a la base de A3"],
             ["mensajes, tanda final", f"{i['tanda_final']['unidades_que_cambian']} unidades de {i['tanda_final']['documentos_que_cambian']} documentos cambian, todas solo en la línea de alcance ({i['tanda_final']['cambian_solo_en_la_linea_de_alcance']}); los otros, iguales: {i['tanda_final']['los_otros_documentos_iguales_byte_a_byte']}"],
             ["selftest_clave_cache sin cuentas = A3 sin cuentas (JSON, consola)", f"{sc['json_igual_al_de_a3_sin_cuentas']}, {sc['consola_igual_a_la_de_a3_sin_cuentas']}; veredicto {sc['veredicto_del_selftest']}"],
             ["control en contra", ce["controles"]["m_carga_y_control_en_contra"]["control_en_contra"].get("documento")],
             ["recorte de herencia (tanda final)", ce["controles"]["j_herencia_recortada_tanda_final"]["por_to"]]])

    # 5. la corrida en seco
    s = leer(f"{T1}/seco/corrida_en_seco_t1.json")
    pe = s["pedidos_por_etapa"]
    out["seco"] = {k: s[k] for k in ("rc_del_runner", "excepcion", "llamadas_a_la_api", "ramas_recorridas", "ramas_forzadas",
                                     "sin_declarar", "veredicto", "unidades_e0", "primer_intento_e1",
                                     "claves_ya_en_las_bases_de_la_copia")}
    tabla("5. La corrida en seco: pedidos por etapa", ["etapa", "pedidos", "claves distintas", "modelos", "max_tokens",
                                                       "temperaturas", "namespaces"],
          [[e, v["pedidos"], v["claves_distintas"], v["modelos"], v["max_tokens"], v["temperaturas"], v["namespaces"]]
           for e, v in pe.items()])
    ped = [json.loads(x) for x in (r / f"{T1}/seco/pedidos_t1.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    dup: dict[str, list] = {}
    for p in ped:
        if p["etapa"] == "e1" and p["max_tokens"] == 8192:
            dup.setdefault(p["clave"], []).append(p)
    rep = {k: v for k, v in dup.items() if len(v) > 1}
    out["seco"]["primer_intento_claves_repetidas"] = {"claves": len(rep), "pedidos_de_mas": sum(len(v) - 1 for v in rep.values())}
    ra = s["ramas"]
    tabla("6. Las cinco ramas", ["rama", "unidades"],
          [["corte y reintento por corte", f"{len(ra['corte_y_reintento_por_corte_resuelto'])}"],
           ["partición por corte", {k: len(v) for k, v in ra["particion_por_corte"].items()}],
           ["tercer escalón", f"{len(ra['tercer_escalon'])}; cortan también: {len(ra['tercer_escalon_corta_tambien'])}"],
           ["salida mal formada (rforma1 bien, reparada, error)", f"{ra['salida_mal_formada_rforma1_bien']}, {ra['salida_mal_formada_reparada']}, {ra['salida_mal_formada_error']}"],
           ["ratchet de E3", ra["reintento_ratchet_e3"]],
           ["llamadas a la API", s["llamadas_a_la_api"]], ["rc del runner", s["rc_del_runner"]],
           ["claves ya en las bases de la copia", {k: v.get("presentes") for k, v in s["claves_ya_en_las_bases_de_la_copia"].items()}],
           ["primer intento de E1: pedidos y claves distintas", f"{s['primer_intento_e1']['pedidos']} y {s['primer_intento_e1']['claves_distintas']} ({out['seco']['primer_intento_claves_repetidas']['claves']} claves con más de un pedido)"]])
    ce_ = leer(f"{T1}/seco/censo_unidades_grandes_t1.json")
    cap = ce_["capacidad"]
    out["censo"] = {k: v for k, v in ce_.items() if k != "censo"}
    tabla(f"7. Las unidades que no entran en una llamada (capacidad del reintento con la p90: {cap['reintento_p90_chars']} caracteres; del tercer escalón: {cap['tercer_escalon_p90_chars']})",
          ["unidad", "caracteres", "se parte", "partes (caracteres)", "mecanismo", "en la corrida en seco"],
          [[d["chunk_id"], d["chars_propio"], "sí" if d["se_parte"] else f"no ({d['particion'].get('motivo')})",
            [p["chars_propio"] for p in d.get("partes", [])] or "—", d["mecanismo"],
            ("tercer escalón" if d["en_la_corrida_en_seco"]["escalon_3"] else "")
            + (f"partes {len(d['en_la_corrida_en_seco']['partes'])}; con tercer escalón {d['en_la_corrida_en_seco']['partes_con_escalon_3']}"
               if d["en_la_corrida_en_seco"]["partes"] else "")] for d in ce_["censo"]])
    md.append(f"\nClase A (sin partición posible, sobre la capacidad del reintento): {len(ce_['clase_a_sin_particion_posible'])}; "
              f"sobre la capacidad con la mediana: {len(ce_['clase_a_sobre_la_capacidad_mediana'])}; sobre el tercer escalón: "
              f"{len(ce_['sobre_el_tercer_escalon_p90'])}; sin declarar: {len(ce_['sin_declarar'])}; entre 8.192 y 16.384 con la p90: "
              f"{ce_['entre_8192_y_16384_con_la_p90']}.")

    # 8. el estimado por TO
    est = leer(f"{T1}/seco/estimado_por_to_t1.json")
    out["estimado"] = {k: v for k, v in est.items() if k != "por_to"}
    tabla("8. El estimado por TO (tarifa del §3 y líneas de A3; el del manifiesto, plano; y el de la alternativa con el reparto)",
          ["#", "TO", "tramo", "unid.", "chars_completo", "e1", "e3", "total", "= manifiesto", "reparto (alternativa)", "cortes p90"],
          [[n + 1, to, 1 if n < 30 else 2, f["unidades_e0"], f["chars_completo"], f["e1_usd"], f["e3_usd"], f["total_usd"],
            f["igual_al_manifiesto"], str(Decimal(str(mr["limites"]["estimado_usd"][to]["e1"])) + Decimal(str(mr["limites"]["estimado_usd"][to]["e3"]))),
            f["pedidos_que_cortan_con_la_p90"]] for n, (to, f) in enumerate(est["por_to"].items())])
    md.append(f"\nTotal: {est['unidades']} unidades, USD {est['total_usd']} ({est['total_a_4_decimales']} a 4 decimales); "
              f"iguales al manifiesto: {est['iguales_al_manifiesto']} de {est['tos']}; tope {est['tope_usd']}, margen "
              f"{est['margen_usd']}, tope sobre estimado {est['tope_sobre_estimado']}; el runner lo lee como "
              f"{est['estimado_total_del_runner_usd']}; cota de la salida de los cortes con la p90: {est['salida_de_los_cortes_p90_usd_cota']}.")

    # 9. el ensamblado del subconjunto
    en = leer(f"{T1}/ensamblado/resumen_ensamblado_tramo1_t1.json")
    out["ensamblado"] = {"corrio": en["corrio"], "grafos": {n: {k: g.get(k) for k in ("rc", "nodos", "aristas", "kg_sha256",
                         "manifiesto_carga", "nombres_remision_tos")} | {"doble": (g.get("reporte") or {}).get("doble_corrida_byte_identica")}
                         for n, g in en["grafos"].items()}}
    tabla("9. El ensamblado del tramo 1 (salida stub con el TextoOrdenado)", ["grafo", "rc", "nodos", "aristas", "kg sha256",
                                                                            "doble corrida interna", "TOs", "con nombres_remision"],
          [[n, g["rc"], g["nodos"], g["aristas"], g["kg_sha256"][:16] + "…", g["doble"], g["manifiesto_carga"],
            g["nombres_remision_tos"]] for n, g in out["ensamblado"]["grafos"].items()])

    # 10. las pruebas de T2
    filas = []
    for log in ("lanzador_prueba_1.log", "lanzador_prueba_2_control_freno.log", "lanzador_prueba_3_pausa.log",
                "lanzador_prueba_3b_antes_de_la_pausa.log", "lanzador_prueba_4_caso_en_contra_modelo.log"):
        lin = (r / f"{T1}/pruebas_t2/{log}").read_text(encoding="utf-8").splitlines()
        evs = [json.loads(x) for x in lin if x.startswith("{")]
        rc = next(x for x in lin if x.startswith("rc="))
        cnt = Counter(e["evento"] for e in evs)
        ct = [e["resultado"] for e in evs if e["evento"] == "control_entre_tramos"]
        fm = [e.get("resultado") for e in evs if e["evento"] == "freno_modelo_antes"] + [e["freno_modelo"] for e in evs if e["evento"] == "to_fin"]
        par = [e["motivo"] for e in evs if e["evento"] == "parada"]
        filas.append([log, rc, cnt.get("to_inicio", 0), ", ".join(fm), ", ".join(ct) or "—", "; ".join(par) or "—"])
    out["pruebas_t2"] = filas
    tabla("10. Las pruebas del lanzador sobre la copia", ["prueba", "salida", "TOs lanzados", "freno por modelo (antes y después de cada TO)",
                                                          "control entre tramos", "parada"], filas)

    # 11. las estimaciones de T2
    es = leer(f"{T1}/estimaciones/estimaciones_t2_t1.json")
    out["estimaciones"] = es
    d, co = es["duracion"], es["costo"]
    tabla("11. La duración y el costo estimados de T2", ["cifra", "valor"],
          [["tanda 1: lanzamientos (min)", d["tanda_1_lanzamientos_min"]], ["tanda 1: total (min)", d["tanda_1_total_min"]],
           ["segundos por unidad", d["segundos_por_unidad"]],
           ["tanda final por unidades (min, h)", f"{d['por_unidades']['min']}, {d['por_unidades']['horas']}"],
           ["tramo 1 y tramo 2 por unidades (min)", f"{d['por_unidades']['tramo_1']['min']} y {d['por_unidades']['tramo_2']['min']}"],
           ["tanda final por caracteres (min, h; información)", f"{d['por_caracteres_informacion']['min']}, {d['por_caracteres_informacion']['horas']}"],
           ["tramo 1 y tramo 2 por caracteres (min)", f"{d['por_caracteres_informacion']['tramo_1']['min']} y {d['por_caracteres_informacion']['tramo_2']['min']}"],
           ["freno por modelo (corridas, s, min)", f"{d['freno_por_modelo']['corridas']}, {d['freno_por_modelo']['segundos_por_corrida_medidos']}, {d['freno_por_modelo']['min']}"],
           ["estimado (USD)", co["estimado_a_4_decimales"]], ["con la razón de la tanda 1", f"{co['estimado_con_la_razon_de_la_tanda_1_usd']} ({co['razon_tanda1']})"],
           ["tope, margen, tope sobre estimado", f"{co['tope_usd']}, {co['margen_sobre_el_estimado_usd']}, {co['tope_sobre_estimado']}"]])

    # 12. las comprobaciones de reproducción
    cp = leer(f"{T1}/comprobaciones_t1.json")
    out["comprobaciones"] = {"todo_igual": cp["todo_igual"], "runner": {k: cp["4_corrida_en_seco"][k] for k in
                             ("runner_archivos", "runner_difieren", "runner_difieren_por_clase")}}
    tabla("12. Las comprobaciones de reproducción (comprobaciones_t1.py)", ["comprobación", "resultado"],
          [["la E0 del repo contra la corrida 1", f"{cp['1_e0_repo_contra_corrida_1']['repo']} archivos, iguales: {cp['1_e0_repo_contra_corrida_1']['iguales']}"],
           ["el manifiesto del repo contra el primer armado", cp["2_manifiesto_repo_contra_primer_armado"]["iguales"]],
           ["la derivada regenerada (md, huecos)", f"{cp['3_derivada_regenerada']['md']['iguales']}, {cp['3_derivada_regenerada']['huecos']['iguales']}"],
           ["corrida en seco: mis salidas 1 = 2, y 3 igual salvo la clave nueva", f"{cp['4_corrida_en_seco']['mis_salidas_1_y_2_iguales']}, {cp['4_corrida_en_seco']['mis_salidas_3_igual_salvo_corrida_en_seco_t1']} ({cp['4_corrida_en_seco']['corrida_en_seco_t1_3_contra_2']['claves_nuevas']})"],
           ["corrida en seco: consola y resumen iguales en las tres", cp["4_corrida_en_seco"]["consola_y_resumen_iguales_en_las_tres"]],
           ["corrida en seco: archivos del runner, los que difieren y por qué", f"{cp['4_corrida_en_seco']['runner_archivos']}; {cp['4_corrida_en_seco']['runner_difieren']}: {cp['4_corrida_en_seco']['runner_difieren_por_clase']}"],
           ["ensamblado del tramo 1 en dos procesos", {k: v["iguales"] for k, v in cp["5_ensamblado_tramo1_dos_procesos"].items()}],
           ["bases de la caché del repo antes y después de las pruebas del freno", {Path(k).name: v["iguales"] for k, v in cp["6_bases_de_la_cache_del_repo"].items()}],
           ["todo igual", cp["todo_igual"]]])

    # 13. sha256 para T2
    lineas = (r / f"{T1}/sha256_para_T2.txt").read_text(encoding="utf-8").splitlines()
    out["sha256_para_T2"] = {"sha256": sha(f"{T1}/sha256_para_T2.txt"), "renglones": len(lineas)}
    md.append(f"\n### 13. sha256_para_T2.txt\n\n{len(lineas)} renglones, sha256 `{out['sha256_para_T2']['sha256']}`.")

    a.md.write_text("# Cifras del FRENO T1 de la tanda final (las genera freno_t1_cifras.py)\n" + "\n".join(md) + "\n",
                    encoding="utf-8")
    a.json.write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
    print(f"{a.md.name}: {len(md)} renglones; {a.json.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
