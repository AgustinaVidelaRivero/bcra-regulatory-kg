"""
derivar_catalogo_r2.py — U-CAT-UNICO C2: catálogo de sujetos r2, derivado del
v3 por operaciones declaradas (L-ESQ-R2 §7.3, firmada en 4ef7650).

Entrada: data/experiment/catalogo_unico/catalogo_sujetos_v3.json (candado de
sha256). Salida: data/experiment/catalogo_unico/catalogo_sujetos_r2.json, con
el mismo esquema (formato catalogo_sujetos_unico/1). Ninguna llamada a la API.

Operaciones (cada una queda registrada en `fuentes` con clave `r2_op_NN`, y la
`procedencia` de cada campo tocado apunta a ella o a su ancla):
  BKL-0028  altas de Sujeto_entidad_financiera_del_exterior,
            Sujeto_banco_del_exterior y Sujeto_entidad_cambiaria_del_exterior;
            cambio de alias en Sujeto_entidad_financiera, Sujeto_banco y
            Sujeto_entidad_cambiaria: los alias «del exterior» salen de la
            entrada doméstica y pasan al id nuevo (el plural, como label).
  BKL-0029  alta de Sujeto_titular_de_cuenta_corriente_en_el_bcra; cambio de
            miembro del rol de convca a ese id, y su residuo declarado queda
            sin el campo colectivo_operativo_sin_id; cambio de residuo:
            `remedio` y `anidacion_no_estricta` pasan al estado r2.
  BKL-0034  alta de la clase Sujeto_instancia_de_gobierno_societario y, bajo
            ella, Sujeto_directorio, Sujeto_alta_gerencia y
            Sujeto_comite_de_auditoria. Nombre de la clase: decisión de la
            autora del 01/10/2026; en el corpus, «órgano de gobierno» designa a
            la asamblea de accionistas o socios (lavdin::1.3.1.2).

Anclas: cada label, alias, definición y padre de un id nuevo lleva su ancla en
el texto del corpus (TO::punto) con el extracto literal, que este script
VERIFICA contra el chunk de E0 (texto heredado + texto propio, con los cortes
de palabra con guion al fin de línea unidos y los espacios colapsados). Si un
extracto no aparece, se frena. Lo que no tiene ancla queda NO ENCONTRADO
(campo vacío o nulo) y no se inventa.

Ubicación de los ids nuevos: al final de los vigentes, en el orden de las
operaciones; el bloque los agrupa al final de su encabezado.

Enmienda L-ESQ-R2: se lee la versión FIRMADA, `git show 4ef7650:<ruta>`, con
candado de sha256 (66c4a1b9…), y no el archivo del árbol, que puede llevar
notas posteriores a la firma. En `fuentes.enmienda_l_esq_r2` del JSON quedan
ruta y sha256; el commit queda en ENMIENDA_COMMIT, sin campo nuevo en el JSON,
para que el catálogo siga byte a byte igual al de bd2122d.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/catalogo_unico/code/derivar_catalogo_r2.py
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import copy  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import subprocess  # noqa: E402
from pathlib import Path  # noqa: E402

AQUI = Path(__file__).resolve().parent
CATALOGO_UNICO = AQUI.parent
REPO = AQUI.parents[3]
CAT_V3 = CATALOGO_UNICO / "catalogo_sujetos_v3.json"
SALIDA = CATALOGO_UNICO / "catalogo_sujetos_r2.json"

CAT_V3_SHA256 = "9a2522e41e1086d26bb73a37070efd9913f98ec36e2f957e198b460d21ca6c58"
ENMIENDA_RUTA = "data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md"
ENMIENDA_COMMIT = "4ef7650"  # firma de L-ESQ-R2
ENMIENDA_SHA256 = "66c4a1b9c5edaee1b7c4adeae9534e4829e68241b690eb1e244b8d9128baca72"
PARTICION = REPO / "data" / "experiment" / "segmentacion_84" / "b584_particion"
E0_DEV = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_enm01"
TOS_DEV = ("pro", "cla", "ric", "cap", "ext")

DECISION = "data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md §7.3 (firmada en 4ef7650, 30/09/2026)"
ALTA_R2 = DECISION
NO_ENCONTRADO = "NO ENCONTRADO"

# Clase de BKL-0034. El término «órgano de gobierno» de §7.3 se reemplazó por
# decisión de la autora del 01/10/2026: en el corpus designa a la asamblea de
# accionistas o socios, distinta del órgano de administración (Directorio).
ID_INSTANCIA = "Sujeto_instancia_de_gobierno_societario"
LABEL_INSTANCIA = "Instancias de gobierno societario"
DECISION_NOMBRE_INSTANCIA = (
    "nombre de la clase por decisión de la autora del 01/10/2026 (revisión de C2), en lugar de «órgano de "
    "gobierno»: en el corpus «órgano(s) de gobierno» designa a la asamblea de accionistas o socios "
    "(lavdin::1.3.1.2; lingeef::1.2::intro)")


class FrenoDerivacion(RuntimeError):
    """Una precondición de la derivación no se cumple: se frena."""


def sha256_archivo(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _rel(p: Path) -> str:
    return str(p.resolve().relative_to(REPO))


def sha256_enmienda_firmada() -> str:
    """sha256 de la enmienda tal como quedó en el commit de la firma
    (`git show 4ef7650:<ruta>`); frena si no reproduce ENMIENDA_SHA256."""
    r = subprocess.run(["git", "-C", str(REPO), "show", f"{ENMIENDA_COMMIT}:{ENMIENDA_RUTA}"],
                       capture_output=True, check=False)
    if r.returncode != 0:
        raise FrenoDerivacion(f"no se pudo leer {ENMIENDA_COMMIT}:{ENMIENDA_RUTA} con git show")
    sha = hashlib.sha256(r.stdout).hexdigest()
    if sha != ENMIENDA_SHA256:
        raise FrenoDerivacion(f"candado: la enmienda en {ENMIENDA_COMMIT} da {sha[:12]}… "
                              f"(esperado {ENMIENDA_SHA256[:12]}…)")
    return sha


# ------------------------------------------------------------------------- #
# Corpus (E0) y verificación de anclas                                        #
# ------------------------------------------------------------------------- #
def ruta_chunks(to: str) -> Path:
    return (E0_DEV / f"chunks_{to}.json") if to in TOS_DEV else (PARTICION / to / f"chunks_{to}.json")


_CACHE_E0: dict[str, dict] = {}


def chunk(cid: str) -> dict:
    to = cid.split("::", 1)[0]
    if to not in _CACHE_E0:
        _CACHE_E0[to] = {c["id"]: c for c in json.loads(ruta_chunks(to).read_text(encoding="utf-8"))}
    if cid not in _CACHE_E0[to]:
        raise FrenoDerivacion(f"ancla {cid}: el chunk no existe en {_rel(ruta_chunks(to))}")
    return _CACHE_E0[to][cid]


def _normalizar(s: str) -> str:
    return " ".join(re.sub(r"-\n", "", s).split())


def texto_verificable(c: dict) -> str:
    """Texto heredado (encabezados) + texto propio del chunk, normalizado."""
    partes = [h.get("texto", "") for h in c.get("herencia") or []] + [c["texto"]]
    return _normalizar("\n".join(partes))


def ancla(cid: str, texto: str) -> dict:
    """Verifica que `texto` esté literalmente en el chunk y devuelve el registro."""
    c = chunk(cid)
    if _normalizar(texto) not in texto_verificable(c):
        raise FrenoDerivacion(f"ancla {cid}: el extracto no aparece en el chunk: {texto[:70]!r}")
    to = cid.split("::", 1)[0]
    return {"chunk": cid, "archivo": c["archivo"], "ruta": _rel(ruta_chunks(to)),
            "sha256": sha256_archivo(ruta_chunks(to)), "texto": texto}


def fuente_anclas(anclas: list[dict], nota: str | None = None) -> dict:
    d = {"objeto": "ancla en el corpus (TO::punto), verificada contra el chunk de E0", "anclas": anclas}
    if nota:
        d["nota"] = nota
    return d


def fuente_no_encontrado(nota: str, contrarias: list[dict] | None = None) -> dict:
    d = {"objeto": NO_ENCONTRADO, "nota": nota}
    if contrarias:
        d["anclas_contrarias"] = contrarias
    return d


# ------------------------------------------------------------------------- #
# Ids nuevos (altas)                                                          #
# ------------------------------------------------------------------------- #
def altas() -> list[dict]:
    """Una entrada por id nuevo: valores, anclas por campo y operación."""
    contraparte_512 = ancla("ext::5.12::intro", "Dichas entidades podrán realizar operaciones de arbitrajes y "
                                                "canjes en el exterior siempre que la contraparte sea:")
    ccbcra_11 = ancla("ccbcra::1.1", "Las entidades financieras deberán mantener abierta en el Banco Central de "
                                     "la República Argentina una cuenta corriente en pesos. Dicha cuenta tendrá "
                                     "carácter optativo para las cajas de crédito (Ley 25.782) y las entidades "
                                     "cambiarias.")
    lingob_12 = ancla("lingob::1.2::intro", "El código de gobierno societario se refiere a la manera en la que el "
                                            "Directorio y la Alta Gerencia de la entidad financiera dirigen sus "
                                            "actividades y negocios")
    lingob_41 = ancla("lingob::4.1", "los miembros del Directorio que integren el Comité de auditoría")
    return [
        {"bkl": "BKL-0028", "id": "Sujeto_entidad_financiera_del_exterior", "nivel": "clase",
         "grupo_bloque": "## Contrapartes", "padre": "Sujeto_contraparte",
         "label": "Entidades financieras del exterior", "alias": ["Entidad financiera del exterior"],
         "definicion": ("ES la entidad que, constituida de acuerdo con el derecho extranjero aplicable, tiene "
                        "por actividad permitida desarrollar en las plazas del exterior en que opera la "
                        "intermediación habitual entre la oferta y la demanda de recursos financieros "
                        "(depósitos del público) en los términos de la Ley de Entidades Financieras argentina, "
                        "independientemente del tipo social que adopte y de su carácter público, privado o mixto."),
         "provenance_esqueleto": {"source_doc": "ctacor.pdf", "location": "Punto 1.4"},
         "fuentes": {
             "label": fuente_anclas([ancla("ctacor::1.4", "1.4. Entidades financieras del exterior.")],
                                    "el alias plural del v3 pasa a ser el label del id nuevo"),
             "alias": fuente_anclas([ancla("ext::5.12.2", "una entidad financiera del exterior de propiedad "
                                                          "total o mayoritaria de estados extranjeros")]),
             "definicion": fuente_anclas([ancla(
                 "ctacor::1.4", "se considerarán entidades financieras del exterior a aquellas que, constituidas "
                 "de acuerdo con el derecho extranjero aplicable, tengan por actividad permitida desarrollar en "
                 "las plazas del exterior en que operen, la intermediación habitual entre la oferta y la demanda "
                 "de recursos financieros -depósitos del público- en los términos de la Ley de Entidades "
                 "Financieras argentina y su reglamentación independientemente del tipo social que adopten y/o "
                 "de su carácter público, privado o mixto")]),
             "padre": fuente_anclas([contraparte_512, ancla("ext::5.12.2", "una entidad financiera del exterior")],
                                    "el TO la nombra como contraparte; no es subclase de Sujeto_entidad_financiera "
                                    "(ctacor::1.1 y 1.4 separan «del país» de «del exterior»)"),
         }},
        {"bkl": "BKL-0028", "id": "Sujeto_banco_del_exterior", "nivel": "clase",
         "grupo_bloque": "## Contrapartes", "padre": "Sujeto_contraparte",
         "label": "Bancos del exterior", "alias": ["Banco del exterior"], "definicion": None,
         "provenance_esqueleto": {"source_doc": "actgar.pdf", "location": "Punto 2.3.3.2"},
         "fuentes": {
             "label": fuente_anclas([ancla("actgar::2.3.3.2", "2.3.3.2. Bancos del exterior que cumplan con lo "
                                                              "previsto en el punto 3.1.")],
                                    "el alias plural del v3 pasa a ser el label del id nuevo"),
             "alias": fuente_anclas([ancla("actgar::2.2.1.2", "a) Ser un banco del exterior")]),
             "definicion": fuente_no_encontrado("ningún punto del corpus define «banco del exterior»; búsqueda "
                                                "de patrones definitorios sobre los 157 TOs sin resultado"),
             "padre": fuente_anclas([ancla("actgar::2.2.1.2", "iii) La contraparte deberá: a) Ser un banco del "
                                                              "exterior")],
                                    "el TO lo nombra como contraparte; que sea subclase de "
                                    "Sujeto_entidad_financiera_del_exterior no está dicho en el texto"),
         }},
        {"bkl": "BKL-0028", "id": "Sujeto_entidad_cambiaria_del_exterior", "nivel": "clase",
         "grupo_bloque": "## Contrapartes", "padre": "Sujeto_contraparte",
         "label": "Entidades cambiarias del exterior", "alias": ["Compañía cambista del exterior"],
         "definicion": None,
         "provenance_esqueleto": {"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 5.12.3"},
         "fuentes": {
             "label": fuente_anclas([ancla("ext::5.12.3", "una entidad financiera o cambiaria del exterior")],
                                    "forma elíptica («entidad financiera o cambiaria del exterior»); el plural "
                                    "literal no aparece en el corpus"),
             "alias": fuente_no_encontrado("«compañía cambista del exterior» no aparece en los 157 TOs; viene del "
                                           "catálogo v3 (esquema_v2_clases.json) y docs/esquema_v2_diseño.md:204 la "
                                           "lista como concepto #110; el pasaje más cercano es ext::5.12.4 («una "
                                           "compañía del exterior que se dedique a la compraventa de billetes»). Pasa "
                                           "al id nuevo por la decisión, sin ancla literal"),
             "definicion": fuente_no_encontrado("ningún punto del corpus define la entidad cambiaria del exterior"),
             "padre": fuente_anclas([contraparte_512, ancla("ext::5.12.3", "una entidad financiera o cambiaria del "
                                                                           "exterior")],
                                    "el TO la nombra como contraparte"),
         }},
        {"bkl": "BKL-0029", "id": "Sujeto_titular_de_cuenta_corriente_en_el_bcra", "nivel": "clase",
         "grupo_bloque": "## Sujetos regulados", "padre": "Sujeto_sujeto_regulado",
         "label": "Titulares de cuenta corriente en el BCRA", "alias": ["Cuentacorrentistas del Banco Central"],
         "definicion": ("ES la entidad que mantiene abierta una cuenta corriente en el Banco Central de la "
                        "República Argentina, obligatoria para las entidades financieras y optativa para las "
                        "cajas de crédito (Ley 25.782) y las entidades cambiarias."),
         "provenance_esqueleto": {"source_doc": "convca.pdf", "location": "Punto 2.1.3"},
         "fuentes": {
             "label": fuente_anclas([ancla("convca::2.1.3", "Los titulares de cuentas corrientes en este Banco "
                                                            "Central")]),
             "alias": fuente_anclas([ancla("convca::2.1::intro", "ordenadas por cuentacorrentistas del Banco "
                                                                 "Central")],
                                    "encabezado del punto 2.1 (texto heredado del chunk)"),
             "definicion": fuente_anclas([ccbcra_11]),
             "padre": fuente_anclas([ccbcra_11, ancla("convca::1.1", "a solicitud de las entidades financieras y "
                                                                     "otras habilitadas")],
                                    "los titulares que enumera ccbcra::1.1 (entidades financieras, cajas de "
                                    "crédito, entidades cambiarias) son clases de Sujeto_sujeto_regulado"),
         }},
        {"bkl": "BKL-0034", "id": ID_INSTANCIA, "nivel": "clase",
         "grupo_bloque": "## Sujetos regulados", "padre": "Sujeto_sujeto_regulado",
         "label": LABEL_INSTANCIA, "alias": [], "definicion": None,
         "provenance_esqueleto": {"source_doc": "lingob.pdf", "location": "Punto 1.2"},
         "op_extra": {"nota": DECISION_NOMBRE_INSTANCIA,
                      "anclas": [ancla("lavdin::1.3.1.2", "miembro de los órganos de gobierno (accionistas, "
                                                          "socios o equivalentes), de administración (directores, "
                                                          "consejeros o autoridades equivalentes)"),
                                 ancla("lingeef::1.2::intro", "la Asamblea de Accionistas u órgano de gobierno de "
                                                              "la sociedad")]},
         "fuentes": {
             "label": fuente_anclas([ancla("lingob::1.2::intro", "El código de gobierno societario se refiere a la "
                                                                 "manera en la que el Directorio y la Alta Gerencia "
                                                                 "de la entidad financiera dirigen sus actividades")],
                                    "el corpus usa «gobierno societario»; el label «Instancias de gobierno "
                                    "societario» no aparece literal (0 apariciones en los 157 TOs)"),
             "definicion": fuente_no_encontrado("ningún punto del corpus define un colectivo que reúna Directorio, "
                                                "Alta Gerencia y Comité de auditoría"),
             "padre": fuente_anclas([ancla("lingob::2.1::intro", "El Directorio y cada uno de sus miembros –según "
                                                                 "corresponda–, deberán velar por la liquidez y "
                                                                 "solvencia de la entidad financiera"), lingob_12],
                                    "la norma dirige deberes a los órganos que la clase reúne; padre propuesto por "
                                    "U-CAT-UNICO"),
         }},
        {"bkl": "BKL-0034", "id": "Sujeto_directorio", "nivel": "clase",
         "grupo_bloque": "## Sujetos regulados", "padre": ID_INSTANCIA,
         "label": "Directorio", "alias": ["Consejo de Administración"],
         "definicion": ("ES el Directorio de la entidad financiera o el órgano o autoridad que cumpla funciones "
                        "semejantes, independientemente de la designación que utilice la entidad."),
         "provenance_esqueleto": {"source_doc": "lingob.pdf", "location": "Punto 1.3"},
         "fuentes": {
             "label": fuente_anclas([ancla("lingob::1.3::intro", "El Directorio de la entidad financiera, entre "
                                                                 "otros aspectos, será responsable de:")]),
             "alias": fuente_anclas([ancla("ctacor::2.1", "aprobada por el Directorio o Consejo de Administración"),
                                     ancla("nmcief::S2", "el Directorio o Consejo de Administración de la entidad "
                                                         "financiera")]),
             "definicion": fuente_anclas([ancla("lingob::1.5", "Asamblea de accionistas o Directorio: órganos o "
                                                               "autoridades que cumplan funciones semejantes, "
                                                               "independientemente de la designación utilizada "
                                                               "por las entidades financieras.")]),
             "padre": fuente_anclas([ancla("lingob::2.1.7", "Realice la autoevaluación de su desempeño como "
                                                            "órgano"), lingob_12]),
         }},
        {"bkl": "BKL-0034", "id": "Sujeto_alta_gerencia", "nivel": "clase",
         "grupo_bloque": "## Sujetos regulados", "padre": ID_INSTANCIA,
         "label": "Alta Gerencia", "alias": [],
         "definicion": ("ES la Gerencia General y los gerentes que tienen poder decisorio y dependen "
                        "directamente de ella o del presidente del Directorio."),
         "provenance_esqueleto": {"source_doc": "lingob.pdf", "location": "Punto 1.4"},
         "fuentes": {
             "label": fuente_anclas([ancla("lingob::1.4::intro", "La Alta Gerencia, entre otros aspectos, será "
                                                                 "responsable de:")]),
             "definicion": fuente_anclas([ancla("lingob::1.5", "Alta Gerencia: Gerencia General y gerentes que "
                                                               "tengan poder decisorio y dependan directamente de "
                                                               "ésta o del presidente del Directorio")]),
             "padre": fuente_anclas([lingob_12]),
         }},
        {"bkl": "BKL-0034", "id": "Sujeto_comite_de_auditoria", "nivel": "clase",
         "grupo_bloque": "## Sujetos regulados", "padre": ID_INSTANCIA,
         "label": "Comité de auditoría", "alias": [],
         "definicion": ("ES el comité, integrado por miembros del Directorio, que asiste al Directorio o autoridad "
                        "equivalente en el monitoreo de los controles internos, la gestión de riesgos y el "
                        "cumplimiento de normas, del proceso de emisión de los estados financieros, de la "
                        "idoneidad e independencia del auditor externo y del desempeño de las auditorías interna "
                        "y externa."),
         "provenance_esqueleto": {"source_doc": "lingob.pdf", "location": "Punto 4.1"},
         "fuentes": {
             "label": fuente_anclas([ancla("lingob::4.1", "4.1. Comité de auditoría.")]),
             "definicion": fuente_anclas([ancla(
                 "nmcief::S2", "El Comité de Auditoría será responsable de asistir, en el marco de sus funciones "
                 "específicas, al Directorio o autoridad equivalente en el monitoreo de: (1) los controles "
                 "internos, gestión de riesgos individuales y corporativos y el cumplimiento de normas "
                 "establecidas por la entidad"), lingob_41]),
             "padre": fuente_anclas([lingob_41], "Sección 4 («Comités») de los lineamientos para el gobierno "
                                                 "societario"),
         }},
    ]


# Cambios de alias (BKL-0028): id doméstico → (alias que salen, id que los recibe).
CAMBIOS_ALIAS = (
    ("Sujeto_entidad_financiera", ("Entidades financieras del exterior", "Entidad financiera del exterior"),
     "Sujeto_entidad_financiera_del_exterior"),
    ("Sujeto_banco", ("Bancos del exterior", "Banco del exterior"), "Sujeto_banco_del_exterior"),
    ("Sujeto_entidad_cambiaria", ("Entidades cambiarias del exterior", "Compañía cambista del exterior"),
     "Sujeto_entidad_cambiaria_del_exterior"),
)

ROL_CONVCA = "Sujeto_rol_alcance_convca"
MIEMBRO_CONVCA_ANTES = ["Sujeto_entidad_financiera"]
MIEMBRO_CONVCA_DESPUES = ["Sujeto_titular_de_cuenta_corriente_en_el_bcra"]
CAMPO_RESIDUO_QUE_SALE = "colectivo_operativo_sin_id"

# Residuo de convca al estado r2 (decisión de la autora del 01/10/2026, revisión
# de C2): `remedio` y `anidacion_no_estricta`; los demás campos no se tocan.
DECISION_RESIDUO = "actualización al estado r2 por decisión de la autora del 01/10/2026 (revisión de C2)"
REMEDIO_R2 = ("aplicado en r2 (L-ESQ-R2 §7.3, BKL-0029): se abrió Sujeto_titular_de_cuenta_corriente_en_el_bcra "
              "y el rol lo tiene como miembro en lugar de Sujeto_entidad_financiera")
CAMPO_ANIDACION_QUE_SALE = "regla_3_no_mitiga"
ESTADO_R2_ANIDACION = (
    "sin efecto sobre el rol en r2: su miembro es Sujeto_titular_de_cuenta_corriente_en_el_bcra, que no tiene "
    "subclases ni arista subclase_de con Sujeto_entidad_financiera, de modo que la herencia del rol ya no "
    "desciende a Sujeto_caja_de_credito y la regla 3 deja de hacer falta. La anidación EF ⊆ titulares sigue sin "
    "ser estricta en el texto (ccbcra::1.1), pero el catálogo r2 no la afirma")


# ------------------------------------------------------------------------- #
# Derivación                                                                  #
# ------------------------------------------------------------------------- #
def _corto(sid: str) -> str:
    return sid[len("Sujeto_"):]


def derivar() -> dict:
    if sha256_archivo(CAT_V3) != CAT_V3_SHA256:
        raise FrenoDerivacion("candado: catalogo_sujetos_v3.json no es el de C1 (9a2522e41e10…)")
    v3 = json.loads(CAT_V3.read_text(encoding="utf-8"))
    cat = copy.deepcopy(v3)
    cat["version"] = "r2"
    cat["version_esquema_clases"] = "3.1"
    por_id = {s["id"]: s for s in cat["sujetos"]}
    fuentes = cat["fuentes"]
    fuentes["catalogo_v3"] = {"ruta": _rel(CAT_V3), "objeto": "catálogo base de la derivación",
                              "sha256": CAT_V3_SHA256}
    fuentes["enmienda_l_esq_r2"] = {"ruta": ENMIENDA_RUTA, "objeto": "§7.3", "sha256": sha256_enmienda_firmada()}
    fuentes["derivacion_r2"] = {"ruta": _rel(Path(__file__)), "objeto":
                                "decisión de derivación declarada: los ids nuevos llevan disjunta_con [] (ninguna "
                                "disyunción anclada) y van al final de los vigentes"}
    n_op = 0

    def op(registro: dict) -> str:
        nonlocal n_op
        n_op += 1
        clave = f"r2_op_{n_op:02d}"
        fuentes[clave] = {"objeto": "operación de la derivación r2", **registro}
        return clave

    nuevas = altas()
    ids_nuevos = [a["id"] for a in nuevas]
    if set(ids_nuevos) & set(por_id):
        raise FrenoDerivacion(f"alta de un id existente: {sorted(set(ids_nuevos) & set(por_id))}")
    padres_validos = set(por_id) | set(ids_nuevos)

    # 1. Altas, en el orden declarado, al final de los vigentes.
    entradas_nuevas = []
    for a in nuevas:
        if a["padre"] not in padres_validos:
            raise FrenoDerivacion(f"{a['id']}: padre {a['padre']} fuera del catálogo")
        clave_op = op({"tipo": "alta", "id": a["id"], "decision": f"{DECISION}; {a['bkl']}",
                       **a.get("op_extra", {})})
        proc = {"id": clave_op, "nivel": clave_op, "grupo_bloque": clave_op, "rol_por_to": clave_op,
                "estado": clave_op, "disjunta_con": "derivacion_r2"}
        if set(a["fuentes"]) != {"label", "definicion", "padre"} | ({"alias"} if a["alias"] else set()):
            raise FrenoDerivacion(f"{a['id']}: campos sin ancla ni NO ENCONTRADO declarados")
        for campo, fuente in a["fuentes"].items():
            clave = f"r2_ancla_{_corto(a['id'])}_{campo}"
            fuentes[clave] = fuente
            proc[campo] = clave
        if not a["alias"]:
            proc["alias"] = clave_op  # sin alias: el valor [] lo fija la operación de alta
        proc["provenance_esqueleto"] = proc["label"] if a["fuentes"]["label"]["objeto"] != NO_ENCONTRADO else clave_op
        entradas_nuevas.append({
            "id": a["id"], "nivel": a["nivel"], "label": a["label"], "alias": list(a["alias"]),
            "definicion": a["definicion"], "padre": a["padre"], "instancia_de": None, "parte_de": None,
            "disjunta_con": [], "padre_inferido": None, "provenance_esqueleto": dict(a["provenance_esqueleto"]),
            "grupo_bloque": a["grupo_bloque"], "rol": None, "rol_por_to": [], "marca_revision": None,
            "estado": {"valor": "vigente", "alta": f"{ALTA_R2}; {a['bkl']}"}, "procedencia": proc})
    ultimo_vigente = max(i for i, s in enumerate(cat["sujetos"]) if s["estado"]["valor"] == "vigente")
    cat["sujetos"][ultimo_vigente + 1:ultimo_vigente + 1] = entradas_nuevas
    por_id = {s["id"]: s for s in cat["sujetos"]}

    # 2. Cambios de alias (BKL-0028).
    for sid, salen, destino in CAMBIOS_ALIAS:
        s = por_id[sid]
        faltan = [x for x in salen if x not in s["alias"]]
        if faltan:
            raise FrenoDerivacion(f"{sid}: alias a quitar ausentes: {faltan}")
        antes = list(s["alias"])
        s["alias"] = [x for x in s["alias"] if x not in salen]
        d = por_id[destino]
        recibidos = [x for x in salen if x == d["label"] or x in d["alias"]]
        if recibidos != list(salen):
            raise FrenoDerivacion(f"{destino}: no recibe todos los alias de {sid} (label o alias)")
        s["procedencia"]["alias"] = op({"tipo": "cambio_alias", "id": sid, "antes": antes, "despues": s["alias"],
                                        "destino": destino, "decision": f"{DECISION}; BKL-0028"})

    # 3. Cambio de miembro del rol de convca (BKL-0029).
    r = por_id[ROL_CONVCA]["rol"]
    if r["miembros"] != MIEMBRO_CONVCA_ANTES or CAMPO_RESIDUO_QUE_SALE not in (r["residuo_declarado"] or {}):
        raise FrenoDerivacion("convca: el rol no está en el estado v3 esperado")
    residuo_antes = copy.deepcopy(r["residuo_declarado"])
    r["miembros"] = list(MIEMBRO_CONVCA_DESPUES)
    r["residuo_declarado"] = {k: v for k, v in r["residuo_declarado"].items() if k != CAMPO_RESIDUO_QUE_SALE}
    clave = op({"tipo": "cambio_miembro_rol", "id": ROL_CONVCA,
                "antes": {"miembros": MIEMBRO_CONVCA_ANTES,
                          CAMPO_RESIDUO_QUE_SALE: residuo_antes[CAMPO_RESIDUO_QUE_SALE]},
                "despues": {"miembros": MIEMBRO_CONVCA_DESPUES, CAMPO_RESIDUO_QUE_SALE: "(campo retirado)"},
                "anclas": [ancla("convca::1.1", "entre sus cuentas corrientes abiertas en el Banco Central"),
                           ancla("convca::2.1.3", "Los titulares de cuentas corrientes en este Banco Central")],
                "decision": f"{DECISION}; BKL-0029"})
    por_id[ROL_CONVCA]["procedencia"]["rol.miembros"] = clave

    # 4. Residuo de convca al estado r2: remedio y anidacion_no_estricta.
    res = r["residuo_declarado"]
    an = res.get("anidacion_no_estricta") or {}
    if "remedio" not in res or CAMPO_ANIDACION_QUE_SALE not in an:
        raise FrenoDerivacion("convca: el residuo no tiene remedio o anidacion_no_estricta en su forma v3")
    antes_res = {"remedio": res["remedio"], "anidacion_no_estricta": copy.deepcopy(an)}
    an_r2 = {k: v for k, v in an.items() if k != CAMPO_ANIDACION_QUE_SALE}
    an_r2["estado_r2"] = ESTADO_R2_ANIDACION
    res["anidacion_no_estricta"] = an_r2
    res["remedio"] = REMEDIO_R2
    clave = op({"tipo": "cambio_residuo_rol", "id": ROL_CONVCA, "antes": antes_res,
                "despues": {"remedio": REMEDIO_R2, "anidacion_no_estricta": copy.deepcopy(an_r2)},
                "decision": f"{DECISION}; BKL-0029; {DECISION_RESIDUO}"})
    por_id[ROL_CONVCA]["procedencia"]["rol.residuo_declarado"] = clave
    return cat


def serializar(cat: dict) -> str:
    return json.dumps(cat, ensure_ascii=False, indent=1) + "\n"


def main() -> int:
    texto = serializar(derivar())
    SALIDA.write_text(texto, encoding="utf-8")
    cat = json.loads(texto)
    vig = [s for s in cat["sujetos"] if s["estado"]["valor"] == "vigente"]
    ops = [k for k in cat["fuentes"] if k.startswith("r2_op_")]
    print(f"{_rel(SALIDA)}  sha256 {hashlib.sha256(texto.encode('utf-8')).hexdigest()}")
    print(f"vigentes {len(vig)} · lápidas {sum(1 for s in cat['sujetos'] if s['estado']['valor'] == 'lapida')} · "
          f"operaciones {len(ops)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
