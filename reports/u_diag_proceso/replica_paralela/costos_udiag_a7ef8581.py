"""Estimacion de costo USD de las opciones de U-DIAG-PROCESO. USD 0 (no llama a la API).
Tarifas: data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py:89-94 (E1 in 1,00 / out 5,00 /
cache read 0,10; E3 in 2,00 USD/MTok). Costo medio por unidad de E1+E3 de la tanda 0: 0,0166
(docs/protocolo_entre_tandas.md:177-187, firmado en a304b89). Conteos: censo_particion.json,
censo_tanda0.json, troceo_en_grafo_diez.json, bloques_lista_en_grafo_diez.json.
Supuestos NO VERIFICADOS (los mide P1.c de U-PROMPT-R2): +250 tokens de prefijo por la regla de
composicion; +25 tokens de salida por nodo de item compuesto; +60 por bloque que abre lista;
+30 por relacion hacia una unidad heredada.
Uso: python -B costos.py <dir_con_los_json> <out.json>"""
import json, sys
from pathlib import Path
d = Path(sys.argv[1]); out = Path(sys.argv[2])
P_IN, P_OUT, P_CR, P_IN_E3 = 1.00, 5.00, 0.10, 2.00
U_T0, U_PART, C_UNIDAD = 2434, 9324, 0.0166
ct0 = json.loads((d / "censo_tanda0.json").read_text(encoding="utf-8"))["total"]
cpa = json.loads((d / "censo_particion.json").read_text(encoding="utf-8"))["total"]
blq = json.loads((d / "bloques_lista_en_grafo_diez.json").read_text(encoding="utf-8"))
tro = json.loads((d / "troceo_en_grafo_diez.json").read_text(encoding="utf-8"))
nodos_item = blq["C_nodos_por_unidad_media"]
SUP = {"prefijo_tok": 250, "salida_tok_por_nodo_item": 25, "salida_tok_por_bloque": 60, "salida_tok_por_relacion_heredada": 30}
def f1b(unidades, items, bloques):
    pref = unidades * SUP["prefijo_tok"] * P_CR / 1e6
    out_tok = items * nodos_item * SUP["salida_tok_por_nodo_item"] + bloques * SUP["salida_tok_por_bloque"]
    sal = out_tok * P_OUT / 1e6
    e3 = out_tok * P_IN_E3 / 1e6
    return {"prefijo": round(pref, 4), "salida_e1": round(sal, 4), "entrada_e3": round(e3, 4), "total": round(pref + sal + e3, 4)}
b_t0_con_intro = tro["B_resumen"]["con_intro"]
res = {
    "base": {"tarifas_usd_mtok": {"e1_in": P_IN, "e1_out": P_OUT, "e1_cache_read": P_CR, "e3_in": P_IN_E3},
             "costo_unidad_e1_e3_tanda0": C_UNIDAD, "supuestos_no_verificados": SUP,
             "nodos_por_item_tanda0": nodos_item},
    "F1a_e0": {"unidades_nuevas_tanda0": ct0["A_titulo_con_dos_puntos_sin_intro"],
               "costo_tanda0_dentro_de_UREEXT": round(ct0["A_titulo_con_dos_puntos_sin_intro"] * C_UNIDAD, 4),
               "unidades_nuevas_particion": cpa["A_titulo_con_dos_puntos_sin_intro"],
               "costo_particion": round(cpa["A_titulo_con_dos_puntos_sin_intro"] * C_UNIDAD, 4),
               "afectadas_tanda0_si_va_despues": ct0["A_titulo_con_dos_puntos_sin_intro"] + b_t0_con_intro,
               "costo_si_va_despues": round((ct0["A_titulo_con_dos_puntos_sin_intro"] + b_t0_con_intro) * C_UNIDAD, 4)},
    "F1b_prompt": {"tanda0": f1b(U_T0, ct0["C_item_de_lista"], ct0["D_chapeau_unidad_propia_con_dos_puntos"]),
                   "particion": f1b(U_PART, cpa["C_item_de_lista"], cpa["D_chapeau_unidad_propia_con_dos_puntos"])},
    "Va_relacion_heredada": {"tanda0": round(ct0["C_item_de_lista"] * SUP["salida_tok_por_relacion_heredada"] * P_OUT / 1e6, 4),
                             "particion": round(cpa["C_item_de_lista"] * SUP["salida_tok_por_relacion_heredada"] * P_OUT / 1e6, 4)},
    "control_P4_F1b": {"casos": 7, "brazos_pagados": 12, "cota_usd": round(12 * C_UNIDAD, 4),
                       "nota": "5 fichas de TOs ya excluidos (los dos brazos por la API) + 2 de la tanda 0 (solo el brazo nuevo); cota con el costo medio de E1+E3"},
}
out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
