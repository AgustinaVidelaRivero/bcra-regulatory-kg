"""
armar_acumulado_t3.py — B6.1, tanda 1, T3, punto 3: las entradas del acumulado de las tandas 0 y 1 (30 TOs), por copia, sobre una raíz
(la copia del repo; nunca el repo). USD 0, sin API. Solo lee las salidas selladas de las dos tandas; escribe en <raíz>/data/experiment/
tanda1/t3/acumulado/.

Escribe:
  manifiestos/acumulado_30tos_r2b.json   el manifiesto de EXTRACCIÓN del acumulado, que pide derivar_manifiesto_ensamblado_mesa.py:
      - `tos`: las entradas de tanda0_10tos_r2b.json y después las de tanda1_20tos_r2b.json, tal cual;
      - `orden_corrida`: el de la tanda 0 y después el de la tanda 1;
      - `perfil_e1`: r2b (el de los dos);
      - `rutas.e0_salida`: la E0 combinada de abajo;
      - `limites`: los `estimado_usd` de los dos manifiestos; tope y margen en 0, como el manifiesto de E0 de S1-ter, porque este
        manifiesto no es de una extracción (el ensamblado no lee `limites` ni `sellos`);
      - `sellos`: los de los dos manifiestos, cada uno con su clave (`tanda0`, `tanda1`).
  e0_acumulado_r2b/   los archivos por TO de las dos E0 (chunks_, estructura_, indice_, pies_ y tablas_ de cada TO), copiados de
      reextraccion_v2/e0_chunking/salida_tanda0_r2b/ y salida_tanda1_r2b/. Los agregados (conteos.json, cobertura.json, …) y
      version_e0.json no se copian: el ensamblado (ensamblar_tanda0.py: _chunks_e0_r2, _celdas_por_chunk, version_y_materia_r2b,
      r1_comun.cargar_chunks_enm01) y shapes (S31) leen solo los archivos por TO, y las dos E0 tienen versiones distintas.
  entrada_acumulado_r2b/<TO>/   las carpetas por TO de corpus_tanda0/salida_r2b/ y de corpus_tanda1/salida_r2b/, copiadas enteras
      (el ensamblado lee <entrada>/<TO>/). Los archivos de la raíz de cada salida (estado_corpus.json, checkpoints, …) no se copian:
      el ensamblado no los lee.
  armado_acumulado_t3.json   el sha256 de cada archivo copiado y de su origen, y los conteos.

Frena si un TO aparece en las dos tandas, si falta un archivo por TO de la E0 o una carpeta de la entrada, o si un destino ya existe.

Uso: python3 -I -B armar_acumulado_t3.py <raíz>
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1]).resolve()
REX = RAIZ / "data/experiment/reextraccion_v2"
OUT = RAIZ / "data/experiment/tanda1/t3/acumulado"
MAN_T0 = REX / "manifiestos/tanda0_10tos_r2b.json"
MAN_T1 = REX / "manifiestos/tanda1_20tos_r2b.json"
E0 = {"tanda0": REX / "e0_chunking/salida_tanda0_r2b", "tanda1": REX / "e0_chunking/salida_tanda1_r2b"}
ENT = {"tanda0": REX / "corpus_tanda0/salida_r2b", "tanda1": REX / "corpus_tanda1/salida_r2b"}
E0_REL = "data/experiment/tanda1/t3/acumulado/e0_acumulado_r2b"
POR_TO = ("chunks", "estructura", "indice", "pies", "tablas")
NOMBRE = "acumulado_30tos_r2b"


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main() -> int:
    m0 = json.loads(MAN_T0.read_text(encoding="utf-8"))
    m1 = json.loads(MAN_T1.read_text(encoding="utf-8"))
    ids0, ids1 = [t["id"] for t in m0["tos"]], [t["id"] for t in m1["tos"]]
    if set(ids0) & set(ids1):
        raise SystemExit(f"FRENO: TOs en las dos tandas: {sorted(set(ids0) & set(ids1))}")
    for d in (OUT / "manifiestos" / f"{NOMBRE}.json", OUT / "e0_acumulado_r2b", OUT / "entrada_acumulado_r2b"):
        if d.exists():
            raise SystemExit(f"FRENO: {d.relative_to(RAIZ)} ya existe")
    tanda = {**{t: "tanda0" for t in ids0}, **{t: "tanda1" for t in ids1}}

    man = {
        "version": "1",
        "nombre": NOMBRE,
        "descripcion": (
            "B6.1, tanda 1, T3, punto 3: el manifiesto de extracción del acumulado de las tandas 0 y 1 (30 TOs), armado por "
            "data/experiment/tanda1/t3/scripts/armar_acumulado_t3.py para que derivar_manifiesto_ensamblado_mesa.py derive de él "
            "los manifiestos de ensamblado. `tos`: las entradas de tanda0_10tos_r2b.json (sha256 " + sha(MAN_T0)[:8] + "…) y de "
            "tanda1_20tos_r2b.json (" + sha(MAN_T1)[:8] + "…), tal cual; `orden_corrida`: el de la tanda 0 y el de la tanda 1; "
            "`rutas.e0_salida`: la E0 combinada (los archivos por TO de salida_tanda0_r2b y salida_tanda1_r2b, por copia); "
            "`limites`: los estimados de los dos, con tope y margen en 0 porque no es el manifiesto de una extracción; `sellos`: "
            "los de los dos. El ensamblado no lee `limites` ni `sellos`."),
        "tos": m0["tos"] + m1["tos"],
        "orden_corrida": list(m0["orden_corrida"]) + list(m1["orden_corrida"]),
        "perfil_e1": "r2b",
        "rutas": {"e0_salida": E0_REL},
        "oraculo": {"mapa_territorio": None, "limitaciones_e0": []},
        "limites": {"tope_global_usd": 0.0, "margen_unidad_usd": 0.0,
                    "estimado_usd": {**m0["limites"]["estimado_usd"], **m1["limites"]["estimado_usd"]},
                    "checkpoint_cada": {}, "chequeos_hits": []},
        "tests_respuesta_conocida": None,
        "sellos": {"tanda0": m0["sellos"], "tanda1": m1["sellos"]},
        "indice_fragmentos": None,
    }
    assert m0["perfil_e1"] == m1["perfil_e1"] == "r2b"
    assert m0["tests_respuesta_conocida"] is None and m1["tests_respuesta_conocida"] is None

    registro = {"manifiestos_de_origen": {"tanda0": {"ruta": str(MAN_T0.relative_to(RAIZ)), "sha256": sha(MAN_T0)},
                                          "tanda1": {"ruta": str(MAN_T1.relative_to(RAIZ)), "sha256": sha(MAN_T1)}},
                "e0": [], "entrada": []}
    (OUT / "e0_acumulado_r2b").mkdir(parents=True)
    for to in man["orden_corrida"]:
        for pre in POR_TO:
            o = E0[tanda[to]] / f"{pre}_{to}.json"
            if not o.is_file():
                raise SystemExit(f"FRENO: falta {o.relative_to(RAIZ)}")
            d = OUT / "e0_acumulado_r2b" / o.name
            shutil.copy2(o, d)
            registro["e0"].append({"to": to, "archivo": o.name, "origen": str(o.relative_to(RAIZ)), "sha256": sha(d),
                                   "igual_al_origen": sha(d) == sha(o)})
    (OUT / "entrada_acumulado_r2b").mkdir(parents=True)
    for to in man["orden_corrida"]:
        o = ENT[tanda[to]] / to
        if not o.is_dir():
            raise SystemExit(f"FRENO: falta {o.relative_to(RAIZ)}")
        d = OUT / "entrada_acumulado_r2b" / to
        shutil.copytree(o, d)
        for p in sorted(x for x in o.rglob("*") if x.is_file()):
            q = d / p.relative_to(o)
            registro["entrada"].append({"to": to, "archivo": str(p.relative_to(o)), "origen": str(p.relative_to(RAIZ)),
                                        "sha256": sha(q), "igual_al_origen": sha(q) == sha(p)})
    (OUT / "manifiestos").mkdir(parents=True, exist_ok=True)
    (OUT / "manifiestos" / f"{NOMBRE}.json").write_text(json.dumps(man, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    registro["manifiesto"] = {"ruta": f"data/experiment/tanda1/t3/acumulado/manifiestos/{NOMBRE}.json",
                              "sha256": sha(OUT / "manifiestos" / f"{NOMBRE}.json")}
    registro["conteos"] = {"tos": len(man["tos"]), "tanda0": len(ids0), "tanda1": len(ids1),
                           "archivos_e0": len(registro["e0"]), "archivos_entrada": len(registro["entrada"]),
                           "todos_iguales_al_origen": all(x["igual_al_origen"] for x in registro["e0"] + registro["entrada"])}
    (OUT / "armado_acumulado_t3.json").write_text(json.dumps(registro, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(registro["conteos"], ensure_ascii=False), registro["manifiesto"]["sha256"])
    return 0 if registro["conteos"]["todos_iguales_al_origen"] else 1


if __name__ == "__main__":
    sys.exit(main())
