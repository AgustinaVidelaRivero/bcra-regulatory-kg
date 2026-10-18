"""Mesa, §140 (17/10/2026), U-MED-DESAMB: la lista del censo de C1 para la lectura de la autora, desde la salida de la parte 2 (colisiones
por el código normalizado sellado) y el kg. Por cada colisión: los nodos que C1 uniría, con su código, etiqueta, tipo, documentos y los
tramos donde se los cita. Para cada una, la autora carga «une_bien» o «une_mal» en la hoja. USD 0.
Uso: python3 -I -B censo_c1_mesa.py --tamanos <tamanos_desamb.json> --kg <kg.json> --salida <dir>"""
import argparse
import csv
import io
import json
from pathlib import Path

ap = argparse.ArgumentParser()
for k in ("--tamanos", "--kg", "--salida"):
    ap.add_argument(k, required=True)
a = ap.parse_args()
t = json.loads(Path(a.tamanos).read_text(encoding="utf-8"))
nodos = {n["id"]: n for n in json.loads(Path(a.kg).read_text(encoding="utf-8"))["nodes"]}
cols = t["C_comunicacion_entre_documentos"]["colisiones_para_leer"]
md = ["# Censo de C1: las Comunicacion que la regla uniría entre documentos", "",
      f"{len(cols)} colisiones, por el código normalizado sellado (`codigo_normalizado`, diseño sellado, §6). Cada una se lee entera: "
      "¿todos sus nodos son la misma norma? En `censo_c1.csv`, la columna `decision` lleva `une_bien` o `une_mal`. Una sola `une_mal` frena "
      "la regla o la corrige con una excepción declarada.", ""]
buf = io.StringIO(); w = csv.writer(buf, lineterminator="\n"); w.writerow(["colision", "codigo_normalizado", "nodos", "decision", "nota"])
for k, c in enumerate(cols, 1):
    cid = f"C{k:02d}"
    md += [f"## {cid}: «{c['codigo_normalizado']}»", "", f"- **Documentos:** {', '.join(c['tos'])} · **Nodos:** {c['nodos']} · "
           f"**Códigos crudos distintos:** {'sí' if c['codigos_crudos_distintos'] else 'no'}", ""]
    for f in c["filas"]:
        n = nodos.get(f["id"], {})
        md.append(f"- `{f['id']}` ({', '.join(f['tos'])}): {f['label']}; código «{f['codigo']}»; tipo {f['tipo']}")
        for p in (n.get("provenances") or [])[:6]:
            md.append(f"  - {p.get('to')}::{p.get('punto')}: «{p.get('tramo') or 'sin tramo'}»")
    md.append("")
    w.writerow([cid, c["codigo_normalizado"], c["nodos"], "", ""])
S = Path(a.salida); S.mkdir(parents=True, exist_ok=True)
(S / "censo_c1.md").write_text("\n".join(md), encoding="utf-8")
(S / "censo_c1.csv").write_text(buf.getvalue(), encoding="utf-8")
print(f"censo de C1: {len(cols)} colisiones, {sum(c['nodos'] for c in cols)} nodos")
