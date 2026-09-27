#!/usr/bin/env python3
"""sonda_anclas_C1_C7_UB21.py — U-B2.1 fase 1 (re-diagnóstico), pieza e.

Sondea, sobre los cuatro grafos de la decisión 4 del mandato, las ANCLAS de
las siete correcciones C1–C7 del backlog (BKL-0017, 0006, 0023, 0019, 0004,
0003, 0005): para cada corrección, si el objeto que el retest verificó está
presente en el grafo, direccionado SIN id de nodo — por (archivo del TO,
punto ∈ conjunto de provenances, tipo, cadena normalizada en label o
properties) — y, en paralelo, si el id que el retest registró existe (para
medir la fragilidad del direccionamiento por id entre generaciones).

Adaptador de provenance (solo diagnóstico, no es código de la suite):
  gen 1/2: {source_doc, location} -> punto extraído de "Punto N.N." en location
           (se leen `provenances` si existe, si no `provenance` y
           `additional_provenance`);
  gen 3:   {to, archivo, punto, ...} -> (archivo, punto) directo.
Siempre sobre el CONJUNTO de provenances, nunca provenance[0] solo.

También sondea, fuera del inventario, las anclas de BKL-0024 (ext 3.9, tope
USD 200) y BKL-0025 (pro 1.1.1, definición de usuario), que el plan nombra
«cerrados» y el backlog tiene `triaged`.

Solo lectura; imprime por stdout. Corre desde la raíz del repo:
    PYTHONDONTWRITEBYTECODE=1 python3 reports/revision_UB21_diag/sonda_anclas_C1_C7_UB21.py
"""
import sys
sys.dont_write_bytecode = True

import hashlib
import json
import re
import unicodedata
from collections import Counter, OrderedDict
from pathlib import Path

GRAFOS = [
    ("KG-Base", "data/experiment/run_3_ppf_core/kg.json",
     "12c226e22b8fdc8f46999cae7f1eb808930e71f5dfe803f3a4f637a88348c410"),
    ("KG-Refinado", "data/experiment/grafo_v2/reensamblado_v3/kg.json",
     "26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571"),
    ("KG-Reextraido", "data/experiment/reextraccion_v2/corpus_v2/salida/kg.json",
     "8e2eadee57b48e00ccb51ade9a953ba1469001fe089c45d97c4307ccf2725581"),
    ("KG-Reextraido-r1", "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json",
     "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"),
]
CLA, CAP, PRO, RIC, EXT = ("TO_clasificacion", "TO_capitales", "TO_proteccion",
                           "TO_regimen_informativo", "TO_exterior")
RE_PUNTO = re.compile(r"punto\s+(\d+(?:\.\d+)*)")
RE_MONTO = re.compile(r"(?<![\d.])(5\.000|2\.500)(?![\d.])")


