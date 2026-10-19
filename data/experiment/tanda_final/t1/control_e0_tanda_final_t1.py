"""Controles de la E0 de la tanda final contra el manifiesto de S0-6b (tanda final de B6.1, T1, punto 2.2; solo lectura).

Adapta a los 98 TOs de la tanda final (S2c) el control de la tanda 1
(`tanda1/t1/control_e0_tanda1_t1.py`), que adapta a su vez el de S2
(`segmentacion_oficial_e0r2/s2/scripts/control_e0_contra_manifiesto_S2.py`, que controla los 152). Tres modos:

  codigo --raiz <raíz mínima> --manifiesto <S0-6b> --out <json>
      e0_lib.py, correr_e0.py y e0_tablas.py de la raíz contra `codigo_sha256` del manifiesto.

  e0 --e0 <corrida 1 de los 98> --e0-bis <corrida 2 de los 98> --e0-152 <corrida de los 152>
     --manifiesto <S0-6b> --manifiesto-s1ter <152 de S1-ter> --lista <s2/cifras/tanda_final_S2c.json>
     --pdfs <dir> [--pdfs <dir> ...] --out <json>
      - los 490 archivos por TO (chunks_, estructura_, indice_, pies_ y tablas_ de cada uno): sha256 y bytes de su
        entrada `e0/<archivo>` del manifiesto;
      - el primer nivel de la corrida: los 490, los agregados no vacíos y version_e0.json, y nada más (`por_to/` no
        cuenta);
      - cada agregado, como JSON leído, igual al de la corrida de los 152 restringido a las claves de los 98; si
        falta, el de los 152 restringido tiene que dar vacío (`correr_152.py:81-93` no escribe el vacío);
      - version_e0.json con el sha256 de su entrada del manifiesto;
      - las unidades: cada TO con su `unidades_por_to` del manifiesto y la suma en 4.951 (la U de la versión derivada);
      - las dos corridas de los 98, iguales byte a byte (el árbol entero, con `por_to/`);
      - cada PDF de los 98, en cada carpeta de --pdfs, con el `sha256_pdf` de su entrada en el manifiesto de S1-ter.

  hc --resumen <resumen de esta corrida> --referencia <resumen de S2c> --out <json>
      las diferencias entre los dos resúmenes del health-check, campo por campo.

No imprime texto de unidades: solo nombres de archivo, sha256, bytes y cuentas.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True

AGREGADOS = ("divergencias_indice_cuerpo.json", "conteos.json", "cobertura.json", "correcciones.json",
             "sub_chunking.json", "encabezados_conservados.json", "ids_desambiguados.json")
POR_TO = ("chunks", "estructura", "indice", "pies", "tablas")
U_ESPERADA = 4951
N_TOS = 98


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def leer(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def sin_usuario(p: Path) -> str:
    """La ruta sin la carpeta personal: `<scratchpad>/…` para el scratchpad de la sesión y `$HOME/…` para el resto."""
    s = str(p)
    if "/scratchpad/" in s:
        return "<scratchpad>/" + s.split("/scratchpad/", 1)[1]
    return s.replace(str(Path.home()), "$HOME")


def modo_codigo(a) -> dict:
    m = leer(a.manifiesto)
    d = a.raiz / "data/experiment/reextraccion_v2/e0_chunking"
    filas = {n: {"esperado": h, "raiz": sha(d / n) if (d / n).is_file() else None}
             for n, h in m["codigo_sha256"].items()}
    for f in filas.values():
        f["igual"] = f["esperado"] == f["raiz"]
    ok = len(filas) == 3 and all(f["igual"] for f in filas.values())
    return {"manifiesto_sha256": sha(a.manifiesto), "codigo": filas, "veredicto": "OK" if ok else "FALLA"}


def arbol(d: Path) -> dict[str, str]:
    return {str(p.relative_to(d)): sha(p) for p in sorted(d.rglob("*")) if p.is_file()}


def modo_e0(a) -> dict:
    m = leer(a.manifiesto)
    s1t = {t["id"]: t for t in leer(a.manifiesto_s1ter)["tos"]}
    tos = list(leer(a.lista)["tanda_final"]["lista"])
    esperados = {k[len("e0/"):]: v for k, v in m["sha256"].items() if k.startswith("e0/")}

    # 1. los 490 archivos por TO
    por_to = {}
    for to in tos:
        for pre in POR_TO:
            n = f"{pre}_{to}.json"
            p = a.e0 / n
            e = esperados.get(n)
            por_to[n] = {"existe": p.is_file(), "en_manifiesto": e is not None,
                         "igual": bool(p.is_file() and e and sha(p) == e["sha256"] and p.stat().st_size == e["bytes"])}
    n_por_to_iguales = sum(v["igual"] for v in por_to.values())

    # 2. los agregados contra los de los 152 restringidos a los 98
    agregados = {}
    for n in AGREGADOS:
        p152 = a.e0_152 / n
        v152 = leer(p152) if p152.is_file() else {}
        restr = {k: v for k, v in v152.items() if k in tos}
        p98 = a.e0 / n
        if p98.is_file():
            v98 = leer(p98)
            agregados[n] = {"en_los_98": True, "claves_98": len(v98), "claves_152_restringido": len(restr),
                            "igual": v98 == restr, "mismo_orden_de_claves": list(v98) == list(restr)}
        else:
            agregados[n] = {"en_los_98": False, "claves_152_restringido": len(restr), "igual": restr == {}}
    agregados_ok = all(v["igual"] for v in agregados.values())

    # 3. version_e0.json
    pv = a.e0 / "version_e0.json"
    ev = esperados["version_e0.json"]
    version_ok = pv.is_file() and sha(pv) == ev["sha256"] and pv.stat().st_size == ev["bytes"]

    # 4. el primer nivel: nada que falte ni que sobre
    primer_nivel = {p.name for p in a.e0.iterdir() if p.is_file()}
    esperado_nivel = set(por_to) | {n for n, v in agregados.items() if v["en_los_98"]} | {"version_e0.json"}
    faltan = sorted(esperado_nivel - primer_nivel)
    sobran = sorted(primer_nivel - esperado_nivel)

    # 5. unidades
    upt = m["unidades_por_to"]
    unidades = {to: len(leer(a.e0 / f"chunks_{to}.json")) for to in tos}
    unidades_ok = all(unidades[t] == upt[t] for t in tos) and sum(unidades.values()) == U_ESPERADA

    # 6. las dos corridas de los 98
    ta, tb = arbol(a.e0), arbol(a.e0_bis)
    corridas_iguales = ta == tb
    distintos_ab = sorted(k for k in set(ta) | set(tb) if ta.get(k) != tb.get(k))

    # 7. los PDF
    pdfs = {}
    for i, d in enumerate(a.pdfs):
        for to in tos:
            p = d / f"{to}.pdf"
            pdfs[f"pdfs[{i}]/{to}.pdf"] = {
                "existe": p.is_file(), "igual": p.is_file() and sha(p) == s1t[to]["sha256_pdf"],
                "ruta_manifiesto_s1ter": s1t[to]["pdf"]}
    pdfs_ok = len(pdfs) == N_TOS * len(a.pdfs) and all(v["igual"] for v in pdfs.values())

    ok = (len(tos) == N_TOS and n_por_to_iguales == 5 * N_TOS and agregados_ok and version_ok and not faltan and not sobran
          and unidades_ok and corridas_iguales and pdfs_ok)
    return {"manifiesto_sha256": sha(a.manifiesto), "manifiesto_s1ter_sha256": sha(a.manifiesto_s1ter),
            "lista_sha256": sha(a.lista), "tos": tos, "n_tos": len(tos),
            "por_to_iguales": n_por_to_iguales, "por_to_esperados": len(por_to),
            "por_to_distintos": sorted(n for n, v in por_to.items() if not v["igual"]),
            "agregados": agregados, "agregados_iguales": agregados_ok,
            "version_e0_igual": version_ok, "primer_nivel": len(primer_nivel), "faltan": faltan, "sobran": sobran,
            "unidades_por_to": unidades, "unidades": sum(unidades.values()), "unidades_ok": unidades_ok,
            "corridas_98_iguales": corridas_iguales, "archivos_corrida_1": len(ta), "archivos_corrida_2": len(tb),
            "distintos_entre_corridas": distintos_ab,
            "carpetas_pdfs": [sin_usuario(d) for d in a.pdfs],
            "pdfs": pdfs, "pdfs_iguales": sum(v["igual"] for v in pdfs.values()), "pdfs_ok": pdfs_ok,
            "veredicto": "OK" if ok else "FALLA"}


def diferencias(x, y, ruta="") -> list[str]:
    if isinstance(x, dict) and isinstance(y, dict):
        out = []
        for k in sorted(set(x) | set(y)):
            if k not in x:
                out.append(f"{ruta}/{k}: solo en la referencia")
            elif k not in y:
                out.append(f"{ruta}/{k}: solo en esta corrida")
            else:
                out += diferencias(x[k], y[k], f"{ruta}/{k}")
        return out
    return [] if x == y else [f"{ruta}: {json.dumps(x, ensure_ascii=False)} != {json.dumps(y, ensure_ascii=False)}"]


def modo_hc(a) -> dict:
    r, ref = leer(a.resumen), leer(a.referencia)
    d = diferencias(r, ref)
    return {"resumen_sha256": sha(a.resumen), "referencia_sha256": sha(a.referencia),
            "frena_por_cobertura_o_ids": r["frena_por_cobertura_o_ids"],
            "verde": r["frena_por_cobertura_o_ids"] == [] and r["tos"] == N_TOS,
            "diferencias": d, "n_diferencias": len(d)}


def main() -> None:
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="modo", required=True)
    c = sp.add_parser("codigo")
    c.add_argument("--raiz", type=Path, required=True)
    c.add_argument("--manifiesto", type=Path, required=True)
    c.add_argument("--out", type=Path, required=True)
    e = sp.add_parser("e0")
    for k in ("--e0", "--e0-bis", "--e0-152", "--manifiesto", "--manifiesto-s1ter", "--lista", "--out"):
        e.add_argument(k, type=Path, required=True)
    e.add_argument("--pdfs", type=Path, action="append", required=True)
    h = sp.add_parser("hc")
    for k in ("--resumen", "--referencia", "--out"):
        h.add_argument(k, type=Path, required=True)
    a = ap.parse_args()
    out = {"codigo": modo_codigo, "e0": modo_e0, "hc": modo_hc}[a.modo](a)
    a.out.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    resumen = {k: v for k, v in out.items() if k not in ("pdfs", "agregados", "unidades_por_to", "codigo", "tos")}
    print(json.dumps(resumen, ensure_ascii=False))


if __name__ == "__main__":
    main()
