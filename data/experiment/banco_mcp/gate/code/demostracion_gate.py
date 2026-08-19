#!/usr/bin/env python3
"""demostracion_gate.py — Entregable 5 de U-A2.0-gate: demostración por clase.

Para cada caso adaptado (`corrida/trazas/GATE-*.json`) computa la atribución con
el código de A0.2 **importado**, no reimplementado:

    from atribucion_fallas import atribuir_payload, clasificar

`atribuir_payload` a su vez importa `metrica.evaluar_traza` (sintéticas, sin
editar) y `metrica_ev2.verificar_steps_full` (replay fuerte). Este módulo no
define ninguna regla: solo arma los argumentos (mini-grafo propio + anclas +
veredicto declarado) y contrasta la clase obtenida contra la esperada.

Verificaciones:
  1. clase esperada vs obtenida, por caso.
  2. replay estándar y replay FUERTE por caso.
  3. determinismo: dos corridas de la atribución, comparadas byte a byte.
  4. determinismo del adaptador: las trazas re-adaptadas desde la rebanada
     cruda son byte-idénticas salvo `meta.generado`.

Costo USD 0: todo es re-ejecución determinística sobre un mini-grafo local.

Uso:
  python3 -B demostracion_gate.py [--out ../corrida]
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

GATE_DIR = Path(__file__).resolve().parents[1]
CODE_DIR = GATE_DIR / "code"
EXPERIMENT_DIR = GATE_DIR.parents[1]
REPO_DIR = EXPERIMENT_DIR.parents[1]
A02_CODE = EXPERIMENT_DIR / "ev2_reporte" / "code"

for _p in (str(A02_CODE), str(CODE_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

# Código de A0.2, IMPORTADO tal cual (85d9fdb). Trae consigo, por su propia
# cadena de imports, metrica.evaluar_traza y metrica_ev2.verificar_steps_full.
from atribucion_fallas import atribuir_payload, clasificar, resolver_anclas   # noqa: E402
import tools_juguete as TJ                                                    # noqa: E402

TRAZAS_DIR = GATE_DIR / "corrida" / "trazas"
CASOS_PATH = GATE_DIR / "casos_gate.json"
REBANADA = GATE_DIR / "sesiones" / "rebanada_cruda.jsonl"


def _sin_generado(p: Path) -> str:
    d = json.loads(p.read_text(encoding="utf-8"))
    d.get("meta", {}).pop("generado", None)
    return json.dumps(d, ensure_ascii=False, sort_keys=True)


def determinismo_adaptador(rebanada: Path, trazas_dir: Path, casos_path: Path) -> dict:
    """Re-adapta la rebanada a un directorio temporal y compara con lo persistido."""
    with tempfile.TemporaryDirectory() as td:
        r = subprocess.run([sys.executable, "-B", str(CODE_DIR / "adaptador_cc.py"), "adaptar",
                            "--rebanada", str(rebanada), "--out", td, "--casos", str(casos_path)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            return {"ok": False, "motivo": r.stderr[-500:]}
        difs = []
        for p in sorted(trazas_dir.glob("GATE-*.json")):
            q = Path(td) / p.name
            if not q.exists():
                difs.append(f"{p.name}: ausente en la re-adaptación")
            elif _sin_generado(p) != _sin_generado(q):
                difs.append(f"{p.name}: contenido distinto")
        return {"ok": not difs, "n_trazas": len(list(trazas_dir.glob('GATE-*.json'))),
                "diferencias": difs,
                "nota": "comparación byte a byte del JSON canónico salvo `meta.generado`"}


def correr(out_dir: Path, casos_path: Path = CASOS_PATH, trazas_dir: Path = TRAZAS_DIR,
           rebanada: Path = REBANADA, nombre: str = "demostracion_gate") -> dict:
    casos = {c["caso_id"]: c for c in json.loads(casos_path.read_text(encoding="utf-8"))["casos"]}
    index = TJ.cargar_index()
    aidx = TJ.cargar_ancla_index()

    filas = []
    for caso_id, decl in casos.items():
        p = trazas_dir / f"{caso_id}.json"
        payload = json.loads(p.read_text(encoding="utf-8"))
        anclas = decl["anclas"]
        veredicto = decl["veredicto"]
        censo = {a: resolver_anclas([a], aidx)[a] for a in anclas}
        fila = {"caso_id": caso_id, "contrato": decl.get("contrato", "v1"),
                "anclas": anclas, "censo_nodos": censo, "veredicto": veredicto,
                "clase_esperada": decl["clase_esperada"],
                "n_steps": len(payload["trace"]["steps"]),
                "corte_sesion": payload["gate"]["corte_sesion"],
                "atribuible_por_el_adaptador": payload["gate"]["atribuible"]}
        try:
            a1 = atribuir_payload(payload, anclas, aidx, index, veredicto)
            a2 = atribuir_payload(payload, anclas, aidx, index, veredicto)
            fila["determinismo_atribucion"] = (json.dumps(a1, sort_keys=True, ensure_ascii=False)
                                               == json.dumps(a2, sort_keys=True, ensure_ascii=False))
            fila.update({"clase_obtenida": a1["clase"], "ancla_presente": a1["ancla_presente"],
                         "ancla_vista": a1["ancla_vista"], "ancla_consultada": a1["ancla_consultada"],
                         "replay_ok": a1["replay_ok"], "replay_fuerte_ok": a1["replay_fuerte_ok"],
                         "replay_fallas": a1["replay_fallas"],
                         "replay_fuerte_fallas": a1["replay_fuerte_fallas"],
                         "por_ancla": a1["por_ancla"]})
            fila["error_atribucion"] = None
        except Exception as e:                       # el error también es dato del gate
            fila["error_atribucion"] = f"{type(e).__name__}: {e}"
            fila["clase_obtenida"] = None
        # PASS/FAIL: la clase coincide Y el replay (estándar y fuerte) pasa Y es determinística.
        # Un caso marcado no-atribuible por el adaptador PASA si el adaptador lo detectó
        # (la falla esperada es que el adaptador la declare, no que la atribución acierte).
        if not fila["atribuible_por_el_adaptador"]:
            fila["veredicto_caso"] = "PASS (detectado como no atribuible)"
            fila["clase_si_se_atribuyera_igual"] = fila.get("clase_obtenida")
        else:
            ok = (fila.get("clase_obtenida") == decl["clase_esperada"]
                  and fila.get("replay_ok") and fila.get("replay_fuerte_ok")
                  and fila.get("determinismo_atribucion"))
            fila["veredicto_caso"] = "PASS" if ok else "FAIL"
        filas.append(fila)

    det = determinismo_adaptador(rebanada, trazas_dir, casos_path)
    res = {"generado": datetime.now().isoformat(timespec="seconds"),
           "unidad": "U-A2.0-gate — entregable 5 (demostración por clase)",
           "codigo_a02_importado": str(A02_CODE.relative_to(REPO_DIR)),
           "grafo_juguete": "data/experiment/banco_mcp/gate/grafo_juguete.json",
           "determinismo_adaptador": det,
           "_nombre": nombre,
           "n_casos": len(filas),
           "n_pass": sum(1 for f in filas if f["veredicto_caso"].startswith("PASS")),
           "casos": filas}
    out_dir.mkdir(parents=True, exist_ok=True)
    nombre = res.pop("_nombre", "demostracion_gate")
    (out_dir / f"{nombre}.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / f"{nombre}.md").write_text(render(res), encoding="utf-8")
    return res


def render(res: dict) -> str:
    L = ["# Demostración por clase — U-A2.0-gate (entregable 5)", "",
         f"Casos: {res['n_casos']} | PASS: {res['n_pass']}", "",
         "| caso | contrato | ancla | veredicto | clase esperada | clase obtenida | presente | vista | consultada | replay | replay fuerte | determinismo | PASS/FAIL |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for f in res["casos"]:
        L.append("| {caso} | {c} | {a} | {v} | {ce} | {co} | {p} | {vi} | {cs} | {r} | {rf} | {d} | {res} |".format(
            caso=f["caso_id"], c=f["contrato"], a=",".join(f["anclas"]), v=f["veredicto"],
            ce=f["clase_esperada"], co=f.get("clase_obtenida") or "—",
            p=f.get("ancla_presente"), vi=f.get("ancla_vista"), cs=f.get("ancla_consultada"),
            r=f.get("replay_ok"), rf=f.get("replay_fuerte_ok"),
            d=f.get("determinismo_atribucion"), res=f["veredicto_caso"]))
    L += ["", "## Determinismo del adaptador", "",
          f"- re-adaptación desde la rebanada cruda: `ok = {res['determinismo_adaptador']['ok']}` "
          f"sobre {res['determinismo_adaptador'].get('n_trazas')} trazas "
          f"({res['determinismo_adaptador'].get('nota')})",
          f"- diferencias: {res['determinismo_adaptador'].get('diferencias')}", ""]
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=GATE_DIR / "corrida")
    ap.add_argument("--casos", type=Path, default=CASOS_PATH)
    ap.add_argument("--trazas", type=Path, default=TRAZAS_DIR)
    ap.add_argument("--rebanada", type=Path, default=REBANADA)
    ap.add_argument("--nombre", default="demostracion_gate")
    a = ap.parse_args()
    res = correr(a.out, a.casos, a.trazas, a.rebanada, a.nombre)
    print(render(res))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
