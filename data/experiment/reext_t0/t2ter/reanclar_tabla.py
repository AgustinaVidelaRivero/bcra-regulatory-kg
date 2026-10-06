"""U-REEXT-T0, T2-ter (decisión 4 de la autora sobre el FRENO T2-bis): las anclas de la tabla de reprocesamiento a
runner_corpus.py y a cliente_e1.py, llevadas al código final por contenido, con el método de T2-bis (difflib sobre el
archivo contra el que se escribió cada ancla y el archivo final). Cada mención se escribió contra el código de
a64f8bd (anterior a T2-bis), salvo F20, que T2-bis re-ancló contra el de 4ab7a0a.

USD 0, sin red, sin git. No escribe en el repo: lee la tabla y las versiones de origen (extraídas antes con
`git show <commit>:<ruta>`) y escribe la tabla re-anclada y el informe donde se le indica.

Uso:
  python -B reanclar_tabla.py --tabla RUTA --runner-final RUTA --cliente-final RUTA --origen DIR \
      --out-tabla RUTA --out-informe RUTA
  python -B reanclar_tabla.py --verificar --tabla-origen RUTA --tabla RUTA ... (sin --out-tabla)
  DIR tiene <commit>_runner_corpus.py y <commit>_cliente_e1.py de a64f8bd y de 4ab7a0a.
--verificar: no re-ancla; comprueba que la tabla dada ya tiene cada ancla en su lugar (0 desplazadas) y que el texto
anclado en el código final es el mismo que el anclado en el código de origen, salvo donde el código cambió.
"""
import argparse
import difflib
import json
import re
from pathlib import Path

RUTAS = {"runner_corpus.py": "data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py",
         "cliente_e1.py": "data/experiment/reextraccion_v2/e1_extractor/cliente_e1.py"}
ORIGEN = {"defecto": "a64f8bd", "F20": "4ab7a0a"}
# Rangos cuyo código se reescribió (un extremo no tiene línea igual en el archivo final): se fijan por contenido, con la
# función entera a la que apunta el ancla.
REESCRITOS = {("cliente_e1.py", "a64f8bd", 279, 293): "def crear_reintento_forma(self"}

ap = argparse.ArgumentParser()
ap.add_argument("--tabla", type=Path, required=True)
ap.add_argument("--runner-final", type=Path, required=True)
ap.add_argument("--cliente-final", type=Path, required=True)
ap.add_argument("--out-tabla", type=Path)
ap.add_argument("--out-informe", type=Path, required=True)
ap.add_argument("--origen", type=Path, required=True)
ap.add_argument("--tabla-origen", type=Path, default=None, help="la tabla contra la que se re-ancló (para --verificar)")
ap.add_argument("--verificar", action="store_true")
a = ap.parse_args()

final = {"runner_corpus.py": a.runner_final.read_text(encoding="utf-8").splitlines(),
         "cliente_e1.py": a.cliente_final.read_text(encoding="utf-8").splitlines()}
origen = {(f, rev): (a.origen / f"{rev}_{f}").read_text(encoding="utf-8").splitlines()
          for f in RUTAS for rev in set(ORIGEN.values())}


def mapa(viejo: list[str], nuevo: list[str]) -> dict[int, int]:
    m = {}
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, viejo, nuevo, autojunk=False).get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                m[i1 + k + 1] = j1 + k + 1
    return m


MAPAS = {k: mapa(v, final[k[0]]) for k, v in origen.items()}


def funcion_entera(lineas: list[str], cabecera: str) -> tuple[int, int]:
    ini = next(i for i, x in enumerate(lineas, 1) if x.strip().startswith(cabecera))
    sangria = len(lineas[ini - 1]) - len(lineas[ini - 1].lstrip())
    fin = ini
    for i in range(ini + 1, len(lineas) + 1):
        x = lineas[i - 1]
        if x.strip() and len(x) - len(x.lstrip()) <= sangria:
            break
        if x.strip():
            fin = i
    return ini, fin


RE_INI = re.compile(r"(runner_corpus\.py|cliente_e1\.py):(\d+)(?:-(\d+))?")
RE_SIG = re.compile(r"`, `:(\d+)(?:-(\d+))?")


def menciones(linea: str):
    """(archivo, [(ini, fin, span_en_la_linea)]) por cada mención de la línea."""
    out = []
    for m in RE_INI.finditer(linea):
        rangos = [(int(m.group(2)), int(m.group(3) or m.group(2)), (m.start(2), m.end()))]
        pos = m.end()
        while True:
            n = RE_SIG.match(linea, pos)
            if not n:
                break
            rangos.append((int(n.group(1)), int(n.group(2) or n.group(1)), (n.start(1), n.end())))
            pos = n.end()
        out.append((m.group(1), rangos))
    return out


def fila(linea: str) -> str:
    m = re.match(r"\| (F\w+) \|", linea) or re.match(r"- \*\*(F\w+)\.", linea)
    return m.group(1) if m else "texto"


