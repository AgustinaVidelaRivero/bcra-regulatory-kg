"""Mesa, §131: resume las dos mediciones (la regla de la mesa y la variante con la raya) por corpus. USD 0, solo lee.

Uso: python3 -I -B resumir_medicion_mesa.py <medición con la regla.json> <medición con la variante.json> <out.json>

Por corpus: cuántas menciones de norma hay, cuántas resuelve cada juego de nombres (inventario solo, a mano, la regla y la variante con
la raya), y la lista de las que cambian entre juegos, con el TO de origen, el nombre citado, el destino y la vía.
"""
import json
import sys

A, G, OUT = (json.load(open(sys.argv[1], encoding="utf-8")), json.load(open(sys.argv[2], encoding="utf-8")), sys.argv[3])


def cambios(X: dict, Y: dict) -> list[dict]:
    return [{"to_origen": X[k]["to_origen"], "norma": X[k]["norma"], "antes": [X[k]["to_destino"], X[k]["via"]],
             "despues": [Y[k]["to_destino"], Y[k]["via"]]}
            for k in sorted(X) if (X[k]["to_destino"], X[k]["via"]) != (Y[k]["to_destino"], Y[k]["via"])]


out = {}
for c, cv in A["corpus"].items():
    J = cv["juegos"]; Jg = G["corpus"][c]["juegos"]
    res = lambda ms: sum(1 for m in ms.values() if m["to_destino"])  # noqa: E731
    out[c] = {"tos": len(cv["tos"]), "menciones": len(J["inventario"]["menciones"]),
              "resueltas": {"inventario": res(J["inventario"]["menciones"]), "a_mano": res(J["a_mano"]["menciones"]),
                            "regla": res(J["regla"]["menciones"]), "regla_con_raya": res(Jg["regla"]["menciones"])},
              "tos_con_nombres_de_la_regla": sorted(t for t, v in J["regla"]["nombres_remision"].items() if v),
              "tos_con_nombres_a_mano": sorted(t for t, v in J["a_mano"]["nombres_remision"].items() if v),
              "cambios_inventario_a_regla": cambios(J["inventario"]["menciones"], J["regla"]["menciones"]),
              "cambios_a_mano_a_regla": cambios(J["a_mano"]["menciones"], J["regla"]["menciones"]),
              "cambios_regla_a_regla_con_raya": cambios(J["regla"]["menciones"], Jg["regla"]["menciones"])}
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for c, v in out.items():
    r = v["resueltas"]
    print(f"{c:<17} TOs {v['tos']:>3}  menciones {v['menciones']:>5}  resueltas: inventario {r['inventario']:>4}, a mano {r['a_mano']:>4}, "
          f"regla {r['regla']:>4}, con raya {r['regla_con_raya']:>4} | cambios inv→regla {len(v['cambios_inventario_a_regla'])}, "
          f"a mano→regla {len(v['cambios_a_mano_a_regla'])}, regla→raya {len(v['cambios_regla_a_regla_con_raya'])}")
