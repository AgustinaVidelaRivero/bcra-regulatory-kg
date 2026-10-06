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
     lista), 4 (ri_spi, marcador de letra), 7 (ri_mmsef, reapertura del
     padre), T (ri_dcpc, tabla fundida), 8 (manori, lista de la sección
     vetada), 9 (rdbcra, filas del catálogo) y la cobertura exacta;
  l) casos sintéticos de las reglas 5 (cola de título en la lista de
     páginas), 6 (partición por renglones en E0 y en E1, con la capacidad
     del tercer escalón) y 8 (detección de la lista y sus guardas);
  m) doble corrida de e0-r2 sobre dos de esos TOs, byte a byte igual.
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
TOS_S0 = ("garopt", "ri_dsf", "venliq", "adfsp", "ri_spi", "ri_mmsef", "ri_dcpc", "manori", "rdbcra")


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
    check("regla 4: ri_spi en 95 unidades por el marcador de letra (ri_spi::A.1.1)",
          len(ids["ri_spi"]) == 95 and "ri_spi::A.1.1" in ids["ri_spi"]
          and bool(avisos("ri_spi", "marcador_letra_r2")), f"{len(ids['ri_spi'])} unidades")
    check("regla 7: ri_mmsef reabre el padre (ri_mmsef::2.2.1, aviso padre_reabierto_r2)",
          "ri_mmsef::2.2.1" in ids["ri_mmsef"] and bool(avisos("ri_mmsef", "padre_reabierto_r2")))
    check("acompañamiento T: ri_dcpc funde una tabla partida en intersticiales",
          bool(avisos("ri_dcpc", "tabla_fundida_en_un_intersticial_r2")))
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

    total = len(RESULTADOS)
    ok = sum(1 for _, b, _ in RESULTADOS if b)
    print(f"\nSELFTEST: {ok}/{total} PASS")
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
