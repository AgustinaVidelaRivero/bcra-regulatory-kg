"""
candidatos_miembros_v3.py — U-ESQ-V3 fase 1: CANDIDATOS mecánicos de miembros
para los 30 roles de alcance nuevos del catálogo v3.

QUÉ HACE Y QUÉ NO. Propone; no adjudica. La entrada de cada rol es la lista
`miembros_labels` que el propio módulo sellado ya trae (ROLES_V3, adjudicada
por U-B5.4 fase 1 con su pasaje verbatim); la salida es, por cada uno de esos
colectivos, el id del catálogo v3 que un matcheo por REGLAS VISIBLES propone,
o NINGUNO cuando el colectivo no tiene id en el catálogo. Cero LLM, USD 0.

CRITERIO DE ADJUDICACIÓN (fijado por el mandato, no se re-decide acá): el
miembro de un rol es la clase que el pasaje NOMBRA, a la granularidad en que
la nombra — ni expandida a sus subclases ni colapsada a su clase madre. La
navegación por subclase_de hace el resto. Un pasaje que enumera tres
colectivos da tres miembros. De ahí que el matcheo NUNCA suba al padre: si
«Cajas de valores» no tiene id, la salida es NINGUNO — jamás
Sujeto_entidad_bursatil, que sería colapsar a la madre.

REGLAS DE MATCHEO, en orden de aplicación (la primera que da resultado gana;
la regla que produjo el candidato viaja en la salida). El «núcleo» de un
texto es lo que queda al quitarle el paréntesis final y el tramo posterior a
la primera coma, y se calcula tanto del colectivo como del label del catálogo
(«Cámaras electrónicas de compensación (CEC)» → «Cámaras electrónicas de
compensación»):

  R1 label_exacto     clave(colectivo) == clave(label del catálogo)
  R2 alias_exacto     clave(colectivo) == clave(algún alias)
  R3 nucleo           el núcleo del colectivo == el label, su núcleo o un alias
  R4 sigla            la sigla entre paréntesis del colectivo (PSP, CEC, …)
                      matchea un alias, el id, o el acrónimo de iniciales del
                      label (≥ 3 letras)
  R5 madre_APLANA     el label del catálogo es el PREFIJO en palabras del
                      colectivo, cubriendo ≥ 2 palabras («Entidades
                      financieras D-SIB» → «Entidades financieras»)

R5 NO produce un candidato equivalente: produce el PADRE del colectivo que el
pasaje nombra, que es exactamente lo que el criterio prohíbe. Su salida se
etiqueta y la fila se marca `APLANA_A_LA_MADRE`, para que la adjudicación
elija a la vista entre aceptar el aplanamiento declarándolo o dejar el
colectivo sin id. Nunca se presenta como match limpio.

La columna `relacion` dice, mecánicamente, qué tan literal es el candidato:
  identico            el colectivo y el label coinciden (R1/R2/R4)
  recorte_declarado   coinciden sus núcleos; el colectivo trae una aclaración
                      que el candidato no porta (R3) — puede ser inocua (una
                      sección, la ley que define al sujeto) o restrictiva
                      («filiales del país»): distinguirlas es juicio, no
                      matcheo, y por eso la aclaración queda a la vista
  mas_amplio          el candidato cubre MÁS que el colectivo (R5)

Todo lo demás: NINGUNO, con el colectivo textual para que la adjudicación lo
vea. El matcheo jamás sube al padre por su cuenta fuera de R5, y jamás baja a
las subclases. Un candidato de nivel `instancia` se marca (los 17 miembros
vigentes son los 17 de nivel `clase`: el tipo del miembro es decisión de la
autora).

Uso:  python3 candidatos_miembros_v3.py [--out DIR]
Escribe (por defecto en el directorio de la unidad):
  candidatos_miembros_v3.json         — máquina, con la regla por candidato
  tabla_adjudicacion_miembros_v3.md   — tabla del freno, una fila por rol
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import comun_v3m as C

# --------------------------------------------------------------------------- #
# Citas de los pasajes de alcance: chunk_id por TO, tomadas de la tabla del
# freno 1 de U-B5.4 (gen_tabla_to_rol_f1.py, reconstruida por esta unidad en
# tabla_to_rol_post_f1.md). El texto NO se copia: se lee de e0_dry.
# --------------------------------------------------------------------------- #
CITA_ALCANCE: dict[str, str] = {
    "adrei": "adrei::1.1",
    "autenf": "autenf::1.1::intro",
    "ccbcra": "ccbcra::1.1",
    "convca": "convca::1.1",
    "cryl": "cryl::3.1",
    "ctacor": "ctacor::1.1",
    "depaho": "depaho::1.1.1",
    "efemin": "efemin::4.1",
    "fabcra": "fabcra::S1::chapeau_seccion",
    "icmecma": "icmecma::1.1.1",
    "lavdin": "lavdin::1.1::intro",
    "ordcom": "ordcom::1.5::intro",
    "osapsa": "osapsa::1.1",
    "pagjub": "pagjub::1.1",
    "pfmipyme": "pfmipyme::1.1.1",
    "pimf": "pimf::5.1",
    "ratiofn": "ratiofn::1.1",
    "rdbcra": "rdbcra::1.1.1.1",
    "repefe": "repefe::1.1",
    "retype": "retype::1.1.2",
    "rmrtsd": "rmrtsd::1.1.1",
    "rrci": "rrci::1.2",
    "servco": "servco::1.1",
    "snp_atm": "snp_atm::1.1.1",
    "snp_debin": "snp_debin::2.1",
    "snp_psp": "snp_psp::1.1.2",
    "snp_spd": "snp_spd::S1::chapeau_seccion",
    "snp_tr_nc": "snp_tr_nc::1.2.1",
    "supcon": "supcon::2.2::intro",
    "traval": "traval::1.1::intro",
}


def _nucleo(s: str) -> str:
    """Recorta la aclaración: paréntesis final y tramo tras la primera coma."""
    s = re.sub(r"\s*\([^)]*\)\s*$", "", s).strip()
    s = s.split(",", 1)[0].strip()
    return s


def _siglas(s: str) -> list[str]:
    """Siglas del colectivo: las que van entre paréntesis, y el núcleo mismo
    cuando ES una sigla («PSP (según el servicio)» → núcleo «PSP»)."""
    out = []
    for m in re.finditer(r"\(([^)]*)\)", s):
        for t in re.split(r"[,/;]| y ", m.group(1)):
            t = t.strip()
            if t and t.upper() == t and len(t) <= 8:
                out.append(t)
    nuc = _nucleo(s).strip()
    if nuc and nuc.upper() == nuc and 2 <= len(nuc) <= 8:
        out.append(nuc)
    return out


def pista(colectivo: str, ix: dict[str, dict]) -> dict | None:
    """PISTA para la adjudicación, NO un candidato: la entrada del catálogo
    con mayor solapamiento de palabras con el colectivo. Se emite solo para
    los colectivos que quedaron sin id, y solo por encima de un piso de
    solapamiento. No se propone como miembro: la lee la autora."""
    stop = {"de", "del", "la", "las", "el", "los", "y", "o", "en", "que", "a", "por"}
    toks = {C.singular(t) for t in C.norm(colectivo).split()} - stop
    if not toks:
        return None
    mejor, score = None, 0.0
    for sid, v in ix.items():
        if v["nivel"] not in ("clase", "instancia"):
            continue
        t2 = {C.singular(t) for t in C.norm(_nucleo(v["label"])).split()} - stop
        if not t2:
            continue
        j = len(toks & t2) / len(toks | t2)
        if j > score:
            mejor, score = sid, j
    if mejor is None or score < 0.34:
        return None
    return {"id": mejor, "label": ix[mejor]["label"], "nivel": ix[mejor]["nivel"],
            "solapamiento": round(score, 2)}


def _acronimo(label: str) -> str:
    """Acrónimo de iniciales de las palabras plenas del label (≥ 3 letras)."""
    stop = {"de", "del", "la", "las", "el", "los", "y", "o", "en", "que", "a"}
    ini = [p[0] for p in C.norm(label).split() if p not in stop]
    return "".join(ini) if len(ini) >= 3 else ""


def matchear(colectivo: str, ix: dict[str, dict]) -> tuple[str | None, str, str]:
    """Devuelve (id_candidato | None, regla, relacion). Solo clases e
    instancias: un rol jamás es miembro de otro rol."""
    cand = {k: v for k, v in ix.items() if v["nivel"] in ("clase", "instancia")}
    k_col = C.clave(colectivo)
    k_col_nuc = C.clave(_nucleo(colectivo))

    for sid, v in cand.items():                                   # R1
        if k_col in (C.clave(v["label"]), C.clave(_nucleo(v["label"]))):
            return sid, "R1_label_exacto", "identico"
    for sid, v in cand.items():                                   # R2
        if any(C.clave(a) == k_col for a in v["alias"]):
            return sid, "R2_alias_exacto", "identico"

    if k_col_nuc and k_col_nuc != k_col:                          # R3
        for sid, v in cand.items():
            if k_col_nuc in (C.clave(v["label"]), C.clave(_nucleo(v["label"]))):
                return sid, "R3_nucleo", "recorte_declarado"
        for sid, v in cand.items():
            if any(C.clave(a) == k_col_nuc for a in v["alias"]):
                return sid, "R3_nucleo_alias", "recorte_declarado"

    for sg in _siglas(colectivo):                                 # R4
        k_sg = C.clave(sg)
        for sid, v in cand.items():
            if any(C.clave(a) == k_sg for a in v["alias"]):
                return sid, "R4_sigla", "identico"
            if C.clave(sid.replace("Sujeto_", "").replace("_", " ")) == k_sg:
                return sid, "R4_sigla_id", "identico"
            if _acronimo(_nucleo(v["label"])) == C.norm(sg).replace(" ", ""):
                return sid, "R4_sigla_acronimo", "identico"

    base = k_col_nuc or k_col                                     # R5
    mejor, n_mejor = None, 0
    for sid, v in cand.items():
        for k_lab in {C.clave(v["label"]), C.clave(_nucleo(v["label"]))}:
            n = len(k_lab.split())
            if n >= 2 and (base + " ").startswith(k_lab + " ") and n > n_mejor:
                mejor, n_mejor = sid, n
    if mejor:
        return mejor, "R5_madre_APLANA", "mas_amplio"

    return None, "NINGUNO", "—"


def construir() -> dict:
    v3 = C.cargar_v3()
    ix = C.catalogo_v3_index()
    filas = []
    for to, label_rol, miembros_labels in v3.ROLES_V3:
        cands = []
        for col in miembros_labels:
            sid, regla, relacion = matchear(col, ix)
            cands.append({
                "colectivo": col,
                "candidato_id": sid,
                "regla": regla,
                "relacion": relacion,
                "nivel_candidato": ix[sid]["nivel"] if sid else None,
                "label_candidato": ix[sid]["label"] if sid else None,
                "pista_para_juicio": None if sid else pista(col, ix),
            })
        cita = CITA_ALCANCE[to]
        ch = C.chunk_de(cita)
        sin_id = [c["colectivo"] for c in cands if not c["candidato_id"]]
        instancias = [c["candidato_id"] for c in cands
                      if c["nivel_candidato"] == "instancia"]
        marcas = []
        if len(miembros_labels) > 1:
            marcas.append("MULTI_SUJETO")
        if sin_id:
            marcas.append("SIN_ID_EN_CATALOGO")
        if any(c["relacion"] == "mas_amplio" for c in cands):
            marcas.append("APLANA_A_LA_MADRE")
        if instancias:
            marcas.append("CANDIDATO_INSTANCIA")
        vistos = [c["candidato_id"] for c in cands if c["candidato_id"]]
        if len(vistos) != len(set(vistos)):
            marcas.append("CANDIDATOS_COLAPSAN")
        filas.append({
            "to": to,
            "rol_id": v3.rol_id_de(to),
            "label_rol": label_rol,
            "cita_chunk_id": cita,
            "paginas": ch["paginas"] if ch else None,
            "pasaje": (ch["texto"] if ch else None),
            "titulo_unidad": ch["titulo"] if ch else None,
            "miembros_labels": list(miembros_labels),
            "candidatos": cands,
            "marcas": marcas,
        })
    return {
        "unidad": "U-ESQ-V3",
        "fase": 1,
        "fuente_colectivos": "prompt_v3_b54.ROLES_V3 (módulo SELLADO, solo lectura)",
        "fuente_pasajes": "data/experiment/escalado_prep/e0_dry/<to>/chunks_<to>.json",
        "sello_v3": {"sha256": v3.PREFIJO_SHA256_V3, "hash": v3.PREFIJO_HASH_V3},
        "criterio": ("el miembro de un rol es la clase que el pasaje NOMBRA, a la "
                     "granularidad en que la nombra — ni expandida a subclases ni "
                     "colapsada a la clase madre"),
        "roles": filas,
    }


# --------------------------------------------------------------------------- #
# Render de la tabla del freno (patrón del freno 1 de B5.4: una fila por rol,
# con columna vacía para la marca de la autora).
# --------------------------------------------------------------------------- #

def _corto(s: str, n: int) -> str:
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 1] + "…"


def conteos(d: dict) -> dict:
    cs = [c for r in d["roles"] for c in r["candidatos"]]
    return {
        "roles": len(d["roles"]),
        "colectivos": len(cs),
        "con_candidato": sum(1 for c in cs if c["candidato_id"]),
        "sin_id_en_catalogo": sum(1 for c in cs if not c["candidato_id"]),
        "por_relacion": {k: sum(1 for c in cs if c["relacion"] == k)
                         for k in ("identico", "recorte_declarado", "mas_amplio", "—")},
        "candidatos_instancia": sum(1 for c in cs if c["nivel_candidato"] == "instancia"),
        "roles_con_marca": sum(1 for r in d["roles"] if r["marcas"]),
        "roles_limpios": sum(1 for r in d["roles"] if not r["marcas"]),
        "roles_por_marca": {m: sum(1 for r in d["roles"] if m in r["marcas"])
                            for m in ("MULTI_SUJETO", "SIN_ID_EN_CATALOGO",
                                      "APLANA_A_LA_MADRE", "CANDIDATO_INSTANCIA")},
    }


def render_md(d: dict) -> str:
    k = conteos(d)
    L = [
        "# U-ESQ-V3 fase 1 — Adjudicación de MIEMBROS de los 30 roles de alcance v3",
        "",
        "**Esto es una PROPUESTA mecánica en freno. Nada se escribió en ningún artefacto.**",
        "La adjudicación es de la autora, fila por fila: la última columna está vacía a propósito.",
        "",
        f"Colectivos que los pasajes nombran: **{k['colectivos']}** en {k['roles']} roles · "
        f"con candidato mecánico: **{k['con_candidato']}** "
        f"(idénticos {k['por_relacion']['identico']}, "
        f"recorte declarado {k['por_relacion']['recorte_declarado']}, "
        f"**más amplios (aplanan) {k['por_relacion']['mas_amplio']}**) · "
        f"**sin id en el catálogo v3: {k['sin_id_en_catalogo']}** · "
        f"candidatos de nivel `instancia`: **{k['candidatos_instancia']}** · "
        f"roles sin ninguna marca: **{k['roles_limpios']}** de {k['roles']}.",
        "",
        "Fuente de los colectivos: `prompt_v3_b54.ROLES_V3` (módulo SELLADO, solo lectura) — "
        "ya adjudicados por U-B5.4 fase 1 con su pasaje. Fuente de los pasajes: "
        "`data/experiment/escalado_prep/e0_dry/<to>/chunks_<to>.json`.",
        "",
        "**Criterio (fijado por el mandato, no se re-decide):** el miembro de un rol es la clase "
        "que el pasaje NOMBRA, a la granularidad en que la nombra — ni expandida a sus subclases "
        "ni colapsada a su clase madre. Un pasaje que enumera tres colectivos da tres miembros.",
        "",
        "**Columna `relacion`** — qué tan literal es el candidato respecto del colectivo: "
        "`identico` = coinciden · `recorte_declarado` = coinciden sus núcleos y el colectivo trae "
        "una aclaración que el candidato no porta (puede ser inocua —una sección, la ley que define "
        "al sujeto— o restrictiva; distinguirlas es juicio) · **`mas_amplio` = el candidato cubre MÁS "
        "que el colectivo: es el padre, y adoptarlo ES aplanar a la madre**, que el criterio prohíbe.",
        "",
        "**Marcas:** `MULTI_SUJETO` = el pasaje enumera más de un colectivo (pide juicio, no matcheo) · "
        "`SIN_ID_EN_CATALOGO` = algún colectivo nombrado no tiene id en el catálogo v3 (el matcheo NO "
        "sube al padre por su cuenta) · `APLANA_A_LA_MADRE` = algún candidato es `mas_amplio` · "
        "`CANDIDATO_INSTANCIA` = algún candidato es nivel `instancia`, no `clase` (los 17 miembros "
        "vigentes del grafo son los 17 de nivel `clase`).",
        "",
        "| # | TO | rol_id | colectivo que el pasaje nombra | candidato mecánico | regla | relacion | nivel | marcas del rol | cita | **adjudicación de la autora** |",
        "|---:|---|---|---|---|---|---|---|---|---|---|",
    ]
    i = 0
    for r in d["roles"]:
        for j, c in enumerate(r["candidatos"]):
            i += 1
            cand = f"`{c['candidato_id']}`" if c["candidato_id"] else "**— (sin id)**"
            if c["relacion"] == "mas_amplio":
                cand += " ⚠"
            marcas = ", ".join(r["marcas"]) if j == 0 and r["marcas"] else ""
            L.append(
                f"| {i} | {r['to'] if j == 0 else ''} | "
                f"{'`' + r['rol_id'] + '`' if j == 0 else ''} | "
                f"{_corto(c['colectivo'], 95)} | {cand} | {c['regla']} | "
                f"{c['relacion']} | {c['nivel_candidato'] or '—'} | {marcas} | "
                f"{'`' + r['cita_chunk_id'] + '`' if j == 0 else ''} |  |")
    sin = [(r, c) for r in d["roles"] for c in r["candidatos"] if not c["candidato_id"]]
    L += [
        "",
        f"## Los {len(sin)} colectivos SIN id en el catálogo v3",
        "",
        "El pasaje los nombra y el catálogo v3 no los tiene. El matcheo **no los sube al padre**: "
        "hacerlo sería colapsar a la madre. Las tres salidas posibles —dejar el rol con menos "
        "miembros que los que su pasaje nombra, aceptar el aplanamiento declarándolo, o abrir el "
        "catálogo (que es re-sello del prefijo v3 y por lo tanto otra unidad)— son adjudicación de "
        "la autora, no de esta tabla.",
        "",
        "La columna **pista** NO es un candidato: es la entrada del catálogo con mayor solapamiento "
        "de palabras (≥ 0,34), ofrecida solo para que el juicio tenga a mano lo más cercano que hay. "
        "Vacía = ni siquiera hay algo cercano.",
        "",
        "| # | TO | colectivo que el pasaje nombra | pista (no es candidato) | solapamiento |",
        "|---:|---|---|---|---|",
    ]
    for n, (r, c) in enumerate(sin, 1):
        p = c["pista_para_juicio"]
        L.append(f"| {n} | {r['to']} | {_corto(c['colectivo'], 95)} | "
                 f"{('`' + p['id'] + '` — ' + p['label']) if p else '—'} | "
                 f"{p['solapamiento'] if p else '—'} |")
    L += ["", "## Pasajes de alcance (verbatim de e0_dry, uno por rol)", ""]
    for r in d["roles"]:
        L += [f"### {r['to']} — `{r['rol_id']}`",
              f"**Label del rol:** {r['label_rol']}  ",
              f"**Cita:** `{r['cita_chunk_id']}` · página(s) {r['paginas']} · "
              f"unidad «{r['titulo_unidad']}»  ",
              f"**Marcas:** {', '.join(r['marcas']) or '—'}", "", "```",
              (r["pasaje"] or "(pasaje no encontrado en e0_dry)").strip(), "```", ""]
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=C.UNIDAD)
    args = ap.parse_args()
    d = construir()
    d["conteos"] = conteos(d)
    (args.out / "candidatos_miembros_v3.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    (args.out / "tabla_adjudicacion_miembros_v3.md").write_text(
        render_md(d), encoding="utf-8")
    print(json.dumps(d["conteos"], ensure_ascii=False, indent=1))
    print(f"-> {args.out / 'tabla_adjudicacion_miembros_v3.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
