"""U-ESTUDIO-MATRIZ, paso 1 — control de reproducción (solo lectura, sin API).

(a) Re-valida cada registro de extracciones_e1.jsonl (10 TOs) desde su crudo
    con la matriz congelada SIN ampliar y compara con la validación persistida.
(b) Los rechazos firma_invalida re-obtenidos deben ser los 982 de
    p4_filas.json (misma clave to/chunk_id/idx y mismo par).
(c) Ubica en la caché de reintentos (immutable=1) el crudo que produjo la
    validación final de cada unidad aceptado_tras_reintento y lo verifica
    re-validándolo: debe reproducir validacion de extracciones_finales.
(d) Unidades de cola: la validación que ensambla r1 es la de E1
    (last-wins en extracciones_e1_compact.jsonl, r1_cola_flaggeada).
Salida: uestmat_paso1_control.json (+ uestmat_poblacion_final.json con el
origen del crudo de cada unidad).
"""
from __future__ import annotations

import collections
import json
import time
from pathlib import Path

import uestmat_comun as U

OUT = Path("/tmp/u_estudio_matriz")


def main() -> None:
    t0 = time.time()
    perfil = U.perfil_v3()
    esq = perfil.esquema
    chunks = {to: {c["id"]: c for c in U.cargar_chunks(to)} for to in U.TOS_10}

    # (a)+(b) población E1 primera pasada
    ctrl = collections.Counter()
    rech = []
    for to in U.TOS_10:
        for nl, d in enumerate(U.leer_jsonl(U.SALIDA / to / "extracciones_e1.jsonl"), 1):
            ctrl["registros"] += 1
            crudo = d.get("tool_input_crudo")
            if crudo is None:
                ctrl["sin_crudo"] += 1
                ctrl["sin_crudo_con_error"] += bool(d.get("error"))
                ctrl["sin_crudo_sin_validacion"] += d.get("validacion") is None
                continue
            val = U.validador_e1.validar_salida(crudo, chunks[to][d["chunk_id"]], esquema=esq).as_dict()
            ctrl["revalidacion_igual_persistida"] += val == d.get("validacion")
            for r in val["rechazos"]:
                if r["motivo"] == "firma_invalida":
                    i = int(r["detalle"].split("]")[0].split("[")[1])
                    par = r["detalle"].split(": ", 1)[1]
                    rech.append((to, d["chunk_id"], i, par, nl))
    p4 = json.loads((U.AUDIT / "p4_filas.json").read_text(encoding="utf-8"))
    k_p4 = sorted((x["to"], x["chunk_id"], x["idx"],
                   f"{x['origen']} --{x['predicado']}--> {x['destino']}", x["linea"]) for x in p4)
    ctrl["rechazos_firma_invalida_recomputados"] = len(rech)
    ctrl["rechazos_p4"] = len(p4)
    ctrl["rechazos_iguales_a_p4"] = int(sorted(rech) == k_p4)

    # (c)+(d) población final (lo que ensambla r1)
    filas = U.filas_reintentos()
    ctrl["filas_cache_reintentos_ns"] = len(filas)
    poblacion = {}
    for to in U.TOS_10:
        fin = {d["chunk_id"]: d for d in U.leer_jsonl(U.SALIDA / to / f"extracciones_finales_{to}.jsonl")}
        e1_lw = {}
        for d in U.leer_jsonl(U.SALIDA / to / "extracciones_e1.jsonl"):
            e1_lw[d["chunk_id"]] = d
        comp_lw = {}
        for d in U.leer_jsonl(U.SALIDA / to / "extracciones_e1_compact.jsonl"):
            comp_lw[d["chunk_id"]] = d
        for cid, f in fin.items():
            est = f.get("estado_e3")
            ch = chunks[to][cid]
            ent = {"to": to, "chunk_id": cid, "estado_e3": est}
            if f.get("validacion") is None:
                # cola humana: r1 inyecta la validación E1 last-wins del compact
                base = comp_lw.get(cid)
                ent["fuente_crudo"] = "e1_compact_last_wins"
                crudo = (base or {}).get("tool_input_crudo")
                objetivo = (base or {}).get("validacion")
                ctrl["cola_compact_igual_e1_last_wins"] += (base == e1_lw.get(cid))
            elif est == "aceptado_tras_reintento":
                pref = perfil.build_user_message(ch) + "\n\n" + U.MARCA_REINTENTO
                cands = [x for x in filas if isinstance(x["mensaje"], str) and x["mensaje"].startswith(pref)]
                objetivo = f["validacion"]
                ok = [x for x in cands if x["tool_input"] is not None and
                      U.validador_e1.validar_salida(x["tool_input"], ch, esquema=esq).as_dict() == objetivo]
                ent["fuente_crudo"] = "cache_reintentos"
                ent["candidatos_cache"] = len(cands)
                ent["candidatos_que_reproducen"] = len(ok)
                ent["cache_keys"] = [x["key"] for x in ok]
                crudo = ok[0]["tool_input"] if ok else None
                if ok and len({json.dumps(x["tool_input"], sort_keys=True) for x in ok}) > 1:
                    ent["crudos_distintos_que_reproducen"] = True
            else:
                ent["fuente_crudo"] = "e1_last_wins"
                crudo = e1_lw[cid].get("tool_input_crudo")
                objetivo = f["validacion"]
            if crudo is None:
                ent["crudo_encontrado"] = False
                ent["reproduce"] = False
            else:
                ent["crudo_encontrado"] = True
                ent["reproduce"] = (U.validador_e1.validar_salida(crudo, ch, esquema=esq).as_dict() == objetivo)
            ctrl[f"final_{ent['fuente_crudo']}"] += 1
            ctrl[f"final_{ent['fuente_crudo']}_reproduce"] += ent["reproduce"]
            poblacion[f"{to}|{cid}"] = ent
    ctrl["segundos"] = round(time.time() - t0, 1)
    (OUT / "uestmat_paso1_control.json").write_text(
        json.dumps(dict(ctrl), ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "uestmat_poblacion_final.json").write_text(
        json.dumps(poblacion, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(dict(ctrl), ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
