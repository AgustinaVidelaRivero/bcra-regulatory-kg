"""Mesa, §158 (18/10/2026): el sello del cierre de la lectura de U-MED-DESAMB en la forma que pide el juez (`juez/juez_desamb_mesa.py`,
`--sello-lectura`: un JSON con «sellado» en `%Y-%m-%d %H:%M:%S %z`, `:348-354`). Lo deriva del sello de la autora (`sello_desamb.txt`, que
no cambia): la última línea es la hora; las cuatro anteriores, los sha256 de lo sellado. Controla que la hora se lea con el mismo formato que
el juez y que sea anterior al miércoles 21/10/2026 a las 18:00 (diseño sellado, §8). USD 0, sin API.
Uso: python3 -I -B derivar_sello_para_el_juez_mesa.py <sello_desamb.txt> <salida.json>"""
import hashlib
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ent, out = Path(sys.argv[1]), Path(sys.argv[2])
b = ent.read_bytes()
lineas = b.decode("utf-8").splitlines()
assert len(lineas) == 5 and all(re.fullmatch(r"[0-9a-f]{64}  \S+", l) for l in lineas[:4]), "el sello no tiene la forma esperada"
t = datetime.strptime(lineas[4], "%Y-%m-%d %H:%M:%S %z")                     # el mismo formato que lee el juez
assert t <= datetime(2026, 10, 21, 18, 0, tzinfo=timezone(timedelta(hours=-3))), "la lectura cerró después del límite del juez"
d = {"sellado": lineas[4],
     "derivado_de": {"archivo": "../sellada/sello_desamb.txt", "sha256": hashlib.sha256(b).hexdigest()},
     "sellados_por_la_autora": {l.split("  ", 1)[1]: l.split("  ", 1)[0] for l in lineas[:4]},
     "nota": ("Derivado por la mesa (§158) para el argumento --sello-lectura del juez, que pide un JSON con «sellado». "
              "El sello de la autora es el de sellada/, que no cambia; manda ese.")}
out.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(d, ensure_ascii=False))
