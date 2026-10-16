"""
manifiestos_a2.py — U-ALCANCE-E1, A2 (USD 0, sin API): los manifiestos de los 152 de S1 y de S1-bis de U-SEG-OFICIAL
(y, de referencia, el de S1-ter, que cita la lista de la tanda 1) contra el registro de alcance por tanda y contra el
perfil r2b de la copia que se pasa con --raiz.

  - Documentos con alcance en el registro (filas de clase o de rol reutilizado, de todas las tablas, leídas con el
    lector de R2-2) cuyo `rol_alcance` es null en el manifiesto, con su tanda.
  - Desacuerdo con el perfil r2b de la copia: documentos cuyo `rol_alcance` no es el que da perfil_e1.perfil("r2b")
    .rol_por_to, con la regla de manifiesto_corpus._validar_roles_contra_catalogo (rol_id, o la lista de clase_ids).
  - Si el manifiesto carga con manifiesto_corpus.cargar (con validar_roles, como correr_e0) y, si no, el error.
Uso: PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B manifiestos_a2.py --raiz COPIA --etiqueta head|a2 --salida JSON
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

MANIFIESTOS = (("S1", "data/experiment/segmentacion_oficial_e0r2/s1/manifiesto/segmentacion_oficial_e0r2_152.json"),
               ("S1-bis", "data/experiment/segmentacion_oficial_e0r2/s1bis/manifiesto/segmentacion_oficial_e0r2_152.json"),
               ("S1-ter", "data/experiment/segmentacion_oficial_e0r2/s1ter/manifiesto/segmentacion_oficial_e0r2_152.json"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", type=Path, required=True)
    ap.add_argument("--etiqueta", required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    raiz = a.raiz.resolve()
    ex = raiz / "data" / "experiment"
    sys.path.insert(0, str(ex / "reresolucion_catalogo"))
    sys.path.insert(0, str(ex / "reextraccion_v2"))
    sys.path.insert(0, str(ex / "reextraccion_v2" / "e1_extractor"))
    import reresolver_catalogo as RR  # noqa: PLC0415 — el lector de R2-2 del registro
    import manifiesto_corpus  # noqa: PLC0415
    import perfil_e1  # noqa: PLC0415
    reg = RR.leer_registro_alcance(RR.REGISTRO_ALCANCE_MD)
    con_alcance = {f["archivo"]: t for t, fs in reg["tandas"].items() for f in fs if f["decision"] != "sin_alcance"}
    rpt = perfil_e1.perfil("r2b").rol_por_to

    def rol_del_perfil(archivo):
        rc = rpt.get(archivo)
        return None if rc is None else (rc.get("rol_id") or rc.get("clase_ids"))

    res = {"etiqueta": a.etiqueta, "registro_sha256": reg["fuente_sha256"],
           "documentos_con_alcance_en_el_registro": {k[:-4]: v for k, v in con_alcance.items()},
           "entradas_del_perfil_r2b": len(rpt), "manifiestos": {}}
    for nombre, rel in MANIFIESTOS:
        p = raiz / rel
        man = json.loads(p.read_text(encoding="utf-8"))
        tos = man["tos"]
        nulos = [t["id"] for t in tos if t["archivo"] in con_alcance and t["rol_alcance"] is None]
        desacuerdo = [{"to": t["id"], "manifiesto": t["rol_alcance"], "perfil": rol_del_perfil(t["archivo"])}
                      for t in tos if t["rol_alcance"] != rol_del_perfil(t["archivo"])]
        try:
            manifiesto_corpus.cargar(p)
            carga = "carga"
        except Exception as e:  # noqa: BLE001
            carga = f"{type(e).__name__}: {e}"
        res["manifiestos"][nombre] = {
            "ruta": rel, "sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "tos": len(tos),
            "con_alcance_en_el_registro_y_rol_null": {"cuantos": len(nulos), "tos": nulos,
                                                      "por_tanda": {t: sorted(x for x in nulos
                                                                              if con_alcance[f"{x}.pdf"] == t)
                                                                    for t in sorted(set(con_alcance.values()))}},
            "desacuerdo_con_el_perfil_r2b": {"cuantos": len(desacuerdo), "detalle": desacuerdo},
            "cargar_con_validar_roles": carga}
    a.salida.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for nombre, r in res["manifiestos"].items():
        print(nombre, r["sha256"][:12], "| null con alcance en el registro:", r["con_alcance_en_el_registro_y_rol_null"]["cuantos"],
              "| desacuerdo con el perfil:", r["desacuerdo_con_el_perfil_r2b"]["cuantos"],
              "| carga:", r["cargar_con_validar_roles"][:160])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
