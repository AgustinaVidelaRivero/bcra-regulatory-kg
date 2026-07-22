# Verificaciones de la adjudicación del piloto — barridos determinísticos

Fecha: 2026-07-16. SOLO LECTURA; única escritura: este archivo (zona gitignored). No se
corrió el verificador ni la capa. Sin commits. **Solo hechos** — cero adjudicación.

**Mecanismo:** outputs completos por re-ejecución determinística (mismo mecanismo de
`test_alcanzabilidad.outputs_completos_de_trace`, conservando el número de paso) sobre las
trazas post-hoc `posthoc_run/traces/off/run_3/`; barridos sobre el kg de run_3 (4.050 nodos)
con texto normalizado (lowercase, sin acentos) sobre id+label+properties — sin provenances,
salvo el punto 3b que las reporta por separado —; D1 (`evaluar_alcanzabilidad`) sobre
candidatos no expuestos, con pregunta + consultas del agente + tokens expuestos de la traza
del caso. Los fragmentos de exposición se muestran sobre el texto normalizado.

**Reglas mecánicas de alcance (declaradas, para volumen):** en 2b se pegan íntegros los
candidatos del ancla "situacion normal" (más los que matchean 'puntual' Y '31'); 'puntual' y
'31' se reportan con conteo + lista completa de ids. En 3b se pegan íntegros los candidatos
de términos específicos ('30/06','30-06','junio','transitoria','12.3'); 'vigente'/'vigencia'
con conteo + ids.

## Código (comando completo)

```python
# -*- coding: utf-8 -*-
"""Verificaciones de la adjudicación del piloto — barridos determinísticos. Solo hechos."""
import json, sys, unicodedata, re
from pathlib import Path

EVAL = Path("/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/evaluacion")
sys.path.insert(0, str(EVAL))
import loader, harness
from harness import _tokens
from test_alcanzabilidad import evaluar_alcanzabilidad, tokens_expuestos_de_trace

def norm(s):
    s = unicodedata.normalize("NFD", str(s))
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()

kg = loader.load_graph("run_3")
idx = harness.GraphIndex(kg)
by_id = idx.by_id

def outputs_con_paso(qid):
    """(n, blob_json) por paso re-ejecutable — mismo mecanismo que outputs_completos_de_trace,
    conservando el número de paso."""
    tr = json.load(open(EVAL / f"posthoc_run/traces/off/run_3/{qid}.json"))[0]["trace"]
    out = []
    for s in tr["steps"]:
        tool, inp = s.get("tool"), s.get("input") or {}
        if tool == "buscar_nodos":
            o = idx.buscar_nodos(inp.get("consulta", ""), inp.get("limite", 10))
        elif tool == "ver_nodo":
            o = idx.ver_nodo(inp.get("id", ""))
        elif tool == "ver_vecinos":
            o = idx.ver_vecinos(inp.get("id", ""), inp.get("direccion", "ambas"))
        else:
            continue
        out.append((s["n"], json.dumps(o, ensure_ascii=False)))
    return tr, out

def exposicion(outs, termino, ancho=110, max_frag=3):
    """Matches del término normalizado en los outputs normalizados: [(paso, [fragmentos])]."""
    t = norm(termino)
    hits = []
    for n, blob in outs:
        nb = norm(blob)
        idxs = [m.start() for m in re.finditer(re.escape(t), nb)]
        if idxs:
            frags = []
            for i in idxs[:max_frag]:
                a, b = max(0, i - ancho // 2), min(len(nb), i + len(t) + ancho // 2)
                frags.append("…" + nb[a:b] + "…")
            hits.append((n, len(idxs), frags))
    return hits

def blob_nodo(n):
    props = n.properties or {}
    return norm(f"{n.id} {n.label} " + " ".join(f"{k} {v}" for k, v in props.items()))

def blob_prov(n):
    return norm(json.dumps(n.provenances, ensure_ascii=False))

def dump(nid):
    n = by_id[nid]
    return json.dumps({"id": n.id, "type": n.type, "label": n.label,
                       "properties": n.properties, "provenances": n.provenances},
                      ensure_ascii=False, indent=1)

def d1_reducido(nid, qid, outs_ids_expuestos):
    tr = json.load(open(EVAL / f"posthoc_run/traces/off/run_3/{qid}.json"))[0]["trace"]
    pregunta = tr["question"]
    consultas = [s["input"]["consulta"] for s in tr["steps"] if s.get("tool") == "buscar_nodos"]
    toks = tokens_expuestos_de_trace(EVAL / f"posthoc_run/traces/off/run_3/{qid}.json", index=idx)
    d1 = evaluar_alcanzabilidad(nid, pregunta, consultas, toks, idx)
    ranks = [c["rank"] for c in d1["consultas"] if c["rank"] is not None]
    return {"portador": nid, "alcanzable": d1["alcanzable"],
            "mejor_rank": min(ranks) if ranks else None,
            "n_consultas_simuladas": d1["n_consultas_simuladas"],
            "consultas_en_top10": [{"consulta": c["consulta"], "rank": c["rank"], "origen": c["origen"]}
                                    for c in d1["consultas"] if c["en_top10"]]}

def expuesto_id(nid, outs):
    return [n for n, blob in outs if nid in blob]

SEP = "=" * 78

# ============ 1. CQ-018 ============
print(f"{SEP}\n1. CQ-018\n{SEP}")
tr18, outs18 = outputs_con_paso("CQ-018")
print(f"(pasos re-ejecutables: {len(outs18)})")
for rotulo, terms in (("1a 'énfasis'/'flujos de fondos'", ["enfasis", "flujos de fondos", "flujo de fondos"]),
                      ("1b 'atender adecuadamente'/'todos sus compromisos'", ["atender adecuadamente", "todos sus compromisos"])):
    print(f"\n[{rotulo}] exposición en outputs completos:")
    for t in terms:
        hits = exposicion(outs18, t)
        if hits:
            for n, cnt, frags in hits:
                print(f"  '{t}': paso {n} ({cnt} match/es)")
                for f in frags:
                    print(f"     {f}")
        else:
            print(f"  '{t}': AUSENTE en todos los outputs completos")

# 1c barridos kg para lo no expuesto
print("\n[1c] barrido kg de portadores:")
for t in ("enfasis", "flujos de fondos", "flujo de fondos", "atender adecuadamente", "todos sus compromisos"):
    cands = [n.id for n in kg.nodes if norm(t) in blob_nodo(n)]
    print(f"\n  término '{t}': {len(cands)} candidato/s en id/label/properties")
    for nid in cands:
        exp = expuesto_id(nid, outs18)
        print(f"  --- {nid} | expuesto en outputs de CQ-018: {('pasos ' + str(exp)) if exp else 'NO'} ---")
        print(dump(nid))
        if not exp:
            print("  D1 (reducido):", json.dumps(d1_reducido(nid, "CQ-018", outs18), ensure_ascii=False, indent=1))

# ============ 2. CQ-019 ============
print(f"\n{SEP}\n2. CQ-019\n{SEP}")
tr19, outs19 = outputs_con_paso("CQ-019")
print(f"(pasos re-ejecutables: {len(outs19)})")
print("\n[2a] exposición en outputs completos:")
for t in ("31 dias", "puntual", "situacion normal"):
    hits = exposicion(outs19, t)
    if hits:
        for n, cnt, frags in hits:
            print(f"  '{t}': paso {n} ({cnt} match/es)")
            for f in frags:
                print(f"     {f}")
    else:
        print(f"  '{t}': AUSENTE en todos los outputs completos")

print("\n[2b] barrido kg — regla mecánica de alcance: se pegan ÍNTEGROS los candidatos que")
print("matchean 'situacion normal' (ancla de la definición); para 'puntual' y '31' se reporta")
print("conteo + ids, e íntegro solo si el nodo matchea además otro de los términos.")
c_sn = [n.id for n in kg.nodes if "situacion normal" in blob_nodo(n)]
c_pu = [n.id for n in kg.nodes if "puntual" in blob_nodo(n)]
c_31 = [n.id for n in kg.nodes if re.search(r"(?<!\d)31(?!\d)", blob_nodo(n))]
print(f"\n  'situacion normal': {len(c_sn)} candidatos: {c_sn}")
print(f"  'puntual': {len(c_pu)} candidatos: {c_pu}")
print(f"  '31' (número suelto): {len(c_31)} candidatos: {c_31}")
integros = sorted(set(c_sn) | (set(c_pu) & set(c_31)))
for nid in integros:
    exp = expuesto_id(nid, outs19)
    print(f"\n  --- {nid} | expuesto en outputs de CQ-019: {('pasos ' + str(exp)) if exp else 'NO'} ---")
    print(dump(nid))
    if not exp:
        print("  D1 (reducido):", json.dumps(d1_reducido(nid, "CQ-019", outs19), ensure_ascii=False, indent=1))

# ============ 3. CQ-033 ============
print(f"\n{SEP}\n3. CQ-033\n{SEP}")
tr33, outs33 = outputs_con_paso("CQ-033")
print(f"(pasos re-ejecutables: {len(outs33)})")
print("\n[3a] exposición en outputs completos:")
TERMS33 = ["30/06", "30-06", "junio", "vigente", "vigencia", "transitoria", "12.3"]
for t in TERMS33:
    hits = exposicion(outs33, t)
    if hits:
        for n, cnt, frags in hits:
            print(f"  '{t}': paso {n} ({cnt} match/es)")
            for f in frags:
                print(f"     {f}")
    else:
        print(f"  '{t}': AUSENTE en todos los outputs completos")

print("\n[3b] barrido kg (properties Y provenances por separado) — regla mecánica de alcance:")
print("íntegros los candidatos de términos específicos ('30/06','30-06','junio','transitoria','12.3');")
print("para 'vigente'/'vigencia' conteo + ids, íntegro solo si matchea además un término específico.")
espec = ["30/06", "30-06", "junio", "transitoria", "12.3"]
amplios = ["vigente", "vigencia"]
cand_espec = {}
for t in espec:
    en_p = [n.id for n in kg.nodes if norm(t) in blob_nodo(n)]
    en_v = [n.id for n in kg.nodes if norm(t) not in blob_nodo(n) and norm(t) in blob_prov(n)]
    print(f"\n  '{t}': en properties: {len(en_p)} {en_p} | SOLO en provenances: {len(en_v)} {en_v}")
    for nid in en_p + en_v:
        cand_espec.setdefault(nid, []).append(t)
for t in amplios:
    en_p = [n.id for n in kg.nodes if norm(t) in blob_nodo(n)]
    en_v = [n.id for n in kg.nodes if norm(t) not in blob_nodo(n) and norm(t) in blob_prov(n)]
    print(f"\n  '{t}': en properties: {len(en_p)} | SOLO en provenances: {len(en_v)}")
    print(f"     ids (properties): {en_p}")
    if en_v:
        print(f"     ids (solo provenance): {en_v}")
for nid, ts in sorted(cand_espec.items()):
    exp = expuesto_id(nid, outs33)
    print(f"\n  --- {nid} (términos: {ts}) | expuesto en outputs de CQ-033: {('pasos ' + str(exp)) if exp else 'NO'} ---")
    print(dump(nid))
    if not exp:
        print("  D1 (reducido):", json.dumps(d1_reducido(nid, "CQ-033", outs33), ensure_ascii=False, indent=1))

# ============ 4. CQ-016 backlog ============
print(f"\n{SEP}\n4. CQ-016 — backlog: portador del hecho identitario\n{SEP}")
for t in ("exigencia e integracion", "seccion 4", "apartado 4", "r.i.-c.m."):
    cands = [n.id for n in kg.nodes if norm(t) in blob_nodo(n)]
    print(f"\n  '{t}': {len(cands)} candidato/s en id/label/properties")
    for nid in cands:
        print(f"  --- {nid} ---")
        print(dump(nid))
```

