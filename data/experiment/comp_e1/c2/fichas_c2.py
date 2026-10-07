"""
fichas_c2.py — U-COMP-E1, C2: a partir de la lectura cegada (lectura_c2.jsonl: una línea por clasificación, con su
ancla en la salida y en el texto) arma las fichas por unidad y código (fichas_c2.json y fichas_c2_<codigo>.md), el
resumen por código SIN interpretar contra el criterio (resumen_por_codigo.json; eso es C3) y los sellos
(sellos_c2.json). Controla antes la cobertura: 137 supuestos × 4 códigos + 11 del quinto código (559) y 60 omisiones ×
4 + 5 del quinto código (245); una clasificación por (unidad, ítem, código); clases y subtipos admitidos; categoría
presente cuando la clase es «omision_otra_vez». USD 0, sin API.

La tabla código → brazo/corrida (codigos_c2_cerrado.json) se lee solo para traer la salida que corresponde a cada
código; nunca se imprime ni se escribe en las fichas ni en el resumen (sigue cerrada hasta la adjudicación).
  PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B data/experiment/comp_e1/c2/fichas_c2.py --lectura L --codigos DIR --salida DIR
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_c2 as C  # noqa: E402

CODIGO_SEP = "::"


def ahora() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def cargar_lectura(p: Path) -> list[dict]:
    out = []
    for i, x in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if x.strip():
            r = json.loads(x)
            r["_linea"] = i
            out.append(r)
    return out


def controlar(lect: list[dict], codigos: list[str], cod_h0: str, unids: list[dict], sup: dict, oms: list[dict]) -> dict:
    """Cobertura y validez de la lectura. Devuelve las cuentas; levanta AssertionError con la primera falla."""
    con_reintento = {u["chunk_id"] for u in unids if u["n_reintentos"]}
    cuatro = [c for c in codigos if c != cod_h0]
    assert len(cuatro) == 4 and cod_h0 in codigos, "cinco códigos: cuatro corridas y el quinto"
    m1 = [r for r in lect if r["medida"] == "M1"]
    m2 = [r for r in lect if r["medida"] == "M2"]
    for r in m1:
        assert r["clase"] in C.CLASES_M1, f"clase M1 no admitida (línea {r['_linea']}): {r['clase']}"
        if r["clase"] == "sin_relacion":
            assert r.get("subtipo") in C.SUBTIPOS_SR, f"sin_relacion sin subtipo admitido (línea {r['_linea']})"
        else:
            assert not r.get("subtipo"), f"subtipo en una clase que no es sin_relacion (línea {r['_linea']})"
        assert r.get("donde"), f"M1 sin ancla (línea {r['_linea']})"
        assert r["codigo"] in codigos, f"código desconocido (línea {r['_linea']})"
    for r in m2:
        assert r["clase"] in C.CLASES_M2, f"clase M2 no admitida (línea {r['_linea']}): {r['clase']}"
        if r["clase"] == "omision_otra_vez":
            assert r.get("categoria"), f"omision_otra_vez sin categoría (línea {r['_linea']})"
        assert r.get("donde"), f"M2 sin ancla (línea {r['_linea']})"
        assert r["codigo"] in codigos, f"código desconocido (línea {r['_linea']})"
    # M1: por (unidad, i, código) exactamente una; cada unidad del grupo c con sus n supuestos en los 4 códigos y, si tiene
    # reintento, también en el quinto.
    c1 = collections.Counter((r["chunk_id"], r["i"], r["codigo"]) for r in m1)
    dup = [k for k, v in c1.items() if v > 1]
    assert not dup, f"M1 duplicadas: {dup[:5]}"
    for cid, ss in sup.items():
        for cod in cuatro + ([cod_h0] if cid in con_reintento else []):
            faltan = [i + 1 for i in range(len(ss)) if (cid, i + 1, cod) not in c1]
            assert not faltan, f"M1 faltan {cid} código {cod} supuestos {faltan}"
    esperado_m1 = sum(len(ss) * (4 + (1 if cid in con_reintento else 0)) for cid, ss in sup.items())
    assert len(m1) == esperado_m1, f"M1: {len(m1)} registros, esperados {esperado_m1}"
    extra = [k for k in c1 if k[0] not in sup or k[1] > len(sup[k[0]]) or (k[2] == cod_h0 and k[0] not in con_reintento)]
    assert not extra, f"M1 fuera de las bases: {extra[:5]}"
    # M2: por (unidad, ficha, código) exactamente una.
    c2 = collections.Counter((r["chunk_id"], r["ficha"], r["codigo"]) for r in m2)
    dup = [k for k, v in c2.items() if v > 1]
    assert not dup, f"M2 duplicadas: {dup[:5]}"
    fichas = {(o["chunk_id"], f"{o['grupo']}:{o['n']}") for o in oms}
    for cid, fi in fichas:
        for cod in cuatro + ([cod_h0] if cid in con_reintento else []):
            assert (cid, fi, cod) in c2, f"M2 falta {cid} {fi} código {cod}"
    esperado_m2 = sum(4 + (1 if cid in con_reintento else 0) for cid, _ in fichas)
    assert len(m2) == esperado_m2, f"M2: {len(m2)} registros, esperados {esperado_m2}"
    extra = [k for k in c2 if (k[0], k[1]) not in fichas or (k[2] == cod_h0 and k[0] not in con_reintento)]
    assert not extra, f"M2 fuera de las bases: {extra[:5]}"
    return {"m1": len(m1), "m2": len(m2), "esperado_m1": esperado_m1, "esperado_m2": esperado_m2,
            "unidades_con_reintento": sorted(con_reintento)}


def resumen(lect: list[dict], codigos: list[str], cod_h0: str, oms: list[dict]) -> dict:
    """Conteos por código y clase, sin interpretar contra el criterio (C3)."""
    norm_adj = {(o["chunk_id"], f"{o['grupo']}:{o['n']}"): o["normativo_adjudicado"] for o in oms}
    remis = {(o["chunk_id"], f"{o['grupo']}:{o['n']}"): o["remision_pura"] for o in oms}
    out: dict = {"nota": "conteos por código; la tabla código → brazo/corrida sigue cerrada; el criterio C1/C2 del mandato se aplica en C3",
                 "codigos": {}}
    for cod in codigos:
        m1 = [r for r in lect if r["medida"] == "M1" and r["codigo"] == cod]
        m2 = [r for r in lect if r["medida"] == "M2" and r["codigo"] == cod]
        cl1 = collections.Counter(r["clase"] for r in m1)
        sub = collections.Counter(r["subtipo"] for r in m1 if r["clase"] == "sin_relacion")
        por_u = collections.defaultdict(collections.Counter)
        for r in m1:
            por_u[r["chunk_id"]][r["clase"]] += 1
        m2n = [r for r in m2 if norm_adj[(r["chunk_id"], r["ficha"])]]
        m2nn = [r for r in m2 if not norm_adj[(r["chunk_id"], r["ficha"])]]
        m2r = [r for r in m2 if remis[(r["chunk_id"], r["ficha"])]]
        cats = collections.Counter(r["categoria"] for r in m2 if r["clase"] == "omision_otra_vez")
        out["codigos"][cod] = {
            "es_quinto_codigo": cod == cod_h0,
            "m1": {"n": len(m1), "clases": {k: cl1.get(k, 0) for k in C.CLASES_M1}, "subtipos_sin_relacion": dict(sub),
                   "por_unidad": {u: dict(v) for u, v in sorted(por_u.items())}},
            "m2": {"n": len(m2),
                   "normativas_adjudicadas": {"n": len(m2n), "clases": {k: sum(r["clase"] == k for r in m2n) for k in C.CLASES_M2}},
                   "no_normativas": {"n": len(m2nn), "clases": {k: sum(r["clase"] == k for r in m2nn) for k in C.CLASES_M2}},
                   "remisiones_puras_(dentro_de_las_normativas)": {"n": len(m2r), "clases": {k: sum(r["clase"] == k for r in m2r) for k in C.CLASES_M2}},
                   "categorias_de_omision_otra_vez": dict(cats)},
        }
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lectura", type=Path, required=True, help="lectura_c2.jsonl (primera lectura, cegada)")
    ap.add_argument("--codigos", type=Path, required=True, help="directorio con codigos_c2_cerrado.json y sello_codigos_c2.json")
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    a.salida.mkdir(parents=True, exist_ok=True)

    cerrado = a.codigos / "codigos_c2_cerrado.json"
    sello_cod = json.loads((a.codigos / "sello_codigos_c2.json").read_text(encoding="utf-8"))
    assert sha(cerrado) == sello_cod["sha256_archivo_cerrado"], "el archivo cerrado de códigos no coincide con su sello"
    mapa = json.loads(cerrado.read_text(encoding="utf-8"))["codigo_a_etiqueta"]     # solo en memoria
    inv = {et: cod for cod, et in mapa.items()}
    codigos = sorted(mapa)
    cod_h0 = inv[C.ETIQUETA_HAIKU]

    unids = C.unidades()
    ch = C.chunks(unids)
    res = C.resultados_c1()
    h0 = C.intento0_haiku()
    sup = C.supuestos_t4()
    oms = C.omisiones_t4()
    lect = cargar_lectura(a.lectura)
    cuentas = controlar(lect, codigos, cod_h0, unids, sup, oms)

    oms_por_u: dict[str, list[dict]] = {}
    for o in oms:
        oms_por_u.setdefault(o["chunk_id"], []).append(o)
    l1 = {(r["chunk_id"], r["i"], r["codigo"]): r for r in lect if r["medida"] == "M1"}
    l2 = {(r["chunk_id"], r["ficha"], r["codigo"]): r for r in lect if r["medida"] == "M2"}

    fichas: list[dict] = []
    md_por_cod: dict[str, list[str]] = {cod: [f"# Fichas de C2 — código {cod}", "",
                                              "Lectura cegada (primera lectura de la instancia). El código no dice el brazo ni la corrida; "
                                              "la tabla sigue cerrada hasta la adjudicación. Clases de M1 y M2: `c0/reglas_lectura_c0.md`.", ""]
                                        for cod in codigos}
    for u in unids:
        cid = u["chunk_id"]
        c = ch[cid]
        t = C.texto(c)
        s_u = sup.get(cid, [])
        o_u = oms_por_u.get(cid, [])
        if not s_u and not o_u:
            continue
        cods_u = {inv[et]: res[et][cid] for et in C.ETIQUETAS}
        if u["n_reintentos"]:
            cods_u[cod_h0] = h0[cid]
        for cod in sorted(cods_u):
            val = C.validacion_r2_de(cods_u[cod], c)
            ext = C.render_extraccion(val)
            f = {"chunk_id": cid, "codigo": cod, "to": u["to"], "grupos": u["grupos"], "titulo": C.norm(t["titulo"] or ""),
                 "texto_propio": C.norm(t["propio"]), "texto_heredado": [C.norm(h) for h in t["heredado"]],
                 "extraccion": ext,
                 "m1": [{"i": i + 1, "fragmento": s["fragmento_fase_a"], "miembro": s.get("miembro"),
                         "clase": l1[(cid, i + 1, cod)]["clase"], "subtipo": l1[(cid, i + 1, cod)].get("subtipo") or None,
                         "donde": l1[(cid, i + 1, cod)]["donde"]} for i, s in enumerate(s_u)],
                 "m2": [{"ficha": f"{o['grupo']}:{o['n']}", "normativa_adjudicada": o["normativo_adjudicado"], "remision_pura": o["remision_pura"],
                         "en": o["en"], "tramo_t4": C.norm(o["tramo"]),
                         "clase": l2[(cid, f"{o['grupo']}:{o['n']}", cod)]["clase"],
                         "categoria": l2[(cid, f"{o['grupo']}:{o['n']}", cod)].get("categoria"),
                         "donde": l2[(cid, f"{o['grupo']}:{o['n']}", cod)]["donde"]} for o in o_u]}
            fichas.append(f)
            md = md_por_cod[cod]
            md += [f"## `{cid}` — {f['titulo']}", "", f"Grupos: {', '.join(u['grupos'])}.", "", "### Texto", ""]
            md += [f"> *heredado:* {h}" for h in f["texto_heredado"]] + [f"> *propio:* {f['texto_propio']}", ""]
            md += ["### Extracción (código " + cod + ")", ""] + (ext or ["(sin entidades ni omisiones)"]) + [""]
            if f["m1"]:
                md += ["### M1 — supuestos de la fase A de T4", "", "| n | supuesto | clase | subtipo | ancla |", "|---|---|---|---|---|"]
                md += [f"| {x['i']} | «{x['fragmento']}»{' (' + x['miembro'] + ')' if x['miembro'] else ''} | `{x['clase']}` | {x['subtipo'] or ''} | {x['donde']} |"
                       for x in f["m1"]] + [""]
            if f["m2"]:
                md += ["### M2 — omisiones leídas en T4", "", "| ficha | normativa | tramo de T4 | clase | categoría | ancla |", "|---|---|---|---|---|---|"]
                md += [f"| {x['ficha']} | {'sí' if x['normativa_adjudicada'] else 'no'}{' (remisión pura)' if x['remision_pura'] else ''} | «{C.corto(x['tramo_t4'], 160)}» "
                       f"| `{x['clase']}` | {x['categoria'] or ''} | {x['donde']} |" for x in f["m2"]] + [""]

    (a.salida / "fichas_c2.json").write_text(json.dumps({"unidad": "U-COMP-E1, C2", "generado_utc": ahora(), "cuentas": cuentas,
                                                          "clases_m1": list(C.CLASES_M1), "subtipos_sin_relacion": list(C.SUBTIPOS_SR),
                                                          "clases_m2": list(C.CLASES_M2), "fichas": fichas},
                                                         ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for cod, md in md_por_cod.items():
        (a.salida / f"fichas_c2_{cod}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    r = resumen(lect, codigos, cod_h0, oms)
    r["cuentas"] = cuentas
    (a.salida / "resumen_por_codigo.json").write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sellos = {"unidad": "U-COMP-E1, C2", "hora_sello_utc": ahora(),
              "lectura_c2.jsonl": {"sha256": sha(a.lectura), "registros": len(lect)},
              "fichas_c2.json": {"sha256": sha(a.salida / "fichas_c2.json"), "fichas": len(fichas)},
              "resumen_por_codigo.json": {"sha256": sha(a.salida / "resumen_por_codigo.json")},
              "codigos_c2_cerrado.json": {"sha256": sha(cerrado), "sello_previo": sello_cod},
              "fichas_md": {f"fichas_c2_{cod}.md": sha(a.salida / f"fichas_c2_{cod}.md") for cod in codigos}}
    (a.salida / "sellos_c2.json").write_text(json.dumps(sellos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"cuentas": cuentas, "fichas": len(fichas), "codigos": codigos,
                      "sha256_fichas": sellos["fichas_c2.json"]["sha256"], "sha256_lectura": sellos["lectura_c2.jsonl"]["sha256"]},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
