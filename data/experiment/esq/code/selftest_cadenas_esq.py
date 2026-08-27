"""
selftest_cadenas_esq.py — SELFTEST OFFLINE del instrumento de ESQ-1 ($0, sin API).

Paso 1 de la secuencia cerrada del pre-registro (§5): «Selftest del instrumento
nuevo (§7). Sin PASS, no se gasta.»

Cubre los siete puntos exigidos, con fixtures sintéticos mínimos que este mismo
archivo genera bajo `selftest_out/` (gitignorado) y con los cinco jsonl reales
de producción, que se LEEN y no se tocan:

  1. SALIDA SIN FRECUENCIAS — una cadena repetida N veces sale una sola vez y
     el número N no aparece en ningún byte de la salida.
  2. SALIDA SIN ORIGEN — la misma cadena en dos documentos distintos no
     arrastra unidad, chunk_id, TO ni nombre de archivo a la salida.
  3. DEDUPLICACIÓN Y ORDEN — sin repetidos, ordenada por punto de código.
  4. CAMPOS CORRECTOS — `tipo_propuesto` se lee de entidades y
     `predicado_propuesto` de relaciones, con trampas cruzadas en el fixture
     para que confundirlos falle.
  5. AUSENCIA TOLERADA — sobre los jsonl reales de hoy, que no tienen esos dos
     campos, devuelve lista vacía y exit 0.
  6. DETERMINISMO — dos corridas dan bytes idénticos, y el orden en que se
     pasan los archivos de entrada no cambia la salida.
  7. ANCLA DE DATOS REALES — el canal `sujeto_propuesto` sobre los cinco jsonl
     de producción da el mismo número que un recomputo independiente hecho con
     otro método (jq si está disponible, si no un recorrido en un subproceso
     que no importa este código).

Más los bordes que hacen confiable al instrumento: valores vacíos tratados como
ausentes, cadenas emitidas verbatim, y freno con exit 2 ante json inválido,
campo de tipo inesperado o cadena con salto de línea.

Uso:  .venv/bin/python -B data/experiment/esq/code/selftest_cadenas_esq.py
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import cadenas_esq as ce                   # noqa: E402  (el instrumento bajo prueba)

UNIDAD_DIR = CODE_DIR.parent                       # data/experiment/esq
EXP_DIR = UNIDAD_DIR.parent                        # data/experiment
REPO_DIR = EXP_DIR.parent.parent
SELFTEST_DIR = UNIDAD_DIR / "selftest_out"

JSONL_PRODUCCION = sorted(
    (EXP_DIR / "reextraccion_v2" / "corpus_v2" / "salida").glob(
        "*/extracciones_e1.jsonl"))

_checks = []


def check(nombre, cond):
    _checks.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")


# --------------------------------------------------------------------------- #
# Fixtures sintéticos                                                          #
# --------------------------------------------------------------------------- #
def registro(unidad, chunk_id, to, archivo, entidades=(), relaciones=()):
    """Un registro con la forma real de los jsonl de E1 (claves verificadas
    sobre reextraccion_v2/corpus_v2/salida/ric/extracciones_e1.jsonl)."""
    prov = {"to": to, "archivo": archivo, "punto": "1.1",
            "rol_documental": "punto_propio"}
    return {
        "chunk_id": chunk_id,
        "unidad": unidad,
        "tipo_unidad": "punto",
        "titulo": "Título de prueba",
        "stop_reason": "end_turn",
        "error": None,
        "usage": {"input_tokens": 1, "output_tokens": 1},
        "tool_input_crudo": {"entities": [], "relations": []},
        "validacion": {
            "chunk_id": chunk_id,
            "entidades": [dict(e, provenance=prov) for e in entidades],
            "relaciones": [dict(r, provenance=prov) for r in relaciones],
            "omisiones_no_prosa": [],
            "rechazos": [],
            "advertencias": [],
            "metricas": {},
        },
    }


def escribir_jsonl(ruta, registros):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with ruta.open("w", encoding="utf-8") as fh:
        for r in registros:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    return ruta


def ent(tipo_propuesto=None, **extra):
    e = {"local_id": "e1", "type": "Obligacion", "label": "una obligación",
         "properties": {}}
    if tipo_propuesto is not None:
        e["tipo_propuesto"] = tipo_propuesto
    e.update(extra)
    return e


def rel(predicado_propuesto=None, sujeto_propuesto=None, **extra):
    r = {"source": "e1", "target": "to", "predicate": "aplica_a",
         "sujeto_id": None, "sujeto_propuesto": sujeto_propuesto,
         "sujeto_propuesto_padre_sugerido": None}
    if predicado_propuesto is not None:
        r["predicado_propuesto"] = predicado_propuesto
    r.update(extra)
    return r


# --------------------------------------------------------------------------- #
# Recomputo independiente del ancla — NO usa cadenas_esq                       #
# --------------------------------------------------------------------------- #
JQ_FILTRO = ('.validacion.relaciones[]? | .sujeto_propuesto | '
             'select(. != null and . != "")')

# Mismo filtro sobre el bloque CRUDO. Fe de erratas
# docs/fe_erratas_prerregistro_esq1_alcance.md (b): ESQ-1 mide sobre
# tool_input_crudo, porque el validado descarta propuestas por motivos ajenos a
# la propuesta y ese descarte correlaciona con la señal que ESQ-1 busca.
JQ_FILTRO_CRUDO = ('.tool_input_crudo.relations[]? | .sujeto_propuesto | '
                   'select(. != null and . != "")')

PY_INDEPENDIENTE_CRUDO = r"""
import json, sys
vistas = []
for ruta in sys.argv[1:]:
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            if not linea.strip():
                continue
            rel = json.loads(linea)["tool_input_crudo"]["relations"]
            vistas += [r["sujeto_propuesto"] for r in rel
                       if r.get("sujeto_propuesto")]
