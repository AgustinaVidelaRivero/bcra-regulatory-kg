"""Mesa, §140 (17/10/2026), U-MED-DESAMB: el anexo de las entradas de la planilla, para leer cómoda. Agregado DESPUÉS del sello del
diseño: es solo presentación y no cambia los ítems, la lista sellada ni la clave. Por cada entrada distinta de la planilla: etiqueta,
alias, definición y padre del catálogo; si es un rol, sus miembros (campo `rol` del catálogo); y de qué documentos es el alcance
(rol_por_to_r2.json). Sin vía ni estrato. USD 0.
Uso: python3 -I -B anexo_entradas_planilla_mesa.py --planilla <planilla_lectura.json> --catalogo <catalogo_sujetos_r2.json>
        --rol-por-to <rol_por_to_r2.json> --salida <anexo_entradas.md>"""
import argparse
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    for k in ("--planilla", "--catalogo", "--rol-por-to", "--salida"):
        ap.add_argument(k, required=True)
    a = ap.parse_args()
    pl = json.loads(Path(a.planilla).read_text(encoding="utf-8"))
    cat = {s["id"]: s for s in json.loads(Path(a.catalogo).read_text(encoding="utf-8"))["sujetos"]}
    rp = json.loads(Path(a.rol_por_to).read_text(encoding="utf-8"))
    docs = {}
    for archivo, v in (rp.items() if isinstance(rp, dict) else []):
        if isinstance(v, dict) and v.get("rol_id"):
            docs.setdefault(v["rol_id"], []).append(archivo)
    ids = sorted({e["id"] for h in pl["items"] for e in h["entradas"]})
    out = ["# Anexo: las entradas de la planilla", "",
           f"Las {len(ids)} entradas distintas que aparecen en la planilla (sello de la lista `{pl['sello_de_la_lista']}`), en orden "
           "alfabético. Solo datos del catálogo; no dice en qué ítem ni por qué aparece cada una.", ""]
    for i in ids:
        s = cat.get(i, {})
        out.append(f"## `{i}`")
        out.append("")
        out.append(f"- **Etiqueta:** {s.get('label')}")
        out.append(f"- **Alias:** {', '.join(s.get('alias') or []) or 'sin alias'}")
        out.append(f"- **Definición:** {s.get('definicion') or 'sin definición'}")
        out.append(f"- **Padre:** {s.get('padre') or 'sin padre'}")
        rol = s.get("rol") or {}
        if rol.get("miembros"):
            nombres = [cat.get(m, {}).get("label") or m for m in rol["miembros"]]
            out.append(f"- **Es un rol; sus miembros:** {', '.join(nombres)}")
        if docs.get(i):
            out.append(f"- **Es el alcance de:** {', '.join(sorted(docs[i]))}")
        out.append("")
    Path(a.salida).write_text("\n".join(out), encoding="utf-8")
    print(f"anexo: {len(ids)} entradas, {sum(1 for i in ids if (cat.get(i, {}).get('rol') or {}).get('miembros'))} roles con miembros")


if __name__ == "__main__":
    main()
