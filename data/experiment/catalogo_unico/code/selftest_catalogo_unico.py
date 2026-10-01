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

Etapa C2 (catálogo r2, checks K). Diferencia admitida contra el v3: las
operaciones de L-ESQ-R2 §7.3 registradas por derivar_catalogo_r2.py (8 altas,
3 cambios de alias, 1 cambio de miembro de rol), y nada más. Verifica además
las anclas de los ids nuevos contra sus chunks, las condiciones de cierre de
BKL-0028 (barrido de esq_v3_miembros/code/ en cero) y BKL-0029 (miembro del rol
de convca), la re-resolución de la tanda 0 y un control permanente (K22): las
menciones de la asamblea («órgano de gobierno») no resuelven a la clase de
BKL-0034 ni a sus hijos, y su label no aparece en el corpus. La arista de BKL-0034 sobre el
grafo queda para r2b y se informa como pendiente, sin check.

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
           EXP / "grafo_v2" / "code", REX / "e2_reduce", EXP / "esq_v3_miembros" / "code"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import difflib  # noqa: E402
from types import SimpleNamespace  # noqa: E402

import prompt_v3_b54 as v3              # noqa: E402 — sellado, solo import
import prompt_congelado as pcg          # noqa: E402
import perfil_e1                        # noqa: E402
import r1_e4                            # noqa: E402
import assemble                         # noqa: E402
import barrido_domestico_exterior as BARRIDO  # noqa: E402 — barrido de BKL-0028, importado
import construir_catalogo_v3 as CONS    # noqa: E402
import derivar_catalogo_r2 as DER       # noqa: E402
import generar_desde_catalogo as GEN    # noqa: E402
import reresolver_tanda0 as RERES       # noqa: E402

RUTA_ESQ_V3 = EXP / "esq_v3_miembros" / "esquema_v3_clases.json"
RESIDUO_BARRIDO = EXP / "esq_v3_miembros" / "residuo_catalogo_domestico_exterior.json"
CAT_V3 = CATALOGO_UNICO / "catalogo_sujetos_v3.json"
GEN_V3 = CATALOGO_UNICO / "generados_v3"
CAT_R2 = CATALOGO_UNICO / "catalogo_sujetos_r2.json"
GEN_R2 = CATALOGO_UNICO / "generados_r2"

# Lo que toca L-ESQ-R2 §7.3 en el catálogo (derivar_catalogo_r2.py).
NUEVOS_R2 = ("Sujeto_entidad_financiera_del_exterior", "Sujeto_banco_del_exterior",
             "Sujeto_entidad_cambiaria_del_exterior", "Sujeto_titular_de_cuenta_corriente_en_el_bcra",
             "Sujeto_instancia_de_gobierno_societario", "Sujeto_directorio", "Sujeto_alta_gerencia",
             "Sujeto_comite_de_auditoria")
NUEVOS_EXTERIOR = NUEVOS_R2[:3]
TITULARES = "Sujeto_titular_de_cuenta_corriente_en_el_bcra"
ALIAS_TOCADOS = ("Sujeto_entidad_financiera", "Sujeto_banco", "Sujeto_entidad_cambiaria")
ROL_CONVCA = "Sujeto_rol_alcance_convca"
PADRES_R2 = {"Sujeto_entidad_financiera_del_exterior": "Sujeto_contraparte",
             "Sujeto_banco_del_exterior": "Sujeto_contraparte",
             "Sujeto_entidad_cambiaria_del_exterior": "Sujeto_contraparte",
             TITULARES: "Sujeto_sujeto_regulado",
             "Sujeto_instancia_de_gobierno_societario": "Sujeto_sujeto_regulado",
             "Sujeto_directorio": "Sujeto_instancia_de_gobierno_societario",
             "Sujeto_alta_gerencia": "Sujeto_instancia_de_gobierno_societario",
             "Sujeto_comite_de_auditoria": "Sujeto_instancia_de_gobierno_societario"}
