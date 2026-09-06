"""
selftest_prompt_v3_b54.py — U-B5.4 fase 2: selftest del prefijo v3.

DEMUESTRA (mandato U-B5.4, decisión 3 + fase 2):
  1. Candado del texto base (sha congelado e69feaaa… / hash 1be8304e3d77).
  2. Anclas únicas del bloque de catálogo.
  3. BYTE-IDENTIDAD fuera del bloque de catálogo: reponer el bloque congelado
     dentro del prefijo v3 devuelve EXACTAMENTE el prefijo congelado (sha
     completo verificado); prefijo y sufijo alrededor del bloque son
     byte-idénticos.
  4. Tool schema: fuera de los DOS enums de sujeto (`sujeto_id`,
     `sujeto_propuesto_padre_sugerido`) el schema v3 es byte-idéntico al
     congelado (igualdad del canónico con los enums restaurados + diff
     estructural que enumera exactamente los paths que difieren).
  5. Conteos del catálogo resultante (regla i, recomputados): 102 ids =
     70 − 5 retiros + 7 adiciones + 30 roles (mini-laudo del freno 2: el rol
     de snp_cec RETIRADO — ausente de todo el prefijo y de ambos enums —,
     snp_cec mapea a la clase CEC); desglose 62 clases + 5 instancias +
     35 roles; enum == bloque == SUJETOS_CATALOGO_V3; retirados F1.5 ausentes
     de TODO el prefijo v3; 30 líneas `def:` (24 F1.3 + 6 posicionales F1.4);
     ROL_POR_TO_V3 = 5 dev + 66 nuevos (reparto 35 rol / 36 clase), huecos
     ausentes.
  6. Mensaje: para un chunk dev real, build_user_message_v3 es BYTE-IDÉNTICO
     al de producción; para un chunk nuevo con rol, la única diferencia con
     producción es la línea de alcance; docvig/fimipyme sin línea.
  7. DETERMINISMO cross-proceso: dos subprocesos frescos reconstruyen el
     prefijo v3 y reportan el mismo sha256 y hash canónico que este proceso.
  8. Sha nuevo estable y distinto del congelado (rotación de namespace).

Uso (desde cualquier cwd):  python3 <ruta>/selftest_prompt_v3_b54.py
Costo de API: USD 0 (ninguna llamada LLM).
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

_CODE_DIR = Path(__file__).resolve().parent
_REPO = _CODE_DIR.parents[3]
if str(_CODE_DIR) not in sys.path:
    sys.path.insert(0, str(_CODE_DIR))

import prompt_v3_b54 as v3  # noqa: E402
import prompt_congelado as pcg  # noqa: E402 — ya en path vía prompt_v3_b54
import prompt_e1  # noqa: E402

OK: list[str] = []


def check(nombre: str, cond: bool, detalle: str = "") -> None:
    if not cond:
        raise AssertionError(f"FALLA {nombre}: {detalle}")
    OK.append(f"  ✓ {nombre}" + (f" — {detalle}" if detalle else ""))


def paths_distintos(a, b, path=""):
    """Camina dos estructuras JSON y devuelve los paths donde difieren."""
    if type(a) is not type(b):
        return [path]
    if isinstance(a, dict):
        out = []
        for k in set(a) | set(b):
            if k not in a or k not in b:
                out.append(f"{path}.{k}")
            else:
                out += paths_distintos(a[k], b[k], f"{path}.{k}")
        return out
    if isinstance(a, list):
        if a != b:
            return [path]
        return []
    return [] if a == b else [path]


def main() -> None:
    # -- 1. candado del texto base ---------------------------------------- #
    sha_base = hashlib.sha256(pcg.PREFIJO_SISTEMA_CONGELADO.encode("utf-8")).hexdigest()
    check("candado sha congelado", sha_base == v3.PREFIJO_SHA256_CONGELADO_ESPERADO, sha_base[:12] + "…")
    check("candado hash congelado", pcg.PREFIJO_HASH_CONGELADO == v3.PREFIJO_HASH_CONGELADO_ESPERADO,
          pcg.PREFIJO_HASH_CONGELADO)

    # -- 2. anclas únicas -------------------------------------------------- #
    t = pcg.PREFIJO_SISTEMA_CONGELADO
    check("ancla inicio única", t.count(v3.ANCLA_INICIO_BLOQUE) == 1)
    check("ancla fin única", t.count(v3.ANCLA_FIN_BLOQUE) == 1)
    check("bloque congelado único en el prefijo", t.count(v3.BLOQUE_CATALOGO_CONGELADO) == 1)
    check("bloque v3 presente y único en el prefijo v3",
          v3.PREFIJO_SISTEMA_V3.count(v3.BLOQUE_CATALOGO_V3) == 1)

    # -- 3. byte-identidad fuera del bloque -------------------------------- #
    reconstruido = v3.PREFIJO_SISTEMA_V3.replace(v3.BLOQUE_CATALOGO_V3, v3.BLOQUE_CATALOGO_CONGELADO)
    check("reponer el bloque congelado ⇒ prefijo congelado byte-idéntico",
          reconstruido == pcg.PREFIJO_SISTEMA_CONGELADO)
    check("sha del reconstruido == e69feaaa…",
          hashlib.sha256(reconstruido.encode("utf-8")).hexdigest() == v3.PREFIJO_SHA256_CONGELADO_ESPERADO)
    i = t.index(v3.ANCLA_INICIO_BLOQUE)
    j3 = v3.PREFIJO_SISTEMA_V3.index(v3.ANCLA_INICIO_BLOQUE)
    check("prefijo ANTES del bloque byte-idéntico", t[:i] == v3.PREFIJO_SISTEMA_V3[:j3] and i == j3)
    k = t.index(v3.ANCLA_FIN_BLOQUE)
    k3 = v3.PREFIJO_SISTEMA_V3.index(v3.ANCLA_FIN_BLOQUE)
    check("sufijo DESPUÉS del bloque byte-idéntico", t[k:] == v3.PREFIJO_SISTEMA_V3[k3:])

    # -- 4. tool schema: solo los dos enums cambian ------------------------ #
    import copy
    restaurado = copy.deepcopy(v3.TOOL_SCHEMA_V3)
    pr = restaurado["input_schema"]["properties"]["relations"]["items"]["properties"]
    pr["sujeto_id"]["enum"] = list(pcg.SUJETOS_CATALOGO)
    pr["sujeto_propuesto_padre_sugerido"]["enum"] = list(pcg.SUJETOS_CATALOGO)
    can_rest = json.dumps(restaurado, sort_keys=True, ensure_ascii=False)
    can_cong = json.dumps(pcg.TOOL_SCHEMA_CONGELADO, sort_keys=True, ensure_ascii=False)
    check("tool schema con enums restaurados == congelado (canónico)", can_rest == can_cong)
    difs = paths_distintos(v3.TOOL_SCHEMA_V3, pcg.TOOL_SCHEMA_CONGELADO)
    esperados = {
        ".input_schema.properties.relations.items.properties.sujeto_id.enum",
        ".input_schema.properties.relations.items.properties.sujeto_propuesto_padre_sugerido.enum",
    }
    check("diff estructural del schema == exactamente los 2 enums", set(difs) == esperados, str(sorted(difs)))

    # -- 5. conteos (regla i) ---------------------------------------------- #
    enum_v3 = v3.TOOL_SCHEMA_V3["input_schema"]["properties"]["relations"]["items"]["properties"]["sujeto_id"]["enum"]
    check("102 ids en el enum v3", len(enum_v3) == 102, f"{len(enum_v3)}")
    check("composición 70−5+7+30", len(pcg.SUJETOS_CATALOGO) - len(v3.RETIROS_V3)
          + len(v3.ADICIONES_V3) + len(v3.ROLES_V3) == 102,
          f"{len(pcg.SUJETOS_CATALOGO)}−{len(v3.RETIROS_V3)}+{len(v3.ADICIONES_V3)}+{len(v3.ROLES_V3)}")
    check("enum sujeto_id == enum padre_sugerido",
          enum_v3 == v3.TOOL_SCHEMA_V3["input_schema"]["properties"]["relations"]["items"]["properties"]["sujeto_propuesto_padre_sugerido"]["enum"])
    check("enum == SUJETOS_CATALOGO_V3", enum_v3 == v3.SUJETOS_CATALOGO_V3)
    check("sin duplicados en el enum", len(enum_v3) == len(set(enum_v3)))

    ids_bloque = [l.split(" — ", 1)[0] for l in v3.BLOQUE_CATALOGO_V3.split("\n")
                  if l.startswith("Sujeto_") and " — " in l]
    check("ids del bloque v3 == enum v3 (mismo conjunto)", set(ids_bloque) == set(enum_v3),
          f"bloque {len(ids_bloque)}")
    n_inst = sum(1 for l in v3.BLOQUE_CATALOGO_V3.split("\n") if l.rstrip().endswith("[instancia]"))
    n_rol = sum(1 for x in ids_bloque if x.startswith("Sujeto_rol_"))
    n_clase = len(ids_bloque) - n_inst - n_rol
    check("desglose 62 clases + 5 instancias + 35 roles",
          (n_clase, n_inst, n_rol) == (62, 5, 35), f"({n_clase},{n_inst},{n_rol})")
    for rid in v3.RETIROS_V3:
        check(f"retirado ausente de TODO el prefijo v3: {rid}", rid not in v3.PREFIJO_SISTEMA_V3)
        check(f"retirado ausente del enum: {rid}", rid not in enum_v3)
    # Mini-laudo del freno 2: el rol de snp_cec retirado (corrección pre-sello).
    rol_cec = "Sujeto_rol_alcance_snp_cec"
    check(f"rol retirado por mini-laudo ausente de TODO el prefijo v3: {rol_cec}",
          rol_cec not in v3.PREFIJO_SISTEMA_V3)
    check(f"rol retirado por mini-laudo ausente de ambos enums: {rol_cec}",
          rol_cec not in enum_v3 and rol_cec not in
          v3.TOOL_SCHEMA_V3["input_schema"]["properties"]["relations"]["items"]["properties"]["sujeto_propuesto_padre_sugerido"]["enum"])
    check("snp_cec mapea a la clase CEC",
          v3.MAPEO_CLASE_V3.get("snp_cec") == ("Sujeto_camara_electronica_de_compensacion",))
    # Laudo de cierre (06/09/2026) — H1a rename + H4a def dirigida + H2a guarda.
    import re as _re
    check("id viejo (entidad_originante a secas) AUSENTE del prefijo v3",
          not _re.search(r"Sujeto_entidad_originante(?!_de_transferencia)", v3.PREFIJO_SISTEMA_V3))
    check("id viejo AUSENTE de ambos enums",
          "Sujeto_entidad_originante" not in enum_v3 and "Sujeto_entidad_originante" not in
          v3.TOOL_SCHEMA_V3["input_schema"]["properties"]["relations"]["items"]["properties"]["sujeto_propuesto_padre_sugerido"]["enum"])
    check("id nuevo presente en ambos enums y en el bloque",
          "Sujeto_entidad_originante_de_transferencia" in enum_v3
          and "Sujeto_entidad_originante_de_transferencia — " in v3.BLOQUE_CATALOGO_V3)
    check("def y guarda del renombrado INTACTAS",
          "NO es el originante de una securitización o fideicomiso: ese sujeto sigue en sujeto_propuesto"
          in v3.BLOQUE_CATALOGO_V3)
    check("def dirigida de sector_publico_no_financiero presente (H4a)",
          "NO incluye entidades financieras públicas (bancos públicos) ni entidades autorizadas a operar como entidades financieras"
          in v3.BLOQUE_CATALOGO_V3)
    n_def = sum(1 for l in v3.BLOQUE_CATALOGO_V3.split("\n") if l.startswith("  def: "))
    check("30 líneas def: (24 F1.3 + 6 posicionales F1.4)", n_def == 30, f"{n_def}")
    check("ROL_POR_TO_V3 = 5 dev + 66 nuevos", len(v3.ROL_POR_TO_V3) == 71, f"{len(v3.ROL_POR_TO_V3)}")
    for hueco in v3.HUECOS_SIN_ROL:
        check(f"hueco sin entrada: {hueco}", f"{hueco}.pdf" not in v3.ROL_POR_TO_V3)
    check("los 36 mapeos a clase apuntan a ids del catálogo (no roles)",
          len(v3.MAPEO_CLASE_V3) == 36
          and all(c in enum_v3 and not c.startswith("Sujeto_rol_")
                  for ids in v3.MAPEO_CLASE_V3.values() for c in ids),
          f"{len(v3.MAPEO_CLASE_V3)} TOs")
    check("los 30 roles están en el enum",
          len(v3.ROLES_V3) == 30
          and all(v3.rol_id_de(to) in enum_v3 for to, _, _ in v3.ROLES_V3))
    n_entradas_rol = sum(1 for r in v3.ROL_POR_TO_V3.values()
                         if str(r.get("rol_id", "")).startswith("Sujeto_rol_"))
    check("reparto ROL_POR_TO_V3: 35 rol (5 dev + 30) / 36 clase",
          n_entradas_rol == 35 and len(v3.ROL_POR_TO_V3) - n_entradas_rol == 36,
          f"({n_entradas_rol},{len(v3.ROL_POR_TO_V3) - n_entradas_rol})")
    # dev pass-through byte-idéntico
    check("las 5 entradas dev de ROL_POR_TO_V3 == producción",
          all(v3.ROL_POR_TO_V3[a] == prompt_e1.ROL_POR_TO[a] for a in prompt_e1.ROL_POR_TO),
          f"{len(prompt_e1.ROL_POR_TO)} entradas")

    # -- 6. mensajes ------------------------------------------------------- #
    chunks_cap = json.loads(
        (_REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cap.json").read_text())
    ch_dev = chunks_cap[0]
    check("mensaje dev byte-idéntico a producción",
          v3.build_user_message_v3(ch_dev) == prompt_e1.build_user_message(ch_dev), ch_dev["id"])
    ch_nuevo = json.loads(
        (_REPO / "data/experiment/escalado_prep/e0_dry/efemin/chunks_efemin.json").read_text())[0]
    m_prod = prompt_e1.build_user_message(ch_nuevo)
    m_v3 = v3.build_user_message_v3(ch_nuevo)
    check("mensaje TO nuevo: producción SIN línea de alcance", "Alcance de este TO" not in m_prod)
    check("mensaje TO nuevo: v3 CON línea de alcance", "Alcance de este TO: Sujeto_rol_alcance_efemin" in m_v3)
    parrafos_alcance = [p for p in m_v3.split("\n\n") if p.startswith("Alcance de este TO")]
    check("mensaje TO nuevo: única diferencia = la línea de alcance",
          len(parrafos_alcance) == 1
          and m_v3.replace(parrafos_alcance[0] + "\n\n", "", 1) == m_prod)
    ch_clase = json.loads(
        (_REPO / "data/experiment/escalado_prep/e0_dry/depinv/chunks_depinv.json").read_text())[0]
    m_clase = v3.build_user_message_v3(ch_clase)
    check("mensaje TO de clase: usa el id de clase",
          "Alcance de este TO: Sujeto_entidad_financiera" in m_clase, ch_clase["id"])
    check("mensaje con rol: guarda de ejecuta presente (H2a)",
          "NO es el ejecutor por defecto en ejecuta" in m_v3)
    check("mensaje de clase: guarda de ejecuta presente (H2a)",
          "NO es el ejecutor por defecto en ejecuta" in m_clase)
    ch_hueco = json.loads(
        (_REPO / "data/experiment/escalado_prep/e0_dry/docvig/chunks_docvig.json").read_text())[0]
    check("mensaje de hueco (docvig): SIN línea de alcance",
          "Alcance de este TO" not in v3.build_user_message_v3(ch_hueco), ch_hueco["id"])
    ch_dos = json.loads(
        (_REPO / "data/experiment/escalado_prep/e0_dry/ri2_ci/chunks_ri2_ci.json").read_text())[0]
    m_dos = v3.build_user_message_v3(ch_dos)
    check("mensaje ri2_ci (dos clases): variante declarada",
          "usá Sujeto_casa_de_cambio o Sujeto_agencia_de_cambio como sujeto" in m_dos)

    # -- 7. determinismo cross-proceso ------------------------------------- #
    script = (
        "import sys; sys.path.insert(0, r'''" + str(_CODE_DIR) + "'''); "
        "import prompt_v3_b54 as m; print(m.PREFIJO_SHA256_V3, m.PREFIJO_HASH_V3)"
    )
    corridas = []
    for _ in range(2):
        r = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True, check=True)
        corridas.append(r.stdout.split())
    check("determinismo cross-proceso (2 subprocesos)",
          corridas[0] == corridas[1] == [v3.PREFIJO_SHA256_V3, v3.PREFIJO_HASH_V3],
          f"sha {corridas[0][0][:12]}… hash {corridas[0][1]}")

    # -- 8. sha nuevo ------------------------------------------------------- #
    check("sha v3 ≠ sha congelado", v3.PREFIJO_SHA256_V3 != v3.PREFIJO_SHA256_CONGELADO_ESPERADO)
    check("hash canónico v3 ≠ congelado (namespace nuevo)",
          v3.PREFIJO_HASH_V3 != pcg.PREFIJO_HASH_CONGELADO)

    print(f"SELFTEST prompt_v3_b54: {len(OK)} checks OK")
    for l in OK:
        print(l)
    print()
    print(f"PREFIJO_SHA256_V3   = {v3.PREFIJO_SHA256_V3}")
    print(f"PREFIJO_HASH_V3     = {v3.PREFIJO_HASH_V3}  (namespace de caché)")
    print(f"chars prefijo v3    = {len(v3.PREFIJO_SISTEMA_V3)}  (congelado: {len(pcg.PREFIJO_SISTEMA_CONGELADO)})")
    print(f"ids catálogo v3     = {len(v3.SUJETOS_CATALOGO_V3)}")


if __name__ == "__main__":
    main()
