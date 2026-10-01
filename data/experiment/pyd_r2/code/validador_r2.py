"""
validador_r2.py — U-PYD: validador de la salida de E1 en el perfil r2.

Aplica la política por campo (`data/experiment/pyd_r2/politica_campos_r2.json`,
cuyo sha256 queda en cada resultado) y devuelve los elementos aceptados como
modelos de `modelos_r2`, los rechazos con motivo, las omisiones, los
pendientes del registro de no mapeados y los contadores por campo y
tratamiento. Un valor fuera de lista nunca se descarta en silencio: se
normaliza con contador y original guardado, se registra con la marca
`fuera_de_lista`, o el elemento se rechaza con motivo (L-ESQ-R2 §2.3).

Incluye:
  - pasos de la política por campo (P-a0 a P-a10) y alias (decisión 4);
  - matriz r2: la congelada más condicion_de → Operacion y → Potestad; las
    relaciones que solo valen por la ampliación llevan `no_verificada_e3`
    (L-ESQ-R2 §6.4);
  - coherencia entre Restriccion.tipo y el predicado (`BKL-0038`), como marca;
  - verificación de la mención en dos niveles (P-b3, P-b4), sin rechazar;
  - omisiones: tramo verificado contra el texto propio (P-e2), tipos
    rechazados como `fuera_de_tipos` (P-e3), strings del crudo v3 (P-a10).

`desde_v3` lee el input de un tool call del perfil v3 (o del de desarrollo)
en la forma r2: `sujeto_propuesto` es la mención y cada string de
`omisiones_no_prosa` una omisión sin categoría ni tramo (L-ESQ-R2 §3.4, §5.4).

No edita nada del pipeline: importa `comun_e1` (puntos admitidos y rol
documental) sin cambiarlo. Sin API, sin archivos escritos.
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Optional

AQUI = Path(__file__).resolve().parent
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))
import modelos_r2 as M  # noqa: E402

_E1 = M.REPO / "data" / "experiment" / "reextraccion_v2" / "e1_extractor"
if str(_E1) not in sys.path:
    sys.path.insert(0, str(_E1))
from comun_e1 import chunk_flaggeado, puntos_admitidos, rol_documental_de_punto  # noqa: E402

POLITICA = M.PYD_R2 / "politica_campos_r2.json"
PERFIL = "r2"


# ------------------------------------------------------------------------- #
# Política                                                                    #
# ------------------------------------------------------------------------- #
class Politica:
    """La tabla de configuración versionada, con su sha256."""

    PASOS_CONOCIDOS = {
        "tipo_entidad": ("en_lista", "forma", "alias"),
        "predicado": ("en_lista", "forma", "alias"),
        "Obligacion.tipo": ("en_lista",),
        "Restriccion.tipo": ("en_lista",),
        "Comunicacion.tipo": ("en_lista", "derivar_de_codigo_o_label", "externa_por_lexico"),
        "Obligacion.frecuencia": ("en_lista", "desde_tramo"),
    }

    def __init__(self, ruta: Path = POLITICA):
        crudo = Path(ruta).read_bytes()
        self.ruta = Path(ruta)
        self.sha256 = hashlib.sha256(crudo).hexdigest()
        self.d = json.loads(crudo.decode("utf-8"))
        for campo, pasos in self.PASOS_CONOCIDOS.items():
            declarados = tuple(self.d["campos"][campo]["pasos"])
            for p in declarados:
                if p not in pasos:
                    raise RuntimeError(f"política: paso desconocido {p!r} en {campo}")
        self.alias_tipo = dict(self.d["alias"]["tipo_entidad"])
        self.alias_pred = dict(self.d["alias"]["predicado"])
        self.holgura = self.d["parametros"]["mencion_holgura_tokens"]["valor"]
        self.largo_min_omision = self.d["parametros"]["omision_largo_minimo_tokens"]["valor"]
        self.lexico_externa = frozenset(self.d["campos"]["Comunicacion.tipo"]["lexico_externa"])
        her = self.d["campos"]["claves"]["heredadas_v3"]
        if {t: tuple(v) for t, v in her.items()} != M.CLAVES_HEREDADAS_V3:
            raise RuntimeError("política: claves heredadas de v3 distintas de las del modelo")
        amp = tuple(tuple(x) for x in self.d["campos"]["firma"]["ampliacion"])
        if amp != M.AMPLIACION_R2:
            raise RuntimeError("política: ampliación de la matriz distinta de la del modelo")

    def pasos(self, campo: str) -> tuple[str, ...]:
        return tuple(self.d["campos"][campo]["pasos"])

    def modo(self, campo: str) -> str:
        return self.d["campos"][campo]["si_no_resuelve"]


_POLITICA_DEFAULT: Optional[Politica] = None


def politica_default() -> Politica:
    global _POLITICA_DEFAULT
    if _POLITICA_DEFAULT is None:
        _POLITICA_DEFAULT = Politica()
    return _POLITICA_DEFAULT


# ------------------------------------------------------------------------- #
# Texto: R-NORM (N1) con offsets, verificación de tramos                       #
# ------------------------------------------------------------------------- #
_GUION = re.compile(r"(\w)-\s*\n\s*(\w)")
_ALNUM = frozenset("0123456789abcdefghijklmnopqrstuvwxyz")


def fold(s: str) -> str:
    d = unicodedata.normalize("NFKD", s)
    return "".join(c for c in d if not unicodedata.combining(c)).lower()


def tokens_con_spans(texto: str) -> list[tuple[str, int, int]]:
    """Tokens de R-NORM (reports/u_listas_nomap/u_listas_n1.py:250-254: une los
    cortes por guion de fin de línea, NFKD sin diacríticos, minúsculas, no
    alfanumérico a espacio) con el span de cada token en el texto original."""
    saltar = set()
    for m in _GUION.finditer(texto):
        saltar.update(range(m.start() + 1, m.end() - 1))
    toks: list[tuple[str, int, int]] = []
    actual, ini, fin = [], -1, -1
    for i, ch in enumerate(texto):
        if i in saltar:
            continue
        for c in fold(ch):
            if c in _ALNUM:
                if not actual:
                    ini = i
                actual.append(c)
                fin = i + 1
            elif actual:
                toks.append(("".join(actual), ini, fin))
                actual = []
    if actual:
        toks.append(("".join(actual), ini, fin))
    return toks


def norm_tokens(s: str) -> list[str]:
    return [t for t, _, _ in tokens_con_spans(s)]


def _ventana_minima(texto_toks: list[str], necesarios: set[str]) -> Optional[tuple[int, int]]:
    """Ventana contigua más corta (índices de token, fin exclusivo) que contiene
    todos los tokens necesarios."""
    if not necesarios or not necesarios <= set(texto_toks):
        return None
    falta = len(necesarios)
    cuenta: Counter = Counter()
    mejor = None
    izq = 0
    for der, t in enumerate(texto_toks):
        if t in necesarios:
            cuenta[t] += 1
            if cuenta[t] == 1:
                falta -= 1
        while falta == 0:
            if mejor is None or der + 1 - izq < mejor[1] - mejor[0]:
                mejor = (izq, der + 1)
            u = texto_toks[izq]
            if u in necesarios:
                cuenta[u] -= 1
                if cuenta[u] == 0:
                    falta += 1
            izq += 1
    return mejor


def verificar_tramo(aguja: str, texto: str, holgura: Optional[int]) -> tuple[str, Optional[str]]:
    """Nivel 1 («exacta»): la secuencia de tokens de la aguja aparece contigua
    en el texto (equivale a la subcadena normalizada entre límites de palabra
    de R-NORM). Nivel 2 («tokens»): todos sus tokens distintos aparecen en una
    ventana contigua de a lo sumo len(distintos) + holgura tokens (holgura
    None = sin tope); devuelve el tramo literal mínimo del texto. Si no, «no»."""
    at = norm_tokens(aguja)
    if not at:
        return "no", None
    tt = tokens_con_spans(texto)
    tt_s = [t for t, _, _ in tt]
    n = len(at)
    for i in range(len(tt_s) - n + 1):
        if tt_s[i:i + n] == at:
            return "exacta", None
    v = _ventana_minima(tt_s, set(at))
    if v is None:
        return "no", None
    if holgura is not None and v[1] - v[0] > len(set(at)) + holgura:
        return "no", None
    return "tokens", texto[tt[v[0]][1]:tt[v[1] - 1][2]]


def texto_completo(chunk: dict) -> str:
    """Texto propio más el heredado, como en R-NORM de N1 (unidos por salto)."""
    partes = [chunk.get("texto") or ""] + [h.get("texto") or "" for h in chunk.get("herencia") or []]
    return "\n".join(partes)


# ------------------------------------------------------------------------- #
# Pasos de la política                                                        #
# ------------------------------------------------------------------------- #
_FOLD_TIPOS = {fold(t): t for t in M.TIPOS_ENTIDAD}
_CAMEL = re.compile(r"(?<=[a-z0-9])([A-Z])")


def resolver_tipo(v: Any, pol: Politica) -> tuple[Optional[str], str]:
    if not isinstance(v, str):
        return None, "rechazado"
    for paso in pol.pasos("tipo_entidad"):
        if paso == "en_lista" and v in M.TIPOS_ENTIDAD:
            return v, "en_lista"
        if paso == "forma":
            f = _FOLD_TIPOS.get(fold(v.strip()))
            if f is not None:
                return f, "normalizado_forma"
        if paso == "alias":
            a = pol.alias_tipo.get(v.strip())
            if a is not None:
                return a, "normalizado_alias"
    return None, "rechazado"


def _forma_predicado(v: str) -> str:
    s = re.sub(r"\s+", "", v)
    s = _CAMEL.sub(r"_\1", s)
    return fold(s)


def resolver_predicado(v: Any, pol: Politica) -> tuple[Optional[str], str]:
    if not isinstance(v, str):
        return None, "rechazado"
    for paso in pol.pasos("predicado"):
        if paso == "en_lista" and v in M.PREDICADOS:
            return v, "en_lista"
        if paso == "forma":
            f = _forma_predicado(v)
            if f in M.PREDICADOS:
                return f, "normalizado_forma"
        if paso == "alias":
            for cand in (v.strip(), _forma_predicado(v)):
                a = pol.alias_pred.get(cand)
                if a is not None:
                    return a, "normalizado_alias"
    return None, "rechazado"


_RE_COM = re.compile(
    r"^\s*(?:com(?:unicacion)?\.?\s*)?[\"'“”«»]?\s*([abc])\s*[\"'“”«»]?\s*(?:-|–|\s)\s*(?:n[°ºo]\.?\s*)?(\d[\d.]*)\s*$")


def derivar_comunicacion(codigo: Any, label: Any) -> Optional[str]:
    for s in (codigo, label):
        if isinstance(s, str):
            m = _RE_COM.match(fold(s))
            if m:
                return m.group(1).upper()
    return None


def nombra_norma_externa(s: Any, lexico: frozenset) -> bool:
    return isinstance(s, str) and any(t in lexico for t in norm_tokens(s))


_FRECUENCIA_TOKENS = {}
for _base, _formas in (("diaria", ("diaria", "diario", "diarias", "diarios", "diariamente")),
                       ("semanal", ("semanal", "semanales", "semanalmente")),
                       ("mensual", ("mensual", "mensuales", "mensualmente")),
                       ("trimestral", ("trimestral", "trimestrales", "trimestralmente")),
                       ("semestral", ("semestral", "semestrales", "semestralmente")),
                       ("anual", ("anual", "anuales", "anualmente"))):
    for _f in _formas:
        _FRECUENCIA_TOKENS[_f] = _base


def frecuencia_desde_tramo(v: str) -> Optional[str]:
    hallados = {_FRECUENCIA_TOKENS[t] for t in norm_tokens(v) if t in _FRECUENCIA_TOKENS}
    return hallados.pop() if len(hallados) == 1 else None


# ------------------------------------------------------------------------- #
# Adaptador del crudo v3                                                      #
# ------------------------------------------------------------------------- #
def desde_v3(tool_input: Any) -> tuple[Any, Counter]:
    """Input de un tool call v3 (o de desarrollo) leído en la forma r2. No muta
    el original. `sujeto_propuesto` pasa a `sujeto_mencion`; las cadenas de
    `omisiones_no_prosa` pasan a `omisiones` como omisiones sin categoría ni
    tramo, con la cadena como nota (P-a10 para la forma string)."""
    c: Counter = Counter()
    ti = tool_input
    if isinstance(ti, str):
        try:
            ti = json.loads(ti)
        except json.JSONDecodeError:
            return tool_input, c
    if not isinstance(ti, dict):
        return ti, c
    ti = copy.deepcopy(ti)
    rels = ti.get("relations")
    if isinstance(rels, str):
        try:
            rels = json.loads(rels)
            c["relations_como_string_json"] += 1
        except json.JSONDecodeError:
            pass
    if isinstance(rels, list):
        nuevas = []
        for r in rels:
            if isinstance(r, dict) and "sujeto_propuesto" in r:
                r = dict(r)
                if "sujeto_mencion" in r:
                    c["sujeto_mencion_y_propuesto"] += 1
                    r.setdefault("_campos_v3", {})["sujeto_propuesto"] = r.pop("sujeto_propuesto")
                else:
                    r["sujeto_mencion"] = r.pop("sujeto_propuesto")
                    c["sujeto_propuesto_como_mencion"] += 1
            nuevas.append(r)
        ti["relations"] = nuevas
    om = ti.pop("omisiones_no_prosa", None)
    items = []
    if isinstance(om, str):
        if om.strip():
            c["omisiones_string_a_lista_de_uno"] += 1
            items = [om]
        else:
            c["omisiones_string_vacio"] += 1
    elif isinstance(om, list):
        items = om
    elif om is not None:
        c["omisiones_no_lista"] += 1
        items = [om]
    salida = []
    for o in items:
        if isinstance(o, str):
            if o.strip():
                salida.append({"nota": o, "_origen": "v3_omisiones_no_prosa"})
                c["omision_v3_leida"] += 1
            else:
                c["omision_v3_string_vacio"] += 1
        else:
            salida.append({"_v3_no_string": o, "_origen": "v3_omisiones_no_prosa"})
            c["omision_v3_no_string"] += 1
    if "omisiones" in ti:
        c["omisiones_r2_en_crudo_v3"] += 1
    else:
        ti["omisiones"] = salida
    return ti, c


# ------------------------------------------------------------------------- #
# Validación                                                                  #
# ------------------------------------------------------------------------- #
CAMPOS_ITEM_ENTIDAD = ("local_id", "type", "label", "punto", "properties", "umbrales")
CAMPOS_ITEM_RELACION = ("source", "target", "predicate", "punto", "sujeto_mencion", "sujeto_id",
                        "sujeto_propuesto_padre_sugerido")


def _str_o_none(v):
    if isinstance(v, str):
        v = v.strip()
        return v or None
    return None


def _coerce_lista(valor):
    if isinstance(valor, str):
        try:
            valor = json.loads(valor)
        except json.JSONDecodeError:
            return None
    return valor if isinstance(valor, list) else None


def _clave_valor(v: Any) -> str:
    if v is None:
        return "<ausente>"
    if isinstance(v, str):
        return v
    return json.dumps(v, ensure_ascii=False, sort_keys=True)


_SIN = object()


class _Registro:
    def __init__(self):
        self.contadores: dict[str, Counter] = defaultdict(Counter)
        self.valores: dict[str, dict[str, Counter]] = defaultdict(lambda: defaultdict(Counter))

    def cuenta(self, campo: str, tratamiento: str, valor: Any = _SIN) -> None:
        self.contadores[campo][tratamiento] += 1
        if valor is not _SIN:
            self.valores[campo][_clave_valor(valor)][tratamiento] += 1

    def exportar(self) -> tuple[dict, dict]:
        cont = {k: dict(sorted(v.items())) for k, v in sorted(self.contadores.items())}
        vals = {k: {vv: dict(sorted(t.items())) for vv, t in sorted(d.items())}
                for k, d in sorted(self.valores.items())}
        return cont, vals


def _rechazo(nivel: str, motivo: str, detalle: str, elemento=None) -> dict:
    r = {"nivel": nivel, "motivo": motivo, "detalle": detalle}
    if elemento is not None:
        r["elemento"] = elemento
    return r


def validar(tool_input: Any, chunk: dict, politica: Optional[Politica] = None,
            forma: str = "r2") -> dict:
    """Valida el input del tool call de un chunk con la política r2. `forma`
    es «r2» (salida del prompt nuevo) o «v3» (crudo guardado del perfil v3 o
    del de desarrollo, leído con `desde_v3`)."""
    pol = politica or politica_default()
    reg = _Registro()
    res: dict[str, Any] = {
        "chunk_id": chunk["id"], "perfil": PERFIL, "forma_entrada": forma,
        "politica_sha256": pol.sha256, "entidades": [], "relaciones": [], "omisiones": [],
        "rechazos": [], "pendientes_no_mapeados": [], "advertencias": [],
        "adaptacion_v3": {}, "campos_no_definidos_salida": {},
    }

    def fin(n_ent: int, n_rel: int) -> dict:
        cont, vals = reg.exportar()
        res["contadores"] = cont
        res["valores"] = vals
        por_motivo = Counter(r["motivo"] for r in res["rechazos"])
        res["metricas"] = {"entities_in": n_ent, "entities_out": len(res["entidades"]),
                           "relations_in": n_rel, "relations_out": len(res["relaciones"]),
                           "omisiones_out": len(res["omisiones"]),
                           "rechazos": len(res["rechazos"]),
                           "rechazos_por_motivo": dict(sorted(por_motivo.items()))}
        return res

    if forma == "v3":
        tool_input, adapt = desde_v3(tool_input)
        res["adaptacion_v3"] = dict(sorted(adapt.items()))
    elif forma != "r2":
        raise ValueError(f"forma desconocida: {forma!r}")

    if isinstance(tool_input, str):
        try:
            tool_input = json.loads(tool_input)
        except json.JSONDecodeError as e:
            res["rechazos"].append(_rechazo("chunk", "salida_no_parseable", f"JSON inválido: {e}"))
            return fin(0, 0)
    if not isinstance(tool_input, dict):
        res["rechazos"].append(_rechazo("chunk", "salida_no_dict", f"tipo {type(tool_input).__name__}"))
        return fin(0, 0)

    for k in tool_input:
        if k not in ("entities", "relations", "omisiones"):
            res["campos_no_definidos_salida"][k] = tool_input[k]
            reg.cuenta("campos_de_la_salida", "a_campos_no_definidos", k)

    entities = _coerce_lista(tool_input.get("entities"))
    relations = _coerce_lista(tool_input.get("relations"))
    if entities is None or relations is None:
        res["rechazos"].append(_rechazo("chunk", "entities_o_relations_invalidos",
                                        "entities/relations ausentes o no-lista (ni como string JSON)"))
        return fin(0, 0)
    for nombre in ("entities", "relations"):
        if isinstance(tool_input.get(nombre), str):
            reg.cuenta("estructura", f"{nombre}_como_string_json")

    admitidos = set(puntos_admitidos(chunk))
    texto_mencion = texto_completo(chunk)

    # ---------------- Entidades ----------------
    por_local: dict[str, dict] = {}
    for i, e in enumerate(entities):
        ref = f"entities[{i}]"
        if not isinstance(e, dict):
            res["rechazos"].append(_rechazo("entidad", "entidad_no_dict", ref, e))
            continue
        local_id = _str_o_none(e.get("local_id"))
        label = _str_o_none(e.get("label"))
        punto = _str_o_none(e.get("punto"))
        if local_id is None:
            res["rechazos"].append(_rechazo("entidad", "local_id_ausente", ref, e))
            continue
        if local_id in por_local:
            res["rechazos"].append(_rechazo("entidad", "local_id_duplicado", f"{ref}: '{local_id}'", e))
            continue
        tipo_crudo = e.get("type")
        tipo, trat = resolver_tipo(tipo_crudo, pol)
        reg.cuenta("tipo_entidad", trat, *(() if trat == "en_lista" else (tipo_crudo,)))
        if tipo is None:
            res["rechazos"].append(_rechazo("entidad", "type_invalido", f"{ref}: '{tipo_crudo}'", e))
            # P-e3: el tipo rechazado se registra como omisión fuera_de_tipos.
            nota = f"label: {label!r}; tipo propuesto: {tipo_crudo!r}"
            om = M.OmisionR2(categoria="fuera_de_tipos", tramo=None, nota=nota,
                             origen="validador_p_e3", tramo_verificado="ausente")
            res["omisiones"].append(om.model_dump(mode="json"))
            reg.cuenta("omisiones", "fuera_de_tipos_por_tipo_rechazado")
            continue
        if label is None:
            res["rechazos"].append(_rechazo("entidad", "label_vacio", ref, e))
            continue
        if punto is None:
            res["rechazos"].append(_rechazo("entidad", "punto_ausente", f"{ref} ({local_id})", e))
            continue
        if punto not in admitidos:
            res["rechazos"].append(_rechazo("entidad", "punto_fuera_de_admitidos",
                                            f"{ref} ({local_id}): '{punto}' ∉ {sorted(admitidos)}", e))
            continue

        originales: dict[str, Any] = {}
        if trat != "en_lista":
            originales["type"] = tipo_crudo
        campos_nd: dict[str, Any] = {}
        for k in e:
            if k not in CAMPOS_ITEM_ENTIDAD:
                campos_nd[k] = e[k]
                reg.cuenta("campos_del_item_entidad", "a_campos_no_definidos", k)

        props_in = e.get("properties")
        if props_in is None:
            props_in = {}
        if not isinstance(props_in, dict):
            campos_nd["properties"] = props_in
            reg.cuenta("properties", "no_dict_a_campos_no_definidos")
            props_in = {}
        props: dict[str, Any] = {}
        no_def: dict[str, Any] = {}
        heredadas: dict[str, Any] = {}
        no_tipados: dict[str, Any] = {}
        fuera: list[str] = []
        definidas = M.CLAVES_R2[tipo]
        for k, v in props_in.items():
            if k in definidas and k != "umbrales":
                if v is None or (isinstance(v, str) and not v.strip()):
                    originales[k] = v
                    reg.cuenta("valores", "vacio_a_ausente", f"{tipo}.{k}")
                    continue
                if tipo == "Comunicacion" and k == "numero":
                    if isinstance(v, int) and not isinstance(v, bool):
                        props[k] = v
                    elif isinstance(v, str) and re.fullmatch(r"\s*(\d+|\d{1,3}(\.\d{3})+)\s*", v):
                        props[k] = int(v.strip().replace(".", ""))
                        originales[k] = v
                        reg.cuenta("valores", "numero_string_a_entero", f"{tipo}.{k}")
                    else:
                        no_tipados[k] = v
                        reg.cuenta("valores", "no_tipado_registrado", f"{tipo}.{k}")
                    continue
                if isinstance(v, str):
                    props[k] = v
                else:
                    no_tipados[k] = v
                    reg.cuenta("valores", "no_tipado_registrado", f"{tipo}.{k}")
            elif k in M.CLAVES_HEREDADAS_V3.get(tipo, ()):
                heredadas[k] = v
                reg.cuenta("claves", "heredada_v3", f"{tipo}.{k}")
            else:
                if k in definidas:      # «umbrales» dentro de properties: lugar equivocado
                    campos_nd[f"properties.{k}"] = v
                    reg.cuenta("claves", "umbrales_en_properties_a_campos_no_definidos", f"{tipo}.{k}")
                else:
                    no_def[k] = v
                    reg.cuenta("claves", "a_properties_no_definidas", f"{tipo}.{k}")

        # Campos con lista cerrada.
        if tipo == "Obligacion":
            v = props.get("tipo")
            if v in M.OBLIGACION_TIPO:
                reg.cuenta("Obligacion.tipo", "en_lista")
            else:
                original = props_in.get("tipo")
                props["tipo"] = pol.d["campos"]["Obligacion.tipo"]["valor_normalizado"]
                originales["tipo"] = original
                no_tipados.pop("tipo", None)
                reg.cuenta("Obligacion.tipo",
                           "ausente_normalizado_a_otra" if v is None else "normalizado_a_otra", original)
        if tipo == "Restriccion":
            v = props.get("tipo")
            if v in M.RESTRICCION_TIPO:
                reg.cuenta("Restriccion.tipo", "en_lista")
            else:
                fuera.append("tipo")
                originales.setdefault("tipo", props_in.get("tipo"))
                reg.cuenta("Restriccion.tipo", "registrado_fuera_de_lista", props_in.get("tipo"))
        if tipo == "Comunicacion":
            v = props.get("tipo")
            der = derivar_comunicacion(props.get("codigo"), label)
            if v in M.COMUNICACION_TIPO:
                reg.cuenta("Comunicacion.tipo", "en_lista")
                if der is not None and v in ("A", "B", "C") and der != v:
                    reg.cuenta("Comunicacion.tipo", "en_lista_discrepa_del_codigo", v)
                    res["advertencias"].append({"tipo": "comunicacion_tipo_discrepa_codigo",
                                                "local_id": local_id,
                                                "detalle": f"tipo {v!r}, código o label dan {der!r}"})
            else:
                original = props_in.get("tipo")
                resuelto = None
                for paso in pol.pasos("Comunicacion.tipo"):
                    if paso == "derivar_de_codigo_o_label" and der is not None:
                        resuelto, trat_c = der, "derivado_de_codigo_o_label"
                        break
                    if paso == "externa_por_lexico":
                        if nombra_norma_externa(original, pol.lexico_externa):
                            resuelto, trat_c = "externa", "externa_por_valor"
                            break
                        if (nombra_norma_externa(props.get("codigo"), pol.lexico_externa)
                                or nombra_norma_externa(label, pol.lexico_externa)):
                            resuelto, trat_c = "externa", "externa_por_codigo_o_label"
                            break
                originales.setdefault("tipo", original)
                if resuelto is not None:
                    props["tipo"] = resuelto
                    reg.cuenta("Comunicacion.tipo", trat_c, original)
                else:
                    fuera.append("tipo")
                    reg.cuenta("Comunicacion.tipo", "registrado_fuera_de_lista", original)
        if tipo == "Obligacion" and ("frecuencia" in props or "frecuencia" in originales
                                     or "frecuencia" in no_tipados):
            v = props.get("frecuencia")
            if "frecuencia" in no_tipados:
                reg.cuenta("Obligacion.frecuencia", "no_tipado_registrado", no_tipados["frecuencia"])
            elif v is None:
                reg.cuenta("Obligacion.frecuencia", "vacio_a_ausente")
            elif v in M.FRECUENCIA:
                reg.cuenta("Obligacion.frecuencia", "en_lista")
            else:
                f = frecuencia_desde_tramo(v)
                originales["frecuencia"] = v
                if f is not None:
                    props["frecuencia"] = f
                    reg.cuenta("Obligacion.frecuencia", "normalizado_desde_tramo", v)
                else:
                    fuera.append("frecuencia")
                    reg.cuenta("Obligacion.frecuencia", "registrado_fuera_de_lista", v)

        # Umbrales del ítem (forma r2b): tramos literales.
        tramos: list[str] = []
        if "umbrales" in e:
            u = e.get("umbrales")
            if tipo not in M.TIPOS_CON_UMBRALES:
                campos_nd["umbrales"] = u
                reg.cuenta("umbrales", "tipo_sin_umbrales_a_campos_no_definidos", tipo)
            elif isinstance(u, list):
                invalidos = []
                for x in u:
                    t = _str_o_none(x.get("tramo")) if isinstance(x, dict) else None
                    if t is not None and set(x) == {"tramo"}:
                        tramos.append(x["tramo"])
                        reg.cuenta("umbrales", "tramo")
                    else:
                        invalidos.append(x)
                        reg.cuenta("umbrales", "item_invalido_a_campos_no_definidos")
                if invalidos:
                    campos_nd["umbrales_invalidos"] = invalidos
            elif u is not None:
                campos_nd["umbrales"] = u
                reg.cuenta("umbrales", "no_lista_a_campos_no_definidos")

        ent = M.EntidadR2(
            local_id=local_id, type=tipo, label=label, punto=punto,
            provenance=M.Provenance(to=chunk["to"], archivo=chunk["archivo"], punto=punto,
                                    rol_documental=rol_documental_de_punto(chunk, punto)),
            properties=props, umbrales_tramos=tramos, fuera_de_lista=fuera, originales=originales,
            properties_no_definidas=no_def, campos_heredados_v3=heredadas,
            valores_no_tipados=no_tipados, campos_no_definidos=campos_nd)
        d = ent.model_dump(mode="json")
        por_local[local_id] = d
        res["entidades"].append(d)
        if len(label.split()) > 12:
            res["advertencias"].append({"tipo": "label_largo", "local_id": local_id,
                                        "detalle": f"{len(label.split())} palabras"})

    # ---------------- Relaciones ----------------
    for i, r in enumerate(relations):
        ref = f"relations[{i}]"
        if not isinstance(r, dict):
            res["rechazos"].append(_rechazo("relacion", "relacion_no_dict", ref, r))
            continue
        pred_crudo = r.get("predicate")
        pred, trat = resolver_predicado(pred_crudo, pol)
        reg.cuenta("predicado", trat, *(() if trat == "en_lista" else (pred_crudo,)))
        if pred is None:
            res["rechazos"].append(_rechazo("relacion", "predicado_invalido", f"{ref}: '{pred_crudo}'", r))
            continue
        punto = _str_o_none(r.get("punto"))
        if punto is None:
            res["rechazos"].append(_rechazo("relacion", "punto_ausente", f"{ref} ({pred})", r))
            continue
        if punto not in admitidos:
            res["rechazos"].append(_rechazo("relacion", "punto_fuera_de_admitidos",
                                            f"{ref} ({pred}): '{punto}' ∉ {sorted(admitidos)}", r))
            continue
        originales = {} if trat == "en_lista" else {"predicate": pred_crudo}
        campos_nd = {}
        for k in r:
            if k not in CAMPOS_ITEM_RELACION:
                campos_nd[k] = r[k]
                reg.cuenta("campos_del_item_relacion", "a_campos_no_definidos", k)
        source = _str_o_none(r.get("source"))
        target = _str_o_none(r.get("target"))
        sujeto_id = _str_o_none(r.get("sujeto_id"))
        mencion = _str_o_none(r.get("sujeto_mencion"))
        padre = _str_o_none(r.get("sujeto_propuesto_padre_sugerido"))
        extra: dict[str, Any] = {}

        if pred in M.PREDICADOS_SUJETO:
            ignorado = "target" if pred == "aplica_a" else "source"
            if (target if pred == "aplica_a" else source) is not None:
                campos_nd[f"{ignorado}_ignorado"] = r.get(ignorado)
                reg.cuenta("campos_del_item_relacion", "extremo_sujeto_ignorado", ignorado)
            if pred == "aplica_a":
                target = None
            else:
                source = None
            if sujeto_id is None and mencion is None:
                res["rechazos"].append(_rechazo("relacion", "sujeto_extremo_ausente",
                                                f"{ref} ({pred}): sin sujeto_id ni mención", r))
                reg.cuenta("sujeto", "rechazada_sin_sujeto_id_ni_mencion")
                continue
            if padre is not None and mencion is None:
                res["rechazos"].append(_rechazo("relacion", "padre_sugerido_sin_mencion", ref, r))
                reg.cuenta("padre_sugerido", "rechazada_sin_mencion", padre)
                continue
            extremo = source if pred == "aplica_a" else target
            campo = "source" if pred == "aplica_a" else "target"
            if extremo is None:
                res["rechazos"].append(_rechazo("relacion", "extremo_chunk_ausente",
                                                f"{ref} ({pred}): falta {campo}", r))
                continue
            ent = por_local.get(extremo)
            if ent is None:
                res["rechazos"].append(_rechazo("relacion", "ref_colgante",
                                                f"{ref} ({pred}): {campo}='{extremo}'", r))
                continue
            src_t, tgt_t = ((ent["type"], M.TIPO_SUJETO) if pred == "aplica_a"
                            else (M.TIPO_SUJETO, ent["type"]))
            if not M.firma_r2(src_t, pred, tgt_t):
                res["rechazos"].append(_rechazo("relacion", "firma_invalida",
                                                f"{ref}: {src_t} --{pred}--> {tgt_t}", r))
                continue
            sid_modelo = None
            if sujeto_id is not None:
                if sujeto_id in M.SUJETOS_R2_SET:
                    sid_modelo = sujeto_id
                    reg.cuenta("sujeto_id", "en_catalogo")
                else:
                    originales["sujeto_id"] = sujeto_id
                    reg.cuenta("sujeto_id", "fuera_de_catalogo_a_no_mapeados", sujeto_id)
            if sujeto_id is not None and mencion is not None:
                reg.cuenta("sujeto", "ambos_campos")
            pad_ok = None
            pad_crudo = None
            if padre is not None:
                if padre in M.SUJETOS_R2_SET:
                    pad_ok = padre
                    reg.cuenta("padre_sugerido", "en_catalogo")
                else:
                    pad_crudo = padre
                    reg.cuenta("padre_sugerido", "fuera_de_catalogo_anulado", padre)
            if mencion is None:
                nivel, literal = "ausente", None
            else:
                nivel, literal = verificar_tramo(mencion, texto_mencion, pol.holgura)
            reg.cuenta("sujeto_mencion", nivel)
            mencion_final, mencion_modelo = mencion, None
            if nivel == "tokens" and literal is not None:
                mencion_final, mencion_modelo = literal, mencion
            extra = dict(sujeto_mencion=mencion_final, sujeto_mencion_modelo=mencion_modelo,
                         mencion_verificada=nivel, sujeto_id_modelo=sid_modelo,
                         padre_sugerido=pad_ok, padre_sugerido_crudo=pad_crudo)
            motivo = None
            if sujeto_id is not None and sid_modelo is None:
                motivo = "id_fuera_de_catalogo"
            elif nivel == "no" and sid_modelo is None:
                motivo = "mencion_no_verificada"
            if motivo:
                res["pendientes_no_mapeados"].append({
                    "chunk_id": chunk["id"], "indice_relacion": i, "punto": punto, "predicado": pred,
                    "extremo_local_id": extremo, "extremo_tipo": ent["type"], "mencion": mencion,
                    "mencion_verificada": nivel, "sujeto_id_crudo": sujeto_id,
                    "padre_sugerido_crudo": padre, "motivo": motivo})
                reg.cuenta("no_mapeados_pendientes", motivo)
        else:
            if sujeto_id or mencion or padre:
                res["rechazos"].append(_rechazo("relacion", "sujeto_en_predicado_no_sujeto",
                                                f"{ref}: sujeto_* solo vale en {M.PREDICADOS_SUJETO}", r))
                continue
            if source is None or target is None:
                res["rechazos"].append(_rechazo("relacion", "extremo_chunk_ausente",
                                                f"{ref} ({pred}): requiere source y target", r))
                continue
            se, te = por_local.get(source), por_local.get(target)
            if se is None or te is None:
                res["rechazos"].append(_rechazo("relacion", "ref_colgante",
                                                f"{ref} ({pred}): source='{source}' target='{target}'", r))
                continue
            src_t, tgt_t = se["type"], te["type"]
            if not M.firma_r2(src_t, pred, tgt_t):
                res["rechazos"].append(_rechazo("relacion", "firma_invalida",
                                                f"{ref}: {src_t} --{pred}--> {tgt_t}", r))
                continue
            if pred in ("prohibe", "limita"):
                rt = se["properties"].get("tipo")
                if rt == "prohibicion" or (isinstance(rt, str) and rt.startswith("limite_")):
                    esperado = "prohibe" if rt == "prohibicion" else "limita"
                    coh = "coherente" if esperado == pred else "incoherente"
                else:
                    coh = "no_evaluable"
                extra["coherencia_tipo_predicado"] = coh
                reg.cuenta("coherencia_tipo_predicado", f"{pred}:{coh}", f"{rt}→{pred}")
                if coh == "incoherente":
                    res["advertencias"].append({"tipo": "bkl_0038_incoherencia_tipo_predicado",
                                                "detalle": f"{ref}: Restriccion.tipo {rt!r} con {pred}"})

        nueva = not M.firma_congelada(src_t, pred, tgt_t)
        if nueva:
            reg.cuenta("firma", f"nueva_r2:{src_t}-{pred}-{tgt_t}")
        else:
            reg.cuenta("firma", "congelada")
        rel = M.RelacionR2(
            source=source, target=target, predicate=pred, punto=punto,
            provenance=M.Provenance(to=chunk["to"], archivo=chunk["archivo"], punto=punto,
                                    rol_documental=rol_documental_de_punto(chunk, punto)),
            tipo_source=src_t, tipo_target=tgt_t, no_verificada_e3=nueva, indice_crudo=i,
            originales=originales, campos_no_definidos=campos_nd, **extra)
        res["relaciones"].append(rel.model_dump(mode="json"))

    # ---------------- Omisiones ----------------
    oms = tool_input.get("omisiones")
    if isinstance(oms, str):
        if oms.strip():
            reg.cuenta("omisiones", "string_a_lista_de_uno")
            oms = [oms]
        else:
            reg.cuenta("omisiones", "string_vacio_a_ausente")
            oms = []
    elif oms is None:
        oms = []
    elif not isinstance(oms, list):
        res["rechazos"].append(_rechazo("omision", "omisiones_no_lista", "omisiones", oms))
        oms = []
    texto_propio = chunk.get("texto") or ""
    flags = chunk.get("flags") or {}
    for j, o in enumerate(oms):
        origen = "e1"
        if isinstance(o, dict) and o.get("_origen") == "v3_omisiones_no_prosa":
            origen = "v3_omisiones_no_prosa"
            if "_v3_no_string" in o:
                res["rechazos"].append(_rechazo("omision", "omision_v3_no_string", f"omisiones[{j}]",
                                                o["_v3_no_string"]))
                continue
            om = M.OmisionR2(categoria=None, tramo=None, nota=o["nota"], origen=origen,
                             tramo_verificado="ausente")
            res["omisiones"].append(om.model_dump(mode="json"))
            reg.cuenta("omisiones", "v3_sin_categoria_ni_tramo")
            continue
        if isinstance(o, str):
            if not o.strip():
                reg.cuenta("omisiones", "item_string_vacio_a_ausente")
                continue
            o = {"nota": o}
            reg.cuenta("omisiones", "item_string_a_nota")
        if not isinstance(o, dict):
            res["rechazos"].append(_rechazo("omision", "omision_no_objeto", f"omisiones[{j}]", o))
            continue
        fuera, originales, campos_nd = [], {}, {}
        for k in o:
            if k not in ("categoria", "tramo", "nota"):
                campos_nd[k] = o[k]
        cat = _str_o_none(o.get("categoria"))
        if cat is None or cat not in M.CATEGORIA_OMISION:
            fuera.append("categoria")
            originales["categoria"] = o.get("categoria")
            reg.cuenta("omisiones", "categoria_registrada_fuera_de_lista", o.get("categoria"))
        else:
            reg.cuenta("omisiones", f"categoria:{cat}")
        tramo = _str_o_none(o.get("tramo"))
        tramo_modelo, corto = None, False
        if tramo is None:
            nivel = "ausente"
        else:
            nivel, literal = verificar_tramo(tramo, texto_propio, pol.holgura)
            if nivel == "tokens" and literal is not None:
                tramo, tramo_modelo = literal, o.get("tramo")
            corto = len(norm_tokens(tramo)) < pol.largo_min_omision
            if corto:
                reg.cuenta("omisiones", "tramo_corto")
        reg.cuenta("omisiones", f"tramo:{nivel}")
        senal = ((cat == "tabla" and not flags.get("contenido_tabular"))
                 or (cat == "formula" and not flags.get("formula")))
        if senal:
            reg.cuenta("omisiones", "senal_tabla_no_detectada")
        nota = o.get("nota") if isinstance(o.get("nota"), str) else None
        if o.get("nota") is not None and nota is None:
            campos_nd["nota"] = o.get("nota")
        om = M.OmisionR2(categoria=cat, tramo=tramo, nota=nota, origen=origen,
                         tramo_verificado=nivel, tramo_modelo=tramo_modelo, tramo_corto=corto,
                         senal_tabla_no_detectada=senal, fuera_de_lista=fuera, originales=originales,
                         campos_no_definidos=campos_nd)
        res["omisiones"].append(om.model_dump(mode="json"))

    if chunk_flaggeado(chunk):
        extrajo = any(x["type"] != "TextoOrdenado" for x in res["entidades"])
        con_omision = any(x["origen"] != "validador_p_e3" for x in res["omisiones"])
        if extrajo and not con_omision:
            reg.cuenta("chunk_marcado", "con_extraccion_sin_omision")
            res["advertencias"].append({"tipo": "flag_sin_omisiones_declaradas",
                                        "detalle": "chunk marcado por E0 con extracción y sin omisiones"})
        elif not extrajo and not con_omision:
            reg.cuenta("chunk_marcado", "sin_extraccion_sin_omision")

    return fin(len(entities), len(relations))
