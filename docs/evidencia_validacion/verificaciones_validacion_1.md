# Verificaciones de la adjudicación de la validación — parte 1: run_2 (puntos 1, 2, 5)

Fecha: 2026-07-16. SOLO LECTURA; escrituras: este archivo y su parte 2. No se corrió
verificador ni capa. **Solo hechos — cero adjudicación.** Partido en dos por tamaño:
parte 1 = run_2 (CQ-025, CQ-019, CQ-018) · parte 2 = run_4 (CQ-017, CQ-020, CQ-019).

**Mecanismo:** el de las verificaciones del piloto — outputs completos re-ejecutados con
número de paso y NODO FUENTE por unidad (resultados[i]/nodo/edge), barridos normalizados
(lowercase, sin acentos) sobre id+label+properties del kg del run correspondiente
(provenances aparte donde se pide), y D1 (`evaluar_alcanzabilidad` con pregunta + consultas
reales del agente + tokens expuestos de ESA traza) sobre todo portador no expuesto.
**Regla declarada de volumen:** si un término da más de 12 candidatos, se listan todos los
ids y se pegan íntegros solo los que cruzan con los términos del punto (anotado en el
output como "regla declarada").

## Código (compartido por ambas partes, completo)

```python
# -*- coding: utf-8 -*-
"""Verificaciones de la adjudicación de la validación v6.1-D — barridos determinísticos
sobre run_2 y run_4. Solo hechos; cero adjudicación.
Mecanismo: el de verificaciones_piloto.md (outputs completos re-ejecutados con nº de paso,
barridos normalizados sobre id+label+properties del kg del run, provenances aparte donde se
pide, D1 sobre portadores no expuestos)."""
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

IDX = {r: harness.GraphIndex(loader.load_graph(r)) for r in ("run_2", "run_4")}

def trace_path(run, qid):
    return EVAL / f"posthoc_run/traces/off/{run}/{qid}.json"

_outs_cache = {}
def outputs_con_paso(run, qid):
    key = (run, qid)
    if key in _outs_cache:
        return _outs_cache[key]
    idx = IDX[run]
    tr = json.load(open(trace_path(run, qid)))[0]["trace"]
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
        out.append((s["n"], o))
    _outs_cache[key] = out
    return out

def unidades(paso, o):
    """(descriptor_con_nodo_fuente, texto_json) por unidad del output."""
    if "resultados" in o:
        for i, r in enumerate(o.get("resultados", []), 1):
            yield f"paso {paso} resultados[{i}] id={r['id']}", json.dumps(r, ensure_ascii=False)
    elif "salientes" in o or "entrantes" in o:
        for k in ("salientes", "entrantes"):
            for i, e in enumerate(o.get(k, []), 1):
                yield f"paso {paso} {k}[{i}] {e.get('relation')}→{e.get('vecino_id')}", json.dumps(e, ensure_ascii=False)
    else:
        yield f"paso {paso} nodo id={o.get('id', o.get('error'))}", json.dumps(o, ensure_ascii=False)

def exposicion(run, qid, rx_texto, rotulo, ancho=100, max_por_unidad=2):
    """Matches de la regex normalizada en las unidades de los outputs completos."""
    rx = re.compile(rx_texto)
    hits = 0
    print(f"  ['{rotulo}'] exposición en outputs de {run}/{qid}:")
    for paso, o in outputs_con_paso(run, qid):
        for desc, texto in unidades(paso, o):
            nt = norm(texto)
            ms = list(rx.finditer(nt))[:max_por_unidad]
            for m in ms:
                hits += 1
                a, b = max(0, m.start() - ancho // 2), min(len(nt), m.end() + ancho // 2)
                print(f"    {desc}\n       …{nt[a:b]}…")
    if not hits:
        print("    AUSENTE en todos los outputs completos")
    return hits

def blob_nodo(n):
    props = n.properties or {}
    return norm(f"{n.id} {n.label} " + " ".join(f"{k} {v}" for k, v in props.items()))

def blob_prov(n):
    return norm(json.dumps(n.provenances, ensure_ascii=False))

def dump(run, nid):
    n = IDX[run].by_id[nid]
    return json.dumps({"id": n.id, "type": n.type, "label": n.label,
                       "properties": n.properties, "provenances": n.provenances},
                      ensure_ascii=False, indent=1)

def edges_de(run, nid):
    idx = IDX[run]
    outs = idx.out_edges.get(nid, [])
    ins = idx.in_edges.get(nid, [])
    lines = [f"    edges de {nid}: {len(outs)} salientes, {len(ins)} entrantes"]
    for e in outs:
        lines.append("    SALIENTE: " + json.dumps({"relation": e.relation, "target": e.target,
                     "provenances": e.provenances}, ensure_ascii=False))
    for e in ins:
        lines.append("    ENTRANTE: " + json.dumps({"relation": e.relation, "source": e.source,
                     "provenances": e.provenances}, ensure_ascii=False))
    return "\n".join(lines)

def expuesto_en(run, qid, nid):
    return [paso for paso, o in outputs_con_paso(run, qid) if nid in json.dumps(o, ensure_ascii=False)]

def d1(run, qid, nid):
    tr = json.load(open(trace_path(run, qid)))[0]["trace"]
    consultas = [s["input"]["consulta"] for s in tr["steps"] if s.get("tool") == "buscar_nodos"]
    toks = tokens_expuestos_de_trace(trace_path(run, qid), index=IDX[run])
    r = evaluar_alcanzabilidad(nid, tr["question"], consultas, toks, IDX[run])
    ranks = [c["rank"] for c in r["consultas"] if c["rank"] is not None]
    top = [{"consulta": c["consulta"], "rank": c["rank"]} for c in r["consultas"] if c["en_top10"]]
    return {"alcanzable": r["alcanzable"], "mejor_rank": min(ranks) if ranks else None,
            "n_consultas": r["n_consultas_simuladas"], "top10": top[:4]}

CAP = 12
def barrido(run, qid, rx_props, rotulo, rx_provs=None, con_edges=False, con_d1=True,
            terminos_cruce=None):
    """Barrido del kg del run. Si >CAP candidatos: ids + íntegros solo para los que crucen
    con terminos_cruce (regla declarada). Reporta exposición y D1 sobre no expuestos."""
    kg = IDX[run].kg
    rp = re.compile(rx_props)
    cand_p = [n.id for n in kg.nodes if rp.search(blob_nodo(n))]
    cand_v = []
    if rx_provs is not None:
        rv = re.compile(rx_provs)
        cand_v = [n.id for n in kg.nodes if not rp.search(blob_nodo(n)) and rv.search(blob_prov(n))]
    print(f"  [barrido kg {run}: '{rotulo}'] en id/label/properties: {len(cand_p)}"
          + (f" | SOLO en provenances: {len(cand_v)}" if rx_provs is not None else ""))
    todos = cand_p + cand_v
    if len(todos) > CAP and terminos_cruce:
        rc = re.compile(terminos_cruce)
        integros = [nid for nid in todos if rc.search(blob_nodo(IDX[run].by_id[nid]))]
        print(f"    (> {CAP} candidatos: regla declarada — ids completos abajo; íntegros solo los que cruzan con '{terminos_cruce}': {len(integros)})")
        print(f"    ids: {todos}")
    else:
        integros = todos
    for nid in integros:
        exp = expuesto_en(run, qid, nid)
        origen = "props" if nid in cand_p else "SOLO provenance"
        print(f"\n  --- {nid} ({origen}) | expuesto en outputs de {qid}: {('pasos ' + str(exp)) if exp else 'NO'} ---")
        print(dump(run, nid))
        if con_edges:
            print(edges_de(run, nid))
        if con_d1 and not exp:
            print("    D1:", json.dumps(d1(run, qid, nid), ensure_ascii=False))
    return todos, integros

SEP = "=" * 78

# =====================================================================
# LOG RUN_2 (puntos 1, 2, 5)
# =====================================================================
log2 = open("/private/tmp/claude-501/-Users-agustinavidelarivero-INGENIERIA-IA-TESIS-bcra-regulatory-kg/ae126db0-6781-4d0f-9181-b36bcb16486c/scratchpad/verif_val_run2.txt", "w")
sys.stdout = log2

print(f"{SEP}\n1. run_2/CQ-025 ({len(outputs_con_paso('run_2','CQ-025'))} outputs re-ejecutables)\n{SEP}")
print("\n[1a] exposición de 'mensual':")
exposicion("run_2", "CQ-025", r"mensual", "mensual", max_por_unidad=3)
print("\n[1b] kg run_2: mercado + {mensual|frecuencia|periodicidad}:")
barrido("run_2", "CQ-025", r"(?=.*mercado)(?=.*(mensual|frecuencia|periodicidad))", "mercado ∧ frecuencia-términos")
print("\n[1c-i] kg run_2: trimestral + {mercado|excepcion|4.3|4.4|4.5}:")
barrido("run_2", "CQ-025", r"(?=.*trimestral)(?=.*(mercado|excepcion|4\.3|4\.4|4\.5))", "trimestral ∧ cruce")
print("\n[1c-ii] kg run_2: frecuencia general del régimen:")
barrido("run_2", "CQ-025", r"frecuencia mensual|presentacion de las informaciones|periodicidad", "frecuencia general")

print(f"\n{SEP}\n2. run_2/CQ-019 ({len(outputs_con_paso('run_2','CQ-019'))} outputs)\n{SEP}")
print("\n[2a-i] 'sin deducir' / 'no se deduce':")
t1, _ = barrido("run_2", "CQ-019", r"sin deducir|no se deduce", "sin deducir|no se deduce", con_edges=True)
print("\n[2a-ii] prevision ∧ incobrabilidad:")
t2, _ = barrido("run_2", "CQ-019", r"(?=.*prevision)(?=.*incobrabilidad)", "prevision ∧ incobrabilidad",
                con_edges=True, terminos_cruce=r"sin deducir|no se deduce|situacion normal|garantias preferidas")
print("\n[2a-iii] situacion normal ∧ prevision:")
t3, _ = barrido("run_2", "CQ-019", r"(?=.*situacion normal)(?=.*prevision)", "situacion normal ∧ prevision", con_edges=True)
print("\n[2a-iv] 'garantias preferidas':")
t4, _ = barrido("run_2", "CQ-019", r"garantias preferidas", "garantias preferidas",
                terminos_cruce=r"prevision|deduc|situacion normal")
print("\n[2a-v] '2.3.1' (props / provenances aparte):")
barrido("run_2", "CQ-019", r"(?<![\d.])2\.3\.1(?!\d)", "2.3.1", rx_provs=r"(?<![\d.])2\.3\.1(?!\d)", con_edges=True)
print("\n[2d] vínculo a la clasificación en candidatos de 2a-i/iii (contenido con 6.5.1/7.2.1/'situacion normal'):")
for nid in sorted(set(t1) | set(t3)):
    b = blob_nodo(IDX["run_2"].by_id[nid])
    marcas = [t for t in ("6.5.1", "7.2.1", "situacion normal") if t in b]
    print(f"  {nid}: contiene {marcas if marcas else 'ninguno de los tres'} en props")

print(f"\n{SEP}\n5. run_2/CQ-018 ({len(outputs_con_paso('run_2','CQ-018'))} outputs)\n{SEP}")
print("\n[5a] exposición de los términos guía de los 8 reprobados:")
GUIAS_18 = [("reclamos", r"reclamos"), ("resolver fundadamente", r"resolver fundadamente|resolucion fundada"),
            ("capacidad de pago", r"capacidad de pago"), ("flujo de fondos", r"flujo de fondos|flujos de fondos"),
            ("morosidad", r"morosidad"), ("situacion juridica", r"situacion juridica"),
            ("refinanciac*", r"refinanciac"), ("informacion+productos", r"informacion sobre (los )?productos|productos y servicios"),
            ("publicar+contratos", r"publicar|contratos de adhesion")]
nodos_fuente_18 = set()
for rot, rx in GUIAS_18:
    print()
    n_hits = exposicion("run_2", "CQ-018", rx, rot)
    if n_hits:
        rxc = re.compile(rx)
        for paso, o in outputs_con_paso("run_2", "CQ-018"):
            for desc, texto in unidades(paso, o):
                if rxc.search(norm(texto)):
                    m = re.search(r'id=([A-Za-z0-9_]+)', desc)
                    if m: nodos_fuente_18.add(m.group(1))
print("\n[5b] contenido ÍNTEGRO de los nodos fuente identificados en 5a:")
for nid in sorted(nodos_fuente_18):
    if nid in IDX["run_2"].by_id:
        print(f"\n  --- {nid} ---")
        print(dump("run_2", nid))
print("\n[5c-i] kg run_2: emisoras ∧ clasific*:")
barrido("run_2", "CQ-018", r"(?=.*emisoras)(?=.*clasific)", "emisoras ∧ clasific")
print("\n[5c-ii] kg run_2: '10.1' (props / provenances aparte):")
barrido("run_2", "CQ-018", r"(?<![\d.])10\.1(?![\d])", "10.1", rx_provs=r"(?<![\d.])10\.1(?![\d])",
        terminos_cruce=r"clasific|emisoras|proveedores")
print("\n[5c-iii] nodo de clasificación-PNFC usado por la respuesta (mora + consumo/vivienda):")
barrido("run_2", "CQ-018", r"(?=.*mora)(?=.*(consumo|vivienda))", "mora ∧ consumo|vivienda")

# =====================================================================
# LOG RUN_4 (puntos 3, 4, 6)
# =====================================================================
log2.close()
log4 = open("/private/tmp/claude-501/-Users-agustinavidelarivero-INGENIERIA-IA-TESIS-bcra-regulatory-kg/ae126db0-6781-4d0f-9181-b36bcb16486c/scratchpad/verif_val_run4.txt", "w")
sys.stdout = log4

print(f"{SEP}\n3. run_4/CQ-017 ({len(outputs_con_paso('run_4','CQ-017'))} outputs)\n{SEP}")
print("\n[3a] barridos kg run_4:")
c1, _ = barrido("run_4", "CQ-017", r"autorizad[ao]s? a operar en cambios|autorizadas a operar", "autorizadas a operar")
c2, _ = barrido("run_4", "CQ-017", r"deberan intervenir", "deberan intervenir")
c3, _ = barrido("run_4", "CQ-017", r"mercado libre de cambios", "mercado libre de cambios")
c4, _ = barrido("run_4", "CQ-017", r"\bcanje\b", "canje", terminos_cruce=r"cambio|mercado")
c5, _ = barrido("run_4", "CQ-017", r"\barbitraje\b", "arbitraje", terminos_cruce=r"cambio|mercado")
print("\n[3a-provs] nodos con provenance 'Punto 1.1' del TO Exterior (aparte):")
kg4 = IDX["run_4"].kg
prov_11 = [n.id for n in kg4.nodes
           if any("exterior" in norm(p.get("source_doc","")) and re.search(r"punto 1\.1(?!\d|\.\d)", norm(p.get("location","")))
                  for p in (n.provenances or []) if isinstance(p, dict))]
print(f"  {len(prov_11)} nodos: {prov_11}")
for nid in prov_11[:CAP]:
    print(f"\n  --- {nid} ---"); print(dump("run_4", nid))
print("\n[3b] nodos operador-de-cambio en run_4 (íntegros + TODOS sus edges) y chequeo 0-aristas:")
ops4 = [n.id for n in kg4.nodes if "operador de cambio" in blob_nodo(n) or "operador_de_cambio" in blob_nodo(n)]
print(f"  nodos operador-de-cambio: {len(ops4)}: {ops4}")
for nid in ops4:
    exp = expuesto_en("run_4", "CQ-017", nid)
    print(f"\n  --- {nid} | expuesto: {('pasos ' + str(exp)) if exp else 'NO'} ---")
    print(dump("run_4", nid)); print(edges_de("run_4", nid))
rx_b = re.compile(r"entidad(es)? autorizada|autorizad[ao]s? a operar|mercado de cambios|mercado libre de cambios")
def match_b(nid):
    n = IDX["run_4"].by_id.get(nid)
    return bool(n and rx_b.search(blob_nodo(n)))
aristas = []
for e in kg4.edges:
    if (e.source in ops4 and match_b(e.target)) or (e.target in ops4 and match_b(e.source)):
        aristas.append(e)
print(f"\n  aristas operador↔(entidad-autorizada|mercado-de-cambios) sobre {len(kg4.edges)} edges: {len(aristas)}")
for e in aristas:
    print("  " + json.dumps({"source": e.source, "relation": e.relation, "target": e.target,
                             "provenances": e.provenances}, ensure_ascii=False))
print("\n[3c] exposición y D1 de candidatos de 3a:")
for nid in sorted(set(c1) | set(c2) | set(c3)):
    exp = expuesto_en("run_4", "CQ-017", nid)
    print(f"  {nid}: expuesto={('pasos ' + str(exp)) if exp else 'NO'}")
    if not exp:
        print("    D1:", json.dumps(d1("run_4", "CQ-017", nid), ensure_ascii=False))
print("\n[3d] secundarios — exposición y nodos fuente:")
exposicion("run_4", "CQ-017", r"mercado libre de cambios", "mercado libre de cambios (output)")
exposicion("run_4", "CQ-017", r"no autorizadas", "'no autorizadas' (output)")
exposicion("run_4", "CQ-017", r"conformidad previa", "conformidad previa (output)", max_por_unidad=1)

print(f"\n{SEP}\n4. run_4/CQ-020 ({len(outputs_con_paso('run_4','CQ-020'))} outputs)\n{SEP}")
print("\n[4a] exposición:")
for rot, rx in [("sefyc", r"sefyc"), ("1,03", r"1,03"), ("1,08", r"1,08"), ("1,13", r"1,13"),
                ("1,19", r"1,19"), ("ponderadores", r"ponderadores"),
                ("activos computables", r"activos computables"),
                ("regimen informativo (∧capital anotado)", r"regimen informativo")]:
    print()
    exposicion("run_4", "CQ-020", rx, rot, max_por_unidad=1)
print("\n[4b-i] kg run_4: frecuencia/periodicidad/mensual ∧ credito|crc:")
b1, _ = barrido("run_4", "CQ-020", r"(?=.*(frecuencia|periodicidad|mensual))(?=.*(riesgo de credito|\bcrc\b))", "freq ∧ credito")
print("\n[4b-ii] kg run_4: frecuencia general del régimen:")
b2, _ = barrido("run_4", "CQ-020", r"frecuencia mensual|presentacion de las informaciones|periodicidad", "frecuencia general")
print("\n[4c-i] kg run_4: escala k ('1,19' | calificacion ∧ token k):")
b3, _ = barrido("run_4", "CQ-020", r"1,19", "1,19")
cal_k = [n.id for n in kg4.nodes if "calificacion" in blob_nodo(n) and "k" in IDX["run_4"]._node_tokens[n.id]]
print(f"  [calificacion ∧ token 'k']: {len(cal_k)}: {cal_k}")
for nid in cal_k[:CAP]:
    exp = expuesto_en("run_4", "CQ-020", nid)
    print(f"\n  --- {nid} | expuesto: {('pasos ' + str(exp)) if exp else 'NO'} ---")
    print(dump("run_4", nid))
    if not exp: print("    D1:", json.dumps(d1("run_4", "CQ-020", nid), ensure_ascii=False))
print("\n[4c-ii] kg run_4: 'ponderadores' | 'aprc':")
b4, _ = barrido("run_4", "CQ-020", r"ponderadores|(?<![a-z])aprc", "ponderadores|aprc",
                terminos_cruce=r"riesgo de credito|capital|activos computables")

print(f"\n{SEP}\n6. run_4/CQ-019 ({len(outputs_con_paso('run_4','CQ-019'))} outputs)\n{SEP}")
print("\n[6a] exposición de los términos guía de los 7 reprobados:")
GUIAS_19 = [("prevision especifica", r"prevision especifica"), ("monto bruto", r"monto bruto"),
            ("ksa", r"\bksa\b"), ("previsiones minimas", r"previsiones minimas"),
            ("totalidad de las financiaciones", r"totalidad de las financiaciones"),
            ("cinco categorias|categorias de riesgo", r"cinco categorias|categorias de riesgo"),
            ("criterios objetivos", r"criterios objetivos")]
nodos_fuente_19 = set()
for rot, rx in GUIAS_19:
    print()
    n_hits = exposicion("run_4", "CQ-019", rx, rot)
    if n_hits:
        rxc = re.compile(rx)
        for paso, o in outputs_con_paso("run_4", "CQ-019"):
            for desc, texto in unidades(paso, o):
                if rxc.search(norm(texto)):
                    m = re.search(r'id=([A-Za-z0-9_]+)', desc)
                    if m: nodos_fuente_19.add(m.group(1))
print("\n[6b] nodos fuente ÍNTEGROS — con titulizacion/securitizacion/3.1.11/ksa en PROPERTIES vs PROVENANCE (aparte):")
rx_tit = re.compile(r"titulizacion|securitizacion|3\.1\.11|\bksa\b")
for nid in sorted(nodos_fuente_19):
    if nid not in IDX["run_4"].by_id: continue
    n = IDX["run_4"].by_id[nid]
    en_props = bool(rx_tit.search(blob_nodo(n)))
    en_prov = bool(rx_tit.search(blob_prov(n)))
    print(f"\n  --- {nid} | titulizacion/securitizacion/3.1.11/ksa: PROPERTIES={en_props} · PROVENANCE={en_prov} ---")
    print(dump("run_4", nid))
print("\n[6c] kg run_4: portador del 2.3.1 correcto:")
barrido("run_4", "CQ-019", r"sin deducir|no se deduce", "sin deducir|no se deduce")
barrido("run_4", "CQ-019", r"(?=.*situacion normal)(?=.*prevision)", "situacion normal ∧ prevision")
barrido("run_4", "CQ-019", r"(?<![\d.])2\.3\.1(?!\d)", "2.3.1", rx_provs=r"(?<![\d.])2\.3\.1(?!\d)")

log4.close()
sys.stdout = sys.__stdout__
print("logs generados")
```

