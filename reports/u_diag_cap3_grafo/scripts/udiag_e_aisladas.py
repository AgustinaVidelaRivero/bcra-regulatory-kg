"""Tarea e: «condiciones aisladas» con la definición vigente y con la redefinición propuesta, en los grafos de las
columnas del tablero de correcciones (r1, tanda 0 con el perfil r1, r2a, r2b, sin cola).

Definición vigente: `scripts/metricas_intrinsecas.py:243` (aislado = grado 0 en la versión no dirigida del grafo de
aristas únicas) y [c3] de `docs/tablero_correcciones.md:52` («Nodos Condicion sin ninguna arista»).
Redefinición propuesta:
  (A) Condicion sin ninguna arista de contenido: ninguna arista, entrante o saliente, salvo `establecida_en`,
      `remite_a` y, en los grafos del perfil r1, la remisión en su forma anterior (`referencia` con
      `rol_fuente = referencia_cruzada`); (A-literal) la misma sin esa tercera exclusión;
  (B) Condicion sin `condicion_de` saliente.
Uso: PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B udiag_e_aisladas.py
Escribe salida/aisladas_e.json.
"""
import collections
import json
import os

from udiag_comun import AQUI, SRC, sha

GRAFOS = [  # (columna del tablero, nombre, archivo, sha256 esperado)
    ("r1", "KG-Reextraído-r1", "kg_r1.json", "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"),
    ("tanda 0 (perfil r1)", "desarrollo r1", "kg_desarrollo_r1.json",
     "eab2fdd01dec4dad026d596a793919e666920fab127d7efb14b5b00857ae64ef"),
    ("tanda 0 (perfil r1)", "cinco r1", "kg_cinco_r1.json",
     "4097d4fd3f300cb1c2cf09bef59e3ccb9a30b1de18334e6230102a5a3106d00a"),
    ("tanda 0 (perfil r1)", "diez r1", "kg_diez_r1.json",
     "dd42d6d9c0c8379da90ec4ed4e4659157a960a0d1ceaf8af5a008bdd9cad9010"),
    ("r2a", "diez r2a", "kg_diez_r2a.json", "99fe2bfa0de05704e4c636bdf9b0455a30e29b378e3b0e61eadc49dad3f7c649"),
    ("r2a", "desarrollo r2a", "kg_desarrollo_r2a.json",
     "93a7af7279a415ee72cfec547bcd080d4c85a96746e219ed94dea4239007e8dd"),
    ("r2b", "diez r2b", "kg_diez_r2b.json", "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57"),
    ("r2b", "desarrollo r2b", "kg_desarrollo_r2b.json",
     "6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2"),
    ("r2b sin cola", "diez r2b sin cola", "kg_diez_r2b_sincola.json",
     "e22fae1afc3cf37fbe5b49ee0b220d51d0ec5febc13abeb6ebf7b74226da34fb"),
    ("r2b sin cola", "desarrollo r2b sin cola", "kg_desarrollo_r2b_sincola.json",
     "2922b72dca2c2bcb204a04f53fc89f265ac2c57e83e6aaab2ce1af8b82d413e4"),
]
NO_CONTENIDO = {"establecida_en", "remite_a"}


def es_remision_r1(e):
    return e["relation"] == "referencia" and e.get("rol_fuente") == "referencia_cruzada"


def medir(kg):
    tipo = {n["id"]: n["type"] for n in kg["nodes"]}
    unicas = {(e["source"], e["target"], e["relation"]): e for e in kg["edges"]}
    grado = collections.Counter()
    contenido = collections.Counter()
    contenido_lit = collections.Counter()
    cdd = set()
    for (s, t, r), e in unicas.items():
        grado[s] += 1
        grado[t] += 1
        if r not in NO_CONTENIDO:
            contenido_lit[s] += 1
            contenido_lit[t] += 1
            if not es_remision_r1(e):
                contenido[s] += 1
                contenido[t] += 1
        if r == "condicion_de":
            cdd.add(s)
    cond = [n for n in tipo if tipo[n] == "Condicion"]
    aislados = [n for n in tipo if grado[n] == 0]
    return {
        "nodos": len(tipo), "aristas": len(kg["edges"]), "condicion": len(cond),
        "vigente_condicion_sin_ninguna_arista": sum(1 for n in cond if grado[n] == 0),
        "vigente_aislados_de_todo_tipo": len(aislados),
        "vigente_aislados_por_tipo": dict(collections.Counter(tipo[n] for n in aislados).most_common()),
        "A_condicion_sin_arista_de_contenido": sum(1 for n in cond if contenido[n] == 0),
        "A_literal_sin_establecida_en_ni_remite_a": sum(1 for n in cond if contenido_lit[n] == 0),
        "B_condicion_sin_condicion_de_saliente": sum(1 for n in cond if n not in cdd),
        "condicion_con_arista_de_contenido_que_no_es_condicion_de": sum(
            1 for n in cond if contenido[n] > 0 and n not in cdd),
        "remisiones_r1_desde_condicion": sum(1 for (s, t, r), e in unicas.items()
                                             if tipo.get(s) == "Condicion" and es_remision_r1(e)),
        "remite_a_desde_o_hacia_condicion": sum(1 for (s, t, r) in unicas if r == "remite_a"
                                                and "Condicion" in (tipo.get(s), tipo.get(t))),
    }


def main():
    out = {"grafos": []}
    for col, nombre, archivo, esperado in GRAFOS:
        p = os.path.join(SRC, "grafos_tablero", archivo)
        h = sha(p)
        assert h == esperado, (nombre, h)
        m = medir(json.load(open(p, encoding="utf-8")))
        out["grafos"].append({"columna": col, "grafo": nombre, "sha256": h, **m})
        print(f"{nombre:26s} Condicion {m['condicion']:5d} | vigente {m['vigente_condicion_sin_ninguna_arista']:4d} "
              f"(aislados {m['vigente_aislados_de_todo_tipo']}) | A {m['A_condicion_sin_arista_de_contenido']:4d} "
              f"| A-lit {m['A_literal_sin_establecida_en_ni_remite_a']:4d} | B {m['B_condicion_sin_condicion_de_saliente']:4d}")
    json.dump(out, open(os.path.join(AQUI, "salida", "aisladas_e.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
