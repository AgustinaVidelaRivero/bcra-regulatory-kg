#!/usr/bin/env python3
"""corrida_en_seco_n6.py — La corrida en seco del corredor de N6 (correr_n6.py), a USD 0, con el CLI falso
(n6/seco/claude_falso_n6.py) y el juez falso de la corrida en seco de A2.2 (corrida_en_seco_a2_2.ClienteJuezFalso, envuelto en
la caché sellada), por el mismo camino de imports que el corredor: importa correr_n6 desde su carpeta y llama a su main, sin
tocar el sys.path. Las sesiones son reales para el lote y para los servidores (los del banco, sobre el Neo4j propio de N6): solo
el CLI y el juez son falsos. Ninguna petición sale a la API (el CLI falso no la usa; la clave del entorno es de prueba y la URL
base apunta a un puerto cerrado).

Arma su carpeta de trabajo (--trabajo, fuera del repo): el envoltorio `claude` del PATH, el estado del CLI falso, los envoltorios
`vm_stat`, `footprint` y `docker` del PATH (seco/sistema_falso_n6.py, con su estado: la memoria en uso, la huella de cada
proceso, el tope de la VM de Docker y la salud del contenedor; ningún control de esta prueba llama al `docker` real), el proceso de
juguete de otro paso pago (un script con un token propio en su nombre, que espera una señal) y, por rama, las preguntas
sintéticas (con la forma de las de N3, sin ninguna pregunta real), la entrada seca y la salida. La guarda de otro paso pago corre
con un patrón propio (--patron-de-prueba): ningún `pgrep` de esta prueba lleva el patrón real.

Ramas:
  R0 el camino de imports: correr_n6 importa lanzar_lote_paralelo_r5.py de HEAD (sha256) y le pone la guarda nueva; el
     patrón real de la guarda nueva ve lanzar_lote_paralelo_r5.py y correr_n6.py, y el de HEAD no (el hueco), por regex y sin
     pgrep; con el patrón propio, la guarda ve el proceso de juguete y no lo ve cuando termina;
  R1 completa: 8 preguntas × 4 corridas, en los dos lotes (sin codificador: B dos veces y BM25 de F1, 24 sesiones, P = 2; con
     codificador: T, 8 sesiones, P = 1), primero el sin, cada uno en el orden sellado restringido a sus sesiones: la completa,
     el corte por R5, la salida mal formada del agente, la falla de infraestructura (solo en el intento 1, el error de la API
     solo en el intento 1, y la que falla en los dos), el reintento con «-i2» en el lote siguiente de su lote, la respuesta que
     el juez no puede parsear y el juez con sus tres repeticiones; el CLI medido (la huella de cada sesión en sus tres partes,
     con la del CLI en el registro de cada lote), la guarda de cada tanda con la memoria y Docker registrados, y el control
     antes del lote con codificador con la huella de CLI más alta del primero; código 0;
  R2 retomar R1 con la misma entrada: ningún lote nuevo, ninguna sesión repetida y ninguna llamada nueva del juez;
  R3 otro paso pago: con el proceso de juguete corriendo antes de empezar, frena (7) sin lanzar nada; y lanzado por la primera
     sesión, frena (7) en la tanda siguiente; terminado el proceso, retomar completa sin repetir ninguna sesión;
  R4 el freno del gasto: el lote frena (2) por su guarda con el freno de la entrada; retomar frena (2) antes del lote, sin
     lanzar nada, porque el gasto de las sesiones ya corridas cuenta;
  R5 tres formas desconocidas: frena (12) al juntar 3, sin lanzar el lote con codificador;
  R6 lo que se controla de la entrada: otra entrada sobre la misma salida, una entrada seca con el CLI real y la real con el CLI
     falso frenan (8) sin lanzar nada;
  R7 la P que no entra al lanzar: con lo fijo de 10 GB, la P 1 del lote con codificador no entra (entra hasta 0); con 5,5 GB, la
     P 2 no entra (entra hasta 1); con 14,2 GB, la P 2 del lote sin codificador no entra (entra hasta 0): frena (13) sin lanzar
     nada y dice cuál entra; sin una de las dos P, frena (8);
  R8 la tanda que deja de entrar: una sesión de la primera tanda sube la memoria en uso a 14,4 GB y el lote frena (13) antes de la
     tanda siguiente, sin cortar las sesiones que corren y sin cambiar la P; retomar con la memoria de vuelta completa sin
     repetir ninguna sesión. Y antes del lote con codificador: una sesión del primer lote sube lo fijo a 6 GB, la P 2 del lote
     con codificador deja de entrar y frena (13) antes de lanzarlo, diciendo que entra 1; retomar con P = 1 completa;
  R9 Docker: con la VM de más (4 GB) o el contenedor no sano al lanzar, frena (14) sin lanzar nada; con el contenedor que deja
     de estar sano a mitad del lote, frena (14) antes de la tanda siguiente; retomar con el contenedor sano completa.
Imprime PASS/FAIL por control y escribe un JSON con el resumen (--salida-json). Código 1 si algún control falla.
Uso: NEO4J_URI=bolt://127.0.0.1:57687 BANCO_VENV_VECTOR=<venv> .venv/bin/python -B data/experiment/banco_mcp/n6/corrida_en_seco_n6.py \\
       --trabajo <carpeta fuera del repo> --salida-json <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
from collections import Counter
from pathlib import Path

import correr_n6 as CN                   # el corredor, desde su carpeta: el mismo camino de imports

AQUI = Path(__file__).resolve().parent
SECO = AQUI / "seco"
RES: list[dict] = []
SHA_R5_HEAD = "73b21753e826b91fb878b8ebc6f5fd34262e27be6a974fdb17051e825934e2e2"
SHA_GUARDA_R5_HEAD = "04f81fe3bc522fb76166fe2190761b66de68e65e72191302b87c4461b532fae2"
# El estado del sistema falso con el que todo entra: lo fijo de 5 GB (la P 2 del lote con codificador entra), 20 MB por proceso, la
# VM de Docker en 2,5 GB y el contenedor sano.
SISTEMA_BIEN = {"en_uso_gb": 5.0, "libre_gb": 6.0, "huella_mb": 20, "docker_mem_total": 2_684_354_560, "docker_salud": "healthy"}


def rama(nombre: str, ok: bool, det: str = "") -> None:
    RES.append({"control": nombre, "ok": bool(ok), "detalle": det})
    print(("PASS " if ok else "FAIL ") + nombre + (f" — {det}" if det else ""), flush=True)


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


# --------------------------------------------------------------------------- #
# La carpeta de trabajo                                                        #
# --------------------------------------------------------------------------- #
class Trabajo:
    def __init__(self, raiz: Path):
        self.raiz = raiz.resolve()
        if self.raiz.is_relative_to(CN.REPO_DIR) or self.raiz.exists():
            raise SystemExit("FRENO: la carpeta de trabajo tiene que ser nueva y estar fuera del repo")
        self.bin = self.raiz / "bin"
        self.bin.mkdir(parents=True)
        self.bin_sistema = self.raiz / "bin_sistema"
        self.bin_sistema.mkdir()
        self.estado_sistema = self.raiz / "estado_sistema.json"
        self.sistema(**SISTEMA_BIEN)
        for h in ("vm_stat", "footprint", "docker"):
            w = self.bin_sistema / h
            w.write_text(f"#!/bin/sh\n# El {h} falso de la corrida en seco de N6 (sistema_falso_n6.py), con su estado.\n"
                         f"exec '{sys.executable}' -B '{SECO / 'sistema_falso_n6.py'}' {h} --estado '{self.estado_sistema}' \"$@\"\n",
                         encoding="utf-8")
            w.chmod(0o755)
        self.token = f"ensayoseco{os.getpid()}x"
        self.otro = self.raiz / f"{self.token}_n6.py"
        # El proceso de juguete: retiene un candado sobre `candado` mientras vive, avisa que ya corre y espera una señal.
        self.otro.write_text("import fcntl, signal, sys\nf = open(sys.argv[1], 'a')\nfcntl.flock(f, fcntl.LOCK_EX)\n"
                             "sys.stdout.write('listo\\n')\nsys.stdout.flush()\nsignal.pause()\n", encoding="utf-8")
        self.candado = self.raiz / "candado_otro_paso_pago"
        self.pid_otro = self.raiz / "pid_otro_paso_pago.txt"
        self.estado = self.raiz / "estado_cli_falso.json"
        self.estado.write_text(json.dumps({"planes": str(SECO / "planes_seco_n6.json"), "otro_paso_pago": str(self.otro),
                                           "candado_otro_paso_pago": str(self.candado),
                                           "pid_otro_paso_pago": str(self.pid_otro), "estado_sistema": str(self.estado_sistema)},
                                          ensure_ascii=False), encoding="utf-8")
        envol = self.bin / "claude"
        envol.write_text("#!/bin/sh\n# El CLI falso de la corrida en seco de N6 (claude_falso_n6.py), con su estado.\n"
                         f"exec '{sys.executable}' -B '{SECO / 'claude_falso_n6.py'}' --estado '{self.estado}' \"$@\"\n",
                         encoding="utf-8")
        envol.chmod(0o755)
        self.path_falso = f"{self.bin}:{self.bin_sistema}:{os.environ['PATH']}"
        self.path_real = f"{self.bin_sistema}:{os.environ['PATH']}"      # el CLI real; vm_stat, footprint y docker, falsos

    def sistema(self, **kw) -> dict:
        """El estado del vm_stat, el footprint y el docker falsos: lo cambia con kw y lo devuelve."""
        d = json.loads(self.estado_sistema.read_text(encoding="utf-8")) if self.estado_sistema.exists() else {}
        d.update(kw)
        self.estado_sistema.write_text(json.dumps(d), encoding="utf-8")
        return d

    def con_cli_falso(self, si: bool) -> None:
        os.environ["PATH"] = self.path_falso if si else self.path_real

    def preguntas(self, nombre: str, planes: list[str]) -> tuple[Path, str]:
        """Las preguntas sintéticas de una rama, con la forma de las de N3; el plan k va a la pregunta k del orden de la entrada."""
        ids = [f"SECO-{i:02d}" for i in range(1, len(planes) + 1)]
        orden = sorted(ids)
        import random                     # noqa: PLC0415  (el mismo orden que arma correr_n6.armar_orden)
        random.Random(CN.SEMILLA_ORDEN).shuffle(orden)
        plan_de = dict(zip(orden, planes))
        ps = [{"id": q, "conjunto": "mezcla", "to": "cla", "tipo": "dato_directo", "subtipo": None, "necesidad": None,
               "familia": None, "cuenta_para_la_mezcla": True,
               "pregunta": f"consulta sintética {q} de la corrida en seco de N6 [[seco:{plan_de[q]}]]",
               "gold": {"anclas": [{"to": "cla", "punto": "5.1.1.", "detalle": "sintético", "pagina_pdf": 1}],
                        "criterios": [{"id": f"c{j}", "criterio": f"criterio sintético {q}.{j}", "cita": f"cita sintética {j}",
                                       "ancla": "5.1.1.", "pagina_pdf": 1} for j in (1, 2)]}} for q in ids]
        p = self.raiz / nombre / f"preguntas_{nombre}.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps({"version": 1, "unidad": "N6 — corrida en seco", "preguntas": ps}, ensure_ascii=False, indent=1)
                     + "\n", encoding="utf-8")
        return p, sha256(p)

    def entrada(self, nombre: str, planes: list[str], tope: float = CN.TOPE, freno: float = CN.FRENO) -> tuple[Path, str]:
        p, s = self.preguntas(nombre, planes)
        e = self.raiz / nombre / "entrada_seca.json"
        rc = CN.main(["entrada", "--modo-entrada", "seco", "--preguntas", str(p), "--sha-preguntas", s,
                      "--config-agentes", str(SECO / "config_agentes_seco_n6.json"),
                      "--lanzador", str(SECO / "lanzar_agente_n6_seco.py"), "--tope", str(tope), "--freno", str(freno),
                      "--entrada", str(e)])
        if rc:
            raise SystemExit(f"FRENO: no se armó la entrada seca de {nombre}")
        return e, sha256(e)

    def otro_paso(self) -> int:
        """El proceso de juguete, desacoplado: lo lanza un proceso intermedio, que espera su aviso, da su pid y termina; así el
        de juguete queda huérfano y no es descendiente de este proceso (la guarda excluye a los descendientes propios)."""
        intermedio = ("import subprocess, sys\n"
                      "p = subprocess.Popen([sys.executable, '-B', sys.argv[1], sys.argv[2]], stdin=subprocess.DEVNULL, "
                      "stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, start_new_session=True, text=True)\n"
                      "assert p.stdout.readline().strip() == 'listo'\nprint(p.pid)\n")
        r = subprocess.run([sys.executable, "-B", "-c", intermedio, str(self.otro), str(self.candado)], capture_output=True,
                           text=True, check=True)
        return int(r.stdout.strip())

    def terminar(self, pid: int) -> None:
        """Termina el proceso de juguete y espera su fin tomando su candado (una espera sin plazo, sobre el candado)."""
        import fcntl                     # noqa: PLC0415
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        with open(self.candado, "a") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            fcntl.flock(f, fcntl.LOCK_UN)

    def terminar_otro_paso_lanzado(self) -> bool:
        """El que lanzó una sesión del CLI falso (su pid, en pid_otro_paso_pago.txt): lo termina y espera su fin."""
        if not self.pid_otro.is_file():
            return False
        self.terminar(int(self.pid_otro.read_text(encoding="utf-8")))
        self.pid_otro.unlink()
        return True


def factory_juez_falso(salida: Path):
    return CN.factory_juez_falso(salida / "juez" / "cache")     # la del corredor, la misma de --juez-falso


def correr(t: Trabajo, accion: str, e: Path, s: str, salida: Path, P_sin: int | None = 2, P_con: int | None = 1,
           juez: bool = True, extra=()) -> int:
    argv = [accion, "--entrada", str(e), "--sha256-entrada", s, "--salida", str(salida), "--patron-de-prueba", t.token,
            "--timeout-s", "600", *extra]
    argv += ["--P-sin-codificador", str(P_sin)] if P_sin is not None else []
    argv += ["--P-con-codificador", str(P_con)] if P_con is not None else []
    return CN.main(argv, client_factory=factory_juez_falso(salida) if juez else None)


def dirs_de_sesiones(salida: Path) -> list[str]:
    return sorted(p.name for p in (salida / "agente").glob("lote_*/N6-*") if p.is_dir())


def lotes(salida: Path) -> int:
    return len([p for p in (salida / "agente").glob("lote_*") if p.is_dir()])


def lotes_n6(salida: Path) -> list[str]:
    """El lote de N6 (sin o con codificador) de cada lote del lanzador, en orden."""
    return [json.loads(p.read_text(encoding="utf-8"))["lote_n6"] for p in sorted((salida / "agente").glob("lote_*.json"))]


def registros_lote(salida: Path) -> list[dict]:
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted((salida / "agente").glob("lote_*/registro_lote.json"))]


def eventos(salida: Path) -> list[dict]:
    return json.loads((salida / "registro_n6.json").read_text(encoding="utf-8"))["corridas"][-1]["eventos"]


def todas_cerradas(salida: Path) -> bool:
    """Cada sesión lanzada terminó con su meta (ninguna quedó cortada por un freno de la tanda)."""
    return all((d / f"meta_{d.name}.json").is_file() for d in (salida / "agente").glob("lote_*/N6-*") if d.is_dir())


def estado(e: Path, s: str, salida: Path) -> dict:
    en = CN.cargar_entrada(e, s)
    return CN.estado(en, salida)


# --------------------------------------------------------------------------- #
def r0(t: Trabajo) -> None:
    rama("R0 correr_n6 importa lanzar_lote_paralelo_r5.py de HEAD, sin editarlo", sha256(Path(CN.R5.__file__)) == SHA_R5_HEAD,
         f"{Path(CN.R5.__file__).name}")
    rama("R0 la guarda del lote es la nueva (guardas_lote_n6), sobre guardas_lote_r5.py de HEAD",
         CN.R5.BASE.G is CN.G and sha256(Path(CN.G.R5.__file__)) == SHA_GUARDA_R5_HEAD)
    real = CN.G.PATRON_PAGO_REAL
    ve = all(re.search(real, x) for x in ("lanzar_lote_paralelo_r5.py", "correr_n6.py", "correr_b63.py", "correr_a2_2.py"))
    hueco = not any(re.search(CN.G.R5.PATRON_PAGO_REAL, x) for x in ("lanzar_lote_paralelo_r5.py", "correr_n6.py"))
    rama("R0 el patrón real de la guarda nueva ve lanzar_lote_paralelo_r5.py y correr_n6.py (por regex, sin pgrep)", ve)
    rama("R0 el de guardas_lote_r5.py de HEAD no los ve (el hueco que cierra)", hueco)
    CN.fijar_patron_de_prueba(t.token)
    rama("R0 el patrón de prueba tiene la forma del real y no coincide con ningún paso pago",
         CN.G.PATRON_PAGO != real and not re.search(CN.G.PATRON_PAGO, "correr_n6.py lanzar_lote_paralelo_r5.py"),
         CN.G.PATRON_PAGO)
    pid = t.otro_paso()
    visto = CN.G.otro_paso_pago()
    t.terminar(pid)
    despues = CN.G.otro_paso_pago()
    rama("R0 con el patrón de prueba la guarda ve el proceso de juguete y, terminado, no",
         [x["pid"] for x in visto] == [pid] and visto[0]["script"] == t.otro.name and not despues,
         f"visto {len(visto)}, después {len(despues)}")


def r1_r2(t: Trabajo) -> Path:
    planes = ["ok", "incorrecta", "juez_mal", "corte", "mal_formada", "infra_i1", "api_i1", "infra_siempre"]
    e, s = t.entrada("R1", planes)
    salida = t.raiz / "R1" / "salida"
    rc = correr(t, "todo", e, s, salida)
    st = CN.estado(CN.cargar_entrada(e, s), salida)
    clases = st["clases_finales"]
    rama("R1 completa: código 0", rc == 0, f"código {rc}")
    rama("R1 las clases finales: 20 completas, 4 cortes por R5, 4 mal formadas, 4 de infraestructura",
         clases == {"completa": 20, "corte_R5": 4, "mal_formada": 4, "infraestructura": 4}, json.dumps(clases, ensure_ascii=False))
    ds = dirs_de_sesiones(salida)
    i2 = [d for d in ds if d.endswith("-i2")]
    rama("R1 el reintento: 12 intentos 2 (9 en el lote 2, del sin codificador, y 3 en el 4, del con), y ninguna sesión con más de 2",
         lotes(salida) == 4 and len(i2) == 12 and len(ds) == 44 and all(len(v["intentos"]) <= 2 for v in st["por_sesion"].values())
         and len([d for d in (salida / "agente" / "lote_02").iterdir() if d.name.startswith("N6-")]) == 9,
         f"lotes {lotes(salida)}, carpetas {len(ds)}, intentos 2 {len(i2)}")
    en = json.loads(e.read_text(encoding="utf-8"))
    L = {x["nombre"]: x for x in en["lotes"]}
    l1 = [x["id"] for x in json.loads((salida / "agente" / "lote_01.json").read_text(encoding="utf-8"))["sesiones"]]
    l3 = [x["id"] for x in json.loads((salida / "agente" / "lote_03.json").read_text(encoding="utf-8"))["sesiones"]]
    rama("R1 los dos lotes: primero el sin codificador (B y BM25 de F1, 24) y después el con (T, 8), cada uno en el orden sellado "
         "restringido a sus sesiones",
         lotes_n6(salida) == ["sin_codificador"] * 2 + ["con_codificador"] * 2
         and L["sin_codificador"]["por_configuracion"] == {"B": 16, "F1_bm25": 8} and L["con_codificador"]["por_configuracion"] == {"T": 8}
         and l1 == L["sin_codificador"]["ids"] == [x["id"] for x in en["orden"]["sesiones"] if x["configuracion"] != "T"]
         and l3 == L["con_codificador"]["ids"] == [x["id"] for x in en["orden"]["sesiones"] if x["configuracion"] == "T"],
         f"lotes {lotes_n6(salida)}")
    regs = registros_lote(salida)
    medidas = [{k: v for k, v in h.items()} for r in regs[:1] for h in r["huellas_n6"].values() if isinstance(h, dict)]
    medidas3 = [h for h in regs[2]["huellas_n6"].values() if isinstance(h, dict)]
    rama("R1 el CLI medido: la huella de las sesiones de cada lote en sus tres partes (lanzador, CLI y servidores), en su registro",
         all(any(h.get("cli_gb", 0) > 0 and h.get("servidores_gb", 0) > 0 and h.get("lanzador_gb", 0) > 0 for h in m)
             for m in (medidas, medidas3)),
         f"medidas en el lote 1: {len(medidas)}, en el 3: {len(medidas3)}")
    tandas_ok = all(len(r["guarda_tanda_n6"]) == -(-len(r["sesiones"]) // P) and all(
        g["docker"]["ok"] and g["entra"] and "swap_gb" in g and g["docker"]["stats"] for g in r["guarda_tanda_n6"])
        for r, P in zip(regs, (2, 2, 1, 1)))
    rama("R1 la guarda de cada tanda: una por tanda (P = 2 en el sin, 1 en el con), con lo fijo, el swap y Docker registrados",
         tandas_ok, f"guardas por lote {[len(r['guarda_tanda_n6']) for r in regs]}")
    ev = eventos(salida)
    al = next(x for x in ev if x["evento"] == "memoria y Docker al lanzar")
    antes = next(x for x in ev if x["evento"] == "memoria antes del lote con codificador")["memoria"]
    cli_max = max(h.get("cli_gb", 0) for r in regs[:2] for h in r["huellas_n6"].values() if isinstance(h, dict))
    g3 = regs[2]["guarda_tanda_n6"]
    rama("R1 al lanzar, lo fijo y las dos P; antes del lote con codificador, la huella de CLI más alta del primero más 4,565 GB",
         al["memoria"]["lo_fijo_gb"] == 5.0 and al["memoria"]["entra"] and al["docker"]["ok"] and antes["entra"]
         and antes["cli_max_gb"] == cli_max > 0 and antes["huella_por_sesion_gb"] == round(CN.CM.HUELLA_SERVIDOR_CON_CODIFICADOR_GB
                                                                                           + cli_max, 3)
         and all(g["huella_por_sesion_gb"] >= antes["huella_por_sesion_gb"] for g in g3),
         f"lo fijo {al['memoria']['lo_fijo_gb']}, CLI más alto {antes['cli_max_gb']}, por sesión {antes['huella_por_sesion_gb']}")
    infra2 = [v for v in st["por_sesion"].values() if (v["final"] or {}).get("clase") == "infraestructura"]
    rama("R1 la que falla en los dos intentos queda de infraestructura, sin un tercero",
         len(infra2) == 4 and all(len(v["intentos"]) == 2 and not v["pendiente"] for v in infra2))
    res = json.loads((salida / "juez" / "resumen_juez_n6.json").read_text(encoding="utf-8"))
    agg = json.loads((salida / "juez" / "agregados_n6_ciego.json").read_text(encoding="utf-8"))
    rama("R1 el juez: 20 respuestas, 16 agregadas con sus 3 repeticiones y 4 con la salida del juez mal formada en las 3",
         res["n_respuestas"] == 20 and agg["n_agregados"] == 16 and len(agg["incompletas"]) == 4
         and res["errores_nuevos"] == 12 and res["llamadas_nuevas"] == 48,
         f"respuestas {res['n_respuestas']}, agregadas {agg['n_agregados']}, incompletas {len(agg['incompletas'])}, "
         f"llamadas {res['llamadas_nuevas']}, errores {res['errores_nuevos']}")
    rama("R1 los faltantes del juez, por motivo", res["faltantes_del_agente"] == {"corte_R5": 4, "mal_formada": 4,
                                                                              "infraestructura": 4},
         json.dumps(res["faltantes_del_agente"], ensure_ascii=False))
    reg = json.loads((salida / "registro_n6.json").read_text(encoding="utf-8"))
    c = reg["corridas"][-1]
    rama("R1 la foto del repo (la copia) al empezar y al terminar, sin b63/, igual", c["repo_igual"] is True
         and "data/experiment/banco_mcp/b63" in c["foto_repo_al_empezar"]["podadas"], f"{c['foto_repo_al_empezar']['n_archivos']} archivos")
    tabla = salida / "juez" / "desanonimizacion_SOLO_MESA" / "tabla_id_opaco_n6_SOLO_MESA.json"
    orden = json.loads((salida / "juez" / "orden_juez_n6.json").read_text(encoding="utf-8"))
    rama("R1 la tabla de ids opacos va aparte, y el orden del juez trae solo ids opacos",
         tabla.is_file() and all(x.startswith(CN.PREFIJO_ID) for x in orden["ids_opacos_en_orden"]))
    # R2
    antes_dirs, antes_lotes = dirs_de_sesiones(salida), lotes(salida)
    rc2 = correr(t, "todo", e, s, salida)
    res2 = json.loads((salida / "juez" / "resumen_juez_n6.json").read_text(encoding="utf-8"))
    rama("R2 retomar R1: código 0, ningún lote nuevo, ninguna sesión repetida y ninguna llamada nueva del juez",
         rc2 == 0 and dirs_de_sesiones(salida) == antes_dirs and lotes(salida) == antes_lotes and res2["llamadas_nuevas"] == 0,
         f"código {rc2}, lotes {lotes(salida)}, llamadas nuevas {res2['llamadas_nuevas']}")
    return salida


def r3(t: Trabajo) -> None:
    e, s = t.entrada("R3", ["otro_paso", "ok", "ok"])
    salida = t.raiz / "R3" / "salida"
    pid = t.otro_paso()
    rc0 = correr(t, "todo", e, s, salida)
    t.terminar(pid)
    rama("R3 con otro paso pago corriendo antes de empezar: frena (7) sin lanzar nada",
         rc0 == CN.OTRO_PASO_PAGO and not dirs_de_sesiones(salida), f"código {rc0}")
    rc1 = correr(t, "todo", e, s, salida)
    lanzadas1 = dirs_de_sesiones(salida)
    lanzado = t.terminar_otro_paso_lanzado()
    rama("R3 la primera sesión lanza otro paso pago: el lote frena (7) en la tanda siguiente, con sesiones sin lanzar",
         rc1 == CN.OTRO_PASO_PAGO and lanzado and 0 < len(lanzadas1) < 12, f"código {rc1}, lanzadas {len(lanzadas1)} de 12")
    rc2 = correr(t, "todo", e, s, salida)
    t.terminar_otro_paso_lanzado()
    ds = dirs_de_sesiones(salida)
    base = Counter(re.sub(r"-i\d+$", "", d) for d in ds)
    rama("R3 retomar con el proceso terminado: completa (0), sin repetir ninguna sesión ya terminada",
         rc2 == 0 and len(base) == 12 and set(lanzadas1) <= set(ds) and all(v == 1 for v in base.values()),
         f"código {rc2}, sesiones {len(base)}, carpetas {len(ds)}")


def r4(t: Trabajo) -> None:
    e, s = t.entrada("R4", ["caro", "caro", "caro"], tope=8.0, freno=5.0)
    salida = t.raiz / "R4" / "salida"
    rc1 = correr(t, "todo", e, s, salida)
    reg = json.loads((salida / "registro_n6.json").read_text(encoding="utf-8"))
    fin_lote = [x for x in reg["corridas"][-1]["eventos"] if x["evento"] == "terminó el lote"]
    lanzadas1 = dirs_de_sesiones(salida)
    st = CN.estado(CN.cargar_entrada(e, s), salida)
    rama("R4 el freno del gasto: el lote frena (2) por su guarda, con sesiones sin lanzar y el gasto debajo del freno",
         rc1 == CN.FRENO_GASTO and fin_lote and fin_lote[-1]["codigo"] == CN.FRENO_GASTO and 0 < len(lanzadas1) < 12
         and st["gasto_agente_guarda_usd"] <= 5.0, f"código {rc1}, lanzadas {len(lanzadas1)}, gasto {st['gasto_agente_guarda_usd']}")
    rc2 = correr(t, "todo", e, s, salida)
    reg2 = json.loads((salida / "registro_n6.json").read_text(encoding="utf-8"))
    ev = [x["evento"] for x in reg2["corridas"][-1]["eventos"]]
    rama("R4 retomar: frena (2) antes del lote, sin lanzar nada, porque lo ya gastado cuenta",
         rc2 == CN.FRENO_GASTO and dirs_de_sesiones(salida) == lanzadas1 and "freno del gasto antes del lote" in ev
         and "lanza el lote" not in ev, f"código {rc2}")


def r5(t: Trabajo) -> Path:
    e, s = t.entrada("R5", ["desconocida"])
    salida = t.raiz / "R5" / "salida"
    rc = correr(t, "todo", e, s, salida)
    st = CN.estado(CN.cargar_entrada(e, s), salida)
    rama("R5 tres formas desconocidas: frena (12) al juntar 3, sin el lote con codificador y sin juez", rc == CN.FORMAS_DESCONOCIDAS
         and st["clases_finales"] == {"desconocida": 3, "sin correr": 1} and lotes_n6(salida) == ["sin_codificador"]
         and not (salida / "juez" / "resumen_juez_n6.json").exists(),
         f"código {rc}, {json.dumps(st['clases_finales'], ensure_ascii=False)}")
    return e


def r6(t: Trabajo, salida_r1: Path, e5: Path) -> None:
    s5 = sha256(e5)
    antes = dirs_de_sesiones(salida_r1)
    rc = correr(t, "agente", e5, s5, salida_r1)
    rama("R6 otra entrada sobre la salida de R1: frena (8) sin lanzar nada", rc == CN.PRECONDICION
         and dirs_de_sesiones(salida_r1) == antes, f"código {rc}")
    t.con_cli_falso(False)
    try:
        rc2 = correr(t, "agente", e5, s5, t.raiz / "R6" / "salida_cli_real")
    finally:
        t.con_cli_falso(True)
    rama("R6 una entrada seca con el CLI real: frena (8) sin lanzar nada", rc2 == CN.PRECONDICION
         and not (t.raiz / "R6" / "salida_cli_real" / "agente").exists(), f"código {rc2}")
    er = CN.ENTRADA_DEFAULT
    rc3 = CN.main(["agente", "--entrada", str(er), "--sha256-entrada", sha256(er), "--salida", str(t.raiz / "R6" / "salida_real"),
                   "--P-sin-codificador", "2", "--P-con-codificador", "1", "--patron-de-prueba", t.token])
    rama("R6 la entrada real con el CLI falso: frena (8) sin lanzar nada", rc3 == CN.PRECONDICION
         and not (t.raiz / "R6" / "salida_real").exists(), f"código {rc3}")
    e1 = t.raiz / "R1" / "entrada_seca.json"
    llamadas = sum(len(CN.leer_jsonl(salida_r1 / "juez" / f"veredictos_r{r}.jsonl")) for r in CN.REPS_JUEZ)
    rc4 = correr(t, "juez", e1, sha256(e1), salida_r1, juez=False)
    rama("R6 una entrada seca nunca llama al juez real: sin el juez falso, frena (8) sin ninguna llamada",
         rc4 == CN.PRECONDICION and sum(len(CN.leer_jsonl(salida_r1 / "juez" / f"veredictos_r{r}.jsonl"))
                                        for r in CN.REPS_JUEZ) == llamadas, f"código {rc4}")


def r7(t: Trabajo) -> None:
    e, s = t.entrada("R7", ["ok"])
    casos = [("con lo fijo de 10 GB, la P 1 del lote con codificador", 10.0, 2, 1, "con codificador hasta 0"),
             ("con lo fijo de 5,5 GB, la P 2 del lote con codificador", 5.5, 2, 2, "con codificador hasta 1"),
             ("con lo fijo de 14,2 GB, la P 2 del lote sin codificador", 14.2, 2, 1, "sin codificador entra hasta 0")]
    for k, (que, fijo, P_sin, P_con, dice) in enumerate(casos, 1):
        t.sistema(**SISTEMA_BIEN | {"en_uso_gb": fijo})
        salida = t.raiz / "R7" / f"salida_{k}"
        rc = correr(t, "todo", e, s, salida, P_sin=P_sin, P_con=P_con)
        reg = json.loads((salida / "registro_n6.json").read_text(encoding="utf-8"))["corridas"][-1]
        rama(f"R7 {que} no entra al lanzar: frena (13) sin lanzar nada y dice cuál entra",
             rc == CN.MEMORIA and not (salida / "agente").exists() and dice in reg["freno"], f"código {rc}: {reg['freno']}")
    t.sistema(**SISTEMA_BIEN)
    rc = correr(t, "todo", e, s, t.raiz / "R7" / "salida_sin_P", P_con=None)
    rama("R7 sin una de las dos P: frena (8) sin lanzar nada", rc == CN.PRECONDICION and not (t.raiz / "R7" / "salida_sin_P").exists(),
         f"código {rc}")


def r8(t: Trabajo) -> None:
    e, s = t.entrada("R8", ["sube_memoria", "ok", "ok"])
    salida = t.raiz / "R8" / "salida"
    t.sistema(**SISTEMA_BIEN)
    rc1 = correr(t, "todo", e, s, salida)
    lanzadas1 = dirs_de_sesiones(salida)
    ev = eventos(salida)
    fin = [x for x in ev if x["evento"] == "terminó el lote"]
    P_lotes = {x["P"] for x in ev if x["evento"] == "lanza el lote"}
    rama("R8 la tanda que deja de entrar: frena (13) antes de la tanda siguiente, sin cortar las que corren y sin cambiar la P",
         rc1 == CN.MEMORIA and len(lanzadas1) == 2 and todas_cerradas(salida) and P_lotes == {2}
         and fin and "pasa de 14.5 GB antes de una tanda" in (fin[-1]["freno_de_la_guarda_de_la_tanda"] or ""),
         f"código {rc1}, lanzadas {len(lanzadas1)} de 12, P {sorted(P_lotes)}")
    t.sistema(**SISTEMA_BIEN)
    rc2 = correr(t, "todo", e, s, salida)
    ds = dirs_de_sesiones(salida)
    rama("R8 retomar con la memoria de vuelta: completa (0), sin repetir ninguna sesión",
         rc2 == 0 and len(ds) == 12 and set(lanzadas1) <= set(ds), f"código {rc2}, carpetas {len(ds)}")
    e2, s2 = t.entrada("R8b", ["sube_memoria_poco"])
    salida2 = t.raiz / "R8b" / "salida"
    t.sistema(**SISTEMA_BIEN)
    rc3 = correr(t, "todo", e2, s2, salida2, P_sin=2, P_con=2)
    ev3 = eventos(salida2)
    antes = [x["memoria"] for x in ev3 if x["evento"] == "memoria antes del lote con codificador"]
    rama("R8 antes del lote con codificador: lo fijo sube a 6 GB, la P 2 deja de entrar y frena (13) sin lanzarlo, diciendo que entra 1",
         rc3 == CN.MEMORIA and lotes_n6(salida2) == ["sin_codificador"] and len(dirs_de_sesiones(salida2)) == 3
         and antes and not antes[-1]["entra"] and antes[-1]["P_que_entra"] == 1 and antes[-1]["lo_fijo_gb"] == 6.0,
         f"código {rc3}, {antes[-1]['necesita_gb'] if antes else None} GB con P = 2")
    rc4 = correr(t, "todo", e2, s2, salida2, P_sin=2, P_con=1)
    rama("R8 retomar con P = 1 en el lote con codificador: completa (0), sin repetir el primer lote",
         rc4 == 0 and lotes_n6(salida2) == ["sin_codificador", "con_codificador"] and len(dirs_de_sesiones(salida2)) == 4,
         f"código {rc4}")
    t.sistema(**SISTEMA_BIEN)


def r9(t: Trabajo) -> None:
    e, s = t.entrada("R9", ["docker_no_sano", "ok"])
    for k, (que, cambio) in enumerate((("la VM de Docker de más (4 GB)", {"docker_mem_total": 4_000_000_000}),
                                       ("el contenedor no sano", {"docker_salud": "unhealthy"})), 1):
        t.sistema(**SISTEMA_BIEN | cambio)
        salida = t.raiz / "R9" / f"salida_{k}"
        rc = correr(t, "todo", e, s, salida)
        reg = json.loads((salida / "registro_n6.json").read_text(encoding="utf-8"))["corridas"][-1]
        rama(f"R9 {que} al lanzar: frena (14) sin lanzar nada", rc == CN.DOCKER and not (salida / "agente").exists(),
             f"código {rc}: {reg['freno']}")
    t.sistema(**SISTEMA_BIEN)
    salida = t.raiz / "R9" / "salida_tanda"
    rc1 = correr(t, "todo", e, s, salida)
    lanzadas1 = dirs_de_sesiones(salida)
    rama("R9 el contenedor que deja de estar sano a mitad del lote: frena (14) antes de la tanda siguiente, sin cortar las que corren",
         rc1 == CN.DOCKER and 0 < len(lanzadas1) < 8 and todas_cerradas(salida), f"código {rc1}, lanzadas {len(lanzadas1)} de 8")
    t.sistema(**SISTEMA_BIEN)
    rc2 = correr(t, "todo", e, s, salida)
    ds = dirs_de_sesiones(salida)
    rama("R9 retomar con el contenedor sano: completa (0), sin repetir ninguna sesión",
         rc2 == 0 and len(ds) == 8 and set(lanzadas1) <= set(ds), f"código {rc2}, carpetas {len(ds)}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo", type=Path, required=True)
    ap.add_argument("--salida-json", type=Path, required=True)
    a = ap.parse_args()
    if os.environ.get("NEO4J_URI") != "bolt://127.0.0.1:57687" or not os.environ.get("BANCO_VENV_VECTOR"):
        raise SystemExit("FRENO: hace falta NEO4J_URI del Neo4j propio de N6 y BANCO_VENV_VECTOR")
    os.environ["ANTHROPIC_API_KEY"] = "sk-ant-falso-corrida-en-seco-n6"
    os.environ["ANTHROPIC_BASE_URL"] = "http://127.0.0.1:9"
    t = Trabajo(a.trabajo)
    t.con_cli_falso(True)
    rama("la versión del CLI del PATH es la del CLI falso", CN.cli_falso(), CN.R5.cli_del_path()["version"])
    r0(t)
    salida_r1 = r1_r2(t)
    r3(t)
    r4(t)
    e5 = r5(t)
    r6(t, salida_r1, e5)
    r7(t)
    r8(t)
    r9(t)
    n_ok = sum(r["ok"] for r in RES)
    a.salida_json.parent.mkdir(parents=True, exist_ok=True)
    a.salida_json.write_text(json.dumps({"corrida_en_seco": "corrida_en_seco_n6.py", "token": t.token, "controles": RES,
                                         "ok": n_ok, "total": len(RES)}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{n_ok} de {len(RES)} controles PASS")
    return 0 if n_ok == len(RES) else 1


if __name__ == "__main__":
    raise SystemExit(main())
