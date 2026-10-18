"""Mesa, §155 (v3 de la §163): la prueba en seco del control entre tramos, sobre la tanda 1, en una copia de HEAD hecha con `git archive` (sin enlaces,
sin `.env` ni `NO_ABRIR_`). USD 0. El «tramo» de prueba son los TOs de la tanda 1 de las 548 unidades RI o `sin_raiz`, que es la base:
tiene que dar OK en los cuatro. Las pruebas en contra cambian solo los umbrales (un JSON de bases propio) o las métricas, con
`evaluar`, para ver que cada criterio frena. Toma la foto del repo antes y después.
Uso: python3 -I -B probar_control_entre_tramos_mesa.py <paquete H> <salida.txt>"""
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

PAQ, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
AQUI = PAQ / "decisiones_163_mesa/preregistro_tf"
REPO = Path.home() / "INGENIERIA IA/TESIS/bcra-regulatory-kg"
git = lambda *a: subprocess.run(["git", "--no-optional-locks", "-C", str(REPO), *a], capture_output=True, check=True)  # noqa: E731
T4 = ("data/experiment/tanda1/t4/", "data/experiment/tanda1/t3/muestras/unidades_a_la_vista_T4.json")   # lo que escribe T4 mientras corre (v3)
foto = lambda: hashlib.sha256(git("rev-parse", "HEAD").stdout + b"".join(l + b"\n" for l in git("status", "--porcelain=v1", "-uall").stdout.splitlines()
                                                                      if not l[3:].decode().startswith(T4))
                              + git("diff", "--", ".", *[f":(exclude){x}" for x in T4]).stdout).hexdigest()  # noqa: E731
sal = []


def p(*x):
    sal.append(" ".join(str(y) for y in x))
    print(*x, flush=True)


antes = foto()
bases = json.loads((AQUI / "salida_cifras_preregistro_tanda_final.json").read_text(encoding="utf-8"))
b = bases["bases_control_entre_tramos"]
pob = json.loads(git("show", "HEAD:data/experiment/tanda1/t3/muestras/poblaciones_t4.json").stdout)
tramo = sorted(t for t, c in pob["celda_por_to"].items() if c.startswith("RI:") or c == "NG:sin_raiz")
with tempfile.TemporaryDirectory(prefix="control_tramos_") as t:
    T = Path(t)
    copia = T / "copia"
    copia.mkdir()
    rutas = ["data/experiment/tanda1/t2/resumen_t2.py", "data/experiment/reextraccion_v2/manifiestos/tanda1_20tos_r2b.json",
             "data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b", "data/experiment/reextraccion_v2/corpus_tanda1/salida_r2b"]
    tar = subprocess.run(["git", "--no-optional-locks", "-C", str(REPO), "archive", "HEAD", "--", *rutas], capture_output=True, check=True).stdout
    subprocess.run(["tar", "-x", "-C", str(copia)], input=tar, check=True)
    malos = [x for x in copia.rglob("*") if x.is_symlink() or x.name.startswith(("NO_ABRIR_", ".env")) or x.name.endswith(".env")]
    p("copia con git archive de HEAD:", sum(1 for x in copia.rglob("*") if x.is_file()), "archivos; enlaces, .env o NO_ABRIR_:", len(malos))
    assert not malos
    (T / "tramo.json").write_text(json.dumps(tramo), encoding="utf-8")
    ctl = AQUI / "control_entre_tramos_tanda_final_mesa.py"
    corr = lambda bases_p: subprocess.run([sys.executable, "-I", "-B", str(ctl), "--repo", str(copia), "--manifiesto",  # noqa: E731
                                           "data/experiment/reextraccion_v2/manifiestos/tanda1_20tos_r2b.json", "--salida",
                                           str(copia / "data/experiment/reextraccion_v2/corpus_tanda1/salida_r2b"), "--tramo",
                                           str(T / "tramo.json"), "--bases", str(bases_p), "--out", str(T / "out.json")],
                                          capture_output=True, text=True)
    r = corr(AQUI / "salida_cifras_preregistro_tanda_final.json")
    p(f"la base como tramo ({len(tramo)} TOs: {', '.join(tramo)}): rc {r.returncode}")
    for l in r.stdout.strip().splitlines():
        p("  ", l)
    med = json.loads((T / "out.json").read_text(encoding="utf-8"))["medido"]
    ok_base = r.returncode == 0 and med["unidades"] == b["unidades_548"] and med["cola"] == b["cola_548"]
    p("  las unidades y la cola son las de la base (548 y 11):", ok_base)
    malas = 0
    for k, v in (("umbral_costo_por_unidad_1_3", 0.01), ("umbral_salidas_invalidas", 0.0), ("umbral_proporcion_cola_1_5", 0.001)):
        bb = json.loads(json.dumps(bases))
        bb["bases_control_entre_tramos"][k] = v
        (T / "b.json").write_text(json.dumps(bb), encoding="utf-8")
        r2 = corr(T / "b.json")
        frena = r2.returncode == 3 and any(l.startswith("FRENO") for l in r2.stdout.splitlines())
        if k == "umbral_salidas_invalidas" and med["salidas_invalidas_e1"] == 0:
            frena = r2.returncode == 0       # sin salidas inválidas en la base, el umbral 0 no frena: es lo correcto
        sin_inval = k == "umbral_salidas_invalidas" and med["salidas_invalidas_e1"] == 0
        etiqueta = ("no frena, y está bien: la base tiene 0 salidas inválidas" if sin_inval else "frena") if frena else "MAL"
        p(f"  en contra: {k} = {v} → {etiqueta} (rc {r2.returncode})")
        malas += not frena
    spec = importlib.util.spec_from_file_location("ctl", ctl)
    C = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(C)
    sint = {"unidades": 601, "gasto_usd": 601 * 0.02, "errores": 1, "cola": 5, "salidas_invalidas_e1": 0}
    e = C.evaluar(sint, b)
    p("  en contra, sintético con 1 error definitivo:", [x[3] for x in e], "→", "frena" if e[2][3] == "FRENO" else "MAL")
    malas += e[2][3] != "FRENO"
    sint = {"unidades": 601, "gasto_usd": 601 * 0.02, "errores": 0, "cola": 5, "salidas_invalidas_e1": 7}
    e = C.evaluar(sint, b)
    p("  en contra, sintético con 7 salidas inválidas de 601 (1,16 %):", [x[3] for x in e], "→", "frena" if e[1][3] == "FRENO" else "MAL")
    malas += e[1][3] != "FRENO"
despues = foto()
p("la foto del repo, igual antes y después:", antes == despues)
p("RESULTADO:", "PASA" if ok_base and not malas and antes == despues else "MAL")
OUT.write_text("\n".join(sal) + "\n", encoding="utf-8")
sys.exit(0 if ok_base and not malas and antes == despues else 1)