tabla = a.tabla.read_text(encoding="utf-8").splitlines()
informe, nuevas = [], list(tabla)
for i, linea in enumerate(tabla, 1):
    f_ = fila(linea)
    rev = ORIGEN["F20"] if f_ == "F20" else ORIGEN["defecto"]
    reemplazos = []
    for archivo, rangos in menciones(linea):
        m = MAPAS[(archivo, rev)]
        for ini, fin, span in rangos:
            if a.verificar:
                # la tabla ya está re-anclada: el texto anclado en el final contra el de origen, vía la tabla de origen
                continue
            n_ini, n_fin = m.get(ini), m.get(fin)
            nota = ""
            if n_ini is None or n_fin is None:
                cab = REESCRITOS.get((archivo, rev, ini, fin))
                if cab is None:
                    informe.append({"linea": i, "fila": f_, "archivo": archivo, "ancla": f"{ini}-{fin}",
                                    "estado": "SIN_RESOLVER"})
                    continue
                n_ini, n_fin = funcion_entera(final[archivo], cab)
                nota = f"reescrito: la función «{cab}» entera"
            txt_new = f"{n_ini}-{n_fin}" if n_ini != n_fin else f"{n_ini}"
            txt_old = f"{ini}-{fin}" if ini != fin else f"{ini}"
            if (n_ini, n_fin) != (ini, fin):
                reemplazos.append((span, txt_old, txt_new))
            informe.append({"linea": i, "fila": f_, "archivo": archivo, "origen": rev, "ancla": txt_old,
                            "final": txt_new, "cambia": (n_ini, n_fin) != (ini, fin), "nota": nota})
    for (s, e), txt_old, txt_new in sorted(reemplazos, reverse=True):
        seg = nuevas[i - 1][s:e]
        nuevas[i - 1] = nuevas[i - 1][:s] + seg.replace(txt_old, txt_new, 1) + nuevas[i - 1][e:]

if a.verificar:
    # 0 desplazadas: re-anclar la tabla de origen debe dar exactamente la tabla dada
    assert a.tabla_origen, "--verificar necesita --tabla-origen"
    base = a.tabla_origen.read_text(encoding="utf-8").splitlines()
    dada = {}
    for i, linea in enumerate(tabla, 1):
        for archivo, rangos in menciones(linea):
            dada.setdefault((fila(linea), archivo), []).extend((x, y) for x, y, _ in rangos)
    esperada, texto_distinto = {}, []
    for linea in base:
        f_ = fila(linea)
        rev = ORIGEN["F20"] if f_ == "F20" else ORIGEN["defecto"]
        for archivo, rangos in menciones(linea):
            m = MAPAS[(archivo, rev)]
            for ini, fin, _ in rangos:
                n_ini, n_fin = m.get(ini), m.get(fin)
                if n_ini is None or n_fin is None:
                    n_ini, n_fin = funcion_entera(final[archivo], REESCRITOS[(archivo, rev, ini, fin)])
                else:
                    viejo = origen[(archivo, rev)][ini - 1:fin]
                    nuevo = final[archivo][n_ini - 1:n_fin]
                    if viejo != nuevo:
                        texto_distinto.append({"fila": f_, "archivo": archivo, "origen": f"{ini}-{fin}",
                                               "final": f"{n_ini}-{n_fin}", "lineas_viejas": len(viejo),
                                               "lineas_nuevas": len(nuevo)})
                esperada.setdefault((f_, archivo), []).append((n_ini, n_fin))
    faltan = {f"{k[0]} {k[1]}": sorted(set(v) - set(dada.get(k, []))) for k, v in esperada.items()
              if set(v) - set(dada.get(k, []))}
    res = {"menciones_de_origen": sum(len(v) for v in esperada.values()), "desplazadas": faltan,
           "n_desplazadas": sum(len(v) for v in faltan.values()),
           "rangos_con_texto_distinto (el código cambió dentro del rango)": texto_distinto}
    a.out_informe.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: v for k, v in res.items() if k != "rangos_con_texto_distinto (el código cambió dentro del rango)"},
                     ensure_ascii=False))
    print("rangos con texto distinto:", len(texto_distinto))
else:
    a.out_tabla.write_text("\n".join(nuevas) + "\n", encoding="utf-8")
    a.out_informe.write_text(json.dumps(informe, ensure_ascii=False, indent=1), encoding="utf-8")
    cambian = [x for x in informe if x.get("cambia")]
    print(f"menciones: {len(informe)} | cambian: {len(cambian)} | sin resolver: "
          f"{sum(1 for x in informe if x.get('estado') == 'SIN_RESOLVER')}")
    for x in informe:
        if x.get("cambia") or x.get("estado"):
            print(f"  línea {x['linea']} ({x['fila']}) {x['archivo']}: {x['ancla']} → {x.get('final')} {x.get('nota', '')}")
