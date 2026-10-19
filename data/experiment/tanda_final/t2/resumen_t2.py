"""
resumen_t2.py — B6.1, tanda final, T2: el resumen que el cegamiento de U-MED-VERIF deja reportar (pre-registro firmado de
la tanda final, §4.1; pre-registro de la tanda 1, §7; despacho de T1 de la tanda final, punto 1.5). Es el de la tanda 1
(data/experiment/tanda1/t2/resumen_t2.py), con las rutas de la tanda final y sin otro cambio. USD 0, sin red. Solo lee; imprime y, con --out, escribe lo mismo en JSON.

Por TO y en total:
  - unidades: las de la E0 (rutas.e0_salida del manifiesto), y con las partes por corte (una unidad partida cuenta
    por sus partes; particiones_por_corte.json, runner_corpus.py:562-579);
  - aceptadas: los tres estados de aceptación de E3 juntos (completo_ok_directo, aceptado_con_residuales y
    aceptado_tras_reintento; ratchet_e3.ESTADOS), del último expediente de cada unidad en finales.jsonl;
  - cola: los tres estados de cola humana juntos;
  - errores: las unidades con un error definitivo en su último registro de E1 (extracciones_e1.jsonl), que no
    llegan a E3; la partida por corte no cuenta (la reemplazan sus partes);
  - ids repetidos: en la E0;
  - cobertura: que cada unidad (con partes) tenga destino (aceptada, cola o error), y la cobertura exacta de la E0
    (cobertura.json);
  - gasto: el del TO (sus dos fases cerradas, o la abierta) y el global (Estado.gasto_global, runner_corpus.py:373-378)
    contra el tope.
De la salida de pantalla del runner (--consola, el NO_ABRIR_ de T2, leído solo por este script) toma solo las líneas
`FRENO:` y `ERROR:` y la de `corrida completa` (runner_corpus.py:1453, :1458, :1462), con el TO de la línea
`### lanzar_t2:` que las precede.
No imprime ni escribe el desglose por estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`,
las `marcas_e3` ni el gasto de los reintentos aparte: eso es de conteos_t2.py.

Uso: <python> -B resumen_t2.py --repo <raíz> [--salida <salida del runner>] [--consola <archivo>] [--out <json>]
     (por defecto, la --salida y la consola de T2)
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True

ACEPTADAS = ("completo_ok_directo", "aceptado_con_residuales", "aceptado_tras_reintento")
COLA = ("cola_humana", "cola_humana_veredicto_inutilizable", "cola_humana_reextraccion_invalida")
PARTICIONADA = "particionada_por_corte"
MANIFIESTO_REL = "data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json"
SALIDA_REL = "data/experiment/reextraccion_v2/corpus_tanda_final/salida_r2b"
CONSOLA_REL = "data/experiment/tanda_final/t2/NO_ABRIR_salida_e3_tanda_final.txt"


def last_wins(p: Path) -> dict[str, dict]:
    out = {}
    if p.exists():
        for x in p.read_text(encoding="utf-8").splitlines():
            if x.strip():
                r = json.loads(x)
                out[r["chunk_id"]] = r
    return out


def lineas_permitidas(consola: Path) -> list[dict]:
    if not consola.exists():
        return []
    out, to = [], None
    for x in consola.read_text(encoding="utf-8").splitlines():
        s = x.strip()
        if s.startswith("### lanzar_t2: "):
            to = s.split()[2]
        elif s.startswith(("FRENO:", "ERROR:", "corrida completa")):
            out.append({"to": to, "linea": s})
    return out


def resumir(repo: Path, salida: Path, consola: Path) -> dict:
    man = json.loads((repo / MANIFIESTO_REL).read_text(encoding="utf-8"))
    e0 = repo / man["rutas"]["e0_salida"]
    cobertura_e0 = json.loads((e0 / "cobertura.json").read_text(encoding="utf-8"))
    tope = man["limites"]["tope_global_usd"]
    estado = json.loads((salida / "estado_corpus.json").read_text(encoding="utf-8")) \
        if (salida / "estado_corpus.json").exists() else {"fases_cerradas": {}, "fase_actual": None}
    filas, tot = {}, Counter()
    for to in man["orden_corrida"]:
        tdir = salida / to
        chunks = json.loads((e0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
        ids = Counter(c["id"] for c in chunks)
        partes = json.loads((tdir / "particiones_por_corte.json").read_text(encoding="utf-8")) \
            if (tdir / "particiones_por_corte.json").exists() else {}
        con_partes = [p["id"] for c in chunks for p in (partes[c["id"]]["partes"] if c["id"] in partes else [c])]
        fin = last_wins(tdir / "finales.jsonl")
        e1 = last_wins(tdir / "extracciones_e1.jsonl")
        aceptadas = sum(1 for u in con_partes if (fin.get(u) or {}).get("estado") in ACEPTADAS)
        cola = sum(1 for u in con_partes if (fin.get(u) or {}).get("estado") in COLA)
        errores = sum(1 for u in con_partes if u not in fin and (e1.get(u) or {}).get("error") not in (None, PARTICIONADA))
        otros = sum(1 for u in con_partes if u in fin and fin[u].get("estado") not in ACEPTADAS + COLA)
        gasto_to = 0.0
        for fase in ("e1", "e3"):
            k = f"{to}:{fase}"
            if k in estado["fases_cerradas"]:
                gasto_to += estado["fases_cerradas"][k]["gasto_usd"]
            elif (estado.get("fase_actual") or {}).get("key") == k:
                gasto_to += estado["fase_actual"]["gasto_previo_usd"] + estado["fase_actual"]["gasto_proceso_usd"]
        cerrado = all(f"{to}:{f}" in estado["fases_cerradas"] for f in ("e1", "e3"))
        filas[to] = {"unidades": len(chunks), "unidades_con_partes": len(con_partes), "aceptadas": aceptadas,
                     "cola": cola, "errores": errores, "estado_fuera_del_vocabulario": otros,
                     "sin_destino": len(con_partes) - aceptadas - cola - errores - otros,
                     "ids_repetidos": sum(v - 1 for v in ids.values() if v > 1),
                     "cobertura_completa": aceptadas + cola + errores == len(con_partes),
                     "cobertura_exacta_e0": cobertura_e0[to]["cobertura_exacta"],
                     "fases_cerradas": cerrado, "gasto_usd": round(gasto_to, 6)}
        for k in ("unidades", "unidades_con_partes", "aceptadas", "cola", "errores", "estado_fuera_del_vocabulario",
                  "sin_destino", "ids_repetidos"):
            tot[k] += filas[to][k]
        tot["gasto_usd"] += gasto_to
    g = sum(f["gasto_usd"] for f in estado["fases_cerradas"].values())
    fa = estado.get("fase_actual")
    if fa:
        g += fa["gasto_previo_usd"] + fa["gasto_proceso_usd"]
    return {"por_to": filas, "total": {**{k: v for k, v in tot.items() if k != "gasto_usd"},
                                        "gasto_por_to_sumado_usd": round(tot["gasto_usd"], 6),
                                        "tos_cerrados": sum(f["fases_cerradas"] for f in filas.values())},
            "gasto_global_usd": round(g, 6), "tope_usd": tope, "dentro_del_tope": g <= tope,
            "lineas_del_runner": lineas_permitidas(consola)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--salida", type=Path, default=None)
    ap.add_argument("--consola", type=Path, default=None)
    ap.add_argument("--out", type=Path, default=None)
    a = ap.parse_args()
    repo = a.repo.resolve()
    r = resumir(repo, (a.salida or repo / SALIDA_REL).resolve(), (a.consola or repo / CONSOLA_REL).resolve())
    print(f"{'TO':<10} {'unid':>5} {'c/part':>6} {'acept':>6} {'cola':>5} {'err':>4} {'s/dest':>6} {'idsrep':>6} "
          f"{'cob':>4} {'cobE0':>5} {'gasto':>9}")
    for to, f in r["por_to"].items():
        print(f"{to:<10} {f['unidades']:>5} {f['unidades_con_partes']:>6} {f['aceptadas']:>6} {f['cola']:>5} "
              f"{f['errores']:>4} {f['sin_destino']:>6} {f['ids_repetidos']:>6} {str(f['cobertura_completa'])[0]:>4} "
              f"{str(f['cobertura_exacta_e0'])[0]:>5} {f['gasto_usd']:>9.4f}")
    t = r["total"]
    print(f"{'total':<10} {t['unidades']:>5} {t['unidades_con_partes']:>6} {t['aceptadas']:>6} {t['cola']:>5} "
          f"{t['errores']:>4} {t['sin_destino']:>6} {t['ids_repetidos']:>6}")
    print(f"gasto global USD {r['gasto_global_usd']:.4f} de un tope de USD {r['tope_usd']} "
          f"({'dentro' if r['dentro_del_tope'] else 'FUERA'} del tope); TOs con las dos fases cerradas: {t['tos_cerrados']}")
    for x in r["lineas_del_runner"]:
        print(f"[{x['to']}] {x['linea']}")
    if a.out:
        a.out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
