"""
comun_v.py — U-TRIP-V (etapa V de la evaluación por tripletas): constantes y funciones comunes de los scripts de la
preparación. Pre-registro FIRMADO (docs/preregistro_evaluacion_tripletas.md, firma en 4afbe51), con sus notas al pie y
sus enmiendas 1 (umbrales) y 2 (desambiguación, firmada en 593e5db2). Solo biblioteca estándar; no importa código del
repo (las constantes del esquema se leen con `ast` desde el fuente, sin ejecutarlo). USD 0, sin API.

Rutas: la COPIA del repo (rsync de la cláusula, en el scratchpad) se pasa con --copia; nada se lee del repo vivo salvo
git para los controles de blobs y de HEAD (00_control_insumos.py).
"""
from __future__ import annotations

import ast
import hashlib
import json
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent                 # tripletas_v/scripts
RAIZ = AQUI.parent                                     # tripletas_v
SALIDAS = RAIZ / "salidas"
FICHAS = RAIZ / "fichas"
LECTURA = RAIZ / "lectura"
INSUMO_DESAMB = RAIZ / "insumos" / "items_U-MED-DESAMB_para_el_solapamiento.json"
INSUMO_DESAMB_SHA256 = "57eca4e3ae9b028d478b37dd71244fe7817ec3d105dbf4c58937723b5b70f8c1"

# El grafo de V: el sello vigente al sortear (nota del 15/10/2026 al pie del pre-registro; grafos.py:216-223).
KG_REL = "data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2b_sincola_rs1/r2/kg.json"
KG_SHA256 = "66e745f57397ab754cde09eb641e9f0d9ef6259ea7e6445d086ecbf1c36dcc6c"
KG_NOMBRE = "KG-Tanda0-Desarrollo-r2b-sincola-rs1"
KG_N_NODOS, KG_N_ARISTAS = 6711, 21996
# El grafo que cita el texto firmado (§2 y §3.1), sellado y reemplazado por el re-sellado único: solo para declarar
# la diferencia de la población (3.983 en el texto firmado).
KG_PREVIO_REL = "data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2b_sincola/r2/kg.json"
KG_PREVIO_SHA256 = "2922b72dca2c2bcb204a04f53fc89f265ac2c57e83e6aaab2ce1af8b82d413e4"
DIFF_RESELLADO_REL = ("data/experiment/resellado_t0/salidas/diff_contra_sellado/"
                      "diff_declarado_contra_sellado_r2b_sincola_desarrollo.json")
E0_REL = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b"
PDF_DIR_REL = "data/experiment/subset"
SELLOS_L0_REL = "data/experiment/lectura_aceptadas/sellos_l0.json"
MODELOS_R2_REL = "data/experiment/pyd_r2/code/modelos_r2.py"
SCHEMA_REL = "data/experiment/grafo_v2/code/schema.py"
E5_REL = "data/experiment/reextraccion_v2/corpus_v2/r1_e5_esqueleto.py"
REF_REL = "data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py"
ENS_REL = "data/experiment/tanda0/code/ensamblar_tanda0.py"
E2_REL = "data/experiment/reextraccion_v2/e2_reduce/e2_lib.py"
CADENA_REL = "data/experiment/resellado_t0/scripts/cadena_rs1.sh"
MANIFIESTO_REL = "data/experiment/reextraccion_v2/manifiestos/tanda0_ens_desarrollo_r2b_sincola_rs1.json"

TOS_V = ("cap", "cla", "ext", "pro", "ric")

# §3.1: las diez relaciones de contenido del esquema, con aplica_a, y la lista de fuera del texto firmado.
CONTENIDO = ("aplica_a", "condicion_de", "limita", "regula", "requiere", "condiciona", "exceptua_obligacion",
             "exceptua", "prohibe", "ejecuta")
FUERA_PREREGISTRO = ("remite_a", "establecida_en", "subclase_de", "miembro_de", "instancia_de", "parte_de",
                     "modificada_por", "padre_sugerido", "referencia")
POBLACION_PREREGISTRO = {"aplica_a": 1770, "condicion_de": 1379, "limita": 267, "regula": 169, "requiere": 117,
                         "condiciona": 85, "exceptua_obligacion": 69, "exceptua": 62, "prohibe": 54, "ejecuta": 11}
PREDICADOS_SUJETO = ("aplica_a", "ejecuta")        # aplica_a: Sujeto en el destino; ejecuta: Sujeto en la fuente

