"""Sorteo de las 20 respuestas de la mitad de verificación del gold de Q12: las de A2.2 (mesa, §276, 25/10/2026). USD 0, sin API.

La regla está en regla_sorteo_gold_q12_verificacion_mesa.md, al lado de este script; los dos se sellan antes de correrlo.

Uso: python3 -I -B sortear_gold_q12_verificacion_mesa.py <repo> <salida.json> [--solo-controles]

Lee del repo, solo lectura, cada entrada igual a la de HEAD (si no, frena):
  - las preguntas de EV2: de cada una, solo su id y su TO;
  - del juez de A2.2 de N = 1: el orden (los ids opacos) y los agregados (de cada id opaco, solo `veredicto_pregunta` y `n_criterios`);
  - las metas de las sesiones de N = 1 (`resultados/n1/meta_*.json`), por las funciones congeladas del juez de A2.2 (`respuestas` e
    `id_opaco`), para recalcular el brazo de cada id opaco. No abre ninguna carpeta `desanonimizacion_SOLO_MESA/`.
Imprime solo cuentas que no dicen nada del juez. La salida es la clave: va a clave_para_despues/, en el paquete de la mesa.
--solo-controles: hace los controles de las entradas y del recálculo de los ids, sin sortear ni escribir nada.
"""
import hashlib
import json
import random
import subprocess
import sys
from pathlib import Path

SEMILLA = "gold-q12-verificacion-a22-v1"
N = 20
BRAZOS = ["kg", "fragmentos_bm25", "fragmentos_denso"]
CLASES = ["correcto", "parcial_o_incorrecto"]
A = "data/experiment/banco_mcp/a2_2"
ENTRADAS = {"preguntas": "data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json",
            "orden_juez": f"{A}/juez/n1/orden_juez_n1.json", "agregados": f"{A}/juez/n1/agregados_n1_ciego.json",
            "orden_corridas": f"{A}/orden_corridas_a2_2.json", "juez_a2_2": f"{A}/juez_a2_2.py", "comun_a2_2": f"{A}/comun_a2_2.py"}


def frena(m):
    raise SystemExit(f"FRENO: {m}")


def rng(uso: str) -> random.Random:
    """Un generador por uso, todos de la misma semilla: cambiar un paso no mueve los otros."""
    return random.Random(f"{SEMILLA}|{uso}")