## Output completo

```
==============================================================================
1. CQ-018
==============================================================================
(pasos re-ejecutables: 15)

[1a 'énfasis'/'flujos de fondos'] exposición en outputs completos:
  'enfasis': paso 12 (1 match/es)
     …n_propiedades": "al evaluar la capacidad de repago, el enfasis debera ponerse en el analisis de los flujos de fondos …
  'flujos de fondos': paso 12 (2 match/es)
     …e_fondos", "type": "obligacion", "label": "analisis de flujos de fondos", "tokens_matcheados": 2, "resumen_propiedades": "al e…
     …epago, el enfasis debera ponerse en el analisis de los flujos de fondos realizado por la entidad."}, {"id": "restriccion_prese…
  'flujo de fondos': paso 9 (1 match/es)
     …n seguimiento especial en observacion: el analisis del flujo de fondos del cliente demuestra que puede atender la totalidad d…
  'flujo de fondos': paso 11 (1 match/es)
     …ara clasificacion en situacion normal: el analisis del flujo de fondos del cliente demuestra que es capaz de atender adecuada…
  'flujo de fondos': paso 12 (8 match/es)
     …d_de_pago", "type": "operacion", "label": "analisis de flujo de fondos del deudor", "tokens_matcheados": 6, "resumen_propieda…
     …l_cliente", "type": "operacion", "label": "analisis de flujo de fondos", "tokens_matcheados": 3, "resumen_propiedades": "tipo…
     …cheados": 3, "resumen_propiedades": "tipo: analisis de flujo de fondos del cliente"}, {"id": "obligacion_la_entidad_debera_an…

[1b 'atender adecuadamente'/'todos sus compromisos'] exposición en outputs completos:
  'atender adecuadamente': paso 11 (1 match/es)
     … flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financ…"}, {"id": "restriccion_e…
  'atender adecuadamente': paso 12 (1 match/es)
     … flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financ…"}, {"id": "obligacion_lo…
  'todos sus compromisos': paso 11 (1 match/es)
     …liente demuestra que es capaz de atender adecuadamente todos sus compromisos financ…"}, {"id": "restriccion_en_caso_de_no_efectuars…
  'todos sus compromisos': paso 12 (1 match/es)
     …liente demuestra que es capaz de atender adecuadamente todos sus compromisos financ…"}, {"id": "obligacion_los_analisis_previos_al_…

[1c] barrido kg de portadores:

  término 'enfasis': 5 candidato/s en id/label/properties
  --- Operacion_evaluacion_de_capacidad | expuesto en outputs de CQ-018: NO ---
{
 "id": "Operacion_evaluacion_de_capacidad",
 "type": "Operacion",
 "label": "Evaluación de capacidad de repago",
 "properties": {
  "tipo": "evaluacion_de_capacidad",
  "description": "Al evaluar la capacidad de repago, el énfasis deberá ponerse en el análisis de los flujos de fondos realizado por la entidad."
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 4.3. Evaluación de la capacidad de pago."
  }
 ]
}
  D1 (reducido): {
 "portador": "Operacion_evaluacion_de_capacidad",
 "alcanzable": false,
 "mejor_rank": 111,
 "n_consultas_simuladas": 45,
 "consultas_en_top10": []
}
  --- Obligacion_analisis_de_flujos_de_fondos | expuesto en outputs de CQ-018: pasos [12] ---
{
 "id": "Obligacion_analisis_de_flujos_de_fondos",
 "type": "Obligacion",
 "label": "Análisis de flujos de fondos",
 "properties": {
  "tipo": "calculo",
  "description": "Al evaluar la capacidad de repago, el énfasis deberá ponerse en el análisis de los flujos de fondos realizado por la entidad.",
  "plazo": "durante evaluación de capacidad"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 4.3. Evaluación de la capacidad de pago."
  }
 ]
}
  --- Obligacion_medir_exposicion_en_moneda_extranjera | expuesto en outputs de CQ-018: NO ---
{
 "id": "Obligacion_medir_exposicion_en_moneda_extranjera",
 "type": "Obligacion",
 "label": "Medir exposición en moneda extranjera",
 "properties": {
  "tipo": "calculo",
  "description": "En ese análisis, se pondrá énfasis en la medición del grado de exposición que se registre en moneda extranjera en función de su endeudamiento y generación de ingresos en esa especie"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.2. Criterio de clasificación."
  }
 ]
}
  D1 (reducido): {
 "portador": "Obligacion_medir_exposicion_en_moneda_extranjera",
 "alcanzable": false,
 "mejor_rank": 714,
 "n_consultas_simuladas": 45,
 "consultas_en_top10": []
}
  --- Obligacion_analizar_capacidad_de_pago_con_variaciones_cambiarias | expuesto en outputs de CQ-018: NO ---
{
 "id": "Obligacion_analizar_capacidad_de_pago_con_variaciones_cambiarias",
 "type": "Obligacion",
 "label": "Analizar capacidad de pago con variaciones cambiarias",
 "properties": {
  "tipo": "calculo",
  "description": "Respecto de clientes por financiaciones en moneda extranjera, deberá ponerse énfasis en analizar si el cliente cuenta con una capacidad de pago suficiente que permita cubrir los vencimientos aún ante variaciones significativas en el tipo de cambio"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.2. Criterio de clasificación."
  }
 ]
}
  D1 (reducido): {
 "portador": "Obligacion_analizar_capacidad_de_pago_con_variaciones_cambiarias",
 "alcanzable": false,
 "mejor_rank": 20,
 "n_consultas_simuladas": 45,
 "consultas_en_top10": []
}
  --- Obligacion_elevar_al_directorio_o_autoridad_equivalente_como_minimo_trimestralmente_un_repo | expuesto en outputs de CQ-018: NO ---
{
 "id": "Obligacion_elevar_al_directorio_o_autoridad_equivalente_como_minimo_trimestralmente_un_repo",
 "type": "Obligacion",
 "label": "Elevar reporte trimestral al Directorio",
 "properties": {
  "descripcion": "Elevar al Directorio o autoridad equivalente, como mínimo trimestralmente, un reporte de análisis con las acciones realizadas en el marco de sus responsabilidades haciendo especial énfasis en el resultado de la evaluación realizada sobre el informe que trimestralmente le eleva el Responsable de atención al usuario de servicios financieros. El referido reporte deberá ser evaluado por ese órgano directivo, dejando constancia en el Libro de Actas respectivo.",
  "tipo": "presentacion_informativa",
  "plazo": "trimestral"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 3.2. Controles. (parte 1)"
  }
 ]
}
  D1 (reducido): {
 "portador": "Obligacion_elevar_al_directorio_o_autoridad_equivalente_como_minimo_trimestralmente_un_repo",
 "alcanzable": false,
 "mejor_rank": 856,
 "n_consultas_simuladas": 45,
 "consultas_en_top10": []
}

  término 'flujos de fondos': 5 candidato/s en id/label/properties
  --- Obligacion_el_originante_o_fiduciario_debera_poner_a_disposicion_de_los_inversores_tanto_an | expuesto en outputs de CQ-018: NO ---
{
 "id": "Obligacion_el_originante_o_fiduciario_debera_poner_a_disposicion_de_los_inversores_tanto_an",
 "type": "Obligacion",
 "label": "Poner a disposición modelo de flujos",
 "properties": {
  "descripcion": "El originante o fiduciario deberá poner a disposición de los inversores, tanto antes de determinar el precio de los títulos valores como durante la vida de la titulización, el modelo de flujos de fondos de los compromisos o la información que permita a los inversores modelizar apropiadamente la cascada de pagos de la titulización.",
  "tipo": "presentacion_informativa"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 3.1. Tratamiento de las titulizaciones. (parte 11)"
  }
 ]
}
  D1 (reducido): {
 "portador": "Obligacion_el_originante_o_fiduciario_debera_poner_a_disposicion_de_los_inversores_tanto_an",
 "alcanzable": false,
 "mejor_rank": 530,
 "n_consultas_simuladas": 45,
 "consultas_en_top10": []
}
  --- Obligacion_para_asegurar_total_transparencia_hacia_los_inversores_asistirlos_en_el_proceso_ | expuesto en outputs de CQ-018: NO ---
{
 "id": "Obligacion_para_asegurar_total_transparencia_hacia_los_inversores_asistirlos_en_el_proceso_",
 "type": "Obligacion",
 "label": "Definir obligaciones contractuales claramente",
 "properties": {
  "descripcion": "Para asegurar total transparencia hacia los inversores, asistirlos en el proceso de debida diligencia y evitar que se vean sujetos a disrupciones inesperadas en la cobranza de flujos de fondos y servicios, las obligaciones contractuales, deberes y responsabilidades de los participantes de la titulización –incluyendo tanto a aquellos con responsabilidad fiduciaria como a los proveedores de servicios auxiliares–, deberán estar claramente definidos en la oferta inicial y en los documentos de apoyo de la titulización.",
  "tipo": "presentacion_informativa"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 3.1. Tratamiento de las titulizaciones. (parte 11)"
  }
 ]
}
  D1 (reducido): {
 "portador": "Obligacion_para_asegurar_total_transparencia_hacia_los_inversores_asistirlos_en_el_proceso_",
 "alcanzable": false,
 "mejor_rank": 1266,
 "n_consultas_simuladas": 45,
 "consultas_en_top10": []
}
  --- Restriccion_los_flujos_de_fondos_deberan_estar_contractualmente_identificados_ser_periodicos | expuesto en outputs de CQ-018: NO ---
{
 "id": "Restriccion_los_flujos_de_fondos_deberan_estar_contractualmente_identificados_ser_periodicos",
 "type": "Restriccion",
 "label": "Flujos fondos contractualmente identificados",
 "properties": {
  "descripcion": "Los flujos de fondos deberán estar contractualmente identificados, ser periódicos y consistir exclusivamente en pagos del principal e intereses o de arrendamientos financieros",
  "tipo": "limite_cualitativo"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 3.1. Tratamiento de las titulizaciones. (parte 8)"
  }
 ]
}
  D1 (reducido): {
 "portador": "Restriccion_los_flujos_de_fondos_deberan_estar_contractualmente_identificados_ser_periodicos",
 "alcanzable": false,
 "mejor_rank": 245,
 "n_consultas_simuladas": 45,
 "consultas_en_top10": []
}
  --- Operacion_evaluacion_de_capacidad | expuesto en outputs de CQ-018: NO ---
{
 "id": "Operacion_evaluacion_de_capacidad",
 "type": "Operacion",
 "label": "Evaluación de capacidad de repago",
 "properties": {
  "tipo": "evaluacion_de_capacidad",
  "description": "Al evaluar la capacidad de repago, el énfasis deberá ponerse en el análisis de los flujos de fondos realizado por la entidad."
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 4.3. Evaluación de la capacidad de pago."
  }
 ]
}
  D1 (reducido): {
 "portador": "Operacion_evaluacion_de_capacidad",
 "alcanzable": false,
 "mejor_rank": 111,
 "n_consultas_simuladas": 45,
 "consultas_en_top10": []
}
  --- Obligacion_analisis_de_flujos_de_fondos | expuesto en outputs de CQ-018: pasos [12] ---
{
 "id": "Obligacion_analisis_de_flujos_de_fondos",
 "type": "Obligacion",
 "label": "Análisis de flujos de fondos",
 "properties": {
  "tipo": "calculo",
  "description": "Al evaluar la capacidad de repago, el énfasis deberá ponerse en el análisis de los flujos de fondos realizado por la entidad.",
  "plazo": "durante evaluación de capacidad"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 4.3. Evaluación de la capacidad de pago."
  }
 ]
}

  término 'flujo de fondos': 11 candidato/s en id/label/properties
  --- Restriccion_un_proyecto_se_encuentra_en_etapa_preoperativa_si_a_el_ente_creado_para_gestiona | expuesto en outputs de CQ-018: NO ---
{
 "id": "Restriccion_un_proyecto_se_encuentra_en_etapa_preoperativa_si_a_el_ente_creado_para_gestiona",
 "type": "Restriccion",
 "label": "Etapa preoperativa proyecto infraestructura",
 "properties": {
  "descripcion": "Un proyecto se encuentra en etapa preoperativa si: a) el ente creado para gestionarlo aún no cuenta con un flujo de fondos positivo suficiente como para cubrir las obligaciones contractuales; y b) la deuda de largo plazo no es decreciente",
  "tipo": "limite_cualitativo"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.7. Exposiciones a empresas."
  }
 ]
}
  D1 (reducido): {
 "portador": "Restriccion_un_proyecto_se_encuentra_en_etapa_preoperativa_si_a_el_ente_creado_para_gestiona",
 "alcanzable": false,
 "mejor_rank": 3225,
 "n_consultas_simuladas": 45,
 "consultas_en_top10": []
}
  --- Restriccion_el_repago_de_las_financiaciones_no_debera_depender_significativamente_del_flujo_ | expuesto en outputs de CQ-018: NO ---
{
 "id": "Restriccion_el_repago_de_las_financiaciones_no_debera_depender_significativamente_del_flujo_",
 "type": "Restriccion",
 "label": "Repago no depende flujo inmueble",
 "properties": {
  "descripcion": "El repago de las financiaciones no deberá depender significativamente del flujo de fondos generados por el inmueble objeto de la garantía hipotecaria",
  "tipo": "limite_cualitativo"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 5. ii) El valor del inmueble se corresponda al del momento del otorgamiento, ex-"
  }
 ]
}
  D1 (reducido): {
 "portador": "Restriccion_el_repago_de_las_financiaciones_no_debera_depender_significativamente_del_flujo_",
 "alcanzable": false,
 "mejor_rank": 51,
 "n_consultas_simuladas": 45,
 "consultas_en_top10": []
}
  --- Excepcion_excepcion_informacion_de_repago_si_deuda_cubierta | expuesto en outputs de CQ-018: NO ---
{
 "id": "Excepcion_excepcion_informacion_de_repago_si_deuda_cubierta",
 "type": "Excepcion",
 "label": "Excepción información de repago si deuda cubierta",
 "properties": {
  "description": "Cuando no corresponda evaluar la capacidad de repago del deudor por encontrarse la deuda cubierta con garantías preferidas A, no será obligatorio incorporar al legajo del cliente el flujo de fondos, los estados contables ni toda otra información necesaria para efectuar ese análisis"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 3.4. Legajo del cliente. (parte 1)"
  }
 ]
}
  D1 (reducido): {
 "portador": "Excepcion_excepcion_informacion_de_repago_si_deuda_cubierta",
 "alcanzable": false,
 "mejor_rank": 3381,
 "n_consultas_simuladas": 45,
 "consultas_en_top10": []
}
  --- Obligacion_la_entidad_debera_analizar_el_flujo_de_fondos_proyectado_para_clasificar_cliente | expuesto en outputs de CQ-018: pasos [12] ---
{
 "id": "Obligacion_la_entidad_debera_analizar_el_flujo_de_fondos_proyectado_para_clasificar_cliente",
 "type": "Obligacion",
 "label": "Análisis flujo fondos proyectado",
 "properties": {
  "descripcion": "La entidad deberá analizar el flujo de fondos proyectado para clasificar clientes que no registren asistencia crediticia previa.",
  "tipo": "calculo"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.5. Niveles de clasificación. (parte 1)"
  }
 ]
}
  --- Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien | expuesto en outputs de CQ-018: pasos [11, 12] ---
{
 "id": "Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien",
 "type": "Obligacion",
 "label": "Evaluación situación financiera normal",
 "properties": {
  "descripcion": "Para clasificación en situación normal: El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financieros.",
  "tipo": "calculo"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.5. Niveles de clasificación. (parte 1)"
  }
 ]
}
  --- Obligacion_para_clasificacion_con_seguimiento_especial_en_observacion_el_analisis_del_flujo | expuesto en outputs de CQ-018: pasos [9] ---
{
 "id": "Obligacion_para_clasificacion_con_seguimiento_especial_en_observacion_el_analisis_del_flujo",
 "type": "Obligacion",
 "label": "Evaluación situación en observación",
 "properties": {
  "descripcion": "Para clasificación con seguimiento especial en observación: El análisis del flujo de fondos del cliente demuestra que puede atender la totalidad de sus compromisos financieros pero existen situaciones posibles que podrían comprometer la capacidad futura de pago.",
  "tipo": "calculo"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.5. Niveles de clasificación. (parte 1)"
  }
 ]
}
  --- Operacion_analisis_de_capacidad_de_pago | expuesto en outputs de CQ-018: pasos [12] ---
{
 "id": "Operacion_analisis_de_capacidad_de_pago",
 "type": "Operacion",
 "label": "Análisis de flujo de fondos del deudor",
 "properties": {
  "tipo": "análisis de capacidad de pago"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.5. Niveles de clasificación. (parte 2)"
  }
 ]
}
  --- Restriccion_presente_una_situacion_financiera_iliquida_y_un_nivel_de_flujo_de_fondos_que_no_ | expuesto en outputs de CQ-018: pasos [12] ---
{
 "id": "Restriccion_presente_una_situacion_financiera_iliquida_y_un_nivel_de_flujo_de_fondos_que_no_",
 "type": "Restriccion",
 "label": "Situación financiera ilíquida",
 "properties": {
  "descripcion": "Presente una situación financiera ilíquida y un nivel de flujo de fondos que no le permita atender el pago de la totalidad del capital y de los intereses de las deudas, pudiendo cubrir solamente estos últimos.",
  "tipo": "limite_cualitativo"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.5. Niveles de clasificación. (parte 3)"
  }
 ]
}
  --- Operacion_analisis_de_flujo_de_fondos_del_cliente | expuesto en outputs de CQ-018: pasos [12] ---
{
 "id": "Operacion_analisis_de_flujo_de_fondos_del_cliente",
 "type": "Operacion",
 "label": "Análisis de flujo de fondos",
 "properties": {
  "tipo": "análisis de flujo de fondos del cliente"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.5. Niveles de clasificación. (parte 4)"
  }
 ]
}
  --- Restriccion_el_flujo_de_fondos_es_manifiestamente_insuficiente_no_alcanzando_a_cubrir_el_pag | expuesto en outputs de CQ-018: pasos [12] ---
{
 "id": "Restriccion_el_flujo_de_fondos_es_manifiestamente_insuficiente_no_alcanzando_a_cubrir_el_pag",
 "type": "Restriccion",
 "label": "Insuficiencia de flujo de fondos",
 "properties": {
  "descripcion": "El flujo de fondos es manifiestamente insuficiente, no alcanzando a cubrir el pago de intereses.",
  "tipo": "limite_cualitativo"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.5. Niveles de clasificación. (parte 4)"
  }
 ]
}
  --- Operacion_prestamos_financieros | expuesto en outputs de CQ-018: NO ---
{
 "id": "Operacion_prestamos_financieros",
 "type": "Operacion",
 "label": "Préstamos financieros vigentes al 31/08/19",
 "properties": {
  "tipo": "préstamos financieros",
  "description": "Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones de bienes"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 7.3. Aplicación de divisas de cobros de exportaciones. (parte 1)"
  }
 ]
}
  D1 (reducido): {
 "portador": "Operacion_prestamos_financieros",
 "alcanzable": false,
 "mejor_rank": 101,
 "n_consultas_simuladas": 45,
 "consultas_en_top10": []
}

  término 'atender adecuadamente': 1 candidato/s en id/label/properties
  --- Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien | expuesto en outputs de CQ-018: pasos [11, 12] ---
{
 "id": "Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien",
 "type": "Obligacion",
 "label": "Evaluación situación financiera normal",
 "properties": {
  "descripcion": "Para clasificación en situación normal: El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financieros.",
  "tipo": "calculo"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.5. Niveles de clasificación. (parte 1)"
  }
 ]
}

  término 'todos sus compromisos': 1 candidato/s en id/label/properties
  --- Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien | expuesto en outputs de CQ-018: pasos [11, 12] ---
{
 "id": "Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien",
 "type": "Obligacion",
 "label": "Evaluación situación financiera normal",
 "properties": {
  "descripcion": "Para clasificación en situación normal: El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financieros.",
  "tipo": "calculo"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.5. Niveles de clasificación. (parte 1)"
  }
 ]
}

==============================================================================
2. CQ-019
==============================================================================
(pasos re-ejecutables: 9)

[2a] exposición en outputs completos:
  '31 dias': paso 7 (1 match/es)
     …o de sus obligaciones o con atrasos que no superan los 31 dias"}, {"id": "obligacion_para_clasificacion_en_situacion_…
  'puntual': paso 7 (2 match/es)
     …striccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones", "type": "restriccion", "…
     …edades": "comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no super…
  'situacion normal': paso 2 (1 match/es)
     …respondiente a la cartera de deudores clasificados 'en situacion normal' –puntos…"}, {"id": "operacion_venta_de_activos_de_imp…
  'situacion normal': paso 4 (1 match/es)
     …respondiente a la cartera de deudores clasificados 'en situacion normal' –puntos 6.5.1. y 7.2.1. del to sobre clasificacion de…
  'situacion normal': paso 7 (6 match/es)
     …{"consulta": "deudores situacion normal prevision", "total_con_match": 60, "resultados": [{"id…
     …"restriccion", "label": "cancelacion de intereses para situacion normal", "tokens_matcheados": 3, "resumen_propiedades": "los …
     … los intereses devengados, podran ser clasificados en 'situacion normal' si ademas observan las otras condicione…"}, {"id": "o…

[2b] barrido kg — regla mecánica de alcance: se pegan ÍNTEGROS los candidatos que
matchean 'situacion normal' (ancla de la definición); para 'puntual' y '31' se reporta
conteo + ids, e íntegro solo si el nodo matchea además otro de los términos.

  'situacion normal': 9 candidatos: ['Obligacion_computar_conceptos_sobre_saldos_mensuales', 'Restriccion_limite_de_deduccion_de_prevision_normal', 'Restriccion_limite_maximo_previsiones_por_incobrabilidad', 'Restriccion_la_diferencia_positiva_resultante_de_comparar_el_importe_de_la_prevision_regulat', 'Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien', 'Restriccion_los_deudores_que_hayan_cancelado_la_totalidad_de_los_intereses_devengados_podran', 'Restriccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones', 'Obligacion_informar_previsiones_por_incobrabilidad', 'Restriccion_limite_previsiones_incobrabilidad']
  'puntual': 6 candidatos: ['Restriccion_las_empresas_con_grado_de_inversion_son_aquellas_con_capacidad_suficiente_para_a', 'Restriccion_debe_ser_incondicional_el_contrato_de_proteccion_no_debe_contener_ninguna_clausu', 'Restriccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones', 'Operacion_pago_de_cuotas', 'Obligacion_deudores_con_deudas_refinanciadas_mediante_obligaciones_periodicas_deben_cumplir', 'Operacion_consulta']
  '31' (número suelto): 36 candidatos: ['Excepcion_financiaciones_acordadas_a_partir_del_18_05_2020_y_hasta_el_31_10_24_y_financiac', 'Restriccion_desde_el_01_06_24_y_hasta_el_31_12_24_las_entidades_en_funcionamiento_deberan_ap', 'Restriccion_aplicacion_de_ccf_del_0_desde_01_01_25_al_30_06_25_y_del_5_desde_01_07_25_al_31_', 'Obligacion_convertir_compromisos_en_equivalentes', 'Obligacion_cuando_al_menos_se_haya_cumplido_con_el_pago_sin_haber_incurrido_en_atrasos_supe', 'Restriccion_los_deudores_que_incurran_en_atrasos_de_mas_de_31_dias_respecto_de_las_condicion', 'Restriccion_no_se_podran_efectuar_mejoras_en_las_clasificaciones_de_los_clientes_si_los_mism', 'Restriccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones', 'Restriccion_comprende_los_clientes_que_registran_incumplimientos_ocasionales_en_la_atencion_', 'Obligacion_en_caso_de_verificarse_atrasos_mayores_a_31_dias_en_el_pago_de_los_servicios_de_', 'Restriccion_no_se_permite_reclasificacion_si_hay_atrasos_mayores_a_31_dias_en_el_pago_de_ser', 'Obligacion_deudores_con_deudas_refinanciadas_mediante_obligaciones_periodicas_deben_cumplir', 'Obligacion_intervenir_documentacion_aduanera_monto_deuda', 'Obligacion_obtener_declaracion_jurada_de_importador', 'Restriccion_posiciones_arancelarias_ncm_8802_11_00_8802_12_10_8802_12_90_8802_20_10_8802_20_', 'Restriccion_requisito_fletes_de_exportacion_con_embarque', 'Excepcion_el_pago_se_concreta_en_el_marco_de_lo_dispuesto_en_el_punto_4_8_4_por_un_cliente', 'Excepcion_el_pago_se_concreta_en_el_marco_de_lo_dispuesto_en_el_punto_4_8_5_por_un_cliente', 'Operacion_prefinanciacion', 'Restriccion_los_fondos_adquiridos_sean_depositados_en_cuentas_abiertas_en_entidades_financie', 'Restriccion_limite_de_capital_en_mercado_de_cambios', 'Restriccion_suscripcion_por_intereses_vencidos_financieros', 'Restriccion_clientes_deben_haber_suscrito_bopreal_serie_1_con_anterioridad_al_31_01_24_por_m', 'Restriccion_clientes_que_suscribieron_bopreal_serie_1_con_anterioridad_al_31_01_24_por_monto', 'Operacion_prestamos_financieros', 'Operacion_prefinanciaciones_y_financiaciones_de_exportaciones', 'Operacion_anticipos_y_prefinanciaciones_del_exterior', 'Restriccion_conformidad_previa_del_bcra_para_prefinanciaciones_anteriores', 'Restriccion_su_emision_haya_tenido_lugar_entre_el_07_01_21_y_el_31_12_23', 'Restriccion_concertadas_a_partir_entre_el_09_10_20_y_el_31_12_23', 'Restriccion_el_monto_de_capital_por_el_cual_se_accedio_al_mercado_de_cambios_hasta_el_31_12_', 'Operacion_anticipo', 'Obligacion_requerir_declaracion_jurada_exportador', 'Obligacion_la_entidad_debe_contar_con_una_declaracion_jurada_del_exportador_detallando_el_m', 'Restriccion_cargo_de_capital_escalonado_segun_dias_habiles_posteriores_a_liquidacion', 'Obligacion_se_reemplazaran_las_dos_ultimas_posiciones_de_cada_partida_de_exigencia_por_el_u']

  --- Obligacion_computar_conceptos_sobre_saldos_mensuales | expuesto en outputs de CQ-019: NO ---
{
 "id": "Obligacion_computar_conceptos_sobre_saldos_mensuales",
 "type": "Obligacion",
 "label": "Computar conceptos sobre saldos mensuales",
 "properties": {
  "tipo": "calculo",
  "description": "Los conceptos comprendidos se computarán sobre la base de los saldos al último día de cada mes (capitales, intereses, primas, actualizaciones –por el Coeficiente de Estabilización de Referencia CER– y diferencias de cotización, según corresponda, netos de las previsiones por riesgos de incobrabilidad –incluyendo, de corresponder, las previsiones contabilizadas en el pasivo– y desvalorización y de las depreciaciones y amortizaciones acumuladas que les sean atribuibles y demás cuentas regularizadoras, sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados 'en situación normal' –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A).",
  "plazo": "mensual"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.3. Cómputo de los conceptos comprendidos."
  }
 ]
}
  D1 (reducido): {
 "portador": "Obligacion_computar_conceptos_sobre_saldos_mensuales",
 "alcanzable": false,
 "mejor_rank": 64,
 "n_consultas_simuladas": 37,
 "consultas_en_top10": []
}

  --- Obligacion_deudores_con_deudas_refinanciadas_mediante_obligaciones_periodicas_deben_cumplir | expuesto en outputs de CQ-019: NO ---
{
 "id": "Obligacion_deudores_con_deudas_refinanciadas_mediante_obligaciones_periodicas_deben_cumplir",
 "type": "Obligacion",
 "label": "Cumplimiento de 3 cuotas para reclasificación",
 "properties": {
  "tipo": "otra",
  "descripcion": "Deudores con deudas refinanciadas mediante obligaciones periódicas deben cumplir puntualmente o con atrasos no superiores a 31 días con el pago de 3 cuotas consecutivas para ser reclasificados",
  "plazo": "3 cuotas consecutivas"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 7.2. Niveles de clasificación. (parte 2)"
  }
 ]
}
  D1 (reducido): {
 "portador": "Obligacion_deudores_con_deudas_refinanciadas_mediante_obligaciones_periodicas_deben_cumplir",
 "alcanzable": false,
 "mejor_rank": 46,
 "n_consultas_simuladas": 37,
 "consultas_en_top10": []
}

  --- Obligacion_informar_previsiones_por_incobrabilidad | expuesto en outputs de CQ-019: NO ---
{
 "id": "Obligacion_informar_previsiones_por_incobrabilidad",
 "type": "Obligacion",
 "label": "Informar previsiones por incobrabilidad",
 "properties": {
  "tipo": "presentacion_informativa",
  "description": "Se informarán las previsiones por riesgo de incobrabilidad correspondientes a financiaciones en situación normal o cubiertas con garantías preferidas A que no superen el 1,25 % de los APRs."
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 6.1. Normas de procedimiento (parte 2)"
  }
 ]
}
  D1 (reducido): {
 "portador": "Obligacion_informar_previsiones_por_incobrabilidad",
 "alcanzable": true,
 "mejor_rank": 4,
 "n_consultas_simuladas": 37,
 "consultas_en_top10": [
  {
   "consulta": "prevision incobrabilidad",
   "rank": 4,
   "origen": "ngrama_pregunta"
  }
 ]
}

  --- Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien | expuesto en outputs de CQ-019: pasos [7] ---
{
 "id": "Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien",
 "type": "Obligacion",
 "label": "Evaluación situación financiera normal",
 "properties": {
  "descripcion": "Para clasificación en situación normal: El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financieros.",
  "tipo": "calculo"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.5. Niveles de clasificación. (parte 1)"
  }
 ]
}

  --- Restriccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones | expuesto en outputs de CQ-019: pasos [7] ---
{
 "id": "Restriccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones",
 "type": "Restriccion",
 "label": "Límite de atraso en situación normal",
 "properties": {
  "descripcion": "Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días",
  "tipo": "limite_cuantitativo",
  "umbral": "31 días"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 7.2. Niveles de clasificación. (parte 1)"
  }
 ]
}

  --- Restriccion_la_diferencia_positiva_resultante_de_comparar_el_importe_de_la_prevision_regulat | expuesto en outputs de CQ-019: pasos [2, 8] ---
{
 "id": "Restriccion_la_diferencia_positiva_resultante_de_comparar_el_importe_de_la_prevision_regulat",
 "type": "Restriccion",
 "label": "Deducción de previsión NIIF 9",
 "properties": {
  "descripcion": "La diferencia positiva resultante de comparar el importe de la previsión regulatoria o la contable correspondiente al balance de saldos al 30.11.19, la mayor de ambas, y la previsión contable por la aplicación del punto 5.5. 'Deterioro de Valor' de la NIIF 9. Previo a su deducción deberá absorberse el importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera en 'situación normal' computado como patrimonio neto complementario.",
  "tipo": "limite_cualitativo"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 8.4. Conceptos deducibles. (parte 1)"
  }
 ]
}

  --- Restriccion_limite_de_deduccion_de_prevision_normal | expuesto en outputs de CQ-019: pasos [2, 4, 6, 7] ---
{
 "id": "Restriccion_limite_de_deduccion_de_prevision_normal",
 "type": "Restriccion",
 "label": "Límite de deducción de previsión normal",
 "properties": {
  "tipo": "limite_cualitativo",
  "description": "Sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados 'en situación normal' –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A)."
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.3. Cómputo de los conceptos comprendidos."
  }
 ]
}

  --- Restriccion_limite_maximo_previsiones_por_incobrabilidad | expuesto en outputs de CQ-019: NO ---
{
 "id": "Restriccion_limite_maximo_previsiones_por_incobrabilidad",
 "type": "Restriccion",
 "label": "Límite máximo previsiones por incobrabilidad",
 "properties": {
  "tipo": "limite_cuantitativo",
  "description": "Las previsiones por riesgo de incobrabilidad sobre la cartera correspondiente a deudores clasificados en situación normal y sobre las financiaciones cubiertas con garantías preferidas A, no pueden superar el 1,25% de los activos ponderados por riesgo de crédito",
  "umbral": "1,25%"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 8.2. Conceptos computables."
  }
 ]
}
  D1 (reducido): {
 "portador": "Restriccion_limite_maximo_previsiones_por_incobrabilidad",
 "alcanzable": true,
 "mejor_rank": 7,
 "n_consultas_simuladas": 37,
 "consultas_en_top10": [
  {
   "consulta": "prevision incobrabilidad",
   "rank": 7,
   "origen": "ngrama_pregunta"
  }
 ]
}

  --- Restriccion_limite_previsiones_incobrabilidad | expuesto en outputs de CQ-019: NO ---
{
 "id": "Restriccion_limite_previsiones_incobrabilidad",
 "type": "Restriccion",
 "label": "Límite previsiones incobrabilidad",
 "properties": {
  "tipo": "limite_cuantitativo",
  "umbral": "1,25%",
  "description": "Las previsiones por riesgo de incobrabilidad correspondientes a financiaciones en situación normal o cubiertas con garantías preferidas A no deben superar el 1,25 % de los APRs."
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 6.1. Normas de procedimiento (parte 2)"
  }
 ]
}
  D1 (reducido): {
 "portador": "Restriccion_limite_previsiones_incobrabilidad",
 "alcanzable": true,
 "mejor_rank": 3,
 "n_consultas_simuladas": 37,
 "consultas_en_top10": [
  {
   "consulta": "prevision incobrabilidad",
   "rank": 3,
   "origen": "ngrama_pregunta"
  }
 ]
}

  --- Restriccion_los_deudores_que_hayan_cancelado_la_totalidad_de_los_intereses_devengados_podran | expuesto en outputs de CQ-019: pasos [7] ---
{
 "id": "Restriccion_los_deudores_que_hayan_cancelado_la_totalidad_de_los_intereses_devengados_podran",
 "type": "Restriccion",
 "label": "Cancelación de intereses para situación normal",
 "properties": {
  "descripcion": "Los deudores que hayan cancelado la totalidad de los intereses devengados, podrán ser clasificados en 'situación normal' si además observan las otras condiciones previstas para esa categoría.",
  "tipo": "limite_cuantitativo",
  "umbral": "100% intereses devengados"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.5. Niveles de clasificación. (parte 2)"
  }
 ]
}

==============================================================================
3. CQ-033
==============================================================================
(pasos re-ejecutables: 7)

[3a] exposición en outputs completos:
  '30/06': paso 3 (1 match/es)
     …on de la expresion descripta en el punto 7.2. hasta el 30/06/26 no podra superar el 17% del promedio de los ultimos…
  '30-06': AUSENTE en todos los outputs completos
  'junio': AUSENTE en todos los outputs completos
  'vigente': AUSENTE en todos los outputs completos
  'vigencia': AUSENTE en todos los outputs completos
  'transitoria': AUSENTE en todos los outputs completos
  '12.3': paso 3 (1 match/es)
     … "to_capitales_minimos_actual.pdf", "location": "punto 12.3. para aquellas entidades financieras que sean reclasif…
  '12.3': paso 4 (5 match/es)
     … "to_capitales_minimos_actual.pdf", "location": "punto 12.3. para aquellas entidades financieras que sean reclasif…
     … "to_capitales_minimos_actual.pdf", "location": "punto 12.3. para aquellas entidades financieras que sean reclasif…
     … "to_capitales_minimos_actual.pdf", "location": "punto 12.3. para aquellas entidades financieras que sean reclasif…
  '12.3': paso 5 (1 match/es)
     … "to_capitales_minimos_actual.pdf", "location": "punto 12.3. para aquellas entidades financieras que sean reclasif…
  '12.3': paso 6 (1 match/es)
     … "to_capitales_minimos_actual.pdf", "location": "punto 12.3. para aquellas entidades financieras que sean reclasif…
  '12.3': paso 7 (3 match/es)
     … "to_capitales_minimos_actual.pdf", "location": "punto 12.3. para aquellas entidades financieras que sean reclasif…
     … "to_capitales_minimos_actual.pdf", "location": "punto 12.3. para aquellas entidades financieras que sean reclasif…
     … "to_capitales_minimos_actual.pdf", "location": "punto 12.3. para aquellas entidades financieras que sean reclasif…

[3b] barrido kg (properties Y provenances por separado) — regla mecánica de alcance:
íntegros los candidatos de términos específicos ('30/06','30-06','junio','transitoria','12.3');
para 'vigente'/'vigencia' conteo + ids, íntegro solo si matchea además un término específico.

  '30/06': en properties: 3 ['Restriccion_aplicacion_de_ccf_del_0_desde_01_01_25_al_30_06_25_y_del_5_desde_01_07_25_al_31_', 'Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ', 'Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_c_determ'] | SOLO en provenances: 0 []

  '30-06': en properties: 0 [] | SOLO en provenances: 0 []

  'junio': en properties: 2 ['Excepcion_informacion_con_frecuencia_trimestral', 'Obligacion_los_datos_se_informaran_con_frecuencia_trimestral_y_se_integraran_con_los_datos_'] | SOLO en provenances: 0 []

  'transitoria': en properties: 1 ['Operacion_adquisicion_con_caracter_transitorio_de_participaciones_en_empresas_para_facilit'] | SOLO en provenances: 0 []

  '12.3': en properties: 0 [] | SOLO en provenances: 19 ['Comunicacion_a_8383', 'EntidadFinanciera_entidad_del_grupo_2', 'EntidadFinanciera_entidad_del_grupo_b', 'EntidadFinanciera_entidad_del_grupo_c', 'Operacion_reclasificacion', 'Operacion_calculo', 'Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ', 'Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_c_determ', 'Excepcion_los_limites_maximos_se_reduciran_a_11_y_8_respectivamente_cuando_la_entidad_fina', 'Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c', 'Obligacion_se_considerara_la_ultima_calificacion_informada_para_el_calculo_de_la_exigencia_', 'Operacion_ajuste_contable_por_convergencia_a_niif', 'Operacion_calculo_de_resultados_de_ajustes_niif', 'Operacion_presentacion_de_informacion_contable_trimestral', 'Excepcion_se_consideran_admitidos_los_defectos_surgidos_de_la_conciliacion_trimestral_en_c', 'Restriccion_los_resultados_provenientes_de_ajustes_niif_por_primera_vez_dentro_de_la_rpc_se_', 'Obligacion_debera_presentarse_conciliacion_de_estados_contables_trimestrales_en_el_marco_de', 'Obligacion_de_reunir_los_requisitos_se_consignara_en_la_partida_60500000_la_porcion_pertine', 'Obligacion_se_consignara_como_numero_y_fecha_de_resolucion_la_de_la_comunicacion_a_6456_y_s']

  'vigente': en properties: 33 | SOLO en provenances: 0
     ids (properties): ['Obligacion_se_computara_el_importe_que_surja_de_aplicar_a_los_valores_contables_de_los_inst', 'Obligacion_calculo_ead_vigente_neto_cva', 'Restriccion_el_requerimiento_de_capital_por_riesgo_de_credito_de_contraparte_equivaldra_a_la', 'Operacion_operacion_con_reformulacion_periodica', 'Obligacion_la_documentacion_vinculada_con_la_crc_debera_observar_los_requisitos_legales_vig', 'Obligacion_convertir_posicion_neta_a_pesos', 'TextoOrdenado_to_clasificacion_deudores_actual_pdf', 'Restriccion_las_facilidades_adicionales_que_se_otorguen_respecto_de_los_margenes_vigentes_ac', 'Excepcion_no_se_consideraran_refinanciaciones_las_facilidades_adicionales_que_se_otorguen_', 'Obligacion_venta_divisas_con_debito_en_cuentas_locales', 'Operacion_venta_de_moneda_extranjera', 'Obligacion_la_venta_de_las_divisas_es_cursada_con_debito_en_cuentas_del_cliente_en_entidade', 'Excepcion_sin_necesidad_de_contar_con_conformidad_previa_del_bcra_si_tal_requisito_estuvie', 'Excepcion_sin_necesidad_de_contar_con_conformidad_previa_del_bcra_si_este_requisito_estuvi', 'Excepcion_sin_necesidad_de_contar_con_conformidad_previa_del_bcra_ni_respetar_plazos_minim', 'Restriccion_conformidad_previa_del_bcra_no_requerida', 'Excepcion_excepcion_por_punto_3_13', 'Obligacion_realizar_denuncia_de_incumplido', 'Obligacion_la_entidad_interviniente_haya_verificado_que_el_endeudamiento_cuyo_servicio_sera', 'Restriccion_se_debera_acreditar_el_cumplimiento_de_los_restantes_requisitos_generales_y_espe', 'Obligacion_en_todos_los_casos_se_debera_acreditar_el_cumplimiento_de_los_restantes_requisit', 'Restriccion_en_la_medida_que_se_encuentre_vigente_el_requisito_de_conformidad_previa_del_bcr', 'Obligacion_cumplimiento_de_requisitos_de_mercado_cambios', 'Operacion_prestamos_financieros', 'Excepcion_cuando_en_el_pais_de_destino_existiese_un_plazo_minimo_de_financiacion_de_la_imp', 'Obligacion_computo_de_liquidaciones_de_divisas', 'Restriccion_aplicacion_de_reduccion_de_plazo', 'Obligacion_los_limites_de_compra_de_compra_en_cuotas_de_financiacion_y_de_adelanto_de_diner', 'Obligacion_el_usuario_de_servicios_financieros_podra_solicitar_a_su_cargo_y_en_cualquier_mo', 'Obligacion_publicar_modelos_de_contrato_de_adhesion', 'Obligacion_los_sujetos_obligados_deberan_establecer_este_servicio_para_dar_tratamiento_y_re', 'Obligacion_participar_en_el_diseno_de_nuevos_productos_y_servicios_asi_como_en_la_modificac', 'Restriccion_verificar_que_la_publicidad_que_por_cualquier_medio_realice_el_sujeto_obligado_s']

  'vigencia': en properties: 14 | SOLO en provenances: 0
     ids (properties): ['Excepcion_financiaciones_acordadas_a_partir_del_18_05_2020_y_hasta_el_31_10_24_y_financiac', 'Restriccion_el_periodo_de_vigencia_del_derivado_de_credito_no_podra_ser_inferior_a_cualquier', 'Excepcion_no_se_consideraran_como_refinanciacion_las_refinanciaciones_otorgadas_a_producto', 'Obligacion_a_los_fines_de_la_clasificacion_debera_tenerse_en_cuenta_la_mora_en_el_atraso_de', 'Restriccion_condiciones_previas_para_cesion_de_seguimiento', 'Restriccion_plazo_vigencia_garantia_maximo_180_dias', 'Obligacion_presentacion_de_documento_identidad', 'Restriccion_aplicacion_de_ampliacion_de_plazo', 'Restriccion_aplicacion_de_reduccion_de_plazo', 'Excepcion_en_caso_de_tratarse_de_una_operacion_del_exterior_liquidada_parcialmente_durante', 'Obligacion_las_bonificaciones_convenidas_las_condiciones_para_su_aplicacion_y_su_plazo_de_v', 'Obligacion_el_usuario_de_servicios_financieros_debe_ser_notificado_de_las_modificaciones_qu', 'Obligacion_en_el_cuerpo_de_las_notificaciones_deberan_incluirse_la_leyenda_usted_podra_opta', 'Obligacion_adjuntar_documentacion_de_identificacion']

  --- Comunicacion_a_8383 (términos: ['12.3']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Comunicacion_a_8383",
 "type": "Comunicacion",
 "label": "Com. A 8383",
 "properties": {
  "codigo": "A-8383",
  "tipo": "A",
  "numero": "8383"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ]
}
  D1 (reducido): {
 "portador": "Comunicacion_a_8383",
 "alcanzable": false,
 "mejor_rank": 2590,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

  --- EntidadFinanciera_entidad_del_grupo_2 (términos: ['12.3']) | expuesto en outputs de CQ-033: pasos [1] ---
{
 "id": "EntidadFinanciera_entidad_del_grupo_2",
 "type": "EntidadFinanciera",
 "label": "Entidades del grupo 2",
 "properties": {
  "categoria": "entidades del grupo 2"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ]
}

  --- EntidadFinanciera_entidad_del_grupo_b (términos: ['12.3']) | expuesto en outputs de CQ-033: pasos [4] ---
{
 "id": "EntidadFinanciera_entidad_del_grupo_b",
 "type": "EntidadFinanciera",
 "label": "Entidades del grupo B",
 "properties": {
  "categoria": "entidades del grupo B"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ]
}

  --- EntidadFinanciera_entidad_del_grupo_c (términos: ['12.3']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "EntidadFinanciera_entidad_del_grupo_c",
 "type": "EntidadFinanciera",
 "label": "Entidades del grupo C",
 "properties": {
  "categoria": "entidades del grupo C"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ]
}
  D1 (reducido): {
 "portador": "EntidadFinanciera_entidad_del_grupo_c",
 "alcanzable": true,
 "mejor_rank": 8,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": [
  {
   "consulta": "entidad grupo",
   "rank": 8,
   "origen": "ngrama_pregunta"
  },
  {
   "consulta": "operacional entidad grupo",
   "rank": 8,
   "origen": "ngrama_pregunta"
  },
  {
   "consulta": "entidad grupo 2",
   "rank": 9,
   "origen": "ngrama_pregunta"
  }
 ]
}

  --- Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c (términos: ['12.3']) | expuesto en outputs de CQ-033: pasos [4, 6, 7] ---
{
 "id": "Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c",
 "type": "Excepcion",
 "label": "Reducción límite con calificación SEFYC 1-2",
 "properties": {
  "descripcion": "En los casos en que la entidad financiera cuente en todos los citados aspectos con calificación 1 o 2, el límite máximo disminuirá a 7% o 5%, según pertenezca al grupo B o C"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ]
}

  --- Excepcion_informacion_con_frecuencia_trimestral (términos: ['junio']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Excepcion_informacion_con_frecuencia_trimestral",
 "type": "Excepcion",
 "label": "Información con frecuencia trimestral",
 "properties": {
  "description": "Excepto las siguientes informaciones que tendrán frecuencia trimestral y se integrarán con los datos correspondientes al último mes de cada trimestre (marzo, junio, septiembre y diciembre)"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al m"
  }
 ]
}
  D1 (reducido): {
 "portador": "Excepcion_informacion_con_frecuencia_trimestral",
 "alcanzable": false,
 "mejor_rank": null,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

  --- Excepcion_los_limites_maximos_se_reduciran_a_11_y_8_respectivamente_cuando_la_entidad_fina (términos: ['12.3']) | expuesto en outputs de CQ-033: pasos [4, 5] ---
{
 "id": "Excepcion_los_limites_maximos_se_reduciran_a_11_y_8_respectivamente_cuando_la_entidad_fina",
 "type": "Excepcion",
 "label": "Reducción límite con calificación SEFYC 1-3",
 "properties": {
  "descripcion": "Los límites máximos se reducirán a 11% y 8%, respectivamente, cuando la entidad financiera cuente con calificación 1, 2 o 3 conforme a la valoración otorgada por la SEFYC"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ]
}

  --- Excepcion_se_consideran_admitidos_los_defectos_surgidos_de_la_conciliacion_trimestral_en_c (términos: ['12.3']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Excepcion_se_consideran_admitidos_los_defectos_surgidos_de_la_conciliacion_trimestral_en_c",
 "type": "Excepcion",
 "label": "Defectos admitidos por convergencia NIIF",
 "properties": {
  "descripcion": "Se consideran admitidos los defectos surgidos de la conciliación trimestral en convergencia a NIIF con informe de auditor externo, si de haberse considerado resultados positivos al 100% en lugar del 50% no se hubiera registrado tal defecto"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 12.3. Tratamiento de los defectos originados en el cómputo del 50 % –en lugar del 100"
  }
 ]
}
  D1 (reducido): {
 "portador": "Excepcion_se_consideran_admitidos_los_defectos_surgidos_de_la_conciliacion_trimestral_en_c",
 "alcanzable": false,
 "mejor_rank": 176,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

  --- Obligacion_de_reunir_los_requisitos_se_consignara_en_la_partida_60500000_la_porcion_pertine (términos: ['12.3']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Obligacion_de_reunir_los_requisitos_se_consignara_en_la_partida_60500000_la_porcion_pertine",
 "type": "Obligacion",
 "label": "Consignar neutralización en partida 60500000",
 "properties": {
  "descripcion": "De reunir los requisitos, se consignará en la partida 60500000 la porción pertinente para la neutralización del defecto generado",
  "tipo": "asignacion"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 12.3. Tratamiento de los defectos originados en el cómputo del 50 % –en lugar del 100"
  }
 ]
}
  D1 (reducido): {
 "portador": "Obligacion_de_reunir_los_requisitos_se_consignara_en_la_partida_60500000_la_porcion_pertine",
 "alcanzable": false,
 "mejor_rank": 232,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

  --- Obligacion_debera_presentarse_conciliacion_de_estados_contables_trimestrales_en_el_marco_de (términos: ['12.3']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Obligacion_debera_presentarse_conciliacion_de_estados_contables_trimestrales_en_el_marco_de",
 "type": "Obligacion",
 "label": "Presentar conciliación trimestral NIIF",
 "properties": {
  "descripcion": "Deberá presentarse conciliación de estados contables trimestrales en el marco de convergencia a NIIF que cuente con informe de auditor externo",
  "tipo": "presentacion_informativa",
  "plazo": "trimestral"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 12.3. Tratamiento de los defectos originados en el cómputo del 50 % –en lugar del 100"
  }
 ]
}
  D1 (reducido): {
 "portador": "Obligacion_debera_presentarse_conciliacion_de_estados_contables_trimestrales_en_el_marco_de",
 "alcanzable": false,
 "mejor_rank": 1642,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

  --- Obligacion_los_datos_se_informaran_con_frecuencia_trimestral_y_se_integraran_con_los_datos_ (términos: ['junio']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Obligacion_los_datos_se_informaran_con_frecuencia_trimestral_y_se_integraran_con_los_datos_",
 "type": "Obligacion",
 "label": "Informar frecuencia trimestral",
 "properties": {
  "descripcion": "Los datos se informarán con frecuencia trimestral y se integrarán con los datos correspondientes al último mes de cada trimestre (marzo, junio, septiembre y diciembre), sobre base individual y consolidada mensual",
  "tipo": "presentacion_informativa",
  "plazo": "trimestral"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 4. EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.)"
  }
 ]
}
  D1 (reducido): {
 "portador": "Obligacion_los_datos_se_informaran_con_frecuencia_trimestral_y_se_integraran_con_los_datos_",
 "alcanzable": false,
 "mejor_rank": 35,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

  --- Obligacion_se_considerara_la_ultima_calificacion_informada_para_el_calculo_de_la_exigencia_ (términos: ['12.3']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Obligacion_se_considerara_la_ultima_calificacion_informada_para_el_calculo_de_la_exigencia_",
 "type": "Obligacion",
 "label": "Considerar última calificación SEFYC",
 "properties": {
  "descripcion": "Se considerará la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación",
  "tipo": "calculo",
  "plazo": "tercer mes siguiente a la notificación"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ]
}
  D1 (reducido): {
 "portador": "Obligacion_se_considerara_la_ultima_calificacion_informada_para_el_calculo_de_la_exigencia_",
 "alcanzable": false,
 "mejor_rank": 94,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

  --- Obligacion_se_consignara_como_numero_y_fecha_de_resolucion_la_de_la_comunicacion_a_6456_y_s (términos: ['12.3']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Obligacion_se_consignara_como_numero_y_fecha_de_resolucion_la_de_la_comunicacion_a_6456_y_s",
 "type": "Obligacion",
 "label": "Registrar datos de Resolución y cálculo",
 "properties": {
  "descripcion": "Se consignará como 'número' y 'fecha de Resolución' la de la Comunicación A 6456, y se agregará una descripción detallada del cálculo del importe para el período informado",
  "tipo": "presentacion_informativa"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 12.3. Tratamiento de los defectos originados en el cómputo del 50 % –en lugar del 100"
  }
 ]
}
  D1 (reducido): {
 "portador": "Obligacion_se_consignara_como_numero_y_fecha_de_resolucion_la_de_la_comunicacion_a_6456_y_s",
 "alcanzable": false,
 "mejor_rank": 170,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

  --- Operacion_adquisicion_con_caracter_transitorio_de_participaciones_en_empresas_para_facilit (términos: ['transitoria']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Operacion_adquisicion_con_caracter_transitorio_de_participaciones_en_empresas_para_facilit",
 "type": "Operacion",
 "label": "Adquisición transitoria participaciones",
 "properties": {
  "tipo": "Adquisición con carácter transitorio de participaciones en empresas para facilitar su desarrollo, con la finalidad de vender posteriormente las tenencias"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.6. de las citadas normas. (parte 1)"
  }
 ]
}
  D1 (reducido): {
 "portador": "Operacion_adquisicion_con_caracter_transitorio_de_participaciones_en_empresas_para_facilit",
 "alcanzable": false,
 "mejor_rank": 1682,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

  --- Operacion_ajuste_contable_por_convergencia_a_niif (términos: ['12.3']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Operacion_ajuste_contable_por_convergencia_a_niif",
 "type": "Operacion",
 "label": "Ajustes NIIF por primera vez",
 "properties": {
  "tipo": "ajuste contable por convergencia a NIIF"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 12.3. Tratamiento de los defectos originados en el cómputo del 50 % –en lugar del 100"
  }
 ]
}
  D1 (reducido): {
 "portador": "Operacion_ajuste_contable_por_convergencia_a_niif",
 "alcanzable": false,
 "mejor_rank": 1372,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

  --- Operacion_calculo (términos: ['12.3']) | expuesto en outputs de CQ-033: pasos [1, 2, 4] ---
{
 "id": "Operacion_calculo",
 "type": "Operacion",
 "label": "Cálculo exigencia capital riesgo operacional",
 "properties": {
  "tipo": "cálculo",
  "description": "Cálculo de K (exigencia de capital promedio de las exposiciones subyacentes); es decir, el ratio entre la suma de las exposiciones subyacentes ponderadas por riesgo y la suma de las exposiciones subyacentes, todo multiplicado por 8%."
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ]
}

  --- Operacion_calculo_de_resultados_de_ajustes_niif (términos: ['12.3']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Operacion_calculo_de_resultados_de_ajustes_niif",
 "type": "Operacion",
 "label": "Cómputo de resultados NIIF",
 "properties": {
  "tipo": "cálculo de resultados de ajustes NIIF"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 12.3. Tratamiento de los defectos originados en el cómputo del 50 % –en lugar del 100"
  }
 ]
}
  D1 (reducido): {
 "portador": "Operacion_calculo_de_resultados_de_ajustes_niif",
 "alcanzable": false,
 "mejor_rank": 2741,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

  --- Operacion_presentacion_de_informacion_contable_trimestral (términos: ['12.3']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Operacion_presentacion_de_informacion_contable_trimestral",
 "type": "Operacion",
 "label": "Presentación de estados contables",
 "properties": {
  "tipo": "presentación de información contable trimestral"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 12.3. Tratamiento de los defectos originados en el cómputo del 50 % –en lugar del 100"
  }
 ]
}
  D1 (reducido): {
 "portador": "Operacion_presentacion_de_informacion_contable_trimestral",
 "alcanzable": false,
 "mejor_rank": 3004,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

  --- Operacion_reclasificacion (términos: ['12.3']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Operacion_reclasificacion",
 "type": "Operacion",
 "label": "Reclasificación de entidad financiera",
 "properties": {
  "tipo": "reclasificación"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ]
}
  D1 (reducido): {
 "portador": "Operacion_reclasificacion",
 "alcanzable": false,
 "mejor_rank": 121,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

  --- Restriccion_aplicacion_de_ccf_del_0_desde_01_01_25_al_30_06_25_y_del_5_desde_01_07_25_al_31_ (términos: ['30/06']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Restriccion_aplicacion_de_ccf_del_0_desde_01_01_25_al_30_06_25_y_del_5_desde_01_07_25_al_31_",
 "type": "Restriccion",
 "label": "Aplicación de CCF por período",
 "properties": {
  "tipo": "limite_cuantitativo",
  "descripcion": "Aplicación de CCF del 0% desde 01/01/25 al 30/06/25 y del 5% desde 01/07/25 al 31/12/25",
  "description": "Desde el 01/01/25 y hasta el 31/12/25, las entidades financieras clasificadas en el grupo 2 que al 01/01/25 pertenezcan a los grupos B y C deberán convertir los compromisos mediante la aplicación de los CCF de acuerdo con el siguiente cronograma: 01/01/25 al 30/06/25 0%; 01/07/25 al 31/12/25 5%"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.2. Desde el 01/01/25 y hasta el 31/12/25, las entidades financieras clasificadas en"
  }
 ]
}
  D1 (reducido): {
 "portador": "Restriccion_aplicacion_de_ccf_del_0_desde_01_01_25_al_30_06_25_y_del_5_desde_01_07_25_al_31_",
 "alcanzable": false,
 "mejor_rank": 483,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

  --- Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ (términos: ['30/06', '12.3']) | expuesto en outputs de CQ-033: pasos [1, 2, 3, 4, 7] ---
{
 "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
 "type": "Restriccion",
 "label": "Límite exigencia capital operacional grupo B",
 "properties": {
  "descripcion": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta el 30/06/26 no podrá superar el 17% del promedio de los últimos 36 meses",
  "tipo": "limite_cuantitativo",
  "umbral": "17%"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ]
}

  --- Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_c_determ (términos: ['30/06', '12.3']) | expuesto en outputs de CQ-033: pasos [1, 2, 7] ---
{
 "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_c_determ",
 "type": "Restriccion",
 "label": "Límite exigencia capital operacional grupo C",
 "properties": {
  "descripcion": "La exigencia de capital por riesgo operacional para entidades del grupo C determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta el 30/06/26 no podrá superar el 14% del promedio de los últimos 36 meses",
  "tipo": "limite_cuantitativo",
  "umbral": "14%"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ]
}

  --- Restriccion_los_resultados_provenientes_de_ajustes_niif_por_primera_vez_dentro_de_la_rpc_se_ (términos: ['12.3']) | expuesto en outputs de CQ-033: NO ---
{
 "id": "Restriccion_los_resultados_provenientes_de_ajustes_niif_por_primera_vez_dentro_de_la_rpc_se_",
 "type": "Restriccion",
 "label": "Limitación cómputo al 50% resultados NIIF",
 "properties": {
  "descripcion": "Los resultados provenientes de ajustes NIIF por primera vez dentro de la RPC se cómputan al 50% en lugar del 100% en el período enero-marzo 2018",
  "tipo": "limite_cuantitativo",
  "umbral": "50%"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 12.3. Tratamiento de los defectos originados en el cómputo del 50 % –en lugar del 100"
  }
 ]
}
  D1 (reducido): {
 "portador": "Restriccion_los_resultados_provenientes_de_ajustes_niif_por_primera_vez_dentro_de_la_rpc_se_",
 "alcanzable": false,
 "mejor_rank": 197,
 "n_consultas_simuladas": 30,
 "consultas_en_top10": []
}

==============================================================================
4. CQ-016 — backlog: portador del hecho identitario
==============================================================================

  'exigencia e integracion': 0 candidato/s en id/label/properties

  'seccion 4': 2 candidato/s en id/label/properties
  --- Restriccion_en_la_relacion_de_activos_inmovilizados_y_otros_conceptos_seccion_4_del_respecti ---
{
 "id": "Restriccion_en_la_relacion_de_activos_inmovilizados_y_otros_conceptos_seccion_4_del_respecti",
 "type": "Restriccion",
 "label": "Límite de activos inmovilizados",
 "properties": {
  "descripcion": "en la relación de activos inmovilizados y otros conceptos (Sección 4. del respectivo TO), excluidos los computados para la determinación del INC(inversiones significativas en empresas)",
  "tipo": "limite_cualitativo"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 4.1. DvP: operaciones de entrega contra pago fallidas (a los efectos de estas normas,"
  }
 ]
}
  --- Operacion_calculo_de_riesgo_de_mercado ---
{
 "id": "Operacion_calculo_de_riesgo_de_mercado",
 "type": "Operacion",
 "label": "Cálculo exigencia riesgo de mercado",
 "properties": {
  "tipo": "cálculo de riesgo de mercado",
  "description": "Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5. de la Sección 4.) en base individual y consolidado mensual (códigos de consolidación 0 o 1 y 2)"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al m"
  }
 ]
}

  'apartado 4': 0 candidato/s en id/label/properties

  'r.i.-c.m.': 0 candidato/s en id/label/properties
```

