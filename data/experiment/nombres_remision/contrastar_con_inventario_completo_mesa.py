"""Mesa, §131: contrasta cada resolución de la regla (g) en un corpus con la que daría la misma mención si la tabla de nombres tuviera
los 157 TOs del inventario (la referencia). USD 0. Corre sobre una COPIA del repo e importa el detector sellado sin cambiarlo.

Por qué: el ensamblado arma la tabla solo con los TOs de su manifiesto. Una cita a un TO que no está en el corpus puede resolverse
entonces a otro TO del corpus cuyo nombre empieza igual (vía «prefijo» o «comienzo»). Con los 157, el que gana es el de verdad. Una
resolución del corpus que no coincide con la referencia es sospechosa.

Uso: python3 -I -B contrastar_con_inventario_completo_mesa.py <copia> <medición.json> <regla de la referencia.py> <out.json>
     --e0-152 <dir>
<medición.json> es una salida de medir_nombres_remision_mesa.py: para cada corpus y juego, las menciones con su clave.
La referencia lee el mismo texto, con la tabla de los 157 y los nombres de <regla de la referencia>.
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

COPIA, MED, REGLA_REF, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
E0_152 = Path(sys.argv[sys.argv.index("--e0-152") + 1]).resolve()
sys.dont_write_bytecode = True
assert (Path.home() / "INGENIERIA IA/TESIS/bcra-regulatory-kg").resolve() != COPIA, "nunca sobre el repo"
sys.path.insert(0, str(COPIA / "data/experiment/reextraccion_v2/corpus_v2"))
import r1_referencias as REF  # noqa: E402

spec = importlib.util.spec_from_file_location("regla_ref", REGLA_REF)
regla = importlib.util.module_from_spec(spec)
spec.loader.exec_module(regla)
oficial = {r["id"]: r["titulo_oficial"] for r in csv.DictReader(REF.INVENTARIO_TITULOS.open(encoding="utf-8"))}
for x in json.loads(REF.INVENTARIO_RESUMEN.read_text(encoding="utf-8"))["subset_excluido"]:
    oficial[x["id_interno"]] = x["titulo"]
TODOS = sorted(oficial)
REF.TITULOS_TOS = REF.titulos_de_inventario(TODOS, {t: regla.nombres(oficial[t]) for t in TODOS})
E0 = COPIA / "data/experiment/reextraccion_v2/e0_chunking"
med = json.loads(MED.read_text(encoding="utf-8"))


def e0_de(corpus: dict, to: str) -> Path:
    for x in corpus["e0"]:
        if x.startswith("salida_") and (E0 / x / f"chunks_{to}.json").exists():
            return E0 / x
    return E0_152


def tramos(chunk: dict) -> list[tuple[str, str]]:
    out = [(f"heredado|{h['unidad_origen']}|{hashlib.sha256(h['texto'].encode()).hexdigest()[:16]}", h["texto"])
           for h in chunk.get("herencia", [])]
    out.append((f"propio|{chunk['id']}", chunk.get("texto") or ""))
    return out


out = {}
for cn, cv in med["corpus"].items():
    ref, vistos = {}, set()
    for to in cv["tos"]:
        for ch in json.loads((e0_de(cv, to) / f"chunks_{to}.json").read_text(encoding="utf-8")):
            previas: list[str | None] = []
            for clave, texto in tramos(ch):
                t_norm, _ = REF.normalizar_e0(texto, tolerar_linea_suelta="a" in REF.REGLAS_R2)
                ms = REF.detectar_menciones_r2(t_norm, to, REF.REGLAS_R2, normas_previas=previas)
                previas = previas + [m["to_destino"] for m in ms if m["clase"] == "externa"]
                if clave in vistos:
                    continue
                vistos.add(clave)
                for i, m in enumerate(ms):
                    if m["clase"] in ("externa", "externa_anaforica"):
                        ref[f"{to}|{clave}|{i}"] = m["to_destino"]
    tos = set(cv["tos"])
    out[cn] = {}
    for j, jv in cv["juegos"].items():
        ms = jv["menciones"]
        res = {k: m for k, m in ms.items() if m["to_destino"]}
        coincide = [k for k, m in res.items() if ref.get(k) == m["to_destino"]]
        distinta = [k for k, m in res.items() if ref.get(k) != m["to_destino"]]
        perdidas = [k for k, m in ms.items() if not m["to_destino"] and ref.get(k) in tos]
        out[cn][j] = {"resueltas": len(res), "coinciden_con_la_referencia": len(coincide),
                      "distintas_de_la_referencia": [{"to_origen": ms[k]["to_origen"], "norma": ms[k]["norma"][:120],
                                                      "destino": ms[k]["to_destino"], "via": ms[k]["via"],
                                                      "referencia": ref.get(k)} for k in distinta],
                      "sin_resolver_con_referencia_en_el_corpus": len(perdidas)}
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for cn, v in out.items():
    print(cn, " | ".join(f"{j}: {x['resueltas']} resueltas, {len(x['distintas_de_la_referencia'])} distintas, "
                         f"{x['sin_resolver_con_referencia_en_el_corpus']} perdidas" for j, x in v.items()))
