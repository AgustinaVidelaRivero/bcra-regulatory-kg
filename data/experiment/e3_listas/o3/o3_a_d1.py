"""U-E3-LISTAS, O3 (a), sin API: qué faltantes nuevos tienen la cita verificada solo por D1 (el bloque que abre la lista
en el fuente de las citas, ratchet_e3.py:283): cita_en_fuente con el bloque y sin él, sobre el chunk de cada unidad.
Es el riesgo que declaró la enmienda 1 (una cita al encabezado se vuelve feedback del reintento).
Uso: python o3_a_d1.py <copia> <dir_o3>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

COPIA, O3 = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
rex = COPIA / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(rex / "e3_verificador"))
import comun_e3  # noqa: E402

e0 = rex / "e0_chunking" / "salida_tanda0_r2b"
out, tot = {}, {"faltantes": 0, "cita_verificada": 0, "solo_por_D1": 0, "bloqueantes_solo_por_D1": 0}
for x in (O3 / "a" / "evaluacion_e3_o3.jsonl").read_text(encoding="utf-8").splitlines():
    r = json.loads(x)
    cid = r["chunk_id"]
    ch = {c["id"]: c for c in json.loads((e0 / f"chunks_{cid.split('::')[0]}.json").read_text(encoding="utf-8"))}[cid]
    filas = []
    for k, f in enumerate(r["evaluacion"]["faltantes"]):
        cita = f.get("cita_textual_del_fuente") or ""
        con, sin = comun_e3.cita_en_fuente(cita, ch, True), comun_e3.cita_en_fuente(cita, ch, False)
        assert con == f["cita_verificada"], (cid, k)
        filas.append({"k": k, "bloqueante": f["bloqueante"], "cita_verificada": con, "sin_el_bloque": sin,
                      "solo_por_D1": con and not sin})
        tot["faltantes"] += 1
        tot["cita_verificada"] += con
        tot["solo_por_D1"] += con and not sin
        tot["bloqueantes_solo_por_D1"] += bool(con and not sin and f["bloqueante"])
    out[cid] = filas
res = {"totales": tot, "unidades_con_bloqueante_solo_por_D1": sorted(c for c, fs in out.items()
                                                                      if any(f["solo_por_D1"] and f["bloqueante"] for f in fs)),
       "detalle": out}
(O3 / "a" / "d1_citas.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: res[k] for k in ("totales", "unidades_con_bloqueante_solo_por_D1")}, ensure_ascii=False))
