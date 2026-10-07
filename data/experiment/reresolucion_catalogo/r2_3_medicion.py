"""U-RERESOL-CAT, R2-3 — controles de la salida de S19 y de la parte A en el runner (USD 0, sin API ni Neo4j). Corre
desde la raíz de una COPIA del repo y solo escribe en --trabajo y en --out.

  seco --etiqueta E --cadena D --trabajo W --out J
      Corrida en seco de `runner_corpus.cerrar_e2_r2` sobre docvig con lo guardado de la tanda 0
      (corpus_tanda0/salida_r2b/docvig, copiado a W/salida_r2b/docvig; nada se escribe en la salida guardada). Corre
      en un proceso aparte con el directorio del runner como sys.path[0], como `python runner_corpus.py` (CLAUDE.md
      §4.l: el camino de imports del runner, sin arreglar el sys.path por fuera), con el manifiesto de la extracción
      (manifiestos/tanda0_10tos_r2b.json) y PERFIL_R2 como lo fija `main`. Compara su resolucion_sujetos.jsonl con el
      del ensamblado r2b de D (D = <cadena r2b diez>/r2, por_to/docvig/): las 4 filas de docvig::3.4 (relaciones 5,
      6, 7 y 9), byte a byte, y el archivo entero; el registro de no mapeados, entero; y cada archivo del runner con el
      guardado (las líneas que cambian y la diferencia del grafo del TO). E es la etiqueta del código de la copia
      (head o nuevo).

  controles --head H --nuevo N --out J [--nuevo2 N2] [--suite S]
      H y N: las seis cadenas de controles_r2_1.sh (fase cadenas) con el código de HEAD y con el nuevo; N2, una
      segunda corrida de las dos de diez con el código nuevo (doble corrida); S, el directorio de la fase suite (viejo
      y nuevo). Para cada cadena: el sha256 del grafo contra el sellado y contra HEAD, y los archivos de r2/ de HEAD
      contra los nuevos (los distintos, con las claves del reporte que cambian). En r2b diez y sin cola diez: la
      diferencia del grafo nuevo contra el sellado y contra HEAD (nodos, aristas y procedencias de sujeto), el
      propuesto de la parte A antes y después, la arista padre_sugerido, el resumen de los propuestos del reporte y
      las shapes del perfil r2 (sellado, HEAD y nuevo: veredicto, bloqueantes en FAIL y las shapes cuyas cifras o
      resultado cambian). Más: los propuestos que reciben el rol de alcance por defecto (paso c) con el motivo de sus
      filas, que en un documento sin alcance quedarían sin padre (no son de la parte A), y los sha nuevos en la
      fixture de la suite.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reresolucion_catalogo/r2_3_medicion.py seco \\
      --etiqueta nuevo --cadena <dir>/r2b_diez/r2 --trabajo <dir> --out <json>
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reresolucion_catalogo/r2_3_medicion.py controles \\
      --head <dir> --nuevo <dir> [--nuevo2 <dir>] [--suite <dir>] --out <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import reresolver_catalogo as RR        # noqa: E402  (por él, el ensamblador y r1_e4)
import r2_1_resumen_controles as RC1    # noqa: E402  (comparar_dir)

E4, RAIZ = RR.E4, RR.RAIZ
X = "data/experiment/reextraccion_v2"
T = f"{X}/corpus_tanda0"
CORPUS_V2 = RAIZ / X / "corpus_v2"
MANIFIESTO_RUNNER = RAIZ / X / "manifiestos" / "tanda0_10tos_r2b.json"
E0_R2B = RAIZ / X / "e0_chunking" / "salida_tanda0_r2b"
GUARDADO_DOCVIG = RAIZ / T / "salida_r2b" / "docvig"
CADENAS = OrderedDict([("r2a_diez", "ens_diez_r2a"), ("r2a_desarrollo", "ens_desarrollo_r2a"),
                       ("r2b_diez", "ens_diez_r2b"), ("r2b_desarrollo", "ens_desarrollo_r2b"),
                       ("r2b_sincola_diez", "ens_diez_r2b_sincola"),
                       ("r2b_sincola_desarrollo", "ens_desarrollo_r2b_sincola")])
DIEZ_R2B = ("r2b_diez", "r2b_sincola_diez")
# la cadena r2a del código (decisión e de la nota del 04/10/2026 al mandato; controles de R2-1 y R2-2)
REFERENCIA_R2A = {"r2a_diez": "70d51e429b0e2cc1aafa697e32bc83462d371dfdd5edafb34e92fe4f7be45bdd",
                  "r2a_desarrollo": "fa4c1043d859081e49dce6cb940a9f5d4c09fc6d449efb85355f95312257178a"}
PROPUESTO = "Sujeto_propuesto_las_entidades"
FILAS_3_4 = (5, 6, 7, 9)
FIXTURE = RAIZ / "scripts" / "regression_kg_esperado.json"
MARCAS = ("padre_desde_sugerencia_modelo", "padre_por_defecto_generico", "padre_por_defecto", "sin_rol_de_alcance")


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def lineas(p) -> list[str]:
    return Path(p).read_text(encoding="utf-8").splitlines()


def cargar(p) -> dict:
    return json.loads(Path(p).read_text(encoding="utf-8"))


# --------------------------------------------------------------------------------------------------------------- #
# seco: cerrar_e2_r2 del runner sobre docvig                                                                       #
# --------------------------------------------------------------------------------------------------------------- #
CODIGO_SECO = r"""
import json, sys
from pathlib import Path
import runner_corpus as RC
RC.configurar(RC.manifiesto_corpus.cargar(Path(sys.argv[1])))
RC.PERFIL_R2 = RC.perfil_forma_r2(RC.PERFIL)
rep = RC.cerrar_e2_r2("docvig", Path(sys.argv[2]))
print("@@" + json.dumps({"sys_path": sys.path, "runner": RC.__file__, "perfil": RC.PERFIL.nombre,
                         "perfil_forma_r2": RC.perfil_forma_r2(RC.PERFIL), "PERFIL_R2": RC.PERFIL_R2,
                         "e0_dir": str(RC.E0_DIR), "resolucion_sujetos": rep["resolucion_sujetos"],
                         "sha256_grafo": rep["sha256_grafo"]}))
