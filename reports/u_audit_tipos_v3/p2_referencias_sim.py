"""Punto 2 (r1_referencias.TIPOS_ORIGEN): efecto medido sobre ens_desarrollo/r1/kg.json.
Simulacion EN MEMORIA (nada se escribe en el repo). Control: quitar las aristas
rol_fuente=referencia_cruzada y re-detectar con TIPOS_ORIGEN original debe reproducir
exactamente las aristas existentes. Luego se re-detecta con los 9 tipos."""
import json, sys, copy, collections
from pathlib import Path
REPO = Path("/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg")
REX = REPO / "data/experiment/reextraccion_v2"
sys.path.insert(0, str(REX / "corpus_v2"))
import r1_comun as C  # noqa
import r1_referencias as REF  # noqa
man = json.load(open(REX / "manifiestos/tanda0_ens_desarrollo.json"))
rep = json.load(open(REX / "corpus_tanda0/ens_desarrollo/r1/reporte_ensamblado_r1.json"))
C.TOS_ORDEN = tuple(man["orden_corrida"])
C.E0_ENM01 = REPO / rep["manifiesto"]["e0_salida"]
REF.INVENTARIO_TOS = {t["id"]: tuple(t["nombres_remision"]) for t in sorted(man["tos"], key=lambda t: t["id"])}
kg0 = json.load(open(REX / "corpus_tanda0/ens_desarrollo/r1/kg.json"))
existentes = {(e["source"], e["relation"], e["target"]) for e in kg0["edges"] if e.get("rol_fuente") == "referencia_cruzada"}
base = {"nodes": kg0["nodes"], "edges": [e for e in kg0["edges"] if e.get("rol_fuente") != "referencia_cruzada"]}
tipo = {n["id"]: n["type"] for n in kg0["nodes"]}

def correr(tipos_origen):
    REF.TIPOS_ORIGEN = tipos_origen
    kg = copy.deepcopy(base)
    r = REF.detectar_y_resolver(kg)
    nuevas = {(e["source"], e["relation"], e["target"]) for e in kg["edges"] if e.get("rol_fuente") == "referencia_cruzada"}
    return r, nuevas

ORIG = ("Obligacion", "Restriccion", "Excepcion", "Operacion")
r_ctrl, n_ctrl = correr(ORIG)
control = {"aristas_existentes": len(existentes), "aristas_re_detectadas": len(n_ctrl),
           "identicas": n_ctrl == existentes,
           "resumen_ctrl_vs_reporte_iguales": {k: r_ctrl["resumen"].get(k) == rep["referencias"].get(k)
                                               for k in ("nodos_con_remision", "menciones", "resueltas", "parciales", "irresolubles", "aristas_referencia_nuevas")}}
r_ext, n_ext = correr(ORIG + ("Condicion", "Potestad", "Definicion"))
extra = n_ext - n_ctrl
perdidas = n_ctrl - n_ext
por_origen = collections.Counter(tipo[s] for s, _, _ in extra)
por_firma = collections.Counter((tipo[s], tipo[t]) for s, _, t in extra)
nodos_origen = collections.Counter(tipo[s] for s in {s for s, _, _ in extra})
# nodos de los tres tipos con al menos una mencion detectada (aunque no resuelva)
rem_nuevos = [x for x in r_ext["remisiones"] if tipo[x["nodo"]] in ("Condicion", "Potestad", "Definicion")]
irr_nuevos = [x for x in r_ext["irresolubles"] if tipo[x["nodo"]] in ("Condicion", "Potestad", "Definicion")]
n_tipo = collections.Counter(n["type"] for n in kg0["nodes"])
res = {"control": control,
       "nodos_excluidos_como_origen": {t: n_tipo[t] for t in ("Condicion", "Potestad", "Definicion")},
       "con_9_tipos": {"aristas_referencia_adicionales": len(extra), "aristas_perdidas": len(perdidas),
                       "por_tipo_origen": dict(por_origen),
                       "nodos_origen_con_arista_por_tipo": dict(nodos_origen),
                       "por_firma_origen_destino": {f"{a}->{b}": c for (a, b), c in por_firma.most_common()},
                       "menciones_en_nodos_nuevos": len(rem_nuevos),
                       "nodos_nuevos_con_remision": len({x["nodo"] for x in rem_nuevos}),
                       "nodos_nuevos_con_remision_por_tipo": dict(collections.Counter(tipo[x] for x in {x["nodo"] for x in rem_nuevos})),
                       "irresolubles_en_nodos_nuevos": len(irr_nuevos),
                       "resumen_detector": {k: r_ext["resumen"][k] for k in ("nodos_con_remision", "menciones", "resueltas", "parciales", "irresolubles", "aristas_referencia_nuevas")}}}
json.dump(res, open("/tmp/u_audit_tipos/p2_referencias_sim.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