# ----------------------------- normalización ----------------------------- #
def norm(s) -> str:
    s = unicodedata.normalize("NFD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("“", '"').replace("”", '"').replace("’", "'")
    return re.sub(r"\s+", " ", s.lower()).strip()


def _vals(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from _vals(v)
    elif isinstance(o, list):
        for v in o:
            yield from _vals(v)
    else:
        yield str(o)


def texto(n: dict) -> str:
    return norm(" | ".join([n.get("label") or ""] + list(_vals(n.get("properties") or {}))))


def prop(n: dict, k: str):
    return (n.get("properties") or {}).get(k)


def provs(o: dict) -> list:
    ps = list(o.get("provenances") or [])
    if not ps and isinstance(o.get("provenance"), dict):
        ps = [o["provenance"]]
    extra = o.get("additional_provenance")
    if isinstance(extra, list):
        ps += [p for p in extra if isinstance(p, dict)]
    return ps


def anclas(o: dict) -> set:
    """Conjunto de (archivo, punto) sobre TODAS las provenances del objeto."""
    out = set()
    for p in provs(o):
        if "punto" in p:                                   # gen 3
            out.add((p.get("archivo") or "", str(p.get("punto") or "")))
        else:                                              # gen 1/2
            for pt in RE_PUNTO.findall(norm(p.get("location"))):
                out.add((p.get("source_doc") or "", pt))
    return out


def con_ancla(o: dict, archivo_pref: str, punto: str = None, prefijo_punto: bool = False) -> bool:
    for a, p in anclas(o):
        if not a.startswith(archivo_pref):
            continue
        if punto is None or p == punto or (prefijo_punto and p.startswith(punto + ".")):
            return True
    return False


def buscar(N, tipo=None, archivo=None, punto=None, contiene=(), no_contiene=(), prefijo_punto=False):
    out = []
    for n in N:
        if tipo and n.get("type") != tipo:
            continue
        if archivo and not con_ancla(n, archivo, punto, prefijo_punto):
            continue
        t = texto(n)
        if any(norm(c) not in t for c in contiene):
            continue
        if any(norm(c) in t for c in no_contiene):
            continue
        out.append(n)
    return out


def ids(ns, k=3):
    return [n["id"][:72] for n in ns[:k]]


# ------------------------------- checks ---------------------------------- #
def sondear(kg: dict) -> "OrderedDict[str, dict]":
    N, E = kg["nodes"], kg["edges"]
    by_id = {n["id"]: n for n in N}
    out_e, in_e = {}, {}
    for e in E:
        out_e.setdefault(e["source"], []).append(e)
        in_e.setdefault(e["target"], []).append(e)
    R = OrderedDict()

    def reg(k, estado, detalle):
        R[k] = {"estado": estado, "detalle": detalle}

    def rel_salientes(n):
        return Counter((e["relation"], (by_id.get(e["target"]) or {}).get("type")) for e in out_e.get(n["id"], []))

    # ---- C1 (BKL-0017): criterio general 1.1 de Clasificación ----
    c1 = buscar(N, "Obligacion", CLA, "1.1", contiene=["los clientes de la entidad (tanto residentes en el pais"])
    reg("C1.nodo_criterio_1_1", "PASS" if c1 else "FAIL", f"n={len(c1)} {ids(c1)}")
    reg("C1.id_e1946e", "PASS" if "Obligacion_los_clientes_de_la_entidad_tanto_residentes_en_el_pais_de_los_sectores_publico_y_e1946e" in by_id else "FAIL", "")
    if c1:
        rs = rel_salientes(c1[0])
        ok = any(r == "establecida_en" and t == "TextoOrdenado" for r, t in rs) and \
             any(r == "aplica_a" and t in ("Sujeto", "EntidadFinanciera") for r, t in rs)
        reg("C1.aristas_establecida_en+aplica_a", "PASS" if ok else "FAIL", f"salientes={dict(rs)}")
    else:
        reg("C1.aristas_establecida_en+aplica_a", "N/A", "sin nodo")

    # ---- C2 (BKL-0006): montos del 1.2 de CapMin ----
    tabla = buscar(N, None, CAP, "1.2", contiene=["exigencia basica"])
    filas, bancos_ok, restantes_ok, invertido = [], False, False, False
    for n in tabla:
        t = texto(n)
        clase = "restantes" if "restantes entidades" in t else ("bancos" if "bancos" in t else "otro")
        montos = sorted(set(RE_MONTO.findall(t)))
        umbral = prop(n, "umbral") or prop(n, "monto")
        filas.append(f"{n['type']}:{n['id'][:60]} clase={clase} montos={montos} umbral={umbral!r}")
        if clase == "bancos" and n["type"] != "Excepcion":
            bancos_ok |= ("5.000" in montos and "2.500" not in montos)
            invertido |= ("2.500" in montos)
        if clase == "restantes" and n["type"] != "Excepcion":
            restantes_ok |= ("2.500" in montos and "5.000" not in montos)
            invertido |= ("5.000" in montos)
    est = "PASS" if (bancos_ok and restantes_ok and not invertido) else ("FAIL(invertido)" if invertido else "FAIL")
    reg("C2.tabla_1_2_bancos_5000_restantes_2500", est, f"n={len(tabla)}; " + " || ".join(filas))
    exc = buscar(N, "Excepcion", CAP, "1.2", contiene=["cajas de credito cooperativas"])
    if exc:
        tg = [(e["relation"], texto(by_id[e["target"]])[:50]) for e in out_e.get(exc[0]["id"], [])
              if e["relation"].startswith("exceptua") and e["target"] in by_id]
        ok = any("restantes" in t for _, t in tg)
        reg("C2.excepcion_cajas_apunta_a_restantes", "PASS" if ok else "FAIL", f"n_exc={len(exc)} targets={tg}")
    else:
        reg("C2.excepcion_cajas_apunta_a_restantes", "N/A", "sin Excepcion de cajas en cap 1.2")
    viejos = ["Restriccion_bancos_salvo_cajas_de_credito_cooperativas_deberan_observar_exigencia_basica_de__2d3063",
              "Restriccion_restantes_entidades_deberan_observar_exigencia_basica_de_5_000_millones_de_pesos_50658f",
              "Excepcion_cajas_de_credito_cooperativas_estan_exceptuadas_de_la_exigencia_basica_de_bancos_c19412"]
    nuevos = ["Restriccion_bancos_deberan_observar_exigencia_basica_de_5_000_millones_de_pesos_380229",
              "Restriccion_restantes_entidades_salvo_cajas_de_credito_cooperativas_deberan_observar_exigenc_7b4b77",
              "Excepcion_cajas_de_credito_cooperativas_estan_exceptuadas_de_la_exigencia_basica_de_restan_53466d"]
    reg("C2.ids_nuevos_presentes/viejos_ausentes",
        "PASS" if all(i in by_id for i in nuevos) and not any(i in by_id for i in viejos) else "FAIL",
        f"nuevos={[i in by_id for i in nuevos]} viejos={[i in by_id for i in viejos]}")

    # ---- C3 (BKL-0023): umbral de compañías financieras ----
    c3 = buscar(N, "Restriccion", CAP, "1.2", contiene=["companias financieras que realicen, en forma directa, operaciones de comercio exterior"])
    if c3:
        u = [prop(n, "umbral") for n in c3]
        if all(x is None for x in u):
            reg("C3.umbral_companias_5000", "N/A(sin umbral)", f"n={len(c3)} {ids(c3)} umbral={u}")
        else:
            reg("C3.umbral_companias_5000", "PASS" if any(norm(x) == "5.000 millones de pesos" for x in u if x) else "FAIL",
                f"n={len(c3)} umbral={u}")
    else:
        reg("C3.umbral_companias_5000", "N/A(sin nodo)", "ningun Restriccion en cap 1.2 con la oracion")
    reg("C3.id_7bb7bb", "PASS" if "Restriccion_las_companias_financieras_que_realicen_en_forma_directa_operaciones_de_comercio__7bb7bb" in by_id else "FAIL", "")

    # ---- C4 (BKL-0019): 8 aristas de jerarquia de cuarentena ----
    # (id del sujeto en KG-Refinado, label en cuarentena.json, padre laudado) — C4_retest_2026-08-02.md:33-42
    c4 = [("Sujeto_propuesto_inversor", "Inversor", "Sujeto_contraparte"),
          ("Sujeto_propuesto_entidades_financieras_del_grupo_1", "Entidades financieras del grupo 1", "Sujeto_entidad_financiera"),
          ("Sujeto_propuesto_beneficiarios_de_radpip_y_o_radpign", "Beneficiarios de RADPIP y/o RADPIGN", "Sujeto_contraparte"),
          ("Sujeto_propuesto_entidades_del_grupo_a", "Entidades del Grupo A", "Sujeto_entidad_financiera"),
          ("Sujeto_propuesto_entidades_financieras_del_grupo_2", "Entidades financieras del grupo 2", "Sujeto_entidad_financiera"),
          ("Sujeto_propuesto_inversores_y_tenedores_de_titulizacion", "Inversores y tenedores de titulización", "Sujeto_contraparte"),
          ("Sujeto_propuesto_originante_fiduciario", "Originante/fiduciario", "Sujeto_fiduciario_de_fideicomiso_financiero"),
          ("Sujeto_propuesto_personas_juridicas_beneficiarias_del_regimen_de_economia_del_conocimiento",
           "Personas jurídicas beneficiarias del régimen de economía del conocimiento", "Sujeto_beneficiario_economia_conocimiento")]
    sujetos_por_label = {norm(n.get("label")): n["id"] for n in N if n.get("type") == "Sujeto"}
    n_src = n_tgt = n_sub = n_ps = n_prop = 0
    filas = []
    for s, lab, t in c4:
        src = s if s in by_id else sujetos_por_label.get(norm(lab))
        sp, tp = src is not None, t in by_id
        sub = sp and any(e["relation"] == "subclase_de" and e["target"] == t for e in out_e.get(src, []))
        ps = sp and any(e["relation"] == "padre_sugerido" and e["target"] == t for e in out_e.get(src, []))
        pr = sp and prop(by_id[src], "padre_sugerido") == t
        n_src += sp; n_tgt += tp; n_sub += sub; n_ps += ps; n_prop += pr
        filas.append(f"{lab[:28]}->{t[7:30]} src={'si' if sp else 'NO'} tgt={'si' if tp else 'NO'} subclase_de={'si' if sub else 'no'} padre_sugerido_arista={'si' if ps else 'no'} prop={'si' if pr else 'no'}")
    reg("C4.8_subclase_de_laudadas", "PASS" if n_sub == 8 else "FAIL", f"subclase_de={n_sub}/8 src_presentes={n_src}/8 tgt_presentes={n_tgt}/8")
    reg("C4.8_padre_sugerido_flaggeadas(gen3)", "PASS" if n_ps == 8 else "FAIL", f"aristas_padre_sugerido={n_ps}/8 prop_padre_sugerido={n_prop}/8")
    for f in filas:
        R.setdefault("C4.detalle", {"estado": "info", "detalle": ""})["detalle"] += f + " || "
    exclu = "Sujeto_propuesto_originante_acreedor_inicial"
    if exclu in by_id:
        tiene = any(e["relation"] == "subclase_de" for e in out_e.get(exclu, []))
        reg("C4.excluida_sin_subclase_de", "PASS" if not tiene else "FAIL", f"nodo presente; subclase_de saliente={tiene}")
    else:
        reg("C4.excluida_sin_subclase_de", "N/A", "nodo ausente")

    # ---- C5 (BKL-0004): enumeración del 6.5 ----
    c5 = [("N1", "6.5", "cada cliente, y la totalidad de sus financiaciones comprendidas"),
          ("N2", "6.5.1", "situacion normal"), ("N3", "6.5.2", "seguimiento especial"),
          ("N4", "6.5.2.1", "en observacion"), ("N5", "6.5.2.2", "en negociacion o con acuerdos de refinanciacion"),
          ("N6", "6.5.2.3", "tratamiento especial"), ("N7", "6.5.3", "con problemas"),
          ("N8", "6.5.4", "alto riesgo de insolvencia"), ("N9", "6.5.5", "irrecuperable")]
    hall = {}
    filas = []
    for k, pt, frase in c5:
        ns = buscar(N, None, CLA, pt, contiene=[frase])
        hall[k] = ns
        filas.append(f"{k}@{pt}:{len(ns)}{'(' + ','.join(sorted({n['type'] for n in ns})) + ')' if ns else ''}")
    n_ok = sum(1 for k in hall if hall[k])
    reg("C5.9_nodos_6_5_por_ancla+frase", "PASS" if n_ok == 9 else "FAIL", f"{n_ok}/9 -> " + " ".join(filas))
    ids_c5 = ["Obligacion_cada_cliente_y_la_totalidad_de_sus_financiaciones_comprendidas_se_incluira_en_un_772a57",
              "Operacion_clasificacion_de_deudor_de_la_cartera_comercial_en_situacion_normal_6_5_1_1a22ee",
              "Operacion_clasificacion_de_deudor_de_la_cartera_comercial_con_seguimiento_especial_6_5_2_s_1d1a4b",
              "Operacion_seguimiento_especial_situacion_en_observacion_6_5_2_1_cartera_comercial_9ef6cc",
              "Operacion_seguimiento_especial_situacion_en_negociacion_o_con_acuerdos_de_refinanciacion_6_838263",
              "Operacion_seguimiento_especial_situacion_en_tratamiento_especial_6_5_2_3_cartera_comercial_8569f5",
              "Operacion_clasificacion_de_deudor_de_la_cartera_comercial_con_problemas_6_5_3_1e9da8",
              "Operacion_clasificacion_de_deudor_de_la_cartera_comercial_con_alto_riesgo_de_insolvencia_6_495c77",
              "Operacion_clasificacion_de_deudor_de_la_cartera_comercial_irrecuperable_6_5_5_36b64c"]
    reg("C5.9_ids_presentes", "PASS" if all(i in by_id for i in ids_c5) else "FAIL", f"{sum(1 for i in ids_c5 if i in by_id)}/9")
    if hall["N1"]:
        n1 = hall["N1"][0]
        hijos = {n["id"] for k in ("N2", "N3", "N4", "N5", "N6", "N7", "N8", "N9") for n in hall[k]}
        regula = sum(1 for e in out_e.get(n1["id"], []) if e["relation"] == "regula" and e["target"] in hijos)
        est_en = sum(1 for k in hall for n in hall[k][:1]
                     if any(e["relation"] == "establecida_en" and (by_id.get(e["target"]) or {}).get("type") == "TextoOrdenado"
                            for e in out_e.get(n["id"], [])))
        reg("C5.aristas_8_regula+9_establecida_en", "PASS" if regula == 8 and est_en == 9 else "FAIL", f"regula_N1->hijos={regula}/8 establecida_en={est_en}/9")
        niveles_72 = ("riesgo medio", "riesgo bajo", "riesgo alto")
        reg("C5.N1_sin_niveles_del_7_2(RT-C5-5)", "PASS" if not any(x in texto(n1) for x in niveles_72) else "FAIL", "")
    else:
        reg("C5.aristas_8_regula+9_establecida_en", "N/A", "sin N1")
        reg("C5.N1_sin_niveles_del_7_2(RT-C5-5)", "N/A", "sin N1")
    n72 = buscar(N, None, CLA, "7.2")
    rm = buscar(N, None, CLA, "7.2", contiene=["riesgo medio"])
    reg("C5.7_2_riesgo_medio_anclado(RT-C5-5)", "PASS" if rm else "FAIL", f"nodos_en_7_2={len(n72)} con_riesgo_medio={len(rm)}")

    # ---- C6 (BKL-0003): salvedad mutuales/cooperativas 1.1.2.5 ----
    c6 = buscar(N, "Excepcion", PRO, "1.1.2.5", contiene=["mutuales o cooperativas"])
    cualq = buscar(N, None, PRO, "1.1.2.5", contiene=["mutual"])
    reg("C6.excepcion_1_1_2_5_mutuales", "PASS" if c6 else "FAIL", f"Excepcion={len(c6)} {ids(c6)}; cualquier_tipo_con_mutual={len(cualq)} tipos={sorted({n['type'] for n in cualq})}")
    reg("C6.id_5f95b9(cualquier_tipo)", "PASS" if any(i.endswith("_5f95b9") for i in by_id) else "FAIL",
        f"{[i[:50] for i in by_id if i.endswith('_5f95b9')]}")
    if c6:
        rs = rel_salientes(c6[0])
        ok = any(r == "establecida_en" and t == "TextoOrdenado" for r, t in rs) and any(r == "exceptua_obligacion" and t == "Obligacion" for r, t in rs)
        reg("C6.aristas_establecida_en+exceptua_obligacion", "PASS" if ok else "FAIL", f"salientes={dict(rs)}")
        a_suj = sum(1 for e in out_e.get(c6[0]["id"], []) + in_e.get(c6[0]["id"], [])
                    if (by_id.get(e["target"]) or {}).get("type") == "Sujeto" or (by_id.get(e["source"]) or {}).get("type") == "Sujeto")
        reg("C6.N1_sin_aristas_a_Sujeto(RT-C6-4)", "PASS" if a_suj == 0 else "FAIL", f"aristas_con_Sujeto={a_suj}")
    else:
        reg("C6.aristas_establecida_en+exceptua_obligacion", "N/A", "sin nodo")
        reg("C6.N1_sin_aristas_a_Sujeto(RT-C6-4)", "N/A", "sin nodo")
    rol = "Sujeto_rol_sujeto_obligado_proteccion"
    if rol in by_id:
        mde = [e["source"] for e in in_e.get(rol, []) if e["relation"] == "miembro_de"]
        reg("C6.rol_proteccion_7_miembro_de(RT-C6-3)", "PASS" if len(mde) == 7 else "FAIL", f"miembro_de_entrantes={len(mde)}")
        reg("C6.emisoras_tarjetas_miembro_de_rol(RT-C6-4)", "PASS" if "Sujeto_empresa_no_financiera_emisora_de_tarjetas" in mde else "FAIL", "")
    else:
        reg("C6.rol_proteccion_7_miembro_de(RT-C6-3)", "N/A", "rol ausente")
        reg("C6.emisoras_tarjetas_miembro_de_rol(RT-C6-4)", "N/A", "rol ausente")

    # ---- C7 (BKL-0005): calificadores del 7.1 de RegInf ----
    port = buscar(N, "Obligacion", RIC, "7.1", contiene=["para el calculo del importe correspondiente al mes n"])
    q1, q2 = "responsabilidad patrimonial computable informada en el mes n", "franquicia informada en el mes n calculada segun datos del mes n"
    con = [n for n in port if q1 in texto(n) and q2 in texto(n)]
    parc = [n for n in port if (q1 in texto(n)) != (q2 in texto(n))]
    reg("C7.calificadores_7_1_RPC+franquicia", "PASS" if con else ("N/A(sin portador)" if not port else "FAIL"),
        f"portadores={len(port)} con_ambos={len(con)} con_uno_solo={len(parc)} {ids(port)}")
    reg("C7.id_425c6b", "PASS" if "Obligacion_para_el_calculo_del_importe_correspondiente_al_mes_n_procedera_tenerse_en_cuenta_425c6b" in by_id else "FAIL", "")

    # ---- Fuera del inventario: BKL-0024 / BKL-0025 (triaged) ----
    e39 = buscar(N, None, EXT, "3.9", prefijo_punto=True)
    e39_200 = [n for n in e39 if "200" in texto(n)]
    reg("X.BKL-0024_ext_3_9_usd200", "PASS" if e39_200 else "FAIL", f"anclados_3_9*={len(e39)} con_200={len(e39_200)} {ids(e39_200)}")
    p111 = buscar(N, None, PRO, "1.1.1")
    p111_u = [n for n in p111 if "usuario" in texto(n)]
    reg("X.BKL-0025_pro_1_1_1_usuario", "PASS" if p111_u else "FAIL", f"anclados_1_1_1={len(p111)} con_usuario={len(p111_u)} {ids(p111_u)}")
    return R


def main() -> int:
    print("sonda_anclas_C1_C7_UB21 — anclas de C1–C7 (+ BKL-0024/0025) sobre los cuatro grafos, direccionadas sin id")
    todo = OrderedDict()
    for nombre, ruta, sha_esp in GRAFOS:
        sha = hashlib.sha256(Path(ruta).read_bytes()).hexdigest()
        print()
        print(f"===== {nombre}  {ruta}")
        print(f"sha256 {sha}  -> {'OK' if sha == sha_esp else 'DIFIERE de ' + sha_esp}")
        if sha != sha_esp:
            print("  FRENO: sha distinto del declarado en el mandato; no se corre.")
            return 1
        kg = json.loads(Path(ruta).read_text(encoding="utf-8"))
        gen = "gen3" if any("punto" in p for p in provs(kg["nodes"][0])) else "gen1/2"
        print(f"formato de provenance detectado: {gen}; nodos={len(kg['nodes'])} aristas={len(kg['edges'])}")
        R = sondear(kg)
        todo[nombre] = R
        for k, v in R.items():
            print(f"  {k:46s} {v['estado']:16s} {v['detalle'][:1400]}")
    print()
    print("===== Matriz estado por grafo")
    claves = [k for k in todo[GRAFOS[0][0]] if k != "C4.detalle"]
    print("check".ljust(46) + "".join(n.ljust(18) for n, _, _ in GRAFOS))
    for k in claves:
        print(k.ljust(46) + "".join(todo[n][k]["estado"].ljust(18) for n, _, _ in GRAFOS))
    canon = json.dumps(todo, ensure_ascii=False, sort_keys=True)
    print()
    print(f"sha256 del JSON canonico de resultados (determinismo): {hashlib.sha256(canon.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
