"""
apoyo_lectura_p4.py — U-PROMPT-R2, P4.c (USD 0, sin API): los extractos para la lectura asistida de las fichas y para
las mediciones a, b y c del «seguí» de P4. No marca nada: deja a la vista lo que se lee.

  - D1, umbral con tramo literal verificado: por ficha con cuantía en el texto propio, cada cuantía
    (reglas_comparacion.detectar_cuantias) y si queda dentro de un tramo de umbral verificado del brazo nuevo
    (tokens de R-NORM contiguos); las no cubiertas, con su contexto, para leer si son un umbral de una norma;
  - D4, la tabla de `cap::1.2`: el texto y las entidades de los dos brazos;
  - D5, `condicion_de` con la firma nueva (→ Operacion o → Potestad), por brazo;
  - D6, `limita`, por brazo: origen, destino y el texto;
  - a, la modalidad: las entidades del brazo nuevo con `modalidad` o `consecuencia` copiadas y su clase; y, para los
    falsos negativos, las fichas cuyo texto tiene una forma de MODALIDAD_FORMAS y cuyo brazo nuevo no copió nada;
  - b, las Condicion de un ítem sin `condicion_de` en el brazo nuevo, con el ítem y su encabezado;
  - c, la salida de a, b y h: caracteres copiados en `modalidad` y `consecuencia`, y los tokens de salida de los
    mini-chunks a mitad de oración en los dos brazos.

Escribe solo en --salida (apoyo_lectura_p4.md y apoyo_lectura_p4.json). Uso (desde la raíz de una COPIA del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p4/apoyo_lectura_p4.py \
      --analisis A --resultados R --e0-fuera DIR --salida DIR
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
sys.path.insert(0, str(REX / "e1_extractor"))
import validador_r2 as V  # noqa: E402
import reglas_comparacion as RCMP  # noqa: E402
import prompt_r2b as PR  # noqa: E402

TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
FUERA = ("ayccef", "expaef", "opefci", "adrei")


def chunks(d: Path, to: str) -> dict:
    return {c["id"]: c for c in json.loads((d / f"chunks_{to}.json").read_text(encoding="utf-8"))}


def jl(p: Path) -> dict:
    return {r["chunk_id"]: r for r in map(json.loads, p.read_text(encoding="utf-8").splitlines())}


def contiene(aguja: str, pajar: str) -> bool:
    a, p = V.norm_tokens(aguja), V.norm_tokens(pajar)
    return bool(a) and any(p[i:i + len(a)] == a for i in range(len(p) - len(a) + 1))


def corto(s, n=260):
    s = " ".join(str(s or "").split())
    return s if len(s) <= n else s[:n] + "…"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--analisis", type=Path, required=True)
    ap.add_argument("--resultados", type=Path, required=True)
    ap.add_argument("--e0-fuera", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    sal.mkdir(parents=True, exist_ok=True)
    an = json.loads(a.analisis.read_text(encoding="utf-8"))
    res = jl(a.resultados)
    r2 = {}
    for to in TOS:
        r2.update(chunks(REX / "e0_chunking" / "salida_tanda0_r2", to))
    for to in FUERA:
        r2.update(chunks(a.e0_fuera / "e0_r2", to))
    filas = an["filas"]
    out: dict = {"d1": {}, "d5": {}, "d6": {}, "a": {"copiadas": [], "candidatos_falso_negativo": []}, "b": [],
                 "c": {}}
    md = ["# Apoyo a la lectura de P4", ""]

    def ents(cid, brazo):
        return {e["local_id"]: e for e in (res[f"{cid}|{brazo}"].get("tool_input") or {}).get("entities") or []
                if isinstance(e, dict)}

    # ---- D1 ----
    md += ["## D1, umbral con tramo literal verificado: cuantías del texto propio no cubiertas por un tramo verificado", ""]
    for cid, f in sorted(filas.items()):
        texto = r2[cid].get("texto") or ""
        cs = RCMP.detectar_cuantias(texto)
        if not cs:
            continue
        tramos = [u["tramo"] for u in f["hechos"]["nuevo"].get("umbrales") or [] if u["verificacion"] != "no"]
        tramos_full = [t for e in ents(cid, "nuevo").values() for t in
                       [x.get("tramo") for x in e.get("umbrales") or [] if isinstance(x, dict)] if t]
        cub = [{"cuantia": c.texto, "clase": c.clase, "cubierta": any(contiene(c.texto, t) for t in tramos_full),
                "contexto": corto(texto[max(0, c.inicio - 120):c.fin + 80], 260)} for c in cs]
        out["d1"][cid] = {"cuantias": len(cub), "cubiertas": sum(x["cubierta"] for x in cub),
                          "tramos_verificados": len(tramos), "detalle": cub}
        falt = [x for x in cub if not x["cubierta"]]
        md += [f"### `{cid}` — {len(cub) - len(falt)} de {len(cub)} cubiertas; tramos verificados: {len(tramos)}"]
        md += [f"- NO cubierta «{x['cuantia']}» ({x['clase']}): …{x['contexto']}…" for x in falt]
        md += [""]
    # ---- D4 ----
    md += ["## D4, la tabla de `cap::1.2`", "", "```", (r2["cap::1.2"].get("texto") or "")[:4000], "```", ""]
    for b in ("sellado", "nuevo"):
        md += [f"**{b}:**"] + [f"- {e.get('type')} «{e.get('label')}»: {corto((e.get('properties') or {}).get('descripcion'), 400)}"
                               f" | umbrales: {e.get('umbrales') or (e.get('properties') or {}).get('umbral')}"
                               for e in ents("cap::1.2", b).values()] + [""]
    # ---- D5 y D6 ----
    for clave, pred, filtro in (("d5", "condicion_de", lambda e_t: e_t in ("Operacion", "Potestad")),
                                ("d6", "limita", lambda e_t: True)):
        md += [f"## {clave.upper()}, `{pred}`" + (" con firma nueva" if clave == "d5" else ""), ""]
        for cid, f in sorted(filas.items()):
            bloques = []
            for b in ("sellado", "nuevo"):
                es = ents(cid, b)
                for r in (res[f"{cid}|{b}"].get("tool_input") or {}).get("relations") or []:
                    if not isinstance(r, dict) or r.get("predicate") != pred:
                        continue
                    s, t = es.get(r.get("source"), {}), es.get(r.get("target"), {})
                    if not filtro(t.get("type")):
                        continue
                    bloques.append(f"- **{b}**: {s.get('type')} «{corto(s.get('label'), 80)}» ({corto((s.get('properties') or {}).get('descripcion'), 200)}) "
                                   f"--{pred}--> {t.get('type')} «{corto(t.get('label'), 80)}» ({corto((t.get('properties') or {}).get('descripcion'), 160)})")
                    out[clave].setdefault(cid, []).append({"brazo": b, "origen": s.get("label"), "destino_tipo": t.get("type"),
                                                           "destino": t.get("label")})
            if bloques:
                md += [f"### `{cid}`", f"Texto: {corto(r2[cid].get('texto'), 900)}", f"Último heredado: "
                       f"{corto((r2[cid].get('herencia') or [{}])[-1].get('texto'), 300)}"] + bloques + [""]
    # ---- a ----
    formas = V.MODALIDAD_FORMAS
    md += ["## a, la modalidad copiada y su clase (brazo nuevo)", ""]
    for cid, f in sorted(filas.items()):
        copiadas = []
        for e in ents(cid, "nuevo").values():
            otras = e.get("otras_propiedades") or {}
            for k in ("modalidad", "consecuencia"):
                if k in otras:
                    copiadas.append({"chunk_id": cid, "tipo": e.get("type"), "label": e.get("label"), "clave": k,
                                     "tramo": otras[k], "clase": V.clasificar_modalidad(k, otras[k]),
                                     "descripcion": (e.get("properties") or {}).get("descripcion")})
        out["a"]["copiadas"] += copiadas
        md += [f"- `{c['chunk_id']}` {c['tipo']} «{corto(c['label'], 70)}» {c['clave']}=«{c['tramo']}» → {c['clase']} "
               f"| {corto(c['descripcion'], 160)}" for c in copiadas]
        toks = V.norm_tokens(r2[cid].get("texto") or "")
        hallados = sorted({clase for clase, fs in formas.items() for t in toks if t.startswith(fs["prefijos"])} |
                          {clase for clase, fs in formas.items() for i in range(len(toks) - 1)
                           if tuple(toks[i:i + 2]) in fs["pares"]})
        if hallados and not copiadas:
            out["a"]["candidatos_falso_negativo"].append({"chunk_id": cid, "formas_en_el_texto": hallados})
    md += ["", "**Fichas con una forma de la lista en el texto propio y sin nada copiado** (candidatos a falso negativo; "
           "se leen):", ""]
    for x in out["a"]["candidatos_falso_negativo"]:
        md += [f"- `{x['chunk_id']}` ({', '.join(x['formas_en_el_texto'])}): {corto(r2[x['chunk_id']].get('texto'), 500)}"]
    # ---- b ----
    md += ["", "## b, Condicion de un ítem sin `condicion_de` (brazo nuevo)", ""]
    for cid, f in sorted(filas.items()):
        for lab in f.get("condicion_item_sin_condicion_de") or []:
            out["b"].append({"chunk_id": cid, "condicion": lab})
            md += [f"- `{cid}` «{lab}» | ítem: {corto(r2[cid].get('texto'), 300)} | encabezado: "
                   f"{corto((r2[cid].get('herencia') or [{}])[PR.bloque_lista(r2[cid]) or -1].get('texto'), 260)}"]
    # ---- c ----
    mod_chars = sum(len(str(c["tramo"])) for c in out["a"]["copiadas"])
    minis = [cid for cid, f in filas.items() if f.get("mini_a_mitad")]
    out["c"] = {"caracteres_copiados_modalidad_y_consecuencia": mod_chars, "entidades_con_copia": len(out["a"]["copiadas"]),
                "mini_a_mitad": {cid: {b: filas[cid]["usage"][b]["output_tokens"] for b in ("sellado", "nuevo")}
                                 for cid in minis},
                "orden_de_lectura": {cid: {k: v for k, v in filas[cid]["orden_de_lectura"].items() if "orden" in k}
                                     for cid in minis}}
    md += ["", "## c, salida de a, b y h", "", "```", json.dumps(out["c"], ensure_ascii=False, indent=1), "```"]
    (sal / "apoyo_lectura_p4.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (sal / "apoyo_lectura_p4.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"d1": {k: f"{v['cubiertas']}/{v['cuantias']}" for k, v in out["d1"].items()},
                      "d5": len(out["d5"]), "d6": len(out["d6"]), "a_copiadas": len(out["a"]["copiadas"]),
                      "a_candidatos_fn": len(out["a"]["candidatos_falso_negativo"]), "b": len(out["b"]), "c": out["c"]},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
