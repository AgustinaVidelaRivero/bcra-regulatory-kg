#!/usr/bin/env python3
"""correr_a2_2.py — Runner del agente de A2.2 (pre-registro FIRMADO, a78ead7b, §3, §4 y §6). NO corre sin autorización explícita:
exige `--autorizado-tope` y `--freno`, y los de la corrida real son los del pre-registro (93 y 69,75).

Tres modos, cada uno con su carpeta de salida (a2_2/resultados/<modo>/):
  pruebas     las tres sesiones de prueba de A-D5, una por brazo, con la pregunta SMK-01 del smoke del tramo 2 de A2.1, antes
              de la primera de EV2. Frena con el código 4 si alguna falla R3 (la sesión completa) o R6 (el inventario de tools).
  n1          N = 1 de las 40 preguntas de EV2 en los tres brazos (120 sesiones), en el orden de orden_corridas_a2_2.json.
              Pide las tres pruebas completas y en verde.
  recorridas  las tres re-corridas (r2, r3 y r4) de cada par (pregunta, brazo) de la población de N = 3
              (poblacion/poblacion_a2_2.json, que arma poblacion_a2_2.py después de juzgar N = 1), por repetición y en el
              orden de N = 1. Pide las 120 de N = 1 y la población derivada de su juicio.

Una cuarta acción, `orden`, escribe orden_corridas_a2_2.json antes de correr (§4): solo los ids de EV2 y los nombres de los
brazos, leídos por código; no imprime ninguno. Si el archivo ya existe y difiere de lo recomputado, frena.

El corte del agente (§6): antes de cada sesión, si el acumulado R9 de las metas de las TRES carpetas de salida (las tres de
prueba incluidas) más 1,80 (el --max-budget-usd por sesión) pasa el freno o el tope, frena con el código 2 sin lanzar otra.
Una sesión con meta ya escrita no se relanza (reanudación), y una meta de otro modo (init frente a real) aborta la corrida.

Después de cada sesión y antes de la siguiente, el control del disco y la lectura acotada del valor remoto por tool de A2.1
(`a2_1/correr_a2_1.py`: `control_disco` y `valor_remoto_por_tool`, importados sin editar): si un resultado de tool llegó como
referencia a disco, frena con el código 3. El valor remoto se lee por código, en memoria, del `.claude.json` de la carpeta de
configuración de la sesión, y a la meta llegan solo la clave y los nombres de tool con número.

EV2 se lee solo por código (comun_a2_2.cargar_preguntas): nada de lo que imprime este runner trae una pregunta, un id de
pregunta ni un texto; imprime cuentas y costos. El registro de cada modo (registro_<modo>_a2_2.json) lleva los ids.

Precondiciones de cada modo: las entradas sin cambios (sellos_entrada_a2_2.json), los índices de fragmentos y el grafo cargado
en Neo4j (controles_a2_2.py). --modo init corre todo a USD 0 (modo init del lanzador: ninguna petición llega a la API).

Uso (solo con autorización; la clave la pone el envoltorio de A2.1, desde el comando del paso):
  BANCO_VENV_VECTOR=<venv> .venv/bin/python -B data/experiment/banco_mcp/a2_2/correr_a2_2.py pruebas \\
      --autorizado-tope 93 --freno 69.75
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
for _p in (str(AQUI), str(BANCO_DIR), str(BANCO_DIR / "a2_1"), str(BANCO_DIR / "agentes")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import comun_a2_2 as K                                      # noqa: E402
import lanzar_agente_a2_2 as L22                            # noqa: E402
import correr_a2_1 as CR                                    # noqa: E402  (A2.1: solo import)

MODOS = ("pruebas", "n1", "recorridas")
DIRS = {"pruebas": K.OUT_PRUEBAS, "n1": K.OUT_N1, "recorridas": K.OUT_RECORRIDAS}
REGISTRO = "registro_{modo}_a2_2.json"


class Freno(Exception):
    """El corte del agente: la corrida frena con el código 2."""


class FrenoDisco(Freno):
    """Un resultado de tool llegó como referencia a disco: código 3."""


class FrenoPruebas(Freno):
    """Una sesión de prueba falla R3 o R6: código 4."""


class FrenoPrecondicion(Freno):
    """Falta el paso anterior o una entrada cambió: código 5."""


def prueba_en_verde(m: dict) -> bool:
    """R3 (la sesión completa) y R6 (el inventario de tools en init = el esperado)."""
    return bool(m["completitud_R3"]["completa"]) and bool(m["inventario_tools_R6"]["coincide"])


def r5_de(m: dict) -> dict:
    """Lo operativo de R5 de una sesión (pre-registro, §3, opción (1)): las llamadas del log R1 y si la cortó el CLI."""
    h = m.get("hb2") or {}
    n = h.get("n_llamadas_log_r1") or 0
    return {"llamadas_log_r1": n, "al_tope": n >= 30, "pasa_de_30": n > 30, "subtype": h.get("subtype"),
            "cortada": h.get("subtype") not in ("success", None) or not h.get("hay_result"),
            "n_mensajes_asistente": h.get("n_mensajes_asistente"), "num_turns": h.get("num_turns")}


class Corrida:
    def __init__(self, a, out: Path):
        self.a, self.out = a, out
        self.dirs = [a.out_pruebas, a.out_n1, a.out_recorridas]
        self.sesiones = a.sesiones
        self.registro = {"inicio": datetime.now().isoformat(timespec="seconds"), "modo_corrida": a.etapa, "modo": a.modo,
                         "tope": a.autorizado_tope, "freno": a.freno, "presupuesto_por_sesion": K.PRESUPUESTO_SESION,
                         "via": a.via, "eventos": []}

    def sesion(self, s: dict, pregunta: str, k: int, n: int) -> dict:
        pid, out = s["id"], self.out
        p = out / f"meta_{pid}.json"
        if p.exists():
            m = json.loads(p.read_text(encoding="utf-8"))
            if m.get("modo") != self.a.modo:
                raise SystemExit(f"ABORTO: {K.rel_repo(p)} es de modo {m.get('modo')!r} y esta corrida es {self.a.modo!r}: "
                                 "no se mezclan sesiones de la corrida en seco con las reales")
            if (m.get("control_disco") or {}).get("FRENA"):
                raise FrenoDisco(f"una sesión ya corrida tiene un resultado en disco ({K.rel_repo(p)})")
            return m
        r9, _ = CR.gastado(self.dirs)
        if r9 + K.PRESUPUESTO_SESION > self.a.freno or r9 + K.PRESUPUESTO_SESION > self.a.autorizado_tope:
            raise Freno(f"acumulado R9 {r9:.4f} + {K.PRESUPUESTO_SESION} > freno {self.a.freno} (tope {self.a.autorizado_tope}) "
                        f"antes de la sesión {k} de {n}")
        m = self.lanzar(s["brazo"], pid, pregunta, out)
        self.controlar(m, out, pid)
        ev = {"id": pid, "brazo": s["brazo"], "rep": s["rep"], "completa": m["completitud_R3"]["completa"],
              "R6": m["inventario_tools_R6"]["coincide"], "costo_R9": m["tokens_R9"]["costo_recomputado"]["total_usd"],
              "costo_cli": m["tokens_R9"]["total_cost_usd_cli_solo_para_contraste"], "duracion_s": m.get("duracion_s"),
              "denials": len(m.get("permission_denials") or []), "r5": r5_de(m),
              "control_disco": {x: m["control_disco"][x] for x in ("FRENA", "largo_mayor_utf16", "carpeta_tool_results")},
              "valor_remoto": {x: v for x, v in m["valor_remoto_por_tool"].items()
                               if x in ("archivo", "existe", "tools_del_banco_con_numero")},
              "fecha": m.get("generado")}
        self.registro["eventos"].append(ev)
        acum, _ = CR.gastado(self.dirs)
        print(f"[{k}/{n}] {s['brazo']}: completa {'sí' if ev['completa'] else 'no'}, R6 {'sí' if ev['R6'] else 'no'}, "
              f"llamadas {ev['r5']['llamadas_log_r1']}, R9 {ev['costo_R9']:.4f}, acumulado {acum:.4f}", flush=True)
        if m["control_disco"]["FRENA"]:
            raise FrenoDisco(f"la sesión {k} de {n} trajo un resultado de tool como referencia a disco")
        return m

    def controlar(self, m: dict, out: Path, pid: str) -> None:
        """El control del disco y la lectura del valor remoto de la sesión recién corrida (los de A2.1); la meta se reescribe con
        los dos campos."""
        sid = json.loads((out / f"comando_{pid}.json").read_text(encoding="utf-8"))["session_id"]
        m["control_disco"] = CR.control_disco(out, pid)
        m["valor_remoto_por_tool"] = CR.valor_remoto_por_tool(self.sesiones / "config" / sid)
        (out / f"meta_{pid}.json").write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        con_numero = m["valor_remoto_por_tool"].get("tools_del_banco_con_numero")
        if con_numero:
            self.registro.setdefault("valor_remoto_tools_del_banco_con_numero", {})[pid] = con_numero

    def lanzar(self, brazo: str, pid: str, pregunta: str, out: Path) -> dict:
        return L22.lanzar(brazo, pid, pregunta, out, self.a.modo, self.a.via, None, self.a.timeout_s, self.sesiones)

    def cerrar(self, nombre: str) -> None:
        r9, cli = CR.gastado(self.dirs)
        self.registro.update({"fin": datetime.now().isoformat(timespec="seconds"), "gasto_R9_usd_a2_2": round(r9, 6),
                              "gasto_cli_usd_a2_2": round(cli, 6),
                              "razon_cli_sobre_R9": round(cli / r9, 2) if r9 else None})
        self.out.mkdir(parents=True, exist_ok=True)
        (self.out / nombre).write_text(json.dumps(self.registro, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- #
# Las precondiciones de cada modo                                              #
# --------------------------------------------------------------------------- #
def cargar_orden(a) -> dict:
    orden = json.loads(Path(a.orden).read_text(encoding="utf-8"))
    return orden


def controlar_orden(orden: dict, preguntas: dict) -> None:
    ids = sorted(preguntas)
    if orden["sha256_ids_ordenados"] != K.sha256_texto("".join(x + "\n" for x in ids)) or sorted(orden["preguntas_en_orden"]) != ids:
        raise FrenoPrecondicion("orden_corridas_a2_2.json no corresponde a las preguntas que se cargaron")
    if orden != K.armar_orden(ids):
        raise FrenoPrecondicion("orden_corridas_a2_2.json difiere del orden que dan las semillas del pre-registro")


def pruebas_en_verde(out_pruebas: Path, orden: dict) -> list[dict]:
    metas = []
    for s in K.secuencia(orden, "pruebas"):
        p = out_pruebas / f"meta_{s['id']}.json"
        if not p.exists():
            raise FrenoPrecondicion("faltan sesiones de prueba: el paso 1 no está completo")
        m = json.loads(p.read_text(encoding="utf-8"))
        if not prueba_en_verde(m):
            raise FrenoPrecondicion("una sesión de prueba falla R3 o R6: el paso 1 frenó")
        metas.append(m)
    return metas


def n1_completo(out_n1: Path, orden: dict) -> None:
    faltan = [s for s in K.secuencia(orden, "n1") if not (out_n1 / f"meta_{s['id']}.json").exists()]
    if faltan:
        raise FrenoPrecondicion(f"faltan {len(faltan)} sesiones de N = 1: el paso 2 no está completo")


def cargar_poblacion(ruta: Path, orden: dict) -> dict:
    if not Path(ruta).exists():
        raise FrenoPrecondicion("falta la población de N = 1: el paso 3 (el juez de N = 1 y la población) no está completo")
    pob = json.loads(Path(ruta).read_text(encoding="utf-8"))
    validos = {(q, b) for q in orden["preguntas_en_orden"] for b in K.BRAZOS}
    if any((p["qid"], p["brazo"]) not in validos for p in pob["pares"]):
        raise FrenoPrecondicion("la población trae un par que no está en el orden de N = 1")
    return pob


def precondiciones(a, preguntas: dict | None) -> dict:
    """Las entradas, los índices y el grafo en Neo4j (salvo --sin-controles-externos, solo para la corrida en seco)."""
    import controles_a2_2 as CT
    out = {"entradas": K.verificar_entradas()}
    if not a.sin_controles_externos:
        out["indices"] = CT.verificar_indices()
        out["neo4j"] = CT.verificar_neo4j()
    return out


# --------------------------------------------------------------------------- #
def correr(c: Corrida, a, orden: dict, preguntas: dict | None) -> None:
    if a.etapa == "pruebas":
        qid, texto = K.pregunta_de_prueba()
        seq = K.secuencia(orden, "pruebas")
        metas = [c.sesion(s, texto, k, len(seq)) for k, s in enumerate(seq, 1)]
        c.registro["pruebas_en_verde"] = {m["brazo"]: prueba_en_verde(m) for m in metas}
        malas = [m["brazo"] for m in metas if not prueba_en_verde(m)]
        c.registro["PASS"] = not malas
        if malas:
            raise FrenoPruebas(f"{len(malas)} de {len(metas)} sesiones de prueba fallan R3 o R6")
        return
    if a.etapa == "n1":
        pruebas_en_verde(a.out_pruebas, orden)
        seq = K.secuencia(orden, "n1")
    else:
        n1_completo(a.out_n1, orden)
        pob = cargar_poblacion(a.poblacion, orden)
        c.registro["poblacion"] = {"ruta": K.rel_repo(a.poblacion), "sha256": K.sha256_file(Path(a.poblacion)),
                                   "n_pares": len(pob["pares"])}
        seq = K.secuencia(orden, "recorridas", pob)
    for k, s in enumerate(seq, 1):
        c.sesion(s, preguntas[s["qid"]]["pregunta"], k, len(seq))
    c.registro["n_sesiones"] = len(seq)


def escribir_orden(preguntas: dict, salida: Path) -> int:
    nuevo = json.dumps(K.armar_orden(sorted(preguntas)), ensure_ascii=False, indent=1) + "\n"
    if salida.exists() and salida.read_text(encoding="utf-8") != nuevo:
        print("FRENO: orden_corridas_a2_2.json ya existe y difiere del recomputado")
        return 5
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(nuevo, encoding="utf-8")
    print(f"orden escrito: {len(preguntas)} preguntas × {len(K.BRAZOS)} brazos × {len(K.REPETICIONES)} repeticiones ->",
          K.rel_repo(salida))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("etapa", choices=MODOS + ("orden",))
    ap.add_argument("--autorizado-tope", type=float, default=None, help="tope autorizado en USD (explícito)")
    ap.add_argument("--freno", type=float, default=None, help="freno del acumulado R9 de todas las sesiones de A2.2")
    ap.add_argument("--modo", choices=["real", "init"], default="real")
    ap.add_argument("--via", choices=["api", "bedrock"], default="api")
    ap.add_argument("--preguntas", type=Path, default=K.EV2_PATH)
    ap.add_argument("--sha-preguntas", default=K.EV2_SHA256)
    ap.add_argument("--orden", type=Path, default=K.ORDEN)
    ap.add_argument("--poblacion", type=Path, default=K.POBLACION)
    ap.add_argument("--out-pruebas", type=Path, default=K.OUT_PRUEBAS)
    ap.add_argument("--out-n1", type=Path, default=K.OUT_N1)
    ap.add_argument("--out-recorridas", type=Path, default=K.OUT_RECORRIDAS)
    ap.add_argument("--sesiones", type=Path, default=L22.LA.BANCO_SESIONES, help="raíz de las sesiones del banco")
    ap.add_argument("--timeout-s", type=float, default=1800.0)
    ap.add_argument("--sin-controles-externos", action="store_true",
                    help="solo para la corrida en seco: no controla los índices ni Neo4j")
    a = ap.parse_args(argv)
    if a.etapa == "orden":
        return escribir_orden(K.cargar_preguntas(a.preguntas, a.sha_preguntas, real=a.modo == "real"), a.orden)
    if a.autorizado_tope is None or a.freno is None or a.autorizado_tope <= 0:
        raise SystemExit("sin tope autorizado no se corre nada")
    if a.modo == "real" and (a.autorizado_tope != K.TOPE_AGENTE or a.freno != K.FRENO_AGENTE or a.sin_controles_externos):
        raise SystemExit("la corrida real usa el tope 93 y el freno 69,75 del pre-registro, con todos los controles")
    out = {"pruebas": a.out_pruebas, "n1": a.out_n1, "recorridas": a.out_recorridas}[a.etapa]
    out.mkdir(parents=True, exist_ok=True)
    c = Corrida(a, out)
    nombre = REGISTRO.format(modo=a.etapa)
    try:
        preguntas = None if a.etapa == "pruebas" else K.cargar_preguntas(a.preguntas, a.sha_preguntas, real=a.modo == "real")
        orden = cargar_orden(a)
        if preguntas is not None:
            controlar_orden(orden, preguntas)
        c.registro["precondiciones"] = precondiciones(a, preguntas)
        correr(c, a, orden, preguntas)
    except FrenoDisco as e:
        c.registro["FRENO_DISCO"] = str(e); c.cerrar(nombre)
        print("FRENO DEL DISCO:", e); return 3
    except FrenoPruebas as e:
        c.registro["FRENO_PRUEBAS"] = str(e); c.cerrar(nombre)
        print("FRENO DE LAS PRUEBAS (R3 o R6):", e); return 4
    except (FrenoPrecondicion, K.FrenoA22) as e:
        c.registro["FRENO_PRECONDICION"] = str(e); c.cerrar(nombre)
        print("FRENO DE PRECONDICIÓN:", e); return 5
    except Freno as e:
        c.registro["FRENO"] = str(e); c.cerrar(nombre)
        print("FRENO:", e); return 2
    c.cerrar(nombre)
    r9, cli = CR.gastado(c.dirs)
    ev = c.registro["eventos"]
    print(f"{a.etapa}: {len(ev)} sesiones nuevas, {sum(e['completa'] for e in ev)} completas; gasto de A2.2 R9 {r9:.4f} "
          f"(CLI {cli:.4f}); freno {a.freno}, tope {a.autorizado_tope}")
    print("->", K.rel_repo(out / nombre))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
