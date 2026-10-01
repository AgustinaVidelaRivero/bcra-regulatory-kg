"""
selftest_catalogo_unico.py — U-CAT-UNICO: compara cada artefacto generado
desde el catálogo único con el consumidor que hoy lee el catálogo. Es también
el control LN-8 del diseño de U-LISTAS-NOMAP (bloque del prompt y JSON sin
diferencias). Ninguna llamada a la API; no escribe archivos.

Etapa C1 (catálogo v3). Diferencia admitida contra esquema_v3_clases.json:
la 6/5 de L-ESQ-R2 §7.1, y nada más:
  - 6 ids solo en el catálogo único (adiciones de B5.4 F1.4 salvo la CEC);
  - 5 ids solo en esquema_v3_clases.json (retiros de F1.5, lápidas).
Toda otra diferencia es FAIL.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/catalogo_unico/code/selftest_catalogo_unico.py
Código de salida 0 solo si todos los checks pasan.
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import copy  # noqa: E402
import hashlib  # noqa: E402
import importlib.util  # noqa: E402
import json  # noqa: E402
from pathlib import Path  # noqa: E402

AQUI = Path(__file__).resolve().parent
CATALOGO_UNICO = AQUI.parent
REPO = AQUI.parents[3]
EXP = REPO / "data" / "experiment"
REX = EXP / "reextraccion_v2"
for _p in (AQUI, EXP / "b54_catalogo_v3" / "code", REX / "e1_extractor", REX, REX / "corpus_v2",
           EXP / "grafo_v2" / "code", REX / "e2_reduce"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import prompt_v3_b54 as v3              # noqa: E402 — sellado, solo import
import prompt_congelado as pcg          # noqa: E402
import perfil_e1                        # noqa: E402
import r1_e4                            # noqa: E402
import assemble                         # noqa: E402
import construir_catalogo_v3 as CONS    # noqa: E402
import generar_desde_catalogo as GEN    # noqa: E402

RUTA_ESQ_V3 = EXP / "esq_v3_miembros" / "esquema_v3_clases.json"
CAT_V3 = CATALOGO_UNICO / "catalogo_sujetos_v3.json"
GEN_V3 = CATALOGO_UNICO / "generados_v3"

PREFIJO_SHA256_V3 = "35e88c2dd0a2920302c29005b08ab9689405606d4bd5fcf8fb7ce807b1a3c512"
PREFIJO_HASH_V3 = "54a111e2175f"
AMBIGUO = "__AMBIGUO__"

# La 6/5 tal como la nombra L-ESQ-R2 §7.1 (literal, independiente del módulo).
SEIS = frozenset({
    "Sujeto_entidad_girada", "Sujeto_entidad_depositaria", "Sujeto_entidad_receptora",
    "Sujeto_entidad_originante_de_transferencia", "Sujeto_banco_central_del_exterior", "Sujeto_fmi"})
CINCO = frozenset({
    "Sujeto_acreedor_del_exterior", "Sujeto_autoridad_nacional_de_aplicacion",
    "Sujeto_secretaria_de_comercio", "Sujeto_secretaria_de_energia", "Sujeto_secretaria_de_transporte"})


def _cargar_script(nombre: str, ruta: Path):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class _EnMemoria:
    """Sustituto de Path para assemble.CATALOGO_PATH: build_skeleton solo
    llama read_text, y así el selftest no escribe archivos temporales."""

    def __init__(self, texto: str):
        self._texto = texto

    def read_text(self, encoding: str = "utf-8") -> str:
        return self._texto


def build_skeleton_de(texto: str):
    previo = assemble.CATALOGO_PATH
    assemble.CATALOGO_PATH = _EnMemoria(texto)
    try:
        return assemble.build_skeleton()
    finally:
        assemble.CATALOGO_PATH = previo


def _d(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=False)


class Selftest:
    def __init__(self):
        self.filas: list[tuple[str, bool, str]] = []

    def chk(self, cid: str, ok: bool, desc: str) -> bool:
        self.filas.append((cid, bool(ok), desc))
        return ok

    def imprimir(self) -> int:
        for cid, ok, desc in self.filas:
            print(f"{'PASS' if ok else 'FAIL'}  {cid:5s} {desc}")
        n_ok = sum(1 for _, ok, _ in self.filas if ok)
        print(f"\nselftest U-CAT-UNICO: {n_ok}/{len(self.filas)} PASS")
        return 0 if n_ok == len(self.filas) else 1


def _leer_generado(nombre: str) -> str:
    return (GEN_V3 / nombre).read_text(encoding="utf-8")


def checks_v3(T: Selftest) -> None:
    texto_cat = CAT_V3.read_text(encoding="utf-8")
    sha_cat = hashlib.sha256(texto_cat.encode("utf-8")).hexdigest()
    cat = json.loads(texto_cat)
    esq_txt = RUTA_ESQ_V3.read_text(encoding="utf-8")
    esq = json.loads(esq_txt)
    perfil = perfil_e1.perfil("v3_b54")

    # --- I. el catálogo y los generados se reproducen ---------------------- #
    T.chk("I1", CONS.serializar(CONS.construir()) == texto_cat,
          "catalogo_sujetos_v3.json se reconstruye byte a byte desde los artefactos fuente")
    gen1 = GEN.generar_todo(CAT_V3)
    gen2 = GEN.generar_todo(CAT_V3)
    T.chk("I2", gen1 == gen2, "generar_todo es determinístico (dos llamadas en el mismo proceso)")
    en_disco = sorted(p.name for p in GEN_V3.iterdir())
    T.chk("I3", en_disco == sorted(gen1) and all(_leer_generado(n) == t for n, t in gen1.items()),
          f"generados_v3/ en disco = generación en memoria ({len(gen1)} archivos, ni uno más)")
    man = json.loads(gen1["manifest_generados_v3.json"])
    T.chk("I4", man["catalogo_sha256"] == sha_cat,
          f"el manifiesto declara el sha256 del catálogo ({sha_cat[:12]}…)")

    vig = [s for s in cat["sujetos"] if s["estado"]["valor"] == "vigente"]
    lap = [s for s in cat["sujetos"] if s["estado"]["valor"] == "lapida"]
    niv = {n: sum(1 for s in vig if s["nivel"] == n) for n in ("clase", "instancia", "rol")}
    T.chk("I5", len(vig) == 102 and niv == {"clase": 62, "instancia": 5, "rol": 35},
          f"vigentes {len(vig)} = 62 clases + 5 instancias + 35 roles (catalogo_sujetos_v3.md:33-34): {niv}")
    T.chk("I6", {s["id"] for s in lap} == CINCO and len(lap) == 5,
          "lápidas = los cinco retiros de F1.5")
    T.chk("I7", all(s["estado"].get(k) for s in lap for k in ("evidencia", "fecha", "laudo")),
          "cada lápida lleva evidencia, fecha y laudo")
    T.chk("I8", all(s["estado"].get("alta") for s in vig), "cada vigente lleva su alta")
    fuentes = set(cat["fuentes"])
    T.chk("I9", all(set(s["procedencia"].values()) <= fuentes for s in cat["sujetos"])
          and set(cat["politicas"]["procedencia"].values()) <= fuentes,
          "toda procedencia apunta a una clave de `fuentes`")
    T.chk("I10", sum(1 for s in vig if s["definicion"]) == 30,
          "30 definiciones = 24 dirigidas + 6 posicionales (catalogo_sujetos_v3.md:37-39)")
    T.chk("I11", {s["id"] for s in cat["sujetos"] if s["marca_revision"]} == set(v3.MARCADOS_REVISION_R2),
          "marcas de revisión = MARCADOS_REVISION_R2, sin cambios (decisión 4)")
    T.chk("I12", set(v3.sujetos_catalogo_v3()) - {e["id"] for e in esq["clases"] + esq["roles"]} == SEIS
          and {e["id"] for e in esq["clases"] + esq["roles"]} - set(v3.sujetos_catalogo_v3()) == CINCO,
          "la 6/5 literal de L-ESQ-R2 §7.1 coincide con la medida (bloque 102 vs JSON 101)")

    # --- A. bloque del prompt --------------------------------------------- #
    bloque = gen1["bloque_catalogo_v3.txt"]
    T.chk("A1", bloque.encode("utf-8") == v3.BLOQUE_CATALOGO_V3.encode("utf-8"),
          "bloque generado = BLOQUE_CATALOGO_V3 byte a byte (prompt_v3_b54.py:396)")
    t = pcg.PREFIJO_SISTEMA_CONGELADO
    n_bloque = t.count(v3.BLOQUE_CATALOGO_CONGELADO)
    prefijo = t.replace(v3.BLOQUE_CATALOGO_CONGELADO, bloque)
    sha_pref = hashlib.sha256(prefijo.encode("utf-8")).hexdigest()
    T.chk("A2", n_bloque == 1 and sha_pref == PREFIJO_SHA256_V3 == v3.PREFIJO_SHA256_V3,
          f"prefijo v3 recompuesto con el bloque generado: sha256 {sha_pref[:12]}… = PREFIJO_SHA256_V3")
    enums = json.loads(gen1["enums_tool_schema_v3.json"])
    tool = copy.deepcopy(pcg.TOOL_SCHEMA_CONGELADO)
    props = tool["input_schema"]["properties"]["relations"]["items"]["properties"]
    props["sujeto_id"]["enum"] = list(enums["sujeto_id"])
    props["sujeto_propuesto_padre_sugerido"]["enum"] = list(enums["sujeto_propuesto_padre_sugerido"])
    canon = json.dumps({"system": [{"type": "text", "text": prefijo, "cache_control": {"type": "ephemeral"}}],
                        "tools": [tool]}, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    h = hashlib.sha256(canon.encode("utf-8")).hexdigest()[:12]
    T.chk("A3", h == PREFIJO_HASH_V3 == v3.PREFIJO_HASH_V3,
          f"hash canónico system+tools con bloque y enums generados = {h} (namespace de caché v3)")

    # --- B. enums del tool schema ------------------------------------------ #
    T.chk("B1", enums["sujeto_id"] == v3.sujetos_catalogo_v3(),
          "enum sujeto_id = sujetos_catalogo_v3() en contenido y orden (prompt_v3_b54.py:402)")
    pv3 = v3.TOOL_SCHEMA_V3["input_schema"]["properties"]["relations"]["items"]["properties"]
    T.chk("B2", enums["sujeto_propuesto_padre_sugerido"] == pv3["sujeto_propuesto_padre_sugerido"]["enum"]
          and enums["sujeto_id"] == pv3["sujeto_id"]["enum"],
          "los dos enums = los de TOOL_SCHEMA_V3")
    T.chk("B3", set(enums["sujeto_id"]) == perfil.esquema.sujetos_catalogo_set,
          "conjunto del enum = sujetos_catalogo_set del perfil v3_b54 (perfil_e1.py:166)")

    # --- C. ROL_POR_TO ------------------------------------------------------ #
    rpt = json.loads(gen1["rol_por_to_v3.json"])
    T.chk("C1", _d(rpt) == _d(v3.ROL_POR_TO_V3),
          f"ROL_POR_TO generado = ROL_POR_TO_V3 en contenido y orden ({len(rpt)} entradas; prompt_v3_b54.py:453)")
    n_rol = sum(1 for r in rpt.values() if "clase_ids" not in r)
    T.chk("C2", (len(rpt), n_rol, len(rpt) - n_rol) == (71, 35, 36) and _d(perfil.rol_por_to) == _d(rpt),
          f"71 entradas = 35 rol + 36 clase; = rol_por_to del perfil v3_b54")

    # --- D. labels de E2 ---------------------------------------------------- #
    labels = json.loads(gen1["labels_e2_v3.json"])
    T.chk("D1", _d(labels) == _d(perfil.labels_catalogo),
          "labels de E2 = labels_catalogo del perfil v3_b54 en contenido y orden (perfil_e1.py:101, :179)")

    # --- F. entrada del esqueleto ------------------------------------------ #
    ent = json.loads(gen1["entrada_esqueleto_v3.json"])
    g_ent = {e["id"]: e for e in ent["clases"] + ent["roles"]}
    j_ent = {e["id"]: e for e in esq["clases"] + esq["roles"]}
    comunes = set(g_ent) & set(j_ent)
    dif_comunes = sorted(i for i in comunes if _d(g_ent[i]) != _d(j_ent[i]))
    T.chk("F1", set(g_ent) - set(j_ent) == SEIS and set(j_ent) - set(g_ent) == CINCO,
          f"ids de la entrada del esqueleto vs esquema_v3_clases.json: solo generada {len(set(g_ent) - set(j_ent))} "
          f"(la 6), solo JSON {len(set(j_ent) - set(g_ent))} (la 5)")
    T.chk("F2", not dif_comunes,
          f"{len(comunes)} entradas comunes idénticas campo a campo y en orden de claves; distintas: {dif_comunes}")
    orden_ok = ([e["id"] for e in ent["clases"] if e["id"] in comunes] == [e["id"] for e in esq["clases"] if e["id"] in comunes]
                and [e["id"] for e in ent["roles"] if e["id"] in comunes] == [e["id"] for e in esq["roles"] if e["id"] in comunes])
    T.chk("F3", orden_ok, "orden relativo de las entradas comunes = esquema_v3_clases.json (clases y roles)")
    T.chk("F4", _d(ent["excepciones_s15"]) == _d(esq["excepciones_s15"]) and ent["version"] == esq["version"],
          "excepciones_s15 y version idénticas a esquema_v3_clases.json")
    T.chk("F5", set(ent) - {"deriva_de"} == set(esq) - {"deriva_de", "notas_de_construccion"},
          "claves de nivel superior: solo difieren los metadatos deriva_de y notas_de_construccion (no los lee ningún consumidor)")
    n_g, e_g, c_g = build_skeleton_de(gen1["entrada_esqueleto_v3.json"])
    n_j, e_j, c_j = build_skeleton_de(esq_txt)
    n_com = set(n_g) & set(n_j)
    e_com = set(e_g) & set(e_j)
    e_solo_g = set(e_g) - set(e_j)
    e_solo_j = set(e_j) - set(e_g)
    toca = lambda k: k[0] in SEIS | CINCO or k[2] in SEIS | CINCO  # noqa: E731
    T.chk("F6", set(n_g) - set(n_j) == SEIS and set(n_j) - set(n_g) == CINCO
          and all(_d(n_g[i]) == _d(n_j[i]) for i in n_com),
          f"build_skeleton (assemble.py:118): nodos {len(n_g)} vs {len(n_j)}; los {len(n_com)} comunes idénticos")
    T.chk("F7", all(toca(k) for k in e_solo_g | e_solo_j) and all(_d(e_g[k]) == _d(e_j[k]) for k in e_com),
          f"build_skeleton: aristas {len(e_g)} vs {len(e_j)}; solo generada {len(e_solo_g)}, solo JSON "
          f"{len(e_solo_j)}, todas tocan la 6/5; {len(e_com)} comunes idénticas")

    # --- E. índice de E4 ---------------------------------------------------- #
    idx_g = {(c, k): i for c, k, i in json.loads(gen1["indice_e4_v3.json"])}
    idx_j = r1_e4.indice_catalogo(esq)
    T.chk("E1", idx_g == r1_e4.indice_catalogo(ent),
          "índice generado = r1_e4.indice_catalogo sobre la entrada generada (r1_e4.py:74)")
    sin6 = {"clases": [e for e in ent["clases"] if e["id"] not in SEIS], "roles": ent["roles"]}
    sin5 = {"clases": [e for e in esq["clases"] if e["id"] not in CINCO], "roles": esq["roles"]}
    T.chk("E2", r1_e4.indice_catalogo(sin6) == r1_e4.indice_catalogo(sin5),
          "sin la 6/5, el índice generado y el de esquema_v3_clases.json son idénticos")
    solo_g = sorted(set(idx_g) - set(idx_j))
    solo_j = sorted(set(idx_j) - set(idx_g))
    cambia = sorted(k for k in set(idx_g) & set(idx_j) if idx_g[k] != idx_j[k])
    expl = (all(idx_g[k] in SEIS for k in solo_g) and all(idx_j[k] in CINCO for k in solo_j)
            and all(idx_g[k] == AMBIGUO or idx_j[k] == AMBIGUO for k in cambia))
    T.chk("E3", expl,
          f"índice {len(idx_g)} vs {len(idx_j)} claves: solo generado {len(solo_g)} (→ la 6), solo JSON "
          f"{len(solo_j)} (→ la 5), valor distinto {len(cambia)} {[list(k) for k in cambia]}")

    # --- G. S19 ------------------------------------------------------------- #
    sv = _cargar_script("shapes_validator", REPO / "scripts" / "shapes_validator.py")
    ids19 = json.loads(gen1["ids_s19_v3.json"])
    T.chk("G1", ids19 == sorted(v3.sujetos_catalogo_v3()) and len(ids19) == 102,
          f"ids de S19 = los {len(ids19)} vigentes")
    ids_hoy, n_c, n_r, defecto = sv.cargar_catalogo_sujetos(str(RUTA_ESQ_V3))
    T.chk("G2", defecto is None and len(ids_hoy) == 101 and set(ids19) - ids_hoy == SEIS
          and ids_hoy - set(ids19) == CINCO,
          f"S19 hoy (shapes_validator.py:227 sobre esquema_v3_clases.json) lee {len(ids_hoy)}; diferencia = la 6/5")
    ids_ent, _, _, defecto2 = sv.cargar_catalogo_sujetos(str(GEN_V3 / "entrada_esqueleto_v3.json"))
    T.chk("G3", defecto2 is None and ids_ent == set(ids19),
          "con la entrada generada como --excepciones, S19 lee los 102")
    T.chk("G4", sv.cargar_excepciones_s15(str(GEN_V3 / "entrada_esqueleto_v3.json"))
          == sv.cargar_excepciones_s15(str(RUTA_ESQ_V3)),
          "S15 lee la misma lista de excepciones de la entrada generada que de esquema_v3_clases.json")

    # --- H. catálogo de la suite ------------------------------------------- #
    rk = _cargar_script("regression_kg", REPO / "scripts" / "regression_kg.py")
    cs = rk.Catalogo.desde_ruta(GEN_V3 / "catalogo_suite_v3.json")
    cj = rk.Catalogo.desde_ruta(RUTA_ESQ_V3)
    T.chk("H1", cs.ids == frozenset(ids19) and cs.ids - cj.ids == SEIS and cj.ids - cs.ids == CINCO,
          f"regression_kg.Catalogo (:306): {len(cs.ids)} ids generados vs {len(cj.ids)} hoy; diferencia = la 6/5")
    T.chk("H2", cs.version == cj.version and all(cs.miembros(r) == cj.miembros(r) for r in cj.roles)
          and all(_d(cs.clases[i]) == _d(cj.clases[i]) for i in set(cs.clases) & set(cj.clases)),
          "versión, miembros de los 35 roles y clases comunes idénticos a esquema_v3_clases.json")
    T.chk("H3", r1_e4.indice_catalogo(cs.data) == idx_g,
          "el índice de E4 que arma la suite (regression_kg.py:454) = indice_e4_v3.json")


def main() -> int:
    T = Selftest()
    checks_v3(T)
    return T.imprimir()


if __name__ == "__main__":
    raise SystemExit(main())
