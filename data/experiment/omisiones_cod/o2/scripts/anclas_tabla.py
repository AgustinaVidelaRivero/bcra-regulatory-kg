"""Anclas de la tabla de reprocesamiento: la línea de cada texto que nombran, en HEAD y en el código de O2 (por el texto,
no por el número). Uso: python3 anclas_tabla.py <raíz con el código de HEAD> <raíz con el código de O2>"""
import sys
from pathlib import Path
H, N = Path(sys.argv[1]), Path(sys.argv[2])
V = "data/experiment/pyd_r2/code/validador_r2.py"; E = "data/experiment/reextraccion_v2/corpus_v2/r1_e4.py"
RF = "data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py"; T = "data/experiment/tanda0/code/ensamblar_tanda0.py"
ANCLAS = [  # (fila, archivo, texto del inicio, texto del fin o None)
    ("F14b", V, "def validar(tool_input: Any, chunk: dict, politica", None),
    ("F14b", V, 'vistos_ent = None if vistos_e3 is None else set(vistos_e3["entidades"])', 'vistos_rel = None if vistos_e3 is None else set(vistos_e3["relaciones"])'),
    ("F14b", V, "if vistos_ent is not None and i not in vistos_ent:", 'res["no_vistos_e3"].append({"elemento": ref, "local_id": local_id, "type": tipo})'),
    ("F14b", V, "if vistos_rel is not None and i not in vistos_rel:", 'res["no_vistos_e3"].append({"elemento": ref, "predicate": pred'),
    ("F14b", E, "POLITICA_R2_SHA256 = ", None),
    ("F15", T, "def correr_cadena_r2(man: MC.Manifiesto", 'return {"kg": kg, "kg_json": kg_json, "sha256": C.sha256_bytes'),
    ("F15b", T, "def llenar_umbrales_r2(kg: dict", None),
    ("F15b", T, "r_umb = llenar_umbrales_r2(kg, tramos_e1", None),
    ("F15c", RF, "def detectar_menciones_r2(texto: str", None),
    ("F15c", RF, "def detectar_y_resolver_r2(kg: dict", None),
    ("F15c", T, 'r_ref = REF.detectar_y_resolver(kg, perfil="r2"', None),
    ("F15d", E, "EXPRESIONES_COLECTIVAS_R3 = (", None),
    ("F15d", E, "MOTIVOS_PARTE_A = (", None),
    ("F15d", E, 'sin_alcance = parte_a and reg["archivo"] not in rol_por_archivo', 'mencion, nivel = r.get("sujeto_mencion"), r.get("mencion_verificada")'),
    ("F15d", T, "def normalizar_propuestos_r2b(kg: dict", None),
    ("F15d", T, "filas_sin_alcance: dict[str, list[dict]] = {}", 'res["padre_por_defecto_generico"].append({**fila, "sugerencias": sugeridas'),
    ("F15d", T, 'res = E4.resolver_relaciones_r2(regs, cat["indice"]', None),
    ("F16", T, "r_to = E4.canonizar_texto_ordenado(kg)", None, "def correr_cadena_r2(man"),
    ("F16", T, "r_esq = inyectar_esqueleto_v3(kg, catalogo)", None, "def correr_cadena_r2(man"),
    ("F16", T, "def derivar_establecida_en(kg: dict", None),
    ("F16", T, 'resumen["establecida_en_derivada"] = derivar_establecida_en(kg, canon)', None),
    ("F16b", T, "def version_y_materia_r2b(kg: dict", None),
]
def linea(raiz, f, txt, desde=1):
    ls = (raiz / f).read_text(encoding="utf-8").splitlines()
    hits = [i for i, l in enumerate(ls, 1) if i >= desde and txt in l]
    return hits[0] if hits else None
for fila, f, a, b, *ctx in ANCLAS:
    dh = linea(H, f, ctx[0]) if ctx else 1
    dn = linea(N, f, ctx[0]) if ctx else 1
    ha, na = linea(H, f, a, dh), linea(N, f, a, dn)
    hb = linea(H, f, b, ha) if b else None
    nb = linea(N, f, b, na) if b else None
    h = f"{ha}" + (f"-{hb}" if b else ""); n = f"{na}" + (f"-{nb}" if b else "")
    print(f"{fila}\t{Path(f).name}\t{h}\t{n}\t{'igual' if h == n else 'CAMBIA'}")
