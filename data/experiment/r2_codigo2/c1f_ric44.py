"""U-R2-CODIGO-2, C1.f — el bloque 4.4 de ric en E0 (USD 0, sin API ni Neo4j).

Diagnóstico (ver el freno de C1): en el PDF de ric la página 16 numera «4.3.», «4.3.1.» y «4.3.2.» el bloque de los
modelos de información que las citas llaman 4.4, 4.4.1 y 4.4.2; E0 los rechaza como duplicados
(`no_sucede_al_hermano_3`) y, en la página 18, rechaza «4.4.3.» y «4.4.4.» porque el 4.4 nunca se abrió
(`padre_4.4_no_abierto`). Todo queda dentro de `ric::4.3.3`.

Variantes candidatas de e0-r2, armadas EN MEMORIA desde el texto de `e0_lib.py` y `correr_e0.py` con reemplazos
exactos (los archivos no se editan):
  A   padre sintético: un encabezado de profundidad ≥ 3 con forma de título cuyo padre no está abierto, cuando el
      abuelo sí lo está y el número del padre sucede al último hijo del abuelo, abre el padre como nodo sintético
      (sin línea de rótulo, título vacío) y se acepta bajo él; aviso `padre_sintetico`. Solo en e0-r2.
  AB  A más una lista en código de renumeraciones (to, página, número impreso → número): ric, p. 16, 4.3 → 4.4,
      4.3.1 → 4.4.1, 4.3.2 → 4.4.2; aviso `renumerado_por_lista`. Solo en e0-r2.
  AL  A acotada por una lista en código de (TO, padre): solo («ric», «4.4»).
  ABL AL más las renumeraciones de AB.

Modos (las salidas de E0 van a directorios fuera del repo):
  --correr-manifiesto <json> --variante base|A|AB --salida <dir>   e0-r2 de los TOs de un manifiesto
  --correr-tos <ids> --variante … --salida <dir>                   e0-r2 de TOs de la partición (PDF de escalado_prep)
  --parsear-152 --variante … --out <json>                           solo el árbol de E0 (escalera e0-r2) de los 152
  --comparar --base <dir> --variante-dir <dir> --out <json>         ids y textos de chunks, por TO

Uso, desde la raíz de una copia del repo (ver el freno de C1 para la secuencia completa).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import types
from collections import OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parents[3]
E0_DIR = RAIZ / "data" / "experiment" / "reextraccion_v2" / "e0_chunking"
REX = RAIZ / "data" / "experiment" / "reextraccion_v2"
PARTICION = RAIZ / "data" / "experiment" / "segmentacion_84" / "b584_particion"
PDFS = RAIZ / "data" / "experiment" / "escalado_prep" / "pdfs"
for p in (str(E0_DIR), str(REX)):
    if p not in sys.path:
        sys.path.insert(0, p)

RENUMERACIONES_AB = {("ric", 16, "4.3"): "4.4", ("ric", 16, "4.3.1"): "4.4.1", ("ric", 16, "4.3.2"): "4.4.2"}
# Variantes acotadas por lista (AL, ABL): el padre sintético solo para estos (TO, número de padre).
PADRES_SINTETICOS_LISTA = frozenset({("ric", "4.4")})

# ---------------------------------------------------------------------------------------------------------------
# Reemplazos exactos sobre el texto de los módulos (cada uno debe aparecer una sola vez).
# ---------------------------------------------------------------------------------------------------------------
_FIRMA_V = """                   mayusculas_repetidas: set | None = None,
                   pie_desde_version: bool = False) -> ResultadoParseo:"""
_FIRMA_N = """                   mayusculas_repetidas: set | None = None,
                   pie_desde_version: bool = False,
                   padre_sintetico=False,
                   renumeraciones: dict | None = None) -> ResultadoParseo:"""
_NUM_V = """                seccion = pila[0]   # las raíces sintéticas cambian pila a mitad de página
                num = m_num.group(1)
"""
_NUM_N = """                seccion = pila[0]   # las raíces sintéticas cambian pila a mitad de página
                num = m_num.group(1)
                if renumeraciones and (to, linea.pagina, num) in renumeraciones:
                    avisos.append({"tipo": "renumerado_por_lista", "pagina": linea.pagina, "impreso": num,
                                   "numero": renumeraciones[(to, linea.pagina, num)], "texto": linea.texto[:90]})
                    num = renumeraciones[(to, linea.pagina, num)]
"""
_PADRE_V = """                    if padre is None:
                        motivo = f"padre_{padre_num}_no_abierto"
                    else:
