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

    total = len(RESULTADOS)
    ok = sum(1 for _, b, _ in RESULTADOS if b)
    print(f"\nSELFTEST: {ok}/{total} PASS")
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
