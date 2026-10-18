"""Mesa, §139 (17/10/2026), U-MED-DESAMB, parte 3: arma el código preparado de S1, S2 y C1 como copias parchadas de los archivos de HEAD,
con sus diffs, SIN APLICAR. Cada cambio entra detrás de un parámetro que por defecto vale lo de hoy (False o None): con el defecto, la
salida es la misma. Lee los archivos del clon de git; escribe solo en <paquete>/decisiones_139_mesa/parte3/codigo_preparado/.
Frena si un fragmento a reemplazar no aparece exactamente una vez (el archivo de HEAD cambió).
Uso: python3 -I -B armar_parches_mesa.py <clon> <dir de salida>"""
import difflib
import hashlib
import sys
from pathlib import Path

CL, OUT = Path(sys.argv[1]), Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)

E4 = "data/experiment/reextraccion_v2/corpus_v2/r1_e4.py"
RC = "data/experiment/reresolucion_catalogo/reresolver_catalogo.py"
INV = "data/experiment/reextraccion_v2/corpus_v2/r1_invariantes.py"

AYUDA_S1_S2 = '''

# U-MED-DESAMB (mesa, 17/10/2026), reglas candidatas S1 y S2: PROPUESTAS, sin aplicar. Con s1 = s2 = False (el defecto) la
# decisión es la de L-ESQ-R2 §3.3, punto 5 (data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md:580-582).
# S1: cuando la regla del texto (R2, el calificador o R3) y la sugerencia del modelo dan ids distintos, gana la regla del texto.
# S2: la sugerencia del modelo sin mención verificada no resuelve: la relación va a cuarentena con la sugerencia guardada, como la
#     parte A de la enmienda 6.
REGLAS_TEXTO_S1 = ("R2", "R2_calificador", "R3")


def candidata_s1_s2(regla: dict | None, modelo: str | None, nivel: str | None, s1: bool, s2: bool) -> tuple | None:
    """("S1", id, método) si S1 decide; ("S2", None, None) si S2 manda a cuarentena; None si ninguna toca la relación."""
    regla = regla or {}
    if s1 and modelo and regla.get("regla") in REGLAS_TEXTO_S1 and regla.get("id") and regla["id"] != modelo:
        metodo = "R2_" + "+".join(regla.get("criterios") or []) if regla["regla"] == "R2" else regla["regla"]
        return ("S1", regla["id"], metodo)
    if s2 and modelo and nivel not in ("exacta", "tokens"):
        return ("S2", None, None)
    return None
'''