"""
_PADRE_N = """                    if padre is None and padre_sintetico and len(comp) >= 3 and titulo_mayuscula and (
                            padre_sintetico is True or (to, padre_num) in padre_sintetico):
                        abuelo_num = ".".join(str(c) for c in comp[:-2])
                        abuelo = next((n for n in pila if (n.tipo == "seccion" and len(comp) == 3)
                                       or (n.tipo == "punto" and n.numero == abuelo_num)), None)
                        tios = [h for h in abuelo.hijos if h.tipo == "punto"] if abuelo is not None else []
                        ultimo_tio = _componentes(tios[-1].numero)[-1] if tios else 0
                        if abuelo is not None and comp[-2] > ultimo_tio:
                            if comp[-2] != ultimo_tio + 1:
                                saltos.append({"tipo": "salto_hermano", "padre": abuelo.numero,
                                               "de": ultimo_tio, "a": comp[-2], "pagina": linea.pagina})
                            cerrar_hasta(abuelo)
                            padre = Nodo(tipo="punto", numero=padre_num, titulo="", pagina=linea.pagina,
                                         padre=abuelo, sintetica=True)
                            abuelo.hijos.append(padre)
                            pila.append(padre)
                            avisos.append({"tipo": "padre_sintetico", "numero": padre_num, "hijo": num,
                                           "pagina": linea.pagina, "texto": linea.texto[:90]})
                    if padre is None:
                        motivo = f"padre_{padre_num}_no_abierto"
                    else:
