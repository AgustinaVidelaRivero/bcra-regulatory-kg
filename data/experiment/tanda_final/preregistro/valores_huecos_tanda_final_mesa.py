"""Mesa, §170 (18/10/2026): los valores, como texto, de los huecos del pre-registro de la tanda final que salen de archivos ya commiteados:
- `A3.costo_lineas_usd`, desde la medición de A3 (`data/experiment/alcance_e1/a3/salidas/medicion_mensajes_tres_tandas_a3.json`, en `c66c7ecd`);
- `codigo_cadena.commit_y_sha256`, desde la lista re-sellada sobre el commit de A3 (el archivo que se pasa, que entra con este);
- `T4.*`, desde las tasas del segundo tramo de T4 de la tanda 1 (`data/experiment/tanda1/t4/tasas/tasas_t4_tramo2.json`, en `d728e7b0`).
Los tres sha256 de A3 y el costo de T5 no pasan por acá: los huecos los leen de su archivo (`prompt_r2b.py` y `costo_t5.json`).
Lee con `git show`. Coma decimal, como el texto. USD 0. Uso: python3 -I -B valores_huecos_tanda_final_mesa.py <repo> <lista.json> <salida.json>"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

R, LISTA, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
show = lambda c, p: subprocess.run(["git", "--no-optional-locks", "-C", str(R), "show", f"{c}:{p}"], capture_output=True, check=True).stdout  # noqa: E731
d = lambda x, n=4: f"{x:.{n}f}".replace(".", ",")  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
w = lambda iv: f"[{d(iv[0])}; {d(iv[1])}]"  # noqa: E731
A3 = json.loads(show("c66c7ecd", "data/experiment/alcance_e1/a3/salidas/medicion_mensajes_tres_tandas_a3.json"))["tanda_final"]
tot = A3["total"]
lista_b = LISTA.read_bytes()
lista = json.loads(lista_b)
assert lista["commit"].startswith("c66c7ecd") and lista["n"] == 78
t = json.loads(show("d728e7b0", "data/experiment/tanda1/t4/tasas/tasas_t4_tramo2.json"))


def acept(est):
    r = t["aceptadas"][est]["regla"]
    return (f"{r['errores']} de {r['leidas']} con las dudosas como error; ponderada {d(r['tasa_ponderada'])}, Wilson de Kish {w(r['wilson'])}; "
            f"atención: {'sí' if r['atencion'] else 'no'}; freno: {'sí' if r['freno_por_intervalos'] else 'no'}")


co = t["cola"]["regla"]
ri = t["atencion_RI"]["regla"]
v = t["vigilancias"]
o12 = t["observacion:12"]
pt = t["aceptadas"]["total"]["regla"]
val = {
    "A3.costo_lineas_usd": (f"USD {d(tot['usd_agregados'], 6)}, {mil(tot['tokens_agregados'])} tokens en {mil(tot['unidades_que_cambian'])} unidades de "
                            f"{tot['documentos']} documentos"),
    "codigo_cadena.commit_y_sha256": f"c66c7ecd; la lista re-sellada, sha256 {hashlib.sha256(lista_b).hexdigest()}",
    "T4.cola": f"{co['errores']} de {co['leidas']} con las dudosas como error; ponderada {d(co['tasa_ponderada'])}, Wilson de Kish {w(co['wilson'])}; "
               f"la regla del 25 % {'se dispara' if co['regla_del_25_se_dispara'] else 'no se dispara'}",
    "T4.aceptadas_items": acept("items"),
    "T4.aceptadas_no_items": acept("no_items"),
    "T4.ponderada_total": f"{d(pt['tasa_ponderada'])}, Wilson de Kish {w(pt['wilson'])}",
    "T4.atencion_RI": f"{ri['errores']} de {ri['leidas']}; ponderada de RI {d(ri['tasa_ponderada_RI'])}; la atención {'salta' if ri['atencion'] else 'no salta'}",
    "T4.vigilancias_y_12": (f"(1) {v['vigilancia:1']['cruda']['k']} sí de {v['vigilancia:1']['cruda']['n']}; (2) {v['vigilancia:2']['cruda']['k']} vaciamientos de "
                            f"{v['vigilancia:2']['cruda']['n']}; (3) {v['vigilancia:3']['cruda']['k']} duplicaciones de {v['vigilancia:3']['cruda']['n']}; "
                            f"(7) {v['vigilancia:7']['cruda']['k']} sin apoyo de {v['vigilancia:7']['cruda']['n']}; (12) {o12['cruda']['correctas']} correctas de "
                            f"{o12['cruda']['de']}, Wilson {w(o12['cruda']['wilson'])}"),
}
res = {"fuentes": {"A3": "c66c7ecd:data/experiment/alcance_e1/a3/salidas/medicion_mensajes_tres_tandas_a3.json",
                   "lista": LISTA.name, "T4": "d728e7b0:data/experiment/tanda1/t4/tasas/tasas_t4_tramo2.json"}, **val}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(val, ensure_ascii=False, indent=1))
