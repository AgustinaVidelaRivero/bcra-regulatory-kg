"""
marco_sorteo_P.py — U-MED-UMBRALES, etapa P, tramo P-a, puntos 1, 3 y 4: controles de entrada, marco, estratos y
sorteo del piloto, sellados en el acta antes de abrir una ficha y antes del diagnóstico de la comparación no_determinada.
Nada de esto mira un campo para juzgarlo: el estrato sale de los campos guardados, con la regla del mandato.

  - Entrada: el texto firmado de la enmienda (líneas anteriores a «## Firma» del archivo de a0f9815) tiene que dar
    c77e92ad…7e01, y la semilla de P, sha256('U-MED-UMBRALES|P|<ese sha>')[:16], tiene que dar 51fbea50388e7481.
  - Marco: cada elemento de properties.umbrales del grafo sin cola de la tanda 0 (e22fae1a), con id «<nodo>#u<i>» y el
    estrato de comun_P.estrato; los recuentos tienen que dar los del mandato (si no, aborta).
  - Sorteo (§9.2, §4.3, D7 y mandato P-a, punto 4): random.Random(f"{S}:{estrato}").sample(sorted(ids), 4) por
    estrato; random.Random(f"{S}:TOs nuevos").sample(sorted(ids), 8) sobre los elementos de los cinco TOs nuevos que
    no salieron en ningún estrato; lote 1 = los dos primeros de cada estrato, en el orden de sample, y los cuatro
    primeros de los TOs nuevos; lote 2 = el resto; orden de lectura: random.Random(f"{S}:orden:lote{k}").shuffle sobre
    la lista ordenada del lote. La regla del lote 3 se escribe en el acta y no se ejecuta.

Corre desde la raíz de una COPIA del repo (preparar_espejo_P.py) y escribe solo --salida/acta_sorteo_P.json y
--salida/acta_sorteo_P.sha256.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/med_umbrales/p/code/marco_sorteo_P.py --salida DIR
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

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_P as C  # noqa: E402

N_POR_ESTRATO, N_NUEVOS = 4, 8
REGLA_LOTE3 = ("Solo si lo dispara el §9.3 de la enmienda (el lote 2 obliga a cambiar algo que el juicio usa). Por "
               "estrato: random.Random(f'{S}:{estrato}:lote3').sample(sorted(ids del estrato que no salieron en el "
               "sorteo de P), 2); si quedan menos de 2, todos los que quedan. TOs nuevos: "
               "random.Random(f'{S}:TOs nuevos:lote3').sample(sorted(ids de los cinco TOs nuevos que no salieron en "
               "ningún sorteo de P, incluidos los dos por estrato del lote 3), 4). Orden de lectura: "
               "random.Random(f'{S}:orden:lote3').shuffle sobre la lista ordenada del lote 3. Se escribe ahora, en el "
               "acta, y no se ejecuta.")


def texto_firmado() -> tuple[str, str]:
    p = C.REPO / C.ENMIENDA
    lineas = p.read_text(encoding="utf-8").split("\n")
    corte = lineas.index("## Firma")
    texto = "\n".join(lineas[:corte]) + "\n"
    return texto, C.sha(texto.encode("utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()

    # 1. Entrada
    _, s_texto = texto_firmado()
    if s_texto != C.SHA_TEXTO_FIRMADO:
        raise SystemExit(f"texto firmado con sha256 {s_texto}, no {C.SHA_TEXTO_FIRMADO}")
    semilla = hashlib.sha256(f"U-MED-UMBRALES|P|{s_texto}".encode("utf-8")).hexdigest()[:16]
    if semilla != C.SEMILLA_P:
        raise SystemExit(f"semilla de P recalculada {semilla}, no {C.SEMILLA_P}")
    S = C.SEMILLA_P
    kg, s_kg = C.cargar_kg()

    # 3. Marco y estratos
    filas = C.marco(kg)
    ids = [f[0] for f in filas]
    if len(ids) != len(set(ids)):
        raise SystemExit("ids repetidos en el marco")
    por_estrato = Counter(f[3] for f in filas)
    idx = C.indice_elementos(kg)
    con_via = sorted(e for e, (_, _, el) in idx.items() if el.get("base_via"))
    con_destino = sorted(e for e, (_, _, el) in idx.items() if el.get("base_destino"))
    nuevos = [f for f in filas if f[1] not in C.DEV]
    controles = {
        "por_estrato_igual_al_mandato": dict(por_estrato) == C.ESPERADO,
        "total": len(filas) == C.ESPERADO_TOTAL,
        "con_contenido": len(filas) - por_estrato["V-vacío"] == C.ESPERADO_CONTENIDO,
        "tos_nuevos": len(nuevos) == C.ESPERADO_NUEVOS,
        "base_via_igual_a_base_destino": con_via == con_destino and len(con_via) == C.ESPERADO_RESUELTAS,
    }
    if not all(controles.values()):
        raise SystemExit(f"el marco no da lo del mandato: {controles}; {dict(por_estrato)}")

    # 4. Sorteo
    hora = datetime.now().astimezone().isoformat(timespec="seconds")
    muestra = {}
    for e in C.ESTRATOS:
        ids_e = sorted(f[0] for f in filas if f[3] == e)
        muestra[e] = random.Random(f"{S}:{e}").sample(ids_e, N_POR_ESTRATO)
    sorteados = {x for v in muestra.values() for x in v}
    ids_nuevos = sorted(f[0] for f in nuevos if f[0] not in sorteados)
    muestra_nuevos = random.Random(f"{S}:TOs nuevos").sample(ids_nuevos, N_NUEVOS)
    lote1 = [x for e in C.ESTRATOS for x in muestra[e][:2]] + muestra_nuevos[:4]
    lote2 = [x for e in C.ESTRATOS for x in muestra[e][2:]] + muestra_nuevos[4:]
    orden = {}
    for k, lote in ((1, lote1), (2, lote2)):
        lista = sorted(lote)
        random.Random(f"{S}:orden:lote{k}").shuffle(lista)
        orden[f"lote{k}"] = lista
    todos = lote1 + lote2
    if len(todos) != 40 or len(set(todos)) != 40:
        raise SystemExit("la muestra no tiene 40 elementos distintos")
    info = {f[0]: f for f in filas}
    detalle = {e: [{"orden_sorteo": i, "id": x, "to": info[x][1], "tipo": info[x][2]}
                   for i, x in enumerate(muestra[e], 1)] for e in C.ESTRATOS}
    detalle_nuevos = [{"orden_sorteo": i, "id": x, "to": info[x][1], "tipo": info[x][2], "estrato": info[x][3]}
                      for i, x in enumerate(muestra_nuevos, 1)]

    code = Path(__file__).resolve().parent
    out = {
        "unidad": "U-MED-UMBRALES, etapa P (piloto), tramo P-a: acta del sorteo, sellada antes de abrir una ficha y "
                  "antes del diagnóstico de la comparación no_determinada",
        "aviso": "contiene el estrato de cada elemento, que sale de campos guardados (base, origen, comparación): la "
                 "autora no la abre antes de cerrar el paso 1 de cada lote",
        "enmienda": {"ruta": C.ENMIENDA, "commit_firma": C.COMMIT_FIRMA, "sha256_texto_firmado": s_texto,
                     "como": "líneas del archivo de a0f9815 anteriores a «## Firma», unidas por salto, con salto final"},
        "semilla": {"P": S, "derivacion": "sha256('U-MED-UMBRALES|P|<sha256 del texto firmado>')[:16]",
                    "recalculada_igual": True},
        "grafo": {"nombre": "KG-Tanda0-Diez-r2b-sincola", "ruta": str(C.KG.relative_to(C.REPO)), "kg_sha256": s_kg,
                  "sello": "dde9f44 / 235a295", "registro": "data/experiment/neo4j/grafos.py, KG_Tanda0_Diez_r2b_sincola",
                  "re_sellado_unico": "pendiente al sortear (docs/tablero.md:19 en HEAD 2a70b20): se usa este sello"},
        "criterio_estratos": {
            "id": "<id del nodo>#u<i>, i = índice desde 0 en properties.umbrales",
            "orden": ["validador (regla_comparacion empieza con «limite_relativo:»): V-vacío si no tiene valor ni "
                      "base y la comparación es no_determinada; V-con si tiene base; V-sin-cont si no",
                      "ensamblado: base resuelta si tiene base_via; si no, E-e1-sin, E-e1-con, E-desc-sin o E-desc-con "
                      "según el origen (e1 o descripcion) y si tiene base"],
            "etiquetas_utf8_hex": {e: e.encode("utf-8").hex() for e in C.ESTRATOS}},
        "controles": controles,
        "poblacion": {
            "N": len(filas), "por_estrato": {e: por_estrato[e] for e in C.ESTRATOS},
            "con_contenido": len(filas) - por_estrato["V-vacío"], "tos_nuevos": len(nuevos),
            "por_to": dict(sorted(Counter(f[1] for f in filas).items())),
            "base_via": len(con_via),
            "sha256_lista": C.sha(C.canon(filas)), "sha256_ids": C.sha(("\n".join(ids) + "\n").encode("utf-8")),
            "como_se_calcula_el_sha256": "sha256_lista: json.dumps(filas, ensure_ascii=False, separators=(',', ':')) "
                                         "en UTF-8, filas [id, to, tipo, estrato] ordenadas por id; sha256_ids: los "
                                         "ids ordenados, uno por línea, con salto final",
            "filas": filas},
        "sorteo": {
            "hora": hora, "python": sys.version.split()[0],
            "metodo_estrato": "random.Random(f'{S}:{estrato}').sample(sorted(ids del estrato), 4)",
            "metodo_tos_nuevos": "random.Random(f'{S}:TOs nuevos').sample(sorted(ids de los cinco TOs nuevos que no "
                                 "salieron en ningún estrato), 8)",
            "metodo_lotes": "lote 1: los dos primeros de cada estrato en el orden de sample, en el orden de los "
                            "estratos de comun_P.ESTRATOS, y los cuatro primeros de los TOs nuevos; lote 2: el resto",
            "metodo_orden": "random.Random(f'{S}:orden:lote{k}').shuffle(sorted(ids del lote k))",
            "ids_tos_nuevos_disponibles": len(ids_nuevos),
            "muestra_por_estrato": detalle, "muestra_tos_nuevos": detalle_nuevos,
            "lote1": lote1, "lote2": lote2, "orden_de_lectura": orden,
            "sha256_muestra": C.sha(C.canon({"estratos": muestra, "tos_nuevos": muestra_nuevos})),
            "sha256_orden": C.sha(C.canon(orden)),
            "como_se_calcula_el_sha256": "json.dumps({'estratos': {estrato: [ids en el orden de sample]}, "
                                         "'tos_nuevos': [...]}, ensure_ascii=False, separators=(',', ':')) en UTF-8; "
                                         "sha256_orden: json.dumps del orden de lectura de los dos lotes",
            "lote3": REGLA_LOTE3},
        "insumos": {
            "insumos_espejo_P.json_sha256": C.sha((C.REPO / "insumos_espejo_P.json").read_bytes())
            if (C.REPO / "insumos_espejo_P.json").exists() else None,
            "comun_P.py_sha256": C.sha((code / "comun_P.py").read_bytes()),
            "marco_sorteo_P.py_sha256": C.sha(Path(__file__).read_bytes())},
    }
    a.salida.mkdir(parents=True, exist_ok=True)
    p = a.salida / "acta_sorteo_P.json"
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    s_acta = C.sha(p.read_bytes())
    (a.salida / "acta_sorteo_P.sha256").write_text(f"{s_acta}  acta_sorteo_P.json\n", encoding="utf-8")
    print(json.dumps({"hora": hora, "N": len(filas), "por_estrato": out["poblacion"]["por_estrato"],
                      "sha256_lista": out["poblacion"]["sha256_lista"], "sha256_muestra": out["sorteo"]["sha256_muestra"],
                      "sha256_acta": s_acta}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
