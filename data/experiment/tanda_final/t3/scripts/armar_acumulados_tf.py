"""
armar_acumulados_tf.py — B6.1, tanda final, T3, punto 3: las entradas de los dos acumulados nuevos, por copia, sobre una raíz (la copia
del repo; nunca el repo). USD 0, sin API. Es `data/experiment/tanda1/t3/scripts/armar_acumulado_t3.py` con tres tandas en lugar de dos.

  128: las tandas 0, 1 y final (10, 20 y 98 TOs);
  60:  las tandas 0 y 1 y el tramo 1 de la tanda final (10, 20 y 30 TOs: los primeros 30 de `orden_corrida` de su manifiesto).

Lee solo las salidas selladas de las tres tandas y escribe en <raíz>/data/experiment/tanda_final/t3/acumulado/:
  manifiestos/acumulado_<n>tos_r2b.json   el manifiesto de EXTRACCIÓN del acumulado, que pide derivar_manifiesto_ensamblado_mesa.py:
      - `tos`: las entradas de tanda0_10tos_r2b.json, tanda1_20tos_r2b.json y tanda_final_98tos_r2b.json (en el de 60, solo las del
        tramo 1), tal cual; `orden_corrida`: el de cada tanda, en ese orden;
      - `perfil_e1`: r2b; `rutas.e0_salida`: la E0 combinada de abajo;
      - `limites`: los `estimado_usd` de los tres, con tope y margen en 0 (no es el manifiesto de una extracción; el ensamblado no lee
        `limites` ni `sellos`); `sellos`: los de los tres, cada uno con su clave.
  e0_acumulado_<n>_r2b/   los archivos por TO de las tres E0 (chunks_, estructura_, indice_, pies_ y tablas_), copiados de
      reextraccion_v2/e0_chunking/salida_tanda0_r2b/, salida_tanda1_r2b/ y salida_tanda_final_r2b/. Los agregados y version_e0.json no
      se copian: el ensamblado y shapes (S31) leen solo los archivos por TO.
  entrada_acumulado_<n>_r2b/<TO>/   las carpetas por TO de corpus_tanda0/salida_r2b/, corpus_tanda1/salida_r2b/ y
      corpus_tanda_final/salida_r2b/, copiadas enteras (el ensamblado lee <entrada>/<TO>/).
  armado_acumulado_<n>_tf.json   el sha256 de cada archivo copiado de la E0 y de su origen; de la entrada, solo el total de archivos, sus
      bytes, el sha256 de la lista ordenada «ruta sha256» y si todos son iguales a su origen. Los nombres de los archivos de la entrada
      no se escriben: cuántos TOs tienen un archivo de E3 es una cifra de E3 (cegamiento, punto 8 del «seguí» de T3).

Frena si un TO aparece en dos tandas, si falta un archivo por TO de la E0 o una carpeta de la entrada, o si un destino ya existe.
Uso: python3 -I -B armar_acumulados_tf.py <raíz> 128|60
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(sys.argv[1]).resolve()
N = sys.argv[2]
assert N in ("128", "60"), N
REX = RAIZ / "data/experiment/reextraccion_v2"
OUT = RAIZ / "data/experiment/tanda_final/t3/acumulado"
MAN = {"tanda0": REX / "manifiestos/tanda0_10tos_r2b.json", "tanda1": REX / "manifiestos/tanda1_20tos_r2b.json",
       "tanda_final": REX / "manifiestos/tanda_final_98tos_r2b.json"}
E0 = {"tanda0": REX / "e0_chunking/salida_tanda0_r2b", "tanda1": REX / "e0_chunking/salida_tanda1_r2b",
      "tanda_final": REX / "e0_chunking/salida_tanda_final_r2b"}
ENT = {"tanda0": REX / "corpus_tanda0/salida_r2b", "tanda1": REX / "corpus_tanda1/salida_r2b",
       "tanda_final": REX / "corpus_tanda_final/salida_r2b"}
NOMBRE = f"acumulado_{N}tos_r2b"
E0_DIR = f"e0_acumulado_{N}_r2b"
ENT_DIR = f"entrada_acumulado_{N}_r2b"
E0_REL = f"data/experiment/tanda_final/t3/acumulado/{E0_DIR}"
POR_TO = ("chunks", "estructura", "indice", "pies", "tablas")


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main() -> int:
    m = {k: json.loads(p.read_text(encoding="utf-8")) for k, p in MAN.items()}
    if N == "60":
        tramo1 = m["tanda_final"]["orden_corrida"][:30]
        mf = json.loads(json.dumps(m["tanda_final"]))
        mf["tos"] = [t for t in mf["tos"] if t["id"] in tramo1]
        mf["orden_corrida"] = list(tramo1)
        mf["limites"]["estimado_usd"] = {t: v for t, v in mf["limites"]["estimado_usd"].items() if t in tramo1}
        m["tanda_final"] = mf
    ids = {k: [t["id"] for t in v["tos"]] for k, v in m.items()}
    todos = [t for k in m for t in ids[k]]
    if len(todos) != len(set(todos)):
        raise SystemExit("FRENO: hay TOs en dos tandas")
    for d in (OUT / "manifiestos" / f"{NOMBRE}.json", OUT / E0_DIR, OUT / ENT_DIR):
        if d.exists():
            raise SystemExit(f"FRENO: {d.relative_to(RAIZ)} ya existe")
    tanda = {t: k for k in m for t in ids[k]}
    descr_tramo = " (solo el tramo 1 de la tanda final: los primeros 30 de su orden_corrida)" if N == "60" else ""
    man = {
        "version": "1",
        "nombre": NOMBRE,
        "descripcion": (
            f"B6.1, tanda final, T3, punto 3: el manifiesto de extracción del acumulado de las tandas 0, 1 y final{descr_tramo} "
            f"({len(todos)} TOs), armado por data/experiment/tanda_final/t3/scripts/armar_acumulados_tf.py para derivar de él los "
            f"manifiestos de ensamblado. `tos`: las entradas de tanda0_10tos_r2b.json ({sha(MAN['tanda0'])[:8]}…), tanda1_20tos_r2b.json "
            f"({sha(MAN['tanda1'])[:8]}…) y tanda_final_98tos_r2b.json ({sha(MAN['tanda_final'])[:8]}…), tal cual; `orden_corrida`: el de "
            "cada tanda, en ese orden; `rutas.e0_salida`: la E0 combinada (los archivos por TO de las tres E0, por copia); `limites`: los "
            "estimados, con tope y margen en 0 porque no es el manifiesto de una extracción; `sellos`: los de los tres. El ensamblado no "
            "lee `limites` ni `sellos`."),
        "tos": [t for k in m for t in m[k]["tos"]],
        "orden_corrida": [t for k in m for t in m[k]["orden_corrida"]],
        "perfil_e1": "r2b",
        "rutas": {"e0_salida": E0_REL},
        "oraculo": {"mapa_territorio": None, "limitaciones_e0": []},
        "limites": {"tope_global_usd": 0.0, "margen_unidad_usd": 0.0,
                    "estimado_usd": {t: v for k in m for t, v in m[k]["limites"]["estimado_usd"].items()},
                    "checkpoint_cada": {}, "chequeos_hits": []},
        "tests_respuesta_conocida": None,
        "sellos": {k: m[k]["sellos"] for k in m},
        "indice_fragmentos": None,
    }
    assert all(v["perfil_e1"] == "r2b" and v["tests_respuesta_conocida"] is None for v in m.values())
    registro = {"manifiestos_de_origen": {k: {"ruta": str(p.relative_to(RAIZ)), "sha256": sha(p)} for k, p in MAN.items()},
                "e0": [], "entrada": []}
    (OUT / E0_DIR).mkdir(parents=True)
    for to in man["orden_corrida"]:
        for pre in POR_TO:
            o = E0[tanda[to]] / f"{pre}_{to}.json"
            if not o.is_file():
                raise SystemExit(f"FRENO: falta {o.relative_to(RAIZ)}")
            d = OUT / E0_DIR / o.name
            shutil.copy2(o, d)
            registro["e0"].append({"to": to, "archivo": o.name, "origen": str(o.relative_to(RAIZ)), "sha256": sha(d),
                                   "igual_al_origen": sha(d) == sha(o)})
    (OUT / ENT_DIR).mkdir(parents=True)
    lista, iguales, n_ent, b_ent = hashlib.sha256(), True, 0, 0
    for to in man["orden_corrida"]:
        o = ENT[tanda[to]] / to
        if not o.is_dir():
            raise SystemExit(f"FRENO: falta {o.relative_to(RAIZ)}")
        d = OUT / ENT_DIR / to
        shutil.copytree(o, d)
        for p in sorted(x for x in o.rglob("*") if x.is_file()):
            q = d / p.relative_to(o)
            sq = sha(q)
            iguales = iguales and sq == sha(p)
            n_ent += 1
            b_ent += q.stat().st_size
            lista.update(f"{q.relative_to(OUT / ENT_DIR)} {sq}\n".encode())
    registro["entrada"] = {"archivos": n_ent, "bytes": b_ent, "sha256_de_la_lista": lista.hexdigest(), "todos_iguales_al_origen": iguales}
    (OUT / "manifiestos").mkdir(parents=True, exist_ok=True)
    (OUT / "manifiestos" / f"{NOMBRE}.json").write_text(json.dumps(man, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    registro["manifiesto"] = {"ruta": f"data/experiment/tanda_final/t3/acumulado/manifiestos/{NOMBRE}.json",
                              "sha256": sha(OUT / "manifiestos" / f"{NOMBRE}.json")}
    registro["conteos"] = {"tos": len(man["tos"]), **{k: len(ids[k]) for k in m},
                           "archivos_e0": len(registro["e0"]), "archivos_entrada": registro["entrada"]["archivos"],
                           "bytes_entrada": registro["entrada"]["bytes"],
                           "todos_iguales_al_origen": all(x["igual_al_origen"] for x in registro["e0"]) and registro["entrada"]["todos_iguales_al_origen"]}
    (OUT / f"armado_acumulado_{N}_tf.json").write_text(json.dumps(registro, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(registro["conteos"], ensure_ascii=False), registro["manifiesto"]["sha256"])
    return 0 if registro["conteos"]["todos_iguales_al_origen"] else 1


if __name__ == "__main__":
    sys.exit(main())
