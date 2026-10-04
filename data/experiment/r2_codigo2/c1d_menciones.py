"""U-R2-CODIGO-2, C1.d — contador de menciones en texto heredado sin la autocita del encabezado de sección (USD 0, sin
API ni Neo4j). Solo escribe --out.

El contador `texto_heredado.menciones` de `detectar_y_resolver_r2` (r1_referencias.py:1198) suma toda mención que la
regla (i) detecta en el texto que el chunk hereda de otra unidad. La línea «Sección N. Título» del encabezado heredado
se lee como cita de la sección N, que es la propia unidad heredada: es una autocita de encabezado. Definición (la de
M3, `medicion_r2a/m3_cadena_instrumentada.py`): mención sin puntos, con secciones = [N], unidad heredada S<N> y
evidencia que empieza con «Sección N». Contador nuevo = menciones − autocitas de encabezado.

Mide, envolviendo en memoria la lectura del bloque heredado (sin editar ningún módulo):
  1. KG-Tanda0-Diez-r2a y KG-Tanda0-Desarrollo-r2a (cadena r2, `c1_comun`): control, el total es el contador del
     reporte del ensamblado (3.801 y 2.993).
  2. La medición de `r2_codigo/r3d_remisiones.py` (regla firmada sobre KG-Tanda0-Desarrollo-r1, KG-Tanda0-Diez-r1 y
     KG-Reextraído-r1, con el texto de e0-r2), que es la de la cifra 2.870 de `reglas_remisiones_postR3.md:102`.
     Con `--r1-referencias <archivo>` la corre con esa versión del módulo (la de `26d274d`, el commit de la cifra:
     `git show 26d274d:data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py`); control, el total es el de
     `r3d_remisiones.json` de ese commit.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo2/c1d_menciones.py \
      --out data/experiment/r2_codigo2/salidas/c1d_menciones.json
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo2/c1d_menciones.py \
      --r1-referencias <r1_referencias de 26d274d> --out data/experiment/r2_codigo2/salidas/c1d_menciones_26d274d.json
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
RE_SECCION = re.compile(r"^\s*Secci[oó]n\s+(\d+)\b", re.I)
# Totales de `texto_heredado.menciones` en r3d_remisiones.json, por versión (control de la reproducción).
TOTALES_R3D = {"HEAD": {"desarrollo": 2858, "diez": 3655, "r1": 2838},
               "26d274d": {"desarrollo": 2870}}


def es_autocita(m: dict) -> bool:
    mt = RE_SECCION.match(m["evidencia"] or "")
    return (mt is not None and not m["puntos"] and m["secciones"] == [mt.group(1)]
            and m["unidad_heredada"] == f"S{mt.group(1)}")


def instrumentar(REF, registro: list):
    """Parches que registran cada mención de la regla (i) con su unidad heredada. Reconoce la lectura del bloque
    heredado por la línea de `detectar_y_resolver_r2` que la hace (`_tramos_e0_de(p_h, chunk)` desde R5;
    `_texto_e0_de(p_h, chunk)` en la versión de 26d274d)."""
    fuente = Path(REF.__file__).read_text(encoding="utf-8").splitlines()
    estado = {"ultimo": None}
    parches = []
    lineas = [i for i, l in enumerate(fuente, 1) if "_tramos_e0_de(p_h, chunk)" in l]
    if lineas:
        assert len(lineas) == 1, lineas
        linea = lineas[0]
        orig_t, orig_m = REF._tramos_e0_de, REF.menciones_por_tramo

        def tramos(p, chunk):
            out = orig_t(p, chunk)
            f = sys._getframe(1)
            if f.f_code.co_name == "detectar_y_resolver_r2" and f.f_lineno == linea:
                estado["ultimo"] = (out, dict(p), chunk.get("id"))
            return out

        def menciones(tr, to_origen, reglas):
            out = orig_m(tr, to_origen, reglas)
            u = estado["ultimo"]
            if u is not None and u[0] is tr:
                registro.extend({"chunk_id": u[2], "unidad_heredada": u[1].get("punto"),
                                 "tipo": u[1].get("rol_documental"), "clase": m["clase"],
                                 "puntos": list(m["puntos"]), "secciones": list(m["secciones"]),
                                 "evidencia": m["evidencia"]} for m in out)
                estado["ultimo"] = None
            return out
        parches = [(REF, "_tramos_e0_de", tramos), (REF, "menciones_por_tramo", menciones)]
    else:
        linea = [i for i, l in enumerate(fuente, 1) if "_texto_e0_de(p_h, chunk)" in l]
        assert len(linea) == 1, linea
        linea = linea[0]
        orig_t, orig_d = REF._texto_e0_de, REF.detectar_menciones_r2

        def texto(p, chunk):
            out = orig_t(p, chunk)
            f = sys._getframe(1)
            if f.f_code.co_name == "detectar_y_resolver_r2" and f.f_lineno == linea:
                estado["ultimo"] = (dict(p), chunk.get("id"))
            return out

        def detectar(texto_h, to_origen, reglas=REF.REGLAS_R2, *a, **k):
            out = orig_d(texto_h, to_origen, reglas, *a, **k)
            u = estado["ultimo"]
            f = sys._getframe(1)
            if u is not None and f.f_code.co_name == "detectar_y_resolver_r2":
                registro.extend({"chunk_id": u[1], "unidad_heredada": u[0].get("punto"),
                                 "tipo": u[0].get("rol_documental"), "clase": m["clase"],
                                 "puntos": list(m["puntos"]), "secciones": list(m["secciones"]),
                                 "evidencia": m["evidencia"]} for m in out)
                estado["ultimo"] = None
            return out
        parches = [(REF, "_texto_e0_de", texto), (REF, "detectar_menciones_r2", detectar)]
    return parches


def contar(registro: list, total_reportado: int | None) -> OrderedDict:
    contables = [m for m in registro if m["clase"] != "anafora_sin_numero"]
    auto = [m for m in contables if es_autocita(m)]
    return OrderedDict([
        ("menciones", len(contables)), ("total_reportado", total_reportado),
        ("total_coincide", total_reportado is None or len(contables) == total_reportado),
        ("autocitas_de_encabezado", len(auto)),
        ("autocitas_por_tipo_de_herencia", dict(sorted(Counter(m["tipo"] for m in auto).items()))),
        ("contador_nuevo", len(contables) - len(auto)),
        ("contador_nuevo_por_clase", dict(sorted(Counter(m["clase"] for m in contables if not es_autocita(m)).items()))),
        ("chunks_con_autocita", len({m["chunk_id"] for m in auto}))])


def medir_r2a() -> OrderedDict:
    import c1_comun as K   # noqa: PLC0415
    out = OrderedDict()
    for nombre in K.GRAFOS:
        registro: list = []
        r = K.correr_r2(nombre, instrumentar(K.REF, registro))
        reg = r["escritos"]["remisiones_registro.json"]
        autorref = [c for c in reg if c.get("atribucion") == "texto_heredado" and not c.get("puntos")
                    and RE_SECCION.match(c.get("evidencia") or "")
                    and c["procedencia"].get("punto") == f"S{RE_SECCION.match(c['evidencia']).group(1)}"
                    and c.get("secciones") == [RE_SECCION.match(c['evidencia']).group(1)]]
        out[nombre] = OrderedDict([("control_sha", K.control_sha(nombre, r))])
        out[nombre].update(contar(registro, r["resumen"]["remite_a"]["texto_heredado"]["menciones"]))
        out[nombre].update([
            ("autocitas_en_el_registro_de_remisiones", OrderedDict([
                ("citas", len(autorref)), ("aristas_nuevas", sum(c["aristas_nuevas"] for c in autorref)),
                ("causas", dict(sorted(Counter(x["causa"] for c in autorref for x in c["irresolubles"]).items())))])),
            ("aristas_remite_a_con_evidencia_de_autocita", sum(
                1 for e in r["kg"]["edges"] if e["relation"] == "remite_a"
                and RE_SECCION.match(e["properties"].get("evidencia") or "")
                and e["properties"]["destino"] == f"{e['provenance'].get('to')}::S"
                f"{RE_SECCION.match(e['properties']['evidencia']).group(1)}"))])
    return out


def medir_r3d(version: str) -> OrderedDict:
    raiz = Path(__file__).resolve().parents[3]
    sys.path.insert(0, str(raiz / "data" / "experiment" / "r2_codigo"))
    import r3d_remisiones as R3D   # noqa: PLC0415  (de la copia: sus rutas son las de la copia)
    REF = R3D.REF
    e0r2 = raiz / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_tanda0_r2"
    out = OrderedDict()
    for nombre in TOTALES_R3D[version]:
        registro: list = []
        parches = instrumentar(REF, registro)
        if version == "26d274d":
            # redirección de r3d en 26d274d: los títulos del inventario sin los nombres del manifiesto
            orig_titulos = REF.titulos_de_inventario
            parches.append((REF, "titulos_de_inventario", lambda tos, *a, **k: orig_titulos(tos)))
        originales = [(m, a, getattr(m, a)) for m, a, _ in parches]
        try:
            for m, a, v in parches:
                setattr(m, a, v)
            with R3D.redirigido(nombre):
                kg, base, _ = R3D.cargar(nombre)
                em = R3D.emisores()
                r = REF.detectar_y_resolver(copy.deepcopy(base), perfil="r2", emisores=em, reglas=REF.REGLAS_R2,
                                            chunks_e0_r2=R3D.chunks_e0_r2(e0r2))
        finally:
            for m, a, v in originales:
                setattr(m, a, v)
        out[nombre] = OrderedDict([("grafo", str(R3D.GRAFOS[nombre]["kg"].relative_to(raiz)))])
        out[nombre].update(contar(registro, TOTALES_R3D[version][nombre]))
        out[nombre]["contador_del_resumen"] = r["resumen"]["texto_heredado"]["menciones"]
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--r1-referencias", type=Path, default=None,
                    help="r1_referencias.py de otra versión (26d274d): solo la medición de r3d")
    a = ap.parse_args()
    raiz = Path(__file__).resolve().parents[3]
    if a.r1_referencias is not None:
        # el módulo de 26d274d reemplaza a r1_referencias antes de que r3d_remisiones lo importe
        spec = importlib.util.spec_from_file_location("r1_referencias", a.r1_referencias)
        sys.path.insert(0, str(raiz / "data" / "experiment" / "reextraccion_v2" / "corpus_v2"))
        mod = importlib.util.module_from_spec(spec)
        sys.modules["r1_referencias"] = mod
        spec.loader.exec_module(mod)
        out = OrderedDict([("version_r1_referencias", "26d274d"),
                           ("sha256_r1_referencias", hashlib.sha256(Path(a.r1_referencias).read_bytes()).hexdigest()),
                           ("r3d", medir_r3d("26d274d"))])
    else:
        out = OrderedDict([("definicion", "mención de la regla (i) sin puntos, secciones = [N], unidad heredada S<N> y "
                                          "evidencia que empieza con «Sección N»"),
                           ("r2a", medir_r2a()), ("r3d_head", medir_r3d("HEAD"))])
    import json   # noqa: PLC0415
    (raiz / a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for k, v in out.items():
        if isinstance(v, dict):
            for g, x in v.items():
                if isinstance(x, dict) and "menciones" in x:
                    print(k, g, x["menciones"], x["total_coincide"], x["autocitas_de_encabezado"], x["contador_nuevo"])


if __name__ == "__main__":
    main()
