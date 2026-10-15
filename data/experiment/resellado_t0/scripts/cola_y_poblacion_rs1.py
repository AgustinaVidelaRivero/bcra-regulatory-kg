"""Re-sellado único de la tanda 0, §2.4 y §4 (enmienda 7, §1.5): la cola de la tanda 0 antes (74) y después de R0, con la
lista de las unidades que salen o entran y el estado final de cada una; la cifra que dan los grafos nuevos (las unidades
que el ensamblado sin la cola descarta y las que llevan la marca de la cola en el completo); la población de
U-LECTURA-ACEPTADAS y las dos cifras de la línea de base del pre-registro de la tanda 1. USD 0, solo lee.

Usa las mismas funciones que R0 (`ultimas` y `cifras` de r0/controles/r0_f2_cifras_enmienda7.py, importadas sin
editarlas). «Antes» es finales.jsonl en 1d690df3 (antes del anexo de R0; git show sobre el repo, solo lectura); «después»,
el de la raíz dada.
Uso: python -I -B cola_y_poblacion_rs1.py <raiz de la copia> <repo para git show> <salida.json>
"""
import importlib.util
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, REPO, SAL = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3])
REX = RAIZ / "data/experiment/reextraccion_v2"
spec = importlib.util.spec_from_file_location("r0c", REX / "r0/controles/r0_f2_cifras_enmienda7.py")
r0c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r0c)
assert Path(r0c.REX).resolve() == REX.resolve(), "el módulo de R0 no es el de la copia"
T0 = REX / "corpus_tanda0"
ENS = {"diez": T0 / "ens_diez_r2b_rs1", "diez_sin_cola": T0 / "ens_diez_r2b_sincola_rs1",
       "desarrollo": T0 / "ens_desarrollo_r2b_rs1", "desarrollo_sin_cola": T0 / "ens_desarrollo_r2b_sincola_rs1"}
SELLADOS = {"diez": T0 / "ens_diez_r2b", "diez_sin_cola": T0 / "ens_diez_r2b_sincola",
            "desarrollo": T0 / "ens_desarrollo_r2b", "desarrollo_sin_cola": T0 / "ens_desarrollo_r2b_sincola"}


def show(c: str, p: Path) -> str:
    return subprocess.run(["git", "-C", str(REPO), "show", f"{c}:{p.relative_to(RAIZ).as_posix()}"],
                          capture_output=True, check=True, text=True).stdout


def marca(x: dict) -> bool:
    return (x.get("properties") or {}).get("cola_humana") == "true"


def chunks_de(x: dict) -> set:
    return {p.get("chunk_id") for p in [x.get("provenance")] + (x.get("provenances") or []) if p and p.get("chunk_id")}


def en_grafo(d: Path, tos: list, cola: set) -> dict:
    rep = json.loads((d / "r2" / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
    kg = json.loads((d / "r2" / "kg.json").read_text(encoding="utf-8"))
    marcados = [n for n in kg["nodes"] if marca(n)]
    aristas_marca = sum(1 for e in kg["edges"] if marca(e))
    unidades_con_marca = sorted({c for n in marcados for c in chunks_de(n)
                                 if c in cola or c.split("::parte")[0] in cola})
    descartadas = rep.get("cola_descartada_por_to") or {}
    lista_desc = sorted(c for v in descartadas.values() for c in v["chunks"])
    assert all(v["n"] == len(v["chunks"]) for v in descartadas.values())
    n_desc = len(lista_desc)
    cola_tos = sorted(c for c in cola if c.split("::")[0] in tos)
    return {"con_cola": rep.get("con_cola"), "cola_descartada_por_to": {k: v["n"] for k, v in descartadas.items()},
            "n_descartadas": n_desc, "descartadas_igual_a_la_cola_de_sus_tos": (lista_desc == sorted(
                c for c in cola if c.split("::")[0] in tos)) if rep.get("con_cola") is False else None,
            "cola_de_sus_tos_en_finales": len(cola_tos), "nodos_con_marca": len(marcados),
            "aristas_con_marca": aristas_marca, "unidades_de_la_cola_con_nodos_marcados": len(unidades_con_marca)}


def main() -> int:
    chunks = {c["id"]: c for to in r0c.TOS
              for c in json.loads((REX / f"e0_chunking/salida_tanda0_r2b/chunks_{to}.json").read_text(encoding="utf-8"))}
    antes, ahora = {}, {}
    for to in r0c.TOS:
        p = T0 / "salida_r2b" / to / "finales.jsonl"
        antes.update(r0c.ultimas(show("1d690df3", p)))
        ahora.update(r0c.ultimas(p.read_text(encoding="utf-8")))
    es_cola = lambda r: str(r["estado"]).startswith("cola_humana")  # noqa: E731
    cola_antes = {c for c, r in antes.items() if es_cola(r)}
    cola_ahora = {c for c, r in ahora.items() if es_cola(r)}
    res = {
        "e0_unidades": len(chunks), "unidades_en_finales": [len(antes), len(ahora)],
        "unidades_en_finales_que_no_son_unidades_de_la_e0": sorted(c for c in ahora if c not in chunks),
        "antes_1d690df3": r0c.cifras(antes, chunks), "despues": r0c.cifras(ahora, chunks),
        "salen_de_la_cola": {c: [antes[c]["estado"], ahora[c]["estado"]] for c in sorted(cola_antes - cola_ahora)},
        "entran_a_la_cola": {c: [antes[c]["estado"], ahora[c]["estado"]] for c in sorted(cola_ahora - cola_antes)},
        "cola_despues_por_estado": dict(sorted(Counter(ahora[c]["estado"] for c in cola_ahora).items())),
        "cola_despues_por_to": dict(sorted(Counter(c.split("::")[0] for c in cola_ahora).items())),
        "grafos_nuevos": {}, "grafos_sellados": {},
    }
    for g, d in ENS.items():
        tos = json.loads((d / "r2" / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))["manifiesto"]["orden_corrida"]
        res["grafos_nuevos"][g] = en_grafo(d, tos, cola_ahora)
        res["grafos_sellados"][g] = en_grafo(SELLADOS[g], tos, cola_antes)
    d = res["despues"]
    res["linea_de_base_pre_registro_tanda1"] = {
        "r2b_medida": f"{len(cola_antes)} de {len(chunks)}",
        "grafo_re_sellado": f"{res['grafos_nuevos']['diez_sin_cola']['n_descartadas']} de {len(chunks)}",
        "nota": "la cifra del re-sellado es la de unidades que el ensamblado sin la cola de diez descarta"}
    SAL.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in res.items() if k not in ("antes_1d690df3",)}, ensure_ascii=False, indent=1)[:6000])
    print("poblacion L2 despues:", d["poblacion_l2"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
