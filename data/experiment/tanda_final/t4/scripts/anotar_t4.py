"""B6.1, tanda final, T4, primer tramo: agrega propuestas de la lectura asistida al borrador de una muestra (<borrador>/<muestra>.jsonl),
desde un arreglo JSON por la entrada estándar. Cada propuesta: n, propuesta, justificacion y, si hay, omisiones y observacion. Frena si
un n ya está o si la respuesta no es una de las válidas de la muestra (las del LEEME). No escribe en el repo.
Uso: python3 -I -B anotar_t4.py <borrador> <muestra> < propuestas.json
"""
import json
import sys
from pathlib import Path

B, M = Path(sys.argv[1]), sys.argv[2]
CAPAS = ["E0", "E1-prompt", "E1-validador", "catálogo", "E2", "E3", "ensamblado"]
U = ["con error", "sin error", "dudosa"]
VALIDAS = {"cola": U, "aceptadas_items": U, "aceptadas_no_items": U, "vigilancia_2": ["vaciamiento", "no vaciamiento", "no decidible"],
           "vigilancia_7": ["con apoyo", "sin apoyo", "no decidible"], "vigilancia_1": ["sí", "no", "no decidible"],
           "vigilancia_3": ["duplicación", "distintos"],
           "observacion_12": ["correcta", "no decidible"] + [f"incorrecta ({c})" for c in CAPAS]}
p = B / f"{M}.jsonl"
ya = {json.loads(x)["n"] for x in p.read_text(encoding="utf-8").splitlines() if x.strip()} if p.exists() else set()
nuevas = json.loads(sys.stdin.read())
for x in nuevas:
    assert x["n"] not in ya, f"ya está la {x['n']}"
    assert x["propuesta"] in VALIDAS[M], f"{x['n']}: {x['propuesta']!r} no es válida"
    assert x["justificacion"].strip(), f"{x['n']}: sin justificación"
    ya.add(x["n"])
with p.open("a", encoding="utf-8") as f:
    for x in nuevas:
        f.write(json.dumps(x, ensure_ascii=False) + "\n")
print(M, "ahora", len(ya), "propuestas:", sorted(ya))
