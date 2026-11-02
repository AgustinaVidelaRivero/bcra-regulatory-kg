"""Mesa, §406 (02/11/2026): las cifras de los resultados de las 400 de tripletas, leídas por código de sus salidas, cada una con su archivo
y su clave, y el control de la decisión 2: la cifra de las 400 queda entre las dos cotas de las 11, en la cruda y en la ponderada.
Imprime cifras agregadas, sha256 y claves; ninguna ruta de la máquina.
  python3 -I -B las_cifras_y_las_cotas_mesa.py <tripletas_v_juez/>"""
import hashlib
import json
import sys
from pathlib import Path

V = Path(sys.argv[1])
F = {"analisis_T_v2.json": V / "v2/corridas/T/analisis_prueba_T/analisis_T_v2.json",
     "analisis_400_v3.json": V / "v3/corridas/analisis_400/analisis_400_v3.json",
     "todas_correctas": V / "v3/corridas/analisis_400_cotas/todas_correctas/analisis_400_v3.json",
     "todas_incorrectas": V / "v3/corridas/analisis_400_cotas/todas_incorrectas/analisis_400_v3.json"}
d = {k: json.load(open(f, encoding="utf-8")) for k, f in F.items()}
for k, f in F.items():
    print(f"{k}: {f.relative_to(V)} | sha256 {hashlib.sha256(f.read_bytes()).hexdigest()}")


def fila(nom, arch, clave, x):
    c, p = x["cruda"], x["ponderada"]
    print(f"{nom} | {arch} | {clave} | cruda {c['k']} de {c['n']} = {c['p']:.4f}, Wilson {c['wilson'][0]:.4f} a {c['wilson'][1]:.4f} | "
          f"ponderada {p['p_w']:.4f}, n_ef {p['n_ef']:.2f}, Wilson con el n de Kish {p['wilson'][0]:.4f} a {p['wilson'][1]:.4f}")


print("== las cifras")
fila("la de la tesis (tus 100)", "analisis_T_v2.json", "precision_con_las_100_de_la_autora.todo",
     d["analisis_T_v2.json"]["precision_con_las_100_de_la_autora"]["todo"])
fila("las 400 con la opción B", "analisis_400_v3.json", "cifra_principal.todo", d["analisis_400_v3.json"]["cifra_principal"]["todo"])
fila("tu lectura sola (tus 200)", "analisis_400_v3.json", "al_lado.lectura_de_la_autora_en_sus_200.todo",
     d["analisis_400_v3.json"]["al_lado"]["lectura_de_la_autora_en_sus_200"]["todo"])
for k in ("todas_correctas", "todas_incorrectas"):
    fila(f"la cota con las 11 {k.replace('_', ' ')}", k + "/analisis_400_v3.json", "cifra_principal.todo", d[k]["cifra_principal"]["todo"])
s = d["analisis_400_v3.json"]["sensibilidad"]
iv = s["bootstrap"]["intervalos"]
print(f"la sensibilidad (las 400 con la parte de la v3 corregida) | analisis_400_v3.json | sensibilidad | cruda "
      f"{s['las_400_con_la_parte_de_la_v3_corregida']['cruda']:.4f}, bootstrap {iv['las_400_cruda'][0]:.4f} a "
      f"{iv['las_400_cruda'][1]:.4f} | "
      f"ponderada {s['las_400_con_la_parte_de_la_v3_corregida']['ponderada']:.4f}, bootstrap {iv['las_400_ponderada'][0]:.4f} a "
      f"{iv['las_400_ponderada'][1]:.4f} | réplicas {s['bootstrap']['replicas']}, semilla {s['bootstrap']['semilla']}, indefinidas "
      f"{s['bootstrap']['indefinidas']}")
m, c, i = (d[k]["cifra_principal"]["todo"] for k in ("analisis_400_v3.json", "todas_correctas", "todas_incorrectas"))
ok = {"la cruda de las 400 queda entre las dos cotas": i["cruda"]["k"] <= m["cruda"]["k"] <= c["cruda"]["k"],
      "la ponderada de las 400 queda entre las dos cotas": i["ponderada"]["p_w"] <= m["ponderada"]["p_w"] <= c["ponderada"]["p_w"],
      "las dos cotas difieren en exactamente 11 en la cruda": c["cruda"]["k"] - i["cruda"]["k"] == 11,
      "las tres salidas: 400 fichas, todas decididas": all(x["fichas"] == 400 and x["decididas"] == 400 for x in (m, c, i)),
      "las dos cotas guardan las 11 adjudicadas": all(d[k]["adjudicacion_200"]["adjudicadas"] == 11 for k in ("todas_correctas",
                                                                                                         "todas_incorrectas"))}
a = d["analisis_400_v3.json"]
print("== el control de la decisión 2")
for k, v in ok.items():
    print(("OK  " if v else "MAL ") + k)
print(f"la adjudicación de la autora en analisis_400_v3.json: sello {a['adjudicacion_200']['sello_sha256']}, hoja "
      f"{a['adjudicacion_200']['hoja_sha256']}, adjudicadas {a['adjudicacion_200']['adjudicadas']}")
print(f"la composición: {a['cifra_principal']['composicion']['lectura_de_la_autora']}, v3 {a['cifra_principal']['composicion']['v3']}, "
      f"adjudicadas por la autora {a['cifra_principal']['composicion']['adjudicadas_por_la_autora']}")
print("LAS CIFRAS, LEÍDAS; LA DE LAS 400 ENTRE LAS DOS COTAS" if all(ok.values()) else "ALGÚN CONTROL NO PASA")
sys.exit(0 if all(ok.values()) else 1)
