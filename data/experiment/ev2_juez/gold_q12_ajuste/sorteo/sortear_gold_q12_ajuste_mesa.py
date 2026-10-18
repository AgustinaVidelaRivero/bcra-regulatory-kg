"""Sorteo de las 20 respuestas de la mitad de ajuste del gold de Q12 (mesa, §128, 16/10/2026). USD 0, sin API.

La regla está en regla_sorteo_gold_q12_ajuste_mesa.md, al lado de este script; los dos se sellan antes de correrlo.

Uso: python3 -I -B sortear_gold_q12_ajuste_mesa.py <repo> <salida.json>

Lee del repo, solo lectura:
  - data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json: el id y el TO de cada pregunta;
  - data/experiment/ev2_fidelidad_eval/desanonimizacion/tabla_id_opaco.json: las 120 respuestas base, con su pregunta y su grafo;
  - data/experiment/ev2_adjudicacion/adjudicacion/reporte_muestra_simetrica.json: de cada ficha, solo el campo id_opaco_base.
No lee ningún veredicto: del tercer archivo toma solo ese campo, y no imprime nada de él.
La salida lleva el grafo de cada respuesta: es la clave, y va a clave_para_despues/.
"""
import hashlib
import json
import random
import sys
from pathlib import Path

SEMILLA = "gold-q12-ajuste-ev2-v1"
N = 20
TOS = ["ext", "cap", "cla", "ric", "pro"]                 # el orden fijo de los TOs de EV2
GRAFOS = ["run_3", "v3", "v2"]                            # KG-Base, KG-Refinado y KG-Reextraído
NOMBRE_GRAFO = {"run_3": "KG-Base", "v3": "KG-Refinado", "v2": "KG-Reextraído"}
ENTRADAS = {
    "preguntas": "data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json",
    "tabla": "data/experiment/ev2_fidelidad_eval/desanonimizacion/tabla_id_opaco.json",
    "muestra_simetrica": "data/experiment/ev2_adjudicacion/adjudicacion/reporte_muestra_simetrica.json",
}


def rng(uso: str) -> random.Random:
    """Un generador por uso, todos de la misma semilla: cambiar un paso no mueve los otros."""
    return random.Random(f"{SEMILLA}|{uso}")