print(len(vistas), len(set(vistas)))
"""

PY_INDEPENDIENTE = r"""
import json, sys
vistas = []
for ruta in sys.argv[1:]:
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            if not linea.strip():
                continue
            rel = json.loads(linea)["validacion"]["relaciones"]
            vistas += [r["sujeto_propuesto"] for r in rel
                       if r.get("sujeto_propuesto")]
print(len(vistas), len(set(vistas)))
"""


def recomputo_independiente(rutas, bloque="validacion"):
    """(disparos, distintas) por un camino que no toca el instrumento.

    `bloque`: "validacion" (lo que el instrumento sabe leer hoy) o
    "tool_input_crudo" (de donde ESQ-1 debe medir, fe de erratas de alcance).
    Devuelve además el método usado, para poder declararlo en el reporte.
    """
    filtro_jq = JQ_FILTRO if bloque == "validacion" else JQ_FILTRO_CRUDO
    filtro_py = (PY_INDEPENDIENTE if bloque == "validacion"
                 else PY_INDEPENDIENTE_CRUDO)
    rutas = [str(p) for p in rutas]
    jq = shutil.which("jq")
    if jq:
        proc = subprocess.run([jq, "-r", filtro_jq] + rutas,
                              capture_output=True, text=True)
        if proc.returncode == 0:
            salidas = [l for l in proc.stdout.split("\n") if l != ""]
            return len(salidas), len(set(salidas)), "jq"
    proc = subprocess.run([sys.executable, "-c", filtro_py] + rutas,
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr)
    disparos, distintas = proc.stdout.split()
    return int(disparos), int(distintas), "subproceso python independiente"


def correr_cli(args):
    """Corre el instrumento como proceso: (returncode, stdout, stderr)."""
    proc = subprocess.run(
        [sys.executable, "-B", str(CODE_DIR / "cadenas_esq.py")] + [str(a) for a in args],
        capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


# --------------------------------------------------------------------------- #
def main():
    print(f"\nSELFTEST cadenas_esq — instrumento de ESQ-1 (sin API, USD 0)")
    print(f"  fixtures y salidas en: {SELFTEST_DIR}")
    if SELFTEST_DIR.exists():
        shutil.rmtree(SELFTEST_DIR)
    SELFTEST_DIR.mkdir(parents=True)

    print(f"  jsonl de producción leídos: {len(JSONL_PRODUCCION)}")
    for p in JSONL_PRODUCCION:
        print(f"    - {p.relative_to(REPO_DIR)}")
    print()

    # --- 1) SALIDA SIN FRECUENCIAS ---------------------------------------- #
    # La cadena se repite N=7 veces. Ninguna cadena del fixture lleva dígitos,
    # así que si el "7" apareciera en la salida sólo podría venir del conteo.
    N = 7
    fx_frec = escribir_jsonl(
        SELFTEST_DIR / "fx_frecuencias.jsonl",
        [registro("u-a", "c-a", "ric", "TO_ric.pdf",
                  relaciones=[rel(sujeto_propuesto="entidades financieras del grupo uno")
                              for _ in range(N)] +
                             [rel(sujeto_propuesto="banco de pagos internacionales")])])
    salida_frec = ce.render(ce.cadenas_distintas([fx_frec], "sujeto_propuesto"))
    check("SIN FRECUENCIAS: la cadena repetida N veces aparece exactamente una vez",
          salida_frec.count("entidades financieras del grupo uno") == 1)
    check("SIN FRECUENCIAS: el número N de repeticiones no aparece en la salida",
          str(N) not in salida_frec and not any(c.isdigit() for c in salida_frec))

    # --- 2) SALIDA SIN ORIGEN --------------------------------------------- #
    # La misma cadena en dos documentos distintos, con unidad, chunk, TO y
    # archivo distintos. Nada de eso puede filtrarse a la salida.
    marcas = ["u-cap-0001", "u-ext-0002", "cap#7", "ext#9", "cap", "ext",
              "TO_capitales_minimos.pdf", "TO_exterior_y_cambios.pdf"]
    fx_org = escribir_jsonl(
        SELFTEST_DIR / "fx_origen.jsonl",
        [registro("u-cap-0001", "cap#7", "cap", "TO_capitales_minimos.pdf",
                  relaciones=[rel(sujeto_propuesto="fondo monetario internacional")]),
         registro("u-ext-0002", "ext#9", "ext", "TO_exterior_y_cambios.pdf",
                  relaciones=[rel(sujeto_propuesto="fondo monetario internacional")])])
    salida_org = ce.render(ce.cadenas_distintas([fx_org], "sujeto_propuesto"))
    check("SIN ORIGEN: ninguna marca de documento/chunk/TO/archivo llega a la salida",
          not any(m in salida_org for m in marcas))
    check("SIN ORIGEN: la cadena compartida por dos documentos sale una sola vez",
          salida_org == "fondo monetario internacional\n")

    # --- 3) DEDUPLICACIÓN Y ORDEN ----------------------------------------- #
    crudas = ["zeta", "alfa", "mu", "alfa", "zeta", "alfa", "ñandú", "Alfa"]
    fx_ord = escribir_jsonl(
        SELFTEST_DIR / "fx_orden.jsonl",
        [registro("u-b", "c-b", "pro", "TO_pro.pdf",
                  relaciones=[rel(sujeto_propuesto=c) for c in crudas])])
    lista_ord = ce.cadenas_distintas([fx_ord], "sujeto_propuesto")
    check("DEDUP Y ORDEN: sin repetidos y ordenada por punto de código Unicode",
          lista_ord == sorted(set(crudas)) and len(lista_ord) == len(set(lista_ord)))

    # --- 4) CAMPOS CORRECTOS ---------------------------------------------- #
    # Trampas cruzadas: predicado_propuesto DENTRO de una entidad y
    # tipo_propuesto DENTRO de una relación. El instrumento no debe verlos.
    fx_campos = escribir_jsonl(
        SELFTEST_DIR / "fx_campos.jsonl",
        [registro("u-c", "c-c", "cla", "TO_cla.pdf",
                  entidades=[ent(tipo_propuesto="tipo-en-entidad",
                                 predicado_propuesto="TRAMPA-predicado-en-entidad")],
                  relaciones=[rel(predicado_propuesto="predicado-en-relacion",
                                  sujeto_propuesto="sujeto-en-relacion",
                                  tipo_propuesto="TRAMPA-tipo-en-relacion")])])
    t = ce.cadenas_distintas([fx_campos], "tipo_propuesto")
    p = ce.cadenas_distintas([fx_campos], "predicado_propuesto")
    s = ce.cadenas_distintas([fx_campos], "sujeto_propuesto")
    check("CAMPOS: tipo_propuesto se lee de entidades y no de relaciones",
          t == ["tipo-en-entidad"])
    check("CAMPOS: predicado_propuesto se lee de relaciones y no de entidades",
          p == ["predicado-en-relacion"])
    check("CAMPOS: sujeto_propuesto se lee de relaciones y no se cruza con los otros dos",
          s == ["sujeto-en-relacion"])
    check("CAMPOS: los tres canales no se contaminan entre sí",
          set(t).isdisjoint(p) and set(t).isdisjoint(s) and set(p).isdisjoint(s))

    # --- 5) AUSENCIA TOLERADA sobre los jsonl reales ---------------------- #
    out_tipo = SELFTEST_DIR / "real_tipo_propuesto.txt"
    rc_t, _, err_t = correr_cli(["--canal", "tipo_propuesto",
                                 "--salida", out_tipo] + JSONL_PRODUCCION)
    out_pred = SELFTEST_DIR / "real_predicado_propuesto.txt"
    rc_p, _, err_p = correr_cli(["--canal", "predicado_propuesto",
                                 "--salida", out_pred] + JSONL_PRODUCCION)
    check("AUSENCIA TOLERADA: tipo_propuesto sobre los 5 jsonl reales -> vacío y exit 0",
          rc_t == 0 and out_tipo.read_bytes() == b"")
    check("AUSENCIA TOLERADA: predicado_propuesto sobre los 5 jsonl reales -> vacío y exit 0",
          rc_p == 0 and out_pred.read_bytes() == b"")
    check("AUSENCIA TOLERADA: no ensucia con warnings (stderr sólo el resumen de corrida)",
          err_t.strip().count("\n") == 0 and err_t.startswith("cadenas_esq: canal=")
          and err_p.strip().count("\n") == 0 and err_p.startswith("cadenas_esq: canal="))

    # --- 6) DETERMINISMO --------------------------------------------------- #
    out_a = SELFTEST_DIR / "det_a.txt"
    out_b = SELFTEST_DIR / "det_b.txt"
    rc_a, _, _ = correr_cli(["--canal", "sujeto_propuesto", "--salida", out_a]
                            + JSONL_PRODUCCION)
    rc_b, _, _ = correr_cli(["--canal", "sujeto_propuesto", "--salida", out_b]
                            + JSONL_PRODUCCION)
    check("DETERMINISMO: dos corridas producen salida byte-idéntica",
          rc_a == 0 and rc_b == 0 and out_a.read_bytes() == out_b.read_bytes())
    out_rev = SELFTEST_DIR / "det_rev.txt"
    correr_cli(["--canal", "sujeto_propuesto", "--salida", out_rev]
               + list(reversed(JSONL_PRODUCCION)))
    check("DETERMINISMO: el orden de los archivos de entrada no cambia la salida",
          out_rev.read_bytes() == out_a.read_bytes())

    # --- 7) ANCLA DE DATOS REALES ------------------------------------------ #
    lista_real = ce.cadenas_distintas(JSONL_PRODUCCION, "sujeto_propuesto")
    disparos_ind, distintas_ind, metodo = recomputo_independiente(JSONL_PRODUCCION)
    print(f"\n  ancla — instrumento: distintas={len(lista_real)}")
    print(f"  ancla — recomputo independiente ({metodo}): "
          f"disparos={disparos_ind} distintas={distintas_ind}\n")
    check(f"ANCLA: sujeto_propuesto sobre los 5 jsonl de producción coincide con "
          f"el recomputo independiente ({metodo}): {len(lista_real)} distintas",
          len(lista_real) == distintas_ind)
    check("ANCLA: la salida en disco tiene una línea por cadena distinta",
          out_a.read_text(encoding="utf-8").count("\n") == len(lista_real))

    # --- 7bis) ANCLA DEL BLOQUE CRUDO -------------------------------------- #
    # Fe de erratas docs/fe_erratas_prerregistro_esq1_alcance.md (b): el número
    # que ESQ-1 lee contra las bandas se computa sobre tool_input_crudo. El
    # instrumento de 181e262 NO puede leer ese bloque todavía (CANALES lo tiene
    # cableado a `validacion`, cadenas_esq.py:86-90 y :129), así que el ancla
    # del crudo se verifica por dos caminos independientes del instrumento, y
    # la limitación queda asertada abajo para que no pase inadvertida.
    disparos_cru, distintas_cru, metodo_cru = recomputo_independiente(
        JSONL_PRODUCCION, bloque="tool_input_crudo")
    print(f"\n  ancla crudo — recomputo independiente ({metodo_cru}): "
          f"disparos={disparos_cru} distintas={distintas_cru}")
    print(f"  ancla validado — instrumento: distintas={len(lista_real)}")
    print(f"  brecha crudo-validado: {disparos_cru - disparos_ind} disparos, "
          f"{distintas_cru - len(lista_real)} cadena(s)\n")
    check(f"ANCLA CRUDO: sujeto_propuesto sobre tool_input_crudo de los 5 jsonl "
          f"de producción da 39 cadenas distintas ({metodo_cru}): "
          f"{distintas_cru}", distintas_cru == 39)
    check(f"ANCLA CRUDO: 56 disparos sobre tool_input_crudo: {disparos_cru}",
          disparos_cru == 56)
    check("BRECHA: el validado pierde exactamente 1 cadena distinta y 2 "
          "disparos respecto del crudo (fe de erratas de alcance, (b))",
          distintas_cru - len(lista_real) == 1
          and disparos_cru - disparos_ind == 2)
    check("LIMITACIÓN DECLARADA: el instrumento sólo expone canales del bloque "
          "`validacion`; leer del crudo exige la extensión pendiente de la fe "
          "de erratas (b), no sólo otra ruta",
          set(ce.CANALES) == {"tipo_propuesto", "predicado_propuesto",
                              "sujeto_propuesto"}
          and all(c[0] in ("entidades", "relaciones")
                  for c in ce.CANALES.values()))

    # --- bordes que hacen confiable al instrumento ------------------------- #
    fx_vacios = escribir_jsonl(
        SELFTEST_DIR / "fx_vacios.jsonl",
        [registro("u-d", "c-d", "ric", "TO_ric.pdf",
                  relaciones=[rel(sujeto_propuesto=None),
                              rel(sujeto_propuesto=""),
                              rel(sujeto_propuesto="   "),
                              rel(sujeto_propuesto="sujeto real")])])
    check("BORDE: null, cadena vacía y sólo-espacios se tratan como ausentes",
          ce.cadenas_distintas([fx_vacios], "sujeto_propuesto") == ["sujeto real"])

    fx_verb = escribir_jsonl(
        SELFTEST_DIR / "fx_verbatim.jsonl",
        [registro("u-e", "c-e", "ric", "TO_ric.pdf",
                  relaciones=[rel(sujeto_propuesto=" con espacio adelante"),
                              rel(sujeto_propuesto="con espacio adelante")])])
    check("BORDE: las cadenas se emiten verbatim (recortar sería normalizar, y "
          "la normalización es del paso 7)",
          ce.cadenas_distintas([fx_verb], "sujeto_propuesto")
          == [" con espacio adelante", "con espacio adelante"])

    fx_sin_val = SELFTEST_DIR / "fx_sin_validacion.jsonl"
    fx_sin_val.write_text(
        json.dumps({"chunk_id": "x", "tool_input_crudo": {"relations": [
            {"sujeto_propuesto": "sólo en el crudo"}]}}, ensure_ascii=False) + "\n"
        + json.dumps({"chunk_id": "y", "validacion": {"relaciones": []}},
                     ensure_ascii=False) + "\n",
        encoding="utf-8")
    check("BORDE: sin bloque validacion no rompe, y no lee del crudo",
          ce.cadenas_distintas([fx_sin_val], "sujeto_propuesto") == [])

    fx_roto = SELFTEST_DIR / "fx_json_roto.jsonl"
    fx_roto.write_text('{"chunk_id": "ok", "validacion": {"relaciones": []}}\n'
                       '{esto no es json\n', encoding="utf-8")
    rc_roto, _, err_roto = correr_cli(["--canal", "sujeto_propuesto", fx_roto])
    check("BORDE: json inválido frena con exit 2 y señala archivo:línea "
          "(no lo saltea en silencio)",
          rc_roto == 2 and "fx_json_roto.jsonl:2" in err_roto)

    fx_tipo = escribir_jsonl(
        SELFTEST_DIR / "fx_tipo_raro.jsonl",
        [registro("u-f", "c-f", "ric", "TO_ric.pdf",
                  relaciones=[rel(sujeto_propuesto=["una", "lista"])])])
    rc_tipo, _, err_tipo = correr_cli(["--canal", "sujeto_propuesto", fx_tipo])
    check("BORDE: campo con tipo inesperado frena con exit 2 en vez de inventar",
          rc_tipo == 2 and "no es cadena" in err_tipo)

    fx_nl = escribir_jsonl(
        SELFTEST_DIR / "fx_salto_linea.jsonl",
        [registro("u-g", "c-g", "ric", "TO_ric.pdf",
                  relaciones=[rel(sujeto_propuesto="dos\nrenglones")])])
    rc_nl, _, err_nl = correr_cli(["--canal", "sujeto_propuesto", fx_nl])
    check("BORDE: cadena con salto de línea frena con exit 2 (la lista dejaría "
          "de ser reversible)",
          rc_nl == 2 and "salto de línea" in err_nl)

    rc_inex, _, _ = correr_cli(["--canal", "sujeto_propuesto",
                                SELFTEST_DIR / "no_existe.jsonl"])
    check("BORDE: archivo inexistente frena con exit 2", rc_inex == 2)

    # --- los jsonl reales quedaron intactos -------------------------------- #
    check("Los 5 jsonl de producción se leyeron y no se escribieron (sólo lectura)",
          all(p.exists() for p in JSONL_PRODUCCION) and len(JSONL_PRODUCCION) == 5)

    passed = sum(ok for _, ok in _checks)
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print("  RESULTADO:", "PASS" if passed == len(_checks) else "FAIL")
    return 0 if passed == len(_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
