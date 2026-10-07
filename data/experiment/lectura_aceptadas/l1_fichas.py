"""
l1_fichas.py — U-LECTURA-ACEPTADAS, L1, punto 1 (mandato FIRMADO en 9502ca4, §4): las 60 fichas de la muestra
sellada en L0, SIN veredicto (la mesa las lee a ciegas). USD 0, sin API.

Por unidad: id, TO, páginas, estado, estrato, el texto propio y el heredado del chunk de E0 r2b (una parte de una
partición por corte usa el chunk de su unidad, §2), y los nodos y aristas del grafo evaluado sin la cola
(ens_diez_r2b_sincola/r2/kg.json, e22fae1a…) cuya procedencia (alguna de `provenances`) tiene el chunk_id de la
unidad, con su tramo. Cada nodo y arista lleva una referencia local (N1…, A1…, R1…, E1…) para citarlo en la lectura.

Clase de cada arista (declarada para leer, no cambia el criterio):
  - extraccion: los predicados del esquema que emite E1 (aplica_a, condicion_de, condiciona, ejecuta, exceptua,
    exceptua_obligacion, limita, prohibe, regula, requiere);
  - remision_derivada: remite_a, que deriva el código desde el texto de E0 (plan de remite_a, decisión 5);
  - catalogo_sujetos: padre_sugerido (sujeto propuesto → sujeto del catálogo);
  - estructural: establecida_en, miembro_de, subclase_de, instancia_de, parte_de, referencia, modificada_por.

Controles: el sha256 de sellos_l0.json es el que se pasa; la población y la muestra se recomputan desde el sello
(sha256 de la lista y de la muestra, y el sorteo con la semilla); la hora de las fichas es posterior a la del sorteo.

Corre desde la raíz de una COPIA del repo (CLAUDE.md §4.l) y escribe solo --salida/fichas_l1.{jsonl,md} y
--salida/fichas_l1_cabecera.json (horas, sha256 del sello, del kg y de las dos salidas).
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/lectura_aceptadas/l1_fichas.py \
      --sellos <ruta>/sellos_l0.json --sellos-sha256 <sha> --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
SALIDA_R2B = REX / "corpus_tanda0" / "salida_r2b"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
KG = REX / "corpus_tanda0" / "ens_diez_r2b_sincola" / "r2" / "kg.json"
KG_SHA256 = "e22fae1afc3cf37fbe5b49ee0b220d51d0ec5febc13abeb6ebf7b74226da34fb"
ESTRATOS = ("item", "no_item")

EXTRACCION = {"aplica_a", "condicion_de", "condiciona", "ejecuta", "exceptua", "exceptua_obligacion", "limita",
              "prohibe", "regula", "requiere"}
ESTRUCTURAL = {"establecida_en", "miembro_de", "subclase_de", "instancia_de", "parte_de", "referencia",
               "modificada_por"}
CAMPOS_ARISTA = ("sujeto_mencion", "mencion_verificada", "metodo_resolucion", "sujeto_id_modelo",
                 "sujeto_mencion_modelo", "rol_fuente", "calificador", "coherencia_tipo_predicado",
                 "properties_no_definidas")
CAMPOS_NODO = ("rol_fuente", "originales", "fuera_de_lista", "properties_no_definidas")
CAMPOS_PROC = ("punto", "rol_documental", "tramo", "tramo_verificado", "termino_verificado", "tramo_modelo",
               "paginas")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canon(x) -> bytes:
    return json.dumps(x, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def clase_arista(rel: str) -> str:
    if rel == "remite_a":
        return "remision_derivada"
    if rel == "padre_sugerido":
        return "catalogo_sujetos"
    if rel in ESTRUCTURAL:
        return "estructural"
    if rel in EXTRACCION:
        return "extraccion"
    raise SystemExit(f"predicado sin clase: {rel}")


def norm(s) -> str:
    """Para el .md: espacios simples (el .jsonl guarda el texto tal cual)."""
    return re.sub(r"\s+", " ", s or "").strip()


def ultima_version(to: str) -> dict:
    out = {}
    for x in (SALIDA_R2B / to / "finales.jsonl").read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            out[r["chunk_id"]] = r
    return out


def chunks(to: str) -> dict:
    d = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    return {c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)}


def verificar_sello(s: dict) -> dict:
    filas = s["poblacion"]["filas"]
    if sha(canon(filas)) != s["poblacion"]["sha256_lista"]:
        raise SystemExit("la lista de la población no da su sha256 sellado")
    muestra = {e: [m["id"] for m in s["sorteo"]["muestra"][e]] for e in ESTRATOS}
    if sha(canon(muestra)) != s["sorteo"]["sha256_muestra"]:
        raise SystemExit("la muestra no da su sha256 sellado")
    for e in ESTRATOS:
        ids_e = sorted(f[0] for f in filas if f[3] == e)
        if random.Random(f"{s['sorteo']['semilla']}:{e}").sample(ids_e, s["sorteo"]["n_por_estrato"]) != muestra[e]:
            raise SystemExit(f"el sorteo del estrato {e} no reproduce la muestra sellada")
    return muestra


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sellos", type=Path, required=True)
    ap.add_argument("--sellos-sha256", required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()

    s_sellos = sha(a.sellos.read_bytes())
    if s_sellos != a.sellos_sha256:
        raise SystemExit(f"sellos_l0.json con sha256 {s_sellos}, no {a.sellos_sha256}")
    s = json.loads(a.sellos.read_text(encoding="utf-8"))
    muestra = verificar_sello(s)
    hora = datetime.now().astimezone().isoformat(timespec="seconds")
    if datetime.fromisoformat(hora) <= datetime.fromisoformat(s["sorteo"]["hora"]):
        raise SystemExit(f"hora de las fichas {hora} no posterior al sorteo {s['sorteo']['hora']}")
    s_kg = sha(KG.read_bytes())
    if s_kg != KG_SHA256 or s_kg != s["grafo"]["kg_sha256"]:
        raise SystemExit(f"kg.json con sha256 {s_kg}, no el sellado")
    kg = json.loads(KG.read_text(encoding="utf-8"))
    nodos_kg = {n["id"]: n for n in kg["nodes"]}
    poblacion = {f[0]: f for f in s["poblacion"]["filas"]}

    fichas, md = [], [
        "# U-LECTURA-ACEPTADAS, L1: las 60 fichas de la muestra sellada (sin veredicto)", "",
        f"Sello L0: `sellos_l0.json` (sha256 `{s_sellos}`), sorteo a las {s['sorteo']['hora']}; fichas generadas a las "
        f"{hora}. Grafo: KG-Tanda0-Diez-r2b-sincola (`{s_kg[:8]}…`). Criterio (mandato §1, el de T4): una unidad tiene "
        "error si al menos un nodo o una relación suya no se sostiene en el texto de la unidad (propio o heredado); las "
        "omisiones van aparte y no cuentan como error.", "",
        "Clases de arista: **extraccion** (predicados que emite E1), **remision_derivada** (`remite_a`, la deriva el "
        "código desde el texto de E0), **catalogo_sujetos** (`padre_sugerido`) y **estructural** (`establecida_en` y "
        "las del esqueleto). Las remisiones se agrupan por origen y destino; el detalle de cada arista está en "
        "`fichas_l1.jsonl`.", ""]
    n_global = 0
    for e in ESTRATOS:
        for orden, cid in enumerate(muestra[e], 1):
            n_global += 1
            fila = poblacion[cid]
            to = fila[1]
            base = cid.split("::parte")[0]
            c = chunks(to)[base]
            fin = ultima_version(to)[cid]
            if fin["estado"] != fila[2] or fila[3] != e:
                raise SystemExit(f"{cid}: estado o estrato distintos del sello")

            nodos, refs = [], {}
            for n in kg["nodes"]:
                provs = [p for p in n["provenances"] if p.get("chunk_id") == cid]
                if not provs:
                    continue
                ref = f"N{len(nodos) + 1}"
                refs[n["id"]] = ref
                nodos.append({"ref": ref, "id": n["id"], "type": n["type"], "label": n["label"],
                              "properties": n.get("properties") or {},
                              "procedencia": [{k: p[k] for k in CAMPOS_PROC if k in p} for p in provs],
                              "procedencias_en_el_grafo": len(n["provenances"]),
                              **{k: n[k] for k in CAMPOS_NODO if k in n}})

            def extremo(nid: str) -> dict:
                m = nodos_kg[nid]
                return {"ref": refs.get(nid), "id": nid, "type": m["type"], "label": m["label"]}

            aristas, cont = [], Counter()
            for x in kg["edges"]:
                provs = [p for p in x["provenances"] if p.get("chunk_id") == cid]
                if not provs:
                    continue
                cl = clase_arista(x["relation"])
                cont[cl] += 1
                pref = {"extraccion": "A", "remision_derivada": "R", "catalogo_sujetos": "C", "estructural": "E"}[cl]
                ref = f"{pref}{cont[cl]}"
                aristas.append({"ref": ref, "clase": cl, "relation": x["relation"], "source": extremo(x["source"]),
                                "target": extremo(x["target"]), "properties": x.get("properties") or {},
                                "procedencia": [{k: p[k] for k in CAMPOS_PROC if k in p} for p in provs],
                                **{k: x[k] for k in CAMPOS_ARISTA if k in x}})
            ficha = {
                "n": n_global, "estrato": e, "orden_sorteo": orden, "id": cid, "to": to,
                "chunk": base, "unidad": c["unidad"], "tipo": c.get("tipo"), "titulo": c.get("titulo"),
                "paginas": c.get("paginas"), "estado": fin["estado"], "n_reintentos": fin.get("n_reintentos"),
                "flags": {k: v for k, v in (c.get("flags") or {}).items() if v},
                "texto_propio": c.get("texto") or "",
                "heredado": [{"tipo": h.get("tipo"), "unidad_origen": h.get("unidad_origen"), "texto": h.get("texto")}
                             for h in c.get("herencia") or []],
                "nodos": nodos, "aristas": aristas,
                "conteos": {"nodos": len(nodos), "aristas": len(aristas),
                            "aristas_por_clase": {k: cont[k] for k in ("extraccion", "remision_derivada",
                                                                      "catalogo_sujetos", "estructural")}}}
            fichas.append(ficha)

            # .md
            md += [f"## {n_global}. `{cid}` — estrato {e} ({orden} del sorteo) · {to} · págs. "
                   f"{', '.join(map(str, c.get('paginas') or []))} · estado `{fin['estado']}`", ""]
            if base != cid:
                md += [f"(parte de una partición por corte: usa el chunk de `{base}`)", ""]
            if ficha["flags"]:
                md += [f"Flags de E0: `{json.dumps(ficha['flags'], ensure_ascii=False)}`", ""]
            for h in ficha["heredado"]:
                md.append(f"> *heredado ({h['tipo']}, {h['unidad_origen']}):* {norm(h['texto'])}")
            md += [f"> *propio:* {norm(ficha['texto_propio'])}", ""]
            md.append(f"**Nodos ({len(nodos)})**")
            for n in nodos:
                props = {k: v for k, v in n["properties"].items() if k != "descripcion" and v not in (None, "", [], {})}
                desc = n["properties"].get("descripcion")
                for p in n["procedencia"]:
                    md.append(f"- **{n['ref']}** {n['type']} «{n['label']}»"
                              + (f" — {norm(desc)}" if desc else "")
                              + (f" · props: `{json.dumps(props, ensure_ascii=False)}`" if props else "")
                              + (f" · tramo ({p.get('tramo_verificado')}): «{norm(p.get('tramo'))}»" if p.get("tramo")
                                 else " · sin tramo")
                              + f" · {p.get('rol_documental')}"
                              + (f" · compartido ({n['procedencias_en_el_grafo']} procedencias en el grafo)"
                                 if n["procedencias_en_el_grafo"] > 1 else ""))
            ext = [x for x in aristas if x["clase"] == "extraccion"]
            md += ["", f"**Aristas de la extracción ({len(ext)})**"]
            for x in ext:
                t = x["target"]
                men = (f" (mención «{x['sujeto_mencion']}», {x.get('mencion_verificada')}, "
                       f"{x.get('metodo_resolucion')})") if x.get("sujeto_mencion") is not None else ""
                md.append(f"- **{x['ref']}** {x['source']['ref'] or x['source']['id']} —{x['relation']}→ "
                          f"{t['ref'] or ''} {t['type']} «{t['label']}»{men}"
                          + (f" [coherencia: {x['coherencia_tipo_predicado']}]" if x.get("coherencia_tipo_predicado")
                             else "")
                          + (f" · props `{json.dumps(x['properties'], ensure_ascii=False)}`" if x["properties"] else ""))
            rem = [x for x in aristas if x["clase"] == "remision_derivada"]
            md += ["", f"**Remisiones derivadas ({len(rem)} aristas)**"]
            grupos: dict = {}
            for x in rem:
                k = (x["source"]["ref"] or x["source"]["id"], x["properties"].get("destino"),
                     x["properties"].get("alcance"), norm(x["properties"].get("evidencia")))
                grupos.setdefault(k, []).append(x)
            for (src, dest, alc, evid), xs in grupos.items():
                md.append(f"- **{xs[0]['ref']}"
                          + (f"–{xs[-1]['ref']}" if len(xs) > 1 else "")
                          + f"** {src} —remite_a→ `{dest}` ({alc}; {len(xs)} nodo(s) destino: "
                          + "; ".join(f"{y['target']['type']} «{y['target']['label']}»" for y in xs)
                          + f") · evidencia «{evid}»")
            cat = [x for x in aristas if x["clase"] == "catalogo_sujetos"]
            if cat:
                md += ["", f"**Catálogo de sujetos ({len(cat)})**"]
                for x in cat:
                    md.append(f"- **{x['ref']}** {x['source']['type']} «{x['source']['label']}» —padre_sugerido→ "
                              f"{x['target']['type']} «{x['target']['label']}»")
            est = [x for x in aristas if x["clase"] == "estructural"]
            md += ["", f"**Estructurales ({len(est)})**: "
                   + "; ".join(f"{k} ×{v}" for k, v in Counter(
                       f"{x['relation']} → {x['target']['type']} «{x['target']['label']}»" for x in est).items()), ""]

    if len(fichas) != 60 or Counter(f["estrato"] for f in fichas) != Counter({"item": 30, "no_item": 30}):
        raise SystemExit("no son 60 fichas, 30 por estrato")
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "fichas_l1.jsonl").write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in fichas) + "\n", encoding="utf-8")
    (a.salida / "fichas_l1.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    cab = {"unidad": "U-LECTURA-ACEPTADAS, L1 (fichas sin veredicto)", "hora": hora,
           "sellos_l0_sha256": s_sellos, "sha256_muestra": s["sorteo"]["sha256_muestra"],
           "hora_sorteo": s["sorteo"]["hora"], "kg_sha256": s_kg, "fichas": len(fichas),
           "fichas_l1.jsonl_sha256": sha((a.salida / "fichas_l1.jsonl").read_bytes()),
           "fichas_l1.md_sha256": sha((a.salida / "fichas_l1.md").read_bytes()),
           "l1_fichas.py_sha256": sha(Path(__file__).read_bytes())}
    (a.salida / "fichas_l1_cabecera.json").write_text(json.dumps(cab, ensure_ascii=False, indent=1) + "\n",
                                                       encoding="utf-8")
    print(json.dumps({"hora": hora, "fichas": len(fichas),
                      "nodos": sum(f["conteos"]["nodos"] for f in fichas),
                      "aristas": sum(f["conteos"]["aristas"] for f in fichas),
                      "por_clase": dict(sum((Counter(f["conteos"]["aristas_por_clase"]) for f in fichas), Counter()))},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