def restos_mayores(pesos: dict, total: int, desempate: list) -> dict:
    """Cuotas enteras proporcionales a `pesos` que suman `total`; los empates de resto, en el orden de `desempate`."""
    s = sum(pesos.values())
    base = {k: (total * v) // s for k, v in pesos.items()}
    resto = {k: (total * v) % s for k, v in pesos.items()}
    falta = total - sum(base.values())
    for k in sorted(pesos, key=lambda k: (-resto[k], desempate.index(k)))[:falta]:
        base[k] += 1
    return base


def sortear(filas: list, to_de: dict) -> dict:
    """filas: las respuestas de la población (ya sin las que salen), cada una con id_opaco, qid, brazo, clase, id_sesion,
    sha256_respuesta y n_criterios. Devuelve la clave."""
    orden_b = BRAZOS[:]
    rng("brazo_6").shuffle(orden_b)
    cuota_b = {b: N // 3 + (1 if i < N % 3 else 0) for i, b in enumerate(orden_b)}
    celdas = {}
    for b in BRAZOS:
        n = {c: sum(1 for f in filas if f["brazo"] == b and f["clase"] == c) for c in CLASES}
        if sum(n.values()) < cuota_b[b]:
            frena(f"el brazo {b} tiene menos respuestas que su cuota")
        des = CLASES[:]
        rng(f"empate|{b}").shuffle(des)
        q = restos_mayores(n, cuota_b[b], des)
        for c in CLASES:
            otra = next(x for x in CLASES if x != c)
            if n[c] > 0 and q[c] == 0 and q[otra] > 1:
                q[c], q[otra] = 1, q[otra] - 1
        for c in CLASES:
            celdas[(b, c)] = q[c]
    elig = {k: sorted((f for f in filas if (f["brazo"], f["clase"]) == k), key=lambda f: f["id_opaco"]) for k in celdas}
    des = sorted(celdas)
    rng("celdas").shuffle(des)
    orden_c = sorted(celdas, key=lambda k: (len(elig[k]), des.index(k)))
    for k in orden_c:
        rng(f"permutacion|{k[0]}|{k[1]}").shuffle(elig[k])
    usadas, elegidas, pasadas = set(), [], []
    for k in orden_c:
        for _ in range(celdas[k]):
            ids = {e["id_opaco"] for e in elegidas}
            f = next((f for f in elig[k] if f["qid"] not in usadas and f["id_opaco"] not in ids), None)
            if f is None:
                otra = (k[0], next(x for x in CLASES if x != k[1]))
                f = next((f for f in elig[otra] if f["qid"] not in usadas and f["id_opaco"] not in ids), None)
                if f is None:
                    frena(f"la celda {k} y la otra clase de su brazo se quedaron sin respuestas con pregunta libre")
                pasadas.append({"de": f"{k[0]}|{k[1]}", "a": f"{otra[0]}|{otra[1]}"})
            usadas.add(f["qid"])
            elegidas.append(f)
    if len(elegidas) != N or len({f["qid"] for f in elegidas}) != N:
        frena("no salieron 20 respuestas con 20 preguntas distintas")
    if any(sum(1 for f in elegidas if f["brazo"] == b) != cuota_b[b] for b in BRAZOS):
        frena("las cuotas por brazo no se cumplen")
    rng("orden").shuffle(elegidas)
    fichas = [{"ficha": f"VG{i + 1:02d}", "id_opaco": f["id_opaco"], "id_pregunta": f["qid"], "to": to_de[f["qid"]],
               "brazo": f["brazo"], "clase": f["clase"], "id_sesion": f["id_sesion"], "sha256_respuesta": f["sha256_respuesta"],
               "n_criterios": f["n_criterios"]} for i, f in enumerate(elegidas)]
    por_to = {}
    for f in fichas:
        por_to[f["to"]] = por_to.get(f["to"], 0) + 1
    return {"semilla": SEMILLA, "cuota_por_brazo": cuota_b, "celdas": {f"{b}|{c}": v for (b, c), v in celdas.items()},
            "pasadas_a_la_otra_clase": pasadas, "fichas_por_to": por_to, "fichas": fichas}


def leer_del_repo(repo: Path) -> tuple:
    """Las entradas, cada una igual a la de HEAD; la población, con el brazo recalculado por el código congelado del juez."""
    sha = {}
    for k, p in ENTRADAS.items():
        b = (repo / p).read_bytes()
        h = subprocess.run(["git", "--no-optional-locks", "-C", str(repo), "show", f"HEAD:{p}"], capture_output=True)
        if h.returncode != 0 or h.stdout != b:
            frena(f"{p} no es el de HEAD (¿falta el 193?)")
        sha[k] = hashlib.sha256(b).hexdigest()
    sys.path.insert(0, str(repo / A))
    import juez_a2_2 as JZ  # noqa: E402  (congelado: solo import)
    preguntas = json.loads((repo / ENTRADAS["preguntas"]).read_text(encoding="utf-8"))["preguntas"]
    to_de = {p["id"]: p["to"] for p in preguntas}
    orden = json.loads((repo / ENTRADAS["orden_corridas"]).read_text(encoding="utf-8"))
    resps, faltan = JZ.respuestas("n1", repo / A / "resultados/n1", orden, None)
    rec = {}
    for r in resps:
        s = JZ.K.sha256_texto(r["respuesta"])
        rec[JZ.id_opaco(r["qid"], r["brazo"], r["rep"], s)] = {"qid": r["qid"], "brazo": r["brazo"], "id_sesion": r["id_sesion"],
                                                                "sha256_respuesta": s}
    ids_juez = json.loads((repo / ENTRADAS["orden_juez"]).read_text(encoding="utf-8"))["ids_opacos_en_orden"]
    if set(rec) != set(ids_juez) or len(rec) != len(ids_juez):
        frena("los ids recalculados no son los del orden del juez")
    agr = {a["id_opaco"]: a for a in json.loads((repo / ENTRADAS["agregados"]).read_text(encoding="utf-8"))["agregados"]}
    if not set(agr) <= set(rec):
        frena("hay agregados con un id que no es de N = 1")
    filas = []
    for i, a in agr.items():
        v = a["veredicto_pregunta"]
        if v == "requiere_adjudicacion":
            continue
        if v not in ("correcto", "parcial", "incorrecto"):
            frena("un veredicto de pregunta fuera del dominio")
        filas.append(rec[i] | {"id_opaco": i, "clase": "correcto" if v == "correcto" else "parcial_o_incorrecto",
                               "n_criterios": a["n_criterios"]})
    if {f["brazo"] for f in filas} != set(BRAZOS) or not set(rec[i]["qid"] for i in rec) <= set(to_de):
        frena("los brazos o las preguntas no son los esperados")
    return sha, filas, to_de, len(rec), len(faltan), len(agr)


def main() -> None:
    repo, salida = Path(sys.argv[1]), Path(sys.argv[2])
    solo = "--solo-controles" in sys.argv[3:]
    if salida.exists():
        frena("la clave ya existe: el sorteo corre una sola vez")
    sha, filas, to_de, n_ids, n_faltan, n_agr = leer_del_repo(repo)
    print(f"controles: las entradas son las de HEAD; {n_ids} ids recalculados con el código del juez, los de su orden; "
          f"{n_faltan} sesión sin respuesta; {n_agr} con juicio completo")
    if solo:
        print("solo controles: no sorteé ni escribí nada")
        return
    out = sortear(filas, to_de) | {"sha256_entradas": sha, "poblacion_con_juicio": n_agr, "poblacion": len(filas),
                                   "salen_por_requiere_adjudicacion": n_agr - len(filas)}
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    por_b = {b: sum(1 for f in out["fichas"] if f["brazo"] == b) for b in BRAZOS}
    print(f"sorteo hecho: {len(out['fichas'])} fichas, {len({f['id_pregunta'] for f in out['fichas']})} preguntas distintas; "
          f"por brazo {sorted(por_b.values(), reverse=True)}; criterios: {sum(f['n_criterios'] for f in out['fichas'])}")


if __name__ == "__main__":
    main()
