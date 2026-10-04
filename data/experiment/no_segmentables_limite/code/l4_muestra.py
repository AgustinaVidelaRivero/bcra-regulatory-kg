"""U-NOSEG-LIMITE, L4 — sorteo de la muestra declarada en `l4_declaracion_muestra.md`.

Solo lectura del repo, USD 0. No lee texto: arma las poblaciones por estrato y sortea las páginas.
Escribe `l4_muestra.json` en el directorio de la unidad.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/no_segmentables_limite/code/l4_muestra.py \
      --roles <roles_por_pagina_todos.json del scratchpad>
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
PART = REPO / "data" / "experiment" / "segmentacion_84" / "b584_particion"
COBA = REPO / "data" / "experiment" / "cobertura_bloque_a"
OUT = REPO / "data" / "experiment" / "no_segmentables_limite"
DECL = OUT / "l4_declaracion_muestra.md"
SHA_DECL = "d39135d46234cb4f3af1c774be14d9ab266d58b679aecc434e5975edf8d9721b"
SEMILLA = 20261004
NUEVE = ("ri_chr", "ri_con", "ri_fcem", "ri_itme", "ri_pfmipyme", "ri_pscpp", "ri_pspii", "ri_rem", "ri_tii")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--roles", required=True)
    a = ap.parse_args()
    if sha(DECL) != SHA_DECL:
        raise SystemExit("la declaración de L4 cambió después de sellarse")
    roles = json.loads(Path(a.roles).read_text(encoding="utf-8"))
    cont = json.loads((PART / "conteos_b584.json").read_text(encoding="utf-8"))
    for t, v in roles.items():
        assert v["control_b584"] and v["conteo"] == cont[t]["roles_pagina"], t

    def pags(to, rol):
        return [i + 1 for i, r in enumerate(roles[to]["roles"]) if r == rol]

    # estrato 3: páginas de cuerpo listadas por las unidades que cruzan fichas (regla de L2, partición)
    l2 = json.loads((OUT / "l2_regla_parciales.json").read_text(encoding="utf-8"))
    pob3 = []
    for to in ("manual", "ri2_pm"):
        rs = l2["por_fuente"]["particion"][to]
        cruzan = set(rs["cruzan_fichas"]["ids"])
        chunks = json.loads((PART / to / f"chunks_{to}.json").read_text(encoding="utf-8"))
        chunks = chunks["chunks"] if isinstance(chunks, dict) else chunks
        listadas = {p for c in chunks if c["id"] in cruzan for p in c["paginas"]}
        por_punto = set(rs["por_punto"]["paginas"])
        cuerpo = set(pags(to, "cuerpo"))
        pob3 += [(to, p) for p in sorted((listadas - por_punto) & cuerpo)]

    censo = json.loads((COBA / "censo_forma.json").read_text(encoding="utf-8"))
    pob4 = [(to, d["pagina"]) for to in NUEVE
            for d in censo["bloque_a_extraccion"][to]["paginas_detalle"] if d["clase_forma"] == "planilla_ficha"]

    estratos = [
        ("1_ficha_manual", [("manual", p) for p in pags("manual", "ficha_registro")], 20),
        ("2_ficha_ri2_pm", [("ri2_pm", p) for p in pags("ri2_pm", "ficha_registro")], 10),
        ("3_cuerpo_entre_fichas", pob3, 10),
        ("4_planilla_nueve", pob4, 10),
        ("5_optico", [("optico", p) for p in range(1, len(roles["optico"]["roles"]) + 1)], 3),
        ("6_plandecuentas", [("plandecuentas", p) for p in range(1, len(roles["plandecuentas"]["roles"]) + 1)], 3),
        ("7_ri_spi", [("ri_spi", p) for p in range(1, len(roles["ri_spi"]["roles"]) + 1)], 3),
    ]
    muestra, pobl = [], {}
    for nombre, pob, k in estratos:
        pob = sorted(pob)
        rng = random.Random(SEMILLA)
        sel = sorted(rng.sample(pob, k)) if len(pob) >= k else pob
        pobl[nombre] = {"n_poblacion": len(pob), "k": k, "k_efectivo": len(sel)}
        for to, p in sel:
            muestra.append({"estrato": nombre, "to": to, "pagina": p, "rol_pagina": roles[to]["roles"][p - 1]})
    res = {"_meta": {"unidad": "U-NOSEG-LIMITE, L4", "declaracion": str(DECL.relative_to(REPO)),
                     "sha256_declaracion": SHA_DECL, "semilla": SEMILLA, "sha256_roles": sha(Path(a.roles))},
           "poblaciones": pobl, "poblacion_estrato_3": pob3, "poblacion_estrato_4": pob4, "muestra": muestra}
    (OUT / "l4_muestra.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(pobl, ensure_ascii=False))
    print(len(muestra), [(m["estrato"][:1], m["to"], m["pagina"]) for m in muestra])


if __name__ == "__main__":
    main()
