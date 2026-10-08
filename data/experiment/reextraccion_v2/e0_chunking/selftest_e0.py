"""Selftest de E0: determinismo, cero pérdida de texto y tests de aceptación.

Uso: python3 selftest_e0.py [--dir-a DIR] [--dir-b DIR]

Sin argumentos corre el pipeline DOS veces en directorios temporales del
scratchpad de la sesión (o de sistema) y compara sha256 archivo por archivo;
después corre los tests de aceptación T4 sobre la primera corrida.

Tests de aceptación (casos reales documentados del proyecto):
  a) ext 3.9 entero: chunks 3.9.1–3.9.5 presentes, tope 'USD 200' en 3.9.1,
     y 3.9 NO es chunk terminal (es contenedor: título+intro+cierre en herencia).
  b) herencia de chapeau: el plazo '20 (veinte) días hábiles' del encabezado sin
     numerar del 7.6 de ext viaja en la herencia de TODOS los chunks 7.6.x;
     los cierres sin numerar del 2.7 de ext (cómputo a límites + declaración
     jurada) viajan en la herencia de TODOS los chunks 2.7.x.
  c) cla 1.1, cla 4.5 y ext 9.2: el cuerpo SÍ los contiene (labels reales en el
     PDF, verificados contra páginas 4, 15 y 123). El test es que existen como
     chunks CON contenido sustantivo (no cáscaras fabricadas) y con el título
     que el índice anuncia. NOTA: el mandato de la unidad esperaba verlos como
     divergencia 'anunciado sin cuerpo'; esa expectativa proviene de RX-04, que
     describe el output del chunker v1 (que los absorbía en vecinos), no el PDF.
     La contradicción se reporta; el archivo del repo (docs/backlog_reextraccion.md,
     RX-04: 'Su texto está en el corpus … pero no existe como pasaje con nombre')
     respalda esta lectura.
  d) ric: la divergencia de la Sección 3 capturada — el índice anuncia 3.2
     'Modelo de información' sin cuerpo propio; el cuerpo lo rinde como 3.1.4.
  e) tablas: cuadros de ponderadores de cap (2.12.2.4, 2.13) y cuadros de
     partidas de ric (3.1.4, 7.2) flaggeados contenido_tabular.

Tests de mini-chunks (enmienda 01 §2.a, ver e0_lib):
  i) determinismo y criterio: 286 mini-chunks en los 5 TOs (pro: 13), ids
     <to>::<unidad>::<rol>[::<n>] únicos, sha256 propio correcto, herencia
     solo de tramos encabezado, provenance (unidad) = unidad de origen;
     cero mini-chunks de rol encabezado (los títulos puros no materializan);
     el intro de 1.144 chars del 7.6 de ext (el 'encabezado sin numerar' del
     INFORME §6.b, tipo intro en la salida real) SÍ materializa; el intro
     normativo de una línea del 2.7 de pro SÍ materializa (la letra del
     criterio, no la heurística de escala); terminales byte-idénticos a la
     emisión sin minis (mismo contenido, minis interleaved); conteos con
     mini_chunks y censo-oráculo sin cambios.

Tests de la corrección post-calibración (reglas 1 y 2, ver e0_lib):
  f) regla 1 — continuidad de enumeración: los acápites vii)–x) de pro
     2.3.1.1 salen en su texto PROPIO y la herencia de 2.3.1.2–2.3.1.4 ya no
     los porta; el registro de reasignaciones contiene exactamente ese caso.
  g) regla 2 — cero fronteras de segmento intra-palabra en los 5 TOs
     (detector de e0_lib._clasificar_frontera; exclusiones auditadas en
     correcciones.json).
  h) ric 4.4: la regla 1 no aplica (no hay continuidad de lista en esa
     costura) — cero reasignaciones en ric y el contenido de 4.4.3/4.4.4
     sigue, como limitación documentada, dentro del propio de 4.3.3.

Tests de S0 de U-SEG-OFICIAL (S0-2; solo la versión e0-r2, con los PDFs de la
partición, data/experiment/escalado_prep/pdfs/; diseño en
data/experiment/segmentacion_oficial_e0r2/s0_1/ y s0_1bis/):
  j) la versión legada no cambia: los parámetros nuevos de clasificar_paginas
     y parsear_cuerpo están apagados por default;
  k) un caso medido por regla, corriendo e0-r2 sobre nueve TOs: regla 1
     (garopt, «Sección N –»), 2 (ri_dsf, códigos de actividad que no son
     puntos), 3 (venliq, primera página de cuerpo; adfsp p. 3, índice por
     lista), 4 (ri_spi, marcador de letra), 7 (manori, reapertura del
     padre), T (snp_dd, tablas fundidas), 8 (manori, lista de la sección
     vetada), 9 (rdbcra, filas del catálogo) y la cobertura exacta;
  l) casos sintéticos de las reglas 5 (cola de título en la lista de
     páginas), 6 (partición por renglones en E0 y en E1, con la capacidad
     del tercer escalón) y 8 (detección de la lista y sus guardas);
  m) doble corrida de e0-r2 sobre dos de esos TOs, byte a byte igual.
Desde S0-3, el caso medido del acompañamiento T es snp_dd y el de la regla 7, manori: con el mecanismo 1 de S0-3
las tablas de ri_dcpc quedan en el cuerpo de 2.4 y 2.5 y T ya no actúa ahí, y ri_mmsef 2.2 no se cierra, así que
la regla 7 no tiene que reabrirlo (sus unidades no cambian).

Tests de S0-3 de U-SEG-OFICIAL (solo la versión e0-r2; diseño en
data/experiment/segmentacion_oficial_e0r2/s0_3/):
  n) la versión legada no cambia: los parámetros de los mecanismos están apagados por default;
  o) casos sintéticos de cada forma: 1a (y sus dos guardas), 1b, 2 (a, b y c), 3 y 5 (a, b, la cola real y el
     inciso, c);
  p) un caso medido por mecanismo, corriendo e0-r2 sobre nueve TOs: 1a (ri_dcpc, nmcief), 2a (seggar), 2c
     (ri_tar), 3 (ri2_ae), 4a de S0-4 (seguef, que era el caso del mecanismo 4), 5a (fimipyme), 5b (ri2_ci) y 5c
     (ri_ai), y la cobertura exacta.
El mecanismo 4 de S0-3 no está desde S0-4 (lo reemplazan las reglas 4a y 4b).

Tests de S0-4 de U-SEG-OFICIAL (solo la versión e0-r2; diseño en
data/experiment/segmentacion_oficial_e0r2/s0_4/):
  q) la versión legada no cambia: los parámetros de las reglas de S0-4 están apagados por default, y las listas de
     TOs son las del diseño (sub-documento sin ri_tsa ni ri2_pm; 4a y 4b fuera de los diez TOs de la tanda 0);
  r) casos sintéticos: la detección de sub-documentos (anexo, parte, régimen, formulario y circular, con sus
     guardas: el anexo repetido, la serie de letras, la parte suelta, la continuación de un formulario y la
     circular suelta), la lectura con sub-documentos (prefijo, numeración desde cero y herencia del rótulo), la
     guarda de columna dentro del sub-documento, la raíz mayor que MAX_RAIZ dentro del sub-documento (sdmax, de
     S0-4a-bis), 4a, 4b (con su guarda del verbo) y los apartados; y las reglas de S0-4a-ter: el régimen de la página
     1 (sdr1), los apartados de letra con raíces numéricas (apl), el sub-documento de letra (sdl), la herencia de su
     rótulo (sdlh, con sdl y sin ella) y el rótulo «X.n.» con la letra vigente (sdla);
  s) un caso medido por regla, corriendo e0-r2 sobre ocho TOs: sub-documento (ri_sef, nmcief, ri_ccna,
     ri_icpipsp, ri_cc: los cinco casos de prueba del FRENO S0-3), sdg3 (nmcief), sdmax (ri_ccna, ítems 31 a 40 del
     Anexo III; y ri_sef, cuyos códigos 101 a 126 no son sucesores), sdr1 y apl (ri_oc), sdl, sdlh y sdla (ri_ccna,
     Anexo III), 4b (efemin), apartados (ri_ai), y la cobertura exacta.
Desde S0-4 cambian dos casos medidos de etapas anteriores: el de la regla 4 cuenta 93 unidades de ri_spi (4b retira
las intros de un renglón de B.1 y B.3) y el de 1a en nmcief lee nmcief::A2::3.2.1 (el punto es del Anexo II). Desde
S0-4a-ter, el caso medido de sdmax lee los ítems 31 a 40 en el sub-documento de letra (ri_ccna::D1A3L2::S31…).
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

import correr_e0

AQUI = Path(__file__).parent

RESULTADOS: list[tuple[str, bool, str]] = []


def check(nombre: str, ok: bool, detalle: str = "") -> None:
    RESULTADOS.append((nombre, ok, detalle))
    print(f"  [{'PASS' if ok else 'FAIL'}] {nombre}" + (f" — {detalle}" if detalle else ""))


def cargar(d: Path, nombre: str):
    return json.loads((d / nombre).read_text(encoding="utf-8"))


def test_determinismo(dir_a: Path, dir_b: Path) -> None:
    print("== determinismo (dos corridas → sha idénticos)")
    sha_a = correr_e0.shas_salida(dir_a)
    sha_b = correr_e0.shas_salida(dir_b)
    check("mismos archivos de salida", set(sha_a) == set(sha_b),
          f"{len(sha_a)} archivos")
    distintos = [n for n in sha_a if sha_a[n] != sha_b.get(n)]
    check("sha256 idénticos archivo por archivo", not distintos,
          f"difieren: {distintos}" if distintos else f"{len(sha_a)}/{len(sha_a)} iguales")


def test_cobertura(d: Path) -> None:
    print("== cero pérdida de texto (cobertura por línea + suma de chars)")
    cob = cargar(d, "cobertura.json")
    for to, c in cob.items():
        check(f"cobertura exacta {to}", c["cobertura_exacta"],
              f"{c['lineas_en_estructura']}/{c['lineas_contenido_parseadas']} líneas, "
              f"{c['lineas_duplicadas']} duplicadas, {c['lineas_huerfanas']} huérfanas")
    # suma de chars: el texto de la estructura reconstruye el contenido del cuerpo
    for to in ("cap", "cla", "ext", "pro", "ric"):
        est = cargar(d, f"estructura_{to}.json")
        def chars_nodo(n):
            total = len(f"{n['numero']}. {n['titulo']}") if n["tipo"] == "punto" else 0
            total += sum(s["chars"] for s in n["segmentos"])
            return total + sum(chars_nodo(h) for h in n["hijos"])
        total = sum(chars_nodo(s) for s in est["secciones"])
        check(f"chars en estructura {to} > 0 y serializados", total > 0, f"{total:,} chars")


def test_t4(d: Path) -> None:
    print("== T4(a) ext 3.9 entero")
    # T4 habla de chunks TERMINALES; desde la enmienda 01 los archivos traen
    # además mini-chunks (que comparten `unidad` con su punto de origen) — se
    # filtran acá y se testean aparte en test_minichunks.
    ext = [c for c in cargar(d, "chunks_ext.json") if c["tipo"] != "mini_chunk"]
    por_unidad = {c["unidad"]: c for c in ext}
    esperados = [f"3.9.{i}" for i in range(1, 6)]
    check("chunks 3.9.1–3.9.5 presentes", all(u in por_unidad for u in esperados),
          str([u for u in esperados if u in por_unidad]))
    check("'USD 200' en el texto propio de 3.9.1",
          "USD 200" in por_unidad.get("3.9.1", {}).get("texto", ""))
    check("3.9 no es chunk (es contenedor con herencia)", "3.9" not in por_unidad)
    her = por_unidad.get("3.9.1", {}).get("herencia", [])
    check("herencia de 3.9.1 trae intro y cierre del 3.9",
          any(t["unidad_origen"] == "3.9" and t["tipo"] == "intro" for t in her)
          and any(t["unidad_origen"] == "3.9" and t["tipo"] == "cierre" for t in her))

    print("== T4(b) herencia de chapeau (ext 7.6 y 2.7)")
    c76 = [c for c in ext if c["unidad"].startswith("7.6.")]
    check("hay chunks 7.6.x", len(c76) >= 6, f"{len(c76)} chunks")
    ok76 = all(any(t["unidad_origen"] == "7.6"
                   and "20 (veinte) días hábiles" in t["texto"]
                   for t in c["herencia"]) for c in c76)
    check("'20 (veinte) días hábiles' del encabezado del 7.6 viaja en la herencia "
          "de todos los 7.6.x", ok76)
    c27 = [c for c in ext if c["unidad"].startswith("2.7.")]
    check("hay chunks 2.7.1–2.7.4", sorted(c["unidad"] for c in c27) ==
          ["2.7.1", "2.7.2", "2.7.3", "2.7.4"])
    ok27 = all(any(t["unidad_origen"] == "2.7" and t["tipo"] == "cierre"
                   and "límites" in t["texto"] and "declaración jurada" in t["texto"]
                   for t in c["herencia"]) for c in c27)
    check("cierres sin numerar del 2.7 (cómputo a límites + DDJJ) viajan en la "
          "herencia de todos los 2.7.x", ok27)

    print("== T4(c) cla 1.1, cla 4.5, ext 9.2 (ver docstring: contradicción con "
          "el mandato, reportada)")
    cla = [c for c in cargar(d, "chunks_cla.json") if c["tipo"] != "mini_chunk"]
    cla_u = {c["unidad"]: c for c in cla}
    for u, titulo in [("1.1", "Criterio general"),
                      ("4.5", "Deudores que no deben ser objeto de clasificación")]:
        c = cla_u.get(u)
        check(f"cla {u} existe como chunk real (no cáscara)",
              c is not None and c["chars_propio"] > 200 and titulo in c["titulo"],
              f"{c['chars_propio']} chars" if c else "ausente")
    c92 = por_unidad.get("9.2")
    check("ext 9.2 existe como chunk real (no cáscara)",
          c92 is not None and c92["chars_propio"] > 200
          and "Entidad nominada" in c92["titulo"],
          f"{c92['chars_propio']} chars" if c92 else "ausente")
    div = cargar(d, "divergencias_indice_cuerpo.json")
    fabricados = [u for u in ("1.1", "4.5") if cla_u.get(u, {}).get("chars_propio", 0) <= 60]
    check("ningún chunk vacío fabricado para estos puntos", not fabricados)

    print("== T4(d) ric Sección 3: 3.2 anunciado sin cuerpo; el cuerpo lo rinde 3.1.4")
    anuncios = [x["numero"] for x in div["ric"]["anunciado_sin_cuerpo"]]
    check("ric 3.2 en anunciado_sin_cuerpo", "3.2" in anuncios, str(anuncios))
    ric = [c for c in cargar(d, "chunks_ric.json") if c["tipo"] != "mini_chunk"]
    ric_u = {c["unidad"]: c for c in ric}
    check("ric 3.1.4 'Modelo de información' existe como chunk",
          "3.1.4" in ric_u and "Modelo de información" in ric_u["3.1.4"]["titulo"])

    print("== T4(e) tablas flaggeadas")
    cap = [c for c in cargar(d, "chunks_cap.json") if c["tipo"] != "mini_chunk"]
    cap_u = {c["unidad"]: c for c in cap}
    for u in ("2.12.2.4", "2.13"):
        check(f"cap {u} (cuadro de ponderadores/CCF) flag contenido_tabular",
              cap_u.get(u, {}).get("flags", {}).get("contenido_tabular", False))
    for u in ("3.1.4", "7.2"):
        check(f"ric {u} (cuadro de partidas) flag contenido_tabular",
              ric_u.get(u, {}).get("flags", {}).get("contenido_tabular", False))


def test_correcciones(d: Path) -> None:
    print("== T6(f) regla 1: acápites vii)–x) en el propio de pro 2.3.1.1")
    pro = [c for c in cargar(d, "chunks_pro.json") if c["tipo"] != "mini_chunk"]
    pro_u = {c["unidad"]: c for c in pro}
    propio = pro_u["2.3.1.1"]["texto"]
    check("'vii)' en el texto propio de pro 2.3.1.1", "vii)" in propio)
    check("'Régimen de Transparencia' en el texto propio de pro 2.3.1.1",
          "Régimen de Transparencia" in propio)
    check("'x) Los restantes requisitos' en el texto propio de pro 2.3.1.1",
          "x) Los restantes requisitos" in propio)
    sin_acapites = all(
        "vii)" not in t["texto"] and "Régimen de Transparencia" not in t["texto"]
        for u in ("2.3.1.2", "2.3.1.3", "2.3.1.4")
        for t in pro_u[u]["herencia"])
    check("la herencia de 2.3.1.2–2.3.1.4 ya no porta los acápites", sin_acapites)
    corr = cargar(d, "correcciones.json")
    reasig = [(to, r) for to, dd in corr.items()
              for r in dd["reasignaciones_continuidad"]]
    check("toda reasignación de la regla 1 es pro 2.3.1→2.3.1.1 (caso conocido)",
          reasig and all(to == "pro" and r["padre"] == "2.3.1"
                         and r["destino"] == "2.3.1.1" for to, r in reasig),
          f"{len(reasig)} reasignaciones")

    print("== T6(g) regla 2: cero fronteras de segmento intra-palabra")
    for to in ("cap", "cla", "ext", "pro", "ric"):
        f = corr[to]["fronteras_intra_palabra"]
        check(f"fronteras intra-palabra {to}: {f['antes']} → 0",
              f["despues"] == 0, f"{len(f['lineas_corridas'])} líneas corridas")

    print("== T6(h) ric 4.4: regla 1 no aplica (limitación se mantiene)")
    check("cero reasignaciones en ric", not corr["ric"]["reasignaciones_continuidad"])
    ric = [c for c in cargar(d, "chunks_ric.json") if c["tipo"] != "mini_chunk"]
    ric_u = {c["unidad"]: c for c in ric}
    t433 = ric_u["4.3.3"]["texto"]
    check("contenido de 4.4.3/4.4.4 sigue en el propio de ric 4.3.3",
          "4.4.3. Riesgo de cambio" in t433 and "4.4.4." in t433)


def test_minichunks(d: Path) -> None:
    print("== T7(i) mini-chunks (enmienda 01 §2.a)")
    todos = {to: cargar(d, f"chunks_{to}.json") for to in ("cap", "cla", "ext", "pro", "ric")}
    minis = {to: [c for c in cs if c["tipo"] == "mini_chunk"] for to, cs in todos.items()}
    n_total = sum(len(m) for m in minis.values())
    check("286 mini-chunks en los 5 TOs (contraste con estimación 284 de la enmienda)",
          n_total == 286, f"{n_total} ({ {to: len(m) for to, m in minis.items()} })")
    check("pro emite 13 mini-chunks (== estimación de la enmienda)",
          len(minis["pro"]) == 13, str([m["id"] for m in minis["pro"]]))

    ids = [m["id"] for cs in minis.values() for m in cs]
    check("ids de mini-chunks únicos", len(ids) == len(set(ids)))
    import re as _re
    patron = _re.compile(r"^(cap|cla|ext|pro|ric)::[S0-9.]+::(chapeau_seccion|intro|intersticial|cierre)(::\d+)?$")
    malformados = [i for i in ids if not patron.match(i)]
    check("ids con forma <to>::<unidad>::<rol>[::<n>]", not malformados, str(malformados[:5]))
    check("cero mini-chunks de rol encabezado (títulos puros no materializan)",
          not any(m["rol_bloque"] == "encabezado" for cs in minis.values() for m in cs))

    import hashlib as _hl
    check("sha256_propio de cada mini = sha del texto del bloque",
          all(m["sha256_propio"] == _hl.sha256(m["texto"].encode()).hexdigest()
              for cs in minis.values() for m in cs))
    check("herencia de todo mini: solo tramos encabezado (títulos de la cadena)",
          all(t["tipo"] == "encabezado" for cs in minis.values()
              for m in cs for t in m["herencia"]))
    check("la unidad del mini es su unidad de origen (el id la contiene)",
          all(m["id"].split("::")[1] == m["unidad"] for cs in minis.values() for m in cs))

    m76 = [m for m in minis["ext"] if m["id"] == "ext::7.6::intro"]
    check("el bloque de 1.144 chars del 7.6 de ext materializa como intro",
          len(m76) == 1 and m76[0]["chars_propio"] == 1144
          and "20 (veinte) días hábiles" in m76[0]["texto"])
    m27 = [m for m in minis["pro"] if m["id"] == "pro::2.7::intro"]
    check("el intro normativo de UNA línea del 2.7 de pro materializa (letra del "
          "criterio, no la heurística de escala)",
          len(m27) == 1 and "sendos hipervínculos" in m27[0]["texto"])
    m231 = [m for m in minis["pro"] if m["id"] == "pro::2.3.1::intro"]
    check("pro::2.3.1::intro (norma de Caja de ahorros) materializa",
          len(m231) == 1 and "Caja de" in m231[0]["texto"])
    check("pro::S3::chapeau_seccion materializa",
          any(m["id"] == "pro::S3::chapeau_seccion" for m in minis["pro"]))

    inter = sorted(m["id"] for cs in minis.values() for m in cs
                   if m["rol_bloque"] == "intersticial")
    check("los 3 intersticiales de ext materializan (uno por segmento)",
          inter == ["ext::3.16.3::intersticial", "ext::4.2::intersticial",
                    "ext::7.9.3::intersticial"], str(inter))

    # interleaved documental: intro antes del primer hijo, cierre tras el último
    ids_pro = [c["id"] for c in todos["pro"]]
    check("emisión interleaved: pro::2.3.1::intro antes de pro::2.3.1.1 y "
          "pro::2.7::cierre después de pro::2.7.2",
          ids_pro.index("pro::2.3.1::intro") < ids_pro.index("pro::2.3.1.1")
          and ids_pro.index("pro::2.7::cierre") > ids_pro.index("pro::2.7.2"))

    conteos = cargar(d, "conteos.json")
    check("conteos: chunks = terminales + mini_chunks en los 5 TOs",
          all(c["chunks"] == c["chunks_terminales"] + c["mini_chunks"]
              for c in conteos.values()),
          str({to: (c["chunks_terminales"], c["mini_chunks"]) for to, c in conteos.items()}))


# ------------------------------------------- S0 de U-SEG-OFICIAL (e0-r2)

PDFS_PARTICION = AQUI.resolve().parents[1] / "escalado_prep" / "pdfs"
TOS_S0 = ("garopt", "ri_dsf", "venliq", "adfsp", "ri_spi", "ri_mmsef", "snp_dd", "manori", "rdbcra")


class _ManifiestoParticion:
    """Lo que `correr_e0.correr` lee de un manifiesto: ids, archivo y PDF (los de la partición)."""
    tiene_oraculo = False
    mapa_territorio = None

    def __init__(self, ids):
        self.ids = list(ids)

    def archivo_de(self, to: str) -> str:
        return f"{to}.pdf"

    def pdf_de(self, to: str) -> Path:
        return PDFS_PARTICION / f"{to}.pdf"


def _linea(texto: str, pagina: int, top: float, x0: float = 60.0, ngaps: int = 0):
    return correr_e0.E0.Linea(pagina=pagina, top=top, x0=x0, texto=texto, ngaps=ngaps,
                              ultimo_numerico=False, primer_codigo=False)


def _unidad(texto: str, uid: str = "x::S1", tipo: str = "seccion_sin_puntos") -> dict:
    return {"id": uid, "to": "x", "archivo": "x.pdf", "unidad": uid.split("::", 1)[1], "titulo": "t",
            "tipo": tipo, "paginas": [1], "texto": texto, "chars_propio": len(texto),
            "chars_completo": len(texto), "herencia": [], "flags": {}, "sha256_propio": "",
            "sha256_completo": ""}


def test_s0_legada() -> None:
    import inspect
    E0 = correr_e0.E0
    print("== j) S0 de U-SEG-OFICIAL: la versión legada no cambia")
    p = inspect.signature(E0.parsear_cuerpo).parameters
    nuevos = {"seccion_variante": False, "rotulos_r2": False, "marcador_letra": False, "reabrir_padre": False,
              "no_rotulos": frozenset(), "rotulos_fila": frozenset()}
    check("parsear_cuerpo: los parámetros de las reglas 1, 2, 4, 7, 8 y 9 apagados por default",
          all(p[k].default == v for k, v in nuevos.items()), str({k: p[k].default for k in nuevos}))
    q = inspect.signature(E0.clasificar_paginas).parameters
    check("clasificar_paginas: la regla 3 apagada por default", q["continuacion_con_titulo"].default is False)
    r = inspect.signature(E0.separar_encabezado_pie).parameters
    check("separar_encabezado_pie: la regla 1 apagada por default",
          r["seccion_variante"].default is False and r["seccion_abierta"].default is None)


def test_s0_casos(d: Path) -> None:
    print(f"== k) S0 de U-SEG-OFICIAL: un caso medido por regla (e0-r2 sobre {len(TOS_S0)} TOs)")
    correr_e0.correr(d, manifiesto=_ManifiestoParticion(TOS_S0), version_e0="e0-r2")
    ch = {to: cargar(d, f"chunks_{to}.json") for to in TOS_S0}
    ids = {to: [c["id"] for c in ch[to]] for to in TOS_S0}
    est = {to: cargar(d, f"estructura_{to}.json") for to in TOS_S0}

    def avisos(to: str, tipo: str) -> list:
        return [x for x in est[to]["avisos"] if x["tipo"] == tipo]

    check("regla 1: garopt abre «Sección 2 –» y sus puntos (garopt::2.1.1)",
          "garopt::2.1.1" in ids["garopt"], f"{len(ids['garopt'])} chunks")
    check("regla 2: ri_dsf no lee como puntos los códigos de actividad de la sección 10 (sin ri_dsf::10.1)",
          "ri_dsf::10.1" not in ids["ri_dsf"]
          and any(r["motivo"] == "fila_de_lista_de_codigos_r2" for r in est["ri_dsf"]["rechazos_header"]))
    check("regla 3: venliq recupera la primera página de cuerpo (venliq::1.1.1, sin chapeau de S1)",
          "venliq::1.1.1" in ids["venliq"] and "venliq::S1::chapeau_seccion" not in ids["venliq"])
    check("regla 3, ampliación: adfsp p. 3 (una lista entera de la regla 8) es índice: sin adfsp::S6",
          "adfsp::S6" not in ids["adfsp"] and "adfsp::6.1" in ids["adfsp"])
    # desde S0-4, la regla 4b junta al título el renglón que completa los de B.1 y B.3 y retira sus dos intros de un
    # renglón: 93 unidades (95 en S0-2 y S0-3)
    check("regla 4: ri_spi en 93 unidades por el marcador de letra (ri_spi::A.1.1)",
          len(ids["ri_spi"]) == 93 and "ri_spi::A.1.1" in ids["ri_spi"]
          and bool(avisos("ri_spi", "marcador_letra_r2")), f"{len(ids['ri_spi'])} unidades")
    # desde S0-3, el mecanismo 1a no cierra ri_mmsef 2.2 (su cuerpo está en la columna del rótulo) y la regla 7 ya
    # no actúa ahí; las unidades son las mismas. El caso medido de la reapertura pasa a manori 1.5 (p. 39)
    check("regla 7: manori reabre el padre (manori::1.5.2, aviso padre_reabierto_r2); ri_mmsef::2.2.1 sigue",
          "manori::1.5.2" in ids["manori"] and bool(avisos("manori", "padre_reabierto_r2"))
          and "ri_mmsef::2.2.1" in ids["ri_mmsef"])
    check("acompañamiento T: snp_dd funde tablas partidas en intersticiales",
          bool(avisos("snp_dd", "tabla_fundida_en_un_intersticial_r2")))
    vetos = [r for r in est["manori"]["rechazos_header"] if r["motivo"] == "lista_de_puntos_r8"]
    check("regla 8: manori veta los 10 rótulos de sus listas de sección (pp. 3 y 57) y 1.1.1 encuentra padre",
          len(vetos) == 10 and sorted({r["pagina"] for r in vetos}) == [3, 57] and "manori::1.1.1" in ids["manori"],
          f"{len(vetos)} vetos")
    cat = avisos("rdbcra", "filas_de_catalogo_r9")
    u = next((c for c in ch["rdbcra"] if c["id"] == "rdbcra::11.2.7"), None)
    check("regla 9: rdbcra ancla las 119 filas del catálogo (223 renglones) y acepta rdbcra::11.1.1",
          len(cat) == 1 and (cat[0]["filas"], cat[0]["ancladas"], cat[0]["renglones_movidos"]) == (119, 119, 223)
          and "rdbcra::11.1.1" in ids["rdbcra"])
    check("regla 9: rdbcra::11.2.7 lleva su fila entera, en el orden del PDF",
          u is not None and u["texto"] == "Operaciones de cambio en\n11.2.7. días y horarios no habilita- "
                                        "Alta 200 100\ndos al efecto.")
    cob = cargar(d, "cobertura.json")
    check("cobertura exacta en los nueve TOs", all(cob[to]["cobertura_exacta"] for to in TOS_S0))


def test_s0_sinteticos() -> None:
    E0 = correr_e0.E0
    print("== l) S0 de U-SEG-OFICIAL: casos sintéticos de las reglas 5, 6 y 8")
    check("regla 5: la lista de las 9 páginas de la cola de título estricta",
          correr_e0.COLA_TITULO_ESTRICTA_R5 == {"cirmo3": {19}, "cryl": {27}, "manori": {6}, "ri2_ci": {8, 9, 16, 24},
                                                "snp_cheq": {80}, "snp_mep": {19}})
    pag = [_linea("B.C.R.A.", 1, 30.0), _linea("Sección 3. Normas generales.", 1, 44.0),
           _linea("Las entidades deberán informar el saldo diario.", 1, 56.0)]
    _, _, sec_h = E0.separar_encabezado_pie(pag)
    _, _, sec_e = E0.separar_encabezado_pie(pag, cola_titulo_estricta=True)
    check("regla 5: con la cola estricta, un renglón que no continúa el título es texto de la norma",
          sec_h != sec_e and sec_e == "Sección 3. Normas generales.", f"{sec_h!r} / {sec_e!r}")
    check("regla 6: constantes (tercer escalón 27.214, partes por renglones 10.886, por ítems 13.091)",
          (correr_e0.CAPACIDAD_ESCALON_3_R6, correr_e0.OBJETIVO_PARTES_RENGLONES_R6,
           correr_e0.OBJETIVO_CHARS_PARTE) == (27214, 10886, 13091))
    renglon = "Las entidades financieras deberán cumplir con las disposiciones de esta sección y su anexo."
    grande = _unidad("Título de la sección\n" + "\n".join([renglon] * 330))
    chica = _unidad("Título\n" + "\n".join([renglon] * 220))
    p, info = correr_e0.particionar_por_corte(grande)
    check("regla 6 en E1: una unidad sin ítems sobre el tercer escalón se parte por renglones (partes de 10.886 o menos)",
          p is not None and info.get("renglones_r6") == "sin_items_y_sobre_el_tercer_escalon"
          and max(s["chars_propio"] for s in p) <= 10886, str([s["chars_propio"] for s in p] if p else None))
    p, info = correr_e0.particionar_por_corte(chica)
    check("regla 6 en E1: una unidad sin ítems bajo el tercer escalón no se parte (llega entera al tercer escalón)",
          p is None and info["motivo"] == "sin_items_detectables", str(len(chica["texto"])))
    items = ("Encabezado del punto\n1. Primer ítem corto.\n" + "\n".join([renglon] * 5)
             + "\n2. Segundo ítem largo.\n" + "\n".join([renglon] * 440)
             + "\n3. Tercer ítem corto.\n" + "\n".join([renglon] * 5))
    p, info = correr_e0.particionar_por_corte(_unidad(items, "x::1.1", "punto_terminal"))
    tam = [s["chars_propio"] for s in p] if p else []
    check("regla 6 en E1: solo se parte por renglones el ítem que pasa el tercer escalón",
          info.get("renglones_r6") == "parte_sobre_el_tercer_escalon" and len(tam) == 6
          and tam[0] == tam[-1] + 21 and max(tam[1:-1]) <= 10886, str(tam))
    out, rep = correr_e0.subdividir_unidades_grandes([grande], tope_herencia=correr_e0.TOPE_HERENCIA_E0_R2)
    check("regla 6 en E0 (e0-r2): una unidad sin ítems sobre el umbral se parte por renglones",
          len(out) == 3 and not rep["no_particionables"], str([c["chars_propio"] for c in out]))
    out, rep = correr_e0.subdividir_unidades_grandes([grande])
    check("regla 6 en E0 (legada): la misma unidad queda declarada sin partir",
          len(out) == 1 and rep["no_particionables"][0]["motivo"] == "sin_items_detectables")
    out, rep = correr_e0.subdividir_unidades_grandes([grande], no_partir=frozenset({"x::S1"}),
                                                     tope_herencia=correr_e0.TOPE_HERENCIA_E0_R2)
    check("regla 6 en E0: una unidad con tabla serializada no se parte (declarada)",
          len(out) == 1 and rep["no_particionables"][0]["motivo"] == "tabla_serializada")
    # regla 8: lista en la p. 1 cuyos números reaparecen con su título más adelante, con texto entre punto y punto
    titulos = ["Alcance general.", "Requisitos de información.", "Plazos de presentación."]
    p1 = [_linea("Sección 1. Disposiciones.", 1, 30.0)] + [
        _linea(f"1.{i + 1}. {t}", 1, 50.0 + 14 * i, x0=80.0) for i, t in enumerate(titulos)]
    cuerpo = []
    for i, t in enumerate(titulos):
        cuerpo += [_linea(f"1.{i + 1}. {t}", 2, 50.0 + 70 * i, x0=80.0)] + [
            _linea("Texto de la norma que desarrolla el punto con su contenido propio.", 2, 64.0 + 70 * i + 12 * k)
            for k in range(4)]
    roles = [E0.ROL_CUERPO, E0.ROL_CUERPO]
    check("regla 8: detecta la lista de la p. 1 (sus tres rótulos)",
          E0.lineas_de_listas_r8([p1, cuerpo], roles) == frozenset((1, 50.0 + 14 * i) for i in range(3)))
    otro = [_linea(f"1.{i + 1}. {t}", 2, 50.0 + 70 * i, x0=80.0) for i, t in
            enumerate(["Otra cosa.", "Distinto título.", "Nada que ver."])]
    check("regla 8: si los títulos de la reaparición son otros, no es una lista",
          E0.lineas_de_listas_r8([p1, otro], roles) == frozenset())
    check("regla 3, ampliación: la página que es entera la lista pasa a índice; la de cuerpo, no",
          E0.paginas_indice_r8([p1, cuerpo], roles) == [E0.ROL_INDICE, E0.ROL_CUERPO])


TOS_S03 = ("nmcief", "seggar", "ri_tar", "ri2_ae", "fimipyme", "ri2_ci", "ri_ai", "seguef")


def test_s03_legada() -> None:
    import inspect
    E0 = correr_e0.E0
    print("== n) S0-3 de U-SEG-OFICIAL: la versión legada no cambia")
    p = inspect.signature(E0.parsear_cuerpo).parameters
    check("parsear_cuerpo: los mecanismos 1, 2 y 5 apagados por default",
          all(p[k].default == frozenset() for k in ("formas_m1", "formas_m2", "formas_m5")))
    r = inspect.signature(E0.separar_encabezado_pie).parameters
    check("separar_encabezado_pie: las tres formas del mecanismo 5 apagadas por default",
          not any(r[k].default for k in ("cierre_m5", "cola_m5", "zona6_m5")))
    q = inspect.signature(E0.lineas_de_listas_r8).parameters
    s = inspect.signature(E0.construir_chunks).parameters
    check("lineas_de_listas_r8: el mecanismo 3 apagado por default; construir_chunks ya no tiene el mecanismo 4",
          q["forma4_m3"].default is False and "titulo_texto_m4" not in s)


def _parse(paginas, **kw):
    E0 = correr_e0.E0
    roles = [E0.ROL_CUERPO] * len(paginas)
    res = E0.parsear_cuerpo("x", "x.pdf", paginas, roles, mayusculas_repetidas=set(), pie_desde_version=True, **kw)
    return res, E0.construir_chunks(res)


def _texto(chunks, uid):
    return next((c["texto"] for c in chunks if c["id"] == uid), None)


def test_s03_sinteticos() -> None:
    E0 = correr_e0.E0
    print("== o) S0-3 de U-SEG-OFICIAL: casos sintéticos de los cinco mecanismos")
    largo = "Texto de la norma que corre en la columna del rótulo y ocupa un renglón entero de prosa."
    # mecanismo 1, forma a: diseño plano (rótulos y cuerpo en la misma columna)
    p = [_linea("Sección 1. Criterios generales.", 1, 30.0),
         _linea("1.1. Criterios de imputación.", 1, 50.0), _linea(largo, 1, 64.0),
         _linea("1.1.1. Baja en cuentas.", 1, 90.0), _linea(largo, 1, 104.0), _linea(largo, 1, 118.0),
         _linea("1.1.2. Medición.", 1, 140.0), _linea(largo, 1, 154.0)]
    _, ch_h = _parse([p])
    _, ch_a = _parse([p], formas_m1=frozenset({"a"}))
    check("mecanismo 1a: la prosa que sigue al rótulo en su columna es cuerpo del punto (x::1.1.1, x::1.1.2)",
          _texto(ch_a, "x::1.1.1") == "1.1.1. Baja en cuentas.\n" + largo + "\n" + largo
          and _texto(ch_a, "x::1.1.2") == "1.1.2. Medición.\n" + largo
          and _texto(ch_h, "x::1.1.1") == "1.1.1. Baja en cuentas.",
          str([c["id"] for c in ch_a]))
    # guarda: lista de ítems de un renglón; la prosa que sigue al último es el cierre del padre
    q = [_linea("Sección 1. Aportes.", 1, 30.0), _linea("1.1. Aportes de capital.", 1, 50.0),
         _linea(largo, 1, 64.0), _linea("1.1.1. títulos valores públicos nacionales;", 1, 90.0),
         _linea("1.1.2. instrumentos de regulación monetaria;", 1, 104.0),
         _linea("1.1.3. depósitos de la entidad.", 1, 118.0), _linea(largo, 1, 132.0)]
    _, ch_q = _parse([q], formas_m1=frozenset({"a"}))
    check("mecanismo 1a, guarda: tras una lista de renglones sueltos, la prosa sigue siendo el cierre del padre",
          _texto(ch_q, "x::1.1::cierre") == largo and _texto(ch_q, "x::1.1.3") == "1.1.3. depósitos de la entidad.")
    # guarda: sangría colgante (el cuerpo de un hermano corre más adentro que su rótulo)
    g = [_linea("Sección 2. Excepciones.", 1, 30.0), _linea("2.7. Excepción.", 1, 50.0, x0=60.0),
         _linea(largo, 1, 64.0, x0=80.0),
         _linea("2.7.1. El ejercicio de la excepción se efectúe dentro del plazo previsto para la", 1, 90.0, x0=80.0),
         _linea("liquidación de los fondos.", 1, 104.0, x0=100.0),
         _linea("2.7.2. La utilización de este mecanismo deberá resultar neutral.", 1, 118.0, x0=80.0),
         _linea(largo, 1, 132.0, x0=80.0)]
    _, ch_g = _parse([g], formas_m1=frozenset({"a"}))
    check("mecanismo 1a, guarda: con sangría colgante, la prosa a la altura del rótulo es del padre (cierre del 2.7)",
          _texto(ch_g, "x::2.7::cierre") == largo)
    # mecanismo 1, forma b: el cuerpo del punto corre a la izquierda de su rótulo
    b = [_linea("Sección 7. Diseño de registros.", 1, 30.0), _linea("7.1. Registros.", 1, 50.0, x0=40.0),
         _linea(largo, 1, 64.0, x0=56.0), _linea("7.1.1. Registro de cabecera.", 1, 90.0, x0=64.0),
         _linea("Campo 1 2 3", 1, 104.0, x0=48.0), _linea("1. Identificador de registro", 1, 118.0, x0=42.0),
         _linea(largo, 1, 132.0, x0=57.0)]
    _, ch_b0 = _parse([b])
    _, ch_b = _parse([b], formas_m1=frozenset({"b"}))
    check("mecanismo 1b: un punto con el cuerpo a la izquierda de su rótulo no devuelve prosa al padre",
          largo in (_texto(ch_b, "x::7.1.1") or "") and largo not in (_texto(ch_b0, "x::7.1.1") or ""))
    # mecanismo 2 (modo sin raíz): las tres formas de la línea que abre una raíz
    m2 = [_linea("1. Fideicomiso accionista.", 1, 50.0, x0=70.0), _linea(largo, 1, 64.0, x0=90.0),
          _linea("2.Integración de los aportes.", 1, 90.0, x0=70.0), _linea(largo, 1, 104.0, x0=90.0),
          _linea("3- DISPOSICIONES FINALES", 1, 130.0, x0=70.0), _linea(largo, 1, 144.0, x0=90.0),
          _linea("4. CUADRO 1 – DATOS DE LAS CUENTAS", 1, 170.0, x0=85.0), _linea(largo, 1, 184.0, x0=90.0)]
    r0, _ = _parse([m2], modo_sin_raiz=True)
    r2, _ = _parse([m2], modo_sin_raiz=True, formas_m2=frozenset({"a", "b", "c"}))
    check("mecanismo 2: sin las formas, la raíz 1 sola; con a, b y c, las raíces 1 a 4",
          [s.numero for s in r0.secciones] == ["1"] and [s.numero for s in r2.secciones] == ["1", "2", "3", "4"],
          f"{[s.numero for s in r0.secciones]} / {[s.numero for s in r2.secciones]}")
    check("mecanismo 2: cada raíz nueva declarada por su forma (aviso raiz_m2)",
          [(a["numero"], a["forma"]) for a in r2.avisos if a["tipo"] == "raiz_m2"] == [("2", "a"), ("3", "b"), ("4", "c")])
    # mecanismo 3: lista de rótulos de un nivel (índice de un anexo) y su página de cuerpo
    titulos = ["Designación.", "Condiciones para el ejercicio.", "Exclusión del registro.", "Baja del registro."]
    p1 = [_linea("DISPOSICIONES GENERALES", 1, 40.0)] + [
        _linea(f"{i + 1}. {t.rstrip('.')}", 1, 60.0 + 20 * i, x0=76.0, ngaps=1) for i, t in enumerate(titulos)]
    p2 = []
    for i, t in enumerate(titulos):
        p2 += [_linea(f"{i + 1}. {t}", 2, 50.0 + 70 * i, x0=76.0)] + [
            _linea(largo, 2, 64.0 + 70 * i + 12 * k, x0=90.0) for k in range(4)]
    roles = [E0.ROL_CUERPO, E0.ROL_CUERPO]
    check("mecanismo 3: sin la cuarta forma, la lista de un nivel no se detecta; con ella, sí, y la página es índice",
          E0.lineas_de_listas_r8([p1, p2], roles) == frozenset()
          and E0.lineas_de_listas_r8([p1, p2], roles, forma4_m3=True) == frozenset((1, 60.0 + 20 * i) for i in range(4))
          and E0.paginas_indice_r8([p1, p2], roles, forma4_m3=True) == [E0.ROL_INDICE, E0.ROL_CUERPO])
    # mecanismo 5: la zona de encabezado
    enc = [_linea("LÍNEA DE FINANCIAMIENTO", 1, 72.0, x0=220.0), _linea("B.C.R.A. PRODUCTIVA", 1, 85.0, x0=83.0),
           _linea("Sección 1. Entidades alcanzadas.", 1, 98.0, x0=139.0),
           _linea("Las entidades financieras que estén comprendidas en el Grupo A conforme a lo previsto en la",
                  1, 124.0, x0=76.0),
           _linea("Sección 4. de las normas sobre autoridades, para lo cual el indicador del", 1, 137.0, x0=76.0),
           _linea("punto 4.1. de esas normas deberá computarse.", 1, 150.0, x0=76.0)]
    c0, _, _ = E0.separar_encabezado_pie(enc, mayusculas_repetidas=set())
    ca, _, _ = E0.separar_encabezado_pie(enc, mayusculas_repetidas=set(), cierre_m5=True)
    check("mecanismo 5a: una segunda línea de sección que no se repite no cierra el encabezado",
          c0[0].texto.startswith("punto 4.1.") and ca[0].texto.startswith("Las entidades financieras"))
    bc = [_linea("REGIMEN INFORMATIVO", 1, 72.0, x0=259.0), _linea("B.C.R.A. CAJAS DE CRÉDITO", 1, 87.0, x0=91.0),
          _linea("Sección 3. Capitales Mínimos", 1, 103.0, x0=152.0),
          _linea("4. Facilidades Otorgadas por el B.C.R.A.", 1, 128.0, x0=76.0),
          _linea("4.1. Normas de procedimiento", 1, 166.0, x0=90.0)]
    b0, _, _ = E0.separar_encabezado_pie(bc, mayusculas_repetidas=set())
    ba, _, _ = E0.separar_encabezado_pie(bc, mayusculas_repetidas=set(), cierre_m5=True)
    check("mecanismo 5a: después de la sección, un renglón con «B.C.R.A.» que no se repite es texto",
          b0[0].texto.startswith("4.1.") and ba[0].texto.startswith("4. Facilidades"))
    cola = [_linea("NORMAS MINIMAS", 1, 76.0, x0=143.0), _linea("B.C.R.A. DE CAMBIO", 1, 89.0, x0=83.0),
            _linea("Sección 1. Aspectos generales", 1, 102.0, x0=139.0),
            _linea("abordando las expectativas, las responsabilidades de los indivi-", 1, 116.0, x0=184.0),
            _linea("duos y grupos, teniendo en cuenta la clasificación y confidenciali-", 1, 130.0, x0=184.0),
            _linea("dad de la información.", 1, 144.0, x0=184.0)]
    k0, _, _ = E0.separar_encabezado_pie(cola, mayusculas_repetidas=set())
    kb, _, _ = E0.separar_encabezado_pie(cola, mayusculas_repetidas=set(), cola_m5=True)
    check("mecanismo 5b: un renglón en la columna del cuerpo, seguido de otro a interlineado, no es cola del título",
          k0[0].texto.startswith("dad de") and kb[0].texto.startswith("abordando"))
    real = [_linea("TEXTO ORDENADO", 1, 76.0, x0=200.0), _linea("B.C.R.A.", 1, 89.0, x0=83.0),
            _linea("Sección 5. Garantía de los depósitos y Superintendencia de Entidades Financieras y", 1, 102.0,
                   x0=139.0), _linea("Cambiarias.", 1, 115.0, x0=139.0),
            _linea("5.1. Depósitos comprendidos.", 1, 140.0, x0=76.0)]
    _, _, sec_r = E0.separar_encabezado_pie(real, mayusculas_repetidas=set(), cola_m5=True)
    inc = [_linea("B.C.R.A.", 1, 89.0, x0=83.0), _linea("Sección 7. Diseño de registros", 1, 102.0, x0=139.0),
           _linea("ii) Cabecera de lote", 1, 115.0, x0=175.0), _linea(largo, 1, 140.0, x0=76.0)]
    i0, _, _ = E0.separar_encabezado_pie(inc, mayusculas_repetidas=set())
    ib, _, _ = E0.separar_encabezado_pie(inc, mayusculas_repetidas=set(), cola_m5=True)
    check("mecanismo 5b: la cola real del título sigue siéndolo; un inciso «ii)» no es cola",
          sec_r.endswith("Cambiarias.") and i0[0].texto == largo and ib[0].texto == "ii) Cabecera de lote")
    ai = [_linea("REGIMEN INFORMATIVO CONTABLE MENSUAL", 1, 80.0, x0=242.0),
          _linea("6. TEXTO ORDENADO DEL REGIMEN INFORMATIVO", 1, 93.0, x0=189.0),
          _linea("SOBRE LA RELACION PARA LOS ACTIVOS INMOVILIZADOS", 1, 105.0, x0=183.0),
          _linea("B.C.R.A.", 1, 108.0, x0=98.0), _linea("CONCEPTOS. (R.I. – A.I.)", 1, 118.0, x0=302.0),
          _linea("Sección 2. Instrucciones generales", 1, 131.0, x0=172.0),
          _linea("2.1. La información tendrá frecuencia mensual.", 1, 198.0, x0=112.0)]
    _, _, s0 = E0.separar_encabezado_pie(ai, mayusculas_repetidas=set())
    zc, _, sc = E0.separar_encabezado_pie(ai, mayusculas_repetidas=set(), zona6_m5=True)
    check("mecanismo 5c: con el recuadro en los cinco primeros renglones, la sección del sexto se abre",
          s0 is None and sc == "Sección 2. Instrucciones generales" and zc[0].texto.startswith("2.1."))


def test_s03_casos(d: Path) -> None:
    print(f"== p) S0-3 de U-SEG-OFICIAL: un caso medido por mecanismo (e0-r2 sobre {len(TOS_S03)} TOs y ri_dcpc)")
    correr_e0.correr(d, manifiesto=_ManifiestoParticion(TOS_S03 + ("ri_dcpc",)), version_e0="e0-r2")
    ch = {to: cargar(d, f"chunks_{to}.json") for to in TOS_S03 + ("ri_dcpc",)}

    def txt(to: str, uid: str) -> str:
        return next((c["texto"] for c in ch[to] if c["id"] == uid), "")

    check("mecanismo 1a: ri_dcpc::3.1.1 lleva su cuerpo («A los fines de aplicar…»)",
          "A los fines de aplicar las disposiciones de baja" in txt("ri_dcpc", "ri_dcpc::3.1.1"))
    # desde S0-4, el punto es del Anexo II de nmcief (regla de sub-documento): nmcief::A2::3.2.1
    check("mecanismo 1a: nmcief::A2::3.2.1 lleva su cuerpo («El sistema contable constituye…»)",
          "El sistema contable constituye" in txt("nmcief", "nmcief::A2::3.2.1"))
    check("mecanismo 2a: seggar abre la sección 4 («4.Integración de los aportes.») y el cierre de S3 ya no la lleva",
          "Los aportes normales" in txt("seggar", "seggar::S4")
          and "Integración" not in txt("seggar", "seggar::S3::cierre"))
    check("mecanismo 2c: ri_tar abre los cuadros (ri_tar::2.1.1) y ri_tar::1.1 ya no se lleva el documento",
          bool(txt("ri_tar", "ri_tar::2.1.1")) and "CUADRO 1" not in txt("ri_tar", "ri_tar::1.1"))
    pies = cargar(d, "pies_ri2_ae.json")
    check("mecanismo 3: ri2_ae p. 3 es índice y ri2_ae::S1 es la sección 1 del cuerpo",
          next(f["rol"] for f in pies["paginas_detalle"] if f["pagina"] == 3) == "indice"
          and "deberán informar a la Gerencia de Control" in txt("ri2_ae", "ri2_ae::S1"))
    check("regla 4a de S0-4 (el caso del mecanismo 4 de S0-3): seguef::2.1.6::intro empieza en su rótulo",
          txt("seguef", "seguef::2.1.6::intro").startswith("2.1.6. Cuando se decida"))
    check("mecanismo 5a: fimipyme::S1 lleva el comienzo de su párrafo («Las entidades financieras que estén…»)",
          "Las entidades financieras que estén comprendidas" in txt("fimipyme", "fimipyme::S1"))
    check("mecanismo 5b: ri2_ci::1.1.1.4 lleva sus dos renglones («abordando las expectativas…»)",
          "abordando las expectativas" in txt("ri2_ci", "ri2_ci::1.1.1.4"))
    check("mecanismo 5c: ri_ai abre la sección 2 (ri_ai::2.1) y ri_ai::1.2.2 ya no la lleva",
          bool(txt("ri_ai", "ri_ai::2.1")) and "Sección 2." not in txt("ri_ai", "ri_ai::1.2.2"))
    cob = cargar(d, "cobertura.json")
    check("cobertura exacta en los nueve TOs", all(cob[to]["cobertura_exacta"] for to in TOS_S03 + ("ri_dcpc",)))


TOS_S04 = ("ri_sef", "nmcief", "ri_ccna", "ri_icpipsp", "ri_cc", "ri_ai", "efemin", "ri_oc")
TOS_TANDA0 = frozenset({"cap", "cla", "ext", "pro", "ric", "ctacte", "lingob", "polcre", "pagjub", "docvig"})


def test_s04_legada() -> None:
    import inspect
    E0 = correr_e0.E0
    print("== q) S0-4 de U-SEG-OFICIAL: la versión legada no cambia; listas de TOs")
    p = inspect.signature(E0.parsear_cuerpo).parameters
    check("parsear_cuerpo: sub-documento, sdg3, sdmax, las reglas de letra y apartados apagados por default",
          p["subdocumentos"].default is None and p["g3_subdoc"].default is False
          and p["raiz_max_subdoc"].default is False and p["apartados_seccion"].default is False
          and p["letra_corte"].default is False and p["letra_herencia"].default is False
          and p["letra_numero"].default is False)
    ls = inspect.signature(E0.limites_subdocumento).parameters
    check("limites_subdocumento: forma de letra y régimen de la página 1 apagados por default",
          ls["letras"].default is False and ls["sin_regimen_pagina_1"].default is False)
    s = inspect.signature(E0.construir_chunks).parameters
    check("construir_chunks: 4a y 4b apagadas por default",
          s["oracion_titulo_4a"].default is False and s["titulo_envuelto_4b"].default is False)
    check("listas de S0-4: sub-documento en los cinco TOs del diseño (sin ri_tsa ni ri2_pm), apartados en ri_ai, "
          "4a y 4b fuera de la tanda 0, y el mecanismo 4 de S0-3 fuera de las reglas",
          correr_e0.TOS_SUBDOCUMENTO_S0_4 == frozenset({"ri_sef", "nmcief", "ri_ccna", "ri_icpipsp", "ri_cc"})
          and correr_e0.TOS_APARTADOS_S0_4 == frozenset({"ri_ai"})
          and correr_e0.TOS_TANDA0_SIN_4AB == TOS_TANDA0
          and "m4" not in correr_e0.REGLAS_S0_3
          and correr_e0.REGLAS_S0_4 == frozenset({"sd", "sdg3", "sdmax", "sdr1", "apl", "sdl", "sdlh", "sdla", "4a",
                                                  "4b", "ap"})
          and correr_e0.TOS_SUBDOCUMENTO_R1_S0_4 == frozenset({"ri_oc"})
          and correr_e0.TOS_APARTADO_LETRA_S0_4 == frozenset({"ri_oc"})
          and correr_e0.TOS_LETRA_S0_4 == frozenset({"ri_ccna"}))


def _enc(pagina: int, *extra):
    """Zona de encabezado de una página sintética: título del TO, «B.C.R.A.» y los renglones extra."""
    out = [_linea("NORMAS MINIMAS DE PRUEBA", pagina, 72.0, x0=200.0), _linea("B.C.R.A.", pagina, 85.0, x0=83.0)]
    for k, t in enumerate(extra):
        out.append(_linea(t, pagina, 98.0 + 13 * k, x0=140.0))
    return out


def test_s04_sinteticos() -> None:
    E0 = correr_e0.E0
    print("== r) S0-4 de U-SEG-OFICIAL: casos sintéticos")
    largo = "Texto de la norma que corre en la columna del cuerpo y ocupa un renglón entero de prosa."
    # detección: anexo en el encabezado, partes I y II, anexo repetido, anexo II con una parte suelta, serie de letras
    pags = [
        _enc(1, "ANEXO I") + [_linea("I.- CONCEPTOS BÁSICOS", 1, 130.0, x0=76.0),
                              _linea("1. Control interno.", 1, 150.0), _linea(largo, 1, 164.0, x0=90.0)],
        _enc(2, "ANEXO I") + [_linea("II.- COMITÉ DE AUDITORÍA", 2, 130.0, x0=76.0),
                              _linea("1. Integración.", 2, 150.0), _linea(largo, 2, 164.0, x0=90.0)],
        _enc(3, "Anexo II") + [_linea("I. Bienes diversos", 3, 130.0, x0=76.0), _linea(largo, 3, 150.0, x0=90.0)],
        _enc(4, "ANEXO H") + [_linea(largo, 4, 130.0, x0=90.0)],
        _enc(5, "ANEXO I") + [_linea(largo, 5, 130.0, x0=90.0)]]
    roles = [E0.ROL_CUERPO] * len(pags)
    lim = E0.limites_subdocumento(pags, roles)
    check("sub-documento: anexo I con sus partes I y II, anexo II; el anexo repetido, la parte suelta y la serie de "
          "letras («ANEXO I» tras «ANEXO H») no abren sub-documento",
          [(d["prefijo"], d["forma"], d["padre"]) for d in lim]
          == [("A1", "anexo", None), ("A1P1", "parte", "A1"), ("A1P2", "parte", "A1"), ("A2", "anexo", None)],
          str([(d["prefijo"], d["forma"]) for d in lim]))
    # régimen, formulario (con su continuación) y circular (y la circular suelta de otro anexo)
    reg = [_enc(1, "4 - REGULACIONES Y RELACIONES TÉCNICAS") + [_linea(largo, 1, 130.0)],
           _enc(2, "5– PREVENCION DEL LAVADO DE DINERO") + [_linea(largo, 2, 130.0)],
           [_linea("RÉGIMEN INFORMATIVO PARA PUBLICACIÓN", 3, 72.0, x0=200.0),
            _linea("PARA CAJAS DE CRÉDITO (R.I. – P.)", 3, 84.0, x0=258.0), _linea(largo, 3, 130.0)]]
    check("sub-documento: régimen por «N - TÍTULO» y por la sigla «(R.I. – P.)»",
          [d["prefijo"] for d in E0.limites_subdocumento(reg, [E0.ROL_CUERPO] * 3)] == ["R4", "R5", "RIP"])
    form = [_enc(1, "ANEXO I") + [_linea("1. Toma de conocimiento.", 1, 130.0)],
            [_linea("BANCO CENTRAL DE LA REPÚBLICA ARGENTINA", 2, 72.0), _linea("DECLARACIÓN JURADA", 2, 84.0),
             _linea("1. No soy socio de la entidad.", 2, 130.0)],
            [_linea("SOLICITUD Cont. 2", 3, 70.0), _linea("BANCO CENTRAL DE LA REPUBLICA ARGENTINA", 3, 75.0),
             _linea(largo, 3, 130.0)],
            [_linea("BANCO CENTRAL DE LA REPÚBLICA ARGENTINA", 4, 72.0), _linea("SOLICITUD DE INSCRIPCIÓN", 4, 84.0),
             _linea(largo, 4, 130.0)]]
    check("sub-documento: formulario por el membrete; la página con «Cont. 2» sigue el formulario anterior",
          [d["prefijo"] for d in E0.limites_subdocumento(form, [E0.ROL_CUERPO] * 4)] == ["A1", "F1", "F2"])
    circ = [_enc(1, "ANEXO I") + [_linea("Circular SINAP 1. Sistema Nacional de Pagos", 1, 130.0),
                                  _linea("1. Exclusiones - Corroborar.", 1, 150.0),
                                  _linea("Circular CONAU 1. Régimen Informativo", 1, 170.0),
                                  _linea("1. Proveedores de servicios.", 1, 190.0)],
            _enc(2, "ANEXO II") + [_linea("Circular RUNOR 1. Protección de los usuarios", 2, 130.0)]]
    check("sub-documento: dos circulares en el mismo anexo abren C1 y C2; una suelta no",
          [d["prefijo"] for d in E0.limites_subdocumento(circ, [E0.ROL_CUERPO] * 2)] == ["A1", "A1C1", "A1C2", "A2"])
    # lectura con sub-documentos (modo sin raíz): prefijo, numeración desde cero y herencia del rótulo
    sd = [[_linea("Preámbulo de la norma con su texto corrido en la columna del cuerpo de la página.", 1, 100.0),
           _linea("I. Información solicitada", 1, 130.0, x0=76.0), _linea("1. Tipo de trámite.", 1, 150.0, x0=76.0),
           _linea(largo, 1, 164.0, x0=90.0), _linea("2. Etapa del trámite.", 1, 190.0, x0=76.0),
           _linea(largo, 1, 204.0, x0=90.0)],
          [_linea("II. Otras informaciones.", 2, 100.0, x0=76.0),
           _linea("1. Información adicional.", 2, 130.0, x0=76.0), _linea(largo, 2, 144.0, x0=90.0)]]
    rs = [E0.ROL_CUERPO] * 2
    lim_sd = E0.limites_subdocumento(sd, rs)
    r0 = E0.parsear_cuerpo("x", "x.pdf", sd, rs, modo_sin_raiz=True, mayusculas_repetidas=set())
    r1 = E0.parsear_cuerpo("x", "x.pdf", sd, rs, modo_sin_raiz=True, mayusculas_repetidas=set(),
                           subdocumentos=lim_sd)
    ch0 = {c["id"]: c for c in E0.construir_chunks(r0)}
    ch1 = {c["id"]: c for c in E0.construir_chunks(r1)}
    check("sub-documento: sin la regla, la parte II queda dentro del ítem 2; con ella, cada parte con su espacio "
          "de ids",
          "x::S2" in ch0 and "II. Otras informaciones." in ch0["x::S2"]["texto"]
          and set(ch1) == {"x::S0", "x::P1::S0", "x::P1::S1", "x::P1::S2", "x::P2::S0", "x::P2::S1"},
          str(sorted(ch1)))
    check("sub-documento: la unidad hereda el rótulo de su sub-documento; la raíz «0» no se hereda a sí misma",
          ch1["x::P2::S1"]["herencia"][0]["texto"] == "II. Otras informaciones."
          and ch1["x::P2::S1"]["herencia"][0]["unidad_origen"] == "P2"
          and ch1["x::P2::S0"]["herencia"] == [] and ch1["x::P2::S0"]["texto"].startswith("II. Otras"))
    cob = E0.verificar_cobertura(r1)
    check("sub-documento: cobertura exacta", cob["cobertura_exacta"], str(cob))
    # sdg3: dentro de un sub-documento, la raíz que sucede exactamente a la anterior y está más adentro
    g = [[_linea("I. Comité", 1, 100.0, x0=76.0), _linea("1. Integración.", 1, 120.0, x0=76.0),
          _linea(largo, 1, 134.0, x0=100.0), _linea("2. Periodicidad de las reuniones", 1, 160.0, x0=86.0),
          _linea(largo, 1, 174.0, x0=100.0)],
         [_linea("II. Auditoría", 2, 100.0, x0=76.0), _linea(largo, 2, 120.0, x0=100.0)]]
    lg = E0.limites_subdocumento(g, [E0.ROL_CUERPO] * 2)
    sin = E0.parsear_cuerpo("x", "x.pdf", g, [E0.ROL_CUERPO] * 2, modo_sin_raiz=True, mayusculas_repetidas=set(),
                            subdocumentos=lg)
    con = E0.parsear_cuerpo("x", "x.pdf", g, [E0.ROL_CUERPO] * 2, modo_sin_raiz=True, mayusculas_repetidas=set(),
                            subdocumentos=lg, g3_subdoc=True)
    check("sdg3: sin la guarda nueva, la raíz 2 (10 pt más adentro) se rechaza; con ella, se abre y se declara",
          [s.numero for s in sin.secciones if s.prefijo == "P1"] == ["0", "1"]
          and [s.numero for s in con.secciones if s.prefijo == "P1"] == ["0", "1", "2"]
          and any(a["tipo"] == "raiz_g3_subdocumento_sd" for a in con.avisos))
    # sdmax (S0-4a-bis): dentro de un sub-documento, la raíz mayor que MAX_RAIZ que sucede exactamente a la anterior
    items = [_linea("I. Procedimientos mínimos", 1, 60.0, x0=76.0)]
    for k in list(range(1, 32)) + [33]:
        items.append(_linea(f"{k}. Revisión del rubro {k} de los estados contables.", 1, 80.0 + 14 * k, x0=76.0))
    mx = [items, [_linea("II. Códigos de actividad", 2, 60.0, x0=76.0),
                  _linea("101. Estación de servicio", 2, 80.0, x0=76.0), _linea(largo, 2, 94.0, x0=90.0)]]
    lmx = E0.limites_subdocumento(mx, [E0.ROL_CUERPO] * 2)
    kmx = dict(modo_sin_raiz=True, mayusculas_repetidas=set())
    sin_mx = E0.parsear_cuerpo("x", "x.pdf", mx, [E0.ROL_CUERPO] * 2, subdocumentos=lmx, **kmx)
    con_mx = E0.parsear_cuerpo("x", "x.pdf", mx, [E0.ROL_CUERPO] * 2, subdocumentos=lmx, raiz_max_subdoc=True, **kmx)
    fuera = E0.parsear_cuerpo("x", "x.pdf", mx, [E0.ROL_CUERPO] * 2, raiz_max_subdoc=True, **kmx)
    raices_p1 = [s.numero for s in con_mx.secciones if s.prefijo == "P1"]
    rech = [r["texto"].split()[0] for r in con_mx.rechazos_header if r["motivo"] == "raiz_mayor_a_max"]
    check("sdmax: sin la regla, la raíz 31 se rechaza por MAX_RAIZ; con ella, se abre la 31 (sucede a la 30) y no "
          "la 33 ni el código 101 de la parte II; fuera de un sub-documento no corre",
          [s.numero for s in sin_mx.secciones if s.prefijo == "P1"][-1] == "30" and raices_p1[-1] == "31"
          and len(raices_p1) == 32 and rech == ["33.", "101."]
          and [a["numero"] for a in con_mx.avisos if a["tipo"] == "raiz_mayor_a_max_subdocumento_sdmax"] == ["31"]
          and not any(a["tipo"] == "raiz_mayor_a_max_subdocumento_sdmax" for a in fuera.avisos),
          str((raices_p1[-3:], rech)))
    # S0-4a-ter, sdr1: el régimen de la página 1 es el del TO (y su encabezado corrido en las páginas siguientes)
    r1 = [_enc(1, "10 – OPERACIONES DE CAMBIOS") + [_linea(largo, 1, 130.0)],
          _enc(2, "10 – OPERACIONES DE CAMBIOS") + [_linea(largo, 2, 130.0)],
          _enc(3, "10 – OPERACIONES DE CAMBIOS", "ANEXO I: Códigos de instrumentos") + [_linea(largo, 3, 150.0)]]
    sin_r1 = E0.limites_subdocumento(r1, [E0.ROL_CUERPO] * 3)
    con_r1 = E0.limites_subdocumento(r1, [E0.ROL_CUERPO] * 3, sin_regimen_pagina_1=True)
    check("sdr1: sin la regla, el régimen de la página 1 prefija el anexo (R10, R10A1); con ella, solo el anexo, "
          "sin padre",
          [(d["prefijo"], d["padre"]) for d in sin_r1] == [("R10", None), ("R10A1", "R10")]
          and [(d["prefijo"], d["padre"]) for d in con_r1] == [("A1", None)], str((sin_r1, con_r1)))
    # S0-4a-ter, apl: apartados de letra en una lectura sin raíz que también tiene raíces numéricas
    ap_l = [[_linea("APARTADO A: OPERACIONES DE CAMBIOS", 1, 100.0, x0=77.0),
             _linea("1. Instrucciones generales.", 1, 120.0, x0=77.0), _linea(largo, 1, 134.0, x0=85.0),
             _linea("1.1. Para las operaciones de compra.", 1, 150.0, x0=85.0), _linea(largo, 1, 164.0, x0=98.0),
             _linea("APARTADO B: POSICIÓN GENERAL DE CAMBIOS", 1, 190.0, x0=76.0),
             _linea("B.1. Variación Diaria", 1, 210.0, x0=76.0),
             _linea("B.1.1. Posición General de Cambios al cierre del día anterior", 1, 230.0, x0=112.0),
             _linea("B.1.2. Compras concertadas de billetes y divisas con clientes.", 1, 244.0, x0=112.0)]]
    kl = dict(modo_sin_raiz=True, mayusculas_repetidas=set())
    ch_l0 = {c["id"]: c for c in E0.construir_chunks(E0.parsear_cuerpo("x", "x.pdf", ap_l, [E0.ROL_CUERPO], **kl))}
    ch_l1 = {c["id"]: c for c in E0.construir_chunks(E0.parsear_cuerpo("x", "x.pdf", ap_l, [E0.ROL_CUERPO],
                                                                        marcador_letra=True, **kl))}
    check("apl: sin el marcador, el Apartado B queda dentro del punto 1.1; con él, «APARTADO B:» cierra la raíz 1 y "
          "B.1.1 y B.1.2 son puntos de B, con la raíz 1 y su 1.1 como estaban",
          "APARTADO B" in ch_l0.get("x::1.1", {}).get("texto", "") and "x::B.1.1" not in ch_l0
          and {"x::B.1.1", "x::B.1.2", "x::1.1"} <= set(ch_l1) and "APARTADO B" not in ch_l1["x::1.1"]["texto"]
          and [h["unidad_origen"] for h in ch_l1["x::B.1.1"]["herencia"]] == ["SB", "B.1"], str(sorted(ch_l1)))
    # S0-4a-ter, sdl, sdlh y sdla: el Anexo III de ri_ccna en chico
    lt = [_enc(1, "ANEXO I") + [_linea("A. GENERAL", 1, 120.0, x0=115.0),
                                _linea("A.1. PRUEBAS DE CUMPLIMIENTO DEL CONTROL INTERNO.", 1, 134.0, x0=149.0),
                                _linea(largo, 1, 148.0, x0=149.0),
                                _linea("1. Evaluación de las variaciones del activo.", 1, 170.0, x0=203.0),
                                _linea("2. Evaluación de las variaciones de resultados.", 1, 184.0, x0=203.0),
                                _linea(largo, 1, 198.0, x0=203.0),
                                _linea("A.3. El relevamiento del control interno sirve de base.", 1, 220.0, x0=149.0),
                                _linea("B. PRUEBAS SUSTANTIVAS", 1, 240.0, x0=115.0),
                                _linea("1. Arqueo sorpresivo de las existencias.", 1, 260.0, x0=150.0),
                                _linea("2. Obtención de confirmaciones directas.", 1, 274.0, x0=150.0),
                                _linea("3. Revisión de las conciliaciones bancarias.", 1, 288.0, x0=150.0),
                                _linea("C. Datos de la entidad", 1, 310.0, x0=115.0)]]
    rl = [E0.ROL_CUERPO]
    lim_l = E0.limites_subdocumento(lt, rl, letras=True)
    lim_0 = E0.limites_subdocumento(lt, rl)
    check("sdl: la forma de letra da A1L1 y A1L2 dentro del anexo, con su letra; «C. Datos…» (sin mayúsculas) no",
          [(d["prefijo"], d["forma"], d["padre"], d.get("letra")) for d in lim_l]
          == [("A1", "anexo", None, None), ("A1L1", "letra", "A1", "A"), ("A1L2", "letra", "A1", "B")]
          and [d["prefijo"] for d in lim_0] == ["A1"], str(lim_l))
    serie_b = [_enc(1, "ANEXO I") + [_linea("B. PRUEBAS SUSTANTIVAS", 1, 120.0, x0=115.0),
                                     _linea("C. OTRAS PRUEBAS", 1, 140.0, x0=115.0)]]
    check("sdl, guarda: una serie que no empieza en la A no abre sub-documento de letra",
          [d["prefijo"] for d in E0.limites_subdocumento(serie_b, rl, letras=True)] == ["A1"])

    def _chl(**kw):
        return {c["id"]: c for c in E0.construir_chunks(E0.parsear_cuerpo("x", "x.pdf", lt, rl, subdocumentos=lim_l,
                                                                             **kl, **kw))}
    c0, c_sdl, c_h = _chl(), _chl(letra_corte=True), _chl(letra_herencia=True)
    c_sdl_h, c_a = _chl(letra_corte=True, letra_herencia=True), _chl(letra_numero=True)
    c_todas = _chl(letra_corte=True, letra_herencia=True, letra_numero=True)

    def her(c, uid):
        return [h["texto"] for h in c.get(uid, {}).get("herencia", [])]
    check("sdl: sin la regla, B.1 y B.2 se rechazan (la numeración no reinicia) y quedan en el ítem 2 de A; con "
          "ella, B abre su sub-documento y B.1 a B.3 son sus raíces, sin heredar su rótulo",
          "1. Arqueo" in c0["x::A1::S2"]["texto"] and "x::A1::S3" in c0
          and c_sdl["x::A1L2::S1"]["texto"].startswith("1. Arqueo") and "x::A1L2::S3" in c_sdl
          and "B. PRUEBAS SUSTANTIVAS" not in her(c_sdl, "x::A1L2::S3"), str(sorted(c_sdl)))
    check("sdlh: sin sdl, las raíces abiertas después del rótulo heredan la letra vigente (A1::S1 «A. GENERAL», "
          "A1::S3 «B. PRUEBAS SUSTANTIVAS»), sin otro cambio; con sdl, las del sub-documento de letra heredan su "
          "rótulo",
          her(c_h, "x::A1::S1") == ["ANEXO I", "A. GENERAL"]
          and her(c_h, "x::A1::S3") == ["ANEXO I", "B. PRUEBAS SUSTANTIVAS"]
          and set(c_h) == set(c0) and all(c_h[i]["texto"] == c0[i]["texto"] for i in c0)
          and her(c_sdl_h, "x::A1L2::S3") == ["ANEXO I", "B. PRUEBAS SUSTANTIVAS"])
    check("sdla: «A.3.» con la letra vigente y más afuera que la raíz 2 abre la raíz A.3 (sin sdl, A1::SA.3; con "
          "sdl, A1L1::SA.3), y la raíz 2 ya no la lleva",
          c_a["x::A1::SA.3"]["texto"].startswith("A.3. El relevamiento") and "A.3." not in c_a["x::A1::S2"]["texto"]
          and "A.3." in c0["x::A1::S2"]["texto"]
          and c_todas["x::A1L1::SA.3"]["texto"].startswith("A.3.")
          and "B. PRUEBAS" not in c_todas["x::A1L1::SA.3"]["texto"]
          and her(c_todas, "x::A1L1::SA.3") == ["ANEXO I", "A. GENERAL"], str(sorted(c_todas)))
    cob_l = E0.verificar_cobertura(E0.parsear_cuerpo("x", "x.pdf", lt, rl, subdocumentos=lim_l, letra_corte=True,
                                                     letra_herencia=True, letra_numero=True, **kl))
    check("reglas de letra: cobertura exacta", cob_l["cobertura_exacta"], str(cob_l))
    # 4a: oración tomada como título (el caso del mecanismo 4)
    m4 = [_linea("Sección 2. Dispositivos de seguridad.", 1, 30.0),
          _linea("2.1. Sistema de monitoreo.", 1, 50.0, x0=76.0), _linea(largo, 1, 64.0, x0=98.0),
          _linea("2.1.6. Cuando se decida contar con video vigilancia remota, deberán complementar su seguri-",
                 1, 90.0, x0=98.0),
          _linea("dad con dispositivos que dificulten la accesibilidad al dinero, como ser:", 1, 104.0, x0=129.0),
          _linea("2.1.6.1. Sistema de alerta (último billete): consiste en la emisión de una alerta.", 1, 130.0,
                 x0=133.0)]
    r4, ch4 = _parse([m4])
    ch4a = E0.construir_chunks(r4, oracion_titulo_4a=True)
    intro = _texto(ch4a, "x::2.1.6::intro") or ""
    hoja = next((c for c in ch4a if c["id"] == "x::2.1.6.1"), {})
    check("4a: la intro de 2.1.6 empieza en su rótulo y el encabezado heredado es solo el número",
          intro.startswith("2.1.6. Cuando se decida") and (_texto(ch4, "x::2.1.6::intro") or "").startswith("dad con")
          and any(t["texto"] == "2.1.6." for t in hoja.get("herencia", []))
          and E0.clase_titulo_4ab(next(n for n in r4.secciones[0].hijos[0].hijos if n.numero == "2.1.6"))[0] == "4a")
    # 4b: título envuelto, con la intro de un renglón y con una intro más larga; guarda del verbo
    tb = [_linea("Sección 1. Titulares.", 1, 30.0),
          _linea("1.3. Identificación de los titulares de cuentas y de las personas autorizadas a operar en", 1, 50.0,
                 x0=76.0),
          _linea("ellas.", 1, 64.0, x0=98.0),
          _linea("1.3.1. Personas humanas.", 1, 90.0, x0=98.0), _linea(largo, 1, 104.0, x0=120.0),
          _linea("1.4. Reporte de otras circunstancias que modifiquen las obligaciones con el", 1, 130.0, x0=76.0),
          _linea("exterior del importador.", 1, 144.0, x0=98.0), _linea(largo, 1, 158.0, x0=98.0),
          _linea("1.4.1. Plazos.", 1, 180.0, x0=98.0), _linea(largo, 1, 194.0, x0=120.0),
          _linea("1.5. La letra de cambio extendida a favor de una persona determinada, que no posea la", 1, 220.0,
                 x0=76.0),
          _linea("cláusula “no a la orden”, será transmisible por endoso.", 1, 234.0, x0=98.0),
          _linea("1.5.1. Endoso.", 1, 260.0, x0=98.0), _linea(largo, 1, 274.0, x0=120.0)]
    rb, chb0 = _parse([tb])
    chb = E0.construir_chunks(rb, titulo_envuelto_4b=True, oracion_titulo_4a=True)
    ids_b = {c["id"]: c for c in chb}
    h131 = [t["texto"] for t in ids_b["x::1.3.1"]["herencia"] if t["tipo"] == "encabezado"]
    check("4b: el renglón que completa el título se junta al título y la intro de un renglón no se emite",
          "x::1.3::intro" in {c["id"] for c in chb0} and "x::1.3::intro" not in ids_b
          and h131[-1] == "1.3. Identificación de los titulares de cuentas y de las personas autorizadas a operar "
                          "en\nellas.", str(h131))
    check("4b: con más intro, la intro sigue sin ese renglón",
          ids_b["x::1.4::intro"]["texto"] == largo and _texto(chb0, "x::1.4::intro").startswith("exterior del"))
    check("4b, guarda: un renglón con verbo («será transmisible») no se junta; la oración es 4a",
          ids_b["x::1.5::intro"]["texto"].startswith("1.5. La letra de cambio")
          and any(t["texto"] == "1.5." for t in ids_b["x::1.5.1"]["herencia"]))
    # apartados de una sección sin puntos (lectura vigente)
    ap = [_linea("REGIMEN INFORMATIVO", 1, 72.0, x0=226.0), _linea("B.C.R.A.", 1, 85.0, x0=83.0),
          _linea("Sección 4. Determinación de la relación", 1, 98.0, x0=139.0),
          _linea("1. Posición", 1, 130.0, x0=76.0),
          _linea("a) General (sin computar el código 107):", 1, 150.0, x0=90.0),
          _linea("2. Franquicias", 1, 180.0, x0=76.0), _linea(largo, 1, 194.0, x0=90.0)]
    a0 = E0.parsear_cuerpo("x", "x.pdf", [ap], [E0.ROL_CUERPO], mayusculas_repetidas=set(), pie_desde_version=True)
    a1 = E0.parsear_cuerpo("x", "x.pdf", [ap], [E0.ROL_CUERPO], mayusculas_repetidas=set(), pie_desde_version=True,
                           apartados_seccion=True)
    cha = {c["id"]: c for c in E0.construir_chunks(a1)}
    check("apartados: sin la regla, «1. Posición» se rechaza fuera de la sección 4; con ella, abre el punto 4.1",
          any(r["motivo"] == "fuera_de_seccion_4" for r in a0.rechazos_header)
          and set(cha) == {"x::4.1", "x::4.2"} and cha["x::4.1"]["flags"].get("numero_impreso") == "1"
          and cha["x::4.1"]["texto"].startswith("1. Posición"), str(sorted(cha)))


def test_s04_casos(d: Path) -> None:
    print(f"== s) S0-4 de U-SEG-OFICIAL: un caso medido por regla (e0-r2 sobre {len(TOS_S04)} TOs)")
    correr_e0.correr(d, manifiesto=_ManifiestoParticion(TOS_S04), version_e0="e0-r2")
    ch = {to: {c["id"]: c for c in cargar(d, f"chunks_{to}.json")} for to in TOS_S04}

    def txt(to: str, uid: str) -> str:
        return ch[to].get(uid, {}).get("texto", "")

    check("sub-documento, ri_sef (fila 58 de S1): el preámbulo ya no trae la parte I; partes I a III y anexos I a "
          "III",
          "Información solicitada" not in txt("ri_sef", "ri_sef::S0") and bool(txt("ri_sef", "ri_sef::P1::S1"))
          and txt("ri_sef", "ri_sef::P2::S0").startswith("II. Requisitos") and bool(txt("ri_sef", "ri_sef::P3::S1"))
          and txt("ri_sef", "ri_sef::A3::S0").startswith("Anexo III"))
    check("sub-documento, nmcief (fila 71): el Anexo II con su numeración (nmcief::A2::3.2.1) y la herencia desde "
          "«Anexo II»",
          bool(txt("nmcief", "nmcief::A2::3.2.1"))
          and ch["nmcief"]["nmcief::A2::3.2.1"]["herencia"][0]["texto"] == "Anexo II")
    check("sdg3, nmcief (fila 71): «4. Periodicidad…» abre su raíz y la 3 ya no la lleva",
          txt("nmcief", "nmcief::A1P2::S4").startswith("4. Periodicidad")
          and "Periodicidad" not in txt("nmcief", "nmcief::A1P2::S3"))
    check("sub-documento, ri_ccna (fila 82): los anexos de la segunda norma (D2) y los formularios (D1F2) con su "
          "numeración; el Anexo IV ya no lleva los ítems de la declaración jurada",
          bool(txt("ri_ccna", "ri_ccna::D2A2::3.4.1")) and txt("ri_ccna", "ri_ccna::D1F2::S1").startswith("1. No soy")
          and "ri_ccna::D1A4::S5" not in ch["ri_ccna"])
    check("sub-documento, ri_icpipsp (fila 85): la fila 8 de SINAP ya no lleva el bloque CONAU; el Anexo II aparte",
          bool(txt("ri_icpipsp", "ri_icpipsp::A1C1::S8"))
          and "CONAU" not in txt("ri_icpipsp", "ri_icpipsp::A1C1::S8")
          and txt("ri_icpipsp", "ri_icpipsp::A2::S0").startswith("ANEXO II"))
    check("sub-documento, ri_cc: los tres regímenes (R4, R5 y RIP); R5::S3 es solo la p. 75",
          bool(txt("ri_cc", "ri_cc::R4::1.1")) and bool(txt("ri_cc", "ri_cc::R5::2.1"))
          and ch["ri_cc"]["ri_cc::R5::S3"]["paginas"] == [75] and bool(txt("ri_cc", "ri_cc::RIP::S0")))
    check("sdmax, ri_ccna (Anexo III de la primera norma): los ítems 31 a 40 abren su raíz y la 30 ya no los "
          "lleva (desde S0-4a-ter, en el sub-documento de letra D1A3L2)",
          all(f"ri_ccna::D1A3L2::S{k}" in ch["ri_ccna"] for k in range(31, 41))
          and txt("ri_ccna", "ri_ccna::D1A3L2::S31").startswith("31. Arqueo sorpresivo de los valores")
          and len(txt("ri_ccna", "ri_ccna::D1A3L2::S30")) == 350
          and "31. Arqueo" not in txt("ri_ccna", "ri_ccna::D1A3L2::S30"))
    l2 = [i for i in ch["ri_ccna"] if i.startswith("ri_ccna::D1A3L2::") and i != "ri_ccna::D1A3L2::S0"]
    check("sdl, ri_ccna (Anexo III): «A. GENERAL» y «B. PRUEBAS SUSTANTIVAS» abren D1A3L1 y D1A3L2; B.1 y B.2 son "
          "las raíces 1 y 2 de D1A3L2; 164 unidades",
          txt("ri_ccna", "ri_ccna::D1A3L1::S0").startswith("A. GENERAL")
          and txt("ri_ccna", "ri_ccna::D1A3L2::S0") == "B. PRUEBAS SUSTANTIVAS"
          and txt("ri_ccna", "ri_ccna::D1A3L2::S1").startswith("1. Arqueo sorpresivo de las existencias")
          and txt("ri_ccna", "ri_ccna::D1A3L2::S2").startswith("2. Obtención de confirmaciones")
          and "ri_ccna::D1A3::S2" not in ch["ri_ccna"] and len(ch["ri_ccna"]) == 164)
    check("sdlh, ri_ccna (Anexo III): las 49 unidades de la lista B (B.1 a B.40, con los sub-ítems de 26 y 29) "
          "heredan «B. PRUEBAS SUSTANTIVAS», y las de A.2 y A.3, «A. GENERAL»",
          len(l2) == 49
          and all(any(h["texto"] == "B. PRUEBAS SUSTANTIVAS" for h in ch["ri_ccna"][i]["herencia"]) for i in l2)
          and all(any(h["texto"] == "A. GENERAL" for h in ch["ri_ccna"][i]["herencia"])
                  for i in ("ri_ccna::D1A3L1::S1", "ri_ccna::D1A3L1::S2", "ri_ccna::D1A3L1::SA.3")), str(len(l2)))
    check("sdla, ri_ccna (Anexo III): A.3 es su propia unidad (D1A3L1::SA.3) y el ítem 2 de A.2 queda solo (667 "
          "caracteres)",
          txt("ri_ccna", "ri_ccna::D1A3L1::SA.3").startswith("A.3. El relevamiento y evaluación")
          and len(txt("ri_ccna", "ri_ccna::D1A3L1::S2")) == 667 and "A.3." not in txt("ri_ccna", "ri_ccna::D1A3L1::S2"))
    oc = ch["ri_oc"]
    check("sdr1, ri_oc: los Anexos I y II son sub-documentos sin el prefijo del régimen de la página 1",
          bool(txt("ri_oc", "ri_oc::A1::S0")) and all(f"ri_oc::A2::S{k}" in oc for k in range(1, 7))
          and not any("R10" in i for i in oc))
    check("apl, ri_oc: «APARTADO B» y «APARTADO C» abren sus raíces, B.1.1 a B.3.4 y C.1 a C.11 son puntos, y "
          "3.51 queda con su texto (p. 15)",
          all(f"ri_oc::B.1.{k}" in oc for k in range(1, 29)) and "ri_oc::B.3.4" in oc and "ri_oc::C.11" in oc
          and oc["ri_oc::3.51"]["paginas"] == [15] and "APARTADO B" not in txt("ri_oc", "ri_oc::3.51")
          and [h["unidad_origen"] for h in oc["ri_oc::B.1.1"]["herencia"]] == ["SB", "B.1"] and len(oc) == 184)
    est_sef = cargar(d, "estructura_ri_sef.json")
    check("sdmax, ri_sef: los códigos 101 a 126 del Anexo II no suceden a la raíz anterior y siguen rechazados",
          sum(r["motivo"] == "raiz_mayor_a_max" for r in est_sef["rechazos_header"]) == 24
          and not any(a["tipo"] == "raiz_mayor_a_max_subdocumento_sdmax" for a in est_sef["avisos"]))
    check("apartados, ri_ai: «1. Posición», «2. Franquicias», «3. Incumplimientos» son 4.1 a 4.3",
          all(f"ri_ai::4.{k}" in ch["ri_ai"] for k in (1, 2, 3)) and "ri_ai::S4" not in ch["ri_ai"]
          and ch["ri_ai"]["ri_ai::4.1"]["flags"].get("numero_impreso") == "1")
    hijo = next(c for i, c in ch["efemin"].items() if i.startswith("efemin::1.3.1.") and c["tipo"] == "punto_terminal")
    check("4b, efemin 1.3.1 (uno de los 30 títulos partidos de un renglón): sin intro y con el título entero",
          "efemin::1.3.1::intro" not in ch["efemin"]
          and any(t["texto"].endswith("abiertas en las cajas de crédito cooperativas.") for t in hijo["herencia"]))
    cob = cargar(d, "cobertura.json")
    check(f"cobertura exacta en los {len(TOS_S04)} TOs", all(cob[to]["cobertura_exacta"] for to in TOS_S04))


def test_s0_doble(base: Path) -> None:
    print("== m) S0 de U-SEG-OFICIAL: doble corrida de e0-r2, byte a byte")
    for nombre in ("a", "b"):
        correr_e0.correr(base / f"doble_{nombre}", manifiesto=_ManifiestoParticion(("garopt", "ri_spi")),
                         version_e0="e0-r2")
    sha_a, sha_b = correr_e0.shas_salida(base / "doble_a"), correr_e0.shas_salida(base / "doble_b")
    check("e0-r2 sobre garopt y ri_spi: dos corridas con los mismos sha256", sha_a == sha_b and bool(sha_a),
          f"{len(sha_a)} archivos")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir-a", default=None)
    ap.add_argument("--dir-b", default=None)
    args = ap.parse_args()

    if args.dir_a and args.dir_b:
        dir_a, dir_b = Path(args.dir_a), Path(args.dir_b)
    else:
        base = Path(tempfile.mkdtemp(prefix="e0_selftest_"))
        dir_a, dir_b = base / "corrida_a", base / "corrida_b"
        print(f"corriendo el pipeline dos veces bajo {base} …")
        correr_e0.correr(dir_a)
        correr_e0.correr(dir_b)

    test_determinismo(dir_a, dir_b)
    test_cobertura(dir_a)
    test_t4(dir_a)
    test_correcciones(dir_a)
    test_minichunks(dir_a)
    base_s0 = Path(tempfile.mkdtemp(prefix="e0_selftest_s0_"))
    test_s0_legada()
    test_s0_casos(base_s0 / "casos")
    test_s0_sinteticos()
    test_s0_doble(base_s0)
    test_s03_legada()
    test_s03_sinteticos()
    test_s03_casos(base_s0 / "casos_s03")
    test_s04_legada()
    test_s04_sinteticos()
    test_s04_casos(base_s0 / "casos_s04")

    total = len(RESULTADOS)
    ok = sum(1 for _, b, _ in RESULTADOS if b)
    print(f"\nSELFTEST: {ok}/{total} PASS")
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
