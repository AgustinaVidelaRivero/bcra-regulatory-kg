"""
construir_catalogo_v3.py — U-CAT-UNICO C1: catálogo de sujetos en una sola
fuente, con el contenido v3.

Construye data/experiment/catalogo_unico/catalogo_sujetos_v3.json POR PROGRAMA
desde los artefactos que hoy contienen el catálogo, sin editar ninguno:

  - el bloque de catálogo del prompt v3 (prompt_v3_b54.BLOQUE_CATALOGO_V3, 102
    ids; prefijo sha256 35e88c2dd0a2…) y los objetos de los que se construye
    (DEFINICIONES_V3, ADICIONES_V3, ROLES_V3, MAPEO_CLASE_V3, RETIROS_V3,
    MARCADOS_REVISION_R2, HUECOS_SIN_ROL, ROL_POR_TO_V3, sujetos_catalogo_v3());
  - data/experiment/esq_v3_miembros/esquema_v3_clases.json (101 ids; sha256
    dad88cc9…): padres, disjunciones, provenance de esqueleto, miembros de rol,
    causas sin miembro, residuo de convca y textos de excepciones_s15;
  - data/experiment/b54_catalogo_v3/catalogo_sujetos_v3.md: lápidas de los
    cinco retiros (:41-55) y marcas de revisión (:57-63).

Diferencia 6/5 (L-ESQ-R2 §7.3, decisión 2 del mandato): los seis ids que solo
están en el bloque (adiciones de B5.4 F1.4 salvo CEC) son vigentes; los cinco
que solo están en el JSON (retiros de F1.5) quedan como lápidas no vigentes.

ESQUEMA DEL JSON (formato catalogo_sujetos_unico/1)
  Nivel superior: formato, version, version_esquema_clases, fuentes,
  presentacion.grupos_bloque, politicas (excepciones_s15, huecos_sin_rol),
  sujetos.
  `sujetos`: vigentes en el orden del enum del tool schema, después lápidas.
  Por id: id, nivel (clase|instancia|rol), label, alias, definicion, padre
  (subclase de), instancia_de, parte_de, disjunta_con, padre_inferido,
  provenance_esqueleto, grupo_bloque, rol (miembros, sin_miembro_adjudicable,
  residuo_declarado, miembros_ids_mensaje, miembros_labels_mensaje),
  rol_por_to (archivos de TO de los que el id es sujeto por defecto),
  marca_revision, estado (vigente: alta; lápida: evidencia, fecha, laudo,
  destino, registro) y procedencia (campo → clave de `fuentes`).

Candados: si el prefijo v3 no reproduce 35e88c2dd0a2… o el JSON v3 no es
dad88cc9…, se frena. También se frena si bloque y JSON difieren en label,
alias, nivel o TO de algún id común, o si la diferencia de ids no es la 6/5.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/catalogo_unico/code/construir_catalogo_v3.py
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
from pathlib import Path  # noqa: E402

AQUI = Path(__file__).resolve().parent                 # catalogo_unico/code
CATALOGO_UNICO = AQUI.parent
REPO = AQUI.parents[3]
B54_CODE = REPO / "data" / "experiment" / "b54_catalogo_v3" / "code"
if str(B54_CODE) not in sys.path:
    sys.path.insert(0, str(B54_CODE))

import prompt_v3_b54 as v3          # noqa: E402 — módulo sellado, solo import
import prompt_congelado as pcg      # noqa: E402 — en path vía prompt_v3_b54

SALIDA = CATALOGO_UNICO / "catalogo_sujetos_v3.json"
NOMBRE_SALIDA = SALIDA.name

RUTA_PROMPT_V3 = B54_CODE / "prompt_v3_b54.py"
RUTA_CONGELADO = REPO / "data" / "experiment" / "esq" / "code" / "prompt_congelado.py"
RUTA_SCHEMA_V2 = REPO / "data" / "experiment" / "grafo_v2" / "code" / "schema.py"
RUTA_ESQ_V3 = REPO / "data" / "experiment" / "esq_v3_miembros" / "esquema_v3_clases.json"
RUTA_CAT_MD = REPO / "data" / "experiment" / "b54_catalogo_v3" / "catalogo_sujetos_v3.md"
RUTA_LAUDO_F1 = REPO / "docs" / "laudo_B5.4_fase1_catalogo.md"

PREFIJO_SHA256_V3 = "35e88c2dd0a2920302c29005b08ab9689405606d4bd5fcf8fb7ce807b1a3c512"
ESQ_V3_SHA256 = "dad88cc92afc53e922989cad84eb68b2ef142b66c221f2a566e7fb5da1bcfd36"

FORMATO = "catalogo_sujetos_unico/1"
CEC = "Sujeto_camara_electronica_de_compensacion"

# Provenance de esqueleto de las seis adiciones que no estaban en el JSON v3:
# el patrón de la CEC en esquema_v3_clases.json, con el artefacto donde la
# adición entra al esquema de clases (decisión de construcción declarada).
LOCATION_ADICION = "adición del catálogo v3 (laudo B5.4 fase 1)"

ALTA_CONGELADO = ("catálogo del prefijo congelado (data/experiment/esq/code/prompt_congelado.py, "
                  "SUJETOS_CATALOGO; laudo de esquema congelado, commit 2593d4d)")
ALTA_F14 = "docs/laudo_B5.4_fase1_catalogo.md §F1.4 (commit dea56ba, 05/09/2026)"
ALTA_F12 = "docs/laudo_B5.4_fase1_catalogo.md §F1.2 (commit dea56ba, 05/09/2026)"
NOTA_RENAME = {
    "Sujeto_entidad_originante_de_transferencia":
        "id renombrado desde Sujeto_entidad_originante por docs/laudo_B5.4_cierre_catalogo.md "
        "H1(a) (06/09/2026); registro en data/experiment/b54_catalogo_v3/catalogo_sujetos_v3.md:157-160",
}
LAUDO_F15 = "docs/laudo_B5.4_fase1_catalogo.md §F1.5 (commit dea56ba)"


class FrenoConstruccion(RuntimeError):
    """Una precondición de la construcción no se cumple: se frena."""


def sha256_archivo(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _rel(p: Path) -> str:
    return str(p.resolve().relative_to(REPO))


# ------------------------------------------------------------------------- #
# Lectores de los artefactos                                                  #
# ------------------------------------------------------------------------- #
def parsear_bloque(texto: str) -> tuple[list[str], dict[str, dict], list[str]]:
    """Bloque de catálogo → (orden de ids, id → campos, encabezados).

    Línea de id: `id — label[ (alias: a, b)][ [instancia]][ [rol del TO x]]`;
    línea de definición: `  def: texto`; encabezado: `## …`."""
    orden: list[str] = []
    campos: dict[str, dict] = {}
    grupos: list[str] = []
    grupo = None
    ultimo = None
    for linea in texto.rstrip("\n").split("\n"):
        if linea.startswith("## "):
            grupo = linea
            grupos.append(linea)
            continue
        if linea.startswith("  def: "):
            if ultimo is None or campos[ultimo]["definicion"] is not None:
                raise FrenoConstruccion(f"línea def: sin id previo o duplicada: {linea[:60]!r}")
            campos[ultimo]["definicion"] = linea[len("  def: "):]
            continue
        if not (linea.startswith("Sujeto_") and " — " in linea):
            raise FrenoConstruccion(f"línea del bloque no reconocida: {linea[:80]!r}")
        sid, resto = linea.split(" — ", 1)
        if sid in campos:
            raise FrenoConstruccion(f"id duplicado en el bloque: {sid}")
        to = None
        m = re.search(r" \[rol del TO ([^\]]+)\]$", resto)
        if m:
            to, resto = m.group(1), resto[:m.start()]
        instancia = resto.endswith(" [instancia]")
        if instancia:
            resto = resto[:-len(" [instancia]")]
        alias: list[str] = []
        m = re.search(r" \(alias: ([^()]+)\)$", resto)
        if m:
            alias, resto = m.group(1).split(", "), resto[:m.start()]
        campos[sid] = {"label": resto, "alias": alias,
                       "nivel": "rol" if to else ("instancia" if instancia else "clase"),
                       "to": to, "grupo": grupo, "definicion": None}
        orden.append(sid)
        ultimo = sid
    return orden, campos, grupos


def parsear_lapidas(md: str) -> dict:
    """catalogo_sujetos_v3.md, sección «Retiros (laudo F1.5) — LÁPIDAS»:
    fecha y destino del párrafo y evidencia por id de la tabla, con su línea."""
    lineas = md.split("\n")
    ini = next(i for i, l in enumerate(lineas) if l.startswith("## Retiros (laudo F1.5)"))
    fin = next(i for i in range(ini + 1, len(lineas)) if lineas[i].startswith("## "))
    parrafo = " ".join(l.strip() for l in lineas[ini + 1:fin] if l.strip() and not l.startswith("|"))
    m = re.search(r"el (\d{2})/(\d{2})/(\d{4}) por el laudo", parrafo)
    if not m:
        raise FrenoConstruccion("lápidas: no se encontró la fecha del retiro en catalogo_sujetos_v3.md")
    fecha = f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
    m = re.search(r"Destino: ([^.]+)\.", parrafo)
    if not m:
        raise FrenoConstruccion("lápidas: no se encontró el destino en catalogo_sujetos_v3.md")
    destino = m.group(1)
    filas = {}
    for i in range(ini + 1, fin):
        m = re.match(r"^\| `(Sujeto_[a-z0-9_]+)` \| (.+) \|$", lineas[i])
        if m:
            filas[m.group(1)] = {"evidencia": m.group(2), "linea": i + 1}
    return {"fecha": fecha, "destino": destino, "filas": filas}


def parsear_marcas(md: str) -> dict:
    """catalogo_sujetos_v3.md, sección «Mantenidos con marca de revisión en
    r2»: una viñeta por id, con continuación indentada."""
    lineas = md.split("\n")
    ini = next(i for i, l in enumerate(lineas) if l.startswith("## Mantenidos con marca de revisión"))
    fin = next(i for i in range(ini + 1, len(lineas)) if lineas[i].startswith("## "))
    out: dict[str, dict] = {}
    actual = None
    for i in range(ini + 1, fin):
        l = lineas[i]
        m = re.match(r"^- `(Sujeto_[a-z0-9_]+)` — (.*)$", l)
        if m:
            actual = m.group(1)
            out[actual] = {"texto": m.group(2), "desde": i + 1, "hasta": i + 1}
        elif actual and l.startswith("  ") and l.strip():
            out[actual]["texto"] += " " + l.strip()
            out[actual]["hasta"] = i + 1
        elif not l.strip():
            actual = None
    for d in out.values():
        m = re.search(r"\*\*(REVISAR EN r2)\.\*\*$", d["texto"])
        if not m:
            raise FrenoConstruccion("marca de revisión sin «REVISAR EN r2» en catalogo_sujetos_v3.md")
        d["marca"] = m.group(1)
        d["evidencia"] = d["texto"][:m.start()].rstrip()
    return out


# ------------------------------------------------------------------------- #
# Construcción                                                                #
# ------------------------------------------------------------------------- #
def construir() -> dict:
    if v3.PREFIJO_SHA256_V3 != PREFIJO_SHA256_V3:
        raise FrenoConstruccion(f"candado: prefijo v3 {v3.PREFIJO_SHA256_V3[:12]}… ≠ 35e88c2dd0a2…")
    if sha256_archivo(RUTA_ESQ_V3) != ESQ_V3_SHA256:
        raise FrenoConstruccion("candado: esquema_v3_clases.json no es el sellado dad88cc9…")

    esq = json.loads(RUTA_ESQ_V3.read_text(encoding="utf-8"))
    J = {e["id"]: e for e in esq["clases"]}
    J.update({r["id"]: r for r in esq["roles"]})
    md = RUTA_CAT_MD.read_text(encoding="utf-8")
    lapidas = parsear_lapidas(md)
    marcas = parsear_marcas(md)

    orden_b, B, grupos = parsear_bloque(v3.BLOQUE_CATALOGO_V3)
    _, B_cong, _ = parsear_bloque(v3.BLOQUE_CATALOGO_CONGELADO)
    enum = v3.sujetos_catalogo_v3()
    if len(enum) != len(set(enum)) or set(enum) != set(B):
        raise FrenoConstruccion("el enum v3 no coincide con los ids del bloque v3")
    if orden_b != [s for g in grupos for s in enum if B[s]["grupo"] == g]:
        raise FrenoConstruccion("el bloque v3 no es el enum agrupado por encabezado")

    adiciones = {a["id"]: a for a in v3.ADICIONES_V3}
    solo_bloque = set(enum) - set(J)
    solo_json = set(J) - set(enum)
    if solo_bloque != set(adiciones) - {CEC}:
        raise FrenoConstruccion(f"ids solo en el bloque ≠ adiciones F1.4 sin CEC: {sorted(solo_bloque)}")
    if solo_json != set(v3.RETIROS_V3):
        raise FrenoConstruccion(f"ids solo en el JSON ≠ retiros F1.5: {sorted(solo_json)}")
    if set(lapidas["filas"]) != set(v3.RETIROS_V3):
        raise FrenoConstruccion("la tabla de lápidas no lista exactamente los cinco retiros")
    if set(marcas) != set(v3.MARCADOS_REVISION_R2):
        raise FrenoConstruccion("las marcas de revisión del .md no coinciden con MARCADOS_REVISION_R2")

    roles_a2 = {f"{to}.pdf": (label, list(miembros)) for to, label, miembros in v3.ROLES_V3}
    dev = v3.prompt_e1.ROL_POR_TO
    mapeo = {f"{to}.pdf": list(ids) for to, ids in v3.MAPEO_CLASE_V3.items()}
    congelado = set(pcg.SUJETOS_CATALOGO)

    sujetos: list[dict] = []
    for sid in enum:
        b = B[sid]
        j = J.get(sid)
        proc: dict[str, str] = {"id": "enum_v3", "nivel": "bloque_v3", "label": "bloque_v3",
                                "alias": "bloque_v3", "grupo_bloque": "bloque_v3"}
        if j is not None:
            for campo in ("label", "nivel"):
                if j[campo] != b[campo]:
                    raise FrenoConstruccion(f"{sid}: {campo} del bloque ≠ JSON ({b[campo]!r} / {j[campo]!r})")
            if (j.get("alias") or []) != b["alias"]:
                raise FrenoConstruccion(f"{sid}: alias del bloque ≠ JSON")
            if b["nivel"] == "rol" and j.get("to") != b["to"]:
                raise FrenoConstruccion(f"{sid}: TO del bloque ≠ JSON")

        e: dict = {"id": sid, "nivel": b["nivel"], "label": b["label"], "alias": list(b["alias"]),
                   "definicion": b["definicion"], "padre": None, "instancia_de": None,
                   "parte_de": None, "disjunta_con": None, "padre_inferido": None,
                   "provenance_esqueleto": None, "grupo_bloque": b["grupo"], "rol": None,
                   "rol_por_to": [], "marca_revision": None, "estado": None}

        if sid in v3.DEFINICIONES_V3:
            if b["definicion"] != v3.DEFINICIONES_V3[sid]:
                raise FrenoConstruccion(f"{sid}: def del bloque ≠ DEFINICIONES_V3")
            proc["definicion"] = "definiciones_v3"
        elif sid in adiciones and adiciones[sid]["def"] is not None:
            if b["definicion"] != adiciones[sid]["def"]:
                raise FrenoConstruccion(f"{sid}: def del bloque ≠ ADICIONES_V3")
            proc["definicion"] = "adiciones_v3"
        elif b["definicion"] is not None:
            raise FrenoConstruccion(f"{sid}: def en el bloque sin fuente declarada")
        else:
            proc["definicion"] = "bloque_v3"

        if b["nivel"] == "rol":
            to = b["to"]
            if to in dev:
                msg = dev[to]
                fuente_msg = "rol_por_to_dev"
            elif to in roles_a2:
                label_a2, miembros_a2 = roles_a2[to]
                msg = {"rol_id": sid, "label": label_a2, "miembros_ids": [], "miembros_labels": miembros_a2}
                fuente_msg = "roles_v3"
            else:
                raise FrenoConstruccion(f"{sid}: rol sin TO en ROL_POR_TO")
            if v3.ROL_POR_TO_V3[to] != msg or msg["rol_id"] != sid or msg["label"] != b["label"]:
                raise FrenoConstruccion(f"{sid}: entrada de ROL_POR_TO_V3 ≠ fuente {fuente_msg}")
            e["rol"] = {"miembros": list(j["miembros"]),
                        "sin_miembro_adjudicable": j.get("sin_miembro_adjudicable"),
                        "residuo_declarado": j.get("residuo_declarado"),
                        "miembros_ids_mensaje": list(msg["miembros_ids"]),
                        "miembros_labels_mensaje": list(msg["miembros_labels"])}
            e["rol_por_to"] = [to]
            e["provenance_esqueleto"] = dict(j["provenance"])
            proc.update({"rol.miembros": "esquema_v3_clases", "rol.sin_miembro_adjudicable": "esquema_v3_clases",
                         "rol.residuo_declarado": "esquema_v3_clases",
                         "rol.miembros_ids_mensaje": "rol_por_to_v3",
                         "rol.miembros_labels_mensaje": fuente_msg, "rol_por_to": "bloque_v3",
                         "provenance_esqueleto": "esquema_v3_clases"})
        else:
            e["rol_por_to"] = [to for to, ids in mapeo.items() if sid in ids]
            proc["rol_por_to"] = "mapeo_clase_v3"
            if j is not None:
                if b["nivel"] == "clase":
                    e["padre"] = j["padre"]
                    e["disjunta_con"] = list(j["disjunta_con"])
                    e["padre_inferido"] = j.get("padre_inferido")
                    proc.update({"padre": "esquema_v3_clases", "disjunta_con": "esquema_v3_clases",
                                 "padre_inferido": "esquema_v3_clases"})
                else:
                    e["instancia_de"] = j["instancia_de"]
                    e["parte_de"] = j.get("parte_de")
                    proc.update({"instancia_de": "esquema_v3_clases", "parte_de": "esquema_v3_clases"})
                e["provenance_esqueleto"] = dict(j["provenance"])
                proc["provenance_esqueleto"] = "esquema_v3_clases"
            else:
                ad = adiciones[sid]
                if ad["nivel"] != b["nivel"]:
                    raise FrenoConstruccion(f"{sid}: nivel de ADICIONES_V3 ≠ bloque")
                if b["nivel"] == "clase":
                    e["padre"] = ad["padre"]
                    e["disjunta_con"] = []
                    proc.update({"padre": "adiciones_v3", "disjunta_con": "construccion_c1"})
                else:
                    e["instancia_de"] = ad["padre"]
                    proc["instancia_de"] = "adiciones_v3"
                e["provenance_esqueleto"] = {"source_doc": NOMBRE_SALIDA, "location": LOCATION_ADICION}
                proc["provenance_esqueleto"] = "construccion_c1"

        if sid in marcas:
            mk = marcas[sid]
            e["marca_revision"] = {
                "marca": mk["marca"], "evidencia": mk["evidencia"], "laudo": LAUDO_F15,
                "registro": f"{_rel(RUTA_CAT_MD)}:{mk['desde']}-{mk['hasta']}"}
            proc["marca_revision"] = "marcas_md"

        if sid in congelado:
            alta = ALTA_CONGELADO
        elif sid in adiciones:
            alta = ALTA_F14 + ("; " + NOTA_RENAME[sid] if sid in NOTA_RENAME else "")
        elif b["nivel"] == "rol" and b["to"] in roles_a2:
            alta = ALTA_F12
        else:
            raise FrenoConstruccion(f"{sid}: vigente sin alta identificable")
        e["estado"] = {"valor": "vigente", "alta": alta}
        proc["estado"] = "enum_v3"
        e["procedencia"] = proc
        sujetos.append(e)

    for sid in v3.RETIROS_V3:
        j = J[sid]
        bc = B_cong.get(sid)
        if bc is None or bc["label"] != j["label"] or bc["alias"] != (j.get("alias") or []) or bc["nivel"] != j["nivel"]:
            raise FrenoConstruccion(f"lápida {sid}: bloque congelado ≠ JSON v3")
        fila = lapidas["filas"][sid]
        e = {"id": sid, "nivel": j["nivel"], "label": j["label"], "alias": list(j.get("alias") or []),
             "definicion": None, "padre": j.get("padre"), "instancia_de": j.get("instancia_de"),
             "parte_de": j.get("parte_de"),
             "disjunta_con": list(j["disjunta_con"]) if "disjunta_con" in j else None,
             "padre_inferido": j.get("padre_inferido"), "provenance_esqueleto": dict(j["provenance"]),
             "grupo_bloque": bc["grupo"], "rol": None, "rol_por_to": [], "marca_revision": None,
             "estado": {"valor": "lapida", "evidencia": fila["evidencia"], "fecha": lapidas["fecha"],
                        "laudo": LAUDO_F15, "destino": lapidas["destino"],
                        "registro": f"{_rel(RUTA_CAT_MD)}:{fila['linea']}"},
             "procedencia": {"id": "retiros_v3", "nivel": "esquema_v3_clases", "label": "esquema_v3_clases",
                             "alias": "esquema_v3_clases", "padre": "esquema_v3_clases",
                             "instancia_de": "esquema_v3_clases", "disjunta_con": "esquema_v3_clases",
                             "provenance_esqueleto": "esquema_v3_clases", "grupo_bloque": "bloque_congelado",
                             "estado": "lapidas_md"}}
        sujetos.append(e)

    exc = esq["excepciones_s15"]
    fuentes = {
        "bloque_v3": {"ruta": _rel(RUTA_PROMPT_V3), "objeto": "BLOQUE_CATALOGO_V3",
                      "sha256": sha256_archivo(RUTA_PROMPT_V3), "prefijo_sha256": v3.PREFIJO_SHA256_V3},
        "enum_v3": {"ruta": _rel(RUTA_PROMPT_V3), "objeto": "sujetos_catalogo_v3()",
                    "sha256": sha256_archivo(RUTA_PROMPT_V3)},
        "definiciones_v3": {"ruta": _rel(RUTA_PROMPT_V3), "objeto": "DEFINICIONES_V3",
                            "sha256": sha256_archivo(RUTA_PROMPT_V3)},
        "adiciones_v3": {"ruta": _rel(RUTA_PROMPT_V3), "objeto": "ADICIONES_V3",
                         "sha256": sha256_archivo(RUTA_PROMPT_V3)},
        "roles_v3": {"ruta": _rel(RUTA_PROMPT_V3), "objeto": "ROLES_V3",
                     "sha256": sha256_archivo(RUTA_PROMPT_V3)},
        "mapeo_clase_v3": {"ruta": _rel(RUTA_PROMPT_V3), "objeto": "MAPEO_CLASE_V3",
                           "sha256": sha256_archivo(RUTA_PROMPT_V3)},
        "rol_por_to_v3": {"ruta": _rel(RUTA_PROMPT_V3), "objeto": "ROL_POR_TO_V3",
                          "sha256": sha256_archivo(RUTA_PROMPT_V3)},
        "retiros_v3": {"ruta": _rel(RUTA_PROMPT_V3), "objeto": "RETIROS_V3",
                       "sha256": sha256_archivo(RUTA_PROMPT_V3)},
        "huecos_v3": {"ruta": _rel(RUTA_PROMPT_V3), "objeto": "HUECOS_SIN_ROL",
                      "sha256": sha256_archivo(RUTA_PROMPT_V3)},
        "rol_por_to_dev": {"ruta": _rel(RUTA_SCHEMA_V2), "objeto": "ROL_POR_TO (vía prompt_e1)",
                           "sha256": sha256_archivo(RUTA_SCHEMA_V2)},
        "bloque_congelado": {"ruta": _rel(RUTA_CONGELADO), "objeto": "PREFIJO_SISTEMA_CONGELADO",
                             "sha256": sha256_archivo(RUTA_CONGELADO)},
        "esquema_v3_clases": {"ruta": _rel(RUTA_ESQ_V3), "objeto": "clases, roles, excepciones_s15",
                              "sha256": sha256_archivo(RUTA_ESQ_V3)},
        "lapidas_md": {"ruta": _rel(RUTA_CAT_MD), "objeto": "Retiros (laudo F1.5) — LÁPIDAS",
                       "sha256": sha256_archivo(RUTA_CAT_MD)},
        "marcas_md": {"ruta": _rel(RUTA_CAT_MD), "objeto": "Mantenidos con marca de revisión en r2",
                      "sha256": sha256_archivo(RUTA_CAT_MD)},
        "laudo_b54_f1": {"ruta": _rel(RUTA_LAUDO_F1), "objeto": "§F1.2, §F1.4, §F1.5",
                         "sha256": sha256_archivo(RUTA_LAUDO_F1)},
        "construccion_c1": {"ruta": _rel(Path(__file__)), "objeto":
                            "decisión de construcción declarada: disjunta_con [] y provenance de esqueleto "
                            "con el patrón de la CEC para las adiciones que no estaban en el JSON v3"},
    }
    return {
        "formato": FORMATO,
        "version": "v3",
        "version_esquema_clases": esq["version"],
        "fuentes": fuentes,
        "presentacion": {"grupos_bloque": grupos},
        "politicas": {
            "excepciones_s15": {"enunciado": exc["enunciado"], "remedios": dict(exc["remedios"])},
            "huecos_sin_rol": [f"{to}.pdf" for to in v3.HUECOS_SIN_ROL],
            "procedencia": {"excepciones_s15": "esquema_v3_clases", "huecos_sin_rol": "huecos_v3"},
        },
        "sujetos": sujetos,
    }


def serializar(cat: dict) -> str:
    return json.dumps(cat, ensure_ascii=False, indent=1) + "\n"


def main() -> int:
    texto = serializar(construir())
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(texto, encoding="utf-8")
    cat = json.loads(texto)
    vig = [s for s in cat["sujetos"] if s["estado"]["valor"] == "vigente"]
    lap = [s for s in cat["sujetos"] if s["estado"]["valor"] == "lapida"]
    niveles = {n: sum(1 for s in vig if s["nivel"] == n) for n in ("clase", "instancia", "rol")}
    print(f"{_rel(SALIDA)}  sha256 {hashlib.sha256(texto.encode('utf-8')).hexdigest()}")
    print(f"vigentes {len(vig)} {niveles} · lápidas {len(lap)} · definiciones "
          f"{sum(1 for s in vig if s['definicion'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
