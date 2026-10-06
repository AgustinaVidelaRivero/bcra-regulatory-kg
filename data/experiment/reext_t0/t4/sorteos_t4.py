"""U-REEXT-T0, T4, puntos 1 y 8: los sorteos, con las semillas y los procedimientos sellados en T1
(data/experiment/reext_t0/sellos_t4.json, sha256 7845d11a…fac560), antes de leer nada. Escribe la lista de ids con la
hora en --out. No mira extracciones: la cola sale de los estados finales de la corrida y las omisiones, de las claves y
del contador del validador; el texto de los tramos no se usa salvo para el contador.

  Punto 1, cola humana: la cola de los diez TOs son las unidades cuya última versión en finales.jsonl de salida_r2b/
  tiene un estado cola_humana*; con más de 30, random.Random(semilla).sample(sorted(chunk_ids), 30).
  Punto 8, omisiones meta_normativo de omisiones.jsonl del ensamblado r2b de diez (el sellado): la clave de cada una es
  (chunk_id, posición en la lista de omisiones de su unidad, desde 0, en el orden del archivo). La marca del contador es
  la de validador_r2.marcas_meta_normativo sobre el tramo que vio el validador (el del modelo: tramo_modelo si el tramo
  guardado es el literal mínimo, si no tramo); sin ninguna de las siete clases, «sin marca». Con más de 30 por grupo,
  random.Random(semilla).sample(sorted(claves), 30).

Uso (desde la raíz del repo o de una copia): python -B data/experiment/reext_t0/t4/sorteos_t4.py --out ARCHIVO.json
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import random
import sys
from collections import Counter, OrderedDict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
REX = RAIZ / "data" / "experiment" / "reextraccion_v2"
SALIDA = REX / "corpus_tanda0" / "salida_r2b"
ENS = REX / "corpus_tanda0" / "ens_diez_r2b" / "r2"
SELLOS = RAIZ / "data" / "experiment" / "reext_t0" / "sellos_t4.json"
SHA_SELLOS = "7845d11ac2955e7c606357e1f7b50d6ef2d951bb21acb111c16f31e117fac560"
SHA_KG_DIEZ = "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
N = 30
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "pyd_r2" / "code"))
import validador_r2 as V  # noqa: E402 — el contador del validador, importado, no copiado


def sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha_lista(xs) -> str:
    return sha_bytes(json.dumps(xs, ensure_ascii=False).encode("utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    hora = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    crudo = SELLOS.read_bytes()
    assert sha_bytes(crudo) == SHA_SELLOS, "sellos_t4.json no es el sellado en T1"
    assert sha_bytes((ENS / "kg.json").read_bytes()) == SHA_KG_DIEZ, "el ensamblado de diez no es el sellado"
    sellos = json.loads(crudo)["d_semillas_t4"]

    # Punto 1
    estados = {}
    for to in TOS:
        ultima = {}
        for x in (SALIDA / to / "finales.jsonl").read_text(encoding="utf-8").splitlines():
            if x.strip():
                r = json.loads(x)
                ultima[r["chunk_id"]] = r
        estados.update({cid: r["estado"] for cid, r in ultima.items() if str(r.get("estado", "")).startswith("cola_humana")})
    pob_cola = sorted(estados)
    rep = json.loads((ENS / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
    cola_reporte = sorted(c for v in rep["e2_por_to"].values() for c in v["cola_flaggeada"]["chunks_de_cola"])
    sem = sellos["cola_humana"]["semilla"]
    muestra = random.Random(sem).sample(pob_cola, N) if len(pob_cola) > N else list(pob_cola)
    cola = OrderedDict([
        ("semilla", sem), ("procedimiento", sellos["cola_humana"]["procedimiento"]),
        ("poblacion", len(pob_cola)), ("poblacion_por_estado", dict(sorted(Counter(estados.values()).items()))),
        ("poblacion_sha256_lista_ordenada", sha_lista(pob_cola)),
        ("igual_a_la_cola_del_reporte_del_ensamblado", pob_cola == cola_reporte),
        ("parte1_de_cap_4_2_1_2_en_la_muestra", "cap::4.2.1.2::parte1" in muestra),
        ("muestra_en_orden_del_sorteo", [{"chunk_id": c, "estado": estados[c]} for c in muestra]),
        ("fuera_de_la_muestra", sorted(set(pob_cola) - set(muestra)))])

    # Punto 8
    filas = [json.loads(x) for x in (ENS / "omisiones.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    pos, grupos = Counter(), {"sin_marca": [], "con_marca": []}
    marcas = {}
    for f in filas:
        clave = (f["chunk_id"], pos[f["chunk_id"]])
        pos[f["chunk_id"]] += 1
        if f.get("categoria") != "meta_normativo":
            continue
        visto = f.get("tramo_modelo") or f.get("tramo")
        m = V.marcas_meta_normativo(visto) if isinstance(visto, str) else []
        marcas[clave] = m
        grupos["con_marca" if m else "sin_marca"].append(clave)
    omis = OrderedDict()
    for g, nombre in (("sin_marca", "omisiones_meta_normativo_sin_marca"), ("con_marca", "omisiones_meta_normativo_con_marca")):
        pob = sorted(grupos[g])
        sem = sellos[nombre]["semilla"]
        mu = random.Random(sem).sample(pob, N) if len(pob) > N else list(pob)
        omis[g] = OrderedDict([
            ("semilla", sem), ("procedimiento", sellos[nombre]["procedimiento"]), ("poblacion", len(pob)),
            ("poblacion_sha256_lista_ordenada", sha_lista([list(k) for k in pob])),
            ("clases_en_la_poblacion", dict(sorted(Counter(c for k in pob for c in marcas[k]).items()))),
            ("muestra_en_orden_del_sorteo", [{"chunk_id": k[0], "posicion": k[1], "marcas": marcas[k]} for k in mu])])
    out = OrderedDict([
        ("unidad", "U-REEXT-T0, T4, puntos 1 y 8 (sorteos antes de leer)"), ("hora", hora),
        ("sellos_t4_sha256", SHA_SELLOS), ("kg_diez_sha256", SHA_KG_DIEZ),
        ("omisiones_jsonl_sha256", sha_bytes((ENS / "omisiones.jsonl").read_bytes())),
        ("validador_r2_sha256", sha_bytes(Path(V.__file__).read_bytes())),
        ("punto_1_cola_humana", cola), ("punto_8_omisiones", omis),
        ("omisiones_jsonl_filas", len(filas)), ("omisiones_meta_normativo", sum(len(v) for v in grupos.values()))])
    a.out.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"hora": hora, "cola": [len(pob_cola), len(muestra), cola["parte1_de_cap_4_2_1_2_en_la_muestra"],
                                             cola["igual_a_la_cola_del_reporte_del_ensamblado"]],
                      "omisiones": {g: [v["poblacion"], len(v["muestra_en_orden_del_sorteo"])] for g, v in omis.items()}},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