# §3.2 y despacho: semilla, tamaños y método.
SEMILLA = "B4-TRIPLETAS-V:sorteo:2026-10-07"
N_MUESTRA, N_POOL, MINIMO, UMBRAL_ESTRATO = 100, 20, 3, 30
ESTRATO_OTROS = "otros"
N_PILOTO, N_LOTES, TAM_LOTE = 10, 9, 10

# §3.3 y despacho: lo que la ficha NO trae (marcas del pipeline). Todo lo demás del nodo y de la arista va.
PROPS_NODO_FUERA = ("cuarentena", "padre_sugerido", "padre_por_defecto", "cola_humana", "cola_chunks", "estado_e3")
NO_DEFINIDAS_FUERA = ("copia_nota_e3", "modalidad_clasificada", "umbral_no_cuantificable",
                      "umbral_no_cuantificable_motivo", "umbral_no_cuantificable_detector_sha256",
                      "umbral_no_cuantificable_tablas_forzadas_sha256")
CAMPOS_NODO_FUERA = ("originales", "fuera_de_lista", "rol_fuente", "campos_heredados_v3", "valores_no_tipados")
UMBRAL_CAMPOS = ("valor", "unidad", "moneda", "comparacion", "dias_tipo", "base", "base_destino", "tramo")
UMBRAL_FUERA = ("regla_comparacion", "origen", "tramo_verificado", "verificado_en_tabla", "base_no_resuelta",
                "base_via", "originales")
ARISTA_FUERA = ("mencion_verificada", "metodo_resolucion", "sujeto_id_modelo", "sujeto_mencion_modelo",
                "coherencia_tipo_predicado", "no_verificada_e3", "rol_fuente", "cola_humana", "cola_chunks",
                "estado_e3")
# Claves que no pueden aparecer en ninguna ficha (control negativo).
CLAVES_PROHIBIDAS = ("estado_e3", "n_reintentos", "reintentos", "cola_humana", "cola_chunks", "copia_nota_e3",
                     "metodo_resolucion", "sujeto_id_modelo", "coherencia_tipo_predicado", "no_verificada_e3",
                     "regla_comparacion", "modalidad_clasificada", "cuarentena", "padre_sugerido",
                     "padre_por_defecto", "originales", "fuera_de_lista", "rol_fuente", "umbral_no_cuantificable",
                     "estrato", "solapamiento", "juicio", "veredicto", "propuesta")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha_archivo(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def canon(x) -> bytes:
    """La forma canónica de los sha256 de listas (el patrón de l0_sellos.py)."""
    return json.dumps(x, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def hora() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def clave(e: dict) -> str:
    return f"{e['source']}|{e['relation']}|{e['target']}"


def constantes_py(path: Path, nombres: tuple[str, ...]) -> dict:
    """Asignaciones de módulo con valor literal, leídas con ast (sin ejecutar el módulo)."""
    arbol = ast.parse(path.read_text(encoding="utf-8"))
    out = {}
    for nodo in arbol.body:
        if isinstance(nodo, ast.Assign) and len(nodo.targets) == 1 and isinstance(nodo.targets[0], ast.Name):
            n = nodo.targets[0].id
            if n in nombres:
                try:
                    out[n] = ast.literal_eval(nodo.value)
                except ValueError:
                    out[n] = None
    return out


def cargar_kg(copia: Path) -> tuple[dict, str]:
    p = copia / KG_REL
    s = sha_archivo(p)
    if s != KG_SHA256:
        raise SystemExit(f"ABORTO: kg.json con sha256 {s}, no {KG_SHA256}")
    kg = json.loads(p.read_text(encoding="utf-8"))
    if len(kg["nodes"]) != KG_N_NODOS or len(kg["edges"]) != KG_N_ARISTAS:
        raise SystemExit(f"ABORTO: {len(kg['nodes'])} nodos y {len(kg['edges'])} aristas, no los sellados")
    return kg, s


def chunks_e0(copia: Path, to: str) -> dict:
    d = json.loads((copia / E0_REL / f"chunks_{to}.json").read_text(encoding="utf-8"))
    return {c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)}


def base_chunk(cid: str) -> str:
    """Una parte de una partición por corte (`<id>::parteN`) usa el chunk de su unidad (patrón de l1_fichas.py)."""
    return cid.split("::parte")[0]


def escribir_json(p: Path, obj) -> str:
    p.parent.mkdir(parents=True, exist_ok=True)
    texto = json.dumps(obj, ensure_ascii=False, indent=1) + "\n"
    p.write_text(texto, encoding="utf-8")
    return sha(texto.encode("utf-8"))
