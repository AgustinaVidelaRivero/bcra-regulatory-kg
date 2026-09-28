"""Punto 3 (complemento): cuantas de las 35 Condiciones aisladas recibirian una arista
referencia si Condicion estuviera en TIPOS_ORIGEN; detalle de las 2 sin relaciones. Solo lectura."""
import json, sys, copy
from pathlib import Path
REPO = Path("/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg")
REX = REPO / "data/experiment/reextraccion_v2"
sys.path.insert(0, str(REX / "corpus_v2"))
import r1_comun as C  # noqa
import r1_referencias as REF  # noqa
man = json.load(open(REX / "manifiestos/tanda0_ens_desarrollo.json"))
C.TOS_ORDEN = tuple(man["orden_corrida"])
C.E0_ENM01 = REX / "e0_chunking/salida_tanda0"
REF.INVENTARIO_TOS = {t["id"]: tuple(t["nombres_remision"]) for t in sorted(man["tos"], key=lambda t: t["id"])}
kg0 = json.load(open(REX / "corpus_tanda0/ens_desarrollo/r1/kg.json"))
base = {"nodes": kg0["nodes"], "edges": [e for e in kg0["edges"] if e.get("rol_fuente") != "referencia_cruzada"]}
REF.TIPOS_ORIGEN = ("Obligacion", "Restriccion", "Excepcion", "Operacion", "Condicion", "Potestad", "Definicion")
kg = copy.deepcopy(base)
REF.detectar_y_resolver(kg)
filas = json.load(open("/tmp/u_audit_tipos/p3_filas.json"))
ids = {f["id"] for f in filas}
gan_sal = {e["source"] for e in kg["edges"] if e.get("rol_fuente") == "referencia_cruzada" and e["source"] in ids}
gan_ent = {e["target"] for e in kg["edges"] if e.get("rol_fuente") == "referencia_cruzada" and e["target"] in ids}
print("aisladas que ganarian referencia saliente:", len(gan_sal))
print("aisladas que ya podrian ser destino (entrante) con 9 tipos:", len(gan_ent))
print("aisladas con alguna referencia (sal o ent):", len(gan_sal | gan_ent))
for f in filas:
    if not f["relaciones_validas_en_final"] and not f["rechazos_en_final"]:
        print("SIN RELACIONES:", f["id"], f["chunk_id"], f["estado_e3"], f.get("relaciones_crudas_e1"))
json.dump({"ganan_saliente": sorted(gan_sal), "ganan_entrante": sorted(gan_ent)},
          open("/tmp/u_audit_tipos/p3b_cruce.json", "w"), ensure_ascii=False, indent=1)