"""


def rel(p: str) -> str:
    """Una entrada del sys.path del proceso hijo, relativa a la raíz de la copia o marcada como del intérprete."""
    if p == "":
        return "<directorio de trabajo>"
    try:
        return str(Path(p).resolve().relative_to(RAIZ))
    except ValueError:
        return "<intérprete>"


def filas_3_4(ls: list[str]) -> list[str]:
    out = []
    for x in ls:
        f = json.loads(x)
        if f["chunk_id"] == "docvig::3.4" and f["indice_relacion"] in FILAS_3_4:
            out.append(x)
    return out


def seco(a) -> dict:
    W = Path(a.trabajo).resolve()      # el proceso hijo corre en el directorio del runner
    tdir = W / "salida_r2b" / "docvig"
    if tdir.exists():
        shutil.rmtree(tdir)
    shutil.copytree(GUARDADO_DOCVIG, tdir)
    env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    r = subprocess.run([sys.executable, "-B", "-c", CODIGO_SECO, str(MANIFIESTO_RUNNER), str(W / "salida_r2b")],
                       cwd=CORPUS_V2, env=env, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"cerrar_e2_r2 falló (código {r.returncode}):\n{r.stderr[-3000:]}")
    hijo = json.loads(next(x for x in r.stdout.splitlines() if x.startswith("@@"))[2:])
    cad = Path(a.cadena) / "por_to" / "docvig"
    res_run, res_cad = lineas(tdir / "resolucion_sujetos.jsonl"), lineas(cad / "resolucion_sujetos.jsonl")
    reg_run, reg_cad = lineas(tdir / "no_mapeados_sujetos.jsonl"), lineas(cad / "no_mapeados_sujetos.jsonl")
    f_run, f_cad = filas_3_4(res_run), filas_3_4(res_cad)
    archivos = OrderedDict()
    for p in sorted(x for x in tdir.iterdir() if x.is_file()):
        g = GUARDADO_DOCVIG / p.name
        ent = OrderedDict([("igual_al_guardado", p.read_bytes() == g.read_bytes())])
        if not ent["igual_al_guardado"] and p.suffix == ".jsonl":
            a0, a1 = Counter(lineas(g)), Counter(lineas(p))
            ent["lineas"] = [sum(a0.values()), sum(a1.values())]
            ent["lineas_solo_en_el_guardado"] = sum((a0 - a1).values())
            ent["lineas_solo_en_el_runner"] = sum((a1 - a0).values())
            ent["unidades_de_esas_lineas"] = sorted({json.loads(x)["chunk_id"] for x in (a0 - a1) | (a1 - a0)})
        archivos[p.name] = ent
    g0, g1 = cargar(GUARDADO_DOCVIG / "grafo_r2_docvig.json"), cargar(tdir / "grafo_r2_docvig.json")
    reg_nuevas = [json.loads(x) for x in reg_run if x not in set(lineas(GUARDADO_DOCVIG / "no_mapeados_sujetos.jsonl"))]
    return OrderedDict([
        ("etiqueta_del_codigo", a.etiqueta),
        ("proceso_hijo", OrderedDict([("cwd", rel(str(CORPUS_V2))), ("sys_path", [rel(p) for p in hijo["sys_path"]]),
                                      ("runner", rel(hijo["runner"])), ("perfil", hijo["perfil"]),
                                      ("perfil_forma_r2", hijo["perfil_forma_r2"]), ("PERFIL_R2", hijo["PERFIL_R2"]),
                                      ("e0_dir", rel(hijo["e0_dir"]))])),
        ("resolucion_sujetos_del_reporte", hijo["resolucion_sujetos"]),
        ("contra_el_ensamblado_r2b", OrderedDict([
            ("cadena", RR.ruta(cad)),
            ("filas_docvig_3_4", [len(f_run), len(f_cad)]),
            ("filas_docvig_3_4_byte_a_byte_iguales", len(f_run) == len(FILAS_3_4) and f_run == f_cad),
            ("filas_docvig_3_4_runner", [json.loads(x) for x in f_run]),
            ("resolucion_sujetos_entera_igual", res_run == res_cad), ("resolucion_filas", [len(res_run), len(res_cad)]),
            ("no_mapeados_entero_igual", reg_run == reg_cad), ("no_mapeados_filas", [len(reg_run), len(reg_cad)])])),
        ("contra_lo_guardado", OrderedDict([
            ("guardado", RR.ruta(GUARDADO_DOCVIG)), ("archivos", archivos),
            ("no_mapeados_filas_nuevas", [OrderedDict((k, f.get(k)) for k in (
                "chunk_id", "indice_relacion", "mencion", "mencion_verificada", "sujeto_id_modelo", "motivo", "estado",
                "id_nodo")) for f in reg_nuevas]),
            ("grafo_r2_docvig", OrderedDict([("sha256", [sha(GUARDADO_DOCVIG / "grafo_r2_docvig.json"),
                                                         sha(tdir / "grafo_r2_docvig.json")]),
                                             ("diferencia", RR.diferencia(g0, g1))]))]))])


# --------------------------------------------------------------------------------------------------------------- #
# controles: las seis cadenas, el propuesto, las shapes                                                            #
# --------------------------------------------------------------------------------------------------------------- #
def diff_json(a, b, camino="") -> list[str]:
    """Las rutas de las claves que difieren entre dos JSON (listas comparadas enteras)."""
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in sorted(set(a) | set(b), key=str):
            if k not in a or k not in b:
                out.append(f"{camino}/{k} ({'solo nuevo' if k not in a else 'solo HEAD'})")
            elif a[k] != b[k]:
                out += diff_json(a[k], b[k], f"{camino}/{k}")
        return out
    return [] if a == b else [camino]


def reporte(d: Path) -> dict:
    return cargar(d / "reporte_ensamblado_r2.json")


def propuestos_r2b(rep: dict) -> dict:
    """El resumen de normalizar_propuestos_r2b del reporte (la primera corrida de la cadena)."""
    def buscar(o):
        if isinstance(o, dict):
            if "propuestos_r2b" in o:
                return o["propuestos_r2b"]
            for v in o.values():
                x = buscar(v)
                if x is not None:
                    return x
        return None
    return buscar(rep)


def esqueleto(rep: dict) -> dict:
    def buscar(o):
        if isinstance(o, dict):
            if "esqueleto" in o and isinstance(o["esqueleto"], dict) and "aristas_padre_sugerido_flaggeadas" in o["esqueleto"]:
                return o["esqueleto"]
            for v in o.values():
                x = buscar(v)
                if x is not None:
                    return x
        return None
    e = buscar(rep) or {}
    return {k: e.get(k) for k in ("aristas_padre_sugerido_flaggeadas", "propuestos_sin_padre",
                                  "propuestos_padre_fuera_de_catalogo")}


def shapes_de(d: Path) -> dict:
    return RR.shapes(d / "kg.json", d, E0_R2B, "r2b", None)


def tabla_shapes(s: dict) -> dict:
    return {rid: [v["result"], v["severidad"], v.get("conteos")] for rid, v in s["shapes"].items()}


def cambios_shapes(a: dict, b: dict) -> dict:
    ta, tb = tabla_shapes(a), tabla_shapes(b)
    return OrderedDict((rid, OrderedDict([("antes", [ta[rid][0], ta[rid][2]]), ("despues", [tb[rid][0], tb[rid][2]]),
                                          ("severidad", tb[rid][1])]))
                       for rid in tb if ta.get(rid) != tb[rid])


def nodo_y_arista(kg: dict) -> dict:
    n = next((x for x in kg["nodes"] if x["id"] == PROPUESTO), None)
    ar = [e for e in kg["edges"] if e["source"] == PROPUESTO and e["relation"] == "padre_sugerido"]
    return OrderedDict([("properties", n["properties"] if n else None), ("aristas_padre_sugerido", ar),
                        ("aplica_a_entrantes", sorted(e["source"] for e in kg["edges"]
                                                      if e["target"] == PROPUESTO and e["relation"] == "aplica_a"))])


def poblacion_paso_c(d: Path, kg: dict) -> dict:
    """Propuestos que reciben el rol de alcance por defecto (paso c), con el motivo de sus filas del registro: en un
    documento sin alcance no tendrían padre, y la rama de la parte A no los toma si su motivo no es de la parte A."""
    det = propuestos_r2b(reporte(d))["detalle"]
    ids = {x["id"] for x in det["padre_por_defecto"]}
    motivos, por_to = Counter(), Counter()
    for f in RR.leer_jsonl(d / RR.REGISTRO):
        if f.get("id_nodo") in ids and f["estado"] == "cuarentena":
            motivos[f["motivo"]] += 1
            por_to[f["to"]] += 1
    nodos_tos = {n["id"]: sorted({p.get("to") for p in n.get("provenances", []) if p.get("to")})
                 for n in kg["nodes"] if n["id"] in ids}
    return OrderedDict([("propuestos", len(ids)), ("filas_en_cuarentena_por_motivo", dict(sorted(motivos.items()))),
                        ("filas_por_to", dict(sorted(por_to.items()))),
                        ("con_mas_de_un_to", sum(1 for v in nodos_tos.values() if len(v) > 1))])


def mixtos(d: Path, kg: dict) -> list:
    """Propuestos con filas de la parte A que además tienen procedencias de un TO con alcance."""
    det = propuestos_r2b(reporte(d))["detalle"]
    out = []
    for x in det.get("padre_desde_sugerencia_modelo", []) + det.get("padre_por_defecto_generico", []):
        n = next(y for y in kg["nodes"] if y["id"] == x["id"])
        tos = sorted({p.get("to") for p in n.get("provenances", []) if p.get("to")})
        if tos != x["tos"]:
            out.append({"id": x["id"], "tos_del_nodo": tos, "tos_de_las_filas": x["tos"]})
    return out


def reporte_normalizado(d: Path, base: Path) -> dict:
    """El reporte del ensamblado con la ruta de su salida reemplazada por <SALIDA> (la lleva en `redirecciones`)."""
    return json.loads((d / "reporte_ensamblado_r2.json").read_text(encoding="utf-8").replace(str(base), "<SALIDA>"))


def controles(a) -> dict:
    H, N = Path(a.head), Path(a.nuevo)
    out = OrderedDict([("referencia", "r2b: los ensamblados sellados (corpus_tanda0/ens_*_r2b*); r2a: la cadena r2a del "
                                      "código (decisión e del 04/10/2026), no los sellados de f8dedd4")])
    cad = OrderedDict()
    for n, sellado in CADENAS.items():
        s0, sh, sn = (sha(RAIZ / T / sellado / "r2" / "kg.json"), sha(H / n / "r2" / "kg.json"),
                      sha(N / n / "r2" / "kg.json"))
        ref = REFERENCIA_R2A.get(n, s0)
        c = RC1.comparar_dir(H / n / "r2", N / n / "r2", ((str(H), "<SALIDA>"), (str(N), "<SALIDA>")))
        ent = OrderedDict([("sha256_sellado", s0), ("sha256_referencia", ref), ("sha256_head", sh), ("sha256_nuevo", sn),
                           ("nuevo_igual_a_la_referencia", sn == ref), ("nuevo_igual_a_head", sn == sh),
                           ("rc", [lineas(H / f"consola_{n}.txt")[-1], lineas(N / f"consola_{n}.txt")[-1]]),
                           ("r2_head_contra_nuevo", OrderedDict([
                               ("iguales", c["iguales"]), ("iguales_con_la_ruta_normalizada", c["iguales_con_ruta_normalizada"]),
                               ("distintos", c["distintos"]), ("solo_en_una", c["solo_en_a"] + c["solo_en_b"])]))])
        if "reporte_ensamblado_r2.json" in c["distintos"]:
            ent["reporte_claves_que_cambian"] = diff_json(reporte_normalizado(H / n / "r2", H),
                                                          reporte_normalizado(N / n / "r2", N))
        if a.nuevo2 and (Path(a.nuevo2) / n).exists():
            N2 = Path(a.nuevo2)
            c2 = RC1.comparar_dir(N / n / "r2", N2 / n / "r2", ((str(N), "<SALIDA>"), (str(N2), "<SALIDA>")))
            ent["doble_corrida"] = {"sha256_segunda": sha(N2 / n / "r2" / "kg.json"), "iguales": c2["iguales"],
                                    "iguales_con_la_ruta_normalizada": c2["iguales_con_ruta_normalizada"],
                                    "distintos": c2["distintos"], "solo_en_una": c2["solo_en_a"] + c2["solo_en_b"]}
        cad[n] = ent
    out["cadenas"] = cad
    for n in DIEZ_R2B:
        d0, dh, dn = Path(T) / CADENAS[n] / "r2", H / n / "r2", N / n / "r2"     # relativas: S28 guarda la ruta
        k0, kh, kn = cargar(d0 / "kg.json"), cargar(dh / "kg.json"), cargar(dn / "kg.json")
        p0, ph, pn = RR.provs_sujeto(k0), RR.provs_sujeto(kh), RR.provs_sujeto(kn)
        s0, sh_, sn = shapes_de(d0), shapes_de(dh), shapes_de(dn)
        ph_r, pn_r = propuestos_r2b(reporte(dh)), propuestos_r2b(reporte(dn))
        out[n] = OrderedDict([
            ("grafo", OrderedDict([("nodos", [len(k0["nodes"]), len(kh["nodes"]), len(kn["nodes"])]),
                                   ("aristas", [len(k0["edges"]), len(kh["edges"]), len(kn["edges"])]),
                                   ("orden", "sellado, HEAD (R2-2), nuevo (R2-3)")])),
            ("nuevo_contra_sellado", OrderedDict([
                ("diferencia", RR.diferencia(k0, kn)),
                ("procedencias_de_sujeto_quitadas", [list(k) + [v] for k, v in sorted((p0 - pn).items())]),
                ("procedencias_de_sujeto_agregadas", [list(k) + [v] for k, v in sorted((pn - p0).items())])])),
            ("nuevo_contra_head", OrderedDict([
                ("diferencia", RR.diferencia(kh, kn)),
                ("procedencias_de_sujeto_iguales", ph == pn),
                ("resolucion_y_registro_iguales", all((dh / f).read_bytes() == (dn / f).read_bytes()
                                                      for f in (RR.RESOLUCION, RR.REGISTRO)))])),
            ("propuesto_de_la_parte_a", OrderedDict([("head", nodo_y_arista(kh)), ("nuevo", nodo_y_arista(kn))])),
            ("resumen_de_los_propuestos", OrderedDict([
                ("head", {k: v for k, v in ph_r.items() if k != "detalle"}),
                ("nuevo", {k: v for k, v in pn_r.items() if k != "detalle"}),
                ("detalle_nuevo_de_las_marcas", {k: pn_r["detalle"].get(k) for k in MARCAS if k != "padre_por_defecto"})])),
            ("esqueleto", OrderedDict([("head", esqueleto(reporte(dh))), ("nuevo", esqueleto(reporte(dn)))])),
            ("shapes", OrderedDict([
                ("veredicto", [s0["veredicto"], sh_["veredicto"], sn["veredicto"]]),
                ("bloqueantes_en_fail", [s0["bloqueantes_en_fail"], sh_["bloqueantes_en_fail"], sn["bloqueantes_en_fail"]]),
                ("bloqueantes_no_computables", sn["bloqueantes_no_computables"]),
                ("S19", [tabla_shapes(x)["S19"][0::2] for x in (s0, sh_, sn)]),
                ("que_cambian_nuevo_contra_head", cambios_shapes(sh_, sn)),
                ("que_cambian_nuevo_contra_sellado", cambios_shapes(s0, sn))])),
            ("paso_c_poblacion_en_riesgo_sin_alcance", poblacion_paso_c(dn, kn)),
            ("parte_a_con_procedencias_de_un_to_con_alcance", mixtos(dn, kn))])
    fx = FIXTURE.read_text(encoding="utf-8")
    out["fixture_de_la_suite"] = OrderedDict(
        (n, {"sha256_nuevo": out["cadenas"][n]["sha256_nuevo"], "en_la_fixture": out["cadenas"][n]["sha256_nuevo"] in fx,
             "sha256_sellado_en_la_fixture": out["cadenas"][n]["sha256_sellado"] in fx}) for n in DIEZ_R2B)
    if a.suite:
        S = Path(a.suite)
        out["suite_head_contra_nuevo"] = OrderedDict(
            (p.stem.replace("suite_viejo_", ""), {
                "json_igual": p.read_bytes() == p.with_name(p.name.replace("viejo", "nuevo")).read_bytes(),
                "md_igual": p.with_suffix(".md").read_bytes()
                == p.with_name(p.name.replace("viejo", "nuevo")).with_suffix(".md").read_bytes(),
                "rc": [lineas(S / f"consola_{p.stem}.txt")[-1],
                       lineas(S / f"consola_{p.stem.replace('viejo', 'nuevo')}.txt")[-1]],
                "resumen": cargar(p).get("resumen")})
            for p in sorted(S.glob("suite_viejo_*.json")))
        gr = OrderedDict()
        for n in DIEZ_R2B:
            ph, pn = S / f"suite_grafo_head_{n}.json", S / f"suite_grafo_nuevo_{n}.json"
            if not (ph.exists() and pn.exists()):
                continue
            ih, inu = {i["id"]: i for i in cargar(ph)["items"]}, {i["id"]: i for i in cargar(pn)["items"]}
            gr[n] = OrderedDict([
                ("resumen", [cargar(ph).get("resumen"), cargar(pn).get("resumen")]),
                ("rc", [lineas(S / f"consola_suite_grafo_head_{n}.txt")[-1], lineas(S / f"consola_suite_grafo_nuevo_{n}.txt")[-1]]),
                ("sin_entrada_en_la_fixture", ["no tiene entrada con kg_sha256" in (S / f"suite_grafo_{x}_{n}.md").read_text(
                    encoding="utf-8") for x in ("head", "nuevo")]),
                ("estados_que_cambian", sorted(k for k in ih if ih[k]["estado"] != inu[k]["estado"])),
                ("detalles_que_cambian", OrderedDict((k, [ih[k].get("detalle"), inu[k].get("detalle")])
                                                     for k in ih if ih[k].get("detalle") != inu[k].get("detalle")))])
        if gr:
            out["suite_grafos_de_diez_head_contra_nuevo"] = gr
    return out


# --------------------------------------------------------------------------------------------------------------- #
# anclas: las líneas del ensamblador que cita la tabla de reprocesamiento, antes y después                         #
# --------------------------------------------------------------------------------------------------------------- #
ENSAMBLADOR = "data/experiment/tanda0/code/ensamblar_tanda0.py"
TABLA = RAIZ / "data" / "experiment" / "mantenimiento" / "tabla_reprocesamiento.md"


def anclas(a) -> dict:
    import difflib                      # noqa: PLC0415
    import re                           # noqa: PLC0415
    viejo = Path(a.antes).read_text(encoding="utf-8").splitlines()
    nuevo = (RAIZ / ENSAMBLADOR).read_text(encoding="utf-8").splitlines()
    mapa = {}
    for op, i1, i2, j1, _ in difflib.SequenceMatcher(None, viejo, nuevo, autojunk=False).get_opcodes():
        if op == "equal":
            mapa.update({i1 + k + 1: j1 + k + 1 for k in range(i2 - i1)})
    filas = []
    for linea in TABLA.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(F\d{2}[a-z]?)\s*\|", linea)
        if not m or "ensamblar_tanda0.py:" not in linea:
            continue
        for cita in re.finditer(r"ensamblar_tanda0\.py:(\d+(?:-\d+)?)`((?:, `:\d+(?:-\d+)?`)*)", linea):
            for n in (int(v) for v in re.findall(r"\d+", cita.group(1) + cita.group(2))):
                filas.append(OrderedDict([("fila", m.group(1)), ("linea_head", n), ("linea_nueva", mapa.get(n)),
                                          ("corre", (mapa.get(n) or 0) - n), ("texto", viejo[n - 1].strip()[:100])]))
    return OrderedDict([("ensamblador", ENSAMBLADOR), ("tabla", RR.ruta(TABLA)),
                        ("lineas", [len(viejo), len(nuevo)]), ("anclas", filas),
                        ("anclas_que_corren", sum(1 for f in filas if f["corre"]))])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("anclas")
    n.add_argument("--antes", type=Path, required=True, help="el ensamblador de HEAD (git show HEAD:<ruta>)")
    n.add_argument("--out", type=Path, required=True)
    s = sub.add_parser("seco")
    s.add_argument("--etiqueta", required=True, choices=("head", "nuevo"))
    s.add_argument("--cadena", type=Path, required=True)
    s.add_argument("--trabajo", type=Path, required=True)
    s.add_argument("--out", type=Path, required=True)
    c = sub.add_parser("controles")
    c.add_argument("--head", type=Path, required=True)
    c.add_argument("--nuevo", type=Path, required=True)
    c.add_argument("--nuevo2", type=Path, default=None)
    c.add_argument("--suite", type=Path, default=None)
    c.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    obj = seco(a) if a.cmd == "seco" else anclas(a) if a.cmd == "anclas" else controles(a)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{sha(a.out)}  {RR.ruta(a.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