def restos_mayores(pesos: dict, total: int, desempate: list) -> dict:
    """Cuotas enteras proporcionales a `pesos` que suman `total`; los empates de resto, en el orden de `desempate`."""
    s = sum(pesos.values())
    base = {k: (total * v) // s for k, v in pesos.items()}
    resto = {k: (total * v) % s for k, v in pesos.items()}
    falta = total - sum(base.values())
    orden = sorted(pesos, key=lambda k: (-resto[k], desempate.index(k)))
    for k in orden[:falta]:
        base[k] += 1
    return base


def main() -> None:
    repo, salida = Path(sys.argv[1]), Path(sys.argv[2])
    sha = {k: hashlib.sha256((repo / p).read_bytes()).hexdigest() for k, p in ENTRADAS.items()}
    preguntas = json.loads((repo / ENTRADAS["preguntas"]).read_text(encoding="utf-8"))["preguntas"]
    to_de = {p["id"]: p["to"] for p in preguntas}
    filas = json.loads((repo / ENTRADAS["tabla"]).read_text(encoding="utf-8"))["filas"]
    excluidas = {x["id_opaco_base"] for x in
                 json.loads((repo / ENTRADAS["muestra_simetrica"]).read_text(encoding="utf-8"))["muestra"]}
    assert len(filas) == 120 and len(excluidas) == 12 and excluidas <= {f["id_opaco"] for f in filas}
    resp = {(f["id_pregunta"], f["grafo"]): f for f in filas}
    assert len(resp) == 120 and {g for _, g in resp} == set(GRAFOS)
    excl_par = {(f["id_pregunta"], f["grafo"]) for f in filas if f["id_opaco"] in excluidas}

    # 1. Cuotas por TO: proporcionales a la dosificación de EV2, por restos mayores; el empate, con la semilla.
    n_to = {t: sum(1 for p in preguntas if p["to"] == t) for t in TOS}
    desempate_to = TOS[:]
    rng("to_empate").shuffle(desempate_to)
    cuota_to = restos_mayores(n_to, N, desempate_to)

    # 2. Cuotas por grafo: 7, 7 y 6; el grafo con 6 sale de la semilla.
    orden_g = GRAFOS[:]
    rng("grafo_6").shuffle(orden_g)
    cuota_g = {g: (N // 3) + (1 if i < N % 3 else 0) for i, g in enumerate(orden_g)}

    # 3. Celdas: en cada TO, la cuota se reparte entre los grafos lo más parejo posible; lo que sobra de la parte pareja va a los
    #    grafos con más cuota pendiente, y los empates, con la semilla. Los TOs con más sobrante van primero.
    celda = {(t, g): cuota_to[t] // 3 for t in TOS for g in GRAFOS}
    pendiente = {g: cuota_g[g] - sum(celda[(t, g)] for t in TOS) for g in GRAFOS}
    r_celdas = rng("celdas")
    for t in sorted(TOS, key=lambda t: (-(cuota_to[t] % 3), TOS.index(t))):
        desempate = GRAFOS[:]
        r_celdas.shuffle(desempate)
        for g in sorted(GRAFOS, key=lambda g: (-pendiente[g], desempate.index(g)))[:cuota_to[t] % 3]:
            celda[(t, g)] += 1
            pendiente[g] -= 1
    assert all(v == 0 for v in pendiente.values()), pendiente
    assert all(sum(celda[(t, g)] for g in GRAFOS) == cuota_to[t] for t in TOS)
    assert all(max(celda[(t, g)] for g in GRAFOS) - min(celda[(t, g)] for g in GRAFOS) <= 1 for t in TOS)

    # 4. Las respuestas: 20 preguntas distintas. En cada TO, los lugares de la celda se recorren en un orden de la semilla, y cada
    #    uno toma la primera pregunta de una permutación de la semilla que no se usó y cuya respuesta en ese grafo no está excluida.
    elegidas = []
    for t in TOS:
        perm = sorted(q for q in to_de if to_de[q] == t)
        rng(f"preguntas|{t}").shuffle(perm)
        lugares = [g for g in GRAFOS for _ in range(celda[(t, g)])]
        rng(f"lugares|{t}").shuffle(lugares)
        usadas = set()
        for g in lugares:
            q = next(q for q in perm if q not in usadas and (q, g) not in excl_par)
            usadas.add(q)
            elegidas.append(resp[(q, g)])
    assert len(elegidas) == N and len({f["id_pregunta"] for f in elegidas}) == N
    assert not ({f["id_opaco"] for f in elegidas} & excluidas)

    # 5. El orden de las fichas: una permutación de la semilla; los ids van de G01 a G20.
    rng("orden").shuffle(elegidas)
    fichas = [{"ficha": f"G{i + 1:02d}", "id_opaco": f["id_opaco"], "id_pregunta": f["id_pregunta"],
               "to": to_de[f["id_pregunta"]], "grafo": f["grafo"], "grafo_nombre": NOMBRE_GRAFO[f["grafo"]],
               "label": f["label"], "sha256_respuesta": f["sha256_respuesta"], "n_criterios": f["n_criterios"]}
              for i, f in enumerate(elegidas)]
    out = {"semilla": SEMILLA, "sha256_entradas": sha, "poblacion": 120 - len(excluidas), "excluidas_muestra_simetrica": 12,
           "cuota_por_to": cuota_to, "cuota_por_grafo": {NOMBRE_GRAFO[g]: v for g, v in cuota_g.items()},
           "celdas": {f"{t}|{NOMBRE_GRAFO[g]}": celda[(t, g)] for t in TOS for g in GRAFOS}, "fichas": fichas}
    salida.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("sorteo hecho:", len(fichas), "fichas;", "criterios:", sum(f["n_criterios"] for f in fichas))


if __name__ == "__main__":
    main()
