"""
c1_acta.py — U-CONF-MATRIZ, C1 (mandato FIRMADO en 90addb35, §1 a §3): población, sorteo y orden de lectura, sellados antes de
abrir una ficha. Nada de esto mira el texto de una unidad: solo las aristas del grafo y el tipo de sus extremos. USD 0.

  Población: las aristas `condicion_de` de KG-Tanda0-Diez-r2b-sincola (e22fae1a…) con destino de tipo Operacion y, aparte, con
  destino de tipo Potestad, ordenadas por (origen, destino).
  Sorteo: random.Random(semilla).sample(lista, 30) por par, con las semillas de la sección «Firma» del mandato, que este script
  recalcula desde el texto firmado (las líneas anteriores a «## Firma», en el commit de la firma) y compara con las asentadas.
  Orden de lectura: las 60 juntas (las 30 de → Operacion en el orden del sorteo y después las 30 de → Potestad),
  random.Random(semilla_orden).shuffle(...), con semilla_orden = int(sha256("U-CONF-MATRIZ|orden|<sha256 del texto
  firmado>")[:16], 16). El mandato no fija la semilla del orden; se deriva del texto firmado para que no dependa de la muestra.

Corre desde la raíz de una COPIA del repo (CLAUDE.md §4.l) y escribe solo --salida/acta_c1.json.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/conf_matriz/c1_acta.py --salida DIR
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

REPO = Path(__file__).resolve().parents[3]
KG = REPO / "data" / "experiment" / "reextraccion_v2" / "corpus_tanda0" / "ens_diez_r2b_sincola" / "r2" / "kg.json"
KG_V = REPO / "data" / "experiment" / "reextraccion_v2" / "corpus_tanda0" / "ens_desarrollo_r2b_sincola" / "r2" / "kg.json"
MANDATO = REPO / "docs" / "mandatos" / "UCONF_MATRIZ_lectura_confirmacion.md"
PROTOCOLO = REPO / "reports" / "u_estudio_matriz" / "lectura" / "resultado_lectura_matriz.md"
KG_SHA256 = "e22fae1afc3cf37fbe5b49ee0b220d51d0ec5febc13abeb6ebf7b74226da34fb"      # grafos.py:172 (dde9f44)
KG_V_SHA256 = "2922b72dca2c2bcb204a04f53fc89f265ac2c57e83e6aaab2ce1af8b82d413e4"    # grafos.py, etapa V del pre-registro
COMMIT_FIRMA = "90addb35"
COMMIT_PROTOCOLO = "c671b52"
TEXTO_FIRMADO_SHA256 = "1d92fbd6ccfd9404aa3417df96b3fab2ffda1d61aca74074446ea5d6b9366d7d"   # mandato, sección «Firma»
SEMILLAS_ASENTADAS = {                                                                     # mandato, sección «Firma»
    "Operacion": 16560617781465913851, "Potestad": 10236682513526931005,
    "revision|Operacion": 3317428300167781795, "revision|Potestad": 9868107349525416484,
    "complementaria|Operacion": 1949760007166469060, "complementaria|Potestad": 1922576108924699355}
PARES = ("Operacion", "Potestad")
N_POR_PAR = 30
POBLACION_ESPERADA = {"Operacion": 643, "Potestad": 264}                                   # mandato, §1


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canon(x) -> bytes:
    return json.dumps(x, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def semilla(uso: str, texto_sha: str) -> int:
    return int(sha(("U-CONF-MATRIZ|" + uso + "|" + texto_sha).encode())[:16], 16)


def seccion_protocolo(texto: str) -> str:
    """La sección «Protocolo, tal como está asentado», hasta el encabezado siguiente de nivel 1 o 2."""
    out, dentro = [], False
    for linea in texto.splitlines(keepends=True):
        if linea.startswith("## Protocolo, tal como está asentado"):
            dentro = True
        elif dentro and (linea.startswith("# ") or linea.startswith("## ")):
            break
        if dentro:
            out.append(linea)
    if not out:
        raise SystemExit("sin la sección del protocolo")
    return "".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()

    # el texto firmado y las semillas
    mandato = MANDATO.read_bytes()
    texto = mandato.decode("utf-8")
    corte = texto.split("\n## Firma\n")[0] + "\n"
    s_texto = sha(corte.encode("utf-8"))
    if s_texto != TEXTO_FIRMADO_SHA256:
        raise SystemExit(f"texto firmado con sha256 {s_texto}, no el asentado")
    semillas = {u: semilla(u, s_texto) for u in SEMILLAS_ASENTADAS}
    if semillas != SEMILLAS_ASENTADAS:
        raise SystemExit(f"semillas distintas de las asentadas: {semillas}")
    semilla_orden = semilla("orden", s_texto)

    # el criterio
    proto = PROTOCOLO.read_bytes()
    seccion = seccion_protocolo(proto.decode("utf-8"))

    # el grafo
    raw = KG.read_bytes()
    if sha(raw) != KG_SHA256:
        raise SystemExit(f"kg.json con sha256 {sha(raw)}, no el sellado")
    kg = json.loads(raw)
    nodos = {n["id"]: n for n in kg["nodes"]}
    poblacion = {}
    for par in PARES:
        filas = sorted([e["source"], e["target"], e["provenance"]["chunk_id"]] for e in kg["edges"]
                       if e["relation"] == "condicion_de" and nodos[e["target"]]["type"] == par)
        if len({(f[0], f[1]) for f in filas}) != len(filas):
            raise SystemExit(f"pares (origen, destino) repetidos en → {par}")
        if len(filas) != POBLACION_ESPERADA[par]:
            raise SystemExit(f"→ {par}: {len(filas)} aristas, no {POBLACION_ESPERADA[par]}")
        poblacion[par] = filas

    # el sorteo
    hora = datetime.now().astimezone().isoformat(timespec="seconds")
    muestra = {par: random.Random(semillas[par]).sample(poblacion[par], N_POR_PAR) for par in PARES}

    # el orden de lectura
    orden = [(par, i) for par in PARES for i in range(N_POR_PAR)]
    random.Random(semilla_orden).shuffle(orden)
    fichas = []
    for k, (par, i) in enumerate(orden, 1):
        o, d, cid = muestra[par][i]
        fichas.append({"ficha": f"F{k:02d}", "par": par, "orden_en_el_sorteo": i + 1, "origen": o, "destino": d,
                       "chunk_id_arista": cid})

    # aristas de la muestra presentes en el grafo de la etapa V del pre-registro de tripletas (para declarar el solapamiento
    # cuando exista la muestra de V; hoy no hay acta de su sorteo)
    raw_v = KG_V.read_bytes()
    if sha(raw_v) != KG_V_SHA256:
        raise SystemExit(f"kg.json de V con sha256 {sha(raw_v)}, no el sellado")
    aristas_v = {(e["source"], e["relation"], e["target"]) for e in json.loads(raw_v)["edges"]}
    en_v = sorted(f["ficha"] for f in fichas if (f["origen"], "condicion_de", f["destino"]) in aristas_v)

    out = {
        "unidad": "U-CONF-MATRIZ, C1 (acta del sorteo; nada se lee todavía)",
        "mandato": {"ruta": "docs/mandatos/UCONF_MATRIZ_lectura_confirmacion.md", "commit_firma": COMMIT_FIRMA,
                    "sha256_archivo": sha(mandato), "sha256_texto_firmado": s_texto,
                    "texto_firmado": "las líneas anteriores a «## Firma», en el commit de la firma"},
        "grafo": {"nombre": "KG-Tanda0-Diez-r2b-sincola", "ruta": str(KG.relative_to(REPO)), "kg_sha256": KG_SHA256,
                  "registro": "data/experiment/neo4j/grafos.py:172", "sellos": ["dde9f44", "235a295"],
                  "nodos": len(kg["nodes"]), "aristas": len(kg["edges"])},
        "criterio": {"protocolo": {"ruta": "reports/u_estudio_matriz/lectura/resultado_lectura_matriz.md",
                                   "commit": COMMIT_PROTOCOLO, "sha256_archivo": sha(proto),
                                   "seccion": "Protocolo, tal como está asentado",
                                   "sha256_seccion": sha(seccion.encode("utf-8"))},
                     "mandato_seccion_2": "dentro del texto firmado (sha256_texto_firmado)",
                     "regla_por_par": "se confirma si el límite inferior de Wilson al 95 % (z = 1,959964) de correctas / "
                                      "(correctas + incorrectas) es ≥ 0,75; no decidibles excluidas y reportadas; con más "
                                      "de 6 no decidibles el par no se decide con esta muestra"},
        "poblacion": {par: {"N": len(poblacion[par]),
                            "sha256_lista": sha(canon(poblacion[par])),
                            "por_to": dict(sorted(Counter(f[2].split("::")[0] for f in poblacion[par]).items())),
                            "como_se_calcula_el_sha256": "json.dumps(filas, ensure_ascii=False, separators=(',', ':')) en "
                                                         "UTF-8, filas [origen, destino, chunk_id de la arista] ordenadas "
                                                         "por (origen, destino)",
                            "filas": poblacion[par]} for par in PARES},
        "sorteo": {"semillas": {u: str(v) for u, v in semillas.items()},
                   "fuente_semillas": "mandato, sección «Firma»; recalculadas desde el texto firmado y comparadas",
                   "metodo": "random.Random(semilla).sample(lista ordenada por (origen, destino), 30), por par",
                   "hora": hora, "python": sys.version.split()[0],
                   "muestra": {par: [{"orden": i, "origen": f[0], "destino": f[1], "chunk_id_arista": f[2]}
                                     for i, f in enumerate(muestra[par], 1)] for par in PARES},
                   "sha256_muestra": sha(canon(muestra)),
                   "como_se_calcula_el_sha256": "json.dumps({'Operacion': [filas en el orden del sorteo], 'Potestad': "
                                                "[...]}, ensure_ascii=False, separators=(',', ':')) en UTF-8",
                   "muestra_por_to": {par: dict(sorted(Counter(f[2].split("::")[0] for f in muestra[par]).items()))
                                      for par in PARES}},
        "orden_de_lectura": {"semilla_orden": str(semilla_orden),
                             "fuente": "int(sha256('U-CONF-MATRIZ|orden|<sha256 del texto firmado>')[:16], 16); decisión "
                                       "de la sesión lectora, no del mandato",
                             "metodo": "las 30 de → Operacion en el orden del sorteo y después las 30 de → Potestad; "
                                       "random.Random(semilla_orden).shuffle",
                             "fichas": fichas, "sha256_fichas": sha(canon(fichas))},
        "solapamiento_etapa_v": {"grafo_v": {"nombre": "KG-Tanda0-Desarrollo-r2b-sincola", "kg_sha256": KG_V_SHA256},
                                 "fichas_cuya_arista_esta_en_el_grafo_de_v": en_v,
                                 "nota": "la muestra de la etapa V del pre-registro de tripletas no está sorteada (sin acta "
                                         "en el repo); el solapamiento se declara cuando exista, sin excluir (pre-registro, "
                                         ":42)"},
        "insumos": {"c1_acta.py_sha256": sha(Path(__file__).read_bytes())},
    }
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "acta_c1.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"N": {par: len(poblacion[par]) for par in PARES},
                      "sha256_lista": {par: out["poblacion"][par]["sha256_lista"] for par in PARES},
                      "hora": hora, "sha256_muestra": out["sorteo"]["sha256_muestra"],
                      "sha256_fichas": out["orden_de_lectura"]["sha256_fichas"], "en_grafo_v": len(en_v)},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
