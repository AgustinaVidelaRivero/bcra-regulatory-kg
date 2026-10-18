"""U-ALCANCE-E1, A3 (USD 0, sin API; solo lectura): las filas de la tabla «## Tanda final» del registro de alcance, leídas con
un parser propio (sin el lector de R2-2 que usa el derivador), contra el reporte del derivador y contra el derivado:
  - las 46 filas, por decisión;
  - las que tienen alcance (clase, dos clases o rol reutilizado), en el orden del registro, son las del reporte y las
    entradas del derivado que siguen a las de HEAD, con los ids de su fila;
  - las entradas de HEAD (las 10 de la tanda 1) son el comienzo del derivado de A3, iguales clave por clave.
Uso: python3 -I -B filas_tanda_final_a3.py REGISTRO.md REPORTE.json DERIVADO_A3.json DERIVADO_HEAD.json SALIDA.json
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

reg_p, rep_p, der_p, der_h_p, salida = (Path(x) for x in sys.argv[1:6])
filas, dentro = [], False
for n, linea in enumerate(reg_p.read_text(encoding="utf-8").splitlines(), 1):
    if linea.startswith("## "):
        dentro = linea.startswith("## Tanda final")
        continue
    if not dentro or not linea.startswith("|") or linea.startswith("|---") or linea.startswith("| TO |"):
        continue
    c = [x.strip() for x in linea.strip().strip("|").split("|")]
    filas.append({"to": c[0], "decision": c[2], "ids": re.findall(r"`(Sujeto_[A-Za-z0-9_]+)`", c[3]), "renglon": n,
                  "columnas": len(c)})
rep = json.loads(rep_p.read_text(encoding="utf-8"))
der = json.loads(der_p.read_text(encoding="utf-8"))
der_h = json.loads(der_h_p.read_text(encoding="utf-8"))
con = [f for f in filas if f["decision"] != "sin alcance declarado"]
nuevas = list(der)[len(der_h):]


def ids_de(e: dict) -> list:
    return e["clase_ids"] if "clase_ids" in e else [e["rol_id"]]


res = {
    "filas": len(filas), "columnas_por_fila": sorted({f["columnas"] for f in filas}),
    "por_decision": dict(Counter(f["decision"] for f in filas)),
    "renglones": [filas[0]["renglon"], filas[-1]["renglon"]] if filas else [],
    "con_alcance": len(con), "sin_alcance": [f["to"] for f in filas if f["decision"] == "sin alcance declarado"],
    "con_alcance_igual_al_reporte": [f["to"] for f in con] == [f["to"] for f in rep["filas_con_alcance"] if f["tanda"] == "final"],
    "sin_alcance_igual_al_reporte": [f["to"] for f in filas if f["decision"] == "sin alcance declarado"]
    == [f["to"] for f in rep["sin_alcance_declarado"] if f["tanda"] == "final"],
    "entradas_nuevas_del_derivado_en_el_orden_del_registro": nuevas == [f"{f['to']}.pdf" for f in con],
    "ids_de_cada_entrada_iguales_a_los_de_su_fila": all(ids_de(der[f"{f['to']}.pdf"]) == f["ids"] for f in con
                                                        if f"{f['to']}.pdf" in der),
    "las_de_head_son_el_comienzo_del_derivado": list(der)[:len(der_h)] == list(der_h)
    and all(der[a] == der_h[a] for a in der_h),
}
res["todo_bien"] = (res["filas"] == 46 and res["columnas_por_fila"] == [6] and res["con_alcance_igual_al_reporte"]
                    and res["sin_alcance_igual_al_reporte"] and res["entradas_nuevas_del_derivado_en_el_orden_del_registro"]
                    and res["ids_de_cada_entrada_iguales_a_los_de_su_fila"] and res["las_de_head_son_el_comienzo_del_derivado"])
salida.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("filas de la tabla «## Tanda final» (parser propio):", json.dumps(res, ensure_ascii=False))
