"""B6.1, tanda 1, T5, punto 3: las dos corridas de cifras_t5.py, a dos salidas distintas, dan los mismos bytes. Compara archivo por
archivo <salidas 1> con <salidas 2> y las propuestas del backlog que cada corrida escribe al lado (../propuestas_backlog_t5.jsonl), y la
parte del NO_ABRIR_ de cada corrida, solo por su sha256 (no la abre). Escribe <salida.json> y la imprime.
Uso: python3 -I -B dos_corridas_t5.py <salidas 1> <salidas 2> <NO_ABRIR parte 1> <NO_ABRIR parte 2> <salida.json>
"""
import hashlib
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
S1, S2, N1, N2, OUT = (Path(x) for x in sys.argv[1:6])
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()  # noqa: E731
n1 = sorted(p.name for p in S1.iterdir() if p.is_file())
n2 = sorted(p.name for p in S2.iterdir() if p.is_file())
arch = {n: {"sha256": sha(S1 / n), "igual": (S2 / n).exists() and (S1 / n).read_bytes() == (S2 / n).read_bytes()} for n in n1}
pb = "propuestas_backlog_t5.jsonl"
arch[f"../{pb}"] = {"sha256": sha(S1.parent / pb), "igual": (S1.parent / pb).read_bytes() == (S2.parent / pb).read_bytes()}
res = {"mismos_nombres": n1 == n2, "archivos": arch,
       "parte_del_NO_ABRIR_de_cada_corrida_igual_por_sha256": sha(N1) == sha(N2),
       "todo_igual": n1 == n2 and all(v["igual"] for v in arch.values()) and sha(N1) == sha(N2)}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
