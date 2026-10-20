"""B6.1, tanda final, T3: el plan de lo que pasa al repo (el <plan.json> de escribir_en_el_repo_tf.py armar), por etapa. Solo escribe el
plan. Cada entrada: el origen (en la copia o en el scratchpad), el destino relativo al repo y el modo («tal_cual» para los ensamblados,
los manifiestos, la E0 combinada y lo que un script generó con rutas relativas; «saneado» para lo que puede llevar la ruta del
scratchpad o la carpeta personal).
  - ensamblados: los ocho ensamblados de la primera corrida (con el `.gz` y el sello de los que pasan de 100 MB), los manifiestos de
    extracción y de ensamblado de los acumulados y de la prueba de la raya, la E0 combinada de los acumulados y los registros del armado
    (la entrada combinada no: es la salida de la extracción, por copia);
  - gate: las salidas de T3 en la copia (salidas, corridas, gate, gate_decisiones, nombres_remision, intrinsecas_gen3, selftests, las
    consolas de la E0 con las partes) y la fixture;
  - resto: grafos.py, el registro de la vista, neo4j, conteos_sin_leer, el NO_ABRIR_ (tal cual, sin abrirlo), muestras y la versión
    derivada de la lectura.
  Desde el punto 5 (decisiones de la autora sobre el FRENO T3 parcial), dos etapas más, que reemplazan lo que escribió el parcial (antes,
  escribir_en_el_repo_tf.py apartar lo saca del repo, con su control):
  - tramo1_raya: los dos ensamblados del tramo 1 con la variante con la raya;
  - gate2: lo de «gate», rehecho con el tramo 1 con la raya y la R23 y la V23 declaradas, sin la fixture (no cambia: ya está en el repo).
Uso: python3 -I -B plan_escritura_tf.py <copia> <scratchpad> ensamblados|gate|tramo1_raya|gate2|resto <plan.json>
"""
import json
import sys
from pathlib import Path

C, SP, ETAPA, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), sys.argv[3], Path(sys.argv[4])
X = "data/experiment/reextraccion_v2/corpus_tanda_final"
T3 = "data/experiment/tanda_final/t3"
A = f"{T3}/acumulado"
plan = []


def poner(origen: Path, destino: str, modo: str) -> None:
    plan.append({"origen": str(origen), "destino": destino, "modo": modo})


if ETAPA == "ensamblados":
    for e in ("ens_98_r2b", "ens_98_r2b_sincola", "ens_tramo1_r2b", "ens_tramo1_r2b_sincola"):
        poner(C / X / e, f"{X}/{e}", "tal_cual")
    for e in ("ens_128_r2b", "ens_128_r2b_sincola", "ens_60_tramo1_r2b", "ens_60_tramo1_r2b_sincola", "manifiestos",
              "e0_acumulado_128_r2b", "e0_acumulado_60_r2b", "armado_acumulado_128_tf.json", "armado_acumulado_60_tf.json"):
        poner(C / A / e, f"{A}/{e}", "tal_cual")
    poner(C / T3 / "prueba_raya_tramo1/manifiestos", f"{T3}/prueba_raya_tramo1/manifiestos", "tal_cual")
elif ETAPA == "tramo1_raya":
    for e in ("ens_tramo1_r2b", "ens_tramo1_r2b_sincola"):
        poner(C / X / e, f"{X}/{e}", "tal_cual")
elif ETAPA in ("gate", "gate2"):
    # corridas/: el lote de los ensamblados, su registro y las consolas, ya saneados en la copia
    for e in ("salidas", "corridas", "gate", "gate_decisiones", "nombres_remision", "intrinsecas_gen3", "selftests"):
        poner(C / T3 / e, f"{T3}/{e}", "saneado")
    for p in sorted((C / T3 / "e0_con_partes").glob("consola_*.txt")):
        poner(p, f"{T3}/e0_con_partes/{p.name}", "saneado")
    if ETAPA == "gate":
        poner(C / "scripts/regression_kg_esperado.json", "scripts/regression_kg_esperado.json", "tal_cual")
elif ETAPA == "resto":
    poner(C / "data/experiment/neo4j/grafos.py", "data/experiment/neo4j/grafos.py", "tal_cual")
    poner(C / T3 / "registro_vista_r2b_tanda_final.py", f"{T3}/registro_vista_r2b_tanda_final.py", "tal_cual")
    for e in ("neo4j", "conteos_sin_leer", "muestras"):
        poner(C / T3 / e, f"{T3}/{e}", "saneado")
    poner(C / T3 / "NO_ABRIR_conteos_t3.json", f"{T3}/NO_ABRIR_conteos_t3.json", "tal_cual")
    for n in ("preregistro_tanda_final_derivada_T4.md", "preregistro_tanda_final_derivada_T4.huecos.json"):
        poner(SP / "t3/derivada_T4" / n, f"data/experiment/tanda_final/preregistro/{n}", "tal_cual")
else:
    raise SystemExit(f"etapa desconocida: {ETAPA}")
OUT.write_text(json.dumps(plan, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(len(plan), "entradas en el plan de", ETAPA)
