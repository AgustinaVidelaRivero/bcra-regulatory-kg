"""
generar_pares_v3.py — FASE B (SOLO con autorización explícita, precios y tope):
generación de los pares literal + anti-léxica del material nuevo de la ablación
con el pipeline de sintéticas REUSADO sin editar (`runner_faseB.py` +
`cliente_faseB.py` de 5ceb816), sobre `muestreo/samples_v3.json`.

Reuso por INYECCIÓN DE ATRIBUTOS DE MÓDULO (ningún archivo del pipeline se edita):
  runner_faseB.SAMPLES_PATH      -> archivo de samples de ESTA unidad
  runner_faseB.OUT_CALIBRACION   -> pares/calibracion_faseB_v3.json
  runner_faseB.OUT_FINAL         -> pares/preguntas_faseB_v3.json
  cliente_faseB.TOPE_USD         -> 3.00 (tope propio de U-A1.3; el del pipeline era 4.00)
  ClienteFaseB(db_path=..., run_label=...)  -> db PROPIA cache/ablacion_faseB_v3.db
Todo lo demás (prompts de generación/evolución, checks V1/V2/V3, puertas a/b/c/d,
reintento único de descartadas, modelo claude-sonnet-5 sin temperature y con
thinking deshabilitado, contabilidad de gasto sobre tokens reales) es el del
pipeline, byte a byte. CODE_VER del namespace de caché se conserva
("sinteticas-faseB-v1"): identifica el comportamiento del dominio (prompts +
lógica), que no cambió; la db es otra, así que no hay hits cruzados posibles.

Modos:
  --selftest              stub, 0 API: runner completo sobre samples_v3 (PASS/FAIL)
  --preparar [--estratos] escribe el archivo de samples que verá el runner
                          (subconjunto de estratos si se laudó excluir alguno) — $0
  --calibracion           10 samples (2 por estrato del archivo preparado) -> FRENO
                          informativo: imprime aptos/10 y gasto
  --resto                 el resto, con reintento único; incluye los de calibración
  --todo                  calibracion + gate de cordura + resto en una corrida
                          (gate: si aptos en calibración < GATE_MIN_APTOS, aborta y
                          reporta — el pipeline estaría fallando, no se gasta más)

Gating de gasto (además del tope duro del cliente): exige --autorizado y la
variable de entorno ABLACION_TOPE_USD == "3.00" (la autorización se transcribe).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun_ablacion import (CACHE_DIR, EVAL_DIR, MUESTREO_DIR, PARES_DIR,  # noqa: E402
                            rel_repo, verificar_piezas)

import runner_faseB  # noqa: E402  (pipeline: solo import)

SAMPLES_V3 = MUESTREO_DIR / "samples_v3.json"
SAMPLES_FASEB = MUESTREO_DIR / "samples_v3_faseB.json"     # lo que ve el runner
OUT_CALIBRACION = PARES_DIR / "calibracion_faseB_v3.json"
OUT_FINAL = PARES_DIR / "preguntas_faseB_v3.json"
DB_PATH = CACHE_DIR / "ablacion_faseB_v3.db"
RUN_LABEL = "ablacion_faseB_v3"
TOPE_USD = 3.00
GATE_MIN_APTOS = 3      # de 10 en calibración; 5ceb816 dio 64/98 ≈ 65 %
ESTRATOS_TODOS = ("E-A", "E-B", "E-C", "E-D", "E-E")


def _inyectar_rutas():
    runner_faseB.SAMPLES_PATH = SAMPLES_FASEB
    runner_faseB.OUT_CALIBRACION = OUT_CALIBRACION
    runner_faseB.OUT_FINAL = OUT_FINAL
    PARES_DIR.mkdir(parents=True, exist_ok=True)


def preparar(estratos: list[str]) -> dict:
    """Escribe samples_v3_faseB.json = samples_v3.json filtrado por estrato
    (mismos sample_ids, mismo orden, misma config), y deja registro."""
    with SAMPLES_V3.open(encoding="utf-8") as f:
        data = json.load(f)
    sub = [s for s in data["samples"] if s["estrato"] in estratos]
    out = {**data, "samples": sub,
           "conteo_por_estrato": {e: sum(1 for s in sub if s["estrato"] == e) for e in estratos},
           "fase_b_ablacion": {"origen": rel_repo(SAMPLES_V3), "estratos_incluidos": estratos,
                               "estratos_excluidos": [e for e in ESTRATOS_TODOS if e not in estratos]}}
    MUESTREO_DIR.mkdir(parents=True, exist_ok=True)
    with SAMPLES_FASEB.open("w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"samples para fase B: {len(sub)} {out['conteo_por_estrato']} -> {rel_repo(SAMPLES_FASEB)}")
    return out


# Regex de un objeto JSON plano {"pregunta": "..."} (el único formato que piden
# los prompts de generación/evolución del pipeline).
_OBJ_PREGUNTA = re.compile(r'\{\s*"pregunta"\s*:\s*"(?:[^"\\]|\\.)*"\s*\}')
_MARCA_PROMPT_PREGUNTA = 'Respondé SOLO con un objeto JSON: {"pregunta": "..."}'


def _construir_cliente_tolerante(cliente_faseB):
    """DESVÍO DECLARADO (corrida real 2026-08-17): en 1 respuesta de generación
    (ED-008, reintento 2) Sonnet 5 devolvió DOS bloques ```json``` con un
    comentario entre medio; `generador._parse_pregunta` (estricto: json.loads
    del texto entero sin fences) lanzó JSONDecodeError y el runner abortó sin
    persistir el resto. Corrección en ESTA capa, sin editar generador.py: para
    los prompts de generación/evolución, si el texto entero no parsea, se
    devuelve el PRIMER objeto {"pregunta": "..."} completo (el crudo íntegro
    queda en la db; la pregunta elegida pasa igual por las 4 puertas y V1–V3).
    Cada tolerancia se registra en `parseos_tolerados` y se reporta."""

    class ClienteFaseBTolerante(cliente_faseB.ClienteFaseB):
        def __init__(self, *a, **k):
            super().__init__(*a, **k)
            self.parseos_tolerados = []

        def generar(self, prompt: str) -> str:
            texto = super().generar(prompt)
            if _MARCA_PROMPT_PREGUNTA not in prompt:
                return texto
            t = texto.strip()
            if t.startswith("```"):
                t = t.strip("`")
                if t.lower().startswith("json"):
                    t = t[4:]
            try:
                json.loads(t.strip())
                return texto
            except json.JSONDecodeError:
                m = _OBJ_PREGUNTA.search(texto)
                if not m:
                    return texto          # que falle como antes (sin objeto rescatable)
                self.parseos_tolerados.append({
                    "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
                    "prompt_inicio": prompt[:80], "respuesta_cruda": texto,
                    "objeto_elegido": m.group(0)})
                print(f"  [tolerancia de parseo] respuesta con texto extra; se toma el primer objeto JSON "
                      f"({len(self.parseos_tolerados)} acumuladas)", flush=True)
                return m.group(0)

        def resumen(self) -> dict:
            r = super().resumen()
            r["parseos_tolerados"] = self.parseos_tolerados
            return r

    return ClienteFaseBTolerante


def _cliente():
    from dotenv import load_dotenv
    load_dotenv(EVAL_DIR / ".env")
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit(f"ANTHROPIC_API_KEY no está seteada (esperada en {EVAL_DIR / '.env'}).")
    import cliente_faseB
    cliente_faseB.TOPE_USD = TOPE_USD          # tope propio (atributo de módulo)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    c = _construir_cliente_tolerante(cliente_faseB)(db_path=DB_PATH, run_label=RUN_LABEL)
    print(f"cliente fase B: modelo {cliente_faseB.MODELO}, precios in/out {cliente_faseB.PRECIO_IN_POR_MTOK}/"
          f"{cliente_faseB.PRECIO_OUT_POR_MTOK} USD/MTok, tope {cliente_faseB.TOPE_USD}, db {rel_repo(DB_PATH)}")
    return c


def _gate_autorizacion(args):
    if not args.autorizado:
        raise SystemExit("modo real: falta --autorizado (autorización explícita de la autora).")
    if os.environ.get("ABLACION_TOPE_USD") != f"{TOPE_USD:.2f}":
        raise SystemExit(f"modo real: exportar ABLACION_TOPE_USD={TOPE_USD:.2f} (transcripción del tope autorizado).")
    if not SAMPLES_FASEB.exists():
        raise SystemExit("falta muestreo/samples_v3_faseB.json: correr --preparar primero.")


def main() -> int:
    ap = argparse.ArgumentParser(description="Fase B de U-A1.3 (generación de pares v3).")
    modo = ap.add_mutually_exclusive_group(required=True)
    modo.add_argument("--selftest", action="store_true")
    modo.add_argument("--preparar", action="store_true")
    modo.add_argument("--calibracion", action="store_true")
    modo.add_argument("--resto", action="store_true")
    modo.add_argument("--todo", action="store_true")
    ap.add_argument("--estratos", default=",".join(ESTRATOS_TODOS),
                    help="estratos incluidos (coma); default todos")
    ap.add_argument("--autorizado", action="store_true")
    ap.add_argument("--gasto-previo", type=float, default=0.0,
                    help="USD ya gastados en corridas previas de esta fase B (reanudación): "
                         "se suman al contador del cliente para que el tope duro sea ACUMULADO")
    args = ap.parse_args()

    print("piezas selladas:")
    verificar_piezas(verbose=False)
    print("  OK (todas)")
    _inyectar_rutas()

    if args.preparar:
        estratos = [e for e in ESTRATOS_TODOS if e in args.estratos.split(",")]
        preparar(estratos)
        return 0
    if args.selftest:
        if not SAMPLES_FASEB.exists():
            preparar(list(ESTRATOS_TODOS))
        return runner_faseB.modo_selftest()

    _gate_autorizacion(args)
    cliente = _cliente()
    if args.gasto_previo:
        cliente.gasto_usd = args.gasto_previo     # el tope duro del cliente pasa a ser acumulado
        print(f"reanudación: gasto previo USD {args.gasto_previo:.4f} cargado en el contador "
              f"(tope acumulado {TOPE_USD:.2f}); las llamadas ya pagadas serán hits de caché", flush=True)
    try:
        if args.calibracion:
            runner_faseB.modo_calibracion(cliente)
        elif args.resto:
            runner_faseB.modo_resto(cliente)
        else:  # --todo
            runner_faseB.modo_calibracion(cliente)
            with OUT_CALIBRACION.open(encoding="utf-8") as f:
                cal = json.load(f)
            n_aptos = cal["resumen"]["n_aptos"]
            print(f"== GATE calibración: {n_aptos} aptos de {len(cal['config']['samples'])} "
                  f"(mínimo {GATE_MIN_APTOS}); gasto {cliente.gasto_usd:.4f} ==")
            if n_aptos < GATE_MIN_APTOS:
                print("GATE NO SUPERADO: se frena sin correr el resto (reportar a la mesa).")
                return 2
            runner_faseB.modo_resto(cliente)
    finally:
        res = cliente.resumen()
        print("GASTO FINAL:", json.dumps(res, ensure_ascii=False))
        with (PARES_DIR / "gasto_cliente_faseB_v3.json").open("a", encoding="utf-8") as f:
            f.write(json.dumps({"modo": "todo" if args.todo else ("calibracion" if args.calibracion else "resto"),
                                **res}, ensure_ascii=False) + "\n")
        cliente.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