"""
_ESC_V = """        return E0.parsear_cuerpo(to, archivo, paginas, roles, mayusculas_repetidas=rep,
                                 pie_desde_version=True, **kw), rep"""
_ESC_N = """        return E0.parsear_cuerpo(to, archivo, paginas, roles, mayusculas_repetidas=rep,
                                 pie_desde_version=True,
                                 padre_sintetico=(True if VARIANTE_E0 in ("A", "AB") else PADRES_SINTETICOS_E0),
                                 renumeraciones=RENUMERACIONES_E0 if VARIANTE_E0 in ("AB", "ABL") else None,
                                 **kw), rep"""


def _reemplazar(src: str, viejo: str, nuevo: str, nombre: str) -> str:
    if src.count(viejo) != 1:
        raise SystemExit(f"{nombre}: el texto a reemplazar aparece {src.count(viejo)} veces")
    return src.replace(viejo, nuevo)


def cargar_modulos(variante: str):
    """e0_lib y correr_e0 de la copia; con A o AB, desde su texto con los reemplazos, registrados en sys.modules."""
    if variante == "base":
        import e0_lib as E0, correr_e0 as CE   # noqa: E401, PLC0415
        return E0, CE
    src = (E0_DIR / "e0_lib.py").read_text(encoding="utf-8")
    src = _reemplazar(src, _FIRMA_V, _FIRMA_N, "firma de parsear_cuerpo")
    src = _reemplazar(src, _NUM_V, _NUM_N, "número del encabezado")
    src = _reemplazar(src, _PADRE_V, _PADRE_N, "padre no abierto")
    E0 = types.ModuleType("e0_lib")
    E0.__file__ = str(E0_DIR / "e0_lib.py")
    sys.modules["e0_lib"] = E0
    exec(compile(src, E0.__file__, "exec"), E0.__dict__)
    src_c = (E0_DIR / "correr_e0.py").read_text(encoding="utf-8")
    src_c = _reemplazar(src_c, _ESC_V, _ESC_N, "escalera de e0-r2")
    CE = types.ModuleType("correr_e0")
    CE.__file__ = str(E0_DIR / "correr_e0.py")
    CE.__dict__.update({"VARIANTE_E0": variante, "RENUMERACIONES_E0": RENUMERACIONES_AB,
                        "PADRES_SINTETICOS_E0": PADRES_SINTETICOS_LISTA})
    sys.modules["correr_e0"] = CE
    exec(compile(src_c, CE.__file__, "exec"), CE.__dict__)
    return E0, CE


class ManifiestoMinimo:
    """Lo que `correr_e0.correr` usa de un manifiesto, para TOs de la partición (como r2_codigo/r5_escalera_particion)."""
    tiene_oraculo = False
    mapa_territorio = None

    def __init__(self, ids: list[str]):
        self.ids = list(ids)

    def archivo_de(self, t: str) -> str:
        return f"{t}.pdf"

    def pdf_de(self, t: str) -> Path:
        return PDFS / f"{t}.pdf"


def tos_particion() -> list[str]:
    c = json.loads((PARTICION / "conteos_b584.json").read_text(encoding="utf-8"))
    return sorted(t for t, v in c.items() if isinstance(v, dict))


def _fuera_del_repo(d: Path) -> None:
    if Path(d).resolve().is_relative_to(RAIZ.resolve()):
        raise SystemExit(f"--salida dentro del repo: {d}")


def parsear_152(variante: str) -> dict:
    """Árbol de E0 (escalera de e0-r2) de cada TO de la partición: sha256 de la estructura serializada y los
    avisos de padre sintético o renumeración."""
    E0, CE = cargar_modulos(variante)
    out = OrderedDict()
    for to in tos_particion():
        pdf = PDFS / f"{to}.pdf"
        paginas = E0.extraer_lineas(pdf)
        roles = E0.clasificar_paginas(paginas)
        res, *_ = CE.escalera_e0_r2(to, f"{to}.pdf", paginas, roles)
        ser = json.dumps(E0.serializar_estructura(res), ensure_ascii=False, sort_keys=True)
        out[to] = {"sha256_estructura": hashlib.sha256(ser.encode("utf-8")).hexdigest(),
                   "avisos_nuevos": [a for a in res.avisos if a["tipo"] in ("padre_sintetico", "renumerado_por_lista")],
                   "rechazos_padre_no_abierto": [r for r in res.rechazos_header if r["motivo"].startswith("padre_")]}
    return out


def _chunks(d: Path, to: str) -> list[dict]:
    p = Path(d) / f"chunks_{to}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else []


def comparar(base: Path, var: Path) -> dict:
    tos = sorted(p.stem.split("_", 1)[1] for p in Path(base).glob("chunks_*.json"))
    out = OrderedDict()
    for to in tos:
        cb, cv = _chunks(base, to), _chunks(var, to)
        ib, iv = [c["id"] for c in cb], [c["id"] for c in cv]
        tb, tv = {c["id"]: c for c in cb}, {c["id"]: c for c in cv}
        comunes = [i for i in ib if i in tv]
        texto = [i for i in comunes if tb[i]["texto"] != tv[i]["texto"]]
        herencia = [i for i in comunes if tb[i]["texto"] == tv[i]["texto"] and tb[i]["herencia"] != tv[i]["herencia"]]
        otros = [i for i in comunes if i not in texto and i not in herencia and tb[i] != tv[i]]
        out[to] = OrderedDict([
            ("chunks_base", len(cb)), ("chunks_variante", len(cv)),
            ("ids_nuevos", [i for i in iv if i not in tb]), ("ids_que_desaparecen", [i for i in ib if i not in tv]),
            ("orden_igual_en_comunes", [i for i in ib if i in tv] == [i for i in iv if i in tb]),
            ("texto_propio_cambia", texto), ("solo_herencia_cambia", herencia), ("otros_campos_cambian", otros),
            ("archivos_iguales", sorted(p.name for p in Path(base).glob(f"*_{to}.json")
                                        if (Path(var) / p.name).exists()
                                        and (Path(var) / p.name).read_bytes() == p.read_bytes()))])
    return out


def resumen_chunk(d: Path, to: str, cid: str) -> dict | None:
    c = next((x for x in _chunks(d, to) if x["id"] == cid), None)
    if c is None:
        return None
    return {"id": cid, "paginas": c["paginas"], "chars_propio": c["chars_propio"],
            "herencia": [(h["tipo"], h["unidad_origen"], h["texto"][:80]) for h in c["herencia"]],
            "inicio": c["texto"][:160], "fin": c["texto"][-120:]}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variante", choices=("base", "A", "AB", "AL", "ABL"), default="base")
    ap.add_argument("--correr-manifiesto", type=Path)
    ap.add_argument("--correr-tos", type=str)
    ap.add_argument("--parsear-152", action="store_true")
    ap.add_argument("--comparar", action="store_true")
    ap.add_argument("--base", type=Path)
    ap.add_argument("--variante-dir", type=Path)
    ap.add_argument("--salida", type=Path)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    if a.correr_manifiesto or a.correr_tos:
        _fuera_del_repo(a.salida)
        E0, CE = cargar_modulos(a.variante)
        if a.correr_manifiesto:
            import manifiesto_corpus as MC   # noqa: PLC0415
            man = MC.cargar(a.correr_manifiesto)
        else:
            man = ManifiestoMinimo(tos_particion() if a.correr_tos == "todos" else a.correr_tos.split(","))
        CE.correr(a.salida, manifiesto=man, version_e0="e0-r2")
        print("listo", a.variante, a.salida)
        return
    if a.parsear_152:
        r = parsear_152(a.variante)
        (RAIZ / a.out).write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(a.variante, sum(1 for v in r.values() if v["avisos_nuevos"]),
              sum(len(v["rechazos_padre_no_abierto"]) for v in r.values()))
        return
    if a.comparar:
        r = comparar(a.base, a.variante_dir)
        extra = {"ric::4.3.3": resumen_chunk(a.variante_dir, "ric", "ric::4.3.3"),
                 "ric::4.4.3": resumen_chunk(a.variante_dir, "ric", "ric::4.4.3"),
                 "ric::4.4.4": resumen_chunk(a.variante_dir, "ric", "ric::4.4.4"),
                 "ric::4.4.1": resumen_chunk(a.variante_dir, "ric", "ric::4.4.1"),
                 "ric::4.4.2": resumen_chunk(a.variante_dir, "ric", "ric::4.4.2"),
                 "ric::4.3.3_base": resumen_chunk(a.base, "ric", "ric::4.3.3")}
        (RAIZ / a.out).write_text(json.dumps({"por_to": r, "chunks_de_ric": extra}, ensure_ascii=False, indent=1)
                                  + "\n", encoding="utf-8")
        for to, v in r.items():
            if v["ids_nuevos"] or v["ids_que_desaparecen"] or v["texto_propio_cambia"] or v["solo_herencia_cambia"]:
                print(to, "nuevos", v["ids_nuevos"], "desaparecen", v["ids_que_desaparecen"],
                      "texto", v["texto_propio_cambia"][:8], "herencia", len(v["solo_herencia_cambia"]))
        return
    ap.error("elegí un modo")


if __name__ == "__main__":
    main()
