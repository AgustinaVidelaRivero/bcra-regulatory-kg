"""B6.1, tanda final, T3, punto 4: la tabla de los `nombres_remision` medidos en los ensamblados nuevos, con las cifras de la mesa al
lado y la condición de la §19 del registro (la variante con la raya entra solo si su contraste da 0 resoluciones distintas). Solo lee.
  - las mías: el resumen y los dos contrastes de esta carpeta (`resumir_medicion_mesa.py` y `contrastar_con_inventario_completo_mesa.py`,
    sin cambios, sobre las mediciones de `medir_nombres_t3_tf.py`);
  - las de la mesa: la tanda final y el acumulado de las tres, de su medición del 16/10/2026 en el repo
    (`data/experiment/nombres_remision/medicion/`); el tramo 1 y el acumulado con el tramo 1, de la enmienda 9, punto 8
    (`git show 756a0394:docs/enmienda9_protocolo_entre_tandas_2026-10-17_tramo_1_de_respaldo.md`, líneas 81 a 84), escritas aquí con esa
    ancla porque su medición está en el paquete de la mesa y no en el repo;
  - la variante que entró en cada ensamblado: si los `nombres_remision` de su manifiesto son los de la regla o los de la raya (juego
    `a_mano` de la medición, que aquí son las listas del manifiesto).
Uso: python3 -I -B tabla_nombres_t3_tf.py <raíz> <dir de la medición> <salida.json> <salida.md>
"""
import json
import sys
from pathlib import Path

RAIZ, D, OUT, MD = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
MED = RAIZ / "data/experiment/nombres_remision/medicion"
GRAFO = {"tanda_final": "KG-TandaFinal-r2b (y su sin cola)", "tramo1": "KG-TandaFinal-Tramo1-r2b (y su sin cola)",
         "acumulado_final": "KG-Acumulado-Tandas0y1yFinal-r2b (y su sin cola)",
         "acumulado_tramo1": "KG-Acumulado-Tandas0y1yTramo1-r2b (y su sin cola)"}
ENMIENDA_9_8 = {  # 756a0394, enmienda 9, punto 8, líneas 81 a 84
    "tramo1": {"menciones": 309, "regla": 1, "regla_con_raya": 1, "distintas_regla": None, "distintas_raya": 0},
    "acumulado_tramo1": {"menciones": 1113, "regla": 429, "regla_con_raya": 455, "distintas_regla": 0, "distintas_raya": 23}}

res_t3 = L(D / "resumen_t3.json")
c_v2, c_raya = L(D / "contraste_t3_regla_v2.json"), L(D / "contraste_t3_regla_v2_con_raya.json")
m_v2, m_raya = L(D / "medicion_t3_regla_v2.json"), L(D / "medicion_t3_regla_v2_con_raya.json")
res_mesa = L(MED / "resumen_medicion_nombres_remision_mesa.json")
cm_v2, cm_raya = L(MED / "contraste_regla_nombres_remision_v2_mesa.json"), L(MED / "contraste_regla_nombres_remision_v2_con_raya_mesa.json")
filas = {}
for c, g in GRAFO.items():
    r = res_t3[c]
    mio = {"menciones": r["menciones"], "regla": r["resueltas"]["regla"], "regla_con_raya": r["resueltas"]["regla_con_raya"],
           "distintas_regla": len(c_v2[c]["regla"]["distintas_de_la_referencia"]),
           "distintas_raya": len(c_raya[c]["regla"]["distintas_de_la_referencia"])}
    if c in res_mesa:
        rm = res_mesa[c]
        mesa = {"menciones": rm["menciones"], "regla": rm["resueltas"]["regla"], "regla_con_raya": rm["resueltas"]["regla_con_raya"],
                "distintas_regla": len(cm_v2[c]["regla"]["distintas_de_la_referencia"]),
                "distintas_raya": len(cm_raya[c]["regla"]["distintas_de_la_referencia"]),
                "fuente": "data/experiment/nombres_remision/medicion/ (16/10/2026)"}
    else:
        mesa = dict(ENMIENDA_9_8[c], fuente="756a0394, enmienda 9, punto 8, líneas 81 a 84 (17/10/2026)")
    iguales = all(mesa[k] is None or mesa[k] == mio[k] for k in mio)
    entra = mio["distintas_raya"] == 0
    man = m_v2["corpus"][c]["juegos"]["a_mano"]["nombres_remision"]
    regla, raya = m_v2["corpus"][c]["juegos"]["regla"]["nombres_remision"], m_raya["corpus"][c]["juegos"]["regla"]["nombres_remision"]
    usada = "regla con la raya" if man == raya else "regla" if man == regla else "otra"
    filas[c] = {"grafo": g, "manifiesto": m_v2["corpus"][c]["manifiesto"][0], "tos": len(m_v2["corpus"][c]["tos"]),
                "tos_con_nombres_en_el_manifiesto": sum(1 for v in man.values() if v), "mio": mio, "mesa": mesa,
                "iguales_a_la_mesa": iguales, "la_raya_entra_por_la_19": entra, "variante_en_el_manifiesto": usada,
                "manifiesto_sigue_la_19": usada == ("regla con la raya" if entra else "regla"),
                "cambios_regla_a_raya": len(r["cambios_regla_a_regla_con_raya"])}
res = {"filas": filas, "todas_iguales_a_la_mesa": all(f["iguales_a_la_mesa"] for f in filas.values())}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
w = ["| ensamblado | TOs | menciones | resueltas, regla | resueltas, raya | distintas, regla | distintas, raya | la raya entra (§19) | "
     "en el manifiesto | la mesa (menciones / regla / raya / distintas con la raya) | igual |",
     "|---|---:|---:|---:|---:|---:|---:|---|---|---|---|"]
for c, f in filas.items():
    m, k = f["mio"], f["mesa"]
    w.append(f"| {f['grafo']} | {f['tos']} | {m['menciones']} | {m['regla']} | {m['regla_con_raya']} | {m['distintas_regla']} | "
             f"{m['distintas_raya']} | {'sí' if f['la_raya_entra_por_la_19'] else 'no'} | {f['variante_en_el_manifiesto']}, "
             f"{f['tos_con_nombres_en_el_manifiesto']} TOs con nombres | {k['menciones']} / {k['regla']} / {k['regla_con_raya']} / "
             f"{k['distintas_raya']} ({k['fuente']}) | {'sí' if f['iguales_a_la_mesa'] else 'NO'} |")
MD.write_text("\n".join(w) + "\n", encoding="utf-8")
print("\n".join(w))
print("todas iguales a la mesa:", res["todas_iguales_a_la_mesa"])
