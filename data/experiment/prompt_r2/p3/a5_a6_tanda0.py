"""
a5_a6_tanda0.py — U-PROMPT-R2, P3, agregado de la nota del 04/10/2026 al mandato (USD 0, sin API).

A6. Con el crudo guardado de la tanda 0 como referencia, cuántos elementos cambian de estado con cada cambio y si
alguno se pierde. Tres poblaciones:
  - primer intento de los diez TOs (extracciones_e1_compact.jsonl);
  - población final de los diez TOs y de desarrollo (pro, cla, ric, cap, ext): el crudo que lee la cadena r2
    (runner_corpus.entrada_r2 con el perfil v3_b54: el intento que E3 aceptó; en la cola humana, el primero).
Por elemento (entidad o relación del crudo, por su índice):
  - E3 vio (sellado): lo acepta validador_e1 con el perfil v3_b54 (reproduce la validación guardada);
  - r2a: lo admite validador_r2 con la forma v3, con su marca no_verificada_e3 por la firma (los grafos sellados);
  - el crudo leído en la forma r2 (validador_r2.desde_v3) pasa por validador_e1 con el perfil r2b de P2
    (`--validador-e1-p2`, el archivo de 20b7f60) y por el de P3 (con A1): lo que E3 vería;
  - validador_r2 con la forma r2, sin filtro y con vistos_e3 (A2): lo que entra.
Límite declarado: E3 no se vuelve a correr (USD 0). Si E3 viera más elementos, su veredicto y sus reintentos podrían
cambiar; la tabla cuenta qué le llegaría, no qué aceptaría.

A5. Unidades que E3 no terminó (ratchet agotado y veredicto inutilizable: la cola humana). Decisión de la autora del
04/10/2026: entran al grafo marcadas, como hoy, y son la excepción explícita a «cero elementos sin verificar», contada
aparte. En los dos grafos r2a sellados: unidades por estado, nodos y aristas con alguna procedencia de la cola (con la
marca), los que solo tienen procedencia de la cola, y las aristas derivadas que tocan un nodo de la cola sin la marca.
En la simulación r2b de A6, cuántos de sus elementos entran (contados aparte).

Escribe solo en --salida (a5_a6_tanda0.json y .md). Sobre una copia del repo (CLAUDE.md §4, regla l).

Uso (desde la raíz de la copia):
  git -C <repo> show 20b7f60:data/experiment/reextraccion_v2/e1_extractor/validador_e1.py > DIR/validador_e1_p2.py
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3/a5_a6_tanda0.py \
      --validador-e1-p2 DIR/validador_e1_p2.py --salida DIR
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import re
import sys
from collections import Counter
from pathlib import Path

P3 = Path(__file__).resolve().parent
REPO = P3.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2"):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REX))
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
import manifiesto_corpus as MC  # noqa: E402
import comun_e1  # noqa: E402
import perfil_e1  # noqa: E402
import validador_e1  # noqa: E402
import runner_corpus as RC  # noqa: E402
import validador_r2 as V  # noqa: E402

SALIDA_T0 = REX / "corpus_tanda0" / "salida_dirigida"
DIEZ = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
DESARROLLO = ("pro", "cla", "ric", "cap", "ext")
KG_R2A = {"diez": REX / "corpus_tanda0" / "ens_diez_r2a" / "r2" / "kg.json",
          "desarrollo": REX / "corpus_tanda0" / "ens_desarrollo_r2a" / "r2" / "kg.json"}


def aceptados(rechazos: list, n_ent: int, n_rel: int, excluir: list | None = None) -> set:
    """(e|r, índice) aceptados: todos menos los rechazados (por el «entities[i]» o «relations[i]» del detalle,
    como prueba_crudo_t0._indices) y menos los excluidos por no haber pasado por E3."""
    ent_r, rel_r = set(), set()
    for r in rechazos or []:
        if r.get("nivel") == "chunk":
            return set()
        m = re.match(r"(entities|relations)\[(\d+)\]", r.get("detalle") or "")
        if m:
            (ent_r if m.group(1) == "entities" else rel_r).add(int(m.group(2)))
    for x in excluir or []:
        m = re.match(r"(entities|relations)\[(\d+)\]", x["elemento"])
        (ent_r if m.group(1) == "entities" else rel_r).add(int(m.group(2)))
    return {("e", i) for i in range(n_ent) if i not in ent_r} | {("r", i) for i in range(n_rel) if i not in rel_r}


def largos(ti) -> tuple[int, int]:
    if isinstance(ti, str):
        try:
            ti = json.loads(ti)
        except json.JSONDecodeError:
            return 0, 0
    if not isinstance(ti, dict):
        return 0, 0
    e, r = V._coerce_lista(ti.get("entities")), V._coerce_lista(ti.get("relations"))
    return (0, 0) if e is None or r is None else (len(e), len(r))


def cargar_modulo(nombre: str, ruta: Path):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nombre] = m
    spec.loader.exec_module(m)
    return m


def poblaciones() -> dict:
    """{nombre: [(chunk_id, tool_input, chunk)]}."""
    man = MC.cargar(MC.MANIFIESTOS_DIR / "tanda0_10tos.json")
    RC.configurar(man)
    out = {"primer_intento_diez": [], "final_diez": [], "final_desarrollo": []}
    for to in DIEZ:
        tdir = SALIDA_T0 / to
        chunks = RC.chunks_con_partes(RC.chunks_sin_ids_repetidos(
            comun_e1.cargar_chunks((to,), e0_dir=man.e0_salida), to), tdir)
        por_id = {c["id"]: c for c in chunks}
        for linea in (tdir / "extracciones_e1_compact.jsonl").read_text(encoding="utf-8").splitlines():
            r = json.loads(linea)
            if r.get("tool_input_crudo") is not None and r["chunk_id"] in por_id:
                out["primer_intento_diez"].append((r["chunk_id"], r["tool_input_crudo"], por_id[r["chunk_id"]]))
        capt = []
        RC.entrada_r2(to, tdir, chunks, RC.PERFIL, lambda ti, c: capt.append((c["id"], ti, c)) or {})
        out["final_diez"] += capt
        if to in DESARROLLO:
            out["final_desarrollo"] += capt
    return out


def cola_de(tos) -> dict:
    """chunk_id → estado de E3 de las unidades sin validación final (la cola humana)."""
    out = {}
    for to in tos:
        fin = {}
        for r in map(json.loads, (SALIDA_T0 / to / "finales.jsonl").read_text(encoding="utf-8").splitlines()):
            fin[r["chunk_id"]] = r
        out.update({k: r["estado"] for k, r in fin.items() if r.get("validacion_final") is None})
    return out


def a6(pobl: list, e1_p2, esq_v3, esq_r2, cola: dict | None = None) -> dict:
    pol = V.politica_default()
    c = Counter()
    ejemplos: dict[str, list] = {}

    def anotar(clave: str, cid: str, x: tuple) -> None:
        c[clave] += 1
        if len(ejemplos.setdefault(clave, [])) < 12:
            ejemplos[clave].append(f"{cid} {'entities' if x[0] == 'e' else 'relations'}[{x[1]}]")
    for cid, ti, ch in pobl:
        ne, nr = largos(ti)
        s_e3 = aceptados(validador_e1.validar_salida(copy.deepcopy(ti), ch, esquema=esq_v3).as_dict()["rechazos"],
                         ne, nr)
        res_r2a = V.validar(copy.deepcopy(ti), ch, pol, forma="v3")
        s_r2a = aceptados(res_r2a["rechazos"], ne, nr)
        marca = {("r", x["indice_crudo"]) for x in res_r2a["relaciones"] if x["no_verificada_e3"]}
        ti_r2, _ = V.desde_v3(copy.deepcopy(ti))
        s_p2 = aceptados(e1_p2.validar_salida(copy.deepcopy(ti_r2), ch, esquema=esq_r2).as_dict()["rechazos"], ne, nr)
        val_a1 = validador_e1.validar_salida(copy.deepcopy(ti_r2), ch, esquema=esq_r2).as_dict()
        s_a1 = aceptados(val_a1["rechazos"], ne, nr)
        vistos = RC.vistos_por_e3(val_a1)
        libre = V.validar(copy.deepcopy(ti_r2), ch, pol, forma="r2")
        s_libre = aceptados(libre["rechazos"], ne, nr)
        filtrado = V.validar(copy.deepcopy(ti_r2), ch, pol, forma="r2", vistos_e3=vistos)
        s_a2 = aceptados(filtrado["rechazos"], ne, nr, filtrado.get("no_vistos_e3"))
        c["control_lectura_r2_igual_a_v3"] += s_libre == s_r2a
        c["unidades"] += 1
        for x in sorted(s_r2a - s_e3):
            tipo = "relacion" if x[0] == "r" else "entidad"
            anotar(f"r2a_sin_E3:{tipo}:{'con_marca' if x in marca else 'sin_marca'}", cid, x)
            if x in s_p2:
                anotar("visto_por_E3_con_el_esquema_r2b_de_P2", cid, x)
            elif x in s_a1:
                anotar("visto_por_E3_con_A1", cid, x)
            else:
                anotar("sigue_sin_E3_tras_A1", cid, x)
        for x in sorted(s_libre - s_a1):
            anotar("A2_se_pierde:validador_r2_lo_admitiria_y_E3_no_lo_vio", cid, x)
        for x in sorted(s_a1 - s_libre):
            anotar("A2_E3_lo_vio_y_validador_r2_lo_rechaza", cid, x)
        for x in sorted(s_a2 - s_a1):
            anotar("A2_entra_sin_haber_pasado_por_E3", cid, x)
        for x in sorted(marca):
            anotar("A3_marca_por_firma_que_se_retira", cid, x)
            if x in s_a2:
                anotar("A3_la_relacion_marcada_entra_sin_marca", cid, x)
        c["A3_relaciones_con_no_verificada_e3_tras_A2_A3"] += sum(1 for x in filtrado["relaciones"]
                                                                   if x["no_verificada_e3"])
        c["A3_entidades_sin_paso_por_e3_tras_A2_A3"] += sum(1 for x in filtrado["entidades"]
                                                             if x.get("paso_por_e3") is not True)
        c["admitidos_r2a:entidades"] += sum(1 for x in s_r2a if x[0] == "e")
        c["admitidos_r2a:relaciones"] += sum(1 for x in s_r2a if x[0] == "r")
        if cola is not None and cid in cola:
            c["A5_cola_humana:unidades"] += 1
            c["A5_cola_humana:entidades_que_entran"] += sum(1 for x in s_a2 if x[0] == "e")
            c["A5_cola_humana:relaciones_que_entran"] += sum(1 for x in s_a2 if x[0] == "r")
            c["A5_cola_humana:relaciones_con_no_verificada_e3"] += sum(1 for x in filtrado["relaciones"]
                                                                       if x["no_verificada_e3"])
        c["admitidos_con_A2:entidades"] += sum(1 for x in s_a2 if x[0] == "e")
        c["admitidos_con_A2:relaciones"] += sum(1 for x in s_a2 if x[0] == "r")
    c["r2a_sin_E3:total"] = sum(v for k, v in c.items() if k.startswith("r2a_sin_E3:"))
    return {"conteos": dict(sorted(c.items())), "ejemplos": dict(sorted(ejemplos.items()))}


def a5() -> dict:
    out = {}
    for nombre, ruta in KG_R2A.items():
        b = ruta.read_bytes()
        kg = json.loads(b)
        tos = DIEZ if nombre == "diez" else DESARROLLO
        estados = cola_de(tos)
        cola = set(estados)

        def chunks_de(o):
            return {p.get("chunk_id") for p in o.get("provenances", [])}
        res = {"kg": str(ruta.relative_to(REPO)), "sha256": hashlib.sha256(b).hexdigest(),
               "unidades_en_cola": len(cola), "unidades_por_estado": dict(sorted(Counter(estados.values()).items()))}
        for col in ("nodes", "edges"):
            marc = [o for o in kg[col] if o.get("properties", {}).get("cola_humana") == "true"]
            solo = [o for o in marc if chunks_de(o) and chunks_de(o) <= cola]
            res[col] = {"marcados": len(marc), "solo_de_la_cola": len(solo),
                        "marcados_por_tipo" if col == "nodes" else "marcados_por_relacion": dict(sorted(Counter(
                            o["type"] if col == "nodes" else o["relation"] for o in marc).items())),
                        "solo_de_la_cola_por_tipo" if col == "nodes" else "solo_de_la_cola_por_relacion": dict(sorted(
                            Counter(o["type"] if col == "nodes" else o["relation"] for o in solo).items()))}
        ids_solo = {o["id"] for o in kg["nodes"] if o.get("properties", {}).get("cola_humana") == "true"
                    and chunks_de(o) and chunks_de(o) <= cola}
        res["edges"]["que_tocan_un_nodo_solo_de_la_cola"] = sum(
            1 for e in kg["edges"] if e["source"] in ids_solo or e["target"] in ids_solo)
        sin_marca = [e for e in kg["edges"] if (e["source"] in ids_solo or e["target"] in ids_solo)
                     and e.get("properties", {}).get("cola_humana") != "true"]
        res["edges"]["derivadas_sin_la_marca_que_tocan_un_nodo_solo_de_la_cola"] = dict(sorted(Counter(
            f"{e['relation']}|{e.get('rol_fuente')}" for e in sin_marca).items()))
        out[nombre] = res
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--validador-e1-p2", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    e1_p2 = cargar_modulo("validador_e1_p2", a.validador_e1_p2)
    esq_v3, esq_r2 = perfil_e1.perfil("v3_b54").esquema, perfil_e1.perfil("r2b").esquema
    pob = poblaciones()
    res = {"comando": "data/experiment/prompt_r2/p3/a5_a6_tanda0.py --validador-e1-p2 DIR/validador_e1_p2.py "
                      "--salida DIR",
           "validador_e1_p2_sha256": hashlib.sha256(a.validador_e1_p2.read_bytes()).hexdigest(),
           "a6": {k: a6(v, e1_p2, esq_v3, esq_r2, None if k.startswith("primer") else cola_de(DIEZ))
                  for k, v in pob.items()}, "a5": a5()}
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "a5_a6_tanda0.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for k, v in res["a6"].items():
        print(k, json.dumps(v["conteos"], ensure_ascii=False))
    print("a5", json.dumps(res["a5"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
