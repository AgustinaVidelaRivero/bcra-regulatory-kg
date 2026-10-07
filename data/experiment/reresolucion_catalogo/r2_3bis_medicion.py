"""U-RERESOL-CAT, R2-3 bis — regla general del padre del propuesto en los documentos sin alcance (USD 0, sin API ni
Neo4j). Corre desde la raíz de una COPIA del repo y solo escribe en --out.

  simulacion --manifiesto M --entrada E --e0-r2 D --out J [--sin-cola]
      Corre la cadena r2 de M sobre el crudo guardado, en memoria (ensamblar_tanda0.correr_cadena_r2 con las
      redirecciones del ensamblado, sin escribir nada), y guarda el grafo y el registro tal como llegan a
      `normalizar_propuestos_r2b`. Sobre ese estado corre solo la normalización: con el rol_por_to de la release (control:
      el resumen de la cadena) y con cap, ext y los dos marcados en memoria como documentos sin alcance (fuera de
      rol_por_to). Reporta, por variante, las marcas y su detalle, los propuestos que el paso c resolvía con el rol y
      adónde van, `sin_rol_de_alcance` y S19 sobre los Sujetos del grafo normalizado.

  controles --r23 R --bis B --suite S --out J
      R: las cadenas de diez r2b con el código de R2-3 (r2b_diez y r2b_sincola_diez); B: las seis cadenas de
      controles_r2_1.sh con el código de R2-3 bis; S: la fase suite de controles_r2_1.sh (viejo = HEAD, nuevo = R2-3 bis).
      El sha256 de cada grafo contra la referencia (r2b de diez: el de R2-3, de salidas/r2_3_controles.json; r2a: la
      cadena del código; los demás r2b: los sellados), r2/ de R2-3 contra R2-3 bis en las dos de diez, las shapes del
      perfil r2 y el resumen de los propuestos en las dos de diez, la suite HEAD contra R2-3 bis y la fixture.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reresolucion_catalogo/r2_3bis_medicion.py simulacion \\
      --manifiesto data/experiment/reextraccion_v2/manifiestos/tanda0_ens_diez_r2b.json \\
      --entrada data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b \\
      --e0-r2 data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b --out <json>
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reresolucion_catalogo/r2_3bis_medicion.py controles \\
      --r23 <dir> --bis <dir> --suite <dir> --out <json>
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import r2_3_medicion as R3              # noqa: E402  (por él, reresolver_catalogo, el ensamblador y r1_e4)

RR, ENS, E4, C, RAIZ = R3.RR, R3.RR.ENS, R3.E4, R3.RR.C, R3.RAIZ
MARCAS = ("padre_desde_sugerencia_modelo", "padre_por_defecto_generico", "padre_por_defecto", "sin_rol_de_alcance")
VARIANTES = OrderedDict([("release", ()), ("cap_sin_alcance", ("cap",)), ("ext_sin_alcance", ("ext",)),
                         ("cap_y_ext_sin_alcance", ("cap", "ext"))])


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


# --------------------------------------------------------------------------------------------------------------- #
# simulacion                                                                                                       #
# --------------------------------------------------------------------------------------------------------------- #
def capturar(a) -> tuple:
    """El grafo, el registro, los renombres y el catálogo con que la cadena llama a normalizar_propuestos_r2b (copias
    profundas, antes de la llamada), y el resumen que devuelve la llamada real."""
    man = ENS.MC.cargar(a.manifiesto)
    perfil = ENS.perfil_e1.perfil(man.perfil_e1)
    M = E4.modulo_modelos_r2()
    cat = E4.catalogo_r2()
    plan = ENS.plan_redirecciones_r2(man, perfil, Path(a.entrada), Path(a.out).parent / "_simulacion_r2", cat, M)
    original = ENS.normalizar_propuestos_r2b
    capt = {}

    def envoltura(kg, registro, renombres, cat_):
        if not capt:
            capt.update(kg=copy.deepcopy(kg), registro=copy.deepcopy(registro), renombres=copy.deepcopy(renombres),
                        cat=cat_)
        r = original(kg, registro, renombres, cat_)
        capt.setdefault("resumen_cadena", {k: v for k, v in r["resumen"].items() if k != "detalle"})
        return r
    ENS.normalizar_propuestos_r2b = envoltura
    try:
        with ENS.redirigido(plan):
            res = ENS.correr_cadena_r2(man, perfil, None, None, Path(a.e0_r2), con_cola=not a.sin_cola)
    finally:
        ENS.normalizar_propuestos_r2b = original
    return man, plan, capt, res["sha256"]


def simulacion(a) -> dict:
    sys.path.insert(0, str(RAIZ / "scripts"))
    import shapes_validator as SV      # noqa: PLC0415  (importado, no editado)
    man, plan, capt, sha_kg = capturar(a)
    ids19, defecto = SV.cargar_ids_s19_r2()
    cat = capt["cat"]
    filas_cuarentena = Counter((f["motivo"], "con sugerencia" if f.get("sujeto_id_modelo") else "sin sugerencia")
                               for f in capt["registro"] if f["estado"] == "cuarentena")
    out = OrderedDict([("manifiesto", RR.ruta(a.manifiesto)), ("con_cola", not a.sin_cola), ("sha256_kg_de_la_cadena", sha_kg),
                       ("resumen_de_la_normalizacion_en_la_cadena", capt["resumen_cadena"]),
                       ("registro_en_cuarentena_antes_de_normalizar", [[m, s, n] for (m, s), n in sorted(filas_cuarentena.items())]),
                       ("variantes", OrderedDict())])
    referencia = None
    for nombre, sin_alcance in VARIANTES.items():
        cat_v = dict(cat)
        with ENS.redirigido(plan):
            fuera = {C.archivo_de_to(to) for to in sin_alcance}
            cat_v["rol_por_to"] = {k: v for k, v in cat["rol_por_to"].items() if k not in fuera}
            kg, reg = copy.deepcopy(capt["kg"]), copy.deepcopy(capt["registro"])
            r = ENS.normalizar_propuestos_r2b(kg, reg, copy.deepcopy(capt["renombres"]), cat_v)
        det = r["resumen"]["detalle"]
        props = {n["id"]: n["properties"] for n in kg["nodes"] if n["type"] == "Sujeto"
                 and n["properties"].get("nivel") == "propuesto"}
        if referencia is None:
            referencia = {x["id"]: x for x in det["padre_por_defecto"]}
        destino = OrderedDict()
        for i, x in sorted(referencia.items()):
            p = props.get(i, {})
            marca = next((m for m in MARCAS[:3] if p.get(m) == "true"), None)
            filas = [f for f in reg if f.get("id_nodo") == i and f["estado"] == "cuarentena"]
            destino[i] = OrderedDict([("tos", x["tos"]), ("rol_con_alcance", x["padre_sugerido"]),
                                      ("padre_sugerido", p.get("padre_sugerido")), ("marca", marca),
                                      ("padre_sugerido_instancia", p.get("padre_sugerido_instancia")),
                                      ("motivos", sorted(Counter(f["motivo"] for f in filas).items())),
                                      ("sugerencias", sorted({str(f.get("sujeto_id_modelo")) for f in filas}))])
        s19 = SV.shape_s19_catalogo(kg["nodes"], ids19, defecto)
        out["variantes"][nombre] = OrderedDict([
            ("documentos_sin_alcance_marcados", list(sin_alcance)),
            ("resumen", {k: v for k, v in r["resumen"].items() if k != "detalle"}),
            ("detalle", {k: det[k] for k in MARCAS}),
            ("propuestos_del_paso_c_con_alcance", destino),
            ("marcas_de_esos_propuestos", dict(sorted(Counter(str(v["marca"]) for v in destino.values()).items()))),
            ("S19", [s19["result"], s19["conteos"]])])
    out["release_reproduce_la_cadena"] = out["variantes"]["release"]["resumen"] == capt["resumen_cadena"]
    return out


# --------------------------------------------------------------------------------------------------------------- #
# controles                                                                                                        #
# --------------------------------------------------------------------------------------------------------------- #
def controles(a) -> dict:
    Rd, B, S = Path(a.r23), Path(a.bis), Path(a.suite)
    r23 = json.loads((AQUI / "salidas" / "r2_3_controles.json").read_text(encoding="utf-8"))["cadenas"]
    out = OrderedDict([("referencia", "r2b diez y sin cola diez: el grafo de R2-3 (salidas/r2_3_controles.json, "
                                      "sha256_nuevo); r2a: la cadena del código; r2b desarrollo: los sellados")])
    cad = OrderedDict()
    for n, sellado in R3.CADENAS.items():
        ref = r23[n]["sha256_nuevo"] if n in R3.DIEZ_R2B else R3.REFERENCIA_R2A.get(n, sha(RAIZ / R3.T / sellado / "r2" / "kg.json"))
        sb = sha(B / n / "r2" / "kg.json")
        ent = OrderedDict([("sha256_referencia", ref), ("sha256_r2_3bis", sb), ("igual_a_la_referencia", sb == ref),
                           ("rc", R3.lineas(B / f"consola_{n}.txt")[-1])])
        if n in R3.DIEZ_R2B:
            c = RC1.comparar_dir(Rd / n / "r2", B / n / "r2", ((str(Rd), "<SALIDA>"), (str(B), "<SALIDA>")))
            ent["sha256_r2_3_corrida_aqui"] = sha(Rd / n / "r2" / "kg.json")
            ent["r2_de_r2_3_contra_r2_3bis"] = OrderedDict([("iguales", c["iguales"]),
                                                            ("iguales_con_la_ruta_normalizada", c["iguales_con_ruta_normalizada"]),
                                                            ("distintos", c["distintos"]),
                                                            ("solo_en_una", c["solo_en_a"] + c["solo_en_b"])])
            sh = R3.shapes_de(B / n / "r2")
            pr = R3.propuestos_r2b(R3.reporte(B / n / "r2"))
            ent["shapes"] = OrderedDict([("veredicto", sh["veredicto"]), ("bloqueantes_en_fail", sh["bloqueantes_en_fail"]),
                                         ("bloqueantes_no_computables", sh["bloqueantes_no_computables"]),
                                         ("S19", R3.tabla_shapes(sh)["S19"][0::2])])
            ent["resumen_de_los_propuestos"] = {k: v for k, v in pr.items() if k != "detalle"}
            ent["motivos_por_marca"] = {m: [[x["id"], x.get("motivos")] for x in pr["detalle"].get(m, [])]
                                        for m in MARCAS[:2]}
        cad[n] = ent
    out["cadenas"] = cad
    fx = R3.FIXTURE.read_text(encoding="utf-8")
    out["fixture_de_la_suite"] = {n: {"sha256_r2_3bis_en_la_fixture": cad[n]["sha256_r2_3bis"] in fx} for n in R3.DIEZ_R2B}
    out["suite_head_contra_r2_3bis"] = OrderedDict(
        (p.stem.replace("suite_viejo_", ""), {
            "json_igual": p.read_bytes() == p.with_name(p.name.replace("viejo", "nuevo")).read_bytes(),
            "md_igual": p.with_suffix(".md").read_bytes() == p.with_name(p.name.replace("viejo", "nuevo")).with_suffix(".md").read_bytes(),
            "rc": [R3.lineas(S / f"consola_{p.stem}.txt")[-1], R3.lineas(S / f"consola_{p.stem.replace('viejo', 'nuevo')}.txt")[-1]],
            "resumen": R3.cargar(p).get("resumen")})
        for p in sorted(S.glob("suite_viejo_*.json")))
    return out


RC1 = R3.RC1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("simulacion")
    s.add_argument("--manifiesto", type=Path, required=True)
    s.add_argument("--entrada", type=Path, required=True)
    s.add_argument("--e0-r2", dest="e0_r2", type=Path, required=True)
    s.add_argument("--sin-cola", action="store_true")
    s.add_argument("--out", type=Path, required=True)
    c = sub.add_parser("controles")
    c.add_argument("--r23", type=Path, required=True)
    c.add_argument("--bis", type=Path, required=True)
    c.add_argument("--suite", type=Path, required=True)
    c.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    obj = simulacion(a) if a.cmd == "simulacion" else controles(a)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{sha(a.out)}  {RR.ruta(a.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
