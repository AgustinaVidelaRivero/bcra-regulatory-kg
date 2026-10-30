"""N7c, C1, paso 5: el control negativo de selftest_familias_nav_rel.py. Corre su main con una mutación en memoria por
vez (sin tocar ningún archivo) y anota cuántos casos fallan: cada mutación tiene que hacer fallar alguno.
Uso: <python del .venv> -B mutaciones_selftest_rel.py <raiz de la copia> <carpeta de trabajo nueva> <salida.json>
"""
import io, json, sys, contextlib
from pathlib import Path
sys.dont_write_bytecode = True
raiz, trabajo, salida = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3])
sys.path.insert(0, str(raiz / "data/experiment/banco_mcp/mcp_kg"))
import selftest_familias_nav_rel as T
FNR = T.FNR
orig = {"tope": FNR.TOPE_RELACIONADOS, "fuera": FNR.NavegadorRel._fuera, "grupo": dict(FNR.GRUPO_DE),
        "tipos": FNR.TIPOS_RELACIONADOS, "ver_punto": FNR.NavegadorRel.ver_punto, "max": FNR.CONTENEDOR_MAX_ANCLAS,
        "dirs": dict(FNR.DIRECCIONES)}
def restaurar():
    FNR.TOPE_RELACIONADOS = orig["tope"]; FNR.NavegadorRel._fuera = orig["fuera"]
    FNR.GRUPO_DE.clear(); FNR.GRUPO_DE.update(orig["grupo"]); FNR.TIPOS_RELACIONADOS = orig["tipos"]
    FNR.NavegadorRel.ver_punto = orig["ver_punto"]; FNR.CONTENEDOR_MAX_ANCLAS = orig["max"]
    FNR.DIRECCIONES.clear(); FNR.DIRECCIONES.update(orig["dirs"])
MUT = {
    "tope 11": lambda: setattr(FNR, "TOPE_RELACIONADOS", 11),
    "sin excluir hubs": lambda: setattr(FNR.NavegadorRel, "_fuera", lambda self, n: n in self.contenedores),
    "sin excluir contenedores": lambda: setattr(FNR.NavegadorRel, "_fuera", lambda self, n: n in self.hubs),
    "con aplica_a": lambda: (FNR.GRUPO_DE.__setitem__("aplica_a", "remisión"),
                             setattr(FNR, "TIPOS_RELACIONADOS", tuple(FNR.GRUPO_DE))),
    "sin remite_a": lambda: setattr(FNR, "TIPOS_RELACIONADOS", tuple(t for t in FNR.GRUPO_DE if t != "remite_a")),
    "umbral de contenedor 11": lambda: setattr(FNR, "CONTENEDOR_MAX_ANCLAS", 11),
    "direcciones cruzadas": lambda: FNR.DIRECCIONES.update({frozenset({"sale"}): "entra", frozenset({"entra"}): "sale"}),
    "sección antes de la salida": lambda: setattr(FNR.NavegadorRel, "ver_punto", lambda self, punto, max_nodos=15: (
        "\n".join(self.seccion_relacionados(self.resolver_punto(punto))) + "\n" + FNR.FNC.NavegadorCand.ver_punto(self, punto, max_nodos))
        if self.resolver_punto(punto) else FNR.FNC.NavegadorCand.ver_punto(self, punto, max_nodos)),
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
