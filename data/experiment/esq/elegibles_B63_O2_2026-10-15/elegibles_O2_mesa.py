"""Mesa, §102: los documentos elegibles para B6.3 (a) por grupo, con las exclusiones del 15/10/2026, para la opción O2 de U-EVAL-CLASES
(8 de régimen informativo, 4 de normativa general «digerible» y 4 de «necesita reglas»). Solo ids y cuentas.
Uso: python3 -I -B <este> <repo> <constantes_por_documento_E0.json> <json nuevo>"""
import csv, json, sys
from pathlib import Path
R, CONST, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
if OUT.exists(): sys.exit("FRENO: la salida ya existe")
inv = {r["id"]: r for r in csv.DictReader(open(R / "data/experiment/escalado_prep/inventario_unidades.csv", encoding="utf-8"))}
grupo = {t: ("RI" if r["categoria"] == "regimen_informativo" else ("NG_digerible" if r["veredicto"] == "digerible" else "NG_necesita_reglas"))
         for t, r in inv.items()}
exc = json.load(open(R / "data/experiment/esq/documentos_excluidos_evaluacion_final.json", encoding="utf-8"))
excl15 = {d if isinstance(d, str) else d.get("id") for d in exc["documentos"]}
assert len(excl15) == 15, len(excl15)
const = json.load(open(CONST, encoding="utf-8"))
tanda0 = {"ctacte", "docvig", "lingob", "pagjub", "polcre"}
con_correccion = set(const) - tanda0                      # las TOS_TANDA0_* son listas de exclusión, no correcciones
decision2 = set("ri_oc ri_icpipsp ri_pnp ri_psprca gerc ri_spi dmrd ri2_cs ri_cc ri_ccpnp ri_con ri_niif nmaeef ri_saofe ri2_ae".split())
fuera_del_grafo = set("optico plandecuentas ri_chr ri_con ri_fcem ri_itme ri_pfmipyme ri_pscpp ri_pspii ri_rem ri_spi ri_tii manual ri_ao ri2_pm".split())
release_E0 = {"nmaeef", "ri_niif"}                       # corrección por lista de la release de E0 (plan :782, punto 4)
tanda1 = set("ayccef expaef opefci adrei ri_ccna ri_rml ri_gerc ri_pgn snp_cheq ceninf cirmo3 snp_tr lingeef depaho cajasc manori efemin nmcief ri_dcpc ri_oc".split())
base = set(inv) - excl15
assert len(base) == 137
capas = [("los 137", base), ("sin la decisión 2", decision2), ("sin ri2_pm ni lo que queda fuera del grafo (no segmentables, manual, ri_ao)", fuera_del_grafo),
         ("sin los que tienen una constante por documento en E0", con_correccion), ("sin los que saca la release de E0", release_E0)]
res, quedan = {"capas": []}, set(base)
def por_grupo(xs): return {g: sum(1 for x in xs if grupo[x] == g) for g in ("RI", "NG_digerible", "NG_necesita_reglas")}
for nombre, xs in capas:
    if nombre != "los 137": quedan -= xs
    res["capas"].append({"capa": nombre, "quedan": len(quedan), "por_grupo": por_grupo(quedan)})
res["elegibles_final"] = {g: sorted(x for x in quedan if grupo[x] == g) for g in ("RI", "NG_digerible", "NG_necesita_reglas")}
caida = quedan & tanda1
res["rama_de_caida_tanda_1"] = {"quedan": len(caida), "por_grupo": por_grupo(caida), "ids": sorted(caida),
                                 "nota": "sin el sucesor de ri_oc, que fija S2"}
res["O2_pide"] = {"RI": 8, "NG_digerible": 4, "NG_necesita_reglas": 4}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for c in res["capas"]: print(f"{c['capa']}: {c['quedan']} {c['por_grupo']}")
print("rama de caída (solo tanda 1):", res["rama_de_caida_tanda_1"]["quedan"], res["rama_de_caida_tanda_1"]["por_grupo"], res["rama_de_caida_tanda_1"]["ids"])
