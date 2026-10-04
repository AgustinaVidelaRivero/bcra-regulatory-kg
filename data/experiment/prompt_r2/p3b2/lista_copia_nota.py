"""
lista_copia_nota.py — U-PROMPT-R2, P3b-2 (USD 0, sin API): la lista lado a lado de los 45 casos de copia de la nota de
E3 de la tanda 0 (p3b/salida/lazo_e3_p3b.json, corrida salida_dirigida), para leerlos con la regla fijada antes en
regla_lectura_copia_nota.md. Por caso: la unidad (texto propio y heredado), las notas, el texto de la entidad, las
ventanas en común y, como ayuda de la regla, las palabras de contenido de las ventanas que no están en el texto de la
unidad y las de metalenguaje del verificador.

Escribe solo en --salida (lista_copia_nota.md y lista_copia_nota.json). Sobre una copia del repo (regla l).

Uso (desde la raíz de la copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3b2/lista_copia_nota.py --salida DIR
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REX / "e1_extractor"))
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
import comun_e1  # noqa: E402
import validador_r2 as V  # noqa: E402

LAZO = REPO / "data" / "experiment" / "prompt_r2" / "p3b" / "salida" / "lazo_e3_p3b.json"
E0 = REX / "e0_chunking" / "salida_tanda0"
CORRIDA = "salida_dirigida"
# Palabras vacías (lista cerrada de la regla): artículos, preposiciones, conjunciones, pronombres y las formas de
# «ser», «estar» y «haber», en tokens de R-NORM.
VACIAS = frozenset("""el la los las un una unos unas lo al del a ante bajo con contra de desde durante en entre hacia
hasta mediante para por segun sin sobre tras y e ni o u pero sino que como cuando donde si no se su sus le les me te nos
os mi mis tu tus este esta estos estas ese esa esos esas aquel aquella aquellos aquellas esto eso ello ellos ellas el
ella cual cuales quien quienes cuyo cuya cuyos cuyas ser es son era eran fue fueron sera seran sea sean sido siendo
estar esta estan estaba estaban estuvo estara este esten haber ha han habia habian hubo habra haya hayan habido
""".split())
METALENGUAJE = ("falta", "faltan", "faltante", "faltantes", "representado", "representada", "omite", "omitido",
                "omitida", "extraccion", "extractor", "chunk", "unidad", "nodo", "entidad", "deberia")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    sal = ap.parse_args().salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    sal.mkdir(parents=True, exist_ok=True)
    lazo = json.loads(LAZO.read_text(encoding="utf-8"))
    casos = lazo["corridas"][CORRIDA]["k"]["copia_nota"]["casos"]
    tos = sorted({c["chunk_id"].split("::")[0] for c in casos})
    chunks = {c["id"]: c for c in comun_e1.cargar_chunks(tuple(tos), e0_dir=E0)}
    filas, md = [], [f"# Lista lado a lado de los casos de copia de la nota ({CORRIDA})", "",
                     f"{len(casos)} casos en {len({c['chunk_id'] for c in casos})} unidades. Regla: "
                     "`regla_lectura_copia_nota.md`.", ""]
    for i, c in enumerate(casos, 1):
        ch = chunks[c["chunk_id"]]
        texto = V.texto_completo(ch)
        toks_unidad = set(V.norm_tokens(texto))
        toks_v = {t for w in c["ventanas"] for t in w.split()}
        ausentes = sorted(t for t in toks_v if t not in VACIAS and t not in toks_unidad)
        meta = sorted(t for t in toks_v if t in METALENGUAJE)
        filas.append({"n": i, "chunk_id": c["chunk_id"], "local_id": c["local_id"], "type": c["type"],
                      "campo": c["campo"], "texto": c["texto"], "ventanas": c["ventanas"], "notas": c["notas"],
                      "contenido_ausente_de_la_unidad": ausentes, "metalenguaje": meta})
        md += [f"## {i}. `{c['chunk_id']}` — {c['local_id']} ({c['type']}), {c['campo']}", "",
               f"- **Entidad:** {c['texto']}", f"- **Ventanas:** {'; '.join(c['ventanas'])}",
               f"- **Contenido ausente de la unidad:** {', '.join(ausentes) or '—'}",
               f"- **Metalenguaje:** {', '.join(meta) or '—'}"]
        md += [f"- **Nota {k}:** {n}" for k, n in enumerate(c["notas"], 1)]
        md += ["- **Unidad (propio y heredado):**", "", "```", texto.strip(), "```", ""]
    (sal / "lista_copia_nota.json").write_text(json.dumps(filas, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (sal / "lista_copia_nota.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{len(filas)} casos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
