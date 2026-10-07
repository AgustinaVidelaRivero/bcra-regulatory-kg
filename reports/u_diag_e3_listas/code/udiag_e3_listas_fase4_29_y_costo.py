"""U-DIAG-E3-LISTAS, fase 4 (solo lectura, USD 0): mi clasificación, por unidad, de los 17 ítems de lista entre las
29 unidades de flag «cola_humana» (volcada en este archivo antes del tally; ubicación de las citas en
ubicacion_citas_29_items.json) y el costo de re-verificar en E3 los ítems con la tarifa observada (tabla de
reprocesamiento, §5).

Clases: lista_falsa_alarma (el reclamo que persistió cae si E3 recibe el bloque que abre la lista o la regla de
composición), lista_fundada (error real de composición del extractor), lista_dudosa, cierre (reclamo sobre un
párrafo de cierre heredado que el extractor declaró en sus omisiones; E3 no lo recibe), otro_bloque (ídem con el
intro de un ancestro), no_relacionada (texto propio del ítem).

Uso: python fase4_29_y_costo.py <salida_dir>
"""
import json
import sys
from collections import Counter
from pathlib import Path

SAL = Path(sys.argv[1])
CLASE = {
    "pro::4.2.1.3": ("lista_dudosa", "reclama como norma el tramo del encabezado 4.2.1 que el extractor declaró meta_normativo"),
    "pro::4.2.1.4": ("lista_fundada", "el intro del 4.2.1 dice «podrá informar» y la extracción compuso «deberá»"),
    "ext::2.6.1.1": ("cierre", "la cita está en el cierre del 2.6.1"),
    "ext::3.5.6.1": ("lista_falsa_alarma", "polaridad: el intro del 3.5.6 dice que el requisito no es aplicable en los ítems"),
    "ext::3.6.1.1": ("lista_falsa_alarma", "pide la prohibición del 3.6.1 como entidad del ítem (P3C-d2 manda no emitirla)"),
    "ext::3.6.4.2": ("no_relacionada", "salvedad del texto propio"),
    "ext::3.11.1.1": ("lista_falsa_alarma", "«o los fideicomisos...» y la finalidad están en el intro del 3.11.1 y en las descripciones"),
    "ext::3.17.1.2": ("cierre", "la cita está en el cierre del 3.17.1"),
    "ext::3.18.1.1": ("cierre", "la cita está en el cierre del 3.18.1"),
    "ext::4.7.1": ("lista_falsa_alarma", "«contrapartes vinculadas» sigue al título truncado del 4.7, en su intro"),
    "ext::4.8.4.3": ("no_relacionada", "texto propio"),
    "ext::7.10.1.1": ("lista_falsa_alarma", "el contenido que E3 da por agregado está en el intro del 7.10.1"),
    "ext::8.5.19.2": ("otro_bloque", "la cita está en el intro del 8.5 (ancestro), no en el que abre la lista"),
    "ext::10.3.4.1": ("no_relacionada", "texto propio"),
    "ext::13.2.7.1": ("lista_dudosa", "supuesto del encabezado 13.2.7 que R30 manda componer; el segundo reclamo cita el cierre"),
    "ctacte::4.5.2.2": ("no_relacionada", "calificador «solo» del texto propio"),
    "lingob::7.1.7": ("lista_fundada", "el intro del 7.1 recomienda («es deseable»); la extracción compuso un deber"),
}
ub = json.loads((SAL / "ubicacion_citas_29_items.json").read_text(encoding="utf-8"))
assert sorted(CLASE) == sorted({x["id"].split("|")[0] for x in ub}), "las 17 no coinciden"
t = Counter(v[0] for v in CLASE.values())
fase1 = json.loads((SAL / "fase1_resumen.json").read_text(encoding="utf-8"))
items = fase1["unidades_con_linea_item"]
tarifa_e3 = 0.010226      # tabla_reprocesamiento.md §5 (:360): E3 de las afectadas, por unidad
tarifa_f10_tanda0 = 24.9403  # tabla_reprocesamiento.md §5 (:361): F10 paga E3 de todas, observado en la tanda 0
res = {
    "unidades": len(CLASE), "por_clase": dict(t),
    "relacionadas_con_la_lista": sum(t[k] for k in ("lista_falsa_alarma", "lista_fundada", "lista_dudosa")),
    "bloques_heredados_que_E3_no_recibe": sum(t[k] for k in ("cierre", "otro_bloque")),
    "clasificacion": {k: {"clase": v[0], "razon": v[1]} for k, v in sorted(CLASE.items())},
    "costo": {"items": items, "tarifa_e3_por_unidad": tarifa_e3,
              "e3_de_los_items_usd": round(items * tarifa_e3, 2),
              "f10_e3_de_todas_tanda0_usd": tarifa_f10_tanda0},
}
(SAL / "fase4_29_y_costo.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k != "clasificacion"}, ensure_ascii=False, indent=1))
