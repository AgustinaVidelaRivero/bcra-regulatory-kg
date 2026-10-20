"""B6.1, tanda final, T3, punto 4: los `nombres_remision` de los ensamblados nuevos, medidos (pre-registro, §7). Es
`data/experiment/nombres_remision/medir_nombres_remision_mesa.py` con otros corpus: la función `medir` y el texto por tramos, línea por
línea iguales; cambian solo los corpus y de dónde salen sus listas. USD 0, sin API. Corre sobre una COPIA del repo (nunca el repo) e
importa el detector sellado (`corpus_v2/r1_referencias.py`) sin cambiarlo: solo fija `TITULOS_TOS`, como hace el ensamblado.

Uso: python3 -I -B medir_nombres_t3_tf.py <copia> <out.json> --regla <regla_nombres_remision_*.py>

Corpus (con los TOs del manifiesto de ensamblado que se usó en T3, cada TO sobre la E0 de su tanda, en el repo):
  - tanda_final: los 98 de `tanda_final_ens_98_r2b.json` (T1);
  - tramo1: los 30 de `tanda_final_ens_tramo1_r2b_raya.json` (T3; la variante con la raya, por la decisión de la autora sobre el
    FRENO T3 parcial; en el parcial se midió con `tanda_final_ens_tramo1_r2b.json`, de T1);
  - acumulado_final: los 128 de `tanda_final_acumulado_ens_128_r2b.json` (T3);
  - acumulado_tramo1: los 60 de `tanda_final_acumulado_ens_60_tramo1_r2b.json` (T3).
  Las E0: `salida_tanda0_r2b/`, `salida_tanda1_r2b/` y `salida_tanda_final_r2b/` de `reextraccion_v2/e0_chunking/`. Los nombres de las
  carpetas quedan en `e0`, como en la medición de la mesa, para que `contrastar_con_inventario_completo_mesa.py` las encuentre.
Juegos de nombres (como en la medición de la mesa):
  - inventario: solo el título oficial del inventario, sin `nombres_remision`;
  - a_mano: aquí, las listas del manifiesto de ensamblado que se usó (las de la regla que entró en cada uno);
  - regla: con las listas que da la regla de `--regla` (función `nombres(titulo_oficial)`).
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

COPIA, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
REGLA = Path(sys.argv[sys.argv.index("--regla") + 1])
sys.dont_write_bytecode = True
assert not (Path.home() / "INGENIERIA IA/TESIS/bcra-regulatory-kg").resolve() == COPIA, "nunca sobre el repo"
sys.path.insert(0, str(COPIA / "data/experiment/reextraccion_v2/corpus_v2"))
import r1_referencias as REF  # noqa: E402

E0 = COPIA / "data/experiment/reextraccion_v2/e0_chunking"
M1 = "data/experiment/tanda_final/t1/ensamblado/manifiestos"
A = "data/experiment/tanda_final/t3/acumulado/manifiestos"
CORPUS = {"tanda_final": f"{M1}/tanda_final_ens_98_r2b.json", "tramo1": "data/experiment/tanda_final/t3/prueba_raya_tramo1/manifiestos/tanda_final_ens_tramo1_r2b_raya.json",
          "acumulado_final": f"{A}/tanda_final_acumulado_ens_128_r2b.json",
          "acumulado_tramo1": f"{A}/tanda_final_acumulado_ens_60_tramo1_r2b.json"}
E0_POR_TANDA = ("salida_tanda0_r2b", "salida_tanda1_r2b", "salida_tanda_final_r2b")

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


oficial = {r["id"]: r["titulo_oficial"] for r in csv.DictReader(REF.INVENTARIO_TITULOS.open(encoding="utf-8"))}
for x in json.loads(REF.INVENTARIO_RESUMEN.read_text(encoding="utf-8"))["subset_excluido"]:
    oficial[x["id_interno"]] = x["titulo"]
out = {"regla": REGLA.name, "corpus": {}}
for nombre, man in CORPUS.items():
    entradas = json.loads((COPIA / man).read_text(encoding="utf-8"))["tos"]
    ids = [t["id"] for t in entradas]
    assert len(ids) == len(set(ids)), "un TO dos veces"
    e0_de, e0s = {}, []
    for to in ids:
        en = [x for x in E0_POR_TANDA if (E0 / x / f"chunks_{to}.json").exists()]
        assert len(en) == 1, f"{to}: {en}"
        e0_de[to] = E0 / en[0]
        if en[0] not in e0s:
            e0s.append(en[0])
    juegos = {"inventario": {}, "a_mano": {t["id"]: list(t.get("nombres_remision") or []) for t in entradas},
              "regla": {t: regla.nombres(oficial[t]) for t in ids}}
    out["corpus"][nombre] = {"tos": ids, "e0": e0s, "manifiesto": [man], "juegos": {}}
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
