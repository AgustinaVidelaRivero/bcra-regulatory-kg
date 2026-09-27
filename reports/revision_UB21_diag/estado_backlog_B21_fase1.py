#!/usr/bin/env python3
"""estado_backlog_B21_fase1.py — U-B2.1 fase 1 (re-diagnóstico), pieza d.

Reconstruye el ESTADO EFECTIVO de cada id de data/backlog/backlog.jsonl.

Regla (mandato docs/mandatos/UB21_fase1_rediagnostico.md, decisión 2.i): el
archivo es un registro de eventos; una entrada tiene varias líneas y solo
algunas traen el campo `estado` (la entrada inicial y los eventos
`cambio_estado`); el estado efectivo de un id es el de su ÚLTIMA línea (en
orden de archivo) que trae el campo `estado`.

Solo lectura. Imprime por stdout. Corre desde la raíz del repo:
    PYTHONDONTWRITEBYTECODE=1 python3 reports/revision_UB21_diag/estado_backlog_B21_fase1.py
"""
import sys
sys.dont_write_bytecode = True

import hashlib
import json
from collections import Counter, OrderedDict
from pathlib import Path

RUTA = Path("data/backlog/backlog.jsonl")
SHA_ESPERADO = "d8473501b442432ec7b2f698cbb4d2d618e3db1f0947698407b311ac1a07e2a4"
CERRADOS = ("aplicado", "verificado")


def main() -> int:
    raw = RUTA.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    print(f"archivo : {RUTA}")
    print(f"sha256  : {sha}")
    print(f"esperado: {SHA_ESPERADO}  -> {'OK' if sha == SHA_ESPERADO else 'DIFIERE'}")
    texto = raw.decode("utf-8")
    lineas = texto.split("\n")
    if lineas and lineas[-1] == "":
        lineas.pop()
    print(f"lineas  : {len(lineas)} (wc -l = {texto.count(chr(10))}; vacias = {sum(1 for l in lineas if not l.strip())})")

    por_id: "OrderedDict[str, dict]" = OrderedDict()
    eventos = Counter()
    for k, linea in enumerate(lineas, 1):
        if not linea.strip():
            continue
        d = json.loads(linea)
        i = d["id"]
        ev = d.get("evento") or "(entrada inicial)"
        eventos[ev] += 1
        r = por_id.setdefault(i, {"lineas": [], "con_estado": [], "ts_estado": []})
        r["lineas"].append((k, ev))
        if "estado" in d:
            r["con_estado"].append((k, d["estado"], ev))
            r["ts_estado"].append(d.get("ts"))

    print(f"ids     : {len(por_id)}")
    print(f"eventos : {dict(eventos)}")
    print(f"ids con prefijo RT-: {sum(1 for i in por_id if i.startswith('RT-'))}")
    print()
    print("id        | n_lineas | lineas_con_estado (linea:estado) | ESTADO EFECTIVO (linea)")
    print("----------|----------|----------------------------------|------------------------")
    efectivo: "OrderedDict[str, tuple]" = OrderedDict()
    orden_ts_ok = True
    for i, r in por_id.items():
        ult = r["con_estado"][-1] if r["con_estado"] else None
        efectivo[i] = (ult[1], ult[0]) if ult else ("(sin estado)", None)
        ce = " ".join(f"{k}:{e}" for k, e, _ in r["con_estado"])
        est = f"{efectivo[i][0]} ({efectivo[i][1]})" if ult else "(sin estado)"
        print(f"{i} | {len(r['lineas']):8d} | {ce:32s} | {est}")
        ts = [t for t in r["ts_estado"] if t]
        if ts != sorted(ts):
            orden_ts_ok = False
            print(f"    AVISO: ts de las lineas con estado fuera de orden para {i}: {ts}")
    print()
    print(f"orden de archivo == orden cronologico de los ts con estado: {orden_ts_ok}")
    conteo = Counter(e for e, _ in efectivo.values())
    print(f"estado efectivo por valor: {dict(conteo)}")
    cerrados = [i for i, (e, _) in efectivo.items() if e in CERRADOS]
    verificados = [i for i, (e, _) in efectivo.items() if e == "verificado"]
    aplicados = [i for i, (e, _) in efectivo.items() if e == "aplicado"]
    resto = [i for i, (e, _) in efectivo.items() if e not in CERRADOS]
    print(f"CERRADOS (aplicado o verificado): {len(cerrados)} -> {cerrados}")
    print(f"  verificado: {len(verificados)} -> {verificados}")
    print(f"  aplicado (sin verificado posterior): {len(aplicados)} -> {aplicados}")
    print(f"NO CERRADOS: {len(resto)} -> {[(i, efectivo[i][0]) for i in resto]}")
    print(f"suma: {len(cerrados)} + {len(resto)} = {len(cerrados) + len(resto)} (ids = {len(por_id)})")
    # Verificados sin evento de aplicacion (estado 'verificado' desde la entrada inicial).
    sin_aplicacion = [i for i in verificados
                      if not any(ev == "aplicacion" for _, ev in por_id[i]["lineas"])]
    print(f"verificados SIN evento 'aplicacion' (verificado = defecto confirmado, no correccion aplicada): "
          f"{len(sin_aplicacion)} -> {sin_aplicacion}")
    return 0 if sha == SHA_ESPERADO else 1


if __name__ == "__main__":
    sys.exit(main())
