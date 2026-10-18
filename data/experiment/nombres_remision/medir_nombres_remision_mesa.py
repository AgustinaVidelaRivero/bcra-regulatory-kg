"""Mesa, §131 (16/10/2026): cómo resuelve la regla (g) del detector de remisiones del perfil r2 las menciones de norma de la E0,
según los nombres de cada TO. USD 0, sin API. Corre sobre una COPIA del repo (nunca el repo) e importa el detector sellado
(`corpus_v2/r1_referencias.py`) sin cambiarlo: solo fija `TITULOS_TOS`, como hace el ensamblado (`ensamblar_tanda0.py:596-597`).

Uso: python3 -I -B medir_nombres_remision_mesa.py <copia> <out.json> [--regla <regla_nombres_remision_mesa.py>] [--e0-152 <dir>]

Corpus (con los TOs del manifiesto de ensamblado o de extracción que los define):
  - tanda0_diez: los 10 de `tanda0_ens_diez_r2b_rs1.json`, sobre `salida_tanda0_r2b/`;
  - tanda0_desarrollo: los 5 de `tanda0_ens_desarrollo_r2b_rs1.json`, sobre `salida_tanda0_r2b/`;
  - tanda1: los 20 de `tanda1_20tos_r2b.json`, sobre `salida_tanda1_r2b/`;
  - acumulado: los 30 de los dos (los 10 de la tanda 0 y los 20 de la tanda 1), cada uno sobre su E0;
  con --e0-152 <dir> (la E0 de los 152, regenerada con el código del gate sobre una copia):
  - tanda_final: los 98 de `segmentacion_oficial_e0r2/s2/cifras/tanda_final_S2c.json` (`tanda_final.lista`), sobre esa E0;
  - acumulado_final: los 128 de las tres tandas, cada uno sobre su E0.
Juegos de nombres (`titulos_de_inventario(ids, nombres_remision)`):
  - inventario: solo el título oficial del inventario, sin `nombres_remision`;
  - a_mano: con las listas del manifiesto (las de la tanda 0, armadas a mano; las de la tanda 1 están vacías);
  - regla: con las listas que da la regla de `--regla` (función `nombres(titulo_oficial)`).
Texto: el de cada chunk, por tramos, con el bucle de `menciones_por_tramo` (`r1_referencias.py:933-950`): cada bloque heredado y el
texto propio, con los antecedentes de la anáfora de un tramo al siguiente.
Los bloques heredados se cuentan una vez por bloque distinto (unidad de origen y texto).
Por mención de norma (clase `externa` o `externa_anaforica`): el TO de destino y la vía de la regla (g).
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

COPIA, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
REGLA = Path(sys.argv[sys.argv.index("--regla") + 1]) if "--regla" in sys.argv else None
E0_152 = Path(sys.argv[sys.argv.index("--e0-152") + 1]).resolve() if "--e0-152" in sys.argv else None
sys.dont_write_bytecode = True
assert not (Path.home() / "INGENIERIA IA/TESIS/bcra-regulatory-kg").resolve() == COPIA, "nunca sobre el repo"
sys.path.insert(0, str(COPIA / "data/experiment/reextraccion_v2/corpus_v2"))
import r1_referencias as REF  # noqa: E402

MAN = COPIA / "data/experiment/reextraccion_v2/manifiestos"
E0 = COPIA / "data/experiment/reextraccion_v2/e0_chunking"
CORPUS = {"tanda0_diez": ("tanda0_ens_diez_r2b_rs1.json", "salida_tanda0_r2b"),
          "tanda0_desarrollo": ("tanda0_ens_desarrollo_r2b_rs1.json", "salida_tanda0_r2b"),
          "tanda1": ("tanda1_20tos_r2b.json", "salida_tanda1_r2b"),
          "acumulado": (["tanda0_ens_diez_r2b_rs1.json", "tanda1_20tos_r2b.json"], ["salida_tanda0_r2b", "salida_tanda1_r2b"])}

regla = None
if REGLA:
    spec = importlib.util.spec_from_file_location("regla_nombres", REGLA)
    regla = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(regla)


def tramos(chunk: dict) -> list[tuple[str, str]]:
    """(clave del tramo, texto): los bloques heredados por su unidad de origen y su sha256, y el texto propio por el chunk."""
    out = [(f"heredado|{h['unidad_origen']}|{hashlib.sha256(h['texto'].encode()).hexdigest()[:16]}", h["texto"])
           for h in chunk.get("herencia", [])]
    out.append((f"propio|{chunk['id']}", chunk.get("texto") or ""))
    return out


def medir(ids: list[str], e0_de: dict[str, Path], nombres_remision: dict[str, list[str]]) -> dict:
    REF.TITULOS_TOS = REF.titulos_de_inventario(sorted(ids), nombres_remision)
    vistos, res = set(), {}
    for to in ids:
        for ch in json.loads((e0_de[to] / f"chunks_{to}.json").read_text(encoding="utf-8")):
            previas: list[str | None] = []
            for clave, texto in tramos(ch):
                # el bucle de menciones_por_tramo (r1_referencias.py:943-950), con la anáfora que sigue de un tramo al siguiente
                t_norm, _ = REF.normalizar_e0(texto, tolerar_linea_suelta="a" in REF.REGLAS_R2)
                ms = REF.detectar_menciones_r2(t_norm, to, REF.REGLAS_R2, normas_previas=previas)
                previas = previas + [m["to_destino"] for m in ms if m["clase"] == "externa"]
                if clave in vistos:
                    continue
                vistos.add(clave)
                for i, m in enumerate(ms):
                    if m["clase"] not in ("externa", "externa_anaforica"):
                        continue
                    res[f"{to}|{clave}|{i}"] = {"to_origen": to, "clase": m["clase"], "norma": m["norma_nombrada"],
                                               "to_destino": m["to_destino"], "via": m.get("via_norma"),
                                               "evidencia": m["evidencia"][-180:]}
    return {"titulos": {k: list(v) for k, v in REF.TITULOS_TOS.items()}, "menciones": res}


FINAL = [{"id": t, "nombres_remision": []} for t in json.loads(
    (COPIA / "data/experiment/segmentacion_oficial_e0r2/s2/cifras/tanda_final_S2c.json").read_text(encoding="utf-8"))["tanda_final"]["lista"]]
if E0_152:
    CORPUS["tanda_final"] = ([None], [E0_152])
    CORPUS["acumulado_final"] = (["tanda0_ens_diez_r2b_rs1.json", "tanda1_20tos_r2b.json", None],
                                 ["salida_tanda0_r2b", "salida_tanda1_r2b", E0_152])
out = {"corpus": {}}
for nombre, (man_n, e0_n) in CORPUS.items():
    mans = man_n if isinstance(man_n, list) else [man_n]
    e0s = e0_n if isinstance(e0_n, list) else [e0_n]
    entradas, e0_de = [], {}
    for mn, en in zip(mans, e0s):
        tos_mn = FINAL if mn is None else json.loads((MAN / mn).read_text(encoding="utf-8"))["tos"]
        for t in tos_mn:
            entradas.append(t); e0_de[t["id"]] = en if isinstance(en, Path) else E0 / en
    ids = [t["id"] for t in entradas]
    assert len(ids) == len(set(ids)), "un TO en dos manifiestos"
    a_mano = {t["id"]: list(t.get("nombres_remision") or []) for t in entradas}
    juegos = {"inventario": {}, "a_mano": a_mano}
    if regla:
        tit = REF.titulos_de_inventario(sorted(ids))           # el título oficial normalizado (sin listas)
        import csv
        oficial = {r["id"]: r["titulo_oficial"] for r in csv.DictReader(REF.INVENTARIO_TITULOS.open(encoding="utf-8"))}
        for x in json.loads(REF.INVENTARIO_RESUMEN.read_text(encoding="utf-8"))["subset_excluido"]:
            oficial[x["id_interno"]] = x["titulo"]
        juegos["regla"] = {t: regla.nombres(oficial[t]) for t in ids}
    out["corpus"][nombre] = {"tos": ids, "e0": [x if isinstance(x, str) else "e0 de los 152 (copia)" for x in e0s],
                             "manifiesto": [x or "tanda_final_S2c.json" for x in mans], "juegos": {}}
    for j, nr in juegos.items():
        r = medir(ids, e0_de, nr)
        out["corpus"][nombre]["juegos"][j] = {"nombres_remision": nr, **r}
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
for nombre, c in out["corpus"].items():
    for j, r in c["juegos"].items():
        ms = r["menciones"].values()
        res = sum(1 for m in ms if m["to_destino"])
        print(f"{nombre:<18} {j:<11} menciones {len(ms):>5}  resueltas {res:>5}  a un TO del corpus "
              f"{sum(1 for m in ms if m['to_destino'] in c['tos']):>5}")
