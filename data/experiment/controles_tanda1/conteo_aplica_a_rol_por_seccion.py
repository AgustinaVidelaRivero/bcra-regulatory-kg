"""Conteo de las aristas aplica_a hacia el rol de alcance de un documento, por sección (pre-registro de la tanda 1, fijado el
15/10/2026, antes de la corrida). Es una cuenta de aristas sobre un grafo ensamblado, no una lectura: no imprime texto.

Para cada documento y su rol:
- las normas (Obligacion, Restriccion, Potestad) del documento, por sección de primer nivel;
- de ellas, cuántas tienen al menos una arista aplica_a hacia el rol, cuántas solo hacia otro Sujeto y cuántas ninguna;
- las aristas aplica_a hacia el rol por sección, separadas por metodo_resolucion (incluye las derivadas, si el grafo las tiene).
La sección sale del chunk_id de la procedencia (el de la norma o el de la arista): el primer número del punto, o el de una sección S<n>;
lo que no tiene número va en «bloques».
Uso: python3 -I -B conteo_aplica_a_rol_por_seccion.py --kg <kg.json> --par <to>:<rol> [--par <to>:<rol> …] --out <salida.json>
"""
import argparse, json, re, sys
from collections import Counter, OrderedDict
from pathlib import Path

NORMAS = ("Obligacion", "Restriccion", "Potestad")


def seccion(chunk_id: str) -> str:
    u = (chunk_id or "").split("::", 1)[1] if "::" in (chunk_id or "") else (chunk_id or "")
    m = re.match(r"^S?(\d+)", u)
    return m.group(1) if m else "bloques"


def orden(c: dict) -> OrderedDict:
    return OrderedDict(sorted(c.items(), key=lambda kv: (not kv[0].isdigit(), int(kv[0]) if kv[0].isdigit() else 0, kv[0])))


def contar(kg: dict, to: str, rol: str) -> OrderedDict:
    nodos = {n["id"]: n for n in kg["nodes"]}
    normas = {i: n for i, n in nodos.items() if n.get("type") in NORMAS and (n.get("provenance") or {}).get("to") == to}
    salientes = {}
    for e in kg["edges"]:
        if e.get("relation") == "aplica_a" and e.get("source") in normas:
            salientes.setdefault(e["source"], []).append(e)
    por_sec, al_rol, solo_otro, ninguna = Counter(), Counter(), Counter(), Counter()
    aristas = {}
    for i, n in normas.items():
        s = seccion((n.get("provenance") or {}).get("chunk_id"))
        por_sec[s] += 1
        es = salientes.get(i, [])
        if any(e.get("target") == rol for e in es):
            al_rol[s] += 1
        elif es:
            solo_otro[s] += 1
        else:
            ninguna[s] += 1
        for e in es:
            if e.get("target") == rol:
                se = seccion((e.get("provenance") or {}).get("chunk_id") or (n.get("provenance") or {}).get("chunk_id"))
                aristas.setdefault(se, Counter())[e.get("metodo_resolucion") or "sin_metodo"] += 1
    return OrderedDict([
        ("to", to), ("rol", rol), ("normas", sum(por_sec.values())),
        ("normas_por_seccion", orden(por_sec)),
        ("normas_con_aplica_a_al_rol", orden(al_rol)),
        ("normas_con_aplica_a_solo_a_otro_sujeto", orden(solo_otro)),
        ("normas_sin_aplica_a", orden(ninguna)),
        ("aristas_al_rol_por_seccion_y_metodo", OrderedDict((k, OrderedDict(sorted(v.items()))) for k, v in orden(aristas).items())),
        ("totales", OrderedDict([("normas_con_aplica_a_al_rol", sum(al_rol.values())),
                                 ("aristas_al_rol", sum(sum(v.values()) for v in aristas.values()))])),
    ])


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--kg", required=True)
    ap.add_argument("--par", action="append", required=True, help="<to>:<rol>")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    kg = json.loads(Path(a.kg).read_text(encoding="utf-8"))
    pares = [p.split(":", 1) for p in a.par]
    out = OrderedDict([("kg", Path(a.kg).name), ("documentos", [contar(kg, to, rol) for to, rol in pares])])
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for d in out["documentos"]:
        print(d["to"], d["rol"], "normas", d["normas"], "con aplica_a al rol", d["totales"]["normas_con_aplica_a_al_rol"],
              "aristas al rol", d["totales"]["aristas_al_rol"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
