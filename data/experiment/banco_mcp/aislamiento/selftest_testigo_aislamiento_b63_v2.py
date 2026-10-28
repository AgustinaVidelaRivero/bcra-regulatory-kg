#!/usr/bin/env python3
"""selftest_testigo_aislamiento_b63_v2.py — El selftest del testigo v2 (testigo_aislamiento_b63_v2.py: la excepción cerrada de la decisión
de la autora del 28/10/2026, 10:35:10) y de su reaplicación (b63/v2/b2bis/reaplicar_testigo_b63.py), sobre copias de la captura de la
corrida real del testigo de la b2. USD 0 y sin lanzar ningún CLI ni ningún servidor. Una prueba nunca escribe en la captura: cada una
trabaja sobre una copia nueva, y el último caso controla el sha256 de cada archivo de la captura antes y después.
  1. la excepción: una lista de un solo elemento; su ventana, por su sha256, está una vez en la nota de cada config de fragmentos y en
     ninguna parte de la config del grafo;
  2. la captura sin cambios: la reaplicación reproduce la b2 tal cual, y con la excepción pasan los 4 renglones (las sesiones de
     fragmentos, renglón 0 del log_r1, `inicio`, `config.nota`): PASS_de_B63 true, PASS_del_testigo_tal_cual false;
  3. la misma ventana en un pedido (`system` o `messages`) frena;
  4. otra ventana (de un testigo, el CLAUDE.md del repo) en el log_r1, en el mismo renglón y el mismo campo, frena;
  5. la misma ventana en otro campo del renglón de `inicio`, o en otro renglón del log_r1, frena;
  6. la misma ventana en otro archivo (el stream o la carpeta de configuración) frena;
  7. la misma ventana en el log_r1 de una sesión del grafo frena;
  8. la misma ventana en su lugar, con otro `config_sha256` en el renglón de `inicio`, frena;
  9. la captura no cambió.
La ventana se planta tomándola de la nota de la config de fragmentos por su sha256 (su texto no se escribe acá); la otra ventana, de las
8 primeras palabras del CLAUDE.md del repo en HEAD.
Uso, desde la raíz de una copia del repo: SELFTEST_TESTIGO_TMP=<carpeta> SELFTEST_CAPTURA=<el --tmp de medir_testigo_b63 de la b2>
  <python del .venv> -B data/experiment/banco_mcp/aislamiento/selftest_testigo_aislamiento_b63_v2.py
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
sys.path.insert(0, str(BANCO_DIR / "b63" / "v2" / "b2bis"))
import reaplicar_testigo_b63 as RA                        # noqa: E402

T = RA.T
for v in ("SELFTEST_TESTIGO_TMP", "SELFTEST_CAPTURA"):
    if not os.environ.get(v):
        raise SystemExit(f"falta {v}")
if os.environ.get("ANTHROPIC_API_KEY"):
    raise SystemExit("ABORTO: el selftest corre sin ninguna clave en el entorno")
CAPTURA = Path(os.environ["SELFTEST_CAPTURA"]).resolve()
TMP = Path(tempfile.mkdtemp(prefix="selftest_testigo_v2_b63_", dir=os.environ["SELFTEST_TESTIGO_TMP"]))
if CAPTURA.is_relative_to(T.REPO_REAL.resolve()) or TMP.is_relative_to(T.REPO_REAL.resolve()):
    raise SystemExit("ABORTO: la captura y la carpeta de trabajo van fuera del repo")
EXC = T.EXCEPCIONES[0]
FRAG = ["TESTIGO-T2-1-fragmentos_hibrida", "TESTIGO-T3-1-fragmentos_denso", "TESTIGO-T5-1-fragmentos_hibrida",
        "TESTIGO-T6-1-fragmentos_denso"]
H, KG = FRAG[0], "TESTIGO-T1-1-kg"
RES: list[tuple[bool, str]] = []


def caso(nombre: str):
    def deco(f):
        try:
            ok, detalle = f()
        except BaseException as ex:                        # noqa: BLE001  (también SystemExit, para el control)
            ok, detalle = False, f"{type(ex).__name__}: {str(ex)[:160]}"
        RES.append((bool(ok), nombre + (f" — {detalle}" if detalle else "")))
        return f
    return deco


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def foto(d: Path) -> dict:
    return {str(p.relative_to(d)): sha(p.read_bytes()) for p in sorted(d.rglob("*")) if p.is_file()}


FOTO_ANTES = foto(CAPTURA)


def ventanas(texto: str) -> list[tuple]:
    w = T.palabras(texto)
    return [tuple(w[j:j + T.N_PALABRAS]) for j in range(len(w) - T.N_PALABRAS + 1)]


def la_ventana() -> str:
    """La ventana de la excepción, tomada de la nota de la config de la híbrida por su sha256 (no se escribe en este archivo)."""
    nota = json.loads((BANCO_DIR / "mcp_vector/config_fragmentos_hibrida_evaluado_r2b.json").read_text(encoding="utf-8"))["nota"]
    vs = [v for v in ventanas(nota) if T.ventana_sha256(v) == EXC["ventana_sha256"]]
    assert len(vs) == 1
    return " ".join(vs[0])


def otra_ventana() -> str:
    """Las 8 primeras palabras del CLAUDE.md del repo en HEAD (un testigo): una ventana que no es la de la excepción."""
    b = subprocess.run(["git", "-C", str(T.REPO_REAL), "--no-optional-locks", "show", "HEAD:CLAUDE.md"], capture_output=True,
                       check=True).stdout.decode("utf-8")
    v = tuple(T.palabras(b)[:T.N_PALABRAS])
    assert T.ventana_sha256(v) != EXC["ventana_sha256"]
    return " ".join(v)


def copia(nombre: str) -> Path:
    d = TMP / nombre
    shutil.copytree(CAPTURA, d, symlinks=True)
    return d


def cambiar_log_r1(d: Path, sid: str, evento: str, f) -> None:
    p = d / "testigo" / sid / f"log_r1_{sid}.jsonl"
    rs = [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines()]
    assert sum(r.get("evento") == evento for r in rs) == 1
    p.write_text("".join(json.dumps(f(r) if r.get("evento") == evento else r, ensure_ascii=False) + "\n" for r in rs), encoding="utf-8")


def con_nota(r: dict, texto: str) -> dict:
    r["config"]["nota"] = r["config"]["nota"] + " " + texto
    return r


def frena_en(d: Path, sid: str) -> tuple[bool, str]:
    """Reaplica sobre la copia: frena si PASS_de_B63 es false y la sesión tiene su renglón «llega un testigo» con la excepción."""
    out = RA.reaplicar(d)
    llegan = sorted(l.split(":", 1)[0] for l in out["FRENO_con_la_excepcion"] if "llega un testigo" in l)
    return (out["PASS_de_B63"] is False and sid in llegan), \
        f"PASS_de_B63 {out['PASS_de_B63']}; con un testigo que llega, con la excepción: {llegan}"


@caso("1. la excepción: una lista de un solo elemento; su ventana, por su sha256, una vez en la nota de cada config de fragmentos y en ninguna parte de la config del grafo")
def _():
    cuentas = {}
    for n in ("hibrida", "denso"):
        nota = json.loads((BANCO_DIR / f"mcp_vector/config_fragmentos_{n}_evaluado_r2b.json").read_text(encoding="utf-8"))["nota"]
        cuentas[n] = sum(T.ventana_sha256(v) == EXC["ventana_sha256"] for v in ventanas(nota))
    kg = (BANCO_DIR / "n7/config_mcp_kg_n7_evaluado.json").read_text(encoding="utf-8")
    cuentas["grafo"] = sum(T.ventana_sha256(v) == EXC["ventana_sha256"] for v in ventanas(kg))
    shas = {r: sha((BANCO_DIR / r).read_bytes()) == s for r, s in EXC["configs_de_servidor"].items()}
    return (len(T.EXCEPCIONES) == 1 and cuentas == {"hibrida": 1, "denso": 1, "grafo": 0} and all(shas.values())
            and (EXC["archivo"], EXC["evento"], EXC["campo"]) == ("log_r1", "inicio", "config.nota")), \
        f"{len(T.EXCEPCIONES)} elemento; {cuentas}; las dos configs dan su sha256: {all(shas.values())}"


@caso("2. la captura sin cambios: reproduce la b2 tal cual; con la excepción pasan los 4 renglones; PASS_de_B63 true y PASS_del_testigo_tal_cual false")
def _():
    out = RA.reaplicar(copia("sin_cambios"))
    ea = out["excepcion_aplicada"]
    esperado = [{"renglon_del_log_r1": 0, "evento": "inicio", "campo": "config.nota",
                 "testigo": "repo:docs/preregistro_B6_3_evaluacion_final.md", "ventanas": 1}]
    causa = out["por_que_PASS_del_testigo_tal_cual_es_false"]
    ok = (out["control"]["reproduce_la_b2"] and out["PASS_de_B63"] is True and out["PASS_del_testigo_tal_cual"] is False
          and ea["renglones_del_FRENO_que_pasan"] == 4 and sorted(ea["sesiones"]) == FRAG
          and all(v == esperado for v in ea["sesiones"].values()) and not ea["en_otras_sesiones"]
          and causa["renglones_de_la_fecha"] == 12 and len(causa["renglones_que_pasan_por_la_excepcion"]) == 4 and not causa["otros"]
          and out["leer_testigo_de_la_b2"]["su_PASS_de_B63_con_la_excepcion_es_el_del_testigo_v2"])
    return ok, (f"reproduce la b2: {out['control']['reproduce_la_b2']}; PASS_de_B63 {out['PASS_de_B63']}; PASS_del_testigo_tal_cual "
                f"{out['PASS_del_testigo_tal_cual']}; pasan {ea['renglones_del_FRENO_que_pasan']} renglones ({', '.join(sorted(ea['sesiones']))}), "
                f"cada uno en el renglón 0 del log_r1, `inicio`, `config.nota`; la fecha: {causa['renglones_de_la_fecha']}")


def en_pedido(campo: str):
    d = copia(f"en_pedido_{campo}")
    p = d / "testigo_privado_captura" / H / "pedido_1.json"
    c = json.loads(p.read_bytes())
    if campo == "system":
        c["system"] = (c["system"] + [{"type": "text", "text": la_ventana()}] if isinstance(c.get("system"), list)
                       else (c.get("system") or "") + " " + la_ventana())
    else:
        c["messages"] = c["messages"] + [{"role": "user", "content": la_ventana()}]
    p.write_bytes(json.dumps(c, ensure_ascii=False).encode("utf-8"))
    return frena_en(d, H)


@caso("3a. la misma ventana en un pedido, en `system`, frena")
def _():
    return en_pedido("system")


@caso("3b. la misma ventana en un pedido, en `messages`, frena")
def _():
    return en_pedido("messages")


@caso("4. otra ventana en el log_r1, en el mismo renglón (`inicio`) y el mismo campo (`config.nota`), frena")
def _():
    d = copia("otra_ventana")
    cambiar_log_r1(d, H, "inicio", lambda r: con_nota(r, otra_ventana()))
    return frena_en(d, H)


@caso("5a. la misma ventana en otro campo del renglón de `inicio` frena")
def _():
    d = copia("otro_campo")
    cambiar_log_r1(d, H, "inicio", lambda r: r | {"campo_de_prueba": la_ventana()})
    return frena_en(d, H)


@caso("5b. la misma ventana en otro renglón del log_r1 (el de `fin`) frena")
def _():
    d = copia("otro_renglon")
    cambiar_log_r1(d, H, "fin", lambda r: r | {"campo_de_prueba": la_ventana()})
    return frena_en(d, H)


@caso("6a. la misma ventana en otro archivo, el stream, frena")
def _():
    d = copia("en_el_stream")
    p = d / "testigo" / H / f"stream_{H}.jsonl"
    p.write_text(p.read_text(encoding="utf-8") + json.dumps({"type": "prueba_b2bis", "texto": la_ventana()}, ensure_ascii=False) + "\n",
                 encoding="utf-8")
    return frena_en(d, H)


@caso("6b. la misma ventana en otro archivo, la carpeta de configuración de la sesión, frena")
def _():
    d = copia("en_la_configuracion")
    sid = json.loads((d / "testigo" / H / f"sesion_{H}.json").read_text(encoding="utf-8"))["session_id"]
    (d / "testigo_ses" / "config" / sid / "prueba_b2bis.txt").write_text(la_ventana() + "\n", encoding="utf-8")
    return frena_en(d, H)


@caso("7. la misma ventana en el log_r1 de una sesión del grafo (en su `config.nota` de `inicio`) frena")
def _():
    d = copia("en_el_grafo")
    cambiar_log_r1(d, KG, "inicio", lambda r: con_nota(r, la_ventana()))
    return frena_en(d, KG)


@caso("8. la misma ventana en su lugar, con otro `config_sha256` en el renglón de `inicio`, frena")
def _():
    d = copia("otra_config")
    cambiar_log_r1(d, H, "inicio", lambda r: r | {"config_sha256": "0" * 64})
    return frena_en(d, H)


@caso("9. la captura no cambió: el sha256 de cada archivo, antes y después de las pruebas")
def _():
    despues = foto(CAPTURA)
    return despues == FOTO_ANTES, f"{len(FOTO_ANTES)} archivos, iguales: {despues == FOTO_ANTES}"


def main() -> int:
    for ok, t in RES:
        print(("PASS " if ok else "FAIL ") + t)
    n = sum(ok for ok, _ in RES)
    print(f"selftest del testigo v2 de B6.3: {n} de {len(RES)} en PASS")
    return 0 if n == len(RES) else 1


if __name__ == "__main__":
    raise SystemExit(main())