INSTANCIA = "Sujeto_instancia_de_gobierno_societario"
RAMA_INSTANCIA = frozenset({INSTANCIA, "Sujeto_directorio", "Sujeto_alta_gerencia", "Sujeto_comite_de_auditoria"})
# Menciones con que el corpus nombra a la asamblea de accionistas o socios
# (lavdin::1.3.1.2; lingeef::1.2::intro): no deben resolver a RAMA_INSTANCIA.
MENCIONES_ASAMBLEA = ("órgano de gobierno", "órganos de gobierno", "Órgano de gobierno de la sociedad")

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
        self.info: list[str] = []

    def chk(self, cid: str, ok: bool, desc: str) -> bool:
        self.filas.append((cid, bool(ok), desc))
        return ok

    def imprimir(self) -> int:
        for cid, ok, desc in self.filas:
            print(f"{'PASS' if ok else 'FAIL'}  {cid:5s} {desc}")
        for linea in self.info:
            print(f"INFO  {linea}")
        n_ok = sum(1 for _, ok, _ in self.filas if ok)
        print(f"\nselftest U-CAT-UNICO: {n_ok}/{len(self.filas)} PASS")
        return 0 if n_ok == len(self.filas) else 1


def indice_como_comun_v3m(bloque: str) -> dict:
    """Mismo parseo que comun_v3m.catalogo_v3_index (esq_v3_miembros/code/
    comun_v3m.py:78-110) sin su candado de 102 entradas, para correr el
    barrido de BKL-0028 sobre un bloque de otra versión. Su fidelidad se
    comprueba en K19 contra la función original sobre el bloque v3."""
    out: dict[str, dict] = {}
    for linea in bloque.split("\n"):
        if not (linea.startswith("Sujeto_") and " — " in linea):
            continue
        sid, resto = linea.split(" — ", 1)
        nivel = "rol" if "[rol del TO" in resto else ("instancia" if "[instancia]" in resto else "clase")
        alias: list[str] = []
        if " (alias: " in resto:
            cabeza, cola = resto.split(" (alias: ", 1)
            alias = [a.strip() for a in cola.rsplit(")", 1)[0].split(",")]
        else:
            cabeza = resto
        label = cabeza.replace(" [instancia]", "")
        i = label.find(" [rol del TO")
        if i != -1:
            label = label[:i]
        out[sid] = {"label": label.strip(), "alias": alias, "nivel": nivel}
    return out


def barrer_bloque(bloque: str) -> dict:
    """barrido_domestico_exterior.barrer() con el índice del bloque dado."""
    previo = BARRIDO.C.catalogo_v3_index
    BARRIDO.C.catalogo_v3_index = lambda: indice_como_comun_v3m(bloque)
    try:
        return BARRIDO.barrer()
    finally:
        BARRIDO.C.catalogo_v3_index = previo


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


def textos_corpus() -> list[str]:
    """Texto normalizado (rk.norm) de cada TO del corpus de E0: los 152 de la
    partición B5.8 y los 5 de desarrollo (salida_enm01), uno por TO."""
    rk = _cargar_script("regression_kg", REPO / "scripts" / "regression_kg.py")
    archivos = sorted(DER.PARTICION.glob("*/chunks_*.json")) + sorted(DER.E0_DEV.glob("chunks_*.json"))
    return [rk.norm(" ".join(DER.texto_verificable(c) for c in json.loads(a.read_text(encoding="utf-8"))))
            for a in archivos]


def _sin(d: dict, claves) -> dict:
    return {k: v for k, v in d.items() if k not in claves}


