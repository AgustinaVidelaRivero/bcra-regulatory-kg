"""
identificar_error_ri_transpa.py — B6.1, tanda final, T2: la identificación del error definitivo de ri_transpa que hizo frenar el
control entre tramos (FRENO T2 parcial 1, sección 4). USD 0, sin API. Solo lee; escribe --out.

Lee solo los archivos de ri_transpa de la salida del runner (`corpus_tanda_final/salida_r2b/ri_transpa/`):
  - `extracciones_e1.jsonl`: recorre los renglones para encontrar la unidad cuyo último registro trae un error definitivo (no la
    partición por corte), con la regla de `resumen_t2.py`, y de ella sola guarda campos sin contenido: su id, su tipo, el error, el
    `stop_reason`, los tokens de cada intento, si hubo reintento por corte, tercer escalón o reintento por forma, y el informe de
    partición si lo hay. No guarda `tool_input_crudo`, `validacion`, `titulo` ni la salida de ningún intento;
  - `finales.jsonl`: solo si el id de esa unidad está (si estuviera, el error sería de E3). No lee ningún estado;
  - `particiones_por_corte.json`, si existe: solo si esa unidad está.
De la E0 de la tanda final (no de la salida) toma sus caracteres, y con el código de E0 (`correr_e0.particionar_por_corte` y
`runner_corpus.corresponde_escalon_3`) dice si se puede partir. El max_tokens del primer intento sale del perfil r2b.
Si el error fuera de E3, escribe solo el id y la fase; el detalle iría a un NO_ABRIR_ (no es el caso si la unidad no está en
finales.jsonl).
Uso: <repo>/.venv/bin/python -B identificar_error_ri_transpa.py --repo <raíz> --out <json>
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
TO = "ri_transpa"
SALIDA_REL = "data/experiment/reextraccion_v2/corpus_tanda_final/salida_r2b"
E0_REL = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b"
PARTICIONADA = "particionada_por_corte"


def tokens(u: dict | None) -> dict | None:
    return None if u is None else {k: u.get(k) for k in ("input_tokens", "output_tokens")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    r = a.repo.resolve()
    tdir = r / SALIDA_REL / TO
    # 1. la unidad con error: el último registro de E1 por unidad (last wins), con la regla de resumen_t2.py
    renglones: dict[str, list[dict]] = {}
    for x in (tdir / "extracciones_e1.jsonl").read_text(encoding="utf-8").splitlines():
        if x.strip():
            reg = json.loads(x)
            renglones.setdefault(reg["chunk_id"], []).append(reg)
    ultimos = {cid: regs[-1] for cid, regs in renglones.items()}
    en_finales = set()
    for x in (tdir / "finales.jsonl").read_text(encoding="utf-8").splitlines():
        if x.strip():
            en_finales.add(json.loads(x)["chunk_id"])          # solo el id: ningún estado
    con_error = sorted(cid for cid, reg in ultimos.items() if reg.get("error") not in (None, PARTICIONADA) and cid not in en_finales)
    if len(con_error) != 1:
        raise SystemExit(f"se esperaba una unidad con error, hay {len(con_error)}")
    cid = con_error[0]
    regs = renglones[cid]
    reg = regs[-1]
    fase = "E3" if cid in en_finales else "E1"
    res: dict = {"to": TO, "unidad": cid, "fase": fase}
    if fase == "E3":
        res["nota"] = "el detalle va a un NO_ABRIR_"
        a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(json.dumps(res, ensure_ascii=False))
        return 0

    # 2. el código de E0 y del runner, de la copia de trabajo que es el repo (solo lectura)
    for sub in ("e0_chunking", "e1_extractor", "corpus_v2"):
        sys.path.insert(0, str(r / "data/experiment/reextraccion_v2" / sub))
    import correr_e0                                         # noqa: PLC0415
    import cliente_e1                                        # noqa: PLC0415
    import perfil_e1                                         # noqa: PLC0415
    chunks = {c["id"]: c for c in json.loads((r / E0_REL / f"chunks_{TO}.json").read_text(encoding="utf-8"))}
    c = chunks[cid]
    partes, informe = correr_e0.particionar_por_corte(c)
    primer_max = perfil_e1.perfil("r2b").build_request_kwargs(c, model="claude-haiku-4-5")["max_tokens"]

    intentos = [{"intento": 1, "max_tokens": primer_max}]
    if "reintento_corte" in reg:
        i1 = reg["reintento_corte"]["intento_1"]
        intentos[0].update({"stop_reason": i1.get("stop_reason"), **(tokens(i1.get("usage")) or {})})
        intentos.append({"intento": 2, "max_tokens": reg["reintento_corte"]["max_tokens_reintento"]})
    if "escalon_3" in reg:
        i2 = reg["escalon_3"]["intento_2"]
        intentos[-1].update({"stop_reason": i2.get("stop_reason"), **(tokens(i2.get("usage")) or {})})
        intentos.append({"intento": 3, "max_tokens": reg["escalon_3"]["max_tokens"]})
    if not reg.get("reintento_forma"):
        intentos[-1].update({"stop_reason": reg.get("stop_reason"), **(tokens(reg.get("usage")) or {})})
    forma = reg.get("reintento_forma")
    if forma:
        # el primer intento (el que salió mal formado) está en reintento_forma.intento_1; el primer reintento por forma, en
        # reintento_2.intento_2; el registro lleva el stop_reason y los tokens del último. De cada uno, solo stop_reason y tokens.
        i1f = forma.get("intento_1") or {}
        intentos[-1].update({"stop_reason": i1f.get("stop_reason"), **(tokens(i1f.get("usage")) or {}),
                             "salida": f"mal formada ({forma.get('motivo')})"})
        kw_forma = intentos[-1]["max_tokens"]
        r2 = forma.get("reintento_2")
        if r2:
            i2f = r2.get("intento_2") or {}
            intentos.append({"intento": "reintento por forma 1 (-rforma1, temperatura 1)", "max_tokens": kw_forma,
                             "stop_reason": i2f.get("stop_reason"), **(tokens(i2f.get("usage")) or {}),
                             "motivo_del_segundo": r2.get("motivo")})
            intentos.append({"intento": "reintento por forma 2 (-rforma2, temperatura 1)", "max_tokens": kw_forma,
                             "stop_reason": reg.get("stop_reason"), **(tokens(reg.get("usage")) or {})})
        else:
            intentos.append({"intento": "reintento por forma 1 (-rforma1, temperatura 1)", "max_tokens": kw_forma,
                             "stop_reason": reg.get("stop_reason"), **(tokens(reg.get("usage")) or {})})
    part_json = tdir / "particiones_por_corte.json"
    en_particiones = cid in json.loads(part_json.read_text(encoding="utf-8")) if part_json.exists() else False
    res.update({
        "tipo_unidad": reg.get("tipo_unidad"),
        "error": reg.get("error"),
        "stop_reason_del_ultimo_intento": reg.get("stop_reason"),
        "max_tokens_del_ultimo_intento": intentos[-1]["max_tokens"],
        "tokens_de_salida_del_ultimo_intento": (tokens(reg.get("usage")) or {}).get("output_tokens"),
        "intentos_de_e1": len(intentos),
        "intentos": intentos,
        "renglones_de_la_unidad_en_extracciones_e1": len(regs),
        "reintento_por_corte": "reintento_corte" in reg,
        "tercer_escalon": "escalon_3" in reg,
        "el_runner_intento_partirla": {
            "informe_de_particion_en_el_registro": "particion_por_corte" in reg,
            "en_particiones_por_corte_json": en_particiones,
            "particionar_por_corte_hoy": {"se_parte": partes is not None, **{k: v for k, v in informe.items() if k != "id"}},
            "corresponde_tercer_escalon": partes is None,
            "lectura": ("no: particionar_por_corte no la parte, así que el reintento que corta va al tercer escalón "
                        "(runner_corpus.corresponde_escalon_3)") if partes is None else
                       "sí se puede partir: el reintento que corta la parte por corte"},
        "caracteres": {"chars_propio": c["chars_propio"], "chars_completo": c["chars_completo"], "tipo_e0": c["tipo"]},
        "tokens_de_salida_por_caracter_propio_minimo_del_ultimo": (round(intentos[-1]["max_tokens"] / c["chars_propio"], 4)
                                                                  if reg.get("stop_reason") == "max_tokens" else None),
        "el_camino": ("el primer intento no corta y sale mal formado; los reintentos por forma van con su mismo max_tokens "
                      "(runner_corpus.py: kwargs_reintento_forma sobre kwargs, sin techo de corte porque no hubo corte) y, si "
                      "cortan, la unidad queda con salida_mal_formada_tras_reintento: el reintento por forma no escala el "
                      "max_tokens ni parte la unidad") if forma and "reintento_corte" not in reg else None,
        "max_tokens_constantes": {"reintento_por_corte": cliente_e1.MAX_TOKENS_REINTENTO_CORTE_R2,
                                  "tercer_escalon": cliente_e1.MAX_TOKENS_ESCALON_3_R2},
    })
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