PARCHES = {
    E4: [
        ('MOTIVOS_PARTE_A = ("colectivo_sin_sujeto_por_defecto", "sin_mencion", "mencion_no_verificada")\n',
         'MOTIVOS_PARTE_A = ("colectivo_sin_sujeto_por_defecto", "sin_mencion", "mencion_no_verificada")\n' + AYUDA_S1_S2),
        ('                           versiones: dict, parte_a: bool = False) -> dict:\n',
         '                           versiones: dict, parte_a: bool = False, s1: bool = False, s2: bool = False) -> dict:\n'),
        ('            final, metodo = None, None\n            if regla["regla"] == "R1":\n'
         '                final, metodo = regla["id"], "R1_" + "+".join(c for c in regla["criterios"] if c in CRITERIOS_R1)\n'
         '            elif sin_alcance and regla["motivo"] in MOTIVOS_PARTE_A:\n'
         '                pass                    # enmienda 6, parte A: cuarentena con la sugerencia guardada\n'
         '            elif modelo:\n',
         '            final, metodo, cand = None, None, None\n            if regla["regla"] == "R1":\n'
         '                final, metodo = regla["id"], "R1_" + "+".join(c for c in regla["criterios"] if c in CRITERIOS_R1)\n'
         '            elif sin_alcance and regla["motivo"] in MOTIVOS_PARTE_A:\n'
         '                pass                    # enmienda 6, parte A: cuarentena con la sugerencia guardada\n'
         '            elif (cand := candidata_s1_s2(regla, modelo, nivel, s1, s2)):\n'
         '                final, metodo = cand[1], cand[2]   # U-MED-DESAMB, S1 o S2 (con S2, cuarentena)\n'
         '            elif modelo:\n'),
        ('                    "desacuerdo_regla_modelo": desacuerdo, "catalogo_sha256": versiones["catalogo_sha256"]}\n',
         '                    "desacuerdo_regla_modelo": desacuerdo, "catalogo_sha256": versiones["catalogo_sha256"],\n'
         '                    **({"regla_candidata": cand[0]} if cand else {})}\n'),
        ('def reresolver_registro(filas: list[dict], idx: dict, rol_por_archivo: dict, archivo_por_to: dict,\n'
         '                        catalogo_sha256: str) -> dict:\n',
         'def reresolver_registro(filas: list[dict], idx: dict, rol_por_archivo: dict, archivo_por_to: dict,\n'
         '                        catalogo_sha256: str, s1: bool = False, s2: bool = False) -> dict:\n'),
        ('            elif modelo and archivo not in rol_por_archivo and motivo in MOTIVOS_PARTE_A:\n'
         '                pass                    # parte A: sigue en cuarentena mientras el documento no tenga alcance\n'
         '            elif modelo:\n',
         '            elif modelo and archivo not in rol_por_archivo and motivo in MOTIVOS_PARTE_A:\n'
         '                pass                    # parte A: sigue en cuarentena mientras el documento no tenga alcance\n'
         '            elif (cand := candidata_s1_s2(r, modelo, f.get("mencion_verificada"), s1, s2)):\n'
         '                final, metodo = cand[1], cand[2]   # U-MED-DESAMB, S1 o S2 (con S2, sigue en cuarentena)\n'
         '            elif modelo:\n'),
    ],
    RC: [
        ('def decidir(f: dict, padre: str | None, idx: dict, prefijos: list, rol: str | None, sin_alcance: bool = False) -> dict:\n',
         'def decidir(f: dict, padre: str | None, idx: dict, prefijos: list, rol: str | None, sin_alcance: bool = False,\n'
         '            s1: bool = False, s2: bool = False) -> dict:\n'),
        ('    elif sin_alcance and regla.get("motivo") in E4.MOTIVOS_PARTE_A:\n        pass\n    elif modelo:\n',
         '    elif sin_alcance and regla.get("motivo") in E4.MOTIVOS_PARTE_A:\n        pass\n'
         '    elif (cand := E4.candidata_s1_s2(regla, modelo, nivel, s1, s2)):\n'
         '        final, metodo = cand[1], cand[2]   # U-MED-DESAMB, S1 o S2 (con S2, cuarentena)\n'
         '    elif modelo:\n'),
    ],
    INV: [
        ('def merge_grafos_guardado(grafos: dict[str, dict]) -> dict:\n',
         'def merge_grafos_guardado(grafos: dict[str, dict], codigo_comunicacion=None) -> dict:\n'),
        ('    colis = colisiones_cross_to(grafos)\n',
         '    # U-MED-DESAMB (mesa, 17/10/2026), regla candidata C1, PROPUESTA sin aplicar: con `codigo_comunicacion` (una función\n'
         '    # nodo -> código normalizado o None), las Comunicacion de TOs distintos con el mismo código se unen en el id de la primera,\n'
         '    # en el orden de los TOs, y lo registra `uniones_c1`; la colisión no va a la adjudicación. Con None (el defecto), la guarda\n'
         '    # de siempre.\n'
         '    uniones_c1: list[dict] = []\n'
         '    if codigo_comunicacion is not None:\n'
         '        grafos, uniones_c1 = _unir_comunicaciones_c1(grafos, codigo_comunicacion)\n'
         '    colis = colisiones_cross_to(grafos)\n'),
        ('        if _es_sujeto_catalogo(primero):\n            continue\n',
         '        if _es_sujeto_catalogo(primero):\n            continue\n'
         '        if codigo_comunicacion is not None and primero.get("type") == "Comunicacion" and nid in {u["id"] for u in uniones_c1}:\n'
         '            continue                    # C1: la unión la hace el merge sellado, con sus conflictos registrados\n'),
        ('    m["adjudicacion_cross_to"] = adjudicacion\n',
         '    m["adjudicacion_cross_to"] = adjudicacion\n'
         '    if codigo_comunicacion is not None:\n'
         '        m["uniones_c1"] = uniones_c1\n'),
        ('def merges_arista_de(grafos_pre: dict[str, dict], edges_out: list[dict]) -> int:\n',
         'def _unir_comunicaciones_c1(grafos: dict[str, dict], codigo_comunicacion) -> tuple[dict, list]:\n'
         '    """C1: en cada código normalizado que aparece en más de un TO, renombra sus Comunicacion al id de la primera (en el orden\n'
         '    de C.TOS_ORDEN) y re-apunta sus aristas; dentro de ese código, también se unen las variantes de un mismo TO. Un código de\n'
         '    un solo TO, o una Comunicacion sin código normalizado (None), no se toca."""\n'
         '    grupos: dict[str, dict] = {}\n'
         '    for to in C.TOS_ORDEN:\n'
         '        for n in grafos[to]["nodes"]:\n'
         '            if n.get("type") == "Comunicacion":\n'
         '                c = codigo_comunicacion(n)\n'
         '                if c is not None:\n'
         '                    g = grupos.setdefault(c, {"id": n["id"], "codigo_normalizado": c, "nodos": []})\n'
         '                    g["nodos"].append({"to": to, "id_antes": n["id"], "codigo": (n.get("properties") or {}).get("codigo"),\n'
         '                                       "label": n.get("label")})\n'
         '    uniones = [g for g in grupos.values() if len({x["to"] for x in g["nodos"]}) > 1]\n'
         '    canon = {x["id_antes"]: g["id"] for g in uniones for x in g["nodos"] if x["id_antes"] != g["id"]}\n'
         '    salida: dict[str, dict] = {}\n'
         '    for to in C.TOS_ORDEN:\n'
         '        g = deepcopy(grafos[to])\n'
         '        ids_c1 = {n["id"] for n in g["nodes"] if n.get("type") == "Comunicacion" and n["id"] in canon}\n'
         '        for n in g["nodes"]:\n'
         '            if n["id"] in ids_c1:\n'
         '                n["id"] = canon[n["id"]]\n'
         '        for e in g["edges"]:\n'
         '            if e["source"] in ids_c1:\n'
         '                e["source"] = canon[e["source"]]\n'
         '            if e["target"] in ids_c1:\n'
         '                e["target"] = canon[e["target"]]\n'
         '        salida[to] = g\n'
         '    return salida, uniones\n\n\n'
         'def merges_arista_de(grafos_pre: dict[str, dict], edges_out: list[dict]) -> int:\n'),
    ],
}

sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731
manifiesto = []
for rel, ps in PARCHES.items():
    src = (CL / rel).read_text(encoding="utf-8")
    nuevo = src
    for viejo, nuevo_txt in ps:
        n = nuevo.count(viejo)
        if n != 1:
            raise SystemExit(f"FRENO: en {rel} el fragmento aparece {n} veces (tiene que ser 1): {viejo[:80]!r}")
        nuevo = nuevo.replace(viejo, nuevo_txt)
    nombre = Path(rel).name
    (OUT / f"{Path(rel).stem}_con_reglas_candidatas.py").write_text(nuevo, encoding="utf-8")
    d = "".join(difflib.unified_diff(src.splitlines(True), nuevo.splitlines(True), fromfile=f"a/{rel}", tofile=f"b/{rel}"))
    (OUT / f"parche_{Path(rel).stem}.diff").write_text(d, encoding="utf-8")
    mas = sum(1 for l in d.splitlines() if l.startswith("+") and not l.startswith("+++"))
    menos = sum(1 for l in d.splitlines() if l.startswith("-") and not l.startswith("---"))
    manifiesto.append(f"{rel}  HEAD {sha(src.encode())}  parchado {sha(nuevo.encode())}  +{mas} -{menos}")
    print(manifiesto[-1])
(OUT / "base_y_parchados_sha256.txt").write_text("\n".join(manifiesto) + "\n", encoding="utf-8")
print("LISTO")