def checks_r2(T: Selftest) -> None:
    txt_r2 = CAT_R2.read_text(encoding="utf-8")
    sha_r2 = hashlib.sha256(txt_r2.encode("utf-8")).hexdigest()
    c3 = json.loads(CAT_V3.read_text(encoding="utf-8"))
    c2 = json.loads(txt_r2)
    s3 = {s["id"]: s for s in c3["sujetos"]}
    s2 = {s["id"]: s for s in c2["sujetos"]}
    leer3 = lambda n: (GEN_V3 / n).read_text(encoding="utf-8")  # noqa: E731

    # --- reproducción ------------------------------------------------------ #
    T.chk("K1", DER.serializar(DER.derivar()) == txt_r2,
          "catalogo_sujetos_r2.json se re-deriva byte a byte desde el v3 (derivar_catalogo_r2.py)")
    g1 = GEN.generar_todo(CAT_R2)
    g2 = GEN.generar_todo(CAT_R2)
    en_disco = sorted(p.name for p in GEN_R2.iterdir())
    T.chk("K2", g1 == g2 and en_disco == sorted(g1)
          and all((GEN_R2 / n).read_text(encoding="utf-8") == t for n, t in g1.items()),
          f"generados_r2/ en disco = generación determinística en memoria ({len(g1)} archivos, ni uno más)")
    man = json.loads(g1["manifest_generados_r2.json"])
    T.chk("K3", man["catalogo_sha256"] == sha_r2 and man["version"] == "r2",
          f"el manifiesto r2 declara el sha256 del catálogo r2 ({sha_r2[:12]}…)")

    # --- composición y operaciones ------------------------------------------ #
    vig3 = [s["id"] for s in c3["sujetos"] if s["estado"]["valor"] == "vigente"]
    vig2 = [s["id"] for s in c2["sujetos"] if s["estado"]["valor"] == "vigente"]
    niv = {n: sum(1 for i in vig2 if s2[i]["nivel"] == n) for n in ("clase", "instancia", "rol")}
    lap3 = [s for s in c3["sujetos"] if s["estado"]["valor"] == "lapida"]
    lap2 = [s for s in c2["sujetos"] if s["estado"]["valor"] == "lapida"]
    T.chk("K4", vig2 == vig3 + list(NUEVOS_R2) and niv == {"clase": 70, "instancia": 5, "rol": 35}
          and _d(lap2) == _d(lap3),
          f"vigentes {len(vig2)} = 102 del v3 + 8 altas al final ({niv}); las 5 lápidas sin cambios")
    ops = {k: v for k, v in c2["fuentes"].items() if k.startswith("r2_op_")}
    tipos = {t: sum(1 for v in ops.values() if v["tipo"] == t)
             for t in ("alta", "cambio_alias", "cambio_miembro_rol", "cambio_residuo_rol")}
    usadas = {x for s in c2["sujetos"] for x in s["procedencia"].values()}
    T.chk("K5", tipos == {"alta": 8, "cambio_alias": 3, "cambio_miembro_rol": 1, "cambio_residuo_rol": 1}
          and len(ops) == 13
          and set(ops) <= usadas and {v["id"] for v in ops.values() if v["tipo"] == "alta"} == set(NUEVOS_R2),
          f"operaciones registradas {len(ops)} = {tipos}; cada una apunta desde la procedencia de un campo")
    tocados = set(ALIAS_TOCADOS) | {ROL_CONVCA}
    iguales = all(_d(s3[i]) == _d(s2[i]) for i in s3 if i not in tocados)
    ok_alias = all(_d(_sin(s3[i], ("alias", "procedencia"))) == _d(_sin(s2[i], ("alias", "procedencia")))
                   and _d(_sin(s3[i]["procedencia"], ("alias",))) == _d(_sin(s2[i]["procedencia"], ("alias",)))
                   and s2[i]["alias"] == [a for a in s3[i]["alias"] if "del exterior" not in a]
                   for i in ALIAS_TOCADOS)
    r3, r2 = s3[ROL_CONVCA], s2[ROL_CONVCA]
    pr = ("rol.miembros", "rol.residuo_declarado")
    ok_convca = (_d(_sin(r3, ("rol", "procedencia"))) == _d(_sin(r2, ("rol", "procedencia")))
                 and _d(_sin(r3["rol"], ("miembros", "residuo_declarado"))) == _d(_sin(r2["rol"], ("miembros", "residuo_declarado")))
                 and _d(_sin(r3["procedencia"], pr)) == _d(_sin(r2["procedencia"], pr))
                 and _d(_sin(r2["rol"]["residuo_declarado"], ("remedio", "anidacion_no_estricta")))
                 == _d(_sin(r3["rol"]["residuo_declarado"], ("colectivo_operativo_sin_id", "remedio", "anidacion_no_estricta")))
                 and r2["rol"]["residuo_declarado"]["remedio"] == DER.REMEDIO_R2
                 and _d(_sin(r2["rol"]["residuo_declarado"]["anidacion_no_estricta"], ("estado_r2",)))
                 == _d(_sin(r3["rol"]["residuo_declarado"]["anidacion_no_estricta"], ("regla_3_no_mitiga",))))
    T.chk("K6", iguales and ok_alias and ok_convca,
          f"{len(s3) - len(tocados)} entradas del v3 no tocadas idénticas; en las 3 domésticas cambian solo los alias "
          "«del exterior»; en convca, solo miembros y el residuo (campo retirado, remedio y anidación al estado r2)")
    T.chk("K7", c2["version"] == "r2" and c2["version_esquema_clases"] == "3.1" and list(c2) == list(c3)
          and _d(c2["presentacion"]) == _d(c3["presentacion"]) and _d(c2["politicas"]) == _d(c3["politicas"])
          and all(_d(c2["fuentes"][k]) == _d(v) for k, v in c3["fuentes"].items()),
          "mismo esquema que el v3: claves, presentación, políticas y fuentes v3 intactas; version r2, esquema de clases 3.1")

    # --- anclas de los ids nuevos ------------------------------------------- #
    def ancla_ok(a: dict) -> bool:
        c = DER.chunk(a["chunk"])
        return (DER._normalizar(a["texto"]) in DER.texto_verificable(c)
                and DER.sha256_archivo(REPO / a["ruta"]) == a["sha256"] and c["archivo"] == a["archivo"])

    con_ancla, no_enc, extractos, malas = [], [], 0, []
    for i in NUEVOS_R2:
        for campo in ("label", "alias", "definicion", "padre"):
            f = c2["fuentes"].get(s2[i]["procedencia"].get(campo), {})
            if campo == "alias" and s2[i]["alias"] == []:
                continue  # sin alias: lo fija la operación de alta (contados aparte)
            if f.get("objeto") == DER.NO_ENCONTRADO:
                no_enc.append(f"{i[len('Sujeto_'):]}.{campo}")
                extractos += len(f.get("anclas_contrarias", []))
                malas += [(i, campo) for a in f.get("anclas_contrarias", []) if not ancla_ok(a)]
            elif "anclas" in f:
                con_ancla.append((i, campo))
                extractos += len(f["anclas"])
                malas += [(i, campo) for a in f["anclas"] if not ancla_ok(a)]
            else:
                malas.append((i, campo))
    for v in ops.values():
        extractos += len(v.get("anclas", []))
        malas += [(v["id"], "op") for a in v.get("anclas", []) if not ancla_ok(a)]
    sin_alias = sum(1 for i in NUEVOS_R2 if not s2[i]["alias"])
    T.chk("K8", not malas and len(con_ancla) + len(no_enc) + sin_alias == 32,
          f"8 ids nuevos × 4 campos: {len(con_ancla)} con ancla, {len(no_enc)} NO ENCONTRADO, {sin_alias} sin alias; "
          f"{extractos} extractos releídos contra su chunk de E0 (sha del archivo incluido)")
    coh = all(s2[i]["definicion"] is None for i in NUEVOS_R2 if f"{i[len('Sujeto_'):]}.definicion" in no_enc) \
        and all(s2[i]["definicion"] for i in NUEVOS_R2 if f"{i[len('Sujeto_'):]}.definicion" not in no_enc) \
        and all(a in s3["Sujeto_entidad_cambiaria"]["alias"] for a in s2["Sujeto_entidad_cambiaria_del_exterior"]["alias"])
    T.chk("K9", coh, f"NO ENCONTRADO sin inventar: definiciones nulas donde no hay ancla; alias sin ancla solo si viene "
          f"del v3 ({', '.join(no_enc)})")

    # --- bloque, enums, ROL_POR_TO, labels ----------------------------------- #
    b3, b2 = leer3("bloque_catalogo_v3.txt"), g1["bloque_catalogo_r2.txt"]
    diff = list(difflib.unified_diff(b3.split("\n"), b2.split("\n"), lineterm="", n=0))
    menos = [x[1:] for x in diff if x.startswith("-") and not x.startswith("---")]
    mas = [x[1:] for x in diff if x.startswith("+") and not x.startswith("+++")]
    lineas2 = b2.split("\n")
    id_de = lambda x: x.split(" — ", 1)[0]  # noqa: E731
    def_nuevas = [x for x in mas if x.startswith("  def: ")]
    ok_def = all(id_de(lineas2[lineas2.index(x) - 1]) in NUEVOS_R2 for x in def_nuevas)
    T.chk("K10", all(id_de(x) in ALIAS_TOCADOS for x in menos)
          and all(id_de(x) in set(ALIAS_TOCADOS) | set(NUEVOS_R2) for x in mas if not x.startswith("  def: "))
          and ok_def and (len(menos), len(mas), len(def_nuevas)) == (3, 16, 5),
          f"diff del bloque v3→r2: −{len(menos)}/+{len(mas)} líneas = 3 líneas de alias reemplazadas + 8 ids nuevos "
          f"+ {len(def_nuevas)} definiciones; nada más")
    e3 = json.loads(leer3("enums_tool_schema_v3.json"))
    e2 = json.loads(g1["enums_tool_schema_r2.json"])
    T.chk("K11", e2["sujeto_id"] == e3["sujeto_id"] + list(NUEVOS_R2)
          and e2["sujeto_propuesto_padre_sugerido"] == e2["sujeto_id"],
          f"enums r2 = los 102 del v3 en su orden + 8 al final ({len(e2['sujeto_id'])})")
    T.chk("K12", g1["rol_por_to_r2.json"] == leer3("rol_por_to_v3.json"),
          "ROL_POR_TO r2 = v3 byte a byte (ninguna operación lo toca)")
    l3 = json.loads(leer3("labels_e2_v3.json"))
    l2 = json.loads(g1["labels_e2_r2.json"])
    T.chk("K13", _d({k: v for k, v in l2.items() if k not in NUEVOS_R2}) == _d(l3) and set(l2) - set(l3) == set(NUEVOS_R2),
          f"labels de E2 r2 = los del v3 + 8 ({len(l2)})")

    # --- esqueleto, índice de E4, S19, suite --------------------------------- #
    ent3 = json.loads(leer3("entrada_esqueleto_v3.json"))
    ent2 = json.loads(g1["entrada_esqueleto_r2.json"])
    by3 = {e["id"]: e for e in ent3["clases"] + ent3["roles"]}
    by2 = {e["id"]: e for e in ent2["clases"] + ent2["roles"]}
    cambian = sorted(i for i in by3 if _d(by3[i]) != _d(by2[i]))
    ok_ent = (set(by2) - set(by3) == set(NUEVOS_R2) and cambian == sorted(tocados)
              and all(_d(_sin(by3[i], ("alias",))) == _d(_sin(by2[i], ("alias",))) for i in ALIAS_TOCADOS)
              and _d(_sin(by3[ROL_CONVCA], ("miembros", "residuo_declarado"))) == _d(_sin(by2[ROL_CONVCA], ("miembros", "residuo_declarado")))
              and all(by2[i]["padre"] == p for i, p in PADRES_R2.items())
              and _d(ent2["excepciones_s15"]) == _d(ent3["excepciones_s15"]) and ent2["version"] == "3.1")
    T.chk("K14", ok_ent, f"entrada del esqueleto r2: +8 clases con los padres declarados; cambian solo {len(cambian)} "
          "entradas (alias de las 3 domésticas, miembro y residuo de convca); excepciones_s15 idéntica; version 3.1")
    n3, e3s, _ = build_skeleton_de(leer3("entrada_esqueleto_v3.json"))
    n2, e2s, _ = build_skeleton_de(g1["entrada_esqueleto_r2.json"])
    solo_r2 = set(e2s) - set(e3s)
    solo_v3 = set(e3s) - set(e2s)
    esperado_r2 = {(i, "subclase_de", p) for i, p in PADRES_R2.items()} | {(TITULARES, "miembro_de", ROL_CONVCA)}
    esperado_v3 = {("Sujeto_entidad_financiera", "miembro_de", ROL_CONVCA)}
    nodos_cambian = sorted(i for i in n3 if _d(n3[i]) != _d(n2[i]))
    T.chk("K15", set(n2) - set(n3) == set(NUEVOS_R2) and nodos_cambian == sorted(ALIAS_TOCADOS)
          and solo_r2 == esperado_r2 and solo_v3 == esperado_v3
          and all(_d(e2s[k]) == _d(e3s[k]) for k in set(e2s) & set(e3s)),
          f"build_skeleton r2: {len(n2)} nodos / {len(e2s)} aristas (v3 {len(n3)} / {len(e3s)}); +8 subclase_de, "
          "miembro_de de convca de EF a titulares; cambian solo los alias de 3 nodos")
    idx3 = {(c, k): i for c, k, i in json.loads(leer3("indice_e4_v3.json"))}
    idx2 = {(c, k): i for c, k, i in json.loads(g1["indice_e4_r2.json"])}
    quitar = set(ALIAS_TOCADOS) | set(NUEVOS_R2)
    base3 = {"clases": [e for e in ent3["clases"] if e["id"] not in quitar], "roles": ent3["roles"]}
    base2 = {"clases": [e for e in ent2["clases"] if e["id"] not in quitar], "roles": ent2["roles"]}
    cambia_idx = sorted(k for k in set(idx2) & set(idx3) if idx2[k] != idx3[k])
    T.chk("K16", idx2 == r1_e4.indice_catalogo(ent2) and r1_e4.indice_catalogo(base3) == r1_e4.indice_catalogo(base2),
          f"índice de E4 r2 ({len(idx2)} claves vs {len(idx3)}): sin las entradas tocadas y nuevas, idéntico al v3; "
          f"+{len(set(idx2) - set(idx3))} / −{len(set(idx3) - set(idx2))} claves, {len(cambia_idx)} reasignadas "
          f"{[list(k) + [idx2[k]] for k in cambia_idx]}")
    sv = _cargar_script("shapes_validator", REPO / "scripts" / "shapes_validator.py")
    ids19_3 = json.loads(leer3("ids_s19_v3.json"))
    ids19_2 = json.loads(g1["ids_s19_r2.json"])
    ids_ent2, _, _, defecto = sv.cargar_catalogo_sujetos(str(GEN_R2 / "entrada_esqueleto_r2.json"))
    T.chk("K17", ids19_2 == sorted(ids19_3 + list(NUEVOS_R2)) and defecto is None and ids_ent2 == set(ids19_2)
          and sv.cargar_excepciones_s15(str(GEN_R2 / "entrada_esqueleto_r2.json"))
          == sv.cargar_excepciones_s15(str(GEN_V3 / "entrada_esqueleto_v3.json")),
          f"S19: {len(ids19_2)} ids (102 + 8), también como --excepciones; S15 lee la misma lista que en v3")
    rk = _cargar_script("regression_kg", REPO / "scripts" / "regression_kg.py")
    cs2 = rk.Catalogo.desde_ruta(GEN_R2 / "catalogo_suite_r2.json")
    r28 = rk.t_bkl_0028(SimpleNamespace(cat=cs2, grafo=SimpleNamespace(by_id={})))
    v28 = r28.get("valores") or {}
    T.chk("K18", cs2.version == "3.1" and len(cs2.ids) == 110 and v28.get("ids_con_alias_del_exterior") == []
          and set(NUEVOS_EXTERIOR) <= set(v28.get("ids_separados_del_exterior") or []),
          f"suite: catálogo 3.1 con {len(cs2.ids)} ids; t_bkl_0028 (regression_kg.py:781) aplica y su parte de "
          "catálogo se cumple: 0 ids domésticos con alias «del exterior», los 3 ids separados presentes")
    T.info.append(f"t_bkl_0028 sobre el catálogo r2 sin grafo: estado {r28['estado']} (la parte de grafo exige "
                  f"r2b); ids separados que cuenta: {sorted(v28.get('ids_separados_del_exterior') or [])}")

    # --- condiciones de cierre ---------------------------------------------- #
    fiel = indice_como_comun_v3m(v3.BLOQUE_CATALOGO_V3) == BARRIDO.C.catalogo_v3_index()
    bv3 = barrer_bloque(leer3("bloque_catalogo_v3.txt"))
    bv2 = barrer_bloque(b2)
    residuo = json.loads(RESIDUO_BARRIDO.read_text(encoding="utf-8"))
    T.chk("K19", fiel and [a["id"] for a in bv3["ids_afectados"]] == [a["id"] for a in residuo["ids_afectados"]]
          and bv3["n_afectados"] == 3 and bv2["n_afectados"] == 0,
          f"BKL-0028: barrido de esq_v3_miembros/code/barrido_domestico_exterior.py: v3 {bv3['n_afectados']} "
          f"(= residuo_catalogo_domestico_exterior.json), r2 {bv2['n_afectados']}")
    T.info.append(f"barrido r2, ids con extranjería en su propio label (contraste, no afectados): "
                  f"{[a['id'] for a in bv2['ids_extranjeros_propios']]}")
    cand = [i for i, c in cs2.clases.items()
            if "titular" in rk.norm(c.get("label")) and "cuenta corriente" in rk.norm(c.get("label"))]
    res_convca = by2[ROL_CONVCA].get("residuo_declarado") or {}
    sin_hijas = not any(e.get("padre") == TITULARES for e in ent2["clases"])
    sin_arista = not ({("Sujeto_entidad_financiera", "subclase_de", TITULARES),
                       (TITULARES, "subclase_de", "Sujeto_entidad_financiera")} & set(e2s))
    T.chk("K20", by2[ROL_CONVCA]["miembros"] == [TITULARES] and cs2.miembros(ROL_CONVCA) == [TITULARES]
          and "colectivo_operativo_sin_id" not in res_convca and cand == [TITULARES]
          and res_convca.get("remedio") == DER.REMEDIO_R2
          and (res_convca.get("anidacion_no_estricta") or {}).get("estado_r2") == DER.ESTADO_R2_ANIDACION
          and sin_hijas and sin_arista,
          f"BKL-0029: miembro del rol de convca = {TITULARES}; residuo sin colectivo_operativo_sin_id y con remedio y "
          "anidación en estado r2 (lo que afirma estado_r2 se cumple: el id no tiene subclases ni arista subclase_de "
          "con EF); candidato de t_bkl_0029 (regression_kg.py:812) = el id nuevo")
    T.info.append(f"BKL-0034: {INSTANCIA} y bajo ella Directorio, Alta Gerencia y Comité de auditoría están en el "
                  "catálogo; la arista lingob::2.3.2::intro → Sujeto_directorio exige un grafo: PENDIENTE (r2b)")

    # --- re-resolución de la tanda 0 ---------------------------------------- #
    rr1, rr2 = RERES.reresolver(), RERES.reresolver()
    T.chk("K21", rr1 == rr2 and rr1["resuelven_v3"] == rr1["guardado_resueltos"] and not rr1["v3_y_no_r2"]
          and not rr1["cambian_de_destino"],
          "re-resolución idempotente; con v3 reproduce la tabla guardada; con r2 ningún resuelto se pierde ni cambia")
    T.info.append(f"re-resolución (reresolver_tanda0.py), diez: {rr1['propuestos']} propuestos, v3 {rr1['resuelven_v3']}, "
                  f"r2 {rr1['resuelven_r2']}; con r2 y no con v3: {len(rr1['r2_y_no_v3'])} "
                  f"{[(d['label'], d['r2']) for d in rr1['r2_y_no_v3']]}")

    # --- control permanente: menciones de la asamblea y label de la clase --- #
    resueltas = {m: r1_e4.resolver_label(m, None, idx2)[0] for m in MENCIONES_ASAMBLEA}
    corpus = textos_corpus()
    label_n = rk.norm(s2[INSTANCIA]["label"])
    formas = sorted({label_n, " ".join(r1_e4._singular(w) for w in label_n.split())})
    apariciones = {f: sum(t.count(f) for t in corpus) for f in formas}
    T.chk("K22", not (set(resueltas.values()) & RAMA_INSTANCIA) and len(corpus) == 157 and not any(apariciones.values())
          and not s2[INSTANCIA]["alias"],
          f"control permanente: con el índice r2, {list(MENCIONES_ASAMBLEA)} no resuelven a {INSTANCIA} ni a sus "
          f"hijos ({resueltas}); el label y su singular no aparecen en los 157 TOs ({apariciones})")


def main() -> int:
    T = Selftest()
    checks_v3(T)
    checks_r2(T)
    return T.imprimir()


if __name__ == "__main__":
    raise SystemExit(main())
