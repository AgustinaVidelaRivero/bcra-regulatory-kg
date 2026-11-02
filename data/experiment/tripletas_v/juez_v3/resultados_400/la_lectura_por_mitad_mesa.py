"""Mesa, §406 (02/11/2026): la lectura de la autora por mitad (sus 100 de calibración y las 100 de la validación), cruda y ponderada con
su intervalo, como descripción. Usa tal cual cruda() y ponderada() de analisis_T_v2.py (de una copia de su código), con los conteos por
estrato que guardan las salidas: las 200 (analisis_400_v3.json, al_lado.lectura_de_la_autora_en_sus_200) y las 100 de calibración
(analisis_T_v2.json, precision_con_las_100_de_la_autora). Primero reproduce las dos cifras guardadas; la validación es la resta, estrato
por estrato. No lee ninguna hoja de la autora. Imprime cifras agregadas.
  python3 -I -B la_lectura_por_mitad_mesa.py <copia de tripletas_v_juez/, sin vedados> <analisis_400_v3.json> <analisis_T_v2.json> <repo>"""
import hashlib
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
CO, A400, AT2J, REPO = (Path(x) for x in sys.argv[1:5])
sys.path.insert(0, str(CO / "v2/codigo"))
import analisis_T_v2 as AT2  # noqa: E402

assert Path(AT2.__file__).resolve().is_relative_to(CO.resolve())
wk = AT2.cargar_wk(REPO)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()  # noqa: E731
d200 = json.load(open(A400, encoding="utf-8"))["al_lado"]["lectura_de_la_autora_en_sus_200"]["todo"]
d100 = json.load(open(AT2J, encoding="utf-8"))["precision_con_las_100_de_la_autora"]["todo"]
print(f"analisis_400_v3.json {sha(A400)[:16]}… | analisis_T_v2.json {sha(AT2J)[:16]}… | analisis_T_v2.py de la copia "
      f"{sha(Path(AT2.__file__))[:16]}…")


def cuentas(d):
    e = d["ponderada"]["estratos"]
    return {h: (v["k_h"], v["n_h"]) for h, v in e.items()}, {h: v["N_h"] for h, v in e.items()}


c200, N200 = cuentas(d200)
c100, N100 = cuentas(d100)
print("los N_h del grafo, iguales en las dos salidas:", N200 == N100)
ok = {}
for nom, d, c in (("las 200", d200, c200), ("las 100 de calibración", d100, c100)):
    k, n = d["cruda"]["k"], d["cruda"]["n"]
    ok[f"{nom}: cruda() reproduce la guardada"] = AT2.cruda(k, n, wk) == d["cruda"]
    pw = AT2.ponderada(c, N200, wk)
    g = d["ponderada"]
    dif = max([abs(pw["p_w"] - g["p_w"]), abs(pw["n_ef"] - g["n_ef"])] + [abs(x - y) for x, y in zip(pw["wilson"], g["wilson"])])
    ok[f"{nom}: ponderada() reproduce la guardada (p_w, n_ef y Wilson; mayor diferencia {dif:.1e}, por el orden de las sumas)"] = dif < 1e-9
cval = {h: (c200[h][0] - c100.get(h, (0, 0))[0], c200[h][1] - c100.get(h, (0, 0))[1]) for h in c200}
ok["la resta por estrato: ningún k_h ni n_h negativo, k_h ≤ n_h, y suman 100 fichas"] = (
    all(0 <= k <= n for k, n in cval.values()) and sum(n for _, n in cval.values()) == 100)
for k_, v in ok.items():
    print(("OK  " if v else "MAL ") + k_)
kv = sum(k for k, _ in cval.values())
cr = AT2.cruda(kv, 100, wk)
po = AT2.ponderada(cval, N200, wk)
print(f"las 100 de la validación: cruda {cr['fraccion']} = {cr['p']}, Wilson {cr['wilson']} | ponderada {po['p_w']}, n_ef {po['n_ef']},"
      f" Wilson con el n de Kish {po['wilson']}; estratos sin muestra {po['estratos_sin_muestra']}")
print("LA LECTURA POR MITAD, CALCULADA" if all(ok.values()) else "NO SE REPRODUCEN LAS CIFRAS GUARDADAS: no se usa")
sys.exit(0 if all(ok.values()) else 1)
