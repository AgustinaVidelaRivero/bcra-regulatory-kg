"""Mesa, §158 (18/10/2026): el control de la lectura sellada de U-MED-DESAMB (`fuera_del_repo/lectura_desamb/`, sellada a las 14:04:01)
contra su sello y contra la plantilla del paquete de la mesa (`decisiones_140_mesa/lectura/`). Pedido de la autora del 18/10/2026,
recibido a las 14:05:06. USD 0, sin API, sin escribir en el repo ni en la carpeta de la lectura (la conversión se re-corre sobre una copia).
No abre las claves aparte (`decisiones_140_mesa/clave_aparte_…/`, `decisiones_141_mesa/clave_aparte_…/`): las 13 entradas que tienen que
quedar vacías salen de `decisiones_141_mesa/lectura/numeros_que_se_saltean.txt` (solo los números), y no informa ninguna cuenta por clase.
Uso: python3 -I -B control_lectura_desamb_mesa.py <paquete H> <copia permanente P> <salida.json>"""
import csv
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

H, P, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
L = Path.home() / "INGENIERIA IA/TESIS/fuera_del_repo/lectura_desamb"
SHA = {"hoja_clases_marcada.csv": "baab241150414c54c1aa02e31dc4c4172d9cf464e1d4e03f3f4c43d17ef2a200",
       "censo_c1_marcado.csv": "86e493b0f30b5d0fdc7d327566ed1b429c266c6716be7e78a823e43dc16918a1",
       "convertir_desamb.py": "1eb31a9ff86b58d26a5a06fa5a7e82819e0f58daf030e113e666c986d5341b1e"}
PLANT = {"hoja_clases.csv": "ba317008b7a21bbe361bc33923790745145a534abb114e9b36a7f422ac16f2d7",
         "censo_c1.csv": "08eda995f0de732b8b69225ffd1ed5eb1cb51cc1b139d2560a9bec2ccc22cd44"}
CLASES, DECIS = {"correcta", "generica", "incorrecta", "no_decidible"}, {"une_bien", "une_mal"}
sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731
shaf = lambda p: sha(Path(p).read_bytes())  # noqa: E731
res, mal = {}, []


def ok(k, c, d=None):
    res[k] = {"pasa": bool(c), **({"detalle": d} if d is not None else {})}
    if not c:
        mal.append(k)


sello = (L / "sello_desamb.txt").read_text(encoding="utf-8")
ok("1a el sello: los sha256 de las dos marcadas y de las dos exportaciones, con sus archivos",
   all(f"{shaf(L / n)}  {n}" in sello for n in ("hoja_clases_marcada.csv", "censo_c1_marcado.csv", "hoja_clases.csv", "censo_c1.csv")))
ok("1b el sello: la hora 2026-10-18 14:04:01", "2026-10-18 14:04:01" in sello)
ok("1c las dos marcadas, de solo lectura, con los sha256 del mensaje",
   all(shaf(L / n) == SHA[n] for n in ("hoja_clases_marcada.csv", "censo_c1_marcado.csv"))
   and all(not ((L / n).stat().st_mode & 0o222) for n in ("hoja_clases_marcada.csv", "censo_c1_marcado.csv")))
ok("1d la conversión: 1eb31a9f…", shaf(L / "convertir_desamb.py") == SHA["convertir_desamb.py"])
PK = H / "decisiones_140_mesa/lectura"
ok("2a las plantillas del paquete, las selladas (en la copia de trabajo y en la permanente)",
   all(shaf(PK / n) == h == shaf(P / "decisiones_140_mesa/lectura" / n) for n, h in PLANT.items()))
ok("2b el material de la carpeta (planilla, anexo y censo .md), igual al del paquete",
   all(shaf(L / n) == shaf(PK / n) for n in ("planilla_lectura.md", "anexo_entradas.md", "censo_c1.md")))
saltea = set(re.findall(r"\bD\d{3}\b", (H / "decisiones_141_mesa/lectura/numeros_que_se_saltean.txt").read_text(encoding="utf-8")))
conv = (L / "convertir_desamb.py").read_text(encoding="utf-8")
salteo_conv = set(re.findall(r'"(D\d{3})"', conv.split("SALTEO =", 1)[1].split("\n", 1)[0]))
ok("2c los 12 que se saltean: los de la §141, y los mismos en la conversión", len(saltea) == 12 and saltea == salteo_conv, sorted(saltea))
leer = lambda p: list(csv.reader(io.StringIO(Path(p).read_text(encoding="utf-8"), newline="")))  # noqa: E731
pl, mh = leer(PK / "hoja_clases.csv"), leer(L / "hoja_clases_marcada.csv")
ok("3a la hoja marcada: la cabecera y 91 filas de 6 columnas", mh[0] == pl[0] and len(mh) == 92 and all(len(r) == 6 for r in mh))
ok("3b la hoja marcada: item, letra, entrada y etiqueta iguales a la plantilla, fila por fila", [r[:4] for r in mh] == [r[:4] for r in pl])
vacias = [r for r in mh[1:] if not r[4]]
ok("3c 13 entradas vacías, y son las de los 12 que se saltean", len(vacias) == 13 and {r[0] for r in vacias} == saltea
   and all(not r[5] for r in vacias))
clasif = [r for r in mh[1:] if r[0] not in saltea]
ok("3d 78 entradas clasificadas, todas con una clase válida", len(clasif) == 78 and all(r[4] in CLASES for r in clasif))
pc, mc = leer(PK / "censo_c1.csv"), leer(L / "censo_c1_marcado.csv")
ok("4 el censo marcado: 2 colisiones, las columnas fijas de la plantilla y una decisión válida",
   mc[0] == pc[0] and len(mc) == 3 and [r[:3] for r in mc] == [r[:3] for r in pc] and all(r[3] in DECIS for r in mc[1:]))
with tempfile.TemporaryDirectory(prefix="conv_desamb_") as t:
    T = Path(t)
    for n in ("convertir_desamb.py", "hoja_clases.csv", "censo_c1.csv"):
        shutil.copy2(L / n, T / n)
    p = subprocess.run([sys.executable, "-I", "-B", str(T / "convertir_desamb.py"), "hoja_clases.csv", "censo_c1.csv"],
                       capture_output=True, text=True, cwd=str(T))
    iguales = p.returncode == 0 and all((T / n).exists() and shaf(T / n) == SHA[n] for n in ("hoja_clases_marcada.csv", "censo_c1_marcado.csv"))
    ok("5a la conversión, re-corrida sobre una copia de la conversión y las dos exportaciones, da las dos marcadas byte a byte", iguales,
       p.stdout.splitlines()[-3:])
    ok("5b sin arreglos de forma", "arreglos de forma" not in p.stdout)
    res["consola_de_la_conversion_sin_cuentas_por_clase"] = [l for l in p.stdout.splitlines() if "con nota" not in l]
res["mal"] = mal
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for k, v in res.items():
    if isinstance(v, dict) and "pasa" in v:
        print(("OK " if v["pasa"] else "MAL"), k, "" if v["pasa"] else v.get("detalle"))
print(f"controles: {sum(1 for v in res.values() if isinstance(v, dict) and 'pasa' in v)}, mal: {len(mal)} {mal}")
sys.exit(1 if mal else 0)
