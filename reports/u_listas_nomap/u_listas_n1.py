"""
u_listas_n1.py — U-LISTAS-NOMAP, etapa N1: inventario de las listas cerradas del
esquema en el crudo de E1 y mediciones sobre sujetos, re-resolución contrafáctica,
omisiones y catálogo (mandato docs/mandatos/ULISTAS_NOMAP_diseno.md).

Solo lectura, USD 0: ninguna llamada a la API, Neo4j no se usa. Los módulos del
pipeline se IMPORTAN y no se editan. La única db que se abre es
e3_verificador/cache/e1_reintentos.db, con file:…?immutable=1. Escribe
únicamente en --out-dir: n1_inventario.json, n1_inventario.md y
muestra_forzados_30.csv. La salida no lleva fecha ni rutas absolutas: dos
corridas dan bytes idénticos.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_listas_nomap/u_listas_n1.py --out-dir reports/u_listas_nomap

REGLAS DECLARADAS ANTES DE APLICARSE

R-LISTAS  Listas cerradas del prefijo v3 (perfil v3_b54, PREFIJO_SISTEMA_V3):
          tipos de entidad = perfil.esquema.entity_types (9); predicados =
          perfil.esquema.predicates (13); catálogo de sujetos = ids del bloque v3
          = perfil.esquema.sujetos_catalogo_set (102); Obligacion.tipo =
          perfil.esquema.obligacion_tipo_enum (6); Restriccion.tipo =
          {prohibicion, limite_cuantitativo, limite_cualitativo}; Comunicacion.tipo
          = {A, B, C}; claves de properties por tipo como en el comando [c11] de
          docs/tablero_correcciones.md. Un valor vacío o ausente cuenta como fuera
          de lista ([c11]). Las listas de Restriccion.tipo, Comunicacion.tipo y
          claves se contrastan con las líneas «Properties:» del prefijo (guarda:
          si no coinciden, FRENO). Operacion.tipo es texto libre: se describe.
          r1 se extrajo con el perfil produccion_dev (esquema v2); se mide contra
          las listas v3 (como [c11]) y, aparte, contra las de su perfil.
R-CAPAS   Capas por TO: (L0) crudo del primer intento de E1 =
          extracciones_e1_compact.jsonl, tool_input_crudo; (L0r) crudo de los
          reintentos de E3 = e1_reintentos.db, namespace de la generación, cada
          entrada asignada a su chunk por «TO:» y «Punto del chunk:» o
          «MINI-CHUNK de bloque estructural (<bloque> del punto <u>)» del mensaje
          de usuario, con el id verificado contra E0; (L1) validado del primer
          intento = campo validacion del mismo registro de L0; (L2) entrada
          efectiva de E2 de la cadena r1 = extracciones_finales_<to>.jsonl con la
          cola flaggeada inyectada según r1_cola_flaggeada.inyectar_cola
          (r1_cola_flaggeada.py:53-80), aceptados según e2_lib._estado_registro;
          (L3) grafo = r1/kg.json del ensamblado. El efecto del validador se
          mide L0→L1 sobre el mismo registro: el índice del elemento sale del
          campo detalle de validacion.rechazos («entities[i]»/«relations[i]»);
          un rechazo de nivel chunk rechaza todos sus elementos.
R-NORM    Normalización de texto para comparar un nombre con el texto del chunk:
          (1) se unen los cortes de palabra por guion de fin de línea,
          «(\\w)-\\s*\\n\\s*(\\w)» → «\\1\\2»; (2) NFKD sin marcas combinantes;
          (3) minúsculas; (4) todo carácter no alfanumérico pasa a espacio y los
          espacios se colapsan. Presencia = la aguja normalizada, entre límites
          de palabra (« aguja » dentro de « texto »), en el texto propio del
          chunk de E0 (campo texto) o en el heredado (herencia[].texto).
R-FORZ    «Posible forzado»: relación aplica_a o ejecuta del crudo L0 con
          sujeto_id del bloque v3 cuyo nombre no está presente (R-NORM) en el
          texto propio ni heredado del chunk. Variante principal (amplia): las
          agujas son el label, el label sin paréntesis, cada alias y, si el id no
          es un rol, el contenido de cada paréntesis del label; agujas y texto
          se singularizan token a token con r1_e4._singular. Variante estricta
          (sensibilidad): solo label y alias, sin singularizar. La unidad es el
          par (chunk, sujeto_id). Categorías, en este orden de precedencia:
          (1) sujeto por defecto del TO (rol_id o clase_ids de la tabla TO→rol
          del perfil para el archivo del TO), que el prompt prescribe para el
          colectivo («Si la norma se dirige al colectivo del TO…»,
          prompt_e1.py:110, heredado por el prefijo v3); (2) rol de alcance de
          otro TO; (3) el resto de clases e instancias. Es un indicador, no un
          veredicto. En r1, un id que no está en el bloque v3
          se cuenta como «sin entrada en el bloque v3».
R-LIT     sujeto_propuesto literal: el texto de sujeto_propuesto, normalizado
          con R-NORM (sin singularizar), está presente en el texto propio o
          heredado del chunk. Se mide en L0 y en L2, por TO y por grupo.
          Descripción posterior, agregada tras la primera corrida de prueba y
          que no cambia la regla: de los ausentes, cuántos tienen cada token
          normalizado en el texto (en cualquier orden, no contiguos).
R-MUESTRA Muestra de 30 posibles forzados: población = pares (chunk,
          sujeto_id) de la tanda 0 (diez TOs, crudo L0; es el perfil que r2
          modifica) marcados por R-FORZ amplia, con sujeto_id de nivel clase o
          instancia y distinto del sujeto por defecto del TO; orden por
          (chunk_id, sujeto_id); random.Random(20260930).sample(población, 30);
          el CSV sigue el orden de extracción; las columnas de lectura van
          vacías.
R-CAT     Catálogo (ii) de la re-resolución: esquema_v3_clases.json más los ids
          del bloque v3 del perfil que no están en el JSON, con label y nivel
          del perfil (labels_catalogo) y sin alias; los roles con miembros
          vacíos. Misma construcción que reports/u_pre_r2/upre_d1_suite.py:530-537
          (d1_suite.md:10). r1_e4.resolver_label se corre por import, sin
          editar, sobre (label, padre_sugerido) de cada fila de
          e4_propuestos.json. Con el catálogo (i) debe reproducir la tabla
          guardada (control: si no, FRENO). Contrafáctico, no resultado.
R-OMIS    Omisiones: unidad con omisiones_no_prosa no vacío (al menos un string
          no vacío; en L0 se cuenta aparte la forma string, que el validador
          descarta, validador_e1.py:154-156). Marca de E0: flags.contenido_tabular
          (tabla) y flags.formula (fórmula). La capa «finales» es la del comando
          [c15]: extracciones_finales_<to>.jsonl, validacion.omisiones_no_prosa.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import random
import re
import sqlite3
import sys
import unicodedata
import urllib.parse
from collections import Counter, OrderedDict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
REX = RAIZ / "data" / "experiment" / "reextraccion_v2"
for _p in (REX / "e1_extractor", REX / "corpus_v2", REX / "e2_reduce",
           RAIZ / "data" / "experiment" / "grafo_v2" / "code",
           RAIZ / "data" / "experiment" / "b54_catalogo_v3" / "code"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import perfil_e1                      # noqa: E402  (solo import)
import prompt_e1                      # noqa: E402
import prompt_v3_b54 as V3            # noqa: E402
import r1_e4 as E4                    # noqa: E402
from e2_lib import _estado_registro   # noqa: E402

COMANDO = ("PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B "
           "reports/u_listas_nomap/u_listas_n1.py --out-dir reports/u_listas_nomap")
SEMILLA = 20260930
N_MUESTRA = 30

TOS_R1 = ("cap", "cla", "ext", "pro", "ric")
TOS_DEV = ("cap", "cla", "ext", "pro", "ric")
TOS_CINCO = ("ctacte", "docvig", "lingob", "pagjub", "polcre")
TOS_DIEZ = tuple(sorted(TOS_DEV + TOS_CINCO))

NS_R1 = "e1_extraccion|cv=e1-extractor-v1-p4793d6152608|think=0"
NS_T0 = "e1_extraccion|cv=e1-extractor-v1-p54a111e2175f|think=0"

GEN = OrderedDict([
    ("r1", {"base": "data/experiment/reextraccion_v2/corpus_v2/salida", "tos": TOS_R1,
            "ns": NS_R1, "perfil": "produccion_dev"}),
    ("t0", {"base": "data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida",
            "tos": TOS_DIEZ, "ns": NS_T0, "perfil": "v3_b54"}),
])
GRUPOS = OrderedDict([
    ("r1", {"gen": "r1", "tos": TOS_R1, "ens": "data/experiment/reextraccion_v2/corpus_v2/salida_r1",
            "grafo": "KG-Reextraído-r1", "unidades_e0": 1763}),
    ("desarrollo", {"gen": "t0", "tos": TOS_DEV,
                    "ens": "data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1",
                    "grafo": "KG-Tanda0-Desarrollo-r1", "unidades_e0": 1763}),
    ("cinco", {"gen": "t0", "tos": TOS_CINCO,
               "ens": "data/experiment/reextraccion_v2/corpus_tanda0/ens_cinco/r1",
               "grafo": "ensamblado de la tanda 0 sola", "unidades_e0": 671}),
    ("diez", {"gen": "t0", "tos": TOS_DIEZ,
              "ens": "data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1",
              "grafo": "KG-Tanda0-Diez-r1", "unidades_e0": 2434}),
])
E0_DIR = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0"
E0_ENM01 = "data/experiment/reextraccion_v2/e0_chunking/salida_enm01"
DB_REINTENTOS = "data/experiment/reextraccion_v2/e3_verificador/cache/e1_reintentos.db"
CATALOGO_JSON = "data/experiment/esq_v3_miembros/esquema_v3_clases.json"

RESTRICCION_TIPO = ("prohibicion", "limite_cuantitativo", "limite_cualitativo")
COMUNICACION_TIPO = ("A", "B", "C")
CLAVES_ADMITIDAS = OrderedDict([
    ("Comunicacion", ("codigo", "tipo", "numero")),
    ("TextoOrdenado", ("materia", "archivo", "version")),
    ("Operacion", ("tipo", "descripcion")),
    ("Restriccion", ("descripcion", "tipo", "umbral")),
    ("Excepcion", ("descripcion",)),
    ("Obligacion", ("descripcion", "tipo", "plazo", "frecuencia")),
    ("Potestad", ("descripcion",)),
    ("Condicion", ("descripcion",)),
    ("Definicion", ("termino", "descripcion")),
])
CLAVES_PIPELINE = ("cola_humana", "cola_chunks", "estado_e3", "colision_cross_to",
                   "materia_variantes", "version_variantes")
SUJ_PREDS = ("aplica_a", "ejecuta")
CATEGORIAS_FORZ = ("otra_clase_o_instancia", "defecto_del_to", "rol_no_defecto", "sin_entrada_en_bloque_v3")

# Esperados del tablero (criterio de aceptación del mandato) sobre desarrollo.
ESPERADO_TABLERO = {"Restriccion.tipo": 4, "Comunicacion.tipo": 6, "claves": 9,
                    "propuestos": 22, "resueltos": 3, "cuarentena": 19,
                    "solo_bloque": 6, "solo_json": 5}

LISTAS = ("tipo_entidad", "predicado", "sujeto_id", "padre_sugerido", "Obligacion.tipo",
          "Restriccion.tipo", "Comunicacion.tipo", "claves")
MOTIVO_A_LISTA = {
    "type_invalido": "tipo_entidad",
    "predicado_invalido": "predicado",
    "sujeto_id_fuera_de_catalogo": "sujeto_id",
    "sujeto_extremo_invalido": "sujeto_id",
    "padre_sugerido_sin_propuesto": "padre_sugerido",
    "sujeto_en_predicado_no_sujeto": "sujeto_id",
    "firma_invalida": "tipo_entidad×predicado (matriz)",
}


class Freno(SystemExit):
    pass


# --------------------------------------------------------------------------- #
# utilidades                                                                   #
# --------------------------------------------------------------------------- #
def sha256_path(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def leer_jsonl(p: Path) -> list:
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def orden(c: Counter) -> list:
    return [[k, v] for k, v in sorted(c.items(), key=lambda kv: (-kv[1], str(kv[0])))]


def cadena(v) -> str:
    """Valor de un campo como string ('' si ausente); el validador hace str(v)."""
    if v is None:
        return ""
    return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)


def str_o_none(v):
    if isinstance(v, str):
        v = v.strip()
        return v or None
    return None


def coerce_lista(v):
    if isinstance(v, str):
        try:
            v = json.loads(v)
        except json.JSONDecodeError:
            return None
    return v if isinstance(v, list) else None


_GUION = re.compile(r"(\w)-\s*\n\s*(\w)")
_NOALNUM = re.compile(r"[^0-9a-z]+")


def norm_txt(s: str) -> str:
    s = _GUION.sub(r"\1\2", s or "")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return _NOALNUM.sub(" ", s).strip()


def singularizar(s: str) -> str:
    return " ".join(E4._singular(w) for w in s.split())


def presente(aguja: str, texto_pad: str) -> bool:
    return bool(aguja) and f" {aguja} " in texto_pad


# --------------------------------------------------------------------------- #
# catálogo: bloque v3 y JSON                                                   #
# --------------------------------------------------------------------------- #
def parse_bloque(texto: str) -> OrderedDict:
    out, grupo = OrderedDict(), None
    for linea in texto.split("\n"):
        if linea.startswith("## "):
            grupo = linea[3:].strip()
            continue
        if not (linea.startswith("Sujeto_") and " — " in linea):
            continue
        sid, resto = linea.split(" — ", 1)
        to = None
        m = re.search(r" \[rol del TO (.+?)\]$", resto)
        if m:
            nivel, to, resto = "rol", m.group(1), resto[:m.start()]
        elif resto.endswith(" [instancia]"):
            nivel, resto = "instancia", resto[: -len(" [instancia]")]
        else:
            nivel = "clase"
        alias = []
        if " (alias: " in resto:
            resto, a = resto.split(" (alias: ", 1)
            if not a.endswith(")"):
                raise Freno(f"FRENO: alias sin cierre en la línea del bloque de {sid}")
            alias = [x.strip() for x in a[:-1].split(", ") if x.strip()]
        out[sid] = {"label": resto.strip(), "alias": alias, "nivel": nivel, "grupo": grupo, "to": to}
    return out


def agujas(entrada: dict, amplia: bool) -> list:
    base = [entrada["label"]] + list(entrada["alias"])
    if amplia:
        base.append(E4._sin_parentesis(entrada["label"]))
        if entrada["nivel"] != "rol":
            base += re.findall(r"\(([^)]+)\)", entrada["label"])
    out = []
    for a in base:
        n = norm_txt(a)
        if amplia:
            n = singularizar(n)
        if n and n not in out:
            out.append(n)
    return out


# --------------------------------------------------------------------------- #
# listas y guarda contra el prefijo                                            #
# --------------------------------------------------------------------------- #
def listas_v3(perfil) -> dict:
    esq = perfil.esquema
    pref = V3.PREFIJO_SISTEMA_V3
    if 'tipo ("prohibicion"|"limite_cuantitativo"|"limite_cualitativo")' not in pref:
        raise Freno("FRENO: Restriccion.tipo del prefijo v3 no coincide con [c11]")
    if 'tipo ("A"|"B"|"C")' not in pref:
        raise Freno("FRENO: Comunicacion.tipo del prefijo v3 no coincide con [c11]")
    secc = pref[pref.find("# TIPOS DE ENTIDAD"): pref.find("# PREDICADOS")]
    for t, claves in CLAVES_ADMITIDAS.items():
        m = re.search(r"\d\. \*\*" + t + r"\*\*.*?\n\s+Properties: ([^\n]+)", secc, re.S)
        if not m:
            raise Freno(f"FRENO: sin línea Properties para {t} en el prefijo v3")
        linea = m.group(1)
        for k in claves:
            if not re.search(r"\b" + k + r"\b", linea):
                raise Freno(f"FRENO: la clave {k} de {t} no está en la línea Properties del prefijo v3")
    return {"tipo_entidad": tuple(esq.entity_types), "predicado": tuple(esq.predicates),
            "sujeto_id": frozenset(esq.sujetos_catalogo_set),
            "Obligacion.tipo": tuple(esq.obligacion_tipo_enum),
            "Restriccion.tipo": RESTRICCION_TIPO, "Comunicacion.tipo": COMUNICACION_TIPO,
            "claves": CLAVES_ADMITIDAS}


def listas_v2() -> dict:
    pref = prompt_e1.PREFIJO_SISTEMA
    secc = pref[pref.find("6. **Obligacion**"): pref.find("# PREDICADOS")]
    m = re.search(r'tipo \(("[a-z_]+"(?:\|"[a-z_]+")*)\)', secc)
    if not m:
        raise Freno("FRENO: sin enum de Obligacion.tipo en el prefijo v2")
    ob = tuple(re.findall(r'"([a-z_]+)"', m.group(1)))
    claves = OrderedDict((t, CLAVES_ADMITIDAS[t]) for t in prompt_e1.ENTITY_TYPES)
    claves["Operacion"] = ("tipo",)
    if "Properties: tipo (string).\n" not in pref:
        raise Freno("FRENO: Operacion del prefijo v2 no es {tipo}")
    return {"tipo_entidad": tuple(prompt_e1.ENTITY_TYPES), "predicado": tuple(prompt_e1.PREDICATES),
            "sujeto_id": frozenset(prompt_e1.SUJETOS_CATALOGO), "Obligacion.tipo": ob,
            "Restriccion.tipo": RESTRICCION_TIPO, "Comunicacion.tipo": COMUNICACION_TIPO,
            "claves": claves}


# --------------------------------------------------------------------------- #
# elementos por capa                                                           #
# --------------------------------------------------------------------------- #
def elementos_crudo(tool_input):
    """(entidades, relaciones, estado) del crudo, con el índice original."""
    if isinstance(tool_input, str):
        try:
            tool_input = json.loads(tool_input)
        except json.JSONDecodeError:
            return [], [], "no_parseable"
    if not isinstance(tool_input, dict):
        return [], [], "no_dict"
    ents, rels = coerce_lista(tool_input.get("entities")), coerce_lista(tool_input.get("relations"))
    estado = "ok" if ents is not None and rels is not None else "entities_o_relations_invalidos"
    E = [(i, e) for i, e in enumerate(ents or []) if isinstance(e, dict)]
    R = [(i, r) for i, r in enumerate(rels or []) if isinstance(r, dict)]
    return E, R, estado


def elementos_validados(val):
    if not isinstance(val, dict):
        return [], []
    return list(enumerate(val.get("entidades") or [])), list(enumerate(val.get("relaciones") or []))


def contar(E, R, L, crudo: bool) -> OrderedDict:
    """Conteos por lista de una colección de elementos (una capa, un chunk)."""
    c = OrderedDict((k, Counter()) for k in ("tipo_entidad", "predicado", "sujeto_id",
                                             "Obligacion.tipo", "Restriccion.tipo",
                                             "Comunicacion.tipo", "claves", "Operacion.tipo"))
    fuera = OrderedDict((k, Counter()) for k in c)
    forma = Counter()
    for _, e in E:
        t = cadena(e.get("type"))
        c["tipo_entidad"][t] += 1
        if t not in L["tipo_entidad"]:
            fuera["tipo_entidad"][t] += 1
            continue
        props = e.get("properties")
        if not isinstance(props, dict):
            props = {}
        for campo in ("Obligacion.tipo", "Restriccion.tipo", "Comunicacion.tipo"):
            tipo_ent = campo.split(".")[0]
            if t == tipo_ent:
                v = cadena(props.get("tipo"))
                c[campo][v] += 1
                if v not in L[campo]:
                    fuera[campo][v] += 1
        if t == "Operacion":
            c["Operacion.tipo"][cadena(props.get("tipo"))] += 1
        adm = L["claves"].get(t, ())
        for k in props:
            if k in CLAVES_PIPELINE:
                continue
            c["claves"][f"{t}.{k}"] += 1
            if k not in adm:
                fuera["claves"][f"{t}.{k}"] += 1
    for _, r in R:
        p = cadena(r.get("predicate"))
        c["predicado"][p] += 1
        if p not in L["predicado"]:
            fuera["predicado"][p] += 1
        sid = str_o_none(r.get("sujeto_id"))
        sp = str_o_none(r.get("sujeto_propuesto"))
        pad = str_o_none(r.get("sujeto_propuesto_padre_sugerido"))
        if sid is not None:
            c["sujeto_id"][sid] += 1
            if sid not in L["sujeto_id"]:
                fuera["sujeto_id"][sid] += 1
        if p in SUJ_PREDS:
            forma[("solo_sujeto_id" if sid and not sp else "solo_sujeto_propuesto" if sp and not sid
                   else "ambos" if sid and sp else "ninguno")] += 1
            if sp:
                if pad is None:
                    forma["propuesto_sin_padre"] += 1
                elif pad in L["sujeto_id"]:
                    forma["propuesto_padre_en_catalogo"] += 1
                else:
                    forma["propuesto_padre_fuera_de_catalogo"] += 1
            elif pad:
                forma["padre_sin_propuesto"] += 1
        elif sid or sp or pad:
            forma["sujeto_en_predicado_no_sujeto"] += 1
    return c, fuera, forma


def indices_rechazados(val) -> tuple[dict, dict, str | None]:
    """{índice: motivo} para entities y relations, desde validacion.rechazos."""
    ent, rel, chunk = {}, {}, None
    for r in (val or {}).get("rechazos") or []:
        if r.get("nivel") == "chunk":
            chunk = r.get("motivo")
            continue
        m = re.match(r"(entities|relations)\[(\d+)\]", r.get("detalle") or "")
        if not m:
            continue
        (ent if m.group(1) == "entities" else rel).setdefault(int(m.group(2)), r.get("motivo"))
    return ent, rel, chunk


def correspondencia(elems, rechazados: dict, rchunk, validados: list) -> dict:
    """{índice crudo: elemento validado}. El validador agrega los elementos
    aceptados en el orden del crudo (validador_e1.py:160-242 y :250-373), así
    que los índices no rechazados, en orden, se aparean uno a uno con la lista
    validada. Si las longitudes no coinciden no hay correspondencia ({})."""
    if rchunk:
        return {}
    acept = [i for i, _ in elems if i not in rechazados]
    if len(acept) != len(validados):
        return {}
    return dict(zip(acept, validados))


def efecto_validador(E, R, val, L) -> dict:
    """Estado de cada valor fuera de lista del crudo tras el validador (mismo
    registro), observado en el elemento validado correspondiente."""
    rent, rrel, rchunk = indices_rechazados(val)
    ven, vre = elementos_validados(val)
    cen = correspondencia(E, rent, rchunk, [x for _, x in ven])
    cre = correspondencia(R, rrel, rchunk, [x for _, x in vre])
    out = OrderedDict((k, Counter()) for k in LISTAS)
    out["sin_correspondencia"] = Counter()
    for i, e in E:
        t = cadena(e.get("type"))
        motivo = rchunk or rent.get(i)
        estado = f"rechazado:{motivo}" if motivo else None
        par = cen.get(i)
        if estado is None and par is None:
            estado = "sin_correspondencia"
            out["sin_correspondencia"]["entidad"] += 1
        if t not in L["tipo_entidad"]:
            out["tipo_entidad"][estado or "paso"] += 1
            continue
        props = e.get("properties") if isinstance(e.get("properties"), dict) else {}
        vprops = (par or {}).get("properties") or {}
        for campo in ("Obligacion.tipo", "Restriccion.tipo", "Comunicacion.tipo"):
            if t == campo.split(".")[0]:
                v = cadena(props.get("tipo"))
                if v not in L[campo]:
                    if estado:
                        out[campo][estado] += 1
                    else:
                        vv = cadena(vprops.get("tipo"))
                        out[campo]["paso" if vv == v else "normalizado_a_otra" if vv == "otra"
                                   else f"cambiado_a:{vv}"] += 1
        for k in props:
            if k not in CLAVES_PIPELINE and k not in L["claves"].get(t, ()):
                out["claves"][estado or ("paso" if k in vprops else "eliminada")] += 1
    for i, r in R:
        p = cadena(r.get("predicate"))
        motivo = rchunk or rrel.get(i)
        estado = f"rechazado:{motivo}" if motivo else None
        par = cre.get(i)
        if estado is None and par is None:
            estado = "sin_correspondencia"
            out["sin_correspondencia"]["relacion"] += 1
        if p not in L["predicado"]:
            out["predicado"][estado or "paso"] += 1
        sid = str_o_none(r.get("sujeto_id"))
        if sid is not None and sid not in L["sujeto_id"]:
            out["sujeto_id"][estado or "paso"] += 1
        pad = str_o_none(r.get("sujeto_propuesto_padre_sugerido"))
        if pad is not None and pad not in L["sujeto_id"]:
            out["padre_sugerido"][estado or ("anulado_por_el_validador"
                                             if par.get("sujeto_propuesto_padre_sugerido") is None else "paso")] += 1
    return out


# --------------------------------------------------------------------------- #
# carga                                                                        #
# --------------------------------------------------------------------------- #
class Datos:
    def __init__(self):
        self.entradas = OrderedDict()
        self.chunks = {}
        self.to_archivo = {}
        self.texto_norm = {}
        self.texto_norm_sing = {}
        for to in TOS_DIEZ:
            p = RAIZ / E0_DIR / f"chunks_{to}.json"
            self._sello(f"e0_{to}", p)
            for ch in json.loads(p.read_text(encoding="utf-8")):
                self.chunks[ch["id"]] = ch
                self.to_archivo[ch["to"]] = ch["archivo"]
        self.e0_identico_enm01 = OrderedDict(
            (to, (RAIZ / E0_DIR / f"chunks_{to}.json").read_bytes()
             == (RAIZ / E0_ENM01 / f"chunks_{to}.json").read_bytes()) for to in TOS_R1)
        if not all(self.e0_identico_enm01.values()):
            raise Freno("FRENO: el E0 de la tanda 0 no es idéntico al de r1 (salida_enm01)")
        self.gen = OrderedDict()
        for g, cfg in GEN.items():
            base = RAIZ / cfg["base"]
            por_to = OrderedDict()
            for to in cfg["tos"]:
                pc = base / to / "extracciones_e1_compact.jsonl"
                pf = base / to / f"extracciones_finales_{to}.jsonl"
                pfi = base / to / "finales.jsonl"
                for k, p in (("compact", pc), ("finales_ext", pf), ("finales", pfi)):
                    self._sello(f"{g}_{to}_{k}", p)
                compact = leer_jsonl(pc)
                por_to[to] = {"compact": compact, "ext_finales": leer_jsonl(pf),
                              "finales": leer_jsonl(pfi)}
            self.gen[g] = por_to
        for g, cfg in GRUPOS.items():
            for nombre in ("kg.json", "e4_propuestos.json", "e5_esqueleto.json"):
                self._sello(f"{g}_{nombre}", RAIZ / cfg["ens"] / nombre)
        self._sello("catalogo_json_v3", RAIZ / CATALOGO_JSON)
        self._sello("prompt_v3_b54", RAIZ / "data/experiment/b54_catalogo_v3/code/prompt_v3_b54.py")
        self._sello("r1_e4", RAIZ / "data/experiment/reextraccion_v2/corpus_v2/r1_e4.py")
        self._sello("e1_reintentos_db", RAIZ / DB_REINTENTOS)
        self.reintentos = self._cargar_reintentos()

    def _sello(self, clave, p: Path):
        self.entradas[clave] = {"ruta": str(p.relative_to(RAIZ)), "sha256": sha256_path(p)}

    def _cargar_reintentos(self) -> OrderedDict:
        dbp = (RAIZ / DB_REINTENTOS).resolve()
        db = sqlite3.connect(f"file:{urllib.parse.quote(str(dbp))}?immutable=1", uri=True)
        out = OrderedDict()
        try:
            for g, cfg in GEN.items():
                filas = db.execute("select key, request_json, raw_json from cache where namespace = ? "
                                   "order by key", (cfg["ns"],)).fetchall()
                asignadas, no_asignadas, fuera_corpus = [], 0, Counter()
                for key, req, raw in filas:
                    msgs = json.loads(req).get("messages") or []
                    c0 = msgs[0]["content"] if msgs else ""
                    u = c0 if isinstance(c0, str) else " ".join(
                        b.get("text", "") for b in c0 if isinstance(b, dict))
                    m_to = re.search(r"^TO: (\S+)$", u, re.M)
                    m_pt = re.search(r"^Punto del chunk: (\S+)", u, re.M)
                    m_mc = re.search(r"MINI-CHUNK de bloque estructural \((\S+) del punto (\S+)\)", u)
                    if not m_to or not (m_pt or m_mc):
                        no_asignadas += 1
                        continue
                    to = m_to.group(1)
                    cid = f"{to}::{m_pt.group(1)}" if m_pt else f"{to}::{m_mc.group(2)}::{m_mc.group(1)}"
                    if to not in cfg["tos"]:
                        fuera_corpus[to] += 1
                        continue
                    if cid not in self.chunks:
                        no_asignadas += 1
                        continue
                    msg = json.loads(raw)
                    tis = [b.get("input") for b in (msg.get("content") or [])
                           if isinstance(b, dict) and b.get("type") == "tool_use"]
                    asignadas.append({"key": key, "chunk_id": cid, "to": to,
                                      "tool_input": tis[0] if tis else None})
                out[g] = {"namespace": cfg["ns"], "entradas": len(filas), "asignadas": asignadas,
                          "no_asignadas": no_asignadas, "fuera_del_corpus": dict(sorted(fuera_corpus.items()))}
        finally:
            db.close()
        return out

    def texto(self, cid: str, sing: bool) -> str:
        cache = self.texto_norm_sing if sing else self.texto_norm
        if cid not in cache:
            ch = self.chunks[cid]
            partes = [ch.get("texto") or ""] + [h.get("texto") or "" for h in ch.get("herencia") or []]
            n = norm_txt("\n".join(partes))
            cache[cid] = " " + (singularizar(n) if sing else n) + " "
        return cache[cid]


def entrada_e2(reg_to: dict) -> list:
    """Registros aceptados que entran a E2 en la cadena r1, con la cola flaggeada
    inyectada (réplica de la regla de r1_cola_flaggeada.inyectar_cola, :53-80)."""
    fin = {f["chunk_id"]: f for f in reg_to["finales"]}
    e1 = {r["chunk_id"]: r for r in reg_to["compact"]}
    cola = {cid for cid, f in fin.items() if f.get("validacion_final") is None}
    out = []
    for r in reg_to["ext_finales"]:
        cid = r["chunk_id"]
        if cid in cola:
            base = e1.get(cid)
            val = (base or {}).get("validacion")
            rch = bool(val) and any(x.get("nivel") == "chunk" for x in val.get("rechazos", []))
            if not (base is None or base.get("error") or not val or rch):
                r = {"chunk_id": cid, "error": None, "estado_e3": fin[cid]["estado"],
                     "cola_humana": True, "validacion": val}
        if _estado_registro(r)[0] == "aceptado":
            out.append(r)
    return out


# --------------------------------------------------------------------------- #
# mediciones                                                                   #
# --------------------------------------------------------------------------- #
def sumar(dst: dict, src: dict):
    for k, v in src.items():
        dst.setdefault(k, Counter()).update(v)


def inventario_por_to(D: Datos, L3: dict, L2v: dict) -> OrderedDict:
    res = OrderedDict()
    for g, por_to in D.gen.items():
        res[g] = OrderedDict()
        reint_por_to = {}
        for a in D.reintentos[g]["asignadas"]:
            reint_por_to.setdefault(a["to"], []).append(a)
        for to, reg in por_to.items():
            capas = OrderedDict()
            for capa in ("crudo", "validado_e1", "reintentos_crudo", "entrada_e2"):
                capas[capa] = {"conteos": {}, "fuera": {}, "forma_sujeto": Counter(), "registros": 0,
                               "estados_crudo": Counter()}
            efecto = OrderedDict((k, Counter()) for k in LISTAS)
            efecto_v2 = OrderedDict((k, Counter()) for k in LISTAS)
            motivos = Counter()
            advert = Counter()
            for r in reg["compact"]:
                E, R, est = elementos_crudo(r.get("tool_input_crudo"))
                cap = capas["crudo"]
                cap["registros"] += 1
                cap["estados_crudo"][est if not r.get("error") else f"error:{r['error']}"] += 1
                c, f, fo = contar(E, R, L3, True)
                sumar(cap["conteos"], c); sumar(cap["fuera"], f); cap["forma_sujeto"].update(fo)
                val = r.get("validacion")
                sumar(efecto, efecto_validador(E, R, val, L3))
                if g == "r1":
                    sumar(efecto_v2, efecto_validador(E, R, val, L2v))
                Ev, Rv = elementos_validados(val)
                cv = capas["validado_e1"]
                cv["registros"] += 1
                c, f, fo = contar(Ev, Rv, L3, False)
                sumar(cv["conteos"], c); sumar(cv["fuera"], f); cv["forma_sujeto"].update(fo)
                for x in (val or {}).get("rechazos") or []:
                    motivos[(x.get("nivel"), x.get("motivo"))] += 1
                for x in (val or {}).get("advertencias") or []:
                    advert[x.get("tipo")] += 1
            for a in reint_por_to.get(to, []):
                E, R, est = elementos_crudo(a["tool_input"])
                cap = capas["reintentos_crudo"]
                cap["registros"] += 1
                cap["estados_crudo"][est] += 1
                c, f, fo = contar(E, R, L3, True)
                sumar(cap["conteos"], c); sumar(cap["fuera"], f); cap["forma_sujeto"].update(fo)
            for r in entrada_e2(reg):
                Ev, Rv = elementos_validados(r.get("validacion"))
                cap = capas["entrada_e2"]
                cap["registros"] += 1
                c, f, fo = contar(Ev, Rv, L3, False)
                sumar(cap["conteos"], c); sumar(cap["fuera"], f); cap["forma_sujeto"].update(fo)
            res[g][to] = {"capas": capas, "efecto_validador": efecto,
                          "efecto_validador_perfil_v2": efecto_v2 if g == "r1" else None,
                          "motivos_rechazo": motivos, "advertencias": advert}
    return res


def agregar_grupo(inv_to: OrderedDict, grupo: str) -> OrderedDict:
    cfg = GRUPOS[grupo]
    capas, efecto, efecto_v2, motivos, advert = OrderedDict(), OrderedDict(), OrderedDict(), Counter(), Counter()
    for to in cfg["tos"]:
        x = inv_to[cfg["gen"]][to]
        for capa, d in x["capas"].items():
            a = capas.setdefault(capa, {"conteos": {}, "fuera": {}, "forma_sujeto": Counter(),
                                        "registros": 0, "estados_crudo": Counter()})
            sumar(a["conteos"], d["conteos"]); sumar(a["fuera"], d["fuera"])
            a["forma_sujeto"].update(d["forma_sujeto"]); a["registros"] += d["registros"]
            a["estados_crudo"].update(d["estados_crudo"])
        sumar(efecto, x["efecto_validador"])
        if x["efecto_validador_perfil_v2"] is not None:
            sumar(efecto_v2, x["efecto_validador_perfil_v2"])
        motivos.update(x["motivos_rechazo"]); advert.update(x["advertencias"])
    return OrderedDict([("capas", capas), ("efecto_validador", efecto),
                        ("efecto_validador_perfil_v2", efecto_v2 or None),
                        ("motivos_rechazo", motivos), ("advertencias", advert)])


def grafo_c11(kg: dict, L: dict, bloque_ids: set, json_ids: set) -> OrderedDict:
    N, Ed = kg["nodes"], kg["edges"]
    rf = lambda e: e.get("rol_fuente") or (e.get("properties") or {}).get("rol_fuente")  # noqa: E731
    out = OrderedDict()
    tipos = Counter(n["type"] for n in N)
    out["tipo_entidad"] = {"valores": orden(tipos),
                           "fuera": orden(Counter({t: v for t, v in tipos.items()
                                                   if t not in L["tipo_entidad"] and t != "Sujeto"}))}
    preds = Counter((e["relation"], rf(e) or "") for e in Ed)
    out["predicado"] = {"valores": orden(Counter(e["relation"] for e in Ed)),
                        "fuera_por_rol_fuente": orden(Counter({f"{p}|{r}": v for (p, r), v in preds.items()
                                                               if p not in L["predicado"]}))}
    for campo, enum in (("Obligacion.tipo", L["Obligacion.tipo"]), ("Restriccion.tipo", L["Restriccion.tipo"]),
                        ("Comunicacion.tipo", L["Comunicacion.tipo"])):
        t = campo.split(".")[0]
        vals = Counter(cadena((n.get("properties") or {}).get("tipo")) for n in N if n["type"] == t)
        out[campo] = {"valores": orden(vals), "fuera": orden(Counter({v: c for v, c in vals.items() if v not in enum}))}
    cl, clf = Counter(), Counter()
    for n in N:
        if n["type"] == "Sujeto":
            continue
        for k in n.get("properties") or {}:
            if k in CLAVES_PIPELINE:
                continue
            cl[f"{n['type']}.{k}"] += 1
            if k not in L["claves"].get(n["type"], ()):
                clf[f"{n['type']}.{k}"] += 1
    out["claves"] = {"valores": orden(cl), "fuera": orden(clf)}
    out["Operacion.tipo"] = {"distintos": len({cadena((n.get("properties") or {}).get("tipo"))
                                               for n in N if n["type"] == "Operacion"}),
                             "nodos": sum(1 for n in N if n["type"] == "Operacion")}
    suj = [n for n in N if n["type"] == "Sujeto"]
    out["sujetos_nodos"] = OrderedDict([
        ("total", len(suj)),
        ("en_bloque_v3", sum(1 for n in suj if n["id"] in bloque_ids)),
        ("solo_en_json_v3", sorted(n["id"] for n in suj if n["id"] in json_ids and n["id"] not in bloque_ids)),
        ("propuestos", sum(1 for n in suj if (n.get("properties") or {}).get("nivel") == "propuesto")),
        ("otros", sorted(n["id"] for n in suj if n["id"] not in bloque_ids and n["id"] not in json_ids
                         and (n.get("properties") or {}).get("nivel") != "propuesto")),
    ])
    sj = [e for e in Ed if e["relation"] in SUJ_PREDS and rf(e) != "esqueleto"]
    ext = lambda e: e["target"] if e["relation"] == "aplica_a" else e["source"]  # noqa: E731
    ids_prop = {n["id"] for n in suj if (n.get("properties") or {}).get("nivel") == "propuesto"}
    out["aristas_sujeto_no_esqueleto"] = OrderedDict([
        ("total", len(sj)),
        ("a_id_de_catalogo", sum(1 for e in sj if ext(e) not in ids_prop)),
        ("a_propuesto_en_cuarentena", sum(1 for e in sj if ext(e) in ids_prop)),
        ("con_mencion_textual_guardada", sum(1 for e in sj if "mencion" in json.dumps(e.get("properties") or {}))),
    ])
    return out


def resumen_lista(g: OrderedDict, lista: str) -> OrderedDict:
    caps = g["capas"]
    def f(capa):
        return sum(caps[capa]["fuera"].get(lista, Counter()).values()) if lista in caps[capa]["fuera"] else 0
    def e(capa):
        return sum(caps[capa]["conteos"].get(lista, Counter()).values()) if lista in caps[capa]["conteos"] else 0
    ef = g["efecto_validador"].get(lista, Counter())
    return OrderedDict([
        ("emitidos_crudo", e("crudo")), ("fuera_crudo", f("crudo")),
        ("validador_rechazados", sum(v for k, v in ef.items() if k.startswith("rechazado:"))),
        ("validador_normalizados", ef.get("normalizado_a_otra", 0)),
        ("validador_anulados", ef.get("anulado_por_el_validador", 0)),
        ("validador_pasaron", ef.get("paso", 0)),
        ("fuera_validado_e1", f("validado_e1")),
        ("emitidos_reintentos_crudo", e("reintentos_crudo")), ("fuera_reintentos_crudo", f("reintentos_crudo")),
        ("fuera_entrada_e2", f("entrada_e2")),
    ])


def sujetos(D: Datos, bloque: OrderedDict, perfiles: dict) -> OrderedDict:
    """Posibles forzados (R-FORZ) y sujeto_propuesto literal (R-LIT)."""
    agu_a = {sid: agujas(e, True) for sid, e in bloque.items()}
    agu_e = {sid: agujas(e, False) for sid, e in bloque.items()}
    pares = OrderedDict()   # (gen, chunk, sid) -> info
    lit = OrderedDict()
    for g, por_to in D.gen.items():
        rol_por_to = perfiles[GEN[g]["perfil"]].rol_por_to
        for to, reg in por_to.items():
            porder = rol_por_to.get(D.to_archivo[to]) or {}
            defecto = set(filter(None, [porder.get("rol_id")] + list(porder.get("clase_ids") or [])))
            for capa, registros in (("crudo", [(r["chunk_id"], r.get("tool_input_crudo")) for r in reg["compact"]]),
                                    ("entrada_e2", [(r["chunk_id"], {"relations": [
                                        {"predicate": x.get("predicate"), "sujeto_propuesto": x.get("sujeto_propuesto"),
                                         "sujeto_id": x.get("sujeto_id")} for x in (r["validacion"].get("relaciones") or [])],
                                        "entities": []}) for r in entrada_e2(reg)])):
                for cid, ti in registros:
                    E, R, _ = elementos_crudo(ti)
                    by_local = {str_o_none(e.get("local_id")): e for _, e in E}
                    for _, r in R:
                        p = cadena(r.get("predicate"))
                        if p not in SUJ_PREDS:
                            continue
                        sp = str_o_none(r.get("sujeto_propuesto"))
                        if sp is not None:
                            k = (g, to, capa)
                            d = lit.setdefault(k, Counter())
                            d["total"] += 1
                            nsp, tx = norm_txt(sp), D.texto(cid, False)
                            if presente(nsp, tx):
                                d["presente"] += 1
                            else:
                                d["ausente"] += 1
                                if nsp and all(f" {w} " in tx for w in nsp.split()):
                                    d["ausente_con_todos_los_tokens"] += 1
                        if capa != "crudo":
                            continue
                        sid = str_o_none(r.get("sujeto_id"))
                        if sid is None:
                            continue
                        k = (g, cid, sid)
                        if k not in pares:
                            if sid not in bloque:
                                cat = "sin_entrada_en_bloque_v3"
                                pa = pe = None
                            else:
                                pa = any(presente(a, D.texto(cid, True)) for a in agu_a[sid])
                                pe = any(presente(a, D.texto(cid, False)) for a in agu_e[sid])
                                cat = ("defecto_del_to" if sid in defecto else
                                       "rol_no_defecto" if bloque[sid]["nivel"] == "rol" else
                                       "otra_clase_o_instancia")
                            pares[k] = {"gen": g, "to": to, "chunk_id": cid, "sujeto_id": sid,
                                        "categoria": cat, "presente_amplia": pa, "presente_estricta": pe,
                                        "n_rel": 0, "predicados": set(), "elementos": set()}
                        x = pares[k]
                        x["n_rel"] += 1
                        x["predicados"].add(p)
                        extremo = by_local.get(str_o_none(r.get("source") if p == "aplica_a" else r.get("target")))
                        if extremo is not None:
                            x["elementos"].add(f"{cadena(extremo.get('type'))}: {cadena(extremo.get('label'))}")
    return pares, lit


def tabla_forzados(pares, grupo: str, bloque) -> OrderedDict:
    cfg = GRUPOS[grupo]
    sel = [x for x in pares.values() if x["gen"] == cfg["gen"] and x["to"] in cfg["tos"]]
    out = OrderedDict()
    out["relaciones_con_sujeto_id"] = sum(x["n_rel"] for x in sel)
    out["pares_chunk_sujeto"] = len(sel)
    for cat in CATEGORIAS_FORZ:
        s = [x for x in sel if x["categoria"] == cat]
        out[cat] = OrderedDict([
            ("pares", len(s)),
            ("posibles_forzados_amplia", sum(1 for x in s if x["presente_amplia"] is False)),
            ("posibles_forzados_estricta", sum(1 for x in s if x["presente_estricta"] is False)),
        ])
    por_id, tot_id = Counter(), Counter()
    for x in sel:
        if x["categoria"] == "otra_clase_o_instancia":
            tot_id[x["sujeto_id"]] += 1
            if x["presente_amplia"] is False:
                por_id[x["sujeto_id"]] += 1
    out["top_ids_otra_clase_o_instancia"] = [[sid, n, tot_id[sid]] for sid, n in orden(por_id)[:15]]
    return out


def muestra(pares) -> tuple[list, int]:
    pob = sorted(((x["chunk_id"], x["sujeto_id"]) for x in pares.values()
                  if x["gen"] == "t0" and x["categoria"] == "otra_clase_o_instancia"
                  and x["presente_amplia"] is False))
    if len(pob) < N_MUESTRA:
        raise Freno(f"FRENO: población de la muestra {len(pob)} < {N_MUESTRA}")
    return random.Random(SEMILLA).sample(pob, N_MUESTRA), len(pob)


def reresolucion(D: Datos, perfil_v3) -> OrderedDict:
    cat_i = json.loads((RAIZ / CATALOGO_JSON).read_text(encoding="utf-8"))
    ids_json = {e["id"] for e in cat_i["clases"]} | {r["id"] for r in cat_i["roles"]}
    bloque = perfil_v3.labels_catalogo
    faltan = sorted(set(bloque) - ids_json)
    cat_ii = copy.deepcopy(cat_i)
    for i in faltan:
        ent = {"id": i, "label": bloque[i]["label"], "nivel": bloque[i]["nivel"]}
        (cat_ii.setdefault("roles", []) if bloque[i]["nivel"] == "rol" else cat_ii.setdefault("clases", [])).append(
            dict(ent, miembros=[]) if bloque[i]["nivel"] == "rol" else ent)
    idx_i, idx_ii = E4.indice_catalogo(cat_i), E4.indice_catalogo(cat_ii)
    out = OrderedDict([("ids_agregados_en_ii", faltan)])
    for grupo in ("desarrollo", "cinco", "diez"):
        filas = json.loads((RAIZ / GRUPOS[grupo]["ens"] / "e4_propuestos.json").read_text(encoding="utf-8"))
        det, n_i, n_ii = [], 0, 0
        for f in filas:
            ri, mi, _ = E4.resolver_label(f["label"], f.get("padre_sugerido"), idx_i)
            rii, mii, _ = E4.resolver_label(f["label"], f.get("padre_sugerido"), idx_ii)
            if ri != f.get("resuelto_a"):
                raise Freno(f"FRENO: el catálogo (i) no reproduce e4_propuestos.json de {grupo}: {f['id_propuesto']}")
            n_i += ri is not None
            n_ii += rii is not None
            if rii is not None or ri is not None:
                det.append([f["label"], f.get("padre_sugerido"), ri, mi, rii, mii])
        out[grupo] = OrderedDict([("propuestos", len(filas)),
                                  ("guardado_resueltos", sum(1 for f in filas if f["estado"] == "resuelto")),
                                  ("guardado_cuarentena", sum(1 for f in filas if f["estado"] == "cuarentena")),
                                  ("resuelven_catalogo_i", n_i), ("resuelven_catalogo_ii", n_ii),
                                  ("resueltos_detalle", det)])
    return out


def omisiones(D: Datos) -> OrderedDict:
    def no_vacia(v) -> bool:
        return isinstance(v, list) and any(isinstance(o, str) and o.strip() for o in v)

    def extrajo(ents) -> bool:
        return any(isinstance(e, dict) and e.get("type") != "TextoOrdenado" for e in ents or [])

    out = OrderedDict()
    for grupo, cfg in GRUPOS.items():
        por_marca = OrderedDict((capa, Counter()) for capa in ("crudo", "validado_e1", "finales_c15"))
        marcados_sin = OrderedDict((capa, Counter()) for capa in por_marca)
        advert = Counter()
        forma = Counter()
        marcas = Counter()
        for to in cfg["tos"]:
            reg = D.gen[cfg["gen"]][to]
            fin = {r["chunk_id"]: r for r in reg["ext_finales"]}
            for r in reg["compact"]:
                cid = r["chunk_id"]
                fl = D.chunks[cid].get("flags") or {}
                tab, frm = bool(fl.get("contenido_tabular")), bool(fl.get("formula"))
                marca = "tabla_y_formula" if tab and frm else "tabla" if tab else "formula" if frm else "sin_marca"
                marcas[marca] += 1
                ti = r.get("tool_input_crudo")
                om0 = ti.get("omisiones_no_prosa") if isinstance(ti, dict) else None
                if isinstance(om0, str):
                    forma["como_string_con_texto" if om0.strip() else "como_string_vacio"] += 1
                val = r.get("validacion") or {}
                vfin = (fin.get(cid) or {}).get("validacion") or {}
                E0c, _, _ = elementos_crudo(ti)
                capas = OrderedDict([
                    ("crudo", (no_vacia(om0) or (isinstance(om0, str) and bool(om0.strip())),
                               extrajo([e for _, e in E0c]))),
                    ("validado_e1", (no_vacia(val.get("omisiones_no_prosa")), extrajo(val.get("entidades")))),
                    ("finales_c15", (no_vacia(vfin.get("omisiones_no_prosa")), extrajo(vfin.get("entidades")))),
                ])
                for capa, (v, ex) in capas.items():
                    if v:
                        por_marca[capa][marca] += 1
                    elif marca != "sin_marca":
                        marcados_sin[capa]["con_extraccion" if ex else "sin_extraccion"] += 1
                for x in vfin.get("advertencias") or []:
                    if (x.get("tipo") or "").startswith("flag_"):
                        advert[x["tipo"]] += 1
        out[grupo] = OrderedDict([
            ("unidades_e0", sum(marcas.values())), ("unidades_por_marca", dict(sorted(marcas.items()))),
            ("con_omisiones_por_marca", OrderedDict((k, dict(sorted(v.items()))) for k, v in por_marca.items())),
            ("con_omisiones_total", OrderedDict((k, sum(v.values())) for k, v in por_marca.items())),
            ("marcados_sin_omision", OrderedDict((k, OrderedDict([("con_extraccion", v["con_extraccion"]),
                                                                  ("sin_extraccion", v["sin_extraccion"])]))
                                                 for k, v in marcados_sin.items())),
            ("crudo_omisiones_como_string", dict(sorted(forma.items()))),
            ("advertencias_flag_en_finales", dict(sorted(advert.items()))),
        ])
    return out


def conciliacion_c15(D: Datos) -> OrderedDict:
    """[c15] lee corpus_tanda0/salida/ (docs/tablero_correcciones.md, comando
    [c15]); los ensamblados leen salida_dirigida/. Solo cap difiere entre las
    dos (U-TANDA0-2A-DIR). Se recomputa cap sobre salida/ para conciliar."""
    p = RAIZ / "data/experiment/reextraccion_v2/corpus_tanda0/salida/cap/extracciones_finales_cap.jsonl"
    D._sello("t0_cap_finales_ext_salida_no_dirigida", p)

    def con(regs):
        return {r["chunk_id"] for r in regs if isinstance(r.get("validacion"), dict)
                and any(isinstance(o, str) and o.strip() for o in r["validacion"].get("omisiones_no_prosa") or [])}
    a, b = con(leer_jsonl(p)), con(D.gen["t0"]["cap"]["ext_finales"])
    return OrderedDict([("cap_salida", len(a)), ("cap_salida_dirigida", len(b)),
                        ("difieren", sorted(a ^ b))])


def catalogo_diff(bloque: OrderedDict) -> OrderedDict:
    js = json.loads((RAIZ / CATALOGO_JSON).read_text(encoding="utf-8"))
    J = OrderedDict()
    for e in js["clases"]:
        J[e["id"]] = {"label": e["label"], "alias": list(e.get("alias") or []), "nivel": e["nivel"],
                      "padre": e.get("padre"), "to": None}
    for r in js["roles"]:
        J[r["id"]] = {"label": r["label"], "alias": [], "nivel": r["nivel"], "padre": None, "to": r.get("to")}
    padre_mod = {a["id"]: a["padre"] for a in V3.ADICIONES_V3}
    comunes = sorted(set(bloque) & set(J))
    dif = OrderedDict()
    dif["ids_bloque"] = len(bloque)
    dif["ids_json"] = len(J)
    dif["solo_en_bloque"] = sorted(set(bloque) - set(J))
    dif["solo_en_json"] = sorted(set(J) - set(bloque))
    dif["comunes"] = len(comunes)
    dif["label_distinto"] = [[i, bloque[i]["label"], J[i]["label"]] for i in comunes if bloque[i]["label"] != J[i]["label"]]
    dif["alias_distinto"] = [[i, bloque[i]["alias"], J[i]["alias"]] for i in comunes
                             if sorted(bloque[i]["alias"]) != sorted(J[i]["alias"])]
    dif["nivel_distinto"] = [[i, bloque[i]["nivel"], J[i]["nivel"]] for i in comunes if bloque[i]["nivel"] != J[i]["nivel"]]
    dif["to_de_rol_distinto"] = [[i, bloque[i]["to"], J[i]["to"]] for i in comunes
                                 if bloque[i]["nivel"] == "rol" and bloque[i]["to"] != J[i]["to"]]
    dif["padre"] = OrderedDict([
        ("serializado_en_el_bloque", 0),
        ("declarado_en_ADICIONES_V3", len(padre_mod)),
        ("adiciones_en_json", [[i, padre_mod[i], J[i]["padre"]] for i in sorted(padre_mod) if i in J]),
        ("adiciones_fuera_del_json", [[i, padre_mod[i]] for i in sorted(padre_mod) if i not in J]),
        ("padre_en_json_de_ids_solo_json", [[i, J[i]["padre"]] for i in dif["solo_en_json"]]),
    ])
    return dif


# --------------------------------------------------------------------------- #
# salida                                                                       #
# --------------------------------------------------------------------------- #
def a_json(o):
    if isinstance(o, Counter):
        return OrderedDict((str(k) if not isinstance(k, tuple) else "|".join(map(str, k)), v)
                           for k, v in sorted(o.items(), key=lambda kv: (-kv[1], str(kv[0]))))
    if isinstance(o, dict):
        return OrderedDict((str(k) if not isinstance(k, tuple) else "|".join(map(str, k)), a_json(v))
                           for k, v in o.items())
    if isinstance(o, (list, tuple)):
        return [a_json(x) for x in o]
    if isinstance(o, (set, frozenset)):
        return sorted(a_json(x) for x in o)
    return o


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True)
    a = ap.parse_args()
    out_dir = Path(a.out_dir)

    p3 = perfil_e1.perfil("v3_b54")
    p2 = perfil_e1.perfil("produccion_dev")
    L3, L2v = listas_v3(p3), listas_v2()
    bloque = parse_bloque(V3.BLOQUE_CATALOGO_V3)
    if len(bloque) != 102 or set(bloque) != set(p3.esquema.sujetos_catalogo_set):
        raise Freno("FRENO: el bloque parseado no coincide con sujetos_catalogo_set del perfil v3_b54")
    if any(bloque[i]["label"] != p3.labels_catalogo[i]["label"] or bloque[i]["nivel"] != p3.labels_catalogo[i]["nivel"]
           for i in bloque):
        raise Freno("FRENO: label o nivel del bloque parseado ≠ perfil.labels_catalogo")
    js = json.loads((RAIZ / CATALOGO_JSON).read_text(encoding="utf-8"))
    json_ids = {e["id"] for e in js["clases"]} | {r["id"] for r in js["roles"]}

    D = Datos()
    inv_to = inventario_por_to(D, L3, L2v)
    grupos = OrderedDict((g, agregar_grupo(inv_to, g)) for g in GRUPOS)
    grafos = OrderedDict()
    for g, cfg in GRUPOS.items():
        kg = json.loads((RAIZ / cfg["ens"] / "kg.json").read_text(encoding="utf-8"))
        grafos[g] = grafo_c11(kg, L3, set(bloque), json_ids)
    e4 = OrderedDict()
    for g, cfg in GRUPOS.items():
        t = json.loads((RAIZ / cfg["ens"] / "e4_propuestos.json").read_text(encoding="utf-8"))
        esq = json.loads((RAIZ / cfg["ens"] / "e5_esqueleto.json").read_text(encoding="utf-8"))
        e4[g] = OrderedDict([
            ("propuestos", len(t)), ("resueltos", sum(1 for f in t if f["estado"] == "resuelto")),
            ("cuarentena", sum(1 for f in t if f["estado"] == "cuarentena")),
            ("con_padre_sugerido", sum(1 for f in t if f.get("padre_sugerido"))),
            ("sin_padre_sugerido", sum(1 for f in t if not f.get("padre_sugerido"))),
            ("padre_fuera_del_bloque_v3", sum(1 for f in t if f.get("padre_sugerido") and f["padre_sugerido"] not in bloque)),
            ("esqueleto_propuestos_sin_padre", len(esq.get("propuestos_sin_padre") or [])),
            ("esqueleto_padre_fuera_de_catalogo_json", esq.get("propuestos_padre_fuera_de_catalogo") or []),
            ("esqueleto_aristas_padre_sugerido", esq.get("aristas_padre_sugerido_flaggeadas")),
        ])

    # controles del tablero sobre desarrollo
    gd = grafos["desarrollo"]
    obtenido = {"Restriccion.tipo": sum(v for _, v in gd["Restriccion.tipo"]["fuera"]),
                "Comunicacion.tipo": sum(v for _, v in gd["Comunicacion.tipo"]["fuera"]),
                "claves": sum(v for _, v in gd["claves"]["fuera"]),
                "propuestos": e4["desarrollo"]["propuestos"], "resueltos": e4["desarrollo"]["resueltos"],
                "cuarentena": e4["desarrollo"]["cuarentena"]}
    cat = catalogo_diff(bloque)
    obtenido["solo_bloque"] = len(cat["solo_en_bloque"])
    obtenido["solo_json"] = len(cat["solo_en_json"])
    if obtenido != ESPERADO_TABLERO:
        raise Freno(f"FRENO: no se reproducen las cifras del tablero: {obtenido} ≠ {ESPERADO_TABLERO}")

    pares, lit = sujetos(D, bloque, {"v3_b54": p3, "produccion_dev": p2})
    sel, n_pob = muestra(pares)
    rres = reresolucion(D, p3)
    omis = omisiones(D)
    conc15 = conciliacion_c15(D)

    # ---------- JSON ----------
    J = OrderedDict()
    J["unidad"] = "U-LISTAS-NOMAP, etapa N1"
    J["mandato"] = "docs/mandatos/ULISTAS_NOMAP_diseno.md"
    J["comando"] = COMANDO
    J["reglas"] = OrderedDict([
        ("R-LISTAS", "listas del prefijo v3 (perfil v3_b54) y claves de [c11]; vacío o ausente = fuera"),
        ("R-CAPAS", "L0 crudo primer intento; L0r crudo de reintentos E3; L1 validado primer intento; "
                    "L2 entrada efectiva de E2 con cola flaggeada; L3 grafo"),
        ("R-NORM", "une cortes por guion de fin de línea; NFKD sin diacríticos; minúsculas; no alfanumérico→espacio; "
                   "presencia con límites de palabra en texto propio + heredado de E0"),
        ("R-FORZ", "sujeto_id del bloque v3 sin label/alias presente; amplia (principal) con label sin paréntesis, "
                   "contenido de paréntesis (no roles) y singularización r1_e4._singular; estricta: label y alias"),
        ("R-LIT", "sujeto_propuesto normalizado (R-NORM) presente en texto propio o heredado"),
        ("R-MUESTRA", f"pares de la tanda 0, otra_clase_o_instancia, posible forzado amplia; orden (chunk_id, sujeto_id); "
                      f"random.Random({SEMILLA}).sample(población, {N_MUESTRA})"),
        ("R-CAT", "JSON v3 + ids del bloque ausentes del JSON (label y nivel del perfil, sin alias)"),
        ("R-OMIS", "omisiones_no_prosa con al menos un string no vacío; capa finales = [c15]"),
    ])
    J["entradas"] = D.entradas
    J["e0_tanda0_identico_a_enm01"] = D.e0_identico_enm01
    J["listas"] = OrderedDict([
        ("v3", OrderedDict([(k, (sorted(v) if isinstance(v, frozenset) else v)) for k, v in L3.items()])),
        ("v2_perfil_r1", OrderedDict([(k, (sorted(v) if isinstance(v, frozenset) else v)) for k, v in L2v.items()])),
    ])
    J["controles_tablero_desarrollo"] = OrderedDict([("esperado", ESPERADO_TABLERO), ("obtenido", obtenido)])
    J["reintentos_db"] = OrderedDict()
    for g, d in D.reintentos.items():
        n_reint = {f["chunk_id"]: (f.get("n_reintentos") or 0)
                   for to in GEN[g]["tos"] for f in D.gen[g][to]["finales"]}
        por_unidad = Counter(x["chunk_id"] for x in d["asignadas"])
        J["reintentos_db"][g] = OrderedDict([(k, v) for k, v in d.items() if k != "asignadas"] + [
            ("asignadas", len(d["asignadas"])), ("unidades_distintas", len(por_unidad)),
            ("reintentos_en_finales", sum(n_reint.values())),
            ("unidades_con_reintento_en_finales", sum(1 for v in n_reint.values() if v > 0)),
            ("entradas_de_unidades_sin_reintento_en_finales",
             sum(n for c, n in por_unidad.items() if n_reint.get(c, 0) == 0)),
            ("unidades_con_mas_entradas_que_reintentos",
             sum(1 for c, n in por_unidad.items() if n > n_reint.get(c, 0) > 0)),
            ("unidades_con_reintento_sin_entrada", sum(1 for c, v in n_reint.items() if v > 0 and c not in por_unidad)),
        ])
    J["resumen_por_lista"] = OrderedDict(
        (lista, OrderedDict((g, resumen_lista(grupos[g], lista)) for g in GRUPOS))
        for lista in ("tipo_entidad", "predicado", "sujeto_id", "Obligacion.tipo", "Restriccion.tipo",
                      "Comunicacion.tipo", "claves"))
    J["padre_sugerido_validador"] = OrderedDict((g, grupos[g]["efecto_validador"].get("padre_sugerido", Counter())) for g in GRUPOS)
    J["grupos"] = grupos
    J["por_to"] = inv_to
    J["grafos"] = grafos
    J["propuestos_e4"] = e4
    J["sujetos_forzados"] = OrderedDict((g, tabla_forzados(pares, g, bloque)) for g in GRUPOS)
    lit_to = OrderedDict()
    for (g, to, capa), c in lit.items():
        lit_to.setdefault(capa, OrderedDict()).setdefault(g, OrderedDict())[to] = OrderedDict(
            [("total", c["total"]), ("presente", c["presente"]), ("ausente", c["ausente"]),
             ("ausente_con_todos_los_tokens", c["ausente_con_todos_los_tokens"])])
    lit_grupo = OrderedDict()
    for capa in ("crudo", "entrada_e2"):
        lit_grupo[capa] = OrderedDict()
        for g, cfg in GRUPOS.items():
            tot = Counter()
            for to in cfg["tos"]:
                tot.update(lit.get((cfg["gen"], to, capa), Counter()))
            lit_grupo[capa][g] = OrderedDict([("total", tot["total"]), ("presente", tot["presente"]),
                                              ("ausente", tot["ausente"]),
                                              ("ausente_con_todos_los_tokens", tot["ausente_con_todos_los_tokens"])])
    J["sujeto_propuesto_literal"] = OrderedDict([("por_to", lit_to), ("por_grupo", lit_grupo)])
    J["muestra_forzados"] = OrderedDict([("semilla", SEMILLA), ("n", N_MUESTRA), ("poblacion", n_pob),
                                         ("pares", [list(x) for x in sel])])
    J["reresolucion_contrafactica"] = rres
    J["omisiones"] = omis
    J["conciliacion_c15"] = conc15
    J["catalogo_diff"] = cat

    texto_json = json.dumps(a_json(J), ensure_ascii=False, indent=1) + "\n"

    # ---------- CSV ----------
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["orden_muestra", "chunk_id", "to", "unidad", "tipo_unidad", "sujeto_id", "nivel", "label_bloque",
                "alias_bloque", "n_relaciones", "predicados", "elementos_del_chunk", "e0_archivo",
                "e0_sha256_completo", "lectura_mencion_en_texto", "lectura_veredicto", "lectura_nota",
                "lector", "fecha_lectura"])
    for n, (cid, sid) in enumerate(sel, 1):
        x = pares[("t0", cid, sid)]
        ch = D.chunks[cid]
        w.writerow([n, cid, ch["to"], ch["unidad"], ch["tipo"], sid, bloque[sid]["nivel"], bloque[sid]["label"],
                    "; ".join(bloque[sid]["alias"]), x["n_rel"], "; ".join(sorted(x["predicados"])),
                    " | ".join(sorted(x["elementos"])), f"{E0_DIR}/chunks_{ch['to']}.json",
                    ch.get("sha256_completo", ""), "", "", "", "", ""])
    texto_csv = buf.getvalue()

    texto_md = render_md(J)

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "n1_inventario.json").write_text(texto_json, encoding="utf-8")
    (out_dir / "muestra_forzados_30.csv").write_text(texto_csv, encoding="utf-8")
    (out_dir / "n1_inventario.md").write_text(texto_md, encoding="utf-8")
    for nombre in ("n1_inventario.json", "n1_inventario.md", "muestra_forzados_30.csv"):
        print(nombre, sha256_path(out_dir / nombre))


# --------------------------------------------------------------------------- #
# markdown                                                                     #
# --------------------------------------------------------------------------- #
def esc(v) -> str:
    """Valor para mostrar en markdown: escapes JSON (saltos de línea visibles)."""
    v = "(vacío)" if v in ("", None) else str(v)
    return json.dumps(v, ensure_ascii=False)[1:-1].replace("`", "'")


def render_md(J) -> str:
    J = a_json(J)
    G = list(GRUPOS)
    L = []
    A = L.append
    A("# U-LISTAS-NOMAP — N1: inventario de las listas cerradas y mediciones")
    A("")
    A(f"Mandato `{J['mandato']}`. Solo lectura, USD 0, sin API ni Neo4j. Comando: `{J['comando']}`. "
      "Todo número de este archivo sale de `n1_inventario.json` (misma corrida); cada tabla dice de qué clave.")
    A("")
    A("## 1. Reglas declaradas antes de aplicarse")
    A("")
    A("El texto completo de cada regla está en el docstring de `reports/u_listas_nomap/u_listas_n1.py`.")
    A("")
    for k, v in J["reglas"].items():
        A(f"- **{k}**: {v}.")
    A("")
    A("Grupos: r1 = crudo de `corpus_v2/salida` (cinco TOs, perfil produccion_dev) y grafo KG-Reextraído-r1; "
      "desarrollo, cinco y diez = crudo de `corpus_tanda0/salida_dirigida` (perfil v3_b54; la entrada de los "
      "ensamblados, `ens_desarrollo/r1/reporte_ensamblado_r1.json:22`) y el `r1/kg.json` de cada ensamblado. "
      "diez = desarrollo + cinco.")
    A("")
    A("## 2. Entradas y controles")
    A("")
    A("| clave | ruta | sha256 |")
    A("|---|---|---|")
    for k, v in J["entradas"].items():
        A(f"| {k} | `{v['ruta']}` | `{v['sha256'][:16]}…` |")
    A("")
    c = J["controles_tablero_desarrollo"]
    A("Controles contra `docs/tablero_correcciones.md` ([c11], [c12], [c13]) sobre KG-Tanda0-Desarrollo-r1 "
      "(clave `controles_tablero_desarrollo`; el script frena si no coinciden):")
    A("")
    A("| cifra | tablero | obtenido |")
    A("|---|---|---|")
    for k in c["esperado"]:
        A(f"| {k} | {c['esperado'][k]} | {c['obtenido'][k]} |")
    A("")
    A(f"E0 de la tanda 0 idéntico byte a byte al de r1 (`salida_enm01`) en los cinco TOs de desarrollo: "
      f"{all(J['e0_tanda0_identico_a_enm01'].values())} (clave `e0_tanda0_identico_a_enm01`).")
    A("")
    A("Reintentos de E3 en `e1_reintentos.db` (clave `reintentos_db`):")
    A("")
    A("| generación | namespace | entradas | asignadas a un chunk | unidades distintas | no asignadas | de otros TOs | "
      "reintentos en finales (unidades) | entradas de unidades sin reintento en finales | unidades con más entradas que reintentos | unidades con reintento sin entrada |")
    A("|---|---|---|---|---|---|---|---|---|---|---|")
    for g, d in J["reintentos_db"].items():
        A(f"| {g} | `{d['namespace'].split('-p')[-1].split('|')[0]}` | {d['entradas']} | {d['asignadas']} | {d['unidades_distintas']} | "
          f"{d['no_asignadas']} | {d['fuera_del_corpus'] or 0} | {d['reintentos_en_finales']} "
          f"({d['unidades_con_reintento_en_finales']}) | {d['entradas_de_unidades_sin_reintento_en_finales']} | "
          f"{d['unidades_con_mas_entradas_que_reintentos']} | {d['unidades_con_reintento_sin_entrada']} |")
    A("")
    A("L0r inventaría todas las entradas asignadas; el crudo del reintento no está en `finales.jsonl` "
      "(tablero, fila «Crudo del reintento de E3 sin persistir», [c16]).")
    A("")
    A("## 3. Inventario por lista cerrada")
    A("")
    A("Clave `resumen_por_lista.<lista>.<grupo>`. Columnas: emitidos y fuera de lista en el crudo L0; efecto del "
      "validador sobre los fuera de lista del crudo (mismo registro, L0→L1): rechazados (por cualquier motivo), "
      "normalizados a «otra», anulados (padre) y que pasaron; fuera de lista en L1; emitidos y fuera en el crudo "
      "de los reintentos L0r; fuera en la entrada de E2 (L2); fuera en el grafo L3 ([c11]).")
    A("")
    etiquetas = {"tipo_entidad": "Tipos de entidad (9)", "predicado": "Predicados (13)",
                 "sujeto_id": "Catálogo de sujetos, sujeto_id (102)", "Obligacion.tipo": "Obligacion.tipo (enum de 6)",
                 "Restriccion.tipo": "Restriccion.tipo (3)", "Comunicacion.tipo": "Comunicacion.tipo (3)",
                 "claves": "Claves de properties por tipo ([c11])"}
    for lista, et in etiquetas.items():
        A(f"### {et}")
        A("")
        A("| grupo | emitidos L0 | fuera L0 | rechazados | normalizados | pasaron | fuera L1 | emitidos L0r | fuera L0r | fuera L2 | fuera L3 |")
        A("|---|---|---|---|---|---|---|---|---|---|---|")
        for g in G:
            r = J["resumen_por_lista"][lista][g]
            gr = J["grafos"][g]
            if lista == "tipo_entidad":
                f3 = sum(v for _, v in gr["tipo_entidad"]["fuera"])
            elif lista == "predicado":
                pip = sum(v for k, v in gr["predicado"]["fuera_por_rol_fuente"]
                          if k.split("|", 1)[1] in ("esqueleto", "cuarentena_flaggeada"))
                ex = sum(v for _, v in gr["predicado"]["fuera_por_rol_fuente"]) - pip
                f3 = f"{ex} (+{pip} del pipeline)"
            elif lista == "sujeto_id":
                f3 = (f"{len(gr['sujetos_nodos']['otros'])} (+{len(gr['sujetos_nodos']['solo_en_json_v3'])} "
                      "nodos del esqueleto)")
            else:
                f3 = sum(v for _, v in gr[lista]["fuera"])
            A(f"| {g} | {r['emitidos_crudo']} | {r['fuera_crudo']} | {r['validador_rechazados']} | "
              f"{r['validador_normalizados']} | {r['validador_pasaron']} | {r['fuera_validado_e1']} | "
              f"{r['emitidos_reintentos_crudo']} | {r['fuera_reintentos_crudo']} | {r['fuera_entrada_e2']} | {f3} |")
        A("")
        A("Valores fuera de lista (L0 crudo; L3 grafo), clave `grupos.<g>.capas.crudo.fuera` y `grafos.<g>`:")
        A("")
        for g in G:
            fu = J["grupos"][g]["capas"]["crudo"]["fuera"].get(lista, {})
            if lista == "predicado":
                f3 = J["grafos"][g]["predicado"]["fuera_por_rol_fuente"]
            elif lista == "tipo_entidad":
                f3 = J["grafos"][g]["tipo_entidad"]["fuera"]
            elif lista == "sujeto_id":
                f3 = [[i, "solo JSON"] for i in J["grafos"][g]["sujetos_nodos"]["solo_en_json_v3"]] + \
                     [[i, "otro"] for i in J["grafos"][g]["sujetos_nodos"]["otros"]]
            else:
                f3 = J["grafos"][g][lista]["fuera"]
            l0 = ", ".join(f"`{esc(k)}` {v}" for k, v in list(fu.items())[:25]) or "—"
            if len(fu) > 25:
                l0 += f", … ({len(fu)} valores distintos)"
            l3 = ", ".join(f"`{esc(k)}` {v}" for k, v in f3) or "—"
            A(f"- {g}: L0 {l0}. L3 {l3}.")
        A("")
        ef = {g: J["grupos"][g]["efecto_validador"].get(lista, {}) for g in G}
        A("Estado tras el validador de cada valor fuera de lista del crudo (clave `grupos.<g>.efecto_validador`): " +
          "; ".join(f"{g}: " + (", ".join(f"{k} {v}" for k, v in ef[g].items()) or "—") for g in G) + ".")
        A("")
    A("### Operacion.tipo (texto libre, se describe)")
    A("")
    A("| grupo | Operacion en L0 | valores distintos L0 | vacíos L0 | nodos Operacion L3 | valores distintos L3 |")
    A("|---|---|---|---|---|---|")
    for g in G:
        ot = J["grupos"][g]["capas"]["crudo"]["conteos"].get("Operacion.tipo", {})
        A(f"| {g} | {sum(ot.values())} | {len(ot)} | {ot.get('', 0)} | {J['grafos'][g]['Operacion.tipo']['nodos']} | "
          f"{J['grafos'][g]['Operacion.tipo']['distintos']} |")
    A("")
    for g in G:
        ot = J["grupos"][g]["capas"]["crudo"]["conteos"].get("Operacion.tipo", {})
        A(f"- {g}, diez más frecuentes en L0: " + ", ".join(f"`{esc(k)}` {v}" for k, v in list(ot.items())[:10]) + ".")
    A("")
    A("### Padre sugerido de sujeto_propuesto")
    A("")
    A("Clave `padre_sugerido_validador` (crudo L0: padre fuera del bloque v3 en relaciones aplica_a/ejecuta) y "
      "`grupos.<g>.capas.crudo.forma_sujeto`:")
    A("")
    for g in G:
        fo = J["grupos"][g]["capas"]["crudo"]["forma_sujeto"]
        A(f"- {g}: con padre en catálogo {fo.get('propuesto_padre_en_catalogo', 0)}, con padre fuera "
          f"{fo.get('propuesto_padre_fuera_de_catalogo', 0)}, sin padre {fo.get('propuesto_sin_padre', 0)}, "
          f"padre sin propuesto {fo.get('padre_sin_propuesto', 0)}; estado de los padres fuera: " +
          (", ".join(f"{k} {v}" for k, v in J["padre_sugerido_validador"][g].items()) or "—") + ".")
    A("")
    A("## 4. Motivos de rechazo del validador, por lista")
    A("")
    A("Clave `grupos.<g>.motivos_rechazo` (validacion.rechazos del primer intento, L1). La lista a la que se "
      "asigna cada motivo es la del mapeo `MOTIVO_A_LISTA` del script; «sin lista» = motivo ajeno a las listas "
      "cerradas.")
    A("")
    A("| nivel | motivo | lista | " + " | ".join(G) + " |")
    A("|---|---|---|" + "---|" * len(G))
    mot = sorted({k for g in G for k in J["grupos"][g]["motivos_rechazo"]})
    for k in mot:
        nivel, motivo = k.split("|", 1)
        A(f"| {nivel} | {motivo} | {MOTIVO_A_LISTA.get(motivo, 'sin lista')} | " +
          " | ".join(str(J["grupos"][g]["motivos_rechazo"].get(k, 0)) for g in G) + " |")
    A("")
    A("Elementos del crudo sin correspondencia con el validado (clave `grupos.<g>.efecto_validador.sin_correspondencia`): " +
      "; ".join(f"{g} " + (", ".join(f"{k} {v}" for k, v in J["grupos"][g]["efecto_validador"].get("sin_correspondencia", {}).items()) or "0")
                for g in G) + ".")
    A("")
    if J["grupos"]["r1"].get("efecto_validador_perfil_v2"):
        A("r1 contra las listas de su perfil (v2: 6 tipos, 12 predicados, 70 ids, Obligacion.tipo de 5, "
          "Operacion {tipo}), clave `grupos.r1.efecto_validador_perfil_v2`: " +
          "; ".join(f"{k}: " + (", ".join(f"{a} {b}" for a, b in v.items()) or "—")
                    for k, v in J["grupos"]["r1"]["efecto_validador_perfil_v2"].items()) + ".")
        A("")
    A("## 5. Sujetos")
    A("")
    A("### 5.1 Forma de las relaciones aplica_a y ejecuta")
    A("")
    A("Clave `grupos.<g>.capas.<capa>.forma_sujeto` (L0, L1, L2) y `grafos.<g>.aristas_sujeto_no_esqueleto` (L3).")
    A("")
    A("| grupo | capa | solo sujeto_id | solo sujeto_propuesto | ambos | ninguno |")
    A("|---|---|---|---|---|---|")
    for g in G:
        for capa in ("crudo", "validado_e1", "reintentos_crudo", "entrada_e2"):
            fo = J["grupos"][g]["capas"][capa]["forma_sujeto"]
            A(f"| {g} | {capa} | {fo.get('solo_sujeto_id', 0)} | {fo.get('solo_sujeto_propuesto', 0)} | "
              f"{fo.get('ambos', 0)} | {fo.get('ninguno', 0)} |")
        s = J["grafos"][g]["aristas_sujeto_no_esqueleto"]
        A(f"| {g} | grafo L3 | {s['a_id_de_catalogo']} (a id de catálogo) | {s['a_propuesto_en_cuarentena']} (a propuesto en cuarentena) | — | — |")
    A("")
    A("Mención textual guardada en aristas aplica_a/ejecuta del grafo (sin esqueleto): " +
      ", ".join(f"{g} {J['grafos'][g]['aristas_sujeto_no_esqueleto']['con_mencion_textual_guardada']} de "
                f"{J['grafos'][g]['aristas_sujeto_no_esqueleto']['total']}" for g in G) + " ([c12]; el campo no existe).")
    A("")
    A("### 5.2 Propuestos en el ensamblado (E4 y esqueleto)")
    A("")
    A("Clave `propuestos_e4` (`e4_propuestos.json` y `e5_esqueleto.json` de cada ensamblado).")
    A("")
    A("| grupo | propuestos | resueltos | cuarentena | con padre | sin padre | padre fuera del bloque v3 | padre fuera del JSON (esqueleto) | aristas padre_sugerido |")
    A("|---|---|---|---|---|---|---|---|---|")
    for g in G:
        e = J["propuestos_e4"][g]
        pf = "; ".join(f"`{a}`→`{b}`" for a, b in e["esqueleto_padre_fuera_de_catalogo_json"]) or "0"
        A(f"| {g} | {e['propuestos']} | {e['resueltos']} | {e['cuarentena']} | {e['con_padre_sugerido']} | "
          f"{e['sin_padre_sugerido']} | {e['padre_fuera_del_bloque_v3']} | {pf} | {e['esqueleto_aristas_padre_sugerido']} |")
    A("")
    A("### 5.3 Posibles forzados (R-FORZ)")
    A("")
    A("Clave `sujetos_forzados.<g>`. Unidad: par (chunk, sujeto_id) del crudo L0. Indicador, no veredicto.")
    A("")
    A("| grupo | relaciones con sujeto_id | pares | categoría | pares de la categoría | posibles forzados (amplia) | posibles forzados (estricta) |")
    A("|---|---|---|---|---|---|---|")
    for g in G:
        s = J["sujetos_forzados"][g]
        for cat in CATEGORIAS_FORZ:
            A(f"| {g} | {s['relaciones_con_sujeto_id']} | {s['pares_chunk_sujeto']} | {cat} | {s[cat]['pares']} | "
              f"{s[cat]['posibles_forzados_amplia']} | {s[cat]['posibles_forzados_estricta']} |")
    A("")
    A("Ids de clase o instancia (no defecto del TO) con más posibles forzados (amplia), «id posibles/pares»:")
    A("")
    for g in G:
        A(f"- {g}: " + ", ".join(f"`{i}` {n}/{t}" for i, n, t in J["sujetos_forzados"][g]["top_ids_otra_clase_o_instancia"]) + ".")
    A("")
    m = J["muestra_forzados"]
    A(f"Muestra sellada: `muestra_forzados_30.csv`, {m['n']} pares sorteados con semilla {m['semilla']} sobre una "
      f"población de {m['poblacion']} (R-MUESTRA; clave `muestra_forzados`). Columnas de lectura vacías; quién lee "
      "lo decide la autora (checklist P15 y Q12).")
    A("")
    A("### 5.4 sujeto_propuesto literal en el texto del chunk (R-LIT)")
    A("")
    A("Clave `sujeto_propuesto_literal`. Unidad: relación aplica_a/ejecuta con sujeto_propuesto.")
    A("")
    A("La última columna es una descripción posterior, no una regla de presencia: de los ausentes, cuántos "
      "tienen cada token normalizado en el texto del chunk, en cualquier orden y no contiguos.")
    A("")
    A("| capa | grupo | total | presente | ausente | ausente con todos los tokens |")
    A("|---|---|---|---|---|---|")
    for capa in ("crudo", "entrada_e2"):
        for g in G:
            x = J["sujeto_propuesto_literal"]["por_grupo"][capa][g]
            A(f"| {capa} | {g} | {x['total']} | {x['presente']} | {x['ausente']} | {x['ausente_con_todos_los_tokens']} |")
    A("")
    A("Por TO (crudo L0 / entrada E2, «presente/total»):")
    A("")
    for gen in ("r1", "t0"):
        partes = []
        for to in GEN[gen]["tos"]:
            a0 = J["sujeto_propuesto_literal"]["por_to"].get("crudo", {}).get(gen, {}).get(to, {"presente": 0, "total": 0})
            a2 = J["sujeto_propuesto_literal"]["por_to"].get("entrada_e2", {}).get(gen, {}).get(to, {"presente": 0, "total": 0})
            partes.append(f"{to} {a0['presente']}/{a0['total']} · {a2['presente']}/{a2['total']}")
        A(f"- {gen}: " + "; ".join(partes) + ".")
    A("")
    A("## 6. Re-resolución por programa, contrafáctica (R-CAT)")
    A("")
    r = J["reresolucion_contrafactica"]
    A(f"Clave `reresolucion_contrafactica`. `r1_e4.resolver_label` por import sobre cada fila de `e4_propuestos.json`. "
      f"Catálogo (i): `esquema_v3_clases.json`; (ii): (i) más {len(r['ids_agregados_en_ii'])} ids del bloque "
      f"({', '.join('`' + i + '`' for i in r['ids_agregados_en_ii'])}), sin alias. Control: (i) reproduce la tabla "
      "guardada fila a fila. Es un contrafáctico, no un resultado.")
    A("")
    A("| ensamblado | propuestos | guardado: resueltos / cuarentena | resuelven con (i) | resuelven con (ii) |")
    A("|---|---|---|---|---|")
    for g in ("desarrollo", "cinco", "diez"):
        x = r[g]
        A(f"| {g} | {x['propuestos']} | {x['guardado_resueltos']} / {x['guardado_cuarentena']} | "
          f"{x['resuelven_catalogo_i']} | {x['resuelven_catalogo_ii']} |")
    A("")
    for g in ("desarrollo", "cinco", "diez"):
        A(f"- {g}: " + ("; ".join(f"«{lb}» (padre `{pa}`): (i) `{ri}` {mi}; (ii) `{rii}` {mii}"
                                  for lb, pa, ri, mi, rii, mii in r[g]["resueltos_detalle"]) or "—") + ".")
    A("")
    A("## 7. Omisiones (R-OMIS)")
    A("")
    A("Clave `omisiones.<g>`. Marca de E0: tabla = `flags.contenido_tabular`, fórmula = `flags.formula`. "
      "«Marcadas sin omisión» se abre en: con extracción (alguna entidad distinta de TextoOrdenado en esa capa) "
      "y sin extracción (rechazo de chunk, unidad en cola humana o salida vacía).")
    A("")
    A("| grupo | unidades | por marca (E0) | capa | con omisiones: total | por marca | marcadas sin omisión: con extracción / sin extracción |")
    A("|---|---|---|---|---|---|---|")
    for g in G:
        o = J["omisiones"][g]
        pm = ", ".join(f"{k} {v}" for k, v in o["unidades_por_marca"].items())
        for capa in ("crudo", "validado_e1", "finales_c15"):
            ms = o["marcados_sin_omision"][capa]
            A(f"| {g} | {o['unidades_e0']} | {pm} | {capa} | {o['con_omisiones_total'][capa]} | "
              + (", ".join(f"{k} {v}" for k, v in o["con_omisiones_por_marca"][capa].items()) or "—")
              + f" | {ms['con_extraccion']} / {ms['sin_extraccion']} |")
    A("")
    A("omisiones_no_prosa emitido como string en el crudo (el validador solo toma listas, "
      "`validador_e1.py:154-156`): " +
      "; ".join(f"{g} " + (", ".join(f"{k} {v}" for k, v in J["omisiones"][g]["crudo_omisiones_como_string"].items()) or "0")
                for g in G) + ". Advertencias `flag_*` del validador en finales: " +
      "; ".join(f"{g} " + (", ".join(f"{k} {v}" for k, v in J["omisiones"][g]["advertencias_flag_en_finales"].items()) or "0")
                for g in G) + ".")
    A("")
    c15 = J["conciliacion_c15"]
    A(f"Conciliación con [c15] (clave `conciliacion_c15`): el comando [c15] lee `corpus_tanda0/salida/`; los "
      f"ensamblados leen `salida_dirigida/`, que solo difiere en cap. Unidades de cap con omisiones: "
      f"salida/ {c15['cap_salida']}, salida_dirigida/ {c15['cap_salida_dirigida']}; difieren: "
      + (", ".join(f"`{x}`" for x in c15["difieren"]) or "ninguna") + ".")
    A("")
    A("## 8. Catálogo: bloque v3 contra esquema_v3_clases.json")
    A("")
    c = J["catalogo_diff"]
    A(f"Clave `catalogo_diff`. Bloque parseado de `prompt_v3_b54.BLOQUE_CATALOGO_V3` ({c['ids_bloque']} ids; label y "
      f"nivel verificados contra `perfil_e1.perfil('v3_b54').labels_catalogo`); JSON: {c['ids_json']} ids.")
    A("")
    A(f"- Solo en el bloque ({len(c['solo_en_bloque'])}): " + ", ".join(f"`{i}`" for i in c["solo_en_bloque"]) + ".")
    A(f"- Solo en el JSON ({len(c['solo_en_json'])}): " + ", ".join(f"`{i}`" for i in c["solo_en_json"]) + ".")
    A(f"- Comunes: {c['comunes']}. Label distinto: {len(c['label_distinto'])}. Alias distinto: {len(c['alias_distinto'])}. "
      f"Nivel distinto: {len(c['nivel_distinto'])}. TO de rol distinto: {len(c['to_de_rol_distinto'])}.")
    for i, b, j in c["label_distinto"]:
        A(f"  - label `{i}`: bloque «{b}» / JSON «{j}».")
    for i, b, j in c["alias_distinto"]:
        A(f"  - alias `{i}`: bloque {b} / JSON {j}.")
    for i, b, j in c["nivel_distinto"]:
        A(f"  - nivel `{i}`: bloque {b} / JSON {j}.")
    for i, b, j in c["to_de_rol_distinto"]:
        A(f"  - TO de rol `{i}`: bloque {b} / JSON {j}.")
    p = c["padre"]
    A(f"- Padre: el bloque no serializa padres ({p['serializado_en_el_bloque']}); `ADICIONES_V3` "
      f"(`prompt_v3_b54.py:150`) declara padre para {p['declarado_en_ADICIONES_V3']} ids. De ellos, en el JSON: " +
      (", ".join(f"`{i}` módulo `{a}` / JSON `{b}`" for i, a, b in p["adiciones_en_json"]) or "—") +
      "; fuera del JSON: " + (", ".join(f"`{i}` (padre `{a}`)" for i, a in p["adiciones_fuera_del_json"]) or "—") +
      ". Padre en el JSON de los ids solo-JSON: " +
      (", ".join(f"`{i}`→`{a}`" for i, a in p["padre_en_json_de_ids_solo_json"]) or "—") + ".")
    A("")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
