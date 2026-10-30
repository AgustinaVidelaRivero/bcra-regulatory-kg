"""N7c+, C2-bis: el control negativo de mcp_kg/selftest_familias_nav_rel_amp.py. Corre su main con una mutación en memoria
por vez (sin tocar ningún archivo) y anota cuántos casos fallan: cada mutación tiene que hacer fallar alguno.
Uso: <python del .venv> -B mutaciones_selftest_rel_amp.py <raiz de la copia> <carpeta de trabajo nueva> <salida.json>
"""
import contextlib
import io
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
raiz, trabajo, salida = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3])
if trabajo.exists():
    raise SystemExit("ABORTO: la carpeta de trabajo tiene que ser nueva")
sys.path.insert(0, str(raiz / "data/experiment/banco_mcp/mcp_kg"))
import selftest_familias_nav_rel_amp as T  # noqa: E402

A = T.FNRA
N = A.NavegadorRelAmp
ORIG_MOD = {x: getattr(A, x) for x in ("TOPE_FAMILIA", "unidad_para_citar")}
ORIG_PAR = dict(A.PARENTESCOS)
ORIG_MET = {x: getattr(N, x) for x in ("raiz_familia", "familia", "archivo_de", "ver_punto")}


def restaurar():
    for x, v in ORIG_MOD.items():
        setattr(A, x, v)
    A.PARENTESCOS.clear()
    A.PARENTESCOS.update(ORIG_PAR)
    for x, v in ORIG_MET.items():
        setattr(N, x, v)


def raiz_siempre_padre(self, k):
    padre = self.puntos[k]["padre"]
    return None if padre is None or self.puntos[padre]["tipo"] == "to" else (padre, 2)


def raiz_sin_regla_del_to(self, k):
    padre = self.puntos[k]["padre"]
    if padre is None or self.puntos[padre]["tipo"] == "to":
        return None
    return self.puntos[padre]["padre"], 3


def raiz_con_padre_to(self, k):
    padre = self.puntos[k]["padre"]
    return (padre, 2) if self.puntos[padre]["tipo"] == "to" else ORIG_MET["raiz_familia"](self, k)


def familia_con(fuera_de):
    def familia(self, k):
        r = self.raiz_familia(k)
        if r is None:
            return []
        raiz, niveles = r
        fuera = fuera_de(self, k)
        filas = [(c, *self.parentesco(k, c, raiz)) for c in self._descendientes(raiz, niveles) if c not in fuera]
        return sorted(filas, key=lambda f: (f[1], f[0]))
    return familia


def tope10(self, k):
    return {f[0] for f in self.relacionados(k)[:A.FNR.TOPE_RELACIONADOS]}


def familia_por_clave(self, k):
    return sorted(ORIG_MET["familia"](self, k), key=lambda f: f[0])


def ver_punto_orden(partes):
    def ver_punto(self, punto, max_nodos=15):
        out = A.FNR.NavegadorRel.ver_punto(self, punto, max_nodos)
        k = self.resolver_punto(punto)
        if k is None:
            return out
        return partes(self, k, out)
    return ver_punto


def ver_punto_sin_existir(self, punto, max_nodos=15):
    out = ORIG_MET["ver_punto"](self, punto, max_nodos)
    return out if self.resolver_punto(punto) else out + "\n" + A.SIN_FAMILIA


MUT = {
    "tope 11": lambda: setattr(A, "TOPE_FAMILIA", 11),
    "raíz siempre el padre": lambda: setattr(N, "raiz_familia", raiz_siempre_padre),
    "raíz el abuelo aunque sea el TO": lambda: setattr(N, "raiz_familia", raiz_sin_regla_del_to),
    "con el padre TO, la familia del TO": lambda: setattr(N, "raiz_familia", raiz_con_padre_to),
    "sin excluir el punto": lambda: setattr(N, "familia", familia_con(
        lambda s, k: {*s._ancestros(k), *s.puntos[k]["hijos"]} | tope10(s, k))),
    "sin excluir los ancestros": lambda: setattr(N, "familia", familia_con(
        lambda s, k: {k, *s.puntos[k]["hijos"]} | tope10(s, k))),
    "sin excluir los hijos": lambda: setattr(N, "familia", familia_con(
        lambda s, k: {k, *s._ancestros(k)} | tope10(s, k))),
    "sin excluir la sección de N7c": lambda: setattr(N, "familia", familia_con(
        lambda s, k: {k, *s._ancestros(k), *s.puntos[k]["hijos"]})),
    "excluyendo la sección de N7c entera, sin su tope": lambda: setattr(N, "familia", familia_con(
        lambda s, k: {k, *s._ancestros(k), *s.puntos[k]["hijos"]} | {f[0] for f in s.relacionados(k)})),
    "orden solo por la clave": lambda: setattr(N, "familia", familia_por_clave),
    "tío y sobrino cruzados": lambda: A.PARENTESCOS.update({(2, 1): "sobrino", (1, 2): "tío"}),
    "la cita con el id del TO": lambda: setattr(N, "archivo_de", lambda self, k: self.puntos[k]["to"]),
    "la cita con la unidad tal cual": lambda: setattr(A, "unidad_para_citar", lambda u: u),
    "la cita con «Punto» también en las secciones": lambda: setattr(A, "unidad_para_citar", lambda u: f"Punto {u}"),
    "la familia antes de la sección de N7c": lambda: setattr(N, "ver_punto", ver_punto_orden(
        lambda s, k, out: "\n".join(s.seccion_familia(k)) + "\n" + out + "\n" + s.linea_cita(k))),
    "la cita antes de la familia": lambda: setattr(N, "ver_punto", ver_punto_orden(
        lambda s, k, out: out + "\n" + "\n".join([s.linea_cita(k)] + s.seccion_familia(k)))),
    "agregados en un punto que no existe": lambda: setattr(N, "ver_punto", ver_punto_sin_existir),
}
res = {}
for i, (nombre, mut) in enumerate(MUT.items()):
    mut()
    try:
        out = trabajo / f"mut{i}.json"
        sys.argv = ["selftest", "--trabajo", str(trabajo / f"mut{i}"), "--salida", str(out)]
        with contextlib.redirect_stdout(io.StringIO()):
            rc = T.main()
        res[nombre] = {"codigo": rc, "fallos": len(json.loads(out.read_text(encoding="utf-8"))["fallos"])}
    except Exception as e:
        res[nombre] = {"codigo": None, "excepcion": type(e).__name__}
    finally:
        restaurar()
res["todas_fallan"] = all(v.get("codigo") != 0 for k, v in res.items() if isinstance(v, dict))
salida.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False))
