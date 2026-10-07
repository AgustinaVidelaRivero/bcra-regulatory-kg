"""
preparar_c2.py — U-COMP-E1, C2: (1) sortea los cinco códigos de la lectura cegada con una semilla sellada y escribe la
tabla código → brazo/corrida en un archivo CERRADO (codigos_c2_cerrado.json), con su sha256 y su hora en
sello_codigos_c2.json, ANTES de leer; (2) genera el material de lectura por unidad (material/<chunk_id>.md): el texto de
la unidad (propio y heredado) y, por código, la extracción renderizada con sus tramos verificados, los supuestos de T4
a clasificar (unidades del grupo c) con candidatos automáticos, y las omisiones de T4 a clasificar (unidades de
omisiones) con candidatos automáticos. El material no muestra el brazo ni la corrida; el quinto código (intento 0 de
Haiku) aparece solo en las 8 unidades con reintento y por eso se descubre por construcción (se declara). USD 0.
  PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B data/experiment/comp_e1/c2/preparar_c2.py --salida DIR --semilla "U-COMP-E1:codigos:C2:2026-10-07"
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_c2 as C  # noqa: E402

LETRAS = "ABCDEFGHJKLMNPQRSTUVWXYZ"   # sin I ni O


def ahora() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sortear_codigos(semilla: str) -> dict[str, str]:
    rng = random.Random(semilla)
    letras = rng.sample(LETRAS, 5)
    etiquetas = list(C.ETIQUETAS) + [C.ETIQUETA_HAIKU]
    rng.shuffle(etiquetas)
    return {letra: et for letra, et in zip(letras, etiquetas)}   # código → etiqueta


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--semilla", type=str, required=True)
    a = ap.parse_args()
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "material").mkdir(exist_ok=True)

    # 1. Códigos, cerrados y sellados antes de leer.
    cerrado = a.salida / "codigos_c2_cerrado.json"
    if cerrado.exists():
        mapa = json.loads(cerrado.read_text(encoding="utf-8"))["codigo_a_etiqueta"]
    else:
        mapa = sortear_codigos(a.semilla)
        cerrado.write_text(json.dumps({"unidad": "U-COMP-E1, C2", "semilla": a.semilla, "sorteado_utc": ahora(),
                                       "procedimiento": "random.Random(semilla): sample de 5 letras de " + LETRAS + " y shuffle de "
                                                        "[S1, S2, O1, O2, H0]; código i → etiqueta i",
                                       "codigo_a_etiqueta": mapa}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sello = {"unidad": "U-COMP-E1, C2", "semilla": a.semilla, "archivo_cerrado": cerrado.name,
             "sha256_archivo_cerrado": hashlib.sha256(cerrado.read_bytes()).hexdigest(), "hora_sello_utc": ahora(),
             "codigos": sorted(mapa), "nota": "la tabla código → brazo/corrida no se abre hasta la adjudicación; el quinto código "
                                              "(intento 0 de Haiku) aparece solo en las 8 unidades con reintento y se descubre por construcción"}
    (a.salida / "sello_codigos_c2.json").write_text(json.dumps(sello, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in sello.items() if k != "nota"}, ensure_ascii=False))
    inv = {et: cod for cod, et in mapa.items()}     # etiqueta → código (solo en memoria)

    # 2. Material de lectura.
    unids = C.unidades()
    ch = C.chunks(unids)
    res = C.resultados_c1()
    h0 = C.intento0_haiku()
    sup = C.supuestos_t4()
    oms = C.omisiones_t4()
    oms_por_u: dict[str, list[dict]] = {}
    for o in oms:
        oms_por_u.setdefault(o["chunk_id"], []).append(o)
    indice = ["# Material de lectura de C2 — índice", "", "| unidad | grupos | supuestos | omisiones T4 | códigos |", "|---|---|---|---|---|"]
    n_items = {"supuestos": 0, "omisiones": 0}
    for u in unids:
        cid = u["chunk_id"]
        c = ch[cid]
        codigos = {inv[et]: (res[et][cid], "c1") for et in C.ETIQUETAS}
        if u["n_reintentos"]:
            codigos[inv[C.ETIQUETA_HAIKU]] = (h0[cid], "h0")
        t = C.texto(c)
        md = [f"# `{cid}` — {C.norm(t['titulo'] or '')}", "", f"Grupos: {', '.join(u['grupos'])}. "
              f"{'Intento 0 de Haiku con marca: ' + u['marcas_intento0'][0] + '. ' if u['marcas_intento0'] else ''}"
              f"Estado final en la tanda 0: `{u['estado_final']}`.", "", "## Texto", ""]
        md += [f"> *heredado:* {C.norm(h)}" for h in t["heredado"]] + [f"> *propio:* {C.norm(t['propio'])}", ""]
        s_u = sup.get(cid, [])
        o_u = oms_por_u.get(cid, [])
        if s_u:
            md += ["## Supuestos de la fase A de T4 (M1)", ""] + [f"{i + 1}. «{s['fragmento_fase_a']}»" + (f" (miembros {s['miembro']})" if s.get("miembro") else "")
                                                                 for i, s in enumerate(s_u)] + [""]
        if o_u:
            md += ["## Omisiones leídas en T4 (M2)", ""] + [f"{o['grupo']}:{o['n']} [{'normativa' if o['normativo_adjudicado'] else 'no normativa'}"
                                                           f"{', remisión pura' if o['remision_pura'] else ''}; {o['en']}] «{C.norm(o['tramo'])}»" for o in o_u] + [""]
        for cod in sorted(codigos):
            reg, fuente = codigos[cod]
            val = C.validacion_r2_de(reg, c)
            md += [f"## Código {cod}", ""] + C.render_extraccion(val) + [""]
            if s_u:
                md += [f"### {cod} — supuestos a clasificar", ""]
                for i, s in enumerate(s_u):
                    md.append(f"- {i + 1}. «{s['fragmento_fase_a']}» → candidatos: {', '.join(C.candidatos_supuesto(s['fragmento_fase_a'], val)) or '—'}")
                md.append("")
            if o_u:
                md += [f"### {cod} — omisiones de T4 a clasificar", ""]
                for o in o_u:
                    cand = C.candidatos_omision(o["tramo"], val)
                    e_txt = "; ".join(f"{x['local_id']} {x['type']} [{x['tramo_verificado']}] solap {x['solapamiento']}"
                                      f"{' contiene' if x['contiene'] else ''}{' contenido_en' if x['contenido_en'] else ''}" for x in cand["entidades"]) or "—"
                    o_txt = "; ".join(f"om#{x['indice']} {x['categoria']} [{x['tramo_verificado']}] solap {x['solapamiento']}"
                                      f"{' contiene' if x['contiene'] else ''}" for x in cand["omisiones"]) or "—"
                    md.append(f"- {o['grupo']}:{o['n']} → entidades: {e_txt} | omisiones: {o_txt}")
                md.append("")
        (a.salida / "material" / f"{cid.replace('::', '__')}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
        n_items["supuestos"] += len(s_u) * len(codigos)
        n_items["omisiones"] += len(o_u) * len(codigos)
        indice.append(f"| `{cid}` | {', '.join(u['grupos'])} | {len(s_u)} | {len(o_u)} | {len(codigos)} |")
    (a.salida / "material" / "indice.md").write_text("\n".join(indice) + "\n", encoding="utf-8")
    print(json.dumps({"unidades": len(unids), "clasificaciones_a_hacer": n_items, "material": str(a.salida / "material")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
