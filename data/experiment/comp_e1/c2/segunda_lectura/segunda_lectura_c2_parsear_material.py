"""Parsea el material cegado de C2 (solo material/) a una estructura JSON.

Uso: python3 parsear_material.py <dir_material> <salida.json>
No lee ningún otro archivo de C2.
"""
import json
import re
import sys
from pathlib import Path

RE_UNIT = re.compile(r"^# `([^`]+)` — (.*)$")
RE_ENT = re.compile(r"^- \*\*(\S+) (\S+)\*\* «(.*?)» — (.*)$")
RE_SUP = re.compile(r"^(\d+)\. «(.*)»( \(miembros? .*\))?$")
RE_OMI = re.compile(r"^((?:con|sin)_marca:\d+) \[([^\]]*)\] «(.*)»$")
RE_CAND_SUP = re.compile(r"^- (\d+)\. «(.*)»( \(miembros? .*\))? → candidatos: (.*)$")
RE_CAND_OMI = re.compile(r"^- ((?:con|sin)_marca:\d+) → entidades: (.*?) \| omisiones: (.*)$")
RE_OMIS = re.compile(r"^- Omisión `([^`]+)` \[(\w+)\]: «(.*?)»(?: — (.*))?$")
RE_TRAMO = re.compile(r" · tramo \[(\w+)\]: «(.*)»$")


def parse_ent(m, raw):
    eid, tipo, label, rest = m.groups()
    ent = {"id": eid, "tipo": tipo, "label": label, "raw": raw}
    mt = RE_TRAMO.search(rest)
    if mt:
        ent["tramo_nivel"], ent["tramo"] = mt.group(1), mt.group(2)
        rest = rest[: mt.start()]
    else:
        ent["tramo_nivel"], ent["tramo"] = None, None
    partes = rest.split(" · ")
    ent["desc"] = partes[0]
    for p in partes[1:]:
        if p.startswith("props: "):
            ent["props"] = p[len("props: "):]
        elif p.startswith("umbral: "):
            ent["umbral"] = p[len("umbral: "):]
        else:
            ent.setdefault("otros", []).append(p)
    return ent


def parse_file(path):
    lines = path.read_text(encoding="utf-8").split("\n")
    u = {"archivo": path.name, "texto": [], "supuestos": [], "omisiones_t4": [], "codigos": {}}
    sec = None
    cod = None
    for ln in lines:
        m = RE_UNIT.match(ln)
        if m:
            u["unidad"], u["titulo"] = m.groups()
            continue
        if ln.startswith("Grupos: "):
            u["cabecera"] = ln
            continue
        if ln == "## Texto":
            sec = "texto"; continue
        if ln.startswith("## Supuestos de la fase A"):
            sec = "sup"; continue
        if ln.startswith("## Omisiones leídas en T4"):
            sec = "omi"; continue
        m = re.match(r"^## Código ([A-Z])$", ln)
        if m:
            cod = m.group(1)
            u["codigos"][cod] = {"entidades": [], "relaciones": [], "omisiones": [], "otros": [],
                                 "cand_sup": {}, "cand_omi": {}}
            sec = "cod"; continue
        m = re.match(r"^### ([A-Z]) — (supuestos|omisiones)", ln)
        if m:
            assert m.group(1) == cod, (path, ln)
            sec = "cand"; continue
        if not ln.strip():
            continue
        if sec == "texto":
            m = re.match(r"^> \*(heredado|propio):\* (.*)$", ln)
            assert m, (path, ln)
            u["texto"].append([m.group(1), m.group(2)])
        elif sec == "sup":
            m = RE_SUP.match(ln)
            assert m, (path, ln)
            u["supuestos"].append({"n": int(m.group(1)), "frase": m.group(2), "miembro": (m.group(3) or "").strip()})
        elif sec == "omi":
            m = RE_OMI.match(ln)
            assert m, (path, ln)
            u["omisiones_t4"].append({"clave": m.group(1), "attrs": m.group(2), "frase": m.group(3)})
        elif sec == "cod":
            c = u["codigos"][cod]
            m = RE_ENT.match(ln)
            if m:
                c["entidades"].append(parse_ent(m, ln)); continue
            if ln.startswith("- R: "):
                c["relaciones"].append(ln[len("- R: "):]); continue
            m = RE_OMIS.match(ln)
            if m:
                c["omisiones"].append({"cat": m.group(1), "nivel": m.group(2), "tramo": m.group(3),
                                       "nota": m.group(4)}); continue
            c["otros"].append(ln)
        elif sec == "cand":
            c = u["codigos"][cod]
            m = RE_CAND_SUP.match(ln)
            if m:
                c["cand_sup"][int(m.group(1))] = {"frase": m.group(2), "miembro": (m.group(3) or "").strip(), "cand": m.group(4)}; continue
            m = RE_CAND_OMI.match(ln)
            if m:
                c["cand_omi"][m.group(1)] = {"ent": m.group(2), "omi": m.group(3)}; continue
            raise AssertionError((path, ln))
        else:
            if ln.startswith("|") or ln.startswith("# Material"):
                continue
            raise AssertionError((path, ln))
    return u


def main():
    d = Path(sys.argv[1])
    out = {}
    for p in sorted(d.glob("*.md")):
        if p.name == "indice.md":
            continue
        u = parse_file(p)
        out[u["unidad"]] = u
    Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    n_sup = sum(len(c["cand_sup"]) for u in out.values() for c in u["codigos"].values())
    n_omi = sum(len(c["cand_omi"]) for u in out.values() for c in u["codigos"].values())
    print("unidades", len(out), "M1 lineas", n_sup, "M2 lineas", n_omi,
          "supuestos base", sum(len(u["supuestos"]) for u in out.values()),
          "omisiones base", sum(len(u["omisiones_t4"]) for u in out.values()))
    for u in out.values():
        for k, c in u["codigos"].items():
            assert len(c["cand_sup"]) == len(u["supuestos"]), (u["unidad"], k)
            assert len(c["cand_omi"]) == len(u["omisiones_t4"]), (u["unidad"], k)
            if c["otros"]:
                print("OTROS", u["unidad"], k, c["otros"])


if __name__ == "__main__":
    main()
