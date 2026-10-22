"""Mesa, §237 (22/10/2026): el FRENO de T5 da para t5/scripts/freno_t5_armar.py el sha256 de su foto de después (8076089b…), y el del repo
y el del paquete es otro (23ca9355…): el script se editó a las 14:06:47, después de esa foto. Esto controla que el script de hoy sea el
que dio el FRENO: lo corre sobre <copia> (sin el FRENO de la copia, con el NO_ABRIR_ de T5 copiado byte a byte, que el script solo
hashea) con las entradas del paquete de T5, y compara el FRENO que da con el del repo. Escribe solo en <copia>.
Uso: python3 -I -B regenerar_freno_T5_mesa.py <repo> <copia> <paquete de T5> <python> <salida.json>"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

R, C, P, PY, OUT = Path(sys.argv[1]), Path(sys.argv[2]).resolve(), Path(sys.argv[3]), sys.argv[4], Path(sys.argv[5])
T5 = "data/experiment/tanda_final/t5"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
assert not (C / ".git").exists()
na = C / T5 / "NO_ABRIR_conteos_t5.json"
subprocess.run(["cp", "-c", str(R / T5 / "NO_ABRIR_conteos_t5.json"), str(na)], check=True)
fr = C / T5 / "FRENO_T5.md"
fr.unlink(missing_ok=True)
p = subprocess.run([PY, "-I", "-B", str(C / T5 / "scripts/freno_t5_armar.py"), str(C), *(str(P / n) for n in (
    "paso0_T5_salida_T5.txt", "foto_contra_commits_T5.json", "seccion_foto_T5.md", "grep_convenciones_T5.json", "foto_contra_despues_T5.json",
    "control_copia_T5.json"))], capture_output=True)
na.unlink()
res = {"freno_t5_armar_del_repo": sha(R / T5 / "scripts/freno_t5_armar.py"), "el_que_da_el_FRENO_en_su_tabla": "8076089b7c2c0a65184fec183ff71df7de94175b6adf46a39fabe6ade06c079c",
       "armar_rc_0": p.returncode == 0, "el_FRENO_que_da_es_el_del_repo": fr.exists() and fr.read_bytes() == (R / T5 / "FRENO_T5.md").read_bytes()}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
sys.exit(0 if res["armar_rc_0"] and res["el_FRENO_que_da_es_el_del_repo"] else 1)
