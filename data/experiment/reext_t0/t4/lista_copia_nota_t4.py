"""U-REEXT-T0, T4, punto 3: la lista lado a lado de los casos de copia de la nota de E3 de esta corrida (salida_r2b de
los diez TOs), para leerlos con la regla fijada antes (data/experiment/prompt_r2/p3b2/regla_lectura_copia_nota.md, sin
ajustes). Mismo armado que data/experiment/prompt_r2/p3b2/lista_copia_nota.py (sus listas cerradas de palabras vacías y
de metalenguaje se importan, no se copian), con la población de esta corrida:

  - casos: las marcas `copia_nota_e3` de la validación final de cada unidad (finales.jsonl, última versión por unidad;
    solo las aceptadas tras reintento las llevan): por entidad marcada, un caso por campo (descripcion o label), con
    sus ventanas; se cotejan con copias_nota_e3.jsonl (el registro del ratchet, que es de anexar: vale la última línea
    por unidad);
  - notas: las de los faltantes de la verificación anterior al último reintento de la unidad (veredictos.jsonl), que
    son el feedback del reintento; se marca cuáles contienen alguna ventana;
  - texto de la unidad: propio y heredado, de la E0 r2b (validador_r2.texto_completo).

Clases de la regla, en orden: 1 (metalenguaje en las ventanas) y 3 (una palabra de contenido de las ventanas que no está
en el texto de la unidad) salen del cotejo mecánico; si todas las palabras de contenido están en la unidad, el caso es 2
o 4 y queda para leer. Escribe --out (JSON) y --md. USD 0, sin red.

Uso (desde la raíz del repo o de una copia): python -B data/experiment/reext_t0/t4/lista_copia_nota_t4.py --out J --md M
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
REX = RAIZ / "data" / "experiment" / "reextraccion_v2"
SALIDA = REX / "corpus_tanda0" / "salida_r2b"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
REGLA = RAIZ / "data" / "experiment" / "prompt_r2" / "p3b2" / "regla_lectura_copia_nota.md"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "prompt_r2" / "p3b2"))
import lista_copia_nota as L0  # noqa: E402 — VACIAS y METALENGUAJE de la regla, importadas
V = L0.V


def candidatos_flexion(t: str, toks_unidad: set) -> list[str]:
    """Ayuda de lectura (no decide): palabras de la unidad que comparten con t todo menos las 3 últimas letras (al
    menos 4), candidatas a ser una flexión de t. La regla 2 cuenta las flexiones como presentes; una derivación
    (nominalización, otro verbo) es otra palabra."""
    raiz = t[:max(4, len(t) - 3)]
    return sorted(u for u in toks_unidad if u != t and u.startswith(raiz) and abs(len(u) - len(t)) <= 4)


def ultima(path: Path) -> dict:
    out = {}
    if path.exists():
        for x in path.read_text(encoding="utf-8").splitlines():
            if x.strip():
                r = json.loads(x)
                out[r["chunk_id"]] = r
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--md", type=Path, required=True)
    a = ap.parse_args()
    import hashlib  # noqa: PLC0415
    regla_sha = hashlib.sha256(REGLA.read_bytes()).hexdigest()
    chunks = {}
    for to in TOS:
        d = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
        chunks.update({c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)})
    casos, cotejo = [], {"unidades_finales": 0, "unidades_registro": 0, "iguales": 0, "distintas": []}
    for to in TOS:
        fin, reg = ultima(SALIDA / to / "finales.jsonl"), ultima(SALIDA / to / "copias_nota_e3.jsonl")
        ver = [json.loads(x) for x in (SALIDA / to / "veredictos.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
        marc = {cid: (r.get("validacion_final") or {}).get("marcas_e3", {}).get("copia_nota_e3")
                for cid, r in fin.items()}
        marc = {cid: m for cid, m in marc.items() if m}
        cotejo["unidades_finales"] += len(marc)
        cotejo["unidades_registro"] += len(reg)
        for cid in sorted(set(marc) | set(reg)):
            if marc.get(cid) == (reg.get(cid) or {}).get("entidades"):
                cotejo["iguales"] += 1
            else:
                cotejo["distintas"].append({"chunk_id": cid, "en_finales": cid in marc, "en_registro": cid in reg})
        for cid in sorted(marc):
            r = fin[cid]
            ents = {e.get("local_id"): e for e in (r["validacion_final"].get("entidades") or [])}
            vs = [v for v in ver if v["chunk_id"] == cid]
            n = r.get("n_reintentos") or 0
            previa = [v for v in vs if v.get("intento") == n - 1]
            notas = [f.get("nota") or "" for v in previa[-1:] for f in (v.get("faltantes") or [])]
            texto = V.texto_completo(chunks[cid])
            toks_unidad = set(V.norm_tokens(texto))
            for m in marc[cid]:
                e = ents.get(m["local_id"]) or {}
                for campo, ventanas in m["campos"].items():
                    txt = (e.get("properties") or {}).get("descripcion") if campo == "descripcion" else e.get("label")
                    toks_v = {t for w in ventanas for t in w.split()}
                    ausentes = sorted(t for t in toks_v if t not in L0.VACIAS and t not in toks_unidad)
                    meta = sorted(t for t in toks_v if t in L0.METALENGUAJE)
                    clase = 1 if meta else (3 if ausentes else None)
                    con_ventana = [k for k, nota in enumerate(notas, 1)
                                   if any(w in " ".join(V.norm_tokens(nota)) for w in ventanas)]
                    casos.append({"n": len(casos) + 1, "chunk_id": cid, "to": to, "estado": r["estado"],
                                  "n_reintentos": n, "local_id": m["local_id"], "type": m.get("type"),
                                  "campo": campo, "texto": txt, "ventanas": ventanas, "notas": notas,
                                  "notas_con_ventana": con_ventana, "contenido_ausente_de_la_unidad": ausentes,
                                  "metalenguaje": meta, "clase_mecanica": clase,
                                  "candidatos_de_flexion": {t: candidatos_flexion(t, toks_unidad) for t in ausentes},
                                  "razon_mecanica": ("metalenguaje del verificador en las ventanas: " + ", ".join(meta)
                                                     if meta else ("palabras de contenido ausentes de la unidad: "
                                                                   + ", ".join(ausentes) if ausentes else
                                                                   "todas las palabras de contenido están en la unidad: "
                                                                   "2 o 4, por lectura")),
                                  "texto_unidad": texto})
    res = {"regla": str(REGLA.relative_to(RAIZ)), "regla_sha256": regla_sha, "casos": len(casos),
           "unidades": len({c["chunk_id"] for c in casos}), "por_to": dict(Counter(c["to"] for c in casos)),
           "por_campo": dict(Counter(c["campo"] for c in casos)),
           "clase_mecanica": {str(k): v for k, v in Counter(c["clase_mecanica"] for c in casos).items()},
           "cotejo_con_copias_nota_e3_jsonl": cotejo}
    a.out.write_text(json.dumps({"resumen": res, "casos": casos}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    md = [f"# Lista lado a lado de los casos de copia de la nota de E3 (U-REEXT-T0, T4, punto 3)", "",
          f"{len(casos)} casos en {res['unidades']} unidades. Regla: `{res['regla']}` (sha256 `{regla_sha[:12]}…`, sin "
          "ajustes). Clase mecánica: 1 (metalenguaje), 3 (contenido ausente de la unidad); vacía = 2 o 4, por lectura.", ""]
    for c in casos:
        md += [f"## {c['n']}. `{c['chunk_id']}` — {c['local_id']} ({c['type']}), {c['campo']} — clase mecánica "
               f"{c['clase_mecanica'] or '—'}", "",
               f"- **Entidad:** {c['texto']}", f"- **Ventanas:** {'; '.join(c['ventanas'])}",
               f"- **Contenido ausente de la unidad:** {', '.join(c['contenido_ausente_de_la_unidad']) or '—'}",
               f"- **Candidatos de flexión en la unidad (ayuda):** "
               f"{'; '.join(t + ' → ' + (', '.join(v) or '—') for t, v in c['candidatos_de_flexion'].items()) or '—'}",
               f"- **Metalenguaje:** {', '.join(c['metalenguaje']) or '—'}"]
        md += [f"- **Nota {k}{' (con ventana)' if k in c['notas_con_ventana'] else ''}:** {nota}"
               for k, nota in enumerate(c["notas"], 1)]
        md += ["- **Unidad (propio y heredado):**", "", "```", c["texto_unidad"].strip(), "```", ""]
    a.md.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
