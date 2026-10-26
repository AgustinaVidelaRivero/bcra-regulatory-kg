"""controlar_y_convertir_adjudicaciones_a2_2_mesa.py — mesa, §279 (26/10/2026): las adjudicaciones de A2.2 de la autora, selladas a las
14:28:58 (agregado recibido a las 14:30:07, tal cual: «Las marcas son mías, decididas a ciegas.»), controladas y convertidas por código en
los veredictos por id opaco que lee `analizar_a2_2.py --adjudicaciones`. Sin abrir ninguna marca ni ninguna observación: de la planilla, el
conversor lee solo la columna del veredicto, y nada se imprime de ella. USD 0.
  1. el sello: la planilla da su sha256 y sus bytes, y la hora del sello es la que dio la autora;
  2. el material: el armador de la §277 (con su sha256 revisado) lo rehace en una carpeta temporal desde HEAD, y cada archivo de la carpeta
     de la autora, salvo la planilla y el sello, es igual byte a byte; la clave rehecha es la del paquete de la mesa;
  3. la conversión, con el conversor de la §277 (con su sha256 revisado), a una salida nueva;
  4. cada id opaco de la salida es una respuesta que el juez dejó en `requiere_adjudicacion` (en los agregados ciegos de HEAD, sin abrir
     ninguna tabla `SOLO_MESA`), y cada veredicto es uno del mapping de EV2;
  5. el repo, igual antes y después.
  python3 -I -B controlar_y_convertir_adjudicaciones_a2_2_mesa.py <paquete H> <carpeta de lectura> <repo> <carpeta temporal> <salida .json>
"""
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

H, L, REPO, TMP, OUT = (Path(x) for x in sys.argv[1:6])
AD = H / "decisiones_277_mesa/adjudicaciones"
ARMADOR, CONVERSOR = AD / "codigo/armar_adjudicaciones_a2_2_mesa.py", AD / "codigo/convertir_marcas_adjudicacion_a2_2_mesa.py"
CLAVE = AD / "clave_para_despues/clave_adjudicaciones_a2_2_mesa.json"
SHA = {ARMADOR: "23591d04b39e5ed307c5c08781c2f6738c51622e2105ab69cc359693787b0d87",
       CONVERSOR: "a2e9a872cbdb6ac7a6f48382a9bab6cd9e9d652eb9ae65ea993c707959c429f8",
       CLAVE: "dbb71452b609625003d4a618fd9ad129975e4779f7deab09f4bd02c67980db28"}
SELLADO = "2026-10-26 14:28:58 -0300"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
git = lambda *a: subprocess.run(["git", "--no-optional-locks", "-C", str(REPO), *a], capture_output=True, check=True).stdout  # noqa: E731
ok = []


def c(nombre, cond, det=""):
    ok.append(bool(cond))
    print(("OK  " if cond else "MAL ") + nombre + (f" | {det}" if det else ""), flush=True)
    if not cond:
        raise SystemExit("FRENO: un control no dio; no sigo")


def foto():
    st = git("status", "--porcelain=v1", "-uall", "--", ".", ":!data/experiment/banco_mcp/a2_2")
    return hashlib.sha256(git("rev-parse", "HEAD") + st + git("diff")).hexdigest()


antes = foto()
c("0. las piezas de la §277 son las revisadas: el armador, el conversor y la clave", all(sha(p) == s for p, s in SHA.items()))
# 1. el sello
lin = (L / "sello_adjudicacion_a2_2.txt").read_text(encoding="utf-8").splitlines()
datos = [x for x in lin if x and not x.startswith("#")]
hora = next((x.split(":", 1)[1].strip() for x in lin if x.startswith("# sellado:")), None)
pl = L / "planilla_adjudicacion_a2_2.csv"
c("1. el sello: un renglón con el sha256 y los bytes de la planilla, y la hora del sello, la que dio la autora",
  len(datos) == 1 and datos[0].split()[0] == sha(pl) and int(datos[0].split()[1]) == pl.stat().st_size and hora == SELLADO,
  f"sellado {hora}; la planilla, {pl.stat().st_size} bytes")
