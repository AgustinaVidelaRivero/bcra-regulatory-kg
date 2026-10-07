"""U-E3-LISTAS, D3 (enmienda 1 al mandato): conteo por código de los ítems que repiten la norma de su encabezado.
DISEÑADO EN O2, SE CORRE EN O3 (no se corrió sobre la población). Sin API.

Criterio, fijado antes de correr:
  - Universo: las unidades de la lista sellada de O1 (`UE3_LISTAS_O1_lista_unidades_afectadas_tanda0.json`, 20), en dos
    extracciones de la tanda 0 r2b: la que vio E3 en la verificación del intento 0 (`extracciones_e1.jsonl`, la
    validación) y la final (`extracciones_finales_r2_<to>.jsonl`).
  - Encabezado de un ítem (H): el texto de los bloques que abren su lista (`comun_e3.indices_bloque_lista`, con D2) y,
    si el bloque inmediatamente anterior a ellos es el `encabezado` de la misma unidad de origen, también ese (la línea
    de título que la frase continúa; R30: «puede abarcar bloques heredados seguidos, como una línea de título y el
    párrafo que la continúa»).
  - Una entidad del ítem REPITE LA NORMA DEL ENCABEZADO si es una norma (Obligacion, Restriccion o Potestad) y su
    `label` o su `descripcion` comparte con H al menos una ventana de 5 tokens normalizados (`validador_r2.norm_tokens`,
    la normalización de `ratchet_e3.copias_nota`), y ninguna con el texto propio del ítem. Es la norma del encabezado
    emitida como entidad aparte (P3C-d1, P3C-d2): una norma compuesta del ítem comparte ventanas con H y también con el
    texto propio, y no cuenta.
  - Se cuenta por unidad y por extracción: cuántas entidades repiten la norma, cuáles (local_id, tipo y label).
Es una medida, no una adjudicación: un conteo por solapamiento de texto (D3, «como medida»).

Uso:
  python ue3_o3_d3_repite_norma.py --selftest <copia>          (casos sintéticos; no lee la tanda 0)
  python ue3_o3_d3_repite_norma.py <copia> <lista_sellada.json> <salida.json>   (O3)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

VENTANA = 5
TIPOS_NORMA = ("Obligacion", "Restriccion", "Potestad")


def preparar(copia: Path):
    rex = copia / "data" / "experiment" / "reextraccion_v2"
    sys.path.insert(0, str(rex / "e3_verificador"))
    sys.path.insert(0, str(copia / "data" / "experiment" / "pyd_r2" / "code"))
    import comun_e3  # noqa: PLC0415
    import validador_r2  # noqa: PLC0415
    return rex, comun_e3, validador_r2


def ventanas(V, t: str) -> set[tuple[str, ...]]:
    toks = V.norm_tokens(t or "")
    return {tuple(toks[i:i + VENTANA]) for i in range(len(toks) - VENTANA + 1)}


def texto_encabezado(comun_e3, chunk: dict) -> str:
    her = chunk.get("herencia") or []
    idx = comun_e3.indices_bloque_lista(chunk)
    if not idx:
        return ""
    j = idx[0]
    previo = [j - 1] if j > 0 and her[j - 1]["tipo"] == "encabezado" and her[j - 1]["unidad_origen"] == her[j]["unidad_origen"] else []
    return "\n".join(her[k]["texto"] for k in previo + idx)


def repiten(V, comun_e3, chunk: dict, validacion: dict | None) -> list[dict]:
    vh = ventanas(V, texto_encabezado(comun_e3, chunk))
    vp = ventanas(V, chunk.get("texto") or "")
    out = []
    for e in (validacion or {}).get("entidades") or []:
        if e.get("type") not in TIPOS_NORMA:
            continue
        ve = ventanas(V, e.get("label") or "") | ventanas(V, (e.get("properties") or {}).get("descripcion") or "")
        if ve & vh and not ve & vp:
            out.append({"local_id": e.get("local_id"), "type": e.get("type"), "label": e.get("label")})
    return out


def selftest(copia: Path) -> int:
    _, comun_e3, V = preparar(copia)
    her = [{"tipo": "encabezado", "unidad_origen": "9.1", "texto": "9.1. Se prohíbe a las entidades financieras operar con"},
           {"tipo": "intro", "unidad_origen": "9.1", "texto": "terceros no residentes en el país, excepto en los siguientes casos:"}]
    item = {"id": "x::9.1.1", "tipo": "punto_terminal", "unidad": "9.1.1", "herencia": her,
            "texto": "9.1.1. cuando se trate de operaciones de comercio exterior debidamente documentadas."}
    repetida = {"local_id": "e1", "type": "Restriccion", "label": "Prohibición de operar con no residentes",
                "properties": {"descripcion": "Se prohíbe a las entidades financieras operar con terceros no residentes en el país."}}
    compuesta = {"local_id": "e2", "type": "Restriccion", "label": "Prohibición salvo comercio exterior",
                 "properties": {"descripcion": "Se prohíbe a las entidades financieras operar con terceros no residentes, "
                                               "salvo cuando se trate de operaciones de comercio exterior debidamente documentadas."}}
    excepcion = {"local_id": "e3", "type": "Excepcion", "label": "Excepción comercio exterior",
                 "properties": {"descripcion": "Se prohíbe a las entidades financieras operar con terceros no residentes en el país."}}
    casos = [("la norma del encabezado aparte cuenta", [repetida], ["e1"]),
             ("la norma compuesta (con el texto del ítem) no cuenta", [compuesta], []),
             ("una Excepcion no es una norma de las que cuentan", [excepcion], []),
             ("sin entidades, nada", [], [])]
    ok = 0
    for desc, ents, esperado in casos:
        r = [x["local_id"] for x in repiten(V, comun_e3, item, {"entidades": ents})]
        bien = r == esperado
        ok += bien
        print(("  ok  " if bien else " FAIL ") + desc, r)
    mini = dict(item, tipo="mini_chunk", rol_bloque="intro")
    bien = repiten(V, comun_e3, mini, {"entidades": [repetida]}) == []
    ok += bien
    print(("  ok  " if bien else " FAIL ") + "un mini-chunk no tiene encabezado de lista: nada")
    print(f"SELFTEST D3: {ok}/{len(casos) + 1}")
    return 0 if ok == len(casos) + 1 else 1


def correr(copia: Path, lista: Path, salida: Path) -> int:
    rex, comun_e3, V = preparar(copia)
    unidades = [u["chunk_id"] for u in json.loads(lista.read_text(encoding="utf-8"))["unidades"]]
    sr, e0 = rex / "corpus_tanda0" / "salida_r2b", rex / "e0_chunking" / "salida_tanda0_r2b"
    jl = lambda p: [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []  # noqa: E731
    res = {"criterio": __doc__.split("Criterio, fijado antes de correr:")[1].split("Uso:")[0].strip(), "unidades": {}}
    for cid in unidades:
        to = cid.split("::")[0]
        ch = {c["id"]: c for c in json.loads((e0 / f"chunks_{to}.json").read_text(encoding="utf-8"))}[cid]
        v0 = {r["chunk_id"]: r for r in jl(sr / to / "extracciones_e1.jsonl")}.get(cid, {}).get("validacion")
        vf = {r["chunk_id"]: r for r in jl(sr / to / f"extracciones_finales_r2_{to}.jsonl")}.get(cid, {}).get("validacion")
        res["unidades"][cid] = {"intento_0": repiten(V, comun_e3, ch, v0), "final": repiten(V, comun_e3, ch, vf)}
    res["resumen"] = {k: sum(1 for u in res["unidades"].values() if u[k]) for k in ("intento_0", "final")}
    salida.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res["resumen"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    if sys.argv[1] == "--selftest":
        raise SystemExit(selftest(Path(sys.argv[2]).resolve()))
    raise SystemExit(correr(*(Path(x).resolve() for x in sys.argv[1:4])))