## Output completo — run_2

```
==============================================================================
1. run_2/CQ-025 (7 outputs re-ejecutables)
==============================================================================

[1a] exposición de 'mensual':
  ['mensual'] exposición en outputs de run_2/CQ-025:
    paso 1 resultados[4] id=procedimiento:regimen_informativo_contable_mensual
       …"id": "procedimiento:regimen_informativo_contable_mensual", "type": "procedimiento", "label": "regimen info…
    paso 1 resultados[4] id=procedimiento:regimen_informativo_contable_mensual
       …dimiento", "label": "regimen informativo contable mensual", "tokens_matcheados": 2, "resumen_propiedades": …
    paso 1 resultados[4] id=procedimiento:regimen_informativo_contable_mensual
       …men_propiedades": "['procedimiento de informacion mensual sobre exigencia e integracion de capitales minimo…
    paso 1 resultados[10] id=procedimiento:exigencia_e_integracion_de_capitales_minimos
       …men_propiedades": "['regimen informativo contable mensual que requiere el calculo y reporte de capitales mi…
    paso 2 resultados[8] id=obligacion:envio_mensual_de_datos_sobre_riesgo_de_mercado
       …{"id": "obligacion:envio_mensual_de_datos_sobre_riesgo_de_mercado", "type": "oblig…
    paso 2 resultados[8] id=obligacion:envio_mensual_de_datos_sobre_riesgo_de_mercado
       …e_mercado", "type": "obligacion", "label": "envio mensual de datos sobre riesgo de mercado", "tokens_matche…
    paso 2 resultados[8] id=obligacion:envio_mensual_de_datos_sobre_riesgo_de_mercado
       …propiedades": "complementar informacion con envio mensual de datos segun riesgo considerado."}…
    paso 4 nodo id=obligacion:informar_exigencia_por_riesgo_de_mercado
       … [{"source_doc": "to_regimen_informativo_contable_mensual_actual.pdf", "location": "seccion 7 > punto 8.1"}…
    paso 5 nodo id=obligacion:mantenimiento_de_frecuencia_trimestral_del_ratio_de_apalancamiento
       … [{"source_doc": "to_regimen_informativo_contable_mensual_actual.pdf", "location": "seccion 12 > punto 12.4…
    paso 6 nodo id=procedimiento:regimen_informativo_sobre_exigencia_e_integracion_de_capitales_minimos
       … [{"source_doc": "to_regimen_informativo_contable_mensual_actual.pdf", "location": "encabezado"}]}…
    paso 7 salientes[1] referencia→norma_referenciada:lineamientos_para_la_gestion_de_riesgos_en_las_entidades_financieras
       … [{"source_doc": "to_regimen_informativo_contable_mensual_actual.pdf", "location": "seccion 7 > punto 8.1"}…

[1b] kg run_2: mercado + {mensual|frecuencia|periodicidad}:
  [barrido kg run_2: 'mercado ∧ frecuencia-términos'] en id/label/properties: 12

  --- sujeto_regulado:entidad_financiera (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "sujeto_regulado:entidad_financiera",
 "type": "SujetoRegulado",
 "label": "entidad financiera",
 "properties": {
  "description": [
   "Sujeto regulado que debe cumplir con exigencias de capital mínimo bajo supervisión del BCRA.",
   "Sujeto obligado al cálculo y cumplimiento de exigencia de capital por riesgo de crédito conforme a la fórmula establecida.",
   "Sujeto regulado sobre cuya RPC se miden los límites de inversiones significativas.",
   "Entidad que otorga financiaciones y realiza operaciones en mercados de títulos valores, de monedas y de derivados.",
   "Entidad financiera que debe mantener exposiciones minoristas normativas diversificadas dentro de los límites regulados.",
   "Institución obligada a cumplir los límites de endeudamiento minorista y verificar información en operaciones de compra de cartera.",
   "Sujeto regulado responsable del otorgamiento y seguimiento de créditos hipotecarios.",
   "Organización que otorga créditos y mantiene exposiciones a deudores, responsable de evaluar situaciones de incumplimiento.",
   "Institución regulada sujeta a requisitos de capitales mínimos.",
   "Entidad regulada que participa en estructuras de titulización, puede ser originante, cedente o titular de posiciones.",
   "Persona jurídica que realiza operaciones de titulización y está sujeta a requisitos de capital mínimo.",
   "Entidad financiera que realiza operaciones de titulización y requiere calcular exigencia de capital.",
   "Institución sujeta a regulación de capitales mínimos por riesgo de crédito en inversiones en fondos.",
   "Entidad financiera que invierte en fondos y debe cumplir requisitos de capital.",
   "Institución financiera sujeta a las obligaciones de capital y seguimiento de riesgo de crédito de contraparte.",
   "Sujeto que debe constituir contratos de neteo y obtener opinión legal sobre exigibilidad del neteo en operaciones derivadas.",
   "Sujeto regulado que participa en operaciones de garantía y debe mantener capital mínimo.",
   "Sujeto que participa en operaciones con derivados y debe aplicar regulación de capitales mínimos.",
   "Sujeto obligado a calcular los parámetros de riesgo en instrumentos derivados.",
   "Entidad sujeta a regulación que puede tener exposición significativa al riesgo de base de productos.",
   "Sujeto regulado que debe cumplir con las exigencias de capital por exposición al riesgo de contraparte.",
   "Institución sujeta a requerimientos de capital mínimo por riesgo de crédito de contraparte.",
   "Institución sujeta a regulación de capitales mínimos que realiza operaciones con entidades de contraparte central.",
   "Entidad financiera sujeta a requisitos de capitalización mínima y regulaciones sobre exposiciones con contrapartes de compensación centralizada.",
   "Sujeto regulado obligado a cumplir requisitos de capital respecto de exposiciones con QCCP y CCP, y a aplicar ponderadores de riesgo a aportes de fondos de garantía.",
   "Entidad financiera sujeta a requisitos de capital y cobertura de riesgo de crédito.",
   "Institución financiera que contrata protección crediticia y asume garantías.",
   "Entidad financiera que aplica el método simple de cobertura mediante activos admitidos como garantía.",
   "Institución que realiza operaciones de pase y ejecuta procedimientos de liquidación y cobranza.",
   "Entidad financiera que realiza operaciones de financiación con títulos valores.",
   "Entidades financieras sujetas a regulación de capitales mínimos de riesgo de mercado.",
   "Sujeto regulado que posee derivados de crédito e instrumentos de crédito y debe cumplir exigencias de capital regulatorio.",
   "Sujeto regulado que debe cumplir exigencias de capital por riesgo de mercado en posiciones en acciones.",
   "Sujeto que realiza operaciones de derivados, índices y arbitraje sujeto a exigencias de capital mínimo.",
   "Sujeto regulado que utiliza derivados y mantiene posiciones en productos básicos.",
   "Sujeto regulado que debe cumplir con la determinación diaria de integración de capital según lo establecido en la norma.",
   "Institución financiera sujeta a los requisitos de capital mínimo y gestión de riesgos de mercado.",
   "Entidad sujeta a supervisión regulatoria que debe implementar marco de valuación prudente.",
   "Entidad sujeta a obligaciones de valuación de posiciones conforme a las metodologías establecidas.",
   "Entidades financieras sujetas a regulación de capitales mínimos.",
   "Institución financiera sujeta a los requisitos de capital mínimo establecidos por el BCRA.",
   "Entidad sujeta a requisitos de capital mínimo y obligaciones de divulgación de información regulatoria.",
   "Sujeto regulado obligado a computar el capital ordinario de nivel uno conforme a esta normativa.",
   "Institución sujeta a regulación de capitales mínimos por el BCRA.",
   "Sujeto regulado que debe cumplir con todos los requisitos y obligaciones relativos a instrumentos subordinados de capital.",
   "Entidad financiera sujeta a supervisión y regulación por el BCRA, incluyendo entidades y sus subsidiarias.",
   "Sujeto regulado que debe reconocer capital admisible emitido por subsidiarias sujetas a supervisión consolidada en su RPC.",
   "Sujeto regulado que realiza inversiones en capital de otras entidades financieras, empresas de servicios complementarios y compañías de seguro.",
   "Sujeto regulado a quien se aplican las reglas de deducción de capital por inversiones en otras entidades financieras.",
   "Sujeto regulado que integra y aumenta capital mediante aportes sujetos a estas normas.",
   "Sujeto regulado que debe implementar el proceso de mapping de calificaciones a ponderadores de riesgo.",
   "Personas jurídicas que otorgan financiaciones y deben clasificar a sus clientes.",
   "Entidad que cede créditos, otorga préstamos y realiza la clasificación de deudores.",
   "Instituciones financieras sujetas a las obligaciones de clasificación de deudores y previsionamiento reguladas por el BCRA.",
   "Institución financiera obligada a llevar legajo de cada deudor de su cartera y de sus corresponsales.",
   "Institución financiera responsable de la clasificación de deudores y la presentación de informes a la Superintendencia.",
   "Institución financiera responsable de clasificar su cartera según las categorías establecidas.",
   "Institución financiera responsable de clasificar deudores y realizar reevaluaciones de clasificación según los criterios establecidos.",
   "Institución que otorga financiaciones y clasifica clientes.",
   "Sujeto obligado a concertar acuerdos con deudores en mora y ejecutar procedimientos de clasificación.",
   "Institución financiera que otorga financiamiento y clasifica deudores según las normas del BCRA.",
   "Instituciones financieras obligadas a aplicar los criterios de clasificación de deudores y refinanciación establecidos en la norma.",
   "Entidad que asigna clasificación inicial al deudor y está obligada a recategorizar.",
   "Institución financiera sujeta a las obligaciones de reporte de incrementos de cartera irregular.",
   "Institución obligada a comunicar clasificaciones de deudores y cumplir normas de clasificación individual y consolidada.",
   "Sujeto regulado que debe cumplir con regímenes de clasificación de deudores y provisiones mínimas.",
   "Sujeto regulado que emite certificaciones de acceso al mercado de cambios.",
   "Intermediario responsable de verificar requisitos normativos antes de solicitar acceso al BCRA.",
   "Entidad que otorga acceso al mercado de cambios al cliente para operaciones de recompra, rescate y pago de gastos asociados.",
   "Entidad que otorga acceso al mercado de cambios a clientes para operaciones de recompra y rescate de títulos de deuda.",
   "Entidad que otorga acceso al mercado de cambios para pagos de capital e intereses mediante fideicomisos.",
   "Entidad financiera local que proporciona acceso al mercado de cambios para la operación.",
   "Entidad sujeta al deber de contar con conformidad del BCRA o requerir declaración jurada del cliente para acceso al mercado de cambios.",
   "Institución que actúa como intermediaria en operaciones de cambios y debe obtener conformidad o declaración jurada.",
   "Entidad regulada que debe realizar verificaciones y controles sobre operaciones de egresos de fondos al exterior.",
   "Entidad que actúa como intermediaria en operaciones de exportación y emisión de certificaciones.",
   "Intermediaria que canaliza operaciones a través del SML y debe cumplir requisitos.",
   "Entidad autorizada para registrar operaciones de cambio y emitir boletos de venta de cambio.",
   "Entidad que debe realizar el boleto de venta de cambio y obtener la documentación del cliente.",
   "Entidad financiera que realiza operaciones de liquidación de cobros de exportaciones y acceso a mercado de cambios bajo estos mecanismos.",
   "Institución financiera regulada que realiza operaciones con clientes.",
   "Persona jurídica que realiza operaciones en el mercado de cambios y debe registrarlas ante el BCRA.",
   "Entidad autorizada a elaborar boletos globales diarios según las condiciones establecidas en la norma.",
   "Entidad autorizada a recibir depósitos, mantener cuentas corresponsales y seguimiento de permisos de exportación.",
   "Institución financiera responsable de registrar operaciones y cumplir requisitos de ingreso y liquidación de divisas.",
   "Banco o institución de crédito elegible para ser designada por el exportador como responsable del seguimiento de operaciones de exportación.",
   "Entidad encargada del seguimiento de permisos de exportación y de realizar certificaciones y denuncias ante el BCRA.",
   "Entidad que debe cumplimentar el seguimiento de permisos de embarque y archivar documentación a disposición del BCRA.",
   "Entidad que opera en operaciones de comercio exterior y debe cumplir con requisitos de documentación.",
   "Entidad bancaria que autoriza y gestiona la imputación de descuentos, gastos y multas al permiso de embarque.",
   "Entidad regulada que debe cumplir obligaciones de documentación en operaciones de exportación.",
   "Entidad autorizada a operar en el mercado de cambios y registrar permisos de embarque.",
   "Entidad autorizada a emitir certificaciones de aplicación y seguimiento de operaciones de comercio exterior.",
   "Entidad autorizada a emitir certificaciones de aplicación de divisas en operaciones con el exterior.",
   "Entidad sujeta a las obligaciones de certificación, verificación y registro establecidas en la norma.",
   "Entidad financiera regulada por la normativa cambiaria del BCRA.",
   "Entidad que actúa como cliente en operaciones de cambio y debe efectuar boletos de venta según lo establecido en la norma.",
   "Entidad encargada de dar acceso al mercado de cambios y verificar cumplimiento de requisitos.",
   "Entidad autorizada a operar en el mercado de cambios y realizar pagos de importación.",
   "Entidades que operan en el mercado de cambios y deben cumplir requisitos de conformidad previa.",
   "Entidad financiera que emite u otorga cartas de crédito o letras avaladas para operaciones de importación.",
   "Entidad que accede al mercado de cambios para realizar pagos de importaciones y debe cumplir con obligaciones de registro e información.",
   "Entidad regulada que participa en operaciones de cambios y debe verificar requisitos.",
   "Institución que realiza el seguimiento del pago y registro en SEPAIMPO, y exige la documentación requerida.",
   "Entidad bancaria u otro intermediario que debe exigir documentación y declaraciones juradas para autorizar operaciones de importación con mora o insolvencia del proveedor.",
   "Entidad que debe verificar la separación de componentes de pago en operaciones de alquiler con opción de compra.",
   "Entidad financiera que otorga líneas de crédito del exterior para financiar importaciones de bienes y accede al mercado de cambios para su cancelación.",
   "Entidad sujeta a regulación que debe contar con declaración jurada del importador y opera en mercado de cambios.",
   "Institución que debe contar con documentación y requerimientos del cliente para operaciones de pago de deudas comerciales.",
   "Banco o institución financiera elegible para ser nominada por el importador para llevar a cabo el seguimiento de la oficialización de importación, salvo aquellas que hayan optado por no operar en comercio exterior.",
   "Entidad por donde se cursan los fondos y que debe certificar las devoluciones de pagos.",
   "Entidades financieras locales que intervienen en operaciones de cambios, financiamiento y garantías.",
   "Sujeto regulado responsable de verificar requisitos y acceder al mercado de cambios.",
   "Institución financiera que otorga crédito para financiar importaciones de servicios y accede al mercado de cambios.",
   "Entidad que opera en el mercado de cambios y otorga acceso a operaciones de cambio para proyectos RIGI.",
   "Entidad que otorga acceso al mercado de cambios y debe verificar requisitos complementarios.",
   "Institución financiera responsable de registrar aportes de capital en el régimen informático de operaciones de cambio (RIOC).",
   "Proveedor de servicios financieros que opera casas operativas y atiende usuarios.",
   "Sujeto regulado sometido al régimen informativo contable mensual de consolidación.",
   "Sujeto al que se aplica este régimen informativo de exigencia e integración de capitales mínimos.",
   "Sujeto obligado a cumplir con el régimen informativo contable mensual.",
   "Institución sujeta a obligaciones de información y cálculo de exigencias de capital.",
   "Sujeto regulado que debe reportar información contable mensual según régimen informativo.",
   "Sujeto obligado a cumplir requisitos de capitales mínimos y régimen informativo contable mensual.",
   "Sujeto obligado a realizar cálculos de valor económico del patrimonio y reportar información según régimen informativo contable mensual."
  ],
  "version": "vigente_2026-05",
  "modalidad": null
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Encabezado"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 1 > Punto 2.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.10"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 3.1 /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo /d"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Punto 3.2 /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Punto 4.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Punto 5.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo /b"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.3 /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.3 /b"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.5"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 7.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 10.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 7 > Punto 8.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.6"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 9 > Punto 10.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Encabezado"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 1.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 3.3"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 3.4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 3.5"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 5.1"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Punto 6.4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Punto 6.5"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo /b"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Punto 7.3"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Punto 7.4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 5593 /b"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.8"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 4 > Punto 4.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.7"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.8"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 7 > Punto 8.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 8 > Punto 8.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 9 > Sección 9 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Anexo d — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Punto 10.6"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Punto 10.7"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Punto 11.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 11 > Anexo d > Sección 11 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 13 > Anexo d > Sección 13 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 13 > Anexo d > Punto 13.4"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 13 > Anexo d > Punto 13.6"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Sección 14 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Punto 14.4"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 1 > Punto 1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 1 > Sección 1 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 9 > Sección 9 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 11 > Sección 11 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 27, "top10": []}

  --- sujeto_regulado:entidades_financieras (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "sujeto_regulado:entidades_financieras",
 "type": "SujetoRegulado",
 "label": "entidades financieras",
 "properties": {
  "description": [
   "Instituciones financieras sujetas a los requisitos de capitales mínimos y obligadas a presentar planes de regularización ante incumplimientos.",
   "Sujetos regulados sujetos a clasificación en grupos conforme a su importancia sistémica.",
   "Instituciones financieras sujetas a los requisitos de análisis de contrapartes y debida diligencia establecidos en la norma.",
   "Entidades financieras sujetas a la obligación de asignar ponderadores de riesgo conforme a las definiciones establecidas.",
   "Instituciones autorizadas a clasificar exposiciones minoristas normativas según categorías transaccionales o no transaccionales, y obligadas a comunicar esa clasificación a SEFyC.",
   "Instituciones financieras sometidas a regulación por el BCRA.",
   "Entidades financieras sujetas a regulación de capitales mínimos.",
   "Entidades sometidas a los requisitos de capital mínimo y ponderación de riesgo establecidos en la norma.",
   "Sujetos regulados que pueden aplicar neteo bilateral en operaciones con contrapartes sujetas a acuerdos de novación o formas legalmente válidas de neteo.",
   "Entidades obligadas a considerar sensibilidad y volatilidad de subyacentes en operaciones derivadas complejas.",
   "Entidades sujetas al cálculo de parámetros de segmentos CDO y aplicación de factores regulatorios.",
   "Entidades sujetas a regulación de capitales mínimos conforme a normas de capitales mínimos.",
   "Sujetos regulados que pueden tener exposiciones con entidades de contraparte central y considerar QCCP según normas de la CNV.",
   "Instituciones financieras sujetas a los requisitos de capital mínimo y técnicas de cobertura de riesgo de crédito.",
   "Entidades financieras sujetas a los requisitos de aplicación de técnicas de coberturas del riesgo de crédito.",
   "Participantes esenciales del mercado sujetos a requisitos de capital mínimo.",
   "Entidades sujetas a requisitos de capitales mínimos que utilizan método integral para cobertura de riesgo de crédito.",
   "Ente admisible como garante o proveedor de protección crediticia.",
   "Instituciones financieras sujetas a exigencias de capital por riesgo de mercado según régimen de capitales mínimos.",
   "Sujetos obligados al cálculo y cumplimiento de exigencias de capital por riesgo de tasa de interés y riesgo específico.",
   "Personas jurídicas sujetas a la regulación de capitales mínimos por riesgo de mercado.",
   "Sujetos regulados obligados a calcular y mantener capital mínimo por riesgo de tipo de cambio.",
   "Sujetos regulados que emplean posiciones en moneda extranjera y oro, sujetos a requisitos de capital mínimo por riesgo de mercado.",
   "Personas jurídicas sujetas a regulación de capitales mínimos por riesgo de posiciones en opciones.",
   "Sujetos regulados que operan con opciones y deben cumplir con las obligaciones de cálculo y reporte de capital mínimo.",
   "Instituciones sujetas a los lineamientos de valuación prudente de posiciones de menor liquidez.",
   "Instituciones sujetas a la regulación del BCRA que realizan valuaciones de activos.",
   "Entidades sujetas a las normas de capital regulatorio del BCRA.",
   "Personas jurídicas que operan en mercados financieros y están sujetas a regulación del BCRA.",
   "Personas jurídicas sujetas a las prescripciones de los artículos 30 y 32 de la Ley de Entidades Financieras respecto del cálculo de capital regulatorio.",
   "Instituciones financieras sujetas a supervisión y regulación del BCRA en materia de capitales mínimos.",
   "Sujetos regulados a los que aplican los límites mínimos de capital.",
   "Entidades financieras, comprendidas sus filiales en el país y en el exterior, sujetas a supervisión de capitales mínimos.",
   "Instituciones financieras sujetas a regulación de capitales mínimos y evaluación de riesgos crediticios.",
   "Personas jurídicas sujetas a regulación de capitales mínimos por el BCRA.",
   "Sujetos regulados a quienes se aplican los requisitos de capitales mínimos establecidos en el texto ordenado.",
   "Instituciones financieras sujetas a regulación del BCRA que otorgan financiaciones y mantienen legajos de clientes.",
   "Sujetos que deben aplicar los criterios de clasificación de deudores establecidos en la norma.",
   "Instituciones financieras autorizadas que intermedian operaciones de cambios.",
   "Instituciones financieras locales que operan en el mercado de cambios.",
   "Personas jurídicas autorizadas a operar en el mercado de cambios regulado por el BCRA.",
   "Instituciones financieras locales autorizadas a operar en el mercado de cambios.",
   "Instituciones autorizadas a dar acceso al mercado de cambios a personas humanas residentes.",
   "Entidades autorizadas a dar acceso al mercado de cambios a residentes en condiciones específicas.",
   "Entidades autorizadas para operar en el mercado de cambios y dar acceso a residentes.",
   "Personas jurídicas autorizadas a operar en el mercado de cambios y dar acceso a residentes.",
   "Instituciones autorizadas a realizar operaciones de canje y arbitraje con clientes.",
   "Instituciones financieras que cancelan líneas de crédito del exterior y acceden al mercado de cambios.",
   "Instituciones financieras locales responsables de cumplir obligaciones respecto de operaciones de egresos y elaboración de declaraciones juradas.",
   "Entidades autorizadas a operar en el mercado de cambios sin límite de horario.",
   "Instituciones financieras reguladas por el BCRA sujetas a normas sobre posición general de cambios.",
   "Entidades sujetas a las obligaciones de confección de boletos de cambio y registro de operaciones propias.",
   "Entidades financieras locales sujetas a las regulaciones de operaciones de cambio y divisas del BCRA.",
   "Instituciones autorizadas a acceder al mercado de cambios para realizar operaciones de importación y financiamiento.",
   "Instituciones que otorgan acceso al mercado de cambios y verifican requisitos para operaciones de importación.",
   "Instituciones que pueden dar acceso al mercado de cambios para operaciones de importación.",
   "Entidades autorizadas a dar acceso al mercado de cambios y canalizar pagos de servicios a no residentes.",
   "Entidades financieras que emiten u otorgan cartas de crédito o letras avaladas.",
   "Instituciones financieras autorizadas a otorgar acceso al mercado de cambios para egresos.",
   "Personas jurídicas autorizadas por el BCRA para realizar operaciones de cambio de manera permanente o habitual.",
   "Sujetos obligados que ofrecen servicios financieros a usuarios de servicios financieros.",
   "Instituciones financieras reguladas que deben cumplir obligaciones de accesibilidad para usuarios con discapacidad auditiva.",
   "Entidades financieras sujetas a las obligaciones de accesibilidad y renovación de infraestructura.",
   "Instituciones financieras obligadas a cumplir con requisitos mínimos en la relación de consumo.",
   "Instituciones financieras que ofrecen productos y servicios a usuarios de servicios financieros.",
   "Instituciones financieras sujetas a las obligaciones de información sobre comisiones y cargos.",
   "Entidades financieras que atienden a usuarios de servicios financieros y están sujetas a obligaciones de protección.",
   "Sujetos obligados a cumplir el régimen informativo contable mensual relativo a exigencias e integración de capitales mínimos.",
   "Personas jurídicas sujetas a las obligaciones de reporte de exigencia e integración de capitales mínimos.",
   "Entidades financieras sujetas a los requisitos informativos sobre capitales mínimos.",
   "Instituciones financieras del país y del exterior clasificadas en riesgo específico de tasa.",
   "Todas las entidades financieras están obligadas a cumplir este requerimiento de información.",
   "Personas jurídicas sujetas al régimen informativo contable mensual del BCRA.",
   "Entidades sujetas a la presentación de informaciones contables mensuales con códigos de consolidación según lo dispuesto en el régimen informativo."
  ],
  "version": "vigente_2026-05",
  "modalidad": null,
  "valor": null,
  "unidad": null,
  "duracion": null
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 1 > Sección 1 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.8"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 4 > Punto 5.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Punto 5.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Punto 6.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.4"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 2.4"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.6"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.10"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 10.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.11"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 7 > Punto 8.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.5"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.7"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 10 > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 10 > Punto 11.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 12 > Anexo Punto > Punto 2.12"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 6.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 2 > Punto 2.7"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.9"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.11"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.12"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.14"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.15"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.9"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.10"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.12"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 9 > Punto 10.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Punto 10.10"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 12 > Anexo d > Punto 13.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 13 > Anexo d > Punto 13.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Punto 14.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Punto 15.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 5 > Punto 1.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Punto 3"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Punto 2.3"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Punto 2.4"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Punto 2.5"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 3 > Punto 4.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 4 > Punto 4.3"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 9 > Punto 10.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 11 > Punto 3"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 12 > Punto 12.4"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 27, "top10": []}

  --- organismo_regulador:banco_central_de_la_republica_argentina (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "organismo_regulador:banco_central_de_la_republica_argentina",
 "type": "OrganismoRegulador",
 "label": "Banco Central de la República Argentina",
 "properties": {
  "description": [
   "Organismo que admite a las entidades de calificación crediticia externa (ECAI).",
   "Organismo regulador que establece y supervisa los requisitos de capitales mínimos y ponderadores de riesgo.",
   "Autoridad reguladora que establece los requisitos de capitales mínimos para entidades financieras.",
   "Autoridad reguladora que establece las normas sobre capitales mínimos y requisitos prudenciales.",
   "Autoridad emisora de instrumentos de regulación monetaria y supervisora de entidades financieras.",
   "Organismo regulador que establece y supervisa las exigencias de capital por riesgo de mercado.",
   "Institución que difunde tipos de cambio de referencia y comunica tipos de pase.",
   "Autoridad reguladora que emite normas sobre capitales mínimos de entidades financieras.",
   "Organismo regulador que supervisa el cálculo y presentación de capitales mínimos de entidades financieras.",
   "Organismo regulador que supervisa entidades financieras, rechaza planes de regularización, revoca autorizaciones y autoriza reestructuraciones.",
   "Autoridad monetaria responsable de supervisión, convenios de pagos y custodia de instrumentos de deuda pública.",
   "Organismo regulador que emite comunicaciones y supervisa entidades financieras.",
   "Organismo regulador que emite las normas sobre clasificación de deudores.",
   "Autoridad reguladora que emite las normas de clasificación de deudores.",
   "Organismo regulador que emite normas sobre clasificación de deudores.",
   "Organismo regulador que emite y supervisa las normas sobre clasificación de deudores.",
   "Autoridad emisora de las Comunicaciones que regulan la clasificación de deudores.",
   "Organismo regulador que emite comunicaciones y supervisa la clasificación de deudores en entidades financieras.",
   "BCRA, autoridad que autoriza a las entidades a operar en cambios y supervisa el mercado de cambios.",
   "Organismo regulador ante el cual se debe solicitar acceso al mercado de cambios.",
   "Autoridad que otorga conformidad previa para acceso al mercado de cambios.",
   "Organismo regulador que implementa y supervisa el sistema de registro de operaciones de cambios.",
   "Organismo supervisor que otorga conformidad para operaciones de cambio y mantiene sistema online de verificación.",
   "Autoridad reguladora que supervisa operaciones de cambio y puede requerir conformidad previa.",
   "Autoridad que requiere conformidad previa para operaciones de clientes no residentes con títulos valores.",
   "Autoridad reguladora responsable de la supervisión de operaciones de exterior y cambios.",
   "Supervisa y registra los cambios de entidad nominada responsable de certificaciones.",
   "Autoridad que supervisa y registra los cambios de entidades nominadas para la emisión de certificaciones de exportación.",
   "Autoridad reguladora que otorga conformidad previa para acceso al mercado de cambios.",
   "Implementador del Sistema de Monedas Locales (SML).",
   "Autoridad regulatoria que otorga conformidad previa para suscripción de BOPREAL.",
   "Autoridad reguladora que supervisa las operaciones de comercio exterior y cambios.",
   "Autoridad reguladora que supervisa operaciones de exterior y cambios.",
   "Organismo regulador que supervisa las operaciones y tiene disponibilidad de la documentación archivada.",
   "BCRA, organismo regulador que implementa sistemas online y otorga conformidad previa para operaciones.",
   "BCRA, organismo regulador que otorga conformidades previas y gestiona sistemas de validación de operaciones de cambios.",
   "BCRA que otorga conformidad previa y mantiene sistema de convalidación online para operaciones de cambio.",
   "BCRA que otorga conformidad previa para operaciones de cambios y supervisa operaciones reguladas.",
   "BCRA, organismo regulador que supervisa operaciones y otorga conformidades.",
   "Autoridad reguladora que autoriza entidades y personas para operar en el mercado de cambios y establece requisitos y reglamentación.",
   "Autoridad reguladora del mercado de cambios que establece condiciones, plazos y autorizaciones previas.",
   "Organismo regulador que supervisa la actuación de los sujetos obligados en materia de protección de usuarios de servicios financieros.",
   "Autoridad que elabora el régimen de transparencia e impone normas sobre protección de usuarios.",
   "Autoridad receptora de información sobre comisiones y cargos de productos financieros.",
   "Autoridad reguladora que supervisa el cumplimiento de obligaciones de protección de usuarios de servicios financieros.",
   "Autoridad reguladora que emite comunicaciones y establece regímenes informativos contables.",
   "Organismo regulador que establece el régimen informativo contable mensual de consolidación.",
   "Organismo regulador que emite la Comunicación 'A' 8396 sobre régimen informativo contable mensual.",
   "Organismo regulador que establece el régimen informativo contable mensual de exigencia e integración de capitales mínimos.",
   "Autoridad reguladora responsable de la exigencia e integración de capitales mínimos de entidades financieras.",
   "Autoridad que otorga franquicias y supervisa el régimen informativo contable mensual.",
   "Autoridad que emite las comunicaciones y normas sobre régimen informativo contable mensual.",
   "BCRA, organismo que comunica el tipo de pase para conversión de monedas.",
   "Organismo emisor del Régimen Informativo Contable Mensual.",
   "Organismo supervisor que establece y recibe la información contable mensual regulada.",
   "Organismo regulador emisor de la Comunicación A 6643 y del presente régimen informativo contable mensual.",
   "Organismo regulador que emite comunicaciones y exige régimen informativo contable mensual.",
   "Organismo regulador que emite comunicaciones y establece regímenes informativos contables mensuales.",
   "Autoridad reguladora que establece la exigencia de cálculo de medida de riesgo EVE.",
   "Autoridad reguladora que emite las comunicaciones y normas referenciadas."
  ],
  "version": "vigente_2026-05",
  "alt_labels": [
   "banco central de la república argentina"
  ]
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.5"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 3.1 /c"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.3 /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 2.4"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 10.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 7 > Punto 8.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 12 > Anexo Punto > Punto 12.3 /i"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Encabezado"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 1.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 2.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 1.1"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 6.5"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 5593 /b"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.8"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.9"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.14"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 4 > Punto 4.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 4 > Punto 4.7"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 7 > Punto 7.3"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 13 > Anexo d > Sección 13 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Sección 14 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Punto 15.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Punto 15.2"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 5 > Punto 1.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Punto 2.5"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 3 > Punto 2.3"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Encabezado"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 1 > Sección 1 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 4 > Punto 5.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 6 > Punto 7.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 10 > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 10 > Punto 11.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 11 > Sección 11 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 11 > Punto 11.2"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 11 > Punto 12.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 970, "n_consultas": 27, "top10": []}

  --- requisito:valuacion_diaria_a_precios_de_mercado (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "requisito:valuacion_diaria_a_precios_de_mercado",
 "type": "Requisito",
 "label": "valuación diaria a precios de mercado",
 "properties": {
  "description": [
   "Condición técnica que aplica a operaciones con derivados para determinar períodos de mantenimiento mínimo.",
   "Requisito para aplicación de aforos regulatorios en el método integral.",
   "Los activos en garantía deben ser valuados diariamente a precios de mercado para determinar ajustes de aforo.",
   "Las posiciones deben valuarse a precios de mercado al menos diariamente, o evaluarse con periodicidad diaria en caso de valuación a modelo."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 7.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 43, "n_consultas": 27, "top10": []}

  --- requisito:valuacion_a_precios_de_mercado_con_frecuencia_minima_mensual (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "requisito:valuacion_a_precios_de_mercado_con_frecuencia_minima_mensual",
 "type": "Requisito",
 "label": "valuación a precios de mercado con frecuencia mínima mensual",
 "properties": {
  "description": "El activo recibido en garantía deberá contar con una valuación a precios de mercado con una frecuencia mínima mensual.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Punto 5.3"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 9, "n_consultas": 27, "top10": [{"consulta": "frecuencia se", "rank": 9}, {"consulta": "frecuencia se informa", "rank": 9}]}

  --- requisito:politicas_y_procedimientos_documentados_para_valuacion (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "requisito:politicas_y_procedimientos_documentados_para_valuacion",
 "type": "Requisito",
 "label": "políticas y procedimientos documentados para valuación",
 "properties": {
  "description": "Incluye definición clara de responsabilidades, fuentes de información de mercado, guías para datos no observables, frecuencia de valuaciones independientes, ajustes y procedimientos de verificación ad-hoc y mensuales.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 10.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 4135, "n_consultas": 27, "top10": []}

  --- obligacion:realizar_verificacion_de_precios_con_periodicidad_minima_mensual (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "obligacion:realizar_verificacion_de_precios_con_periodicidad_minima_mensual",
 "type": "Obligacion",
 "label": "realizar verificación de precios con periodicidad mínima mensual",
 "properties": {
  "description": "La verificación de precios de mercado o datos del modelo debe llevarse a cabo al menos con periodicidad mensual, o de forma más frecuente según la naturaleza del mercado o actividad de negociación.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1876, "n_consultas": 27, "top10": []}

  --- obligacion:exigencia_de_capital_operacional_mes_1_nuevas_entidades (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "obligacion:exigencia_de_capital_operacional_mes_1_nuevas_entidades",
 "type": "Obligacion",
 "label": "exigencia de capital operacional mes 1 nuevas entidades",
 "properties": {
  "description": "La exigencia mensual de capital mínimo por riesgo operacional en el primer mes será equivalente al 10% de la sumatoria de exigencias por riesgos de crédito y mercado.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 7 > Punto 7.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 76, "n_consultas": 27, "top10": []}

  --- requisito:declaracion_jurada_del_cliente (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "requisito:declaracion_jurada_del_cliente",
 "type": "Requisito",
 "label": "declaración jurada del cliente",
 "properties": {
  "description": [
   "Requisito de que el cliente declare jurada y expresamente tener conocimiento de que los fondos serán computados para el cálculo de límites aplicables.",
   "Documento requerido cuando se utiliza efectivo, en el cual el cliente declara bajo juramento el cumplimiento del requisito de límite mensual.",
   "Documento en el cual el cliente declara que cumple con los requisitos establecidos para acceder al mercado de cambios.",
   "Cliente debe declarar que la operación corresponde al SML y cumple disposiciones aplicables.",
   "El cliente debe presentar declaración jurada acreditando que la deuda está pendiente de pago y que no ha utilizado previamente este mecanismo por esa deuda.",
   "Declaración jurada del cliente que conste el monto suscripto del BOPREAL Serie 1, montos de deudas comerciales elegibles y que el pago queda encuadrado en límites previstos.",
   "Documento que debe constar que los cobros corresponden a exportaciones de bienes relacionadas con economía del conocimiento.",
   "Declaración jurada comprometiéndose a demostrar registro de ingreso aduanero en plazo correspondiente o proceder a liquidación en mercado de cambios.",
   "La entidad debe contar con declaración jurada que certifique el registro de deudas y el cumplimiento de límites de pago.",
   "Cliente debe acreditar que bienes no clasificados como de capital son repuestos, accesorios o materiales necesarios para funcionamiento, construcción o instalación de bienes de capital."
  ],
  "version": "vigente_2026-05",
  "modalidad": null
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 2 > Punto 2.7"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.8"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.9"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 4 > Punto 4.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 13 > Anexo d > Sección 13 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Sección 14 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 27, "top10": []}

  --- obligacion:presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "obligacion:presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado",
 "type": "Obligacion",
 "label": "presentación trimestral de datos complementarios de riesgo de mercado",
 "properties": {
  "description": "Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado se presentarán con frecuencia trimestral con datos del último mes de cada trimestre.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 12 > Punto 1.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 22, "n_consultas": 27, "top10": []}

  --- obligacion:envio_mensual_de_datos_sobre_riesgo_de_mercado (props) | expuesto en outputs de CQ-025: pasos [2] ---
{
 "id": "obligacion:envio_mensual_de_datos_sobre_riesgo_de_mercado",
 "type": "Obligacion",
 "label": "envío mensual de datos sobre riesgo de mercado",
 "properties": {
  "description": "Complementar información con envío mensual de datos según riesgo considerado.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 4 > Punto 4.3"
  }
 ]
}

  --- plazo:periodo_mensual_de_informacion (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "plazo:periodo_mensual_de_informacion",
 "type": "Plazo",
 "label": "período mensual de información",
 "properties": {
  "description": "Período mensual para el cual se determina la exigencia por riesgo de mercado al último día.",
  "unidad": "mes",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 11 > Punto 12.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 12, "n_consultas": 27, "top10": []}

[1c-i] kg run_2: trimestral + {mercado|excepcion|4.3|4.4|4.5}:
  [barrido kg run_2: 'trimestral ∧ cruce'] en id/label/properties: 1

  --- obligacion:presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "obligacion:presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado",
 "type": "Obligacion",
 "label": "presentación trimestral de datos complementarios de riesgo de mercado",
 "properties": {
  "description": "Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado se presentarán con frecuencia trimestral con datos del último mes de cada trimestre.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 12 > Punto 1.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 22, "n_consultas": 27, "top10": []}

[1c-ii] kg run_2: frecuencia general del régimen:
  [barrido kg run_2: 'frecuencia general'] en id/label/properties: 18

  --- plazo:frecuencia_minima_anual (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "plazo:frecuencia_minima_anual",
 "type": "Plazo",
 "label": "frecuencia mínima anual",
 "properties": {
  "description": "La debida diligencia debe realizarse con periodicidad anual como mínimo.",
  "unidad": "anual",
  "duracion": "mínimo una vez por año",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.4"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 1, "n_consultas": 27, "top10": [{"consulta": "minimos frecuencia", "rank": 1}, {"consulta": "frecuencia se", "rank": 1}, {"consulta": "minimos frecuencia se", "rank": 1}, {"consulta": "frecuencia se informa", "rank": 1}]}

  --- plazo:trimestral (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "plazo:trimestral",
 "type": "Plazo",
 "label": "trimestral",
 "properties": {
  "description": [
   "Período de reporte de datos a inversores.",
   "Periodicidad trimestral para observancia de capitales mínimos.",
   "Frecuencia de reportes y evaluaciones del Directivo Responsable.",
   "Frecuencia trimestral para presentación de información bajo consolidación código 3.",
   "Periodicidad de reporte para riesgo de tasa de interés.",
   "Los datos se informarán con frecuencia trimestral.",
   "Frecuencia de presentación de datos correspondientes al último mes de cada trimestre."
  ],
  "unidad": [
   "trimestre",
   "mes",
   "trimestral"
  ],
  "duracion": [
   "cada tres meses",
   "3",
   "trimestral",
   "3 meses"
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo /b"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 9.2"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 1 > Sección 1 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 7 > Punto 8.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 9 > Punto 10.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 10 > Punto 11.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 27, "top10": []}

  --- requisito:valuacion_diaria_a_precios_de_mercado (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "requisito:valuacion_diaria_a_precios_de_mercado",
 "type": "Requisito",
 "label": "valuación diaria a precios de mercado",
 "properties": {
  "description": [
   "Condición técnica que aplica a operaciones con derivados para determinar períodos de mantenimiento mínimo.",
   "Requisito para aplicación de aforos regulatorios en el método integral.",
   "Los activos en garantía deben ser valuados diariamente a precios de mercado para determinar ajustes de aforo.",
   "Las posiciones deben valuarse a precios de mercado al menos diariamente, o evaluarse con periodicidad diaria en caso de valuación a modelo."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 7.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 43, "n_consultas": 27, "top10": []}

  --- plazo:periodicidad_trimestral (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "plazo:periodicidad_trimestral",
 "type": "Plazo",
 "label": "periodicidad trimestral",
 "properties": {
  "description": [
   "Período mínimo de cálculo de KCCP.",
   "Plazo mínimo para elevar el reporte."
  ],
  "duracion": [
   "trimestral",
   "3"
  ],
  "unidad": [
   "trimestral",
   "meses"
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 27, "top10": []}

  --- obligacion:realizar_verificacion_de_precios_con_periodicidad_minima_mensual (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "obligacion:realizar_verificacion_de_precios_con_periodicidad_minima_mensual",
 "type": "Obligacion",
 "label": "realizar verificación de precios con periodicidad mínima mensual",
 "properties": {
  "description": "La verificación de precios de mercado o datos del modelo debe llevarse a cabo al menos con periodicidad mensual, o de forma más frecuente según la naturaleza del mercado o actividad de negociación.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1876, "n_consultas": 27, "top10": []}

  --- plazo:periodicidad_mensual (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "plazo:periodicidad_mensual",
 "type": "Plazo",
 "label": "periodicidad mensual",
 "properties": {
  "description": "Frecuencia mínima de verificación de precios.",
  "unidad": "mensual",
  "duracion": "1 mes",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 27, "top10": []}

  --- plazo:determinacion_mensual (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "plazo:determinacion_mensual",
 "type": "Plazo",
 "label": "determinación mensual",
 "properties": {
  "description": "La exigencia de capital por riesgo operacional se determina con periodicidad mensual.",
  "duracion": "mensual",
  "unidad": "mes",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 7 > Punto 7.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 27, "top10": []}

  --- plazo:mensual (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "plazo:mensual",
 "type": "Plazo",
 "label": "mensual",
 "properties": {
  "description": [
   "Periodicidad mensual para observancia de capitales mínimos.",
   "Frecuencia mensual para presentación de información consolidada.",
   "Periodicidad de los reportes informativos."
  ],
  "unidad": "mes",
  "duracion": [
   "1",
   "mensual"
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 9.2"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 1 > Sección 1 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 7 > Punto 8.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 27, "top10": []}

  --- obligacion:efectuar_clasificacion_de_deudores_con_periodicidad_adecuada (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "obligacion:efectuar_clasificacion_de_deudores_con_periodicidad_adecuada",
 "type": "Obligacion",
 "label": "efectuar clasificación de deudores con periodicidad adecuada",
 "properties": {
  "description": "La clasificación de deudores debe efectuarse con periodicidad que atienda a su importancia, considerando la totalidad de financiaciones comprendidas, con documentación del análisis.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 2.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1748, "n_consultas": 27, "top10": []}

  --- obligacion:efectuar_revision_de_clasificacion_con_periodicidad_minima (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "obligacion:efectuar_revision_de_clasificacion_con_periodicidad_minima",
 "type": "Obligacion",
 "label": "efectuar revisión de clasificación con periodicidad mínima",
 "properties": {
  "description": "Obligación de revisar la clasificación de deudores con la periodicidad indicada en la norma, dejando constancia en el legajo del cliente.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 6.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1680, "n_consultas": 27, "top10": []}

  --- requisito:evaluacion_periodica_del_cliente (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "requisito:evaluacion_periodica_del_cliente",
 "type": "Requisito",
 "label": "evaluación periódica del cliente",
 "properties": {
  "description": "La entidad financiera debe evaluar al cliente con la periodicidad correspondiente, contando con legajo actualizado e información confiable.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 27, "top10": []}

  --- plazo:periodicidad_mensual_de_clasificacion (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "plazo:periodicidad_mensual_de_clasificacion",
 "type": "Plazo",
 "label": "periodicidad mensual de clasificación",
 "properties": {
  "description": "La clasificación de clientes se efectúa al cabo de cada mes.",
  "unidad": "mes",
  "duracion": "mensual",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Punto 7.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1316, "n_consultas": 27, "top10": []}

  --- sujeto_regulado:fiduciario_de_fideicomisos_financieros (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "sujeto_regulado:fiduciario_de_fideicomisos_financieros",
 "type": "SujetoRegulado",
 "label": "fiduciario de fideicomisos financieros",
 "properties": {
  "description": "Entidad responsable de clasificar deudores de créditos fideicomitidos según periodicidad establecida.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1407, "n_consultas": 27, "top10": []}

  --- obligacion:clasificar_deudores_de_creditos_fideicomitidos (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "obligacion:clasificar_deudores_de_creditos_fideicomitidos",
 "type": "Obligacion",
 "label": "clasificar deudores de créditos fideicomitidos",
 "properties": {
  "description": "Fiduciarios deben clasificar deudores según periodicidad y condiciones para cartera comercial o consumo/vivienda.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1928, "n_consultas": 27, "top10": []}

  --- instrumento_financiero:prestamo_personal (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "instrumento_financiero:prestamo_personal",
 "type": "InstrumentoFinanciero",
 "label": "préstamo personal",
 "properties": {
  "description": [
   "Préstamo de capital personal que requiere especificación de importe, monto total a pagar, cantidad de cuotas, periodicidad, vencimiento y sistema de amortización.",
   "Préstamo sin garantía específica otorgado a personas."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 11 > Sección 11 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 27, "top10": []}

  --- instrumento_financiero:prestamo_hipotecario (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "instrumento_financiero:prestamo_hipotecario",
 "type": "InstrumentoFinanciero",
 "label": "préstamo hipotecario",
 "properties": {
  "description": "Préstamo garantizado con hipoteca que debe incluir información sobre importe, monto total, cuotas, periodicidad, vencimiento y amortización.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 27, "top10": []}

  --- obligacion:informar_periodicidad_de_resumen_y_plazo_de_envio (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "obligacion:informar_periodicidad_de_resumen_y_plazo_de_envio",
 "type": "Obligacion",
 "label": "informar periodicidad de resumen y plazo de envío",
 "properties": {
  "description": "Obligación de comunicar al usuario la frecuencia de generación de resumen y el plazo para su entrega.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1313, "n_consultas": 27, "top10": []}

  --- obligacion:presentacion_de_informacion_con_frecuencia_mensual (props) | expuesto en outputs de CQ-025: NO ---
{
 "id": "obligacion:presentacion_de_informacion_con_frecuencia_mensual",
 "type": "Obligacion",
 "label": "presentación de información con frecuencia mensual",
 "properties": {
  "description": "La información se integrará con datos referidos al mes bajo análisis con frecuencia mensual.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 12 > Punto 1.1"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 6, "n_consultas": 27, "top10": [{"consulta": "frecuencia se", "rank": 6}, {"consulta": "frecuencia se informa", "rank": 6}]}

==============================================================================
2. run_2/CQ-019 (15 outputs)
==============================================================================

[2a-i] 'sin deducir' / 'no se deduce':
  [barrido kg run_2: 'sin deducir|no se deduce'] en id/label/properties: 8

  --- requisito:saldo_de_deuda_sin_deducir_previsiones_por_riesgo (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "requisito:saldo_de_deuda_sin_deducir_previsiones_por_riesgo",
 "type": "Requisito",
 "label": "saldo de deuda sin deducir previsiones por riesgo",
 "properties": {
  "description": "El saldo de deuda pendiente debe computarse sin deducir previsiones por riesgo de incobrabilidad ni coberturas del riesgo de crédito.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  }
 ]
}
    edges de requisito:saldo_de_deuda_sin_deducir_previsiones_por_riesgo: 0 salientes, 1 entrantes
    ENTRANTE: {"relation": "requiere", "source": "obligacion:calcular_relacion_ltv_de_manera_prudente", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 2 > Sección 2 — preámbulo"}]}
    D1: {"alcanzable": false, "mejor_rank": 285, "n_consultas": 41, "top10": []}

  --- requisito:usar_monto_bruto_de_exposicion_en_calculo_ksa (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "requisito:usar_monto_bruto_de_exposicion_en_calculo_ksa",
 "type": "Requisito",
 "label": "usar monto bruto de exposición en cálculo KSA",
 "properties": {
  "description": "Si la entidad ha constituido provisión específica o descuento no reembolsable, el cálculo de KSA debe efectuarse usando el monto bruto sin deducir la provisión o descuento.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo /b"
  }
 ]
}
    edges de requisito:usar_monto_bruto_de_exposicion_en_calculo_ksa: 0 salientes, 0 entrantes
    D1: {"alcanzable": false, "mejor_rank": 325, "n_consultas": 41, "top10": []}

  --- concepto_definido:saldos_corresponsalia_casa_matriz_y_filiales (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:saldos_corresponsalia_casa_matriz_y_filiales",
 "type": "ConceptoDefinido",
 "label": "saldos corresponsalía casa matriz y filiales",
 "properties": {
  "description": "Saldos en cuentas de corresponsalía respecto de casa matriz de sucursales locales o sucursales y subsidiarias en otros países que no se deducen.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.4"
  }
 ]
}
    edges de concepto_definido:saldos_corresponsalia_casa_matriz_y_filiales: 0 salientes, 0 entrantes
    D1: {"alcanzable": false, "mejor_rank": 3552, "n_consultas": 41, "top10": []}

  --- obligacion:ponderacion_por_riesgo_de_importes_por_debajo_del_umbral (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "obligacion:ponderacion_por_riesgo_de_importes_por_debajo_del_umbral",
 "type": "Obligacion",
 "label": "ponderación por riesgo de importes por debajo del umbral",
 "properties": {
  "description": "Obligación de ponderar en función del riesgo o considerar para el cómputo de exigencia por riesgo de mercado los importes que no se deducen.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  }
 ]
}
    edges de obligacion:ponderacion_por_riesgo_de_importes_por_debajo_del_umbral: 0 salientes, 1 entrantes
    ENTRANTE: {"relation": "obligado_a", "source": "sujeto_regulado:entidad_financiera", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 8 > Sección 8 — preámbulo"}]}
    D1: {"alcanzable": false, "mejor_rank": 330, "n_consultas": 41, "top10": []}

  --- concepto_definido:prestamos (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:prestamos",
 "type": "ConceptoDefinido",
 "label": "préstamos",
 "properties": {
  "description": "Capitales, diferencias de cotización e intereses devengados a cobrar, sin deducir previsiones por riesgos de incobrabilidad y desvalorización.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 2.1"
  }
 ]
}
    edges de concepto_definido:prestamos: 0 salientes, 0 entrantes
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 41, "top10": []}

  --- concepto_definido:otros_creditos_por_intermediacion_financiera (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:otros_creditos_por_intermediacion_financiera",
 "type": "ConceptoDefinido",
 "label": "otros créditos por intermediación financiera",
 "properties": {
  "description": "Capitales, primas e intereses devengados a cobrar, sin deducir previsiones por riesgos de incobrabilidad y desvalorización.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 2.1"
  }
 ]
}
    edges de concepto_definido:otros_creditos_por_intermediacion_financiera: 0 salientes, 0 entrantes
    D1: {"alcanzable": false, "mejor_rank": 3551, "n_consultas": 41, "top10": []}

  --- concepto_definido:creditos_por_arrendamientos_financieros (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:creditos_por_arrendamientos_financieros",
 "type": "ConceptoDefinido",
 "label": "créditos por arrendamientos financieros",
 "properties": {
  "description": "Créditos derivados de operaciones de arrendamiento financiero sin deducir previsiones correspondientes.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 2.1"
  }
 ]
}
    edges de concepto_definido:creditos_por_arrendamientos_financieros: 0 salientes, 0 entrantes
    D1: {"alcanzable": false, "mejor_rank": 3241, "n_consultas": 41, "top10": []}

  --- concepto_definido:creditos_diversos (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:creditos_diversos",
 "type": "ConceptoDefinido",
 "label": "créditos diversos",
 "properties": {
  "description": "Capitales e intereses devengados a cobrar vinculados a venta de activos inmovilizados, sin deducir previsiones por riesgo de incobrabilidad.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 2.1"
  }
 ]
}
    edges de concepto_definido:creditos_diversos: 0 salientes, 0 entrantes
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 41, "top10": []}

[2a-ii] prevision ∧ incobrabilidad:
  [barrido kg run_2: 'prevision ∧ incobrabilidad'] en id/label/properties: 39
    (> 12 candidatos: regla declarada — ids completos abajo; íntegros solo los que cruzan con 'sin deducir|no se deduce|situacion normal|garantias preferidas': 10)
    ids: ['organismo_regulador:superintendencia_de_entidades_financieras_y_cambiarias', 'concepto_definido:prevision_por_riesgo_de_incobrabilidad', 'concepto_definido:deudor_en_situacion_normal', 'requisito:saldo_de_deuda_sin_deducir_previsiones_por_riesgo', 'concepto_definido:patrimonio_neto_complementario', 'concepto_definido:conceptos_deducibles_del_capital_ordinario_de_nivel_uno', 'concepto_definido:previsiones_por_riesgo_de_incobrabilidad', 'umbral:limite_de_previsiones_por_incobrabilidad', 'concepto_definido:prevision_regulatoria', 'norma_referenciada:niif_9', 'concepto_definido:prevision_por_riesgo_de_incobrabilidad_cartera_situacion_normal', 'norma_referenciada:normas_sobre_provisiones_minimas_por_riesgo_de_incobrabilidad', 'concepto_definido:prevision_regulatoria_por_riesgo_de_incobrabilidad', 'norma_referenciada:comunicacion_a_6851', 'norma_referenciada:comunicacion_a_7928', 'norma_referenciada:comunicacion_a_6489', 'norma_referenciada:comunicacion_a_6938', 'norma_referenciada:comunicacion_b_9104', 'norma_referenciada:comunicacion_a_2729', 'concepto_definido:prestamos', 'concepto_definido:otros_creditos_por_intermediacion_financiera', 'concepto_definido:creditos_diversos', 'obligacion:aprobacion_de_clasificacion_de_deudores_por_directorio', 'concepto_definido:refinanciacion_con_quitas_de_capital', 'norma_referenciada:normas_sobre_previsiones_minimas_por_riesgo_de_incobrabilidad', 'operacion:refinanciacion_con_quitas_de_capital', 'norma_referenciada:comunicacion_a_2216', 'norma_referenciada:comunicacion_a_3630', 'norma_referenciada:comunicacion_a_4070', 'norma_referenciada:comunicacion_a_4467', 'norma_referenciada:comunicacion_a_4683', 'norma_referenciada:comunicacion_a_4738', 'norma_referenciada:comunicacion_a_4781', 'norma_referenciada:comunicacion_a_5398', 'norma_referenciada:comunicacion_a_6558', 'norma_referenciada:comunicacion_a_7024', 'obligacion:registrar_diferencias_de_previsiones_minimas_insuficientes', 'umbral:1_25_de_los_aprs', 'instrumento_financiero:previsiones_por_riesgo_de_incobrabilidad']

  --- concepto_definido:prevision_por_riesgo_de_incobrabilidad (props) | expuesto en outputs de CQ-019: pasos [2, 5, 11] ---
{
 "id": "concepto_definido:prevision_por_riesgo_de_incobrabilidad",
 "type": "ConceptoDefinido",
 "label": "previsión por riesgo de incobrabilidad",
 "properties": {
  "description": [
   "Deducción contable para riesgos de incobrabilidad, incluyendo previsiones en pasivo, aplicable a deudores en situación normal y financiaciones con garantías preferidas.",
   "Concepto técnico regulatorio referido a las previsiones mínimas que deben constituirse por riesgo de incobrabilidad."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.3"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 10.4 /a"
  }
 ]
}
    edges de concepto_definido:prevision_por_riesgo_de_incobrabilidad: 2 salientes, 1 entrantes
    SALIENTE: {"relation": "definido_por", "target": "norma_referenciada:comunicacion_a_2729", "provenances": [{"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 10 > Punto 10.4 /a"}]}
    SALIENTE: {"relation": "definido_por", "target": "norma_referenciada:comunicacion_a_2216", "provenances": [{"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 10 > Punto 10.4 /a"}]}
    ENTRANTE: {"relation": "usa_concepto", "source": "concepto_definido:conceptos_comprendidos", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 2 > Punto 2.3"}]}

  --- concepto_definido:deudor_en_situacion_normal (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:deudor_en_situacion_normal",
 "type": "ConceptoDefinido",
 "label": "deudor en situación normal",
 "properties": {
  "description": "Clasificación de deudor según normativa de clasificación de deudores del BCRA, cuya cartera no será deducida al 100% de la previsión por riesgo de incobrabilidad.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.3"
  }
 ]
}
    edges de concepto_definido:deudor_en_situacion_normal: 1 salientes, 0 entrantes
    SALIENTE: {"relation": "definido_por", "target": "norma_referenciada:texto_ordenado_sobre_clasificacion_de_deudores", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 2 > Punto 2.3"}]}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 41, "top10": []}

  --- requisito:saldo_de_deuda_sin_deducir_previsiones_por_riesgo (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "requisito:saldo_de_deuda_sin_deducir_previsiones_por_riesgo",
 "type": "Requisito",
 "label": "saldo de deuda sin deducir previsiones por riesgo",
 "properties": {
  "description": "El saldo de deuda pendiente debe computarse sin deducir previsiones por riesgo de incobrabilidad ni coberturas del riesgo de crédito.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  }
 ]
}
    edges de requisito:saldo_de_deuda_sin_deducir_previsiones_por_riesgo: 0 salientes, 1 entrantes
    ENTRANTE: {"relation": "requiere", "source": "obligacion:calcular_relacion_ltv_de_manera_prudente", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 2 > Sección 2 — preámbulo"}]}
    D1: {"alcanzable": false, "mejor_rank": 285, "n_consultas": 41, "top10": []}

  --- concepto_definido:previsiones_por_riesgo_de_incobrabilidad (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:previsiones_por_riesgo_de_incobrabilidad",
 "type": "ConceptoDefinido",
 "label": "previsiones por riesgo de incobrabilidad",
 "properties": {
  "description": [
   "Provisiones contables sobre cartera de deudores clasificados en situación normal y financiaciones cubiertas con garantías preferidas tipo A, con límite del 1,25% de activos ponderados por riesgo de crédito.",
   "Previsiones por riesgo de incobrabilidad correspondientes a financiaciones en situación normal o cubiertas con garantías preferidas A que no superen el 1,25% de los APRs."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  }
 ]
}
    edges de concepto_definido:previsiones_por_riesgo_de_incobrabilidad: 2 salientes, 1 entrantes
    SALIENTE: {"relation": "usa_concepto", "target": "concepto_definido:deudores_en_situacion_normal", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 8 > Sección 8 — preámbulo"}]}
    SALIENTE: {"relation": "usa_concepto", "target": "concepto_definido:garantias_preferidas_tipo_a", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 8 > Sección 8 — preámbulo"}]}
    ENTRANTE: {"relation": "usa_concepto", "source": "concepto_definido:patrimonio_neto_complementario", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 8 > Sección 8 — preámbulo"}]}
    D1: {"alcanzable": true, "mejor_rank": 10, "n_consultas": 41, "top10": [{"consulta": "prevision incobrabilidad", "rank": 10}]}

  --- umbral:limite_de_previsiones_por_incobrabilidad (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "umbral:limite_de_previsiones_por_incobrabilidad",
 "type": "Umbral",
 "label": "límite de previsiones por incobrabilidad",
 "properties": {
  "description": "Máximo permitido para previsiones por riesgo de incobrabilidad sobre cartera de deudores en situación normal y financiaciones con garantías preferidas.",
  "valor": "1,25",
  "unidad": "porcentaje de activos ponderados por riesgo de crédito",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  }
 ]
}
    edges de umbral:limite_de_previsiones_por_incobrabilidad: 0 salientes, 0 entrantes
    D1: {"alcanzable": false, "mejor_rank": 12, "n_consultas": 41, "top10": []}

  --- concepto_definido:prevision_por_riesgo_de_incobrabilidad_cartera_situacion_normal (props) | expuesto en outputs de CQ-019: pasos [2, 11] ---
{
 "id": "concepto_definido:prevision_por_riesgo_de_incobrabilidad_cartera_situacion_normal",
 "type": "ConceptoDefinido",
 "label": "previsión por riesgo de incobrabilidad cartera situación normal",
 "properties": {
  "description": "Importe de previsión por riesgo de incobrabilidad correspondiente a cartera en situación normal, computado como patrimonio neto complementario.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.4"
  }
 ]
}
    edges de concepto_definido:prevision_por_riesgo_de_incobrabilidad_cartera_situacion_normal: 0 salientes, 1 entrantes
    ENTRANTE: {"relation": "usa_concepto", "source": "concepto_definido:conceptos_deducibles_del_capital_ordinario_de_nivel_uno", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 8 > Punto 8.4"}]}

  --- concepto_definido:prestamos (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:prestamos",
 "type": "ConceptoDefinido",
 "label": "préstamos",
 "properties": {
  "description": "Capitales, diferencias de cotización e intereses devengados a cobrar, sin deducir previsiones por riesgos de incobrabilidad y desvalorización.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 2.1"
  }
 ]
}
    edges de concepto_definido:prestamos: 0 salientes, 0 entrantes
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 41, "top10": []}

  --- concepto_definido:otros_creditos_por_intermediacion_financiera (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:otros_creditos_por_intermediacion_financiera",
 "type": "ConceptoDefinido",
 "label": "otros créditos por intermediación financiera",
 "properties": {
  "description": "Capitales, primas e intereses devengados a cobrar, sin deducir previsiones por riesgos de incobrabilidad y desvalorización.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 2.1"
  }
 ]
}
    edges de concepto_definido:otros_creditos_por_intermediacion_financiera: 0 salientes, 0 entrantes
    D1: {"alcanzable": false, "mejor_rank": 3551, "n_consultas": 41, "top10": []}

  --- concepto_definido:creditos_diversos (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:creditos_diversos",
 "type": "ConceptoDefinido",
 "label": "créditos diversos",
 "properties": {
  "description": "Capitales e intereses devengados a cobrar vinculados a venta de activos inmovilizados, sin deducir previsiones por riesgo de incobrabilidad.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 2.1"
  }
 ]
}
    edges de concepto_definido:creditos_diversos: 0 salientes, 0 entrantes
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 41, "top10": []}

  --- umbral:1_25_de_los_aprs (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "umbral:1_25_de_los_aprs",
 "type": "Umbral",
 "label": "1,25% de los APRs",
 "properties": {
  "description": "Límite máximo para previsiones por riesgo de incobrabilidad en financiaciones normales o con garantías preferidas A.",
  "valor": "1.25",
  "unidad": "porcentaje",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  }
 ]
}
    edges de umbral:1_25_de_los_aprs: 0 salientes, 0 entrantes
    D1: {"alcanzable": false, "mejor_rank": 745, "n_consultas": 41, "top10": []}

[2a-iii] situacion normal ∧ prevision:
  [barrido kg run_2: 'situacion normal ∧ prevision'] en id/label/properties: 5

  --- concepto_definido:prevision_por_riesgo_de_incobrabilidad (props) | expuesto en outputs de CQ-019: pasos [2, 5, 11] ---
{
 "id": "concepto_definido:prevision_por_riesgo_de_incobrabilidad",
 "type": "ConceptoDefinido",
 "label": "previsión por riesgo de incobrabilidad",
 "properties": {
  "description": [
   "Deducción contable para riesgos de incobrabilidad, incluyendo previsiones en pasivo, aplicable a deudores en situación normal y financiaciones con garantías preferidas.",
   "Concepto técnico regulatorio referido a las previsiones mínimas que deben constituirse por riesgo de incobrabilidad."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.3"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 10.4 /a"
  }
 ]
}
    edges de concepto_definido:prevision_por_riesgo_de_incobrabilidad: 2 salientes, 1 entrantes
    SALIENTE: {"relation": "definido_por", "target": "norma_referenciada:comunicacion_a_2729", "provenances": [{"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 10 > Punto 10.4 /a"}]}
    SALIENTE: {"relation": "definido_por", "target": "norma_referenciada:comunicacion_a_2216", "provenances": [{"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 10 > Punto 10.4 /a"}]}
    ENTRANTE: {"relation": "usa_concepto", "source": "concepto_definido:conceptos_comprendidos", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 2 > Punto 2.3"}]}

  --- concepto_definido:deudor_en_situacion_normal (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:deudor_en_situacion_normal",
 "type": "ConceptoDefinido",
 "label": "deudor en situación normal",
 "properties": {
  "description": "Clasificación de deudor según normativa de clasificación de deudores del BCRA, cuya cartera no será deducida al 100% de la previsión por riesgo de incobrabilidad.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.3"
  }
 ]
}
    edges de concepto_definido:deudor_en_situacion_normal: 1 salientes, 0 entrantes
    SALIENTE: {"relation": "definido_por", "target": "norma_referenciada:texto_ordenado_sobre_clasificacion_de_deudores", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 2 > Punto 2.3"}]}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 41, "top10": []}

  --- concepto_definido:previsiones_por_riesgo_de_incobrabilidad (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:previsiones_por_riesgo_de_incobrabilidad",
 "type": "ConceptoDefinido",
 "label": "previsiones por riesgo de incobrabilidad",
 "properties": {
  "description": [
   "Provisiones contables sobre cartera de deudores clasificados en situación normal y financiaciones cubiertas con garantías preferidas tipo A, con límite del 1,25% de activos ponderados por riesgo de crédito.",
   "Previsiones por riesgo de incobrabilidad correspondientes a financiaciones en situación normal o cubiertas con garantías preferidas A que no superen el 1,25% de los APRs."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  }
 ]
}
    edges de concepto_definido:previsiones_por_riesgo_de_incobrabilidad: 2 salientes, 1 entrantes
    SALIENTE: {"relation": "usa_concepto", "target": "concepto_definido:deudores_en_situacion_normal", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 8 > Sección 8 — preámbulo"}]}
    SALIENTE: {"relation": "usa_concepto", "target": "concepto_definido:garantias_preferidas_tipo_a", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 8 > Sección 8 — preámbulo"}]}
    ENTRANTE: {"relation": "usa_concepto", "source": "concepto_definido:patrimonio_neto_complementario", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 8 > Sección 8 — preámbulo"}]}
    D1: {"alcanzable": true, "mejor_rank": 10, "n_consultas": 41, "top10": [{"consulta": "prevision incobrabilidad", "rank": 10}]}

  --- umbral:limite_de_previsiones_por_incobrabilidad (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "umbral:limite_de_previsiones_por_incobrabilidad",
 "type": "Umbral",
 "label": "límite de previsiones por incobrabilidad",
 "properties": {
  "description": "Máximo permitido para previsiones por riesgo de incobrabilidad sobre cartera de deudores en situación normal y financiaciones con garantías preferidas.",
  "valor": "1,25",
  "unidad": "porcentaje de activos ponderados por riesgo de crédito",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  }
 ]
}
    edges de umbral:limite_de_previsiones_por_incobrabilidad: 0 salientes, 0 entrantes
    D1: {"alcanzable": false, "mejor_rank": 12, "n_consultas": 41, "top10": []}

  --- concepto_definido:prevision_por_riesgo_de_incobrabilidad_cartera_situacion_normal (props) | expuesto en outputs de CQ-019: pasos [2, 11] ---
{
 "id": "concepto_definido:prevision_por_riesgo_de_incobrabilidad_cartera_situacion_normal",
 "type": "ConceptoDefinido",
 "label": "previsión por riesgo de incobrabilidad cartera situación normal",
 "properties": {
  "description": "Importe de previsión por riesgo de incobrabilidad correspondiente a cartera en situación normal, computado como patrimonio neto complementario.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.4"
  }
 ]
}
    edges de concepto_definido:prevision_por_riesgo_de_incobrabilidad_cartera_situacion_normal: 0 salientes, 1 entrantes
    ENTRANTE: {"relation": "usa_concepto", "source": "concepto_definido:conceptos_deducibles_del_capital_ordinario_de_nivel_uno", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Sección 8 > Punto 8.4"}]}

[2a-iv] 'garantias preferidas':
  [barrido kg run_2: 'garantias preferidas'] en id/label/properties: 10

  --- concepto_definido:prevision_por_riesgo_de_incobrabilidad (props) | expuesto en outputs de CQ-019: pasos [2, 5, 11] ---
{
 "id": "concepto_definido:prevision_por_riesgo_de_incobrabilidad",
 "type": "ConceptoDefinido",
 "label": "previsión por riesgo de incobrabilidad",
 "properties": {
  "description": [
   "Deducción contable para riesgos de incobrabilidad, incluyendo previsiones en pasivo, aplicable a deudores en situación normal y financiaciones con garantías preferidas.",
   "Concepto técnico regulatorio referido a las previsiones mínimas que deben constituirse por riesgo de incobrabilidad."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.3"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 10.4 /a"
  }
 ]
}

  --- concepto_definido:previsiones_por_riesgo_de_incobrabilidad (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:previsiones_por_riesgo_de_incobrabilidad",
 "type": "ConceptoDefinido",
 "label": "previsiones por riesgo de incobrabilidad",
 "properties": {
  "description": [
   "Provisiones contables sobre cartera de deudores clasificados en situación normal y financiaciones cubiertas con garantías preferidas tipo A, con límite del 1,25% de activos ponderados por riesgo de crédito.",
   "Previsiones por riesgo de incobrabilidad correspondientes a financiaciones en situación normal o cubiertas con garantías preferidas A que no superen el 1,25% de los APRs."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 10, "n_consultas": 41, "top10": [{"consulta": "prevision incobrabilidad", "rank": 10}]}

  --- umbral:limite_de_previsiones_por_incobrabilidad (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "umbral:limite_de_previsiones_por_incobrabilidad",
 "type": "Umbral",
 "label": "límite de previsiones por incobrabilidad",
 "properties": {
  "description": "Máximo permitido para previsiones por riesgo de incobrabilidad sobre cartera de deudores en situación normal y financiaciones con garantías preferidas.",
  "valor": "1,25",
  "unidad": "porcentaje de activos ponderados por riesgo de crédito",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 12, "n_consultas": 41, "top10": []}

  --- concepto_definido:garantias_preferidas_tipo_a (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:garantias_preferidas_tipo_a",
 "type": "ConceptoDefinido",
 "label": "garantías preferidas tipo A",
 "properties": {
  "description": [
   "Tipo de garantías que pueden cubrir financiaciones sobre las que se calculan previsiones incluibles en patrimonio neto complementario.",
   "Documentos o valores cedidos por deudor en concurso que son cobrables directamente del tercero responsable, tales como facturas de crédito, facturas a consumidores de servicios públicos, cupones de tarjetas de crédito."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 1.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 41, "top10": []}

  --- operacion:agrupacion_de_financiaciones_comerciales_con_creditos_de_consumo_o_vivienda (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "operacion:agrupacion_de_financiaciones_comerciales_con_creditos_de_consumo_o_vivienda",
 "type": "Operacion",
 "label": "agrupación de financiaciones comerciales con créditos de consumo o vivienda",
 "properties": {
  "description": "Opción de agrupar financiaciones comerciales de hasta dos veces el importe de referencia, con o sin garantías preferidas, junto con créditos para consumo o vivienda.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 3.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 2173, "n_consultas": 41, "top10": []}

  --- concepto_definido:deuda_cubierta_con_garantias_preferidas_a (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:deuda_cubierta_con_garantias_preferidas_a",
 "type": "ConceptoDefinido",
 "label": "deuda cubierta con garantías preferidas A",
 "properties": {
  "description": "Categoría de deuda que justifica no evaluar la capacidad de repago del deudor.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 3345, "n_consultas": 41, "top10": []}

  --- obligacion:no_incorporar_flujo_de_fondos_y_estados_contables_cuando_hay_garantias_preferida (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "obligacion:no_incorporar_flujo_de_fondos_y_estados_contables_cuando_hay_garantias_preferida",
 "type": "Obligacion",
 "label": "no incorporar flujo de fondos y estados contables cuando hay garantías preferidas A",
 "properties": {
  "description": "Cuando la deuda cuenta con garantías preferidas A, no es obligatorio incorporar flujo de fondos, estados contables ni información necesaria para análisis de repago.",
  "modalidad": "prohibicion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 298, "n_consultas": 41, "top10": []}

  --- obligacion:exclusion_de_evaluacion_para_financiaciones_con_garantias_preferidas_a (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "obligacion:exclusion_de_evaluacion_para_financiaciones_con_garantias_preferidas_a",
 "type": "Obligacion",
 "label": "exclusión de evaluación para financiaciones con garantías preferidas A",
 "properties": {
  "description": "No corresponderá la evaluación de la capacidad de repago respecto de financiaciones respaldadas con garantías preferidas A.",
  "modalidad": "prohibicion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 3.6"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 629, "n_consultas": 41, "top10": []}

  --- concepto_definido:garantias_preferidas_a (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "concepto_definido:garantias_preferidas_a",
 "type": "ConceptoDefinido",
 "label": "garantías preferidas A",
 "properties": {
  "description": "Tipo de garantía que respalda financiaciones y exime de evaluación de capacidad de repago.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 3.6"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 41, "top10": []}

  --- umbral:1_25_de_los_aprs (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "umbral:1_25_de_los_aprs",
 "type": "Umbral",
 "label": "1,25% de los APRs",
 "properties": {
  "description": "Límite máximo para previsiones por riesgo de incobrabilidad en financiaciones normales o con garantías preferidas A.",
  "valor": "1.25",
  "unidad": "porcentaje",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 745, "n_consultas": 41, "top10": []}

[2a-v] '2.3.1' (props / provenances aparte):
  [barrido kg run_2: '2.3.1'] en id/label/properties: 0 | SOLO en provenances: 0

[2d] vínculo a la clasificación en candidatos de 2a-i/iii (contenido con 6.5.1/7.2.1/'situacion normal'):
  concepto_definido:creditos_diversos: contiene ninguno de los tres en props
  concepto_definido:creditos_por_arrendamientos_financieros: contiene ninguno de los tres en props
  concepto_definido:deudor_en_situacion_normal: contiene ['situacion normal'] en props
  concepto_definido:otros_creditos_por_intermediacion_financiera: contiene ninguno de los tres en props
  concepto_definido:prestamos: contiene ninguno de los tres en props
  concepto_definido:prevision_por_riesgo_de_incobrabilidad: contiene ['situacion normal'] en props
  concepto_definido:prevision_por_riesgo_de_incobrabilidad_cartera_situacion_normal: contiene ['situacion normal'] en props
  concepto_definido:previsiones_por_riesgo_de_incobrabilidad: contiene ['situacion normal'] en props
  concepto_definido:saldos_corresponsalia_casa_matriz_y_filiales: contiene ninguno de los tres en props
  obligacion:ponderacion_por_riesgo_de_importes_por_debajo_del_umbral: contiene ninguno de los tres en props
  requisito:saldo_de_deuda_sin_deducir_previsiones_por_riesgo: contiene ninguno de los tres en props
  requisito:usar_monto_bruto_de_exposicion_en_calculo_ksa: contiene ninguno de los tres en props
  umbral:limite_de_previsiones_por_incobrabilidad: contiene ['situacion normal'] en props

==============================================================================
5. run_2/CQ-018 (15 outputs)
==============================================================================

[5a] exposición de los términos guía de los 8 reprobados:

  ['reclamos'] exposición en outputs de run_2/CQ-018:
    paso 7 salientes[2] obligado_a→obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios
       …": "obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios", "vecino_label": "considerar y resol…
    paso 7 salientes[2] obligado_a→obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios
       …ecino_label": "considerar y resolver fundadamente reclamos de usuarios", "provenances": [{"source_doc": "to_…
    paso 8 salientes[1] obligado_a→obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios
       …": "obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios", "vecino_label": "considerar y resol…
    paso 8 salientes[1] obligado_a→obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios
       …ecino_label": "considerar y resolver fundadamente reclamos de usuarios", "provenances": [{"source_doc": "to_…

  ['resolver fundadamente'] exposición en outputs de run_2/CQ-018:
    paso 7 salientes[2] obligado_a→obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios
       …lamos_de_usuarios", "vecino_label": "considerar y resolver fundadamente reclamos de usuarios", "provenances": [{"source_d…
    paso 8 salientes[1] obligado_a→obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios
       …lamos_de_usuarios", "vecino_label": "considerar y resolver fundadamente reclamos de usuarios", "provenances": [{"source_d…

  ['capacidad de pago'] exposición en outputs de run_2/CQ-018:
    paso 10 resultados[1] id=concepto_definido:capacidad_de_pago
       …d_de_pago", "type": "conceptodefinido", "label": "capacidad de pago", "tokens_matcheados": 2, "resumen_propiedades": …
    paso 10 resultados[1] id=concepto_definido:capacidad_de_pago
       …iedades": "['criterio basico de clasificacion: la capacidad de pago en el futuro de la deuda o de los compromisos obj…
    paso 10 resultados[4] id=concepto_definido:capacidad_de_pago_del_deudor
       …el_deudor", "type": "conceptodefinido", "label": "capacidad de pago del deudor", "tokens_matcheados": 2, "resumen_pro…
    paso 12 nodo id=concepto_definido:capacidad_de_pago
       …d_de_pago", "type": "conceptodefinido", "label": "capacidad de pago", "properties": {"description": ["criterio basico…
    paso 12 nodo id=concepto_definido:capacidad_de_pago
       …cription": ["criterio basico de clasificacion: la capacidad de pago en el futuro de la deuda o de los compromisos obj…

  ['flujo de fondos'] exposición en outputs de run_2/CQ-018:
    paso 12 nodo id=concepto_definido:capacidad_de_pago
       …iciones pactadas, medida a traves del analisis de flujo de fondos."], "version": "vigente_2026-05"}, "provenances":…

  ['morosidad'] exposición en outputs de run_2/CQ-018:
    paso 10 resultados[8] id=concepto_definido:criterios_objetivos_de_clasificacion
       …a para clasificar deudores, incluyendo termino de morosidad, situacion juridica del cliente o sus deudas, cum…
    paso 11 nodo id=concepto_definido:criterios_objetivos_de_clasificacion
       …a para clasificar deudores, incluyendo termino de morosidad, situacion juridica del cliente o sus deudas, cum…

  ['situacion juridica'] exposición en outputs de run_2/CQ-018:
    paso 10 resultados[8] id=concepto_definido:criterios_objetivos_de_clasificacion
       …ificar deudores, incluyendo termino de morosidad, situacion juridica del cliente o sus deudas, cumplimiento de refin…"…
    paso 11 nodo id=concepto_definido:criterios_objetivos_de_clasificacion
       …ificar deudores, incluyendo termino de morosidad, situacion juridica del cliente o sus deudas, cumplimiento de refinan…

  ['refinanciac*'] exposición en outputs de run_2/CQ-018:
    paso 11 nodo id=concepto_definido:criterios_objetivos_de_clasificacion
       …uridica del cliente o sus deudas, cumplimiento de refinanciaciones.", "version": "vigente_2026-05"}, "provenanc…

  ['informacion+productos'] exposición en outputs de run_2/CQ-018:
    paso 8 salientes[4] obligado_a→obligacion:entregar_detalle_de_caracteristicas_de_productos_y_servicios
       …o_label": "entregar detalle de caracteristicas de productos y servicios", "provenances": [{"source_doc": "to_proteccion_u…

  ['publicar+contratos'] exposición en outputs de run_2/CQ-018:
    paso 8 salientes[5] obligado_a→obligacion:publicar_contratos_de_adhesion_en_sitio_de_internet_institucional
       …relation": "obligado_a", "vecino_id": "obligacion:publicar_contratos_de_adhesion_en_sitio_de_internet_instit…
    paso 8 salientes[5] obligado_a→obligacion:publicar_contratos_de_adhesion_en_sitio_de_internet_institucional
       …itio_de_internet_institucional", "vecino_label": "publicar contratos de adhesion en sitio de internet instit…
    paso 8 salientes[6] obligado_a→obligacion:publicar_promociones_y_bonificaciones_con_fechas_y_modalidades
       …relation": "obligado_a", "vecino_id": "obligacion:publicar_promociones_y_bonificaciones_con_fechas_y_modalid…
    paso 8 salientes[6] obligado_a→obligacion:publicar_promociones_y_bonificaciones_con_fechas_y_modalidades
       …iones_con_fechas_y_modalidades", "vecino_label": "publicar promociones y bonificaciones con fechas y modalid…

[5b] contenido ÍNTEGRO de los nodos fuente identificados en 5a:

[5c-i] kg run_2: emisoras ∧ clasific*:
  [barrido kg run_2: 'emisoras ∧ clasific'] en id/label/properties: 1

  --- sujeto_regulado:otras_entidades_acreedoras (props) | expuesto en outputs de CQ-018: NO ---
{
 "id": "sujeto_regulado:otras_entidades_acreedoras",
 "type": "SujetoRegulado",
 "label": "otras entidades acreedoras",
 "properties": {
  "description": "Entidades o fideicomisos financieros y entidades no financieras emisoras de tarjetas de crédito cuyas clasificaciones se consideran para la recategorización.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Punto 7.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 42, "top10": []}

[5c-ii] kg run_2: '10.1' (props / provenances aparte):
  [barrido kg run_2: '10.1'] en id/label/properties: 0 | SOLO en provenances: 29
    (> 12 candidatos: regla declarada — ids completos abajo; íntegros solo los que cruzan con 'clasific|emisoras|proveedores': 3)
    ids: ['sujeto_regulado:entidad_financiera', 'sujeto_regulado:entidades_financieras', 'organismo_regulador:sefyc', 'plazo:trimestral', 'obligacion:implementar_sistemas_y_controles_para_valuacion_prudente', 'requisito:politicas_y_procedimientos_documentados_para_valuacion', 'requisito:lineas_de_reporte_independientes_para_valuacion', 'concepto_definido:marco_de_valuacion_prudente', 'obligacion:integrar_sistemas_de_valuacion_a_gestion_de_riesgos', 'operacion:acceso_al_mercado_de_cambios', 'operacion:cancelacion_de_lineas_de_credito_del_exterior', 'operacion:pagos_al_exterior_por_importaciones_argentinas_de_bienes', 'obligacion:cumplimiento_de_condiciones_para_acceso_al_mercado_de_cambios', 'operacion:cancelacion_de_garantias_y_avales_por_importaciones', 'concepto_definido:importaciones_argentinas_de_bienes', 'concepto_definido:importaciones_argentinas_de_bienes_y_servicios_conexos', 'requisito:cumplimiento_de_requisitos_del_sistema_de_monedas_locales', 'instrumento_financiero:sistema_de_monedas_locales_sml', 'concepto_definido:ratio_de_apalancamiento', 'norma_referenciada:normas_sobre_supervision_consolidada', 'obligacion:informar_ratio_de_apalancamiento_y_sus_componentes', 'concepto_definido:base_individual', 'concepto_definido:base_consolidada_trimestral', 'requisito:plazos_de_presentacion_del_regimen_informativo_contable_mensual', 'requisito:plazos_de_presentacion_del_regimen_informativo_para_supervision', 'concepto_definido:medida_del_capital', 'concepto_definido:medida_de_la_exposicion', 'procedimiento:calculo_del_ratio_de_apalancamiento', 'norma_referenciada:normas_sobre_ratio_de_apalancamiento']

  --- sujeto_regulado:entidad_financiera (SOLO provenance) | expuesto en outputs de CQ-018: NO ---
{
 "id": "sujeto_regulado:entidad_financiera",
 "type": "SujetoRegulado",
 "label": "entidad financiera",
 "properties": {
  "description": [
   "Sujeto regulado que debe cumplir con exigencias de capital mínimo bajo supervisión del BCRA.",
   "Sujeto obligado al cálculo y cumplimiento de exigencia de capital por riesgo de crédito conforme a la fórmula establecida.",
   "Sujeto regulado sobre cuya RPC se miden los límites de inversiones significativas.",
   "Entidad que otorga financiaciones y realiza operaciones en mercados de títulos valores, de monedas y de derivados.",
   "Entidad financiera que debe mantener exposiciones minoristas normativas diversificadas dentro de los límites regulados.",
   "Institución obligada a cumplir los límites de endeudamiento minorista y verificar información en operaciones de compra de cartera.",
   "Sujeto regulado responsable del otorgamiento y seguimiento de créditos hipotecarios.",
   "Organización que otorga créditos y mantiene exposiciones a deudores, responsable de evaluar situaciones de incumplimiento.",
   "Institución regulada sujeta a requisitos de capitales mínimos.",
   "Entidad regulada que participa en estructuras de titulización, puede ser originante, cedente o titular de posiciones.",
   "Persona jurídica que realiza operaciones de titulización y está sujeta a requisitos de capital mínimo.",
   "Entidad financiera que realiza operaciones de titulización y requiere calcular exigencia de capital.",
   "Institución sujeta a regulación de capitales mínimos por riesgo de crédito en inversiones en fondos.",
   "Entidad financiera que invierte en fondos y debe cumplir requisitos de capital.",
   "Institución financiera sujeta a las obligaciones de capital y seguimiento de riesgo de crédito de contraparte.",
   "Sujeto que debe constituir contratos de neteo y obtener opinión legal sobre exigibilidad del neteo en operaciones derivadas.",
   "Sujeto regulado que participa en operaciones de garantía y debe mantener capital mínimo.",
   "Sujeto que participa en operaciones con derivados y debe aplicar regulación de capitales mínimos.",
   "Sujeto obligado a calcular los parámetros de riesgo en instrumentos derivados.",
   "Entidad sujeta a regulación que puede tener exposición significativa al riesgo de base de productos.",
   "Sujeto regulado que debe cumplir con las exigencias de capital por exposición al riesgo de contraparte.",
   "Institución sujeta a requerimientos de capital mínimo por riesgo de crédito de contraparte.",
   "Institución sujeta a regulación de capitales mínimos que realiza operaciones con entidades de contraparte central.",
   "Entidad financiera sujeta a requisitos de capitalización mínima y regulaciones sobre exposiciones con contrapartes de compensación centralizada.",
   "Sujeto regulado obligado a cumplir requisitos de capital respecto de exposiciones con QCCP y CCP, y a aplicar ponderadores de riesgo a aportes de fondos de garantía.",
   "Entidad financiera sujeta a requisitos de capital y cobertura de riesgo de crédito.",
   "Institución financiera que contrata protección crediticia y asume garantías.",
   "Entidad financiera que aplica el método simple de cobertura mediante activos admitidos como garantía.",
   "Institución que realiza operaciones de pase y ejecuta procedimientos de liquidación y cobranza.",
   "Entidad financiera que realiza operaciones de financiación con títulos valores.",
   "Entidades financieras sujetas a regulación de capitales mínimos de riesgo de mercado.",
   "Sujeto regulado que posee derivados de crédito e instrumentos de crédito y debe cumplir exigencias de capital regulatorio.",
   "Sujeto regulado que debe cumplir exigencias de capital por riesgo de mercado en posiciones en acciones.",
   "Sujeto que realiza operaciones de derivados, índices y arbitraje sujeto a exigencias de capital mínimo.",
   "Sujeto regulado que utiliza derivados y mantiene posiciones en productos básicos.",
   "Sujeto regulado que debe cumplir con la determinación diaria de integración de capital según lo establecido en la norma.",
   "Institución financiera sujeta a los requisitos de capital mínimo y gestión de riesgos de mercado.",
   "Entidad sujeta a supervisión regulatoria que debe implementar marco de valuación prudente.",
   "Entidad sujeta a obligaciones de valuación de posiciones conforme a las metodologías establecidas.",
   "Entidades financieras sujetas a regulación de capitales mínimos.",
   "Institución financiera sujeta a los requisitos de capital mínimo establecidos por el BCRA.",
   "Entidad sujeta a requisitos de capital mínimo y obligaciones de divulgación de información regulatoria.",
   "Sujeto regulado obligado a computar el capital ordinario de nivel uno conforme a esta normativa.",
   "Institución sujeta a regulación de capitales mínimos por el BCRA.",
   "Sujeto regulado que debe cumplir con todos los requisitos y obligaciones relativos a instrumentos subordinados de capital.",
   "Entidad financiera sujeta a supervisión y regulación por el BCRA, incluyendo entidades y sus subsidiarias.",
   "Sujeto regulado que debe reconocer capital admisible emitido por subsidiarias sujetas a supervisión consolidada en su RPC.",
   "Sujeto regulado que realiza inversiones en capital de otras entidades financieras, empresas de servicios complementarios y compañías de seguro.",
   "Sujeto regulado a quien se aplican las reglas de deducción de capital por inversiones en otras entidades financieras.",
   "Sujeto regulado que integra y aumenta capital mediante aportes sujetos a estas normas.",
   "Sujeto regulado que debe implementar el proceso de mapping de calificaciones a ponderadores de riesgo.",
   "Personas jurídicas que otorgan financiaciones y deben clasificar a sus clientes.",
   "Entidad que cede créditos, otorga préstamos y realiza la clasificación de deudores.",
   "Instituciones financieras sujetas a las obligaciones de clasificación de deudores y previsionamiento reguladas por el BCRA.",
   "Institución financiera obligada a llevar legajo de cada deudor de su cartera y de sus corresponsales.",
   "Institución financiera responsable de la clasificación de deudores y la presentación de informes a la Superintendencia.",
   "Institución financiera responsable de clasificar su cartera según las categorías establecidas.",
   "Institución financiera responsable de clasificar deudores y realizar reevaluaciones de clasificación según los criterios establecidos.",
   "Institución que otorga financiaciones y clasifica clientes.",
   "Sujeto obligado a concertar acuerdos con deudores en mora y ejecutar procedimientos de clasificación.",
   "Institución financiera que otorga financiamiento y clasifica deudores según las normas del BCRA.",
   "Instituciones financieras obligadas a aplicar los criterios de clasificación de deudores y refinanciación establecidos en la norma.",
   "Entidad que asigna clasificación inicial al deudor y está obligada a recategorizar.",
   "Institución financiera sujeta a las obligaciones de reporte de incrementos de cartera irregular.",
   "Institución obligada a comunicar clasificaciones de deudores y cumplir normas de clasificación individual y consolidada.",
   "Sujeto regulado que debe cumplir con regímenes de clasificación de deudores y provisiones mínimas.",
   "Sujeto regulado que emite certificaciones de acceso al mercado de cambios.",
   "Intermediario responsable de verificar requisitos normativos antes de solicitar acceso al BCRA.",
   "Entidad que otorga acceso al mercado de cambios al cliente para operaciones de recompra, rescate y pago de gastos asociados.",
   "Entidad que otorga acceso al mercado de cambios a clientes para operaciones de recompra y rescate de títulos de deuda.",
   "Entidad que otorga acceso al mercado de cambios para pagos de capital e intereses mediante fideicomisos.",
   "Entidad financiera local que proporciona acceso al mercado de cambios para la operación.",
   "Entidad sujeta al deber de contar con conformidad del BCRA o requerir declaración jurada del cliente para acceso al mercado de cambios.",
   "Institución que actúa como intermediaria en operaciones de cambios y debe obtener conformidad o declaración jurada.",
   "Entidad regulada que debe realizar verificaciones y controles sobre operaciones de egresos de fondos al exterior.",
   "Entidad que actúa como intermediaria en operaciones de exportación y emisión de certificaciones.",
   "Intermediaria que canaliza operaciones a través del SML y debe cumplir requisitos.",
   "Entidad autorizada para registrar operaciones de cambio y emitir boletos de venta de cambio.",
   "Entidad que debe realizar el boleto de venta de cambio y obtener la documentación del cliente.",
   "Entidad financiera que realiza operaciones de liquidación de cobros de exportaciones y acceso a mercado de cambios bajo estos mecanismos.",
   "Institución financiera regulada que realiza operaciones con clientes.",
   "Persona jurídica que realiza operaciones en el mercado de cambios y debe registrarlas ante el BCRA.",
   "Entidad autorizada a elaborar boletos globales diarios según las condiciones establecidas en la norma.",
   "Entidad autorizada a recibir depósitos, mantener cuentas corresponsales y seguimiento de permisos de exportación.",
   "Institución financiera responsable de registrar operaciones y cumplir requisitos de ingreso y liquidación de divisas.",
   "Banco o institución de crédito elegible para ser designada por el exportador como responsable del seguimiento de operaciones de exportación.",
   "Entidad encargada del seguimiento de permisos de exportación y de realizar certificaciones y denuncias ante el BCRA.",
   "Entidad que debe cumplimentar el seguimiento de permisos de embarque y archivar documentación a disposición del BCRA.",
   "Entidad que opera en operaciones de comercio exterior y debe cumplir con requisitos de documentación.",
   "Entidad bancaria que autoriza y gestiona la imputación de descuentos, gastos y multas al permiso de embarque.",
   "Entidad regulada que debe cumplir obligaciones de documentación en operaciones de exportación.",
   "Entidad autorizada a operar en el mercado de cambios y registrar permisos de embarque.",
   "Entidad autorizada a emitir certificaciones de aplicación y seguimiento de operaciones de comercio exterior.",
   "Entidad autorizada a emitir certificaciones de aplicación de divisas en operaciones con el exterior.",
   "Entidad sujeta a las obligaciones de certificación, verificación y registro establecidas en la norma.",
   "Entidad financiera regulada por la normativa cambiaria del BCRA.",
   "Entidad que actúa como cliente en operaciones de cambio y debe efectuar boletos de venta según lo establecido en la norma.",
   "Entidad encargada de dar acceso al mercado de cambios y verificar cumplimiento de requisitos.",
   "Entidad autorizada a operar en el mercado de cambios y realizar pagos de importación.",
   "Entidades que operan en el mercado de cambios y deben cumplir requisitos de conformidad previa.",
   "Entidad financiera que emite u otorga cartas de crédito o letras avaladas para operaciones de importación.",
   "Entidad que accede al mercado de cambios para realizar pagos de importaciones y debe cumplir con obligaciones de registro e información.",
   "Entidad regulada que participa en operaciones de cambios y debe verificar requisitos.",
   "Institución que realiza el seguimiento del pago y registro en SEPAIMPO, y exige la documentación requerida.",
   "Entidad bancaria u otro intermediario que debe exigir documentación y declaraciones juradas para autorizar operaciones de importación con mora o insolvencia del proveedor.",
   "Entidad que debe verificar la separación de componentes de pago en operaciones de alquiler con opción de compra.",
   "Entidad financiera que otorga líneas de crédito del exterior para financiar importaciones de bienes y accede al mercado de cambios para su cancelación.",
   "Entidad sujeta a regulación que debe contar con declaración jurada del importador y opera en mercado de cambios.",
   "Institución que debe contar con documentación y requerimientos del cliente para operaciones de pago de deudas comerciales.",
   "Banco o institución financiera elegible para ser nominada por el importador para llevar a cabo el seguimiento de la oficialización de importación, salvo aquellas que hayan optado por no operar en comercio exterior.",
   "Entidad por donde se cursan los fondos y que debe certificar las devoluciones de pagos.",
   "Entidades financieras locales que intervienen en operaciones de cambios, financiamiento y garantías.",
   "Sujeto regulado responsable de verificar requisitos y acceder al mercado de cambios.",
   "Institución financiera que otorga crédito para financiar importaciones de servicios y accede al mercado de cambios.",
   "Entidad que opera en el mercado de cambios y otorga acceso a operaciones de cambio para proyectos RIGI.",
   "Entidad que otorga acceso al mercado de cambios y debe verificar requisitos complementarios.",
   "Institución financiera responsable de registrar aportes de capital en el régimen informático de operaciones de cambio (RIOC).",
   "Proveedor de servicios financieros que opera casas operativas y atiende usuarios.",
   "Sujeto regulado sometido al régimen informativo contable mensual de consolidación.",
   "Sujeto al que se aplica este régimen informativo de exigencia e integración de capitales mínimos.",
   "Sujeto obligado a cumplir con el régimen informativo contable mensual.",
   "Institución sujeta a obligaciones de información y cálculo de exigencias de capital.",
   "Sujeto regulado que debe reportar información contable mensual según régimen informativo.",
   "Sujeto obligado a cumplir requisitos de capitales mínimos y régimen informativo contable mensual.",
   "Sujeto obligado a realizar cálculos de valor económico del patrimonio y reportar información según régimen informativo contable mensual."
  ],
  "version": "vigente_2026-05",
  "modalidad": null
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Encabezado"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 1 > Punto 2.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.10"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 3.1 /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo /d"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Punto 3.2 /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Punto 4.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Punto 5.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo /b"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.3 /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.3 /b"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.5"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 7.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 10.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 7 > Punto 8.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.6"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 9 > Punto 10.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Encabezado"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 1.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 3.3"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 3.4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 3.5"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 5.1"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Punto 6.4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Punto 6.5"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo /b"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Punto 7.3"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Punto 7.4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 5593 /b"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.8"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 4 > Punto 4.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.7"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.8"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 7 > Punto 8.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 8 > Punto 8.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 9 > Sección 9 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Anexo d — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Punto 10.6"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Punto 10.7"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Punto 11.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 11 > Anexo d > Sección 11 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 13 > Anexo d > Sección 13 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 13 > Anexo d > Punto 13.4"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 13 > Anexo d > Punto 13.6"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Sección 14 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Punto 14.4"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 1 > Punto 1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 1 > Sección 1 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 9 > Sección 9 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 11 > Sección 11 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 42, "top10": []}

  --- sujeto_regulado:entidades_financieras (SOLO provenance) | expuesto en outputs de CQ-018: NO ---
{
 "id": "sujeto_regulado:entidades_financieras",
 "type": "SujetoRegulado",
 "label": "entidades financieras",
 "properties": {
  "description": [
   "Instituciones financieras sujetas a los requisitos de capitales mínimos y obligadas a presentar planes de regularización ante incumplimientos.",
   "Sujetos regulados sujetos a clasificación en grupos conforme a su importancia sistémica.",
   "Instituciones financieras sujetas a los requisitos de análisis de contrapartes y debida diligencia establecidos en la norma.",
   "Entidades financieras sujetas a la obligación de asignar ponderadores de riesgo conforme a las definiciones establecidas.",
   "Instituciones autorizadas a clasificar exposiciones minoristas normativas según categorías transaccionales o no transaccionales, y obligadas a comunicar esa clasificación a SEFyC.",
   "Instituciones financieras sometidas a regulación por el BCRA.",
   "Entidades financieras sujetas a regulación de capitales mínimos.",
   "Entidades sometidas a los requisitos de capital mínimo y ponderación de riesgo establecidos en la norma.",
   "Sujetos regulados que pueden aplicar neteo bilateral en operaciones con contrapartes sujetas a acuerdos de novación o formas legalmente válidas de neteo.",
   "Entidades obligadas a considerar sensibilidad y volatilidad de subyacentes en operaciones derivadas complejas.",
   "Entidades sujetas al cálculo de parámetros de segmentos CDO y aplicación de factores regulatorios.",
   "Entidades sujetas a regulación de capitales mínimos conforme a normas de capitales mínimos.",
   "Sujetos regulados que pueden tener exposiciones con entidades de contraparte central y considerar QCCP según normas de la CNV.",
   "Instituciones financieras sujetas a los requisitos de capital mínimo y técnicas de cobertura de riesgo de crédito.",
   "Entidades financieras sujetas a los requisitos de aplicación de técnicas de coberturas del riesgo de crédito.",
   "Participantes esenciales del mercado sujetos a requisitos de capital mínimo.",
   "Entidades sujetas a requisitos de capitales mínimos que utilizan método integral para cobertura de riesgo de crédito.",
   "Ente admisible como garante o proveedor de protección crediticia.",
   "Instituciones financieras sujetas a exigencias de capital por riesgo de mercado según régimen de capitales mínimos.",
   "Sujetos obligados al cálculo y cumplimiento de exigencias de capital por riesgo de tasa de interés y riesgo específico.",
   "Personas jurídicas sujetas a la regulación de capitales mínimos por riesgo de mercado.",
   "Sujetos regulados obligados a calcular y mantener capital mínimo por riesgo de tipo de cambio.",
   "Sujetos regulados que emplean posiciones en moneda extranjera y oro, sujetos a requisitos de capital mínimo por riesgo de mercado.",
   "Personas jurídicas sujetas a regulación de capitales mínimos por riesgo de posiciones en opciones.",
   "Sujetos regulados que operan con opciones y deben cumplir con las obligaciones de cálculo y reporte de capital mínimo.",
   "Instituciones sujetas a los lineamientos de valuación prudente de posiciones de menor liquidez.",
   "Instituciones sujetas a la regulación del BCRA que realizan valuaciones de activos.",
   "Entidades sujetas a las normas de capital regulatorio del BCRA.",
   "Personas jurídicas que operan en mercados financieros y están sujetas a regulación del BCRA.",
   "Personas jurídicas sujetas a las prescripciones de los artículos 30 y 32 de la Ley de Entidades Financieras respecto del cálculo de capital regulatorio.",
   "Instituciones financieras sujetas a supervisión y regulación del BCRA en materia de capitales mínimos.",
   "Sujetos regulados a los que aplican los límites mínimos de capital.",
   "Entidades financieras, comprendidas sus filiales en el país y en el exterior, sujetas a supervisión de capitales mínimos.",
   "Instituciones financieras sujetas a regulación de capitales mínimos y evaluación de riesgos crediticios.",
   "Personas jurídicas sujetas a regulación de capitales mínimos por el BCRA.",
   "Sujetos regulados a quienes se aplican los requisitos de capitales mínimos establecidos en el texto ordenado.",
   "Instituciones financieras sujetas a regulación del BCRA que otorgan financiaciones y mantienen legajos de clientes.",
   "Sujetos que deben aplicar los criterios de clasificación de deudores establecidos en la norma.",
   "Instituciones financieras autorizadas que intermedian operaciones de cambios.",
   "Instituciones financieras locales que operan en el mercado de cambios.",
   "Personas jurídicas autorizadas a operar en el mercado de cambios regulado por el BCRA.",
   "Instituciones financieras locales autorizadas a operar en el mercado de cambios.",
   "Instituciones autorizadas a dar acceso al mercado de cambios a personas humanas residentes.",
   "Entidades autorizadas a dar acceso al mercado de cambios a residentes en condiciones específicas.",
   "Entidades autorizadas para operar en el mercado de cambios y dar acceso a residentes.",
   "Personas jurídicas autorizadas a operar en el mercado de cambios y dar acceso a residentes.",
   "Instituciones autorizadas a realizar operaciones de canje y arbitraje con clientes.",
   "Instituciones financieras que cancelan líneas de crédito del exterior y acceden al mercado de cambios.",
   "Instituciones financieras locales responsables de cumplir obligaciones respecto de operaciones de egresos y elaboración de declaraciones juradas.",
   "Entidades autorizadas a operar en el mercado de cambios sin límite de horario.",
   "Instituciones financieras reguladas por el BCRA sujetas a normas sobre posición general de cambios.",
   "Entidades sujetas a las obligaciones de confección de boletos de cambio y registro de operaciones propias.",
   "Entidades financieras locales sujetas a las regulaciones de operaciones de cambio y divisas del BCRA.",
   "Instituciones autorizadas a acceder al mercado de cambios para realizar operaciones de importación y financiamiento.",
   "Instituciones que otorgan acceso al mercado de cambios y verifican requisitos para operaciones de importación.",
   "Instituciones que pueden dar acceso al mercado de cambios para operaciones de importación.",
   "Entidades autorizadas a dar acceso al mercado de cambios y canalizar pagos de servicios a no residentes.",
   "Entidades financieras que emiten u otorgan cartas de crédito o letras avaladas.",
   "Instituciones financieras autorizadas a otorgar acceso al mercado de cambios para egresos.",
   "Personas jurídicas autorizadas por el BCRA para realizar operaciones de cambio de manera permanente o habitual.",
   "Sujetos obligados que ofrecen servicios financieros a usuarios de servicios financieros.",
   "Instituciones financieras reguladas que deben cumplir obligaciones de accesibilidad para usuarios con discapacidad auditiva.",
   "Entidades financieras sujetas a las obligaciones de accesibilidad y renovación de infraestructura.",
   "Instituciones financieras obligadas a cumplir con requisitos mínimos en la relación de consumo.",
   "Instituciones financieras que ofrecen productos y servicios a usuarios de servicios financieros.",
   "Instituciones financieras sujetas a las obligaciones de información sobre comisiones y cargos.",
   "Entidades financieras que atienden a usuarios de servicios financieros y están sujetas a obligaciones de protección.",
   "Sujetos obligados a cumplir el régimen informativo contable mensual relativo a exigencias e integración de capitales mínimos.",
   "Personas jurídicas sujetas a las obligaciones de reporte de exigencia e integración de capitales mínimos.",
   "Entidades financieras sujetas a los requisitos informativos sobre capitales mínimos.",
   "Instituciones financieras del país y del exterior clasificadas en riesgo específico de tasa.",
   "Todas las entidades financieras están obligadas a cumplir este requerimiento de información.",
   "Personas jurídicas sujetas al régimen informativo contable mensual del BCRA.",
   "Entidades sujetas a la presentación de informaciones contables mensuales con códigos de consolidación según lo dispuesto en el régimen informativo."
  ],
  "version": "vigente_2026-05",
  "modalidad": null,
  "valor": null,
  "unidad": null,
  "duracion": null
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 1 > Sección 1 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.8"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 4 > Punto 5.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Punto 5.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Punto 6.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.4"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 2.4"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.6"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.10"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 10.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.11"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 7 > Punto 8.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.5"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.7"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 10 > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 10 > Punto 11.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 12 > Anexo Punto > Punto 2.12"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 6.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 2 > Punto 2.7"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.9"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.11"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.12"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.14"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.15"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.9"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.10"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.12"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 9 > Punto 10.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Punto 10.10"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 12 > Anexo d > Punto 13.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 13 > Anexo d > Punto 13.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Punto 14.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Punto 15.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 5 > Punto 1.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Punto 3"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Punto 2.3"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Punto 2.4"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Punto 2.5"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 3 > Punto 4.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 4 > Punto 4.3"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 9 > Punto 10.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 11 > Punto 3"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 12 > Punto 12.4"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 4, "n_consultas": 42, "top10": [{"consulta": "financieras emisoras", "rank": 4}, {"consulta": "financieras emisoras tarjetas", "rank": 6}]}

  --- organismo_regulador:sefyc (SOLO provenance) | expuesto en outputs de CQ-018: NO ---
{
 "id": "organismo_regulador:sefyc",
 "type": "OrganismoRegulador",
 "label": "SEFYC",
 "properties": {
  "description": [
   "Organismo responsable de evaluar y asignar la calificación a las entidades financieras.",
   "Superintendencia de Entidades Financieras y Cambios, organismo supervisor ante el cual las entidades deben demostrar la adecuación de ponderadores de riesgo.",
   "Organismo regulador ante el cual las entidades financieras deben demostrar la adecuación de sus análisis de debida diligencia.",
   "Organismo regulador que recibe comunicación de opciones de clasificación de exposiciones minoristas por parte de entidades financieras.",
   "Superintendencia de Entidades Financieras y Cambios, con facultad de recategorizar posiciones de deuda.",
   "Organismo supervisor ante el cual se reportan fundamentos sobre la clasificación de titulizaciones.",
   "Entidad supervisora que puede detectar incumplimientos de criterios STC y exigir acciones correctivas.",
   "Organismo regulador con capacidad de requerir asignación de operaciones complejas a múltiples clases de activos.",
   "Organismo con facultad de revisar cálculos de capital y recibir información de las entidades financieras.",
   "Organismo regulador que determina el importe de compromisos no desembolsados sujetos a ponderador de riesgo.",
   "Organismo supervisor que recibe notificación de cambios de método.",
   "Superintendencia de Entidades Financieras y Cambiarias, organismo que verifica cumplimiento de normas de riesgo de mercado.",
   "Superintendencia de Entidades Financieras y Cambiarias, autoridad reguladora a la que las entidades deben presentar información metodológica.",
   "Superintendencia de Entidades Financieras y Cambiarias, organismo que determina deficiencias y supervisa el cumplimiento.",
   "Organismo que evalúa el cumplimiento de los lineamientos de valuación para efectos del cálculo de exigencia de capital y gestión de riesgo.",
   "Organismo regulador que supervisa y recibe información sobre valuaciones prudentes y fiables.",
   "Organismo supervisor que evalúa la prudencia de las valuaciones a modelo.",
   "Superintendencia de Entidades Financieras y Cambiarias, autoridad receptora de información.",
   "Organismo regulador que otorga autorizaciones para exclusiones de operaciones discontinuadas del cálculo del indicador de negocio.",
   "Organismo que autoriza exclusiones de pérdidas no relevantes para el perfil de riesgo.",
   "Organismo responsable de la evaluación y calificación de entidades financieras conforme a inspecciones.",
   "Organismo regulador que otorga autorización para rescate de instrumentos y restitución de capital.",
   "Organismo que debe otorgar autorización previa para el ejercicio de opción de compra.",
   "Superintendencia de Entidades Financieras y Cambiarias, autoridad supervisora facultada para requerir deducciones y determinar diferencias en provisiones.",
   "Autoridad que otorga autorización previa para aportes excepcionales de capital.",
   "Superintendencia de Entidades Financieras y Cambiarias, que dicta normas sobre auditorías externas.",
   "Superintendencia de Entidades Financieras y Cambiarias, organismo receptor de programas de encuadramiento.",
   "Organismo regulador que otorga calificaciones en inspecciones de entidades financieras.",
   "Organismo receptor de las informaciones contables y complementarias sobre clasificación de deudores.",
   "Superintendencia de Entidades Financieras y Cambiarias que notifica determinaciones finales de ajuste de previsiones.",
   "Superintendencia de Entidades Financieras y Cambiarias del BCRA.",
   "Organismo que supervisa a bancos del exterior sujetos a supervisión consolidada conforme regímenes de convenios.",
   "Superintendencia de Entidades Financieras y Cambiarias, organismo regulador receptor de informes sobre cartera irregular.",
   "Supervisora de Entidades Financieras y Cambiarias que supervisa registros de beneficios y certificaciones.",
   "Superintendencia de Entidades Financieras y Cambiarias, que elabora y difunde cuadros comparativos de comisiones.",
   "Supervisora de Entidades Financieras y Cambiarias, organismo de fiscalización.",
   "Organismo que emite observaciones e indicaciones sobre el proceso de protección de usuarios de servicios financieros.",
   "Supervisión de Entidades Financieras y Cambiarias; recibe comunicaciones de entidades sobre ponderadores de riesgo específicos.",
   "Superintendencia de Entidades Financieras y Cambiarias, organismo que recibe la información y supervisa el cumplimiento.",
   "Organismo supervisor que tiene a disposición datos de posiciones diarias.",
   "Organismo regulador a quien se dirigen los informes; retiene disposición sobre datos no reportados en el último día del período.",
   "Superintendencia de Entidades Financieras y Cambiarias, organismo que autoriza la capitalización de aportes.",
   "Superintendencia de Entidades Financieras y Cambiarias, autoridad competente para exigir medidas a entidades atípicas.",
   "Superintendencia de Entidades Financieras y Cambiarías.",
   "Organismo que detecta incumplimientos en materia de información y capitales mínimos.",
   "Superintendencia de Entidades Financieras y Cambiarias, autoridad reguladora que determina incrementos de exigencia.",
   "Superintendencia de Entidades Financieras y Cambiarias, organismo regulador que puede determinar incrementos de exigencia de capital."
  ],
  "version": "vigente_2026-05",
  "modalidad": null,
  "alt_labels": [
   "SEFyC"
  ]
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 1 > Punto 2.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.4"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.8"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 3.1 /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 4 > Punto 5.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 7.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.10"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 10.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.11"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 7 > Punto 7.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.6"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.7"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 11 > Punto 12.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 11 > Punto 12.3"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 3.6"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Punto 6.4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo /c"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo /e"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Punto 7.4"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 2 > Punto 3.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 4 > Punto 4.3"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 7 > Punto 8.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 8 > Punto 2"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 9 > Sección 9 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 9 > Punto 9.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 42, "top10": []}

[5c-iii] nodo de clasificación-PNFC usado por la respuesta (mora + consumo/vivienda):
  [barrido kg run_2: 'mora ∧ consumo|vivienda'] en id/label/properties: 5

  --- obligacion:clasificar_a_la_compania_de_seguros_en_funcion_de_la_mora (props) | expuesto en outputs de CQ-018: NO ---
{
 "id": "obligacion:clasificar_a_la_compania_de_seguros_en_funcion_de_la_mora",
 "type": "Obligacion",
 "label": "clasificar a la compañía de seguros en función de la mora",
 "properties": {
  "description": "Obligación de clasificar al asegurador según criterios aplicables a cartera de consumo, considerando la fecha de vencimiento de la primera obligación vencida impaga.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 4.6"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 6, "n_consultas": 42, "top10": [{"consulta": "ademas clasificar", "rank": 6}, {"consulta": "clasificar sus", "rank": 8}, {"consulta": "ademas clasificar sus", "rank": 8}]}

  --- concepto_definido:cartera_de_consumo_o_vivienda (props) | expuesto en outputs de CQ-018: NO ---
{
 "id": "concepto_definido:cartera_de_consumo_o_vivienda",
 "type": "ConceptoDefinido",
 "label": "cartera de consumo o vivienda",
 "properties": {
  "description": "Tipo de cartera crediticia sujeta a normas especiales de clasificación de deudores según mora.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 2443, "n_consultas": 42, "top10": []}

  --- obligacion:clasificar_deudores_segun_mora_en_cartera_consumo_vivienda (props) | expuesto en outputs de CQ-018: pasos [7, 9] ---
{
 "id": "obligacion:clasificar_deudores_segun_mora_en_cartera_consumo_vivienda",
 "type": "Obligacion",
 "label": "clasificar deudores según mora en cartera consumo/vivienda",
 "properties": {
  "description": "Proveedores no financieros deben clasificar deudores en función de su mora aplicando criterios de cartera consumo o vivienda.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  }
 ]
}

  --- obligacion:clasificar_mipymes_canceladas_en_cumplimiento_de_garantias (props) | expuesto en outputs de CQ-018: NO ---
{
 "id": "obligacion:clasificar_mipymes_canceladas_en_cumplimiento_de_garantias",
 "type": "Obligacion",
 "label": "clasificar MiPyMEs canceladas en cumplimiento de garantías",
 "properties": {
  "description": "Sociedades de garantía y fondos públicos deben clasificar MiPyMEs según mora aplicando criterios de cartera consumo/vivienda.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 9, "n_consultas": 42, "top10": [{"consulta": "ademas clasificar", "rank": 9}]}

  --- obligacion:clasificar_deudores_de_creditos_en_plataformas_segun_mora (props) | expuesto en outputs de CQ-018: NO ---
{
 "id": "obligacion:clasificar_deudores_de_creditos_en_plataformas_segun_mora",
 "type": "Obligacion",
 "label": "clasificar deudores de créditos en plataformas según mora",
 "properties": {
  "description": "PSCPP deben clasificar deudores en función de mora según criterios de cartera consumo/vivienda.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 2, "n_consultas": 42, "top10": [{"consulta": "ademas clasificar", "rank": 7}, {"consulta": "clasificar sus", "rank": 9}, {"consulta": "ademas clasificar sus", "rank": 9}, {"consulta": "clasificar sus deudores", "rank": 2}]}
```

