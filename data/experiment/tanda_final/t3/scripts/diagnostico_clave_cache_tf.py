"""B6.1, tanda final, T3, punto 4: la causa de que selftest_clave_cache dé rc=1 después de T2, sin abrir sus salidas (el retiro de cuentas
las mandó a NO_ABRIR_ porque no son las de A3 sin cuentas) y sin leer las bases de la caché. USD 0. Solo lee:
  - el resumen del retiro (resumen_sin_cuentas_t3.json): las rutas de los campos que difieren de A3 sin cuentas, sin valores;
  - el código del selftest (data/experiment/mantenimiento/code/selftest_clave_cache.py): qué variación tiene el campo
    `clave_en_cache_e1` (variacion_to_nuevo, V23 en el perfil sellado y R23 en el r2b) y con qué TO y qué unidad (TO_NUEVO,
    UNIDAD_TO_NUEVO), por su árbol sintáctico;
  - el manifiesto de la tanda final: si ese TO está, en qué lugar de `orden_corrida` y en qué tramo;
  - la E0 de la tanda final y la de la partición b584: si el chunk de esa unidad es el mismo en las dos;
  - la tabla que contrasta el selftest (`mantenimiento/tabla_reprocesamiento.md`), leída con su `leer_tabla` y su `RE_IDS_TABLA`
    (importados del selftest sin correrlo): qué fila es la de índice N de `contraste_tabla/filas[N]` y qué variación es su `observado[i]`.
La variación supone que ese TO nunca se extrae: su clave tiene que faltar en la caché de E1 (miss). Si T2 lo extrajo con el perfil r2b
y el chunk es el mismo, la clave del perfil r2b está en la caché y R23 deja de dar miss.
Uso: python3 -I -B diagnostico_clave_cache_tf.py <raíz> <resumen_sin_cuentas_t3.json> <salida.json>
"""
import ast
import json
import sys
from pathlib import Path

RAIZ, RES, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3])
SELF = RAIZ / "data/experiment/mantenimiento/code/selftest_clave_cache.py"
MAN = RAIZ / "data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json"
E0 = RAIZ / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b"
B584 = RAIZ / "data/experiment/segmentacion_84/b584_particion"

res_retiro = json.loads(RES.read_text(encoding="utf-8"))
rutas = res_retiro.get("json_rutas_que_difieren") or []
arbol = ast.parse(SELF.read_text(encoding="utf-8"))
const = {n.targets[0].id: n.value.value for n in arbol.body if isinstance(n, ast.Assign) and len(n.targets) == 1
         and isinstance(n.targets[0], ast.Name) and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str)}
to, unidad = const["TO_NUEVO"], const["UNIDAD_TO_NUEVO"]
con_campo = sorted(f.name for f in ast.walk(arbol) if isinstance(f, ast.FunctionDef)
                   and any(isinstance(x, ast.Constant) and x.value == "clave_en_cache_e1" for x in ast.walk(f)))
man = json.loads(MAN.read_text(encoding="utf-8"))
orden = man["orden_corrida"]


def chunk(p: Path):
    d = json.loads(p.read_text(encoding="utf-8"))
    return {c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)}.get(unidad)


c_tf, c_b = chunk(E0 / f"chunks_{to}.json"), chunk(B584 / to / f"chunks_{to}.json")
import re  # noqa: E402

_ns = {"re": re, "Path": Path}
_defs = [n for n in arbol.body if (isinstance(n, ast.FunctionDef) and n.name == "leer_tabla") or
         (isinstance(n, ast.Assign) and any(getattr(t, "id", "") in ("COLUMNAS", "RE_IDS_TABLA") for t in n.targets))]
exec(compile(ast.Module(body=_defs, type_ignores=[]), str(SELF), "exec"), _ns)
filas_tabla = [f for f in _ns["leer_tabla"](RAIZ / "data/experiment/mantenimiento/tabla_reprocesamiento.md") if "error" not in f]
filas_citadas = {}
for r in rutas:
    m = re.match(r"^/contraste_tabla/filas\[(\d+)\]/observado\[(\d+)\]/", r)
    if m:
        i, j = int(m.group(1)), int(m.group(2))
        ids = _ns["RE_IDS_TABLA"].findall(filas_tabla[i]["variaciones"]) if i < len(filas_tabla) else []
        filas_citadas[f"filas[{i}]/observado[{j}]"] = {"fila": filas_tabla[i]["fila"] if i < len(filas_tabla) else None,
                                                       "variacion": ids[j] if j < len(ids) else None}
res = {"rutas_que_difieren_de_A3_sin_cuentas": rutas,
       "filas_de_la_tabla_que_difieren": filas_citadas,
       "todas_en_la_variacion_del_TO_nuevo_o_derivadas": all(
           r.startswith(("/perfil_r2b/variaciones[30]/", "/contraste_tabla/", "/variaciones_con_discrepancia", "/veredicto")) for r in rutas),
       "funciones_con_clave_en_cache_e1": con_campo, "TO_NUEVO": to, "UNIDAD_TO_NUEVO": unidad,
       "el_TO_esta_en_la_tanda_final": to in [t["id"] for t in man["tos"]],
       "lugar_en_orden_corrida": (orden.index(to) + 1) if to in orden else None, "tramo": (1 if orden.index(to) < 30 else 2) if to in orden else None,
       "chunk_en_la_E0_de_la_tanda_final": c_tf is not None, "chunk_en_b584": c_b is not None,
       "chunk_igual_en_las_dos": c_tf is not None and c_tf == c_b}
res["la_fila_que_difiere_es_la_de_R23"] = bool(filas_citadas) and all(v["variacion"] == "R23" for v in filas_citadas.values())
res["lectura"] = ("R23 supone que la unidad de un TO fuera de la tanda 0 no está en la caché de E1. T2 extrajo ese TO con el perfil r2b y "
                  "el mismo chunk, así que la clave está y R23 deja de dar miss: el selftest falla por su supuesto, no por el código de la "
                  "clave." if res["el_TO_esta_en_la_tanda_final"] and res["chunk_igual_en_las_dos"] else "la causa no es esa")
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k != "rutas_que_difieren_de_A3_sin_cuentas"}, ensure_ascii=False, indent=1))
