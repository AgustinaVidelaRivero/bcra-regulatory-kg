#!/usr/bin/env python3
"""corrida_en_seco_n7c.py — La corrida en seco del corredor de B2 de N7c (n7c/correr_n7c.py), a USD 0, con el patrón del seco
de N6 (n6/corrida_en_seco_n6.py): el CLI falso (n7c/seco/claude_falso_n7c.py, que envuelve el de N6 sin editarlo), el juez falso
de la corrida en seco de A2.2 (correr_n6.factory_juez_falso), la guarda de otro paso pago con un patrón propio
(--patron-de-prueba), el sistema falso de N6 (n6/seco/sistema_falso_n6.py: vm_stat, footprint y docker) y el servidor de juguete
con las diez herramientas (n7c/seco/servidor_mcp_juguete_n7c.py, en sus tres variantes). Importa correr_n7c desde su carpeta y llama
a su main, sin tocar el sys.path: el mismo camino de imports que el corredor. Las sesiones son reales para el lote y para el
lanzador de N7c (que prepara cada una con la configuración de B2); el CLI, el servidor, el juez y el sistema son falsos. Ninguna
petición sale a la API (la clave del entorno es de prueba y la URL base apunta a un puerto cerrado). El Neo4j de B6.3 se usa
solo en la rama de la precondición, en lectura.

Ramas (las de N6 que aplican, con sus nombres, y las de B2):
  R0 el camino de imports (correr_n6, el lote, la guarda y la memoria de HEAD, por sha256) y la guarda: el patrón real nuevo ve
     correr_n7c.py, correr_juez_v3.py y corrida_cortada_v3.py, además de los de N6, y el de N6 no los ve (por regex, sin pgrep);
     el patrón real ve correr_juez_v3.py también como lo ve la guarda en una línea de comandos (script_python); con el patrón
     propio, la guarda ve el proceso de juguete y, terminado, no;
  R1 completa: 8 preguntas × 3 configuraciones (24 sesiones, P = 2), todas en el lote con codificador: la completa, el corte
     por R5, la mal formada, la falla de infraestructura (en el intento 1, el error de la API en el intento 1 y la que falla en
     los dos), el reintento con «-i2» en el lote siguiente, la respuesta que el juez no puede parsear y el juez con sus tres
     repeticiones; el lote sin codificador, vacío (no lanza ningún lote); cada sesión, preparada con la configuración de su brazo
     (el octavo cambio); la memoria, Docker y el contenedor de B6.3 en el registro; código 0;
  R2 retomar R1: ningún lote nuevo, ninguna sesión repetida y ninguna llamada nueva del juez;
  R3 otro paso pago: antes de empezar, frena (7) sin lanzar nada; lanzado por la primera sesión, frena (7) en la tanda
     siguiente; terminado, retomar completa sin repetir ninguna sesión;
  R4 el freno del gasto: el lote frena (2) por su guarda; retomar frena (2) antes del lote, sin lanzar nada;
  R5 tres formas desconocidas: frena (12) al juntar 3, sin juez;
  R6 lo que se controla de la entrada: otra entrada sobre la misma salida, una seca con el CLI real, la real de B2 y la del humo
     con el CLI falso, y el juez real con una entrada seca, frenan (8) sin lanzar nada;
  R7 la P que no entra al lanzar: con lo fijo de 10 GB (P 1 con codificador), de 5,5 GB (P 2 con codificador) y de 14,2 GB
     (P 1 del lote sin codificador, aunque esté vacío: la regla de N6, tal cual), frena (13); sin una de las dos P, frena (8);
  R8 la tanda que deja de entrar: frena (13) antes de la tanda siguiente, sin cortar las que corren; retomar completa;
  R9 Docker: la VM de más o el contenedor no sano al lanzar frenan (14); el contenedor que deja de estar sano a mitad del lote,
     (14) antes de la tanda siguiente; retomar completa;
  K  la configuración de agentes (cada campo con su fuente) y el id de sesión que no admite «+»;
  C1 a C8 cada uno de los ocho cambios, con su prueba (C2, la precondición con el Neo4j de B6.3, real y en lectura, y con una
     huella equivocada, que frena con 8);
  H  la entrada del humo: la real se carga (3 sesiones, una por configuración); su gemela seca corre y el control del humo
     (n7c/controlar_humo_n7c.py) da «pasa» en las tres; «no concluyente» y «no pasa», con sus casos.
Lo que no corre desde la copia, y qué lo cubre, va en el JSON (`no_corre_desde_la_copia`).
Imprime PASS/FAIL por control y escribe un JSON con el resumen (--salida-json), sin rutas absolutas. Código 1 si algo falla.
Uso: NEO4J_URI=bolt://127.0.0.1:47687 BANCO_VENV_VECTOR=<venv> .venv/bin/python -B data/experiment/banco_mcp/n7c/corrida_en_seco_n7c.py \\
       --trabajo <carpeta nueva fuera del repo> --salida-json <json>
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

import correr_n7c as C7                  # el corredor, desde su carpeta: el mismo camino de imports

CN = C7.CN
AQUI = Path(__file__).resolve().parent
BANCO = AQUI.parent
SECO = AQUI / "seco"
SECO_N6 = BANCO / "n6" / "seco"
RES: list[dict] = []
SHA_HEAD = {"n6/correr_n6.py": "69aab27cc3be", "agentes/lanzar_lote_paralelo.py": "1bcadb445ef4",
            "paralelo/guardas_lote_n6.py": "6287d60f9724", "n6/control_memoria_n6.py": "8c0d60e9fb23",
            "n6/lanzar_agente_n6.py": "2d29389a2c7d", "paralelo/lanzar_agente_n6_prueba.py": "86f88984e1aa",
            "agentes/lanzar_agente.py": "2f0074203832"}
SHA_R5_HEAD = "73b21753e826b91fb878b8ebc6f5fd34262e27be6a974fdb17051e825934e2e2"
SISTEMA_BIEN = {"en_uso_gb": 5.0, "libre_gb": 6.0, "huella_mb": 20, "docker_mem_total": 2_684_354_560, "docker_salud": "healthy"}
CONFIG_HUMO = AQUI / "config_agentes_n7c_humo.json"
CONFIG_B2 = AQUI / "config_agentes_n7c.json"
LANZADOR = AQUI / "lanzar_agente_n7c.py"
ENTRADA_B2, ENTRADA_HUMO = AQUI / "entrada_n7c_n3.json", AQUI / "entrada_n7c_humo.json"
CONTENEDOR = "neo4j-bcra-kg-indices-eval"
VARIANTE = {"N7": "N7", "N7c": "N7c", "N7c_amp": "N7c_amp"}


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
            w.write_text(f"#!/bin/sh\n# El {h} falso de la corrida en seco (n6/seco/sistema_falso_n6.py), con su estado.\n"
                         f"exec '{sys.executable}' -B '{SECO_N6 / 'sistema_falso_n6.py'}' {h} --estado '{self.estado_sistema}' \"$@\"\n",
                         encoding="utf-8")
            w.chmod(0o755)
        self.token = f"ensayoseco{os.getpid()}x"
        self.otro = self.raiz / f"{self.token}_n6.py"
        self.otro.write_text("import fcntl, signal, sys\nf = open(sys.argv[1], 'a')\nfcntl.flock(f, fcntl.LOCK_EX)\n"
                             "sys.stdout.write('listo\\n')\nsys.stdout.flush()\nsignal.pause()\n", encoding="utf-8")
        self.candado = self.raiz / "candado_otro_paso_pago"
        self.pid_otro = self.raiz / "pid_otro_paso_pago.txt"
        # El índice de juguete y los JSON de MCP de juguete, uno por variante, con el bloque `env` del JSON real de N7c.
        sys.path.insert(0, str(BANCO / "mcp_kg"))
        import selftest_familias_nav_rel_amp as ST   # noqa: PLC0415
        self.indice = self.raiz / "indice_juguete"
        ST.indice_juguete(self.indice)
        env_real = json.loads((AQUI / "mcp_kg_n7c_evaluado.json").read_text(encoding="utf-8"))["mcpServers"]["kg"]["env"]
        self.mcp_juguete = {}
        for v in VARIANTE.values():
            p = self.raiz / f"mcp_juguete_{v}.json"
            p.write_text(json.dumps({"mcpServers": {"kg": {"type": "stdio", "timeout": 600000, "command": sys.executable,
                                                           "args": ["-B", str(SECO / "servidor_mcp_juguete_n7c.py"), "--variante", v,
                                                                    "--indice", str(self.indice)],
                                                           "env": env_real}}}, ensure_ascii=False, indent=1), encoding="utf-8")
            self.mcp_juguete[v] = str(p)
        self.registro_mcp = self.raiz / "registro_mcp.jsonl"
        self.estado = self.raiz / "estado_cli_falso.json"
        self.estado.write_text(json.dumps({"planes": str(SECO / "planes_seco_n7c.json"), "otro_paso_pago": str(self.otro),
                                           "candado_otro_paso_pago": str(self.candado),
                                           "pid_otro_paso_pago": str(self.pid_otro), "estado_sistema": str(self.estado_sistema),
                                           "registro_mcp": str(self.registro_mcp), "mcp_juguete": self.mcp_juguete},
                                          ensure_ascii=False), encoding="utf-8")
        envol = self.bin / "claude"
        envol.write_text("#!/bin/sh\n# El CLI falso de la corrida en seco de N7c (claude_falso_n7c.py), con su estado.\n"
                         f"exec '{sys.executable}' -B '{SECO / 'claude_falso_n7c.py'}' --estado '{self.estado}' \"$@\"\n",
                         encoding="utf-8")
        envol.chmod(0o755)
        self.path_falso = f"{self.bin}:{self.bin_sistema}:{os.environ['PATH']}"
        self.path_real = f"{self.bin_sistema}:{os.environ['PATH']}"

    def sistema(self, **kw) -> dict:
        d = json.loads(self.estado_sistema.read_text(encoding="utf-8")) if self.estado_sistema.exists() else {}
        d.update(kw)
        self.estado_sistema.write_text(json.dumps(d), encoding="utf-8")
        return d

    def con_cli_falso(self, si: bool) -> None:
        os.environ["PATH"] = self.path_falso if si else self.path_real

    def preguntas(self, nombre: str, planes: list[str]) -> tuple[Path, str]:
        """Las preguntas sintéticas de una rama, con la forma de las de N3 (sin ninguna marca del juez: ni N6-, ni el nombre de
        una configuración o de un brazo); el plan k va a la pregunta k del orden de la entrada."""
        ids = [f"SECO-{i:02d}" for i in range(1, len(planes) + 1)]
        orden = sorted(ids)
        import random                     # noqa: PLC0415  (el mismo orden que arma correr_n7c.armar_orden)
        random.Random(C7.SEMILLA_ORDEN).shuffle(orden)
        plan_de = dict(zip(orden, planes))
        ps = [{"id": q, "conjunto": "mezcla", "to": "jug", "tipo": "varios_puntos", "subtipo": "remision", "necesidad": None,
               "familia": None, "cuenta_para_la_mezcla": True,
               "pregunta": f"consulta sintética {q} de la corrida en seco de B2 [[seco:{plan_de[q]}]]",
               "gold": {"anclas": [{"to": "jug", "punto": "1.1.", "detalle": "sintético", "pagina_pdf": 1},
                                   {"to": "jug", "punto": "2.2.", "detalle": "sintético", "pagina_pdf": 1}],
                        "criterios": [{"id": f"c{j}", "criterio": f"criterio sintético {q}.{j}", "cita": f"cita sintética {j}",
                                       "ancla": "1.1.", "pagina_pdf": 1} for j in (1, 2)]}} for q in ids]
        p = self.raiz / nombre / f"preguntas_{nombre}.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps({"version": 1, "unidad": "B2 — corrida en seco", "preguntas": ps}, ensure_ascii=False, indent=1)
                     + "\n", encoding="utf-8")
        return p, sha256(p)

    def entrada(self, nombre: str, planes: list[str], tope: float = 45.0, freno: float = 38.0,
                config: Path = CONFIG_HUMO, con_config: bool = True) -> tuple[Path, str]:
        p, s = self.preguntas(nombre, planes)
        e = self.raiz / nombre / "entrada_seca.json"
        argv = ["entrada", "--modo-entrada", "seco", "--preguntas", str(p), "--sha-preguntas", s,
                "--lanzador", str(LANZADOR), "--tope", str(tope), "--freno", str(freno), "--entrada", str(e)]
        argv += ["--config-agentes", str(config)] if con_config else []
        if C7.main(argv):
            raise SystemExit(f"FRENO: no se armó la entrada seca de {nombre}")
        return e, sha256(e)

    def otro_paso(self) -> int:
        intermedio = ("import subprocess, sys\n"
                      "p = subprocess.Popen([sys.executable, '-B', sys.argv[1], sys.argv[2]], stdin=subprocess.DEVNULL, "
                      "stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, start_new_session=True, text=True)\n"
                      "assert p.stdout.readline().strip() == 'listo'\nprint(p.pid)\n")
        r = subprocess.run([sys.executable, "-B", "-c", intermedio, str(self.otro), str(self.candado)], capture_output=True,
                           text=True, check=True)
        return int(r.stdout.strip())

    def terminar(self, pid: int) -> None:
        import fcntl                     # noqa: PLC0415
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        with open(self.candado, "a") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            fcntl.flock(f, fcntl.LOCK_UN)

    def terminar_otro_paso_lanzado(self) -> bool:
        if not self.pid_otro.is_file():
            return False
        self.terminar(int(self.pid_otro.read_text(encoding="utf-8")))
        self.pid_otro.unlink()
        return True


def correr(t: Trabajo, accion: str, e: Path, s: str, salida: Path, P_sin: int | None = 1, P_con: int | None = 2,
           juez: bool = True, neo4j: bool = False, extra=()) -> int:
    argv = [accion, "--entrada", str(e), "--sha256-entrada", s, "--salida", str(salida), "--patron-de-prueba", t.token,
            "--timeout-s", "600", *extra] + ([] if neo4j else ["--sin-neo4j"])
    argv += ["--P-sin-codificador", str(P_sin)] if P_sin is not None else []
    argv += ["--P-con-codificador", str(P_con)] if P_con is not None else []
    return C7.main(argv, client_factory=CN.factory_juez_falso(salida / "juez" / "cache") if juez else None)


def dirs_de_sesiones(salida: Path) -> list[str]:
    return sorted(p.name for p in (salida / "agente").glob("lote_*/N6-*") if p.is_dir())


def lotes(salida: Path) -> int:
    return len([p for p in (salida / "agente").glob("lote_*") if p.is_dir()])


def lotes_n6(salida: Path) -> list[str]:
    return [json.loads(p.read_text(encoding="utf-8"))["lote_n6"] for p in sorted((salida / "agente").glob("lote_*.json"))]


def registros_lote(salida: Path) -> list[dict]:
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted((salida / "agente").glob("lote_*/registro_lote.json"))]


def eventos(salida: Path) -> list[dict]:
    return json.loads((salida / "registro_n6.json").read_text(encoding="utf-8"))["corridas"][-1]["eventos"]


def todas_cerradas(salida: Path) -> bool:
    return all((d / f"meta_{d.name}.json").is_file() for d in (salida / "agente").glob("lote_*/N6-*") if d.is_dir())


def configuracion_de(sid: str) -> str:
    return re.sub(r"-i\d+$", "", sid).rsplit("-r", 1)[0].split("-", 2)[2].split("-", 1)[1]


# --------------------------------------------------------------------------- #
def r0(t: Trabajo) -> None:
    ok = {r: sha256(BANCO / r)[:12] == s for r, s in SHA_HEAD.items()}
    rama("R0 correr_n7c importa correr_n6, el lote, la guarda, la memoria y los lanzadores de HEAD, sin editarlos (sha256)",
         all(ok.values()) and sha256(Path(CN.R5.__file__)) == SHA_R5_HEAD and Path(CN.__file__).resolve() == (BANCO / "n6/correr_n6.py"),
         f"{sum(ok.values())} de {len(ok)} y lanzar_lote_paralelo_r5.py")
    rama("R0 la guarda del lote es guardas_lote_n6 (la de N6), con el patrón de B2", CN.R5.BASE.G is CN.G is C7.G)
    real = CN.G.PATRON_PAGO_REAL
    nuevos = ("correr_n7c.py", "correr_juez_v3.py", "corrida_cortada_v3.py")
    de_n6 = ("lanzar_lote_paralelo_r5.py", "correr_n6.py", "correr_b63.py", "correr_a2_2.py")
    rama("R0 C7 el patrón real nuevo ve correr_n7c.py, correr_juez_v3.py y corrida_cortada_v3.py, y los de N6 (por regex)",
         all(re.search(real, x) for x in nuevos + de_n6) and real == C7.PATRON_N6 + C7.SUFIJO_N7C)
    rama("R0 C7 el patrón de N6 no ve los tres nuevos (el hueco que cierra)", not any(re.search(C7.PATRON_N6, x) for x in nuevos))
    linea = "/opt/x/.venv/bin/python -B /opt/repo con espacios/data/experiment/correr_juez_v3.py --juez"
    guion = CN.G.script_python(linea)
    rama("R0 el patrón real que ve correr_juez_v3.py: la guarda lo saca de una línea de comandos de Python y lo ve; un grep no",
         guion is not None and re.search(real, CN.G.R5.BASE._nombre(guion)) is not None
         and CN.G.script_python("grep -c correr_juez_v3.py registro.txt") is None)
    CN.fijar_patron_de_prueba(t.token)
    rama("R0 el patrón de prueba tiene la forma del real y no coincide con ningún paso pago",
         CN.G.PATRON_PAGO != real and not re.search(CN.G.PATRON_PAGO, " ".join(nuevos + de_n6)), CN.G.PATRON_PAGO)
    pid = t.otro_paso()
    visto = CN.G.otro_paso_pago()
    t.terminar(pid)
    despues = CN.G.otro_paso_pago()
    rama("R0 con el patrón de prueba la guarda ve el proceso de juguete y, terminado, no",
         [x["pid"] for x in visto] == [pid] and visto[0]["script"] == t.otro.name and not despues,
         f"visto {len(visto)}, después {len(despues)}")


def k_config(t: Trabajo) -> None:
    b2, humo = json.loads(CONFIG_B2.read_text(encoding="utf-8")), json.loads(CONFIG_HUMO.read_text(encoding="utf-8"))
    b63 = json.loads((BANCO / "b63/v2/b2/config_agentes_b63.json").read_text(encoding="utf-8"))
    kg = b63["brazos"]["kg"]
    campos = ("prompt", "corte_R5", "modelo", "claude_code_version_sellada", "modo_harness", "env_por_sesion", "base")
    rama("K los campos que salen de config_agentes_b63.json, tal cual", all(b2[c] == b63[c] for c in campos))
    c = b63["corte_R5"]
    rama("K R5, del corte_R5 de B6.3: 30, 32 y 1,80", b2["R5"] == {"tope_tool_calls_prompt": c["tope_tool_calls_en_prompt"],
                                                                   "max_turns": c["max_turns"],
                                                                   "max_budget_usd": c["max_budget_usd_por_sesion"]}
         == {"tope_tool_calls_prompt": 30, "max_turns": 32, "max_budget_usd": 1.8})
    dif = {n: sorted(k for k in set(kg) | set(b) if kg.get(k) != b.get(k)) for n, b in b2["brazos"].items()}
    rama("K kg_N7 es el brazo kg de B6.3 campo por campo; kg_N7c y kg_N7c_amp cambian solo el JSON de MCP, la config y los "
         "módulos del servidor", dif == {"kg_N7": [], "kg_N7c": ["archivos_servidor", "config_servidor", "mcp_config"],
                                         "kg_N7c_amp": ["archivos_servidor", "config_servidor", "mcp_config"]}
         and b2["brazos"]["kg_N7c_amp"]["archivos_servidor"][0] == "mcp_kg/servidor_mcp_kg_nav_rel_amp.py", json.dumps(dif))
    rama("K configuraciones_n6: N7, N7c y N7c+ (N7c_amp), 3 repeticiones, con codificador; cada campo con su fuente",
         b2["configuraciones_n6"] == {c: {"brazo": b, "repeticiones": 3, "carga_codificador": True}
                                      for c, b in (("N7", "kg_N7"), ("N7c", "kg_N7c"), ("N7c_amp", "kg_N7c_amp"))}
         and b2["nombres"]["N7c_amp"] == "N7c+" and set(b2["fuentes_de_los_campos"]) >= set(campos) | {"R5", "configuraciones_n6"})
    sin_rep = lambda c: {k: (v if k != "configuraciones_n6" else {i: {kk: vv for kk, vv in x.items() if kk != "repeticiones"}  # noqa: E731
                                                                  for i, x in v.items()}) for k, v in c.items()}
    rama("K la del humo es la de B2 salvo las repeticiones (1), con los brazos byte a byte",
         sin_rep(humo) == sin_rep(b2) and all(x["repeticiones"] == 1 for x in humo["configuraciones_n6"].values())
         and C7._canonico(humo["brazos"]) == C7._canonico(b2["brazos"]))
    r = subprocess.run([sys.executable, "-I", "-B", str(AQUI / "armar_config_agentes_n7c.py"), "--verificar"],
                       capture_output=True, text=True)
    rama("K armar_config_agentes_n7c.py --verificar: las dos, iguales a las que arma", r.returncode == 0)
    import lanzar_lote_paralelo as LLP   # noqa: PLC0415  (en el path por correr_n6)
    rama("K un id de sesión con «+» no es válido (por eso la clave N7c_amp)",
         LLP.ID_VALIDO.match("N6-SECO-01-N7c+-r1") is None and LLP.ID_VALIDO.match("N6-SECO-01-N7c_amp-r1") is not None)


def r1_r2(t: Trabajo) -> Path:
    planes = ["ok", "incorrecta", "juez_mal", "corte", "mal_formada", "infra_i1", "api_i1", "infra_siempre"]
    e, s = t.entrada("R1", planes)
    salida = t.raiz / "R1" / "salida"
    rc = correr(t, "todo", e, s, salida)
    st = CN.estado(CN.cargar_entrada(e, s), salida)
    clases = st["clases_finales"]
    rama("R1 completa: código 0", rc == 0, f"código {rc}")
    rama("R1 las clases finales: 15 completas, 3 cortes por R5, 3 mal formadas, 3 de infraestructura",
         clases == {"completa": 15, "corte_R5": 3, "mal_formada": 3, "infraestructura": 3}, json.dumps(clases, ensure_ascii=False))
    ds = dirs_de_sesiones(salida)
    i2 = [d for d in ds if d.endswith("-i2")]
    rama("R1 el reintento: 9 intentos 2 en el lote 2, ninguna sesión con más de 2",
         lotes(salida) == 2 and len(i2) == 9 and len(ds) == 33 and all(len(v["intentos"]) <= 2 for v in st["por_sesion"].values())
         and len([d for d in (salida / "agente" / "lote_02").iterdir() if d.name.startswith("N6-")]) == 9,
         f"lotes {lotes(salida)}, carpetas {len(ds)}, intentos 2 {len(i2)}")
    en = json.loads(e.read_text(encoding="utf-8"))
    L = {x["nombre"]: x for x in en["lotes"]}
    l1 = [x["id"] for x in json.loads((salida / "agente" / "lote_01.json").read_text(encoding="utf-8"))["sesiones"]]
    ev = eventos(salida)
    nombres_ev = [x["evento"] for x in ev]
    rama("R1 el lote sin codificador, vacío: no lanza ningún lote; el con codificador, las 24 en el orden sellado",
         L["sin_codificador"]["n_sesiones"] == 0 and lotes_n6(salida) == ["con_codificador"] * 2
         and L["con_codificador"]["por_configuracion"] == {"N7": 8, "N7c": 8, "N7c_amp": 8}
         and l1 == L["con_codificador"]["ids"] == [x["id"] for x in en["orden"]["sesiones"]]
         and nombres_ev.index("lote sin_codificador terminado") < nombres_ev.index("lanza el lote"),
         f"lotes {lotes_n6(salida)}")
    # El octavo cambio: cada sesión, preparada con la configuración de B2 y el JSON de MCP de su brazo.
    cfg = json.loads(CONFIG_B2.read_text(encoding="utf-8"))
    reg_mcp = {}
    for x in (json.loads(y) for y in t.registro_mcp.read_text(encoding="utf-8").splitlines() if y.strip()):
        reg_mcp.setdefault(x["tag"], []).append(x)
    bien = 0
    for d in (salida / "agente").glob("lote_*/N6-*"):
        conf = configuracion_de(d.name)
        brazo = cfg["configuraciones_n6"][conf]["brazo"]
        cmd = json.loads((d / f"comando_{d.name}.json").read_text(encoding="utf-8"))
        argv = cmd["argv"]
        mcp = argv[argv.index("--mcp-config") + 1]
        meta_p = d / f"meta_{d.name}.json"
        meta = json.loads(meta_p.read_text(encoding="utf-8")) if meta_p.is_file() else {}
        bien += (mcp == "data/experiment/banco_mcp/" + cfg["brazos"][brazo]["mcp_config"]
                 and cmd["archivos_identidad"]["config_agentes"]["ruta"] == "data/experiment/banco_mcp/n7c/config_agentes_n7c.json"
                 and cmd["archivos_identidad"]["servidor"]["ruta"] == "data/experiment/banco_mcp/" + cfg["brazos"][brazo]["archivos_servidor"][0]
                 and [r["variante"] for r in reg_mcp.get(d.name, [])] == [VARIANTE[conf]]
                 and (not meta or meta["config_agentes_n6"]["ruta"] == "data/experiment/banco_mcp/n7c/config_agentes_n7c.json"))
    rama("R1 C8 cada sesión, preparada por lanzar_agente_n7c.py con la configuración de B2 y el JSON de MCP de su brazo",
         bien == len(ds) == 33, f"{bien} de {len(ds)}")
    regs = registros_lote(salida)
    medidas = [h for r in regs for h in r["huellas_n6"].values() if isinstance(h, dict)]
    rama("R1 el CLI medido: la huella de las sesiones en sus tres partes, en el registro de su lote",
         any(h.get("cli_gb", 0) > 0 and h.get("servidores_gb", 0) > 0 and h.get("lanzador_gb", 0) > 0 for h in medidas),
         f"medidas {len(medidas)}")
    rama("R1 C6 la guarda de cada tanda: una por tanda, con lo fijo, el swap y Docker del contenedor de B6.3",
         all(len(r["guarda_tanda_n6"]) == -(-len(r["sesiones"]) // 2) and all(
             g["docker"]["ok"] and g["entra"] and "swap_gb" in g and g["docker"]["contenedor"] == CONTENEDOR
             and g["docker"]["stats"]["Name"] == CONTENEDOR for g in r["guarda_tanda_n6"]) for r in regs),
         f"guardas por lote {[len(r['guarda_tanda_n6']) for r in regs]}")
    al = next(x for x in ev if x["evento"] == "memoria y Docker al lanzar")
    antes = next(x for x in ev if x["evento"] == "memoria antes del lote con codificador")["memoria"]
    rama("R1 al lanzar, lo fijo y las dos P; antes del lote con codificador, sin CLI medido (el primer lote vacío): 4,565 GB",
         al["memoria"]["lo_fijo_gb"] == 5.0 and al["memoria"]["entra"] and al["docker"]["ok"] and antes["entra"]
         and antes["cli_max_gb"] == 0.0 and antes["huella_por_sesion_gb"] == CN.CM.HUELLA_SERVIDOR_CON_CODIFICADOR_GB
         and al["docker"]["contenedor"] == CONTENEDOR,
         f"lo fijo {al['memoria']['lo_fijo_gb']}, por sesión {antes['huella_por_sesion_gb']}")
    infra2 = [v for v in st["por_sesion"].values() if (v["final"] or {}).get("clase") == "infraestructura"]
    rama("R1 la que falla en los dos intentos queda de infraestructura, sin un tercero",
         len(infra2) == 3 and all(len(v["intentos"]) == 2 and not v["pendiente"] for v in infra2))
    res = json.loads((salida / "juez" / "resumen_juez_n6.json").read_text(encoding="utf-8"))
    agg = json.loads((salida / "juez" / "agregados_n6_ciego.json").read_text(encoding="utf-8"))
    rama("R1 el juez: 15 respuestas, 12 agregadas con sus 3 repeticiones y 3 con la salida del juez mal formada en las 3",
         res["n_respuestas"] == 15 and agg["n_agregados"] == 12 and len(agg["incompletas"]) == 3
         and res["errores_nuevos"] == 9 and res["llamadas_nuevas"] == 36,
         f"respuestas {res['n_respuestas']}, agregadas {agg['n_agregados']}, llamadas {res['llamadas_nuevas']}, "
         f"errores {res['errores_nuevos']}")
    rama("R1 los faltantes del juez, por motivo", res["faltantes_del_agente"] == {"corte_R5": 3, "mal_formada": 3,
                                                                              "infraestructura": 3},
         json.dumps(res["faltantes_del_agente"], ensure_ascii=False))
    c = json.loads((salida / "registro_n6.json").read_text(encoding="utf-8"))["corridas"][-1]
    rama("R1 la foto del repo (la copia) al empezar y al terminar, igual", c["repo_igual"] is True,
         f"{c['foto_repo_al_empezar']['n_archivos']} archivos")
    orden = json.loads((salida / "juez" / "orden_juez_n6.json").read_text(encoding="utf-8"))
    rama("R1 la tabla de ids opacos va aparte, y el orden del juez trae solo ids opacos",
         (salida / "juez" / "desanonimizacion_SOLO_MESA" / "tabla_id_opaco_n6_SOLO_MESA.json").is_file()
         and all(x.startswith(CN.PREFIJO_ID) for x in orden["ids_opacos_en_orden"]))
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
    rc0 = correr(t, "todo", e, s, salida, P_con=1)
    t.terminar(pid)
    rama("R3 con otro paso pago corriendo antes de empezar: frena (7) sin lanzar nada",
         rc0 == CN.OTRO_PASO_PAGO and not dirs_de_sesiones(salida), f"código {rc0}")
    rc1 = correr(t, "todo", e, s, salida, P_con=1)
    lanzadas1 = dirs_de_sesiones(salida)
    lanzado = t.terminar_otro_paso_lanzado()
    rama("R3 la primera sesión lanza otro paso pago: el lote frena (7) en la tanda siguiente, con sesiones sin lanzar",
         rc1 == CN.OTRO_PASO_PAGO and lanzado and 0 < len(lanzadas1) < 9, f"código {rc1}, lanzadas {len(lanzadas1)} de 9")
    rc2 = correr(t, "todo", e, s, salida, P_con=1)
    t.terminar_otro_paso_lanzado()
    ds = dirs_de_sesiones(salida)
    base = Counter(re.sub(r"-i\d+$", "", d) for d in ds)
    rama("R3 retomar con el proceso terminado: completa (0), sin repetir ninguna sesión ya terminada",
         rc2 == 0 and len(base) == 9 and set(lanzadas1) <= set(ds) and all(v == 1 for v in base.values()),
         f"código {rc2}, sesiones {len(base)}, carpetas {len(ds)}")


def r4(t: Trabajo) -> None:
    e, s = t.entrada("R4", ["caro", "caro", "caro"], tope=8.0, freno=5.0)
    salida = t.raiz / "R4" / "salida"
    rc1 = correr(t, "todo", e, s, salida, P_con=1)
    reg = json.loads((salida / "registro_n6.json").read_text(encoding="utf-8"))
    fin_lote = [x for x in reg["corridas"][-1]["eventos"] if x["evento"] == "terminó el lote"]
    lanzadas1 = dirs_de_sesiones(salida)
    st = CN.estado(CN.cargar_entrada(e, s), salida)
    rama("R4 el freno del gasto: el lote frena (2) por su guarda, con sesiones sin lanzar y el gasto debajo del freno",
         rc1 == CN.FRENO_GASTO and fin_lote and fin_lote[-1]["codigo"] == CN.FRENO_GASTO and 0 < len(lanzadas1) < 9
         and st["gasto_agente_guarda_usd"] <= 5.0, f"código {rc1}, lanzadas {len(lanzadas1)}, gasto {st['gasto_agente_guarda_usd']}")
    rc2 = correr(t, "todo", e, s, salida, P_con=1)
    ev = [x["evento"] for x in json.loads((salida / "registro_n6.json").read_text(encoding="utf-8"))["corridas"][-1]["eventos"]]
    rama("R4 retomar: frena (2) antes del lote, sin lanzar nada, porque lo ya gastado cuenta",
         rc2 == CN.FRENO_GASTO and dirs_de_sesiones(salida) == lanzadas1 and "freno del gasto antes del lote" in ev
         and "lanza el lote" not in ev, f"código {rc2}")


def r5(t: Trabajo) -> Path:
    e, s = t.entrada("R5", ["desconocida"])
    salida = t.raiz / "R5" / "salida"
    rc = correr(t, "todo", e, s, salida, P_con=1)
    st = CN.estado(CN.cargar_entrada(e, s), salida)
    rama("R5 tres formas desconocidas: frena (12) al juntar 3, sin juez", rc == CN.FORMAS_DESCONOCIDAS
         and st["clases_finales"] == {"desconocida": 3} and lotes_n6(salida) == ["con_codificador"]
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
    for nombre, er in (("la de B2", ENTRADA_B2), ("la del humo", ENTRADA_HUMO)):
        sal = t.raiz / "R6" / f"salida_real_{er.stem}"
        rc3 = C7.main(["agente", "--entrada", str(er), "--sha256-entrada", sha256(er), "--salida", str(sal),
                       "--P-sin-codificador", "1", "--P-con-codificador", "1", "--patron-de-prueba", t.token])
        rama(f"R6 la entrada real ({nombre}) con el CLI falso: frena (8) sin lanzar nada", rc3 == CN.PRECONDICION
             and not sal.exists(), f"código {rc3}")
    e1 = t.raiz / "R1" / "entrada_seca.json"
    llamadas = sum(len(CN.leer_jsonl(salida_r1 / "juez" / f"veredictos_r{r}.jsonl")) for r in CN.REPS_JUEZ)
    rc4 = correr(t, "juez", e1, sha256(e1), salida_r1, juez=False)
    rama("R6 una entrada seca nunca llama al juez real: sin el juez falso, frena (8) sin ninguna llamada",
         rc4 == CN.PRECONDICION and sum(len(CN.leer_jsonl(salida_r1 / "juez" / f"veredictos_r{r}.jsonl"))
                                        for r in CN.REPS_JUEZ) == llamadas, f"código {rc4}")


def r7(t: Trabajo) -> None:
    e, s = t.entrada("R7", ["ok"])
    casos = [("con lo fijo de 10 GB, la P 1 del lote con codificador", 10.0, 1, 1, "con codificador hasta 0"),
             ("con lo fijo de 5,5 GB, la P 2 del lote con codificador", 5.5, 1, 2, "con codificador hasta 1"),
             ("con lo fijo de 14,2 GB, la P 1 del lote sin codificador (vacío)", 14.2, 1, 1, "sin codificador entra hasta 0")]
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
         f"código {rc1}, lanzadas {len(lanzadas1)} de 9, P {sorted(P_lotes)}")
    t.sistema(**SISTEMA_BIEN)
    rc2 = correr(t, "todo", e, s, salida)
    ds = dirs_de_sesiones(salida)
    rama("R8 retomar con la memoria de vuelta: completa (0), sin repetir ninguna sesión",
         rc2 == 0 and len(ds) == 9 and set(lanzadas1) <= set(ds), f"código {rc2}, carpetas {len(ds)}")


def r9(t: Trabajo) -> None:
    e, s = t.entrada("R9", ["docker_no_sano", "ok"])
    for k, (que, cambio) in enumerate((("la VM de Docker de más (4 GB)", {"docker_mem_total": 4_000_000_000}),
                                       ("el contenedor no sano", {"docker_salud": "unhealthy"})), 1):
        t.sistema(**SISTEMA_BIEN | cambio)
        salida = t.raiz / "R9" / f"salida_{k}"
        rc = correr(t, "todo", e, s, salida)
        dk = next(x for x in eventos(salida) if x["evento"] == "memoria y Docker al lanzar")["docker"]
        rama(f"R9 {que} al lanzar: frena (14) sin lanzar nada (el contenedor controlado, el de B6.3)",
             rc == CN.DOCKER and not (salida / "agente").exists() and dk["contenedor"] == CONTENEDOR, f"código {rc}")
    t.sistema(**SISTEMA_BIEN)
    salida = t.raiz / "R9" / "salida_tanda"
    rc1 = correr(t, "todo", e, s, salida, P_con=1)
    lanzadas1 = dirs_de_sesiones(salida)
    rama("R9 el contenedor que deja de estar sano a mitad del lote: frena (14) antes de la tanda siguiente, sin cortar las que corren",
         rc1 == CN.DOCKER and 0 < len(lanzadas1) < 6 and todas_cerradas(salida), f"código {rc1}, lanzadas {len(lanzadas1)} de 6")
    t.sistema(**SISTEMA_BIEN)
    rc2 = correr(t, "todo", e, s, salida, P_con=1)
    ds = dirs_de_sesiones(salida)
    rama("R9 retomar con el contenedor sano: completa (0), sin repetir ninguna sesión",
         rc2 == 0 and len(ds) == 6 and set(lanzadas1) <= set(ds), f"código {rc2}, carpetas {len(ds)}")


def cambios(t: Trabajo) -> None:
    # C1: las configuraciones.
    e0, _ = t.entrada("C1", ["ok"], con_config=False)
    en0 = json.loads(e0.read_text(encoding="utf-8"))
    rama("C1 las configuraciones: el valor por defecto de --config-agentes es la de B2 (main lo lee al llamarse)",
         CN.CONFIG_AGENTES == CONFIG_B2 and en0["config_agentes"]["ruta"] == "n7c/config_agentes_n7c.json")
    eb = CN.cargar_entrada(ENTRADA_B2, sha256(ENTRADA_B2))
    eh = CN.cargar_entrada(ENTRADA_HUMO, sha256(ENTRADA_HUMO))
    rama("C1 C4 C5 C6 C7 C8 la entrada real de B2: 270 sesiones, 90 por configuración, la configuración de B2, su lanzador, tope 45 "
         "y freno 38, la semilla N7C:orden:v1, el contenedor de B6.3 y el patrón nuevo, y se carga",
         eb["orden"]["n_sesiones"] == 270 and {x["nombre"]: x["por_configuracion"] for x in eb["lotes"]}["con_codificador"]
         == {"N7": 90, "N7c": 90, "N7c_amp": 90} and eb["config_agentes"]["ruta"] == "n7c/config_agentes_n7c.json"
         and eb["lanzador"] == {"ruta": "n7c/lanzar_agente_n7c.py", "sha256": sha256(LANZADOR)}
         and (eb["tope_usd"], eb["freno_usd"]) == (45.0, 38.0) and eb["orden"]["semilla"] == "N7C:orden:v1"
         and eb["docker"]["contenedor"] == CONTENEDOR and eb["guarda"]["patron"] == CN.G.PATRON_PAGO_REAL)
    # C2: el Neo4j de B6.3, real y en lectura.
    pre = C7.precondiciones(eh, con_neo4j=True)
    rama("C2 la precondición con el Neo4j de B6.3 (real, en lectura): da su huella; el control del Neo4j de N6 no se usa",
         pre["neo4j"]["ok"] and pre["neo4j"]["huella_contenido"] == C7.HUELLA_NEO4J_B63 and pre["neo4j"]["NEO4J_URI"] == C7.URI_B63
         and "control_neo4j_n6" not in sys.modules, f"{pre['neo4j']['n_nodos']} nodos, {pre['neo4j']['n_aristas']} aristas")
    e, s = t.entrada("C2", ["ok"])
    h = C7.HUELLA_NEO4J_B63
    C7.HUELLA_NEO4J_B63 = "0" * 64
    try:
        rc = correr(t, "todo", e, s, t.raiz / "C2" / "salida", neo4j=True)
    finally:
        C7.HUELLA_NEO4J_B63 = h
    reg = json.loads((t.raiz / "C2" / "salida" / "registro_n6.json").read_text(encoding="utf-8"))["corridas"][-1]
    rama("C2 con una huella equivocada: frena (8) sin lanzar nada", rc == CN.PRECONDICION
         and not (t.raiz / "C2" / "salida" / "agente").exists() and "Neo4j de B6.3" in reg["freno"], f"código {rc}")
    # C3: el control de las configuraciones por sha256.
    rama("C3 las tres configuraciones dan su sha256, la de agentes las nombra y sus brazos son los del lanzador",
         all(v["sha256_iguales"] and v["la_config_de_agentes_los_nombra"] for k, v in pre["configuraciones"].items()
             if k in C7.CONFIGURACIONES) and pre["configuraciones"]["brazos_iguales_a_los_del_lanzador"])
    r = "n7c/config_mcp_kg_n7c_amp_evaluado.json"
    viejo = C7.CONFIGURACIONES["N7c_amp"]["archivos"][r]
    C7.CONFIGURACIONES["N7c_amp"]["archivos"][r] = "0" * 64
    try:
        rc = correr(t, "todo", e, s, t.raiz / "C3" / "salida_sha")
    finally:
        C7.CONFIGURACIONES["N7c_amp"]["archivos"][r] = viejo
    rama("C3 una configuración que no da su sha256: frena (8) sin lanzar nada", rc == CN.PRECONDICION
         and not (t.raiz / "C3" / "salida_sha" / "agente").exists(), f"código {rc}")
    otra = t.raiz / "C3" / "config_lanzador_cambiada.json"
    c = json.loads(CONFIG_B2.read_text(encoding="utf-8"))
    c["brazos"]["kg_N7c"]["allowed_tools"] = "mcp__kg__ver_punto"
    otra.write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")
    vl = C7.CONFIG_LANZADOR
    C7.CONFIG_LANZADOR = otra
    try:
        rc = correr(t, "todo", e, s, t.raiz / "C3" / "salida_brazos")
    finally:
        C7.CONFIG_LANZADOR = vl
    rama("C3 una entrada cuyos brazos no son los de la configuración del lanzador: frena (8) sin lanzar nada",
         rc == CN.PRECONDICION and not (t.raiz / "C3" / "salida_brazos" / "agente").exists(), f"código {rc}")
    # C4: el tope y el freno.
    def entrada_cambiada(nombre: str, cambio) -> tuple[Path, str]:
        d = json.loads(ENTRADA_B2.read_text(encoding="utf-8"))
        cambio(d)
        p = t.raiz / "C4C5C7" / f"{nombre}.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        return p, sha256(p)

    def frena(p: Path, s_: str) -> bool:
        try:
            CN.cargar_entrada(p, s_)
        except CN.Freno as f:
            return f.codigo == CN.PRECONDICION
        return False
    rama("C4 el tope y el freno de B2: 45 y 38; una entrada real con 130 y 100 frena (8)",
         (CN.TOPE, CN.FRENO) == (45.0, 38.0) and frena(*entrada_cambiada("tope_n6", lambda d: d.update(tope_usd=130.0,
                                                                                                         freno_usd=100.0))))
    rama("C5 la semilla: el orden de N6 (N6:orden_corridas:v1) no es el que se recomputa y frena (8)",
         C7.armar_orden is CN.armar_orden and CN.SEMILLA_ORDEN == "N7C:orden:v1"
         and frena(*entrada_cambiada("semilla_n6", lambda d: d.update(orden=C7._armar_orden_n6(
             sorted({x["qid"] for x in d["orden"]["sesiones"]}), json.loads(CONFIG_B2.read_text(encoding="utf-8")),
             "N6:orden_corridas:v1")))))
    rama("C6 el contenedor de la guarda de memoria: el del Neo4j de B6.3", CN.CM.CONTENEDOR == CONTENEDOR)
    rama("C7 una entrada con el patrón de N6 frena (8)",
         frena(*entrada_cambiada("patron_n6", lambda d: d["guarda"].update(patron=C7.PATRON_N6))))
    rama("C8 las dos entradas nombran a n7c/lanzar_agente_n7c.py, con su sha256, y él fija la configuración de B2",
         eb["lanzador"] == eh["lanzador"] == {"ruta": "n7c/lanzar_agente_n7c.py", "sha256": sha256(LANZADOR)}
         and 'CONFIG_B2 = AQUI / "config_agentes_n7c.json"' in LANZADOR.read_text(encoding="utf-8"))


def humo(t: Trabajo, salida_r1: Path, e1: Path) -> None:
    import controlar_humo_n7c as CH       # noqa: PLC0415  (en n7c/, como este archivo)
    eh = CN.cargar_entrada(ENTRADA_HUMO, sha256(ENTRADA_HUMO))
    rama("H la entrada real del humo: 3 sesiones, una por configuración, con su configuración y el lanzador de B2",
         eh["orden"]["n_sesiones"] == 3 and {x["nombre"]: x["por_configuracion"] for x in eh["lotes"]}
         == {"sin_codificador": {}, "con_codificador": {"N7": 1, "N7c": 1, "N7c_amp": 1}}
         and eh["config_agentes"]["ruta"] == "n7c/config_agentes_n7c_humo.json"
         and C7.control_configuraciones(eh["_cfg"])["brazos_iguales_a_los_del_lanzador"])
    e, s = t.entrada("H", ["ok"])
    salida = t.raiz / "H" / "salida"
    rc = correr(t, "todo", e, s, salida, P_con=1)
    r = CH.controlar(CN.cargar_entrada(e, s), salida)
    rama("H la gemela seca del humo corre (0) y el control del humo da «pasa» en las tres configuraciones",
         rc == 0 and r["codigo"] == 0 and r["pasan"] == 3
         and {x["configuracion"]: (x["con_seccion"], x["con_familia"], x["con_cita"]) for x in r["sesiones"]}
         == {"N7": (0, 0, 0), "N7c": (1, 0, 0), "N7c_amp": (1, 1, 1)}, f"código {rc}, control {r['codigo']}")
    r1 = CH.controlar(CN.cargar_entrada(e1, sha256(e1)), salida_r1)
    rama("H el control del humo sobre R1: las que no llamaron a ver_punto (las de infraestructura en los dos intentos) dan «no "
         "concluyente» (código 2)", r1["codigo"] == 2 and r1["no_concluyentes"] == 3 and r1["no_pasan"] == 0,
         f"pasan {r1['pasan']}, no concluyentes {r1['no_concluyentes']}")
    log_n7 = next((Path(x["carpeta"]) / f"log_r1_{x['id']}.jsonl"
                   for v in CN.estado(CN.cargar_entrada(e, s), salida)["por_sesion"].values()
                   for x in [v["final"]] if v["sesion"]["configuracion"] == "N7"))
    rama("H «no pasa»: la salida de N7 leída como si fuera de N7c o de N7c+", CH.controlar_sesion(log_n7, "N7c")["veredicto"]
         == CH.controlar_sesion(log_n7, "N7c_amp")["veredicto"] == "no pasa")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo", type=Path, required=True)
    ap.add_argument("--salida-json", type=Path, required=True)
    a = ap.parse_args()
    if os.environ.get("NEO4J_URI") != C7.URI_B63 or not os.environ.get("BANCO_VENV_VECTOR"):
        raise SystemExit("FRENO: hace falta NEO4J_URI del Neo4j de B6.3 y BANCO_VENV_VECTOR")
    os.environ["ANTHROPIC_API_KEY"] = "sk-ant-falso-corrida-en-seco-n7c"
    os.environ["ANTHROPIC_BASE_URL"] = "http://127.0.0.1:9"
    t = Trabajo(a.trabajo)
    t.con_cli_falso(True)
    rama("la versión del CLI del PATH es la del CLI falso", CN.cli_falso(), CN.R5.cli_del_path()["version"])
    r0(t)
    k_config(t)
    salida_r1 = r1_r2(t)
    r3(t)
    r4(t)
    e5 = r5(t)
    r6(t, salida_r1, e5)
    r7(t)
    r8(t)
    r9(t)
    cambios(t)
    humo(t, salida_r1, t.raiz / "R1" / "entrada_seca.json")
    n_ok = sum(r["ok"] for r in RES)
    no_corre = [
        {"rama": "los servidores reales de N7, N7c y N7c+ (el .venv del JSON de MCP, el kg.json y la matriz densa no están en "
                 "la copia)", "la_cubre": "n7c/control_servidores_n7c.py desde el repo, después del commit, y el humo"},
        {"rama": "el CLI real, la API y el juez real", "la_cubre": "el humo (USD 5,40 como mucho del agente, más el juez)"},
        {"rama": "R8 de N6, su segunda parte (lo fijo que sube durante el primer lote, antes del lote con codificador)",
         "la_cubre": "no aplica: en B2 el primer lote (sin codificador) está vacío; antes del lote con codificador se mide "
                     "igual (R1)"}]
    a.salida_json.parent.mkdir(parents=True, exist_ok=True)
    a.salida_json.write_text(json.dumps({"corrida_en_seco": "corrida_en_seco_n7c.py", "controles": RES, "ok": n_ok,
                                         "total": len(RES), "no_corre_desde_la_copia": no_corre},
                                        ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{n_ok} de {len(RES)} controles PASS")
    return 0 if n_ok == len(RES) else 1


if __name__ == "__main__":
    raise SystemExit(main())