## Tabla resumen — run_2

| # | Verificación | Resultado (hechos; evidencia arriba) |
|---|---|---|
| 1a | CQ-025: "mensual" en outputs | EXPUESTO en múltiples unidades — incl. `obligacion:envio_mensual_de_datos_sobre_riesgo_de_mercado` (paso 2, resultados[8], con su resumen) y el nombre del PDF del régimen en provenances de varios nodos |
| 1b | CQ-025: kg mercado ∧ frecuencia-términos | 12 candidatos íntegros con exposición y D1 (detalle arriba) |
| 1c-i | CQ-025: portador trimestral correcto | **1 candidato**: `obligacion:presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado` — **NO expuesto**; D1: `alcanzable=false, mejor_rank=22` |
| 1c-ii | CQ-025: frecuencia general del régimen | 18 candidatos (íntegros con exposición/D1 arriba) |
| 2a | CQ-019: barridos ("sin deducir"/"no se deduce" 8 · prevision∧incobrabilidad 39 —10 cruzados íntegros— · situacion normal∧prevision 5 · garantias preferidas 10 · "2.3.1" **0 props / 0 provenances**) | candidatos íntegros con edges completos, exposición y D1 arriba |
| 2d | CQ-019: vínculo a la clasificación | por candidato de 2a-i/iii: marca de {6.5.1, 7.2.1, "situacion normal"} en props, listado arriba |
| 5a-b | CQ-018: exposición de los 8 contenidos reprobados + nodos fuente íntegros | término por término arriba (con nodo fuente por match) |
| 5c | CQ-018: emisoras∧clasific (1) · "10.1" (**0 props / 29 provenances**, 3 cruzados íntegros) · nodo clasificación-PNFC (5 candidatos mora∧consumo/vivienda, íntegros — la marca "emisoras" en props consta por candidato) | detalle arriba |

---

*Parte 1 de 2. Sin adjudicación. Continúa en `verificaciones_validacion_2.md` (run_4).*