## Tabla resumen — verificación × resultado

| # | Verificación | Resultado (hechos; evidencia en el output de arriba) |
|---|---|---|
| 1a | CQ-018: "énfasis"/"flujos de fondos" en outputs | **EXPUESTOS** — "enfasis" paso 12; "flujos de fondos" paso 12 (×2); "flujo de fondos" pasos 9, 11 y 12 |
| 1b | CQ-018: "atender adecuadamente"/"todos sus compromisos" | **EXPUESTOS** — ambos en pasos 11 y 12 |
| 1c | CQ-018: portadores en kg | El portador de "atender adecuadamente"+"todos sus compromisos" es `Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien`, **expuesto (pasos 11, 12)**. Los demás candidatos de los términos (contenido íntegro pegado) figuran con su exposición; los NO expuestos llevan su D1 reducido |
| 2a | CQ-019: "31 dias"/"puntual"/"situacion normal" en outputs | **EXPUESTOS** — "31 dias" paso 7; "puntual" paso 7 (×2); "situacion normal" pasos 2, 4 y 7 |
| 2b | CQ-019: portadores de la definición | Los dos portadores con texto definicional — `Restriccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones` y `Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien` — **expuestos en el paso 7**; descripciones completas transcriptas en el output (la lectura 7.2.1-consumo vs 6.5.1-comercial queda fuera: solo texto). Candidatos no expuestos con D1 |
| 3a | CQ-033: origen del "hasta el 30/06/26" en outputs | **"30/06" EXPUESTO — paso 3**, fragmento: "…la expresion descripta en el punto 7.2. hasta el 30/06/26 no podra superar el 17% del promedio de los ultimos…". "12.3" expuesto en pasos 3-7 (siempre dentro de `location` de provenances en los outputs). "30-06"/"junio"/"vigente"/"vigencia"/"transitoria": AUSENTES |
| 3b | CQ-033: barrido kg | "30/06" en properties de **3 nodos** (los dos de exigencia por riesgo operacional grupo B/C + un CCF); "12.3" en **0 properties / 19 provenances**; "junio" 2, "transitoria" 1, "vigente" 33, "vigencia" 14 (ids listados). Candidatos específicos íntegros con exposición y D1 donde no expuestos |
| 4 | CQ-016 backlog: portador del hecho identitario | **"exigencia e integracion": 0 candidatos · "apartado 4": 0 · "r.i.-c.m.": 0.** "seccion 4": 2 candidatos (contenido íntegro pegado: un límite de activos inmovilizados de Capitales y el nodo de datos complementarios de riesgo de mercado del R.I.C.M.) |

## git status

```
$ git status --porcelain
 M docs/protocolo_piloto_v6.md
?? docs/evidencia_capa_d/verificacion_estructura_piloto.md
```

Los dos ítems son los entregables de la tarea anterior (enmienda v1.1 + copia de la
verificación estructural), aún sin commitear — **esta tarea no modificó nada en zona
tracked**; este reporte vive en `posthoc_run/dev_set/`, gitignored.

---

*Fin de las verificaciones. Sin adjudicación: los hechos quedan para la adjudicación de casos_piloto.md.*
