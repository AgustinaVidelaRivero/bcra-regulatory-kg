"""
comunicacion_p3b.py — U-PROMPT-R2, P3b-1 (USD 0, sin API): punto l de la etapa P3b (hallazgo 1.12).

Hoy `validador_r2.derivar_comunicacion(codigo, label)` da A, B o C con cualquier código de la forma «A-39»: una ley
escrita como Comunicación pasa la derivación (`ctacte::12.10.2`, «art. 39 inc. d) de la Ley 21.526» → «A»).
Regla propuesta, solo con la forma r2 (que trae el `tramo` de evidencia de la entidad):
  1. si el tramo nombra una Comunicación (com. o comunicación, la letra A, B o C y un número), el tipo es esa letra;
  2. si no, y el tramo nombra una norma externa (el léxico `lexico_externa` de la política), el tipo es «externa»;
  3. si no, no se deriva: el código solo no alcanza; se cuenta.
La forma v3 no cambia (los grafos r2a sellados no se tocan).

La regla lee el tramo solo si verificó (exacta o por tokens): el tramo verificado es texto de la unidad, y la etiqueta
y el código los escribe el modelo.

Medida: sobre los 22 nodos Comunicacion de KG-Tanda0-Diez-r2a y sobre las entidades Comunicacion del primer intento
de la tanda 0. El crudo v3 no trae `tramo`, así que se mide de dos maneras: con la etiqueta como sustituto del tramo
(lo que escribió el modelo) y con el texto de la unidad (propio y heredado de la E0 legada): si contiene la mención de
una Comunicación con el número del código, un tramo verificado la sostendría.

Uso (desde la raíz de una copia):
  .venv/bin/python -B data/experiment/prompt_r2/p3b/comunicacion_p3b.py --salida DIR
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

P3B = Path(__file__).resolve().parent
REPO = P3B.parents[3]
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
import validador_r2 as V  # noqa: E402

KG = REPO / "data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/r2/kg.json"
E0 = REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0"
SAL_T0 = REPO / "data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
RE_COM_EN_TRAMO = re.compile(r"\bcom(?:unicacion(?:es)?)?\b\.?\s*[\"'“”«»]?\s*([abc])\s*[\"'“”«»]?\s*(?:-|–|\s)\s*"
                             r"(?:n[°ºo]\.?\s*)?(\d[\d.]*(?:\s*(?:,|y|e)\s*\d[\d.]*)*)")


def numeros(grupo: str) -> list[str]:
    """Los números de una mención, también en una enumeración («A 5867, 5926 y 5970»)."""
    return [x.replace(".", "").rstrip(".") for x in re.findall(r"\d[\d.]*", grupo)]


def propuesta(tramo: str | None, pol) -> str | None:
    t = V.fold(tramo or "")
    m = RE_COM_EN_TRAMO.search(t)
    if m:
        return m.group(1).upper()
    if V.nombra_norma_externa(tramo, pol.lexico_externa):
        return "externa"
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    sal = ap.parse_args().salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    pol = V.politica_default()
    kg = json.loads(KG.read_text(encoding="utf-8"))
    sys.path.insert(0, str(REPO / "data" / "experiment" / "reextraccion_v2" / "e1_extractor"))
    import comun_e1  # noqa: PLC0415
    chunks = {c["id"]: c for c in comun_e1.cargar_chunks(TOS, e0_dir=E0)}

    def sostiene(cid: str | None, codigo) -> str:
        """Lo que daría la regla con un tramo verificado tomado del texto de la unidad."""
        c = chunks.get(cid or "")
        if c is None:
            return "sin_chunk"
        num = re.search(r"\d[\d.]*", str(codigo or ""))
        texto = V.fold(V.texto_completo(c))
        for m in RE_COM_EN_TRAMO.finditer(texto):
            if num and num.group(0).replace(".", "").rstrip(".") in numeros(m.group(2)):
                return m.group(1).upper()
        return "externa" if V.nombra_norma_externa(V.texto_completo(c), pol.lexico_externa) else "sin_sustento"
    nodos = []
    for n in kg["nodes"]:
        if n["type"] != "Comunicacion":
            continue
        p = n["properties"]
        nodos.append({"id": n["id"], "label": n["label"], "codigo": p.get("codigo"), "tipo_grafo": p.get("tipo"),
                      "hoy": V.derivar_comunicacion(p.get("codigo"), n["label"]),
                      "propuesta_con_etiqueta": propuesta(n["label"], pol),
                      "propuesta_con_texto_de_la_unidad": sostiene(n["provenance"].get("chunk_id"), p.get("codigo")),
                      "chunk_id": n["provenance"].get("chunk_id")})
    crudo = Counter()
    cambios = []
    for to in TOS:
        for linea in (SAL_T0 / to / "extracciones_e1_compact.jsonl").read_text(encoding="utf-8").splitlines():
            r = json.loads(linea)
            ti = r.get("tool_input_crudo")
            ents = V._coerce_lista(ti.get("entities")) if isinstance(ti, dict) else None
            for e in ents or []:
                if not isinstance(e, dict) or e.get("type") != "Comunicacion":
                    continue
                props = e.get("properties") if isinstance(e.get("properties"), dict) else {}
                hoy = V.derivar_comunicacion(props.get("codigo"), e.get("label"))
                nueva = propuesta(e.get("label"), pol)
                crudo[(str(hoy), str(nueva))] += 1
                if hoy in ("A", "B", "C") and nueva != hoy:
                    cambios.append({"chunk_id": r["chunk_id"], "label": e.get("label"), "codigo": props.get("codigo"),
                                    "hoy": hoy, "propuesta": nueva})
    res = {"comando": "data/experiment/prompt_r2/p3b/comunicacion_p3b.py --salida DIR",
           "kg": str(KG.relative_to(REPO)), "nodos": nodos,
           "nodos_resumen": {"total": len(nodos),
                             "hoy_A_B_C": sum(1 for x in nodos if x["hoy"] in ("A", "B", "C")),
                             "propuesta_A_B_C": sum(1 for x in nodos if x["propuesta_con_etiqueta"] in ("A", "B", "C")),
                             "cambian_con_etiqueta": [x["id"] for x in nodos if x["hoy"] != x["propuesta_con_etiqueta"]],
                             "con_texto_de_la_unidad": dict(Counter(f"{x['hoy']} → {x['propuesta_con_texto_de_la_unidad']}"
                                                                    for x in nodos))},
           "crudo_primer_intento": {"pares_hoy_propuesta": {f"{a} → {b}": n for (a, b), n in sorted(crudo.items())},
                                    "dejan_de_derivar_A_B_C": cambios}}
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "comunicacion_p3b.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in res.items() if k != "nodos"}, ensure_ascii=False, indent=1)[:3000])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
