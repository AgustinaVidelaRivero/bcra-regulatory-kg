"""
l0_sellos.py — U-LECTURA-ACEPTADAS, L0 (mandato FIRMADO en 9502ca4, §2 y §3): población, estratos y sorteo,
sellados antes de abrir una unidad. Nada de esto mira una extracción: solo el estado final de cada unidad
(finales.jsonl), el chunk de E0 r2b (para `es_item`) y las listas de unidades que ya leyó T4 de U-REEXT-T0. USD 0.

  Población: las unidades cuya última versión en corpus_tanda0/salida_r2b/<to>/finales.jsonl tiene estado
  completo_ok_directo, aceptado_con_residuales o aceptado_tras_reintento (el grafo evaluado sin la cola,
  KG-Tanda0-Diez-r2b-sincola, sellado en dde9f44 y 235a295).
  Estrato: prompt_r2b.es_item sobre el chunk de e0_chunking/salida_tanda0_r2b/chunks_<to>.json; una parte de una
  partición por corte (`<id>::parteN`) usa el chunk de su unidad (§2 del mandato).
  Sorteo: random.Random(f"{SEMILLA}:{estrato}").sample(sorted(ids del estrato), 30), estrato ∈ {item, no_item}.

Corre desde la raíz de una COPIA del repo (CLAUDE.md §4.l) y escribe solo --salida/sellos_l0.json.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/lectura_aceptadas/l0_sellos.py --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
SALIDA_R2B = REX / "corpus_tanda0" / "salida_r2b"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
KG = REX / "corpus_tanda0" / "ens_diez_r2b_sincola" / "r2" / "kg.json"
E1 = REX / "e1_extractor"
T4 = REPO / "data" / "experiment" / "reext_t0" / "t4" / "salida"
SELLOS_T4 = REPO / "data" / "experiment" / "reext_t0" / "sellos_t4.json"
sys.path.insert(0, str(E1))
import prompt_r2b as P  # noqa: E402 — es_item, importado y no copiado

TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
ACEPTADOS = ("completo_ok_directo", "aceptado_con_residuales", "aceptado_tras_reintento")
ESTRATOS = ("item", "no_item")
SEMILLA = "U-LECTURA-ACEPTADAS:sorteo:2026-10-06"   # decisión 3 de la autora al firmar (9502ca4)
N_POR_ESTRATO = 30
KG_SHA256 = "e22fae1afc3cf37fbe5b49ee0b220d51d0ec5febc13abeb6ebf7b74226da34fb"   # fixture y grafos.py (dde9f44)
# Lecturas de T4 (U-REEXT-T0): archivo y campo con el chunk_id de cada unidad leída.
LECTURAS_T4 = (
    ("punto_1_cola_humana", "fichas_punto1_cola.json", "fichas"),
    ("punto_3_copia_nota", "clasificacion_copia_nota_t4.json", "casos"),
    ("punto_5_p4b", "fichas_punto5_p4b.json", "fichas"),
    ("punto_6_listas", "fichas_punto6_listas.json", "fichas"),
    ("punto_7_grupo_c_fase_a", "fichas_punto7_grupo_c.json", "fichas"),
    ("punto_8_omisiones", "fichas_punto8_omisiones.json", "fichas"),
)


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canon(x) -> bytes:
    return json.dumps(x, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def ultima_version(to: str) -> tuple[dict, int]:
    out, filas = {}, 0
    for x in (SALIDA_R2B / to / "finales.jsonl").read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            out[r["chunk_id"]] = r
            filas += 1
    return out, filas


def chunks(to: str) -> dict:
    d = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    return {c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()

    # el módulo de es_item sale de la misma raíz que este script (la copia), no de otra
    if Path(P.__file__).resolve().parents[4] != REPO:
        raise SystemExit(f"prompt_r2b importado de {P.__file__}, fuera de {REPO}")
    s_kg = sha(KG.read_bytes())
    if s_kg != KG_SHA256:
        raise SystemExit(f"kg.json con sha256 {s_kg}, no el sellado")

    filas_poblacion, filas_finales, ultimas, estados_todos, partes = [], {}, {}, Counter(), []
    for to in TOS:
        ult, n_filas = ultima_version(to)
        filas_finales[to] = n_filas
        ultimas[to] = len(ult)
        estados_todos.update(r["estado"] for r in ult.values())
        ch = chunks(to)
        for cid, r in ult.items():
            if r["estado"] not in ACEPTADOS:
                continue
            base = cid.split("::parte")[0]
            if base != cid:
                partes.append({"id": cid, "chunk_de": base})
            estrato = "item" if P.es_item(ch[base]) else "no_item"
            filas_poblacion.append([cid, to, r["estado"], estrato])
    filas_poblacion.sort(key=lambda f: f[0])
    ids = [f[0] for f in filas_poblacion]
    if len(ids) != len(set(ids)):
        raise SystemExit("ids repetidos en la población")

    N = len(filas_poblacion)
    por_estrato = Counter(f[3] for f in filas_poblacion)
    n1, n2 = por_estrato["item"], por_estrato["no_item"]

    # sorteo
    hora = datetime.now().astimezone().isoformat(timespec="seconds")
    muestra = {}
    for e in ESTRATOS:
        ids_e = sorted(f[0] for f in filas_poblacion if f[3] == e)
        muestra[e] = random.Random(f"{SEMILLA}:{e}").sample(ids_e, N_POR_ESTRATO)
    info = {f[0]: f for f in filas_poblacion}
    muestra_det = {e: [{"orden": i, "id": cid, "to": info[cid][1], "estado": info[cid][2]}
                       for i, cid in enumerate(muestra[e], 1)] for e in ESTRATOS}
    en_muestra = {cid for e in ESTRATOS for cid in muestra[e]}

    # solapamiento con las unidades leídas en T4
    solap = {}
    for punto, nombre, campo in LECTURAS_T4:
        p = T4 / nombre
        leidas = sorted({x["chunk_id"] for x in json.loads(p.read_text(encoding="utf-8"))[campo]})
        solap[punto] = {"fuente": f"data/experiment/reext_t0/t4/salida/{nombre}", "sha256": sha(p.read_bytes()),
                        "unidades_leidas": len(leidas),
                        "en_la_poblacion": sum(1 for x in leidas if x in info),
                        "en_la_muestra": sorted(x for x in leidas if x in en_muestra)}
    todas_t4 = sorted({x for v in solap.values() for x in v["en_la_muestra"]})
    s4 = json.loads(SELLOS_T4.read_text(encoding="utf-8"))
    sellos_t4 = {"fuente": "data/experiment/reext_t0/sellos_t4.json", "sha256": sha(SELLOS_T4.read_bytes()),
                 "a_unidades_p4b_en_la_muestra": sorted(u["id"] for u in s4["a_unidades_p4b"]["unidades"]
                                                        if u["id"] in en_muestra),
                 "b_listas_en_la_muestra": sorted({i for li in s4["b_listas_que_exceptuan"]["listas"]
                                                   for i in li["items"] + [li["intro"], li["contenedor"]]
                                                   if i and i in en_muestra}),
                 "c_orden_completo_en_la_muestra": sorted(x for x in s4["c_grupo_c"]["orden"] if x in en_muestra)}

    out = {
        "unidad": "U-LECTURA-ACEPTADAS, L0 (sello previo; nada se lee todavía)",
        "mandato": {"ruta": "docs/mandatos/ULECTURA_ACEPTADAS_tasa_error_tanda0.md", "commit_firma": "9502ca4"},
        "grafo": {"nombre": "KG-Tanda0-Diez-r2b-sincola", "ruta": str(KG.relative_to(REPO)), "kg_sha256": s_kg,
                  "sc2": "dde9f44", "sello": "235a295"},
        "criterio_poblacion": {"estados": list(ACEPTADOS), "version": "última fila por chunk_id en finales.jsonl",
                               "estrato": "prompt_r2b.es_item sobre el chunk de E0 r2b; una parte usa el chunk de su "
                                          "unidad", "partes": partes},
        "finales": {"filas_por_to": filas_finales, "unidades_por_to": ultimas,
                    "estados_de_todas": dict(sorted(estados_todos.items())), "unidades": sum(ultimas.values())},
        "poblacion": {
            "N": N, "N1_item": n1, "N2_no_item": n2,
            "W1": round(n1 / N, 6), "W2": round(n2 / N, 6), "W1_fraccion": f"{n1}/{N}", "W2_fraccion": f"{n2}/{N}",
            "por_estado": dict(Counter(f[2] for f in filas_poblacion)),
            "por_to": {to: sum(1 for f in filas_poblacion if f[1] == to) for to in TOS},
            "por_estrato_y_estado": {e: dict(Counter(f[2] for f in filas_poblacion if f[3] == e)) for e in ESTRATOS},
            "por_estrato_y_to": {e: {to: sum(1 for f in filas_poblacion if f[3] == e and f[1] == to) for to in TOS}
                                 for e in ESTRATOS},
            "sha256_lista": sha(canon(filas_poblacion)),
            "sha256_ids": sha(("\n".join(ids) + "\n").encode("utf-8")),
            "como_se_calcula_el_sha256": "sha256_lista: json.dumps(filas, ensure_ascii=False, separators=(',', ':')) "
                                         "en UTF-8, filas [id, to, estado, estrato] ordenadas por id; sha256_ids: los "
                                         "ids ordenados, uno por línea, con salto final",
            "filas": filas_poblacion},
        "sorteo": {"semilla": SEMILLA, "fuente_semilla": "decisión 3 de la autora al firmar (9502ca4)",
                   "metodo": "random.Random(f'{semilla}:{estrato}').sample(sorted(ids del estrato), 30)",
                   "n_por_estrato": N_POR_ESTRATO, "hora": hora, "python": sys.version.split()[0],
                   "muestra": muestra_det,
                   "sha256_muestra": sha(canon(muestra)),
                   "como_se_calcula_el_sha256": "json.dumps({'item': [ids en el orden del sorteo], 'no_item': [...]}, "
                                                "ensure_ascii=False, separators=(',', ':')) en UTF-8",
                   "muestra_por_estado": {e: dict(Counter(m["estado"] for m in muestra_det[e])) for e in ESTRATOS},
                   "muestra_por_to": {e: dict(Counter(m["to"] for m in muestra_det[e])) for e in ESTRATOS}},
        "solapamiento_t4": {"por_punto": solap, "unidades_de_la_muestra_leidas_en_t4": todas_t4,
                            "sellos_t4": sellos_t4,
                            "nota": "las unidades leídas en T4 no se excluyen (mandato §3); el punto 7 cuenta las 35 "
                                    "leídas en la fase A"},
        "insumos": {
            "finales_jsonl_sha256": {to: sha((SALIDA_R2B / to / "finales.jsonl").read_bytes()) for to in TOS},
            "e0_salida_tanda0_r2b": {"archivos": len([p for p in E0.iterdir() if p.is_file()]),
                                     "sha256_por_archivo": {p.name: sha(p.read_bytes())
                                                            for p in sorted(E0.iterdir()) if p.is_file()}},
            "prompt_r2b.py_sha256": sha(Path(P.__file__).read_bytes()),
            "l0_sellos.py_sha256": sha(Path(__file__).read_bytes())},
    }
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "sellos_l0.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"N": N, "N1": n1, "N2": n2, "W1": out["poblacion"]["W1"], "W2": out["poblacion"]["W2"],
                      "por_estado": out["poblacion"]["por_estado"], "sha256_lista": out["poblacion"]["sha256_lista"],
                      "hora": hora, "sha256_muestra": out["sorteo"]["sha256_muestra"],
                      "muestra_en_t4": todas_t4}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
