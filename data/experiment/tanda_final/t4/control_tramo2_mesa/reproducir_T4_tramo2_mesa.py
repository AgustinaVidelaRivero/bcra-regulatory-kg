"""Mesa, §227 (21/10/2026): reproduce el segundo tramo de T4 de la tanda final sobre una copia, sin imprimir ninguna cifra ni veredicto:
corre de nuevo las tasas (tasas_t4t2_tf.py), su verificación independiente y el sorteo de la ampliación con los scripts del repo, y
compara sus salidas con las del repo (igual o distinto; la hora fuera). USD 0, sin escribir en el repo: lee el repo solo con git show y
para copiar; las salidas van a una carpeta temporal.
Uso: python3 -I -B reproducir_T4_tramo2_mesa.py <repo> <copia con tanda_final, controles_tanda1 y tanda1/t3/scripts> <salida.json>"""
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO, C, OUT = Path(sys.argv[1]), Path(sys.argv[2]).resolve(), Path(sys.argv[3])
T4 = "data/experiment/tanda_final/t4"
sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731
git = lambda *a: subprocess.run(["git", "--no-optional-locks", "-C", str(REPO), *a], capture_output=True, check=True).stdout  # noqa: E731
res = {}


def sin_hora(x):
    if isinstance(x, dict):
        return {k: sin_hora(v) for k, v in x.items() if k not in ("hora", "generado")}
    if isinstance(x, list):
        return [sin_hora(v) for v in x]
    return x


def correr(*a):
    p = subprocess.run([sys.executable, "-I", "-B", *map(str, a)], capture_output=True, text=True)
    return p.returncode


with tempfile.TemporaryDirectory(prefix="t4t2_mesa_") as t:
    T = Path(t)
    rc = correr(C / T4 / "scripts/tasas_t4t2_tf.py", C, T / "trabajo", T / "tasas.json", T / "dist.json")
    res["tasas_rc_0"] = rc == 0
    rep = json.loads((REPO / T4 / "tasas/tasas_t4_tramo2.json").read_text(encoding="utf-8"))
    res["tasas_iguales_sin_la_hora"] = rc == 0 and sin_hora(json.loads((T / "tasas.json").read_text(encoding="utf-8"))) == sin_hora(rep)
    res["distribuciones_byte_a_byte"] = rc == 0 and (T / "dist.json").read_bytes() == (REPO / T4 / "tasas/distribuciones_bajo_H0_t4_tramo2.json").read_bytes()
    rc = correr(C / T4 / "scripts/verif_tasas_independiente_t4t2_tf.py", C, T / "verif.json")
    v = json.loads((T / "verif.json").read_text(encoding="utf-8")) if rc == 0 else {}
    res["verificacion_independiente_igual_sin_la_hora"] = rc == 0 and sin_hora(v) == sin_hora(
        json.loads((REPO / T4 / "tasas/verif_tasas_independiente_t4t2_tf.json").read_text(encoding="utf-8")))
    pf, fi = T / "para_firmar.md", T / "firmado.md"
    pf.write_bytes(git("show", "5289b02f:docs/preregistro_tanda_final.md"))
    fi.write_bytes(git("show", "4de7f2a7:docs/preregistro_tanda_final.md"))
    res["base_0897d609_y_firmado_b760edf7"] = sha(pf.read_bytes()).startswith("0897d609") and sha(fi.read_bytes()).startswith("b760edf7")
    rc = correr(C / T4 / "scripts/sorteo_ampliacion_t4t2_tf.py", C, pf, fi, REPO / T4 / "tasas/tasas_t4_tramo2.json", T / "sorteo")
    m = T / "sorteo/aceptadas_no_items_ampliacion.json"
    res["sorteo_da_la_muestra_d8c8c337_byte_a_byte"] = rc == 0 and m.exists() and m.read_bytes() == (REPO / T4 / "ampliacion/muestras/aceptadas_no_items_ampliacion.json").read_bytes() \
        and sha(m.read_bytes()).startswith("d8c8c337")
res["copia_sin_cambios"] = sha(subprocess.run(["find", str(C), "-type", "f", "-newer", str(C / "docs/preregistro_tanda_final.md")],
                                               capture_output=True).stdout) == sha(b"")
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for k, x in res.items():
    print("OK " if x else "MAL", k)
sys.exit(0 if all(res.values()) else 1)
