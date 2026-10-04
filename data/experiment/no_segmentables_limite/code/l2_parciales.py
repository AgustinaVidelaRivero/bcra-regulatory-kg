"""U-NOSEG-LIMITE, L2 — aplica la regla de `l2_regla_parciales.md` (escrita antes) a las unidades de
los dos parciales, en la partición de B5.8.4 y en una salida de e0-r2 corrida en el scratchpad.

Solo lectura del repo, USD 0. Escribe `l2_regla_parciales.json` y `l2_parciales.md` en el directorio
de la unidad. Las entradas del scratchpad (roles por página, salida de e0-r2, comparación de R5 y
health-check) se registran con su sha256.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/no_segmentables_limite/code/l2_parciales.py \
      --roles <roles_por_pagina_todos.json> --e0r2 <dir de e0-r2> \
      --r5 <r5_comparar_3tos_atribuido.json> --hc <healthcheck_3tos.json>
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
PART = REPO / "data" / "experiment" / "segmentacion_84" / "b584_particion"
OUT = REPO / "data" / "experiment" / "no_segmentables_limite"
REGLA = OUT / "l2_regla_parciales.md"
SHA_REGLA = "14657c9411114c199748a227d865de0e5a94f75b563d7642d86bf21c4a4a5cf8"
PARCIALES = ("manual", "ri2_pm")
UMBRAL_C8 = 26182   # correr_e0.UMBRAL_CHARS_SUBCHUNK


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def cargar_chunks(p: Path) -> list[dict]:
    d = json.loads(p.read_text(encoding="utf-8"))
    return d["chunks"] if isinstance(d, dict) else d


def clasificar(to: str, chunks: list[dict], roles: list[str]) -> dict:
    ficha = {i + 1 for i, r in enumerate(roles) if r == "ficha_registro"}
    filas = []
    for c in chunks:
        a, b = min(c["paginas"]), max(c["paginas"])
        dentro = sorted(p for p in ficha if a <= p <= b)
        filas.append({"id": c["id"], "tipo": c["tipo"], "paginas_listadas": len(c["paginas"]),
                      "desde": a, "hasta": b, "fichas_dentro": len(dentro),
                      "clase": "cruza_fichas" if dentro else "por_punto",
                      "chars_propio": c["chars_propio"], "chars_completo": c["chars_completo"],
                      "_paginas": c["paginas"], "_herencia": c.get("herencia", [])})
    cruzan = {f["id"] for f in filas if f["clase"] == "cruza_fichas"}
    pags_punto = {p for f in filas if f["clase"] == "por_punto" for p in f["_paginas"]}
    for f in filas:
        her = 0
        for h in f["_herencia"]:
            origen = f"{to}::{h.get('unidad_origen')}::{h.get('tipo')}"
            if origen in cruzan or any(p not in pags_punto for p in h.get("paginas", [])):
                her += len(h.get("texto", ""))
        f["chars_herencia_que_cruza"] = her
    return {"filas": filas, "pags_punto": pags_punto,
            "pags_cruzan": {p for f in filas if f["clase"] == "cruza_fichas" for p in f["_paginas"]}}


def resumen(to: str, cl: dict) -> dict:
    fp = [f for f in cl["filas"] if f["clase"] == "por_punto"]
    fc = [f for f in cl["filas"] if f["clase"] == "cruza_fichas"]
    return {
        "por_punto": {"unidades": len(fp), "paginas_union": len(cl["pags_punto"]),
                      "paginas": sorted(cl["pags_punto"]),
                      "chars_propio": sum(f["chars_propio"] for f in fp),
                      "con_herencia_que_cruza": [{"id": f["id"], "chars": f["chars_herencia_que_cruza"]}
                                                 for f in fp if f["chars_herencia_que_cruza"]]},
        "cruzan_fichas": {"unidades": len(fc), "ids": [f["id"] for f in fc],
                          "paginas_union": len(cl["pags_cruzan"]),
                          "paginas_compartidas_con_por_punto": sorted(cl["pags_cruzan"] & cl["pags_punto"]),
                          "chars_propio": sum(f["chars_propio"] for f in fc),
                          "fichas_dentro_del_tramo": {f["id"]: f["fichas_dentro"] for f in fc}},
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--roles", required=True)
    ap.add_argument("--e0r2", required=True)
    ap.add_argument("--r5", required=True)
    ap.add_argument("--hc", required=True)
    a = ap.parse_args()
    if sha(REGLA) != SHA_REGLA:
        raise SystemExit("la regla de L2 cambió después de sellarse: no se aplica")
    roles_all = json.loads(Path(a.roles).read_text(encoding="utf-8"))
    cont = json.loads((PART / "conteos_b584.json").read_text(encoding="utf-8"))
    for t in PARCIALES:   # control previo obligatorio de la regla
        r = roles_all[t]["roles"]
        assert {x: r.count(x) for x in set(r)} == cont[t]["roles_pagina"], t
    e0 = Path(a.e0r2)
    res = {"_meta": {"unidad": "U-NOSEG-LIMITE, L2", "regla": str(REGLA.relative_to(REPO)),
                     "sha256_regla": SHA_REGLA,
                     "entradas_scratchpad": {"roles": sha(Path(a.roles)), "r5": sha(Path(a.r5)),
                                             "healthcheck": sha(Path(a.hc)),
                                             "e0r2": {p.name: sha(p) for p in sorted(e0.glob("*.json"))}}},
           "por_fuente": {}}
    tot = {}
    for fuente in ("particion", "e0r2"):
        res["por_fuente"][fuente] = {}
        t_pp = t_cf = t_pg_pp = t_pg_cf = t_ch_pp = t_ch_cf = 0
        for t in PARCIALES:
            p = (PART / t / f"chunks_{t}.json") if fuente == "particion" else (e0 / f"chunks_{t}.json")
            chunks = cargar_chunks(p)
            cl = clasificar(t, chunks, roles_all[t]["roles"])
            rs = resumen(t, cl)
            rs["unidades_total"] = len(chunks)
            rs["sobre_umbral_c8"] = [{"id": c["id"], "tipo": c["tipo"], "chars_propio": c["chars_propio"]}
                                     for c in chunks if c["chars_propio"] > UMBRAL_C8]
            rs["filas"] = [{k: v for k, v in f.items() if not k.startswith("_")} for f in cl["filas"]]
            res["por_fuente"][fuente][t] = rs
            t_pp += rs["por_punto"]["unidades"]; t_cf += rs["cruzan_fichas"]["unidades"]
            t_pg_pp += rs["por_punto"]["paginas_union"]; t_pg_cf += rs["cruzan_fichas"]["paginas_union"]
            t_ch_pp += rs["por_punto"]["chars_propio"]; t_ch_cf += rs["cruzan_fichas"]["chars_propio"]
        tot[fuente] = {"por_punto": t_pp, "cruzan": t_cf, "paginas_por_punto": t_pg_pp,
                       "paginas_cruzan": t_pg_cf, "chars_por_punto": t_ch_pp, "chars_cruzan": t_ch_cf}
    res["resumen"] = tot

    # e0-r2: ids, tablas, partición por tamaño, encabezados K, health-check y diferencias de R5
    ids_iguales = {}
    for t in PARCIALES + ("ri_spi",):
        ids_b = [c["id"] for c in cargar_chunks(PART / t / f"chunks_{t}.json")]
        ids_r = [c["id"] for c in cargar_chunks(e0 / f"chunks_{t}.json")]
        ids_iguales[t] = {"b584": len(ids_b), "e0r2": len(ids_r), "iguales": ids_b == ids_r}
    tablas = {t: json.loads((e0 / f"tablas_{t}.json").read_text(encoding="utf-8"))["conteos_e0_tablas"]
              for t in PARCIALES + ("ri_spi",)}
    enc = json.loads((e0 / "encabezados_conservados.json").read_text(encoding="utf-8"))
    hc = json.loads(Path(a.hc).read_text(encoding="utf-8"))
    r5 = json.loads(Path(a.r5).read_text(encoding="utf-8"))
    conteos = json.loads((e0 / "conteos.json").read_text(encoding="utf-8"))
    res["e0r2"] = {
        "version": json.loads((e0 / "version_e0.json").read_text(encoding="utf-8")),
        "ids_contra_particion": ids_iguales,
        "sub_chunking_json": (e0 / "sub_chunking.json").exists(),
        "ids_desambiguados_json": (e0 / "ids_desambiguados.json").exists(),
        "tablas": {t: {k: v[k] for k in ("tablas_logicas", "parseadas", "filas_total",
                                          "paginas_con_tabla_contenido")} for t, v in tablas.items()},
        "encabezados_conservados_por_k": {t: len(v) for t, v in enc.items()},
        "conteos": {t: {k: v[k] for k in ("paginas", "roles_pagina", "modo_lectura", "chunks_terminales",
                                          "mini_chunks", "chunks", "flag_contenido_tabular", "rechazos_header",
                                          "avisos", "lineas_huerfanas")} for t, v in conteos.items()},
        "healthcheck": {t: {"veredicto": v["veredicto"], "modo_lectura": v.get("modo_lectura"),
                            "cid_paginas": v["senales"]["cid"]["paginas"],
                            "cid_lineas": v["senales"]["cid"]["lineas"]} for t, v in hc.items()},
        "r5_texto_distinto_por_clase": r5["chunks_con_texto_distinto_por_clase"],
        "r5_texto_distinto_otra": r5["texto_distinto_otra"],
        "r5_por_to": r5["por_to"],
    }
    (OUT / "l2_regla_parciales.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n",
                                                 encoding="utf-8")

    L = ["# L2 — los dos parciales por la regla sellada (generado por code/l2_parciales.py)", "",
         f"Regla: `l2_regla_parciales.md` (sha256 `{SHA_REGLA[:16]}…`, escrita antes de aplicarla).", "",
         "| fuente | TO | unidades | por punto | páginas por punto | chars por punto | cruzan fichas | páginas que listan | chars que cruzan |",
         "|---|---|--:|--:|--:|--:|--:|--:|--:|"]
    for fuente, d in res["por_fuente"].items():
        for t, rs in d.items():
            L.append(f"| {fuente} | {t} | {rs['unidades_total']} | {rs['por_punto']['unidades']} | "
                     f"{rs['por_punto']['paginas_union']} | {rs['por_punto']['chars_propio']} | "
                     f"{rs['cruzan_fichas']['unidades']} | {rs['cruzan_fichas']['paginas_union']} | "
                     f"{rs['cruzan_fichas']['chars_propio']} |")
    L += ["", "Unidades que cruzan fichas: " + "; ".join(
        f"{t}: " + ", ".join(f"`{i}` ({n} fichas en el tramo)" for i, n in
                             rs["cruzan_fichas"]["fichas_dentro_del_tramo"].items())
        for t, rs in res["por_fuente"]["e0r2"].items()), "",
          "Unidades por punto con herencia que cruza fichas (e0-r2): " + "; ".join(
        f"`{x['id']}` {x['chars']}" for t, rs in res["por_fuente"]["e0r2"].items()
        for x in rs["por_punto"]["con_herencia_que_cruza"]) + ".", ""]
    (OUT / "l2_parciales.md").write_text("\n".join(L), encoding="utf-8")
    print(json.dumps({"resumen": tot, "e0r2": {k: res["e0r2"][k] for k in
                      ("ids_contra_particion", "sub_chunking_json", "tablas", "encabezados_conservados_por_k",
                       "healthcheck", "r5_texto_distinto_por_clase")}}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