# 2. el material, rehecho
if TMP.exists():
    shutil.rmtree(TMP)
TMP.mkdir(parents=True)
r = subprocess.run(["python3", "-I", "-B", str(ARMADOR), str(REPO), str(TMP / "clave.json"), str(TMP / "lectura")], capture_output=True,
                   text=True)
c("2a. el armador rehace el material desde HEAD", r.returncode == 0, r.stdout.strip()[-160:] or r.stderr.strip()[-200:])
reh = sorted(str(p.relative_to(TMP / "lectura")) for p in (TMP / "lectura").rglob("*") if p.is_file())
aut = sorted(str(p.relative_to(L)) for p in L.rglob("*") if p.is_file() and p.name != ".DS_Store")
fuera = {"planilla_adjudicacion_a2_2.csv", "sello_adjudicacion_a2_2.txt"}
distintos = [x for x in reh if x not in fuera and (not (L / x).exists() or (L / x).read_bytes() != (TMP / "lectura" / x).read_bytes())]
PLANTILLA = ["LEEME_primero.md", "regla_de_adjudicacion_a2_2.md", "sellar_planilla_adjudicacion_a2_2.py"]
de_la_plantilla = all((L / x).read_bytes() == (AD / "para_leer_plantilla" / x).read_bytes() for x in PLANTILLA)
c("2b. el material de la carpeta de la autora es, archivo por archivo y byte a byte, el que rehace el armador, y los tres de la plantilla "
  "(el LEEME, la regla y el sellador), los de la §277; solo la planilla y el sello son de ella; la clave rehecha es la del paquete",
  not distintos and set(aut) - set(reh) == {"sello_adjudicacion_a2_2.txt", *PLANTILLA} and set(reh) - set(aut) == set()
  and de_la_plantilla and (TMP / "clave.json").read_bytes() == CLAVE.read_bytes(),
  f"{len(reh)} archivos rehechos y {len(PLANTILLA)} de la plantilla; distintos: {len(distintos)}")
shutil.rmtree(TMP)
# 3. la conversión
if OUT.exists():
    raise SystemExit("FRENO: la salida ya existe: no se pisa")
r = subprocess.run(["python3", "-I", "-B", str(CONVERSOR), str(L), str(CLAVE), str(REPO), str(OUT)], capture_output=True, text=True)
c("3. la conversión: un veredicto por id opaco de la clave, desde las marcas selladas y el mapping de EV2 de HEAD", r.returncode == 0,
  r.stdout.strip() or r.stderr.strip()[-200:])
# 4. los ids y los veredictos
v = json.loads(OUT.read_text(encoding="utf-8"))
clave = json.loads(CLAVE.read_text(encoding="utf-8"))
pend = set()
for etapa in ("n1", "recorridas"):
    agg = json.loads(git("show", f"HEAD:data/experiment/banco_mcp/a2_2/juez/{etapa}/agregados_{etapa}_ciego.json"))
    pend |= {a["id_opaco"] for a in agg["agregados"] if a["veredicto_pregunta"] == "requiere_adjudicacion"}
ids_clave = {i for f in clave["fichas"] for i in f["ids_opacos"]}
c("4. cada id opaco de la salida es una respuesta que el juez dejó en requiere_adjudicacion (agregados ciegos de HEAD), son los de la "
  "clave, y cada veredicto es correcto, parcial o incorrecto",
  set(v) == ids_clave and set(v) <= pend and set(v.values()) <= {"correcto", "parcial", "incorrecto"},
  f"{len(v)} ids de {len(clave['fichas'])} fichas; en requiere_adjudicacion en HEAD: {len(pend)}")
c("5. el repo, igual antes y después (sin la carpeta de A2.2)", foto() == antes)
print(f"la salida: {OUT.name}, sha256 {sha(OUT)}")
print(f"controles: {sum(ok)} de {len(ok)}")
