"""
construir_dopadas_p1bis.py — Construcción de las 10 UNIDADES DOPADAS del
control rediseñado (adenda P1′, `data/experiment/esq/adenda_prerregistro_esq1_P1bis.md`
§3, brazo A′; mandato U-ESQ-1d.b). USD 0, sin API.

Qué es una unidad dopada: una unidad REAL del conjunto de desarrollo (los 5
TOs del corpus de producción) a cuyo texto se le añade exactamente UNA
cláusula normativa plausible, EN PROSA, cuyo contenido está fuera del esquema
v2 a sabiendas — 5 exigen un tipo de entidad nuevo, 5 una relación con
predicado nuevo. Las dopadas son material de INSTRUMENTO: no entran a ningún
conteo de ESQ-1, ni al corpus, ni a ningún archivo de exclusión (adenda §3.c);
sus chunk_ids llevan el prefijo reservado "dop::" para que ninguna herramienta
las confunda con unidades reales.

Selección de las 10 unidades base (determinística, declarada acá):
  - Pool: unidades LIMPIAS del universo de producción (comun_control_esq.es_limpia:
    sin error, sin rechazos, sin omisiones, sin sujeto_propuesto crudo, con
    sustancia), que ADEMÁS (i) no estén entre las 40 del control original
    (disyunción con A, B y C — las C se re-corren limpias en esta misma
    corrida), (ii) no sean mini-chunks (una cláusula plantada al final de un
    chapeau leería antinatural; los puntos tienen cuerpo normativo), y
    (iii) no estén flaggeadas por E0 (la cláusula debe ser el ÚNICO contenido
    fuera de esquema y la regla NO-PROSA no debe intervenir — causa raíz del
    brazo A original, diagnóstico §a).
  - Estratificación: 2 por TO (5 TOs × 2 = 10). Semilla 20260827 (la sellada),
    un único Random consumido en orden cap → cla → ext → pro → ric, pools
    ordenados por chunk_id; de cada par muestreado, la PRIMERA unidad recibe
    la cláusula de TIPO y la SEGUNDA la de PREDICADO.

Las cláusulas plantadas viven SOLO acá y en los artefactos de control/ que
este script escribe. Regla de no-siembra (adenda §3.b): ni las cláusulas ni
los conceptos esperados aparecen en el system, en la description del tool ni
en ningún ejemplo del prompt — solo en el texto de la propia unidad dopada
(que es exactamente lo que el control mide: si el modelo, al leerlas, dispara
el canal). El selftest de U-ESQ-1d.c lo verifica mecánicamente.

Salidas (data/experiment/esq/control/):
  - dopadas_p1bis.json        fixtures: chunk dopado completo + metadatos
  - manifiesto_dopadas_p1bis.md   manifiesto para la aprobación de la autora
                                  (freno del mandato U-ESQ-1d.b)

Uso:  .venv/bin/python3 -B data/experiment/esq/code/construir_dopadas_p1bis.py
"""

from __future__ import annotations

import copy
import json
import random
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_control_esq as cc             # noqa: E402
import runner_control_esq as rc            # noqa: E402
import comun_e1                            # noqa: E402

FIXTURES = cc.CONTROL_DIR / "dopadas_p1bis.json"
MANIFIESTO = cc.CONTROL_DIR / "manifiesto_dopadas_p1bis.md"
PREFIJO_DOP = "dop::"

# --------------------------------------------------------------------------- #
# Las 10 cláusulas plantadas — fuente única.                                   #
# Clave: chunk_id base. mitad: "tipo" | "predicado". La cláusula se appendea   #
# al texto de la unidad como párrafo final. "espera" declara el CANAL cuyo     #
# disparo cuenta para la mitad (P1′ no exige ningún valor de cadena            #
# particular: exige que el canal correcto dispare).                            #
# --------------------------------------------------------------------------- #
CLAUSULAS: dict[str, dict] = {
    # ------------------------------- TIPO --------------------------------- #
    "cap::8.3.2.4": {
        "mitad": "tipo",
        "clausula": (
            "El incumplimiento de las condiciones establecidas en este punto "
            "dará lugar a la aplicación de una sanción de multa equivalente "
            "al 0,5 % del valor computable del instrumento, conforme al "
            "régimen sancionatorio previsto en la Ley de Entidades "
            "Financieras."),
        "concepto": "sanción pecuniaria (multa por incumplimiento)",
        "por_que_fuera": (
            "una sanción es la consecuencia jurídica de un incumplimiento: "
            "no es prohibición ni límite (Restriccion), no es deber positivo "
            "(Obligacion), no suspende ninguna norma (Excepcion) y no es un "
            "acto regulado del sujeto (Operacion)."),
        "espera": "tipo_propuesto",
    },
    "cla::6.5.2.1": {
        "mitad": "tipo",
        "clausula": (
            "Se presumirá, sin admitir prueba en contrario, que el cliente "
            "mantiene la capacidad de pago descripta en este punto cuando la "
            "totalidad de sus obligaciones registre atrasos inferiores a 30 "
            "días."),
        "concepto": "presunción legal (iuris et de iure)",
        "por_que_fuera": (
            "una presunción fija un hecho tenido por cierto: no impone deber "
            "(Obligacion), no prohíbe ni limita (Restriccion), no exceptúa "
            "norma alguna (Excepcion) ni describe un acto regulado "
            "(Operacion)."),
        "espera": "tipo_propuesto",
    },
    "ext::3.17.3.5": {
        # Reemplazo aprobado en el freno (b): la versión original definía una
        # categoría de PERSONA («beneficiario computable») y el modelo tiene
        # canal preexistente para eso (sujeto_propuesto) — un disparo por el
        # canal vecino contaría como fallo sin que el canal de tipos esté
        # muerto. La cláusula vigente define un VALOR: sin canal vecino.
        "mitad": "tipo",
        "clausula": (
            "A los efectos de este punto, se entiende por \"valor de "
            "referencia ajustado\" el promedio simple de los tipos de cambio "
            "de cierre de los últimos cinco días hábiles, incrementado en el "
            "porcentaje que establezca la reglamentación."),
        "concepto": "término definido (definición normativa de un valor)",
        "por_que_fuera": (
            "una definición fija el sentido de un término: no manda, no "
            "prohíbe, no exceptúa ni es un acto; define un valor, no un "
            "sujeto ni una operación, así que tampoco tiene canal vecino "
            "posible (sujeto_propuesto no aplica)."),
        "espera": "tipo_propuesto",
    },
    "pro::1.1.1": {
        "mitad": "tipo",
        "clausula": (
            "Las previsiones del presente punto entrarán en vigencia a los "
            "ciento ochenta días corridos de su difusión, rigiendo hasta esa "
            "fecha el alcance establecido en la reglamentación que se "
            "reemplaza."),
        "concepto": "cláusula de vigencia diferida (disposición transitoria)",
        "por_que_fuera": (
            "una regla de vigencia predica sobre la norma misma (cuándo "
            "rige), no sobre la conducta de un sujeto: no encaja en deber, "
            "prohibición, excepción ni acto regulado."),
        "espera": "tipo_propuesto",
    },
    "ric::8.1.2": {
        "mitad": "tipo",
        "clausula": (
            "La Superintendencia de Entidades Financieras y Cambiarias queda "
            "facultada para adecuar el porcentaje indicado precedentemente "
            "cuando la evolución de las condiciones de mercado lo "
            "justifique."),
        "concepto": "facultad discrecional de la autoridad (permiso, no deber)",
        "por_que_fuera": (
            "una facultad («queda facultada», «podrá») es deónticamente "
            "distinta del deber y de la prohibición; el esquema no tiene "
            "categoría para permisos/potestades."),
        "espera": "tipo_propuesto",
    },
    # ----------------------------- PREDICADO ------------------------------ #
    "cap::2.5.5": {
        "mitad": "predicado",
        "clausula": (
            "A los fines de esta sección, las operaciones de pase pasivo en "
            "pesos mencionadas precedentemente se considerarán equivalentes "
            "a las tenencias de títulos públicos que les dieron origen."),
        "concepto": "equivalencia entre dos operaciones (Operacion→Operacion)",
        "por_que_fuera": (
            "ningún predicado de la lista de 12 conecta Operacion con "
            "Operacion; «se considerarán equivalentes» tampoco es "
            "re-expresable invirtiendo dirección ni re-tipando sin perder el "
            "contenido."),
        "espera": "predicado_propuesto",
    },
    "cla::6.5.3.3": {
        "mitad": "predicado",
        "clausula": (
            "La revisión de la clasificación motivada por este indicador "
            "complementará a la recalificación periódica prevista en esta "
            "sección, sin sustituirla."),
        "concepto": "complementariedad entre dos deberes/actos de clasificación",
        "por_que_fuera": (
            "«complementa» entre dos revisiones/recalificaciones (ambas "
            "tipables como Obligacion u Operacion) no matchea ningún "
            "predicado ni ninguna firma dominio/rango de la matriz."),
        "espera": "predicado_propuesto",
    },
    "ext::6.5.2": {
        "mitad": "predicado",
        "clausula": (
            "A los efectos de esta reglamentación, las operaciones de cambio "
            "concertadas por dichas sucursales quedan asimiladas a las "
            "operaciones concertadas por su casa matriz."),
        "concepto": "asimilación entre dos operaciones (Operacion→Operacion)",
        "por_que_fuera": (
            "misma familia que la equivalencia: no existe predicado "
            "Operacion→Operacion y «quedan asimiladas a» no es prohibición, "
            "límite, excepción ni condición."),
        "espera": "predicado_propuesto",
    },
    "pro::3.2.3.6": {
        "mitad": "predicado",
        "clausula": (
            "La conservación de la documentación indicada en este punto "
            "acreditará el cumplimiento de la obligación de designación "
            "prevista en el punto 3.1.1."),
        "concepto": "acreditación de cumplimiento (deber→deber)",
        "por_que_fuera": (
            "«acredita el cumplimiento de» conecta dos deberes; no es "
            "requiere (Operacion→Obligacion), no es condiciona "
            "(Obligacion→Operacion), no exceptúa nada."),
        "espera": "predicado_propuesto",
    },
    "ric::10.1.1": {
        "mitad": "predicado",
        "clausula": (
            "El requerimiento previsto en el presente punto se computará "
            "conjuntamente con el previsto para el régimen informativo de "
            "Supervisión a los fines del control de cumplimiento."),
        "concepto": "cómputo conjunto entre dos requerimientos informativos",
        "por_que_fuera": (
            "«se computa conjuntamente con» entre dos requerimientos "
            "(Obligacion→Obligacion) no tiene predicado en la lista ni firma "
            "válida en la matriz dominio/rango."),
        "espera": "predicado_propuesto",
    },
}


def seleccionar_bases() -> dict[str, list[str]]:
    """Los 10 chunk_ids base, 2 por TO, con la regla declarada en la
    docstring del módulo. Determinístico: semilla sellada 20260827."""
    universo = cc.cargar_universo()
    sel_orig = {s["chunk_id"] for s in cc.seleccionar(universo)}
    por_id = rc.chunks_por_id()
    po = cc.pools(universo)

    elegibles = {}
    for to in cc.TOS:
        elegibles[to] = sorted(
            cid for cid in po["C"][to]
            if cid not in sel_orig
            and cid in por_id
            and por_id[cid].get("tipo") != "mini_chunk"
            and not comun_e1.chunk_flaggeado(por_id[cid]))

    rng = random.Random(cc.SEMILLA)
    return {to: rng.sample(elegibles[to], 2) for to in cc.TOS}


def construir() -> list[dict]:
    """Fixtures de las 10 dopadas: chunk completo listo para el runner +
    metadatos del manifiesto. El chunk dopado es el base con (i) id con
    prefijo reservado dop::<mitad>::<base_id> y (ii) texto = texto base +
    salto de línea + cláusula plantada. NADA MÁS cambia."""
    bases = seleccionar_bases()
    por_id = rc.chunks_por_id()

    esperado_por_to = {to: {"tipo": par[0], "predicado": par[1]}
                       for to, par in bases.items()}
    declarados = {cid: d["mitad"] for cid, d in CLAUSULAS.items()}
    for to, m in esperado_por_to.items():
        for mitad, cid in m.items():
            if declarados.get(cid) != mitad:
                raise RuntimeError(
                    f"selección y cláusulas desalineadas: {cid} debería ser "
                    f"mitad={mitad} y CLAUSULAS declara {declarados.get(cid)}")

    fixtures = []
    for to in cc.TOS:
        for mitad in ("tipo", "predicado"):
            base_id = esperado_por_to[to][mitad]
            d = CLAUSULAS[base_id]
            base = por_id[base_id]
            dopado = copy.deepcopy(base)
            dopado["id"] = f"{PREFIJO_DOP}{mitad}::{base_id}"
            dopado["texto"] = base["texto"].rstrip() + "\n" + d["clausula"]
            fixtures.append({
                "chunk_id_dopado": dopado["id"],
                "chunk_id_base": base_id,
                "to": to,
                "mitad": mitad,
                "espera": d["espera"],
                "concepto": d["concepto"],
                "por_que_fuera": d["por_que_fuera"],
                "clausula_plantada": d["clausula"],
                "chunk": dopado,
            })
    return fixtures


def render_manifiesto(fixtures: list[dict]) -> str:
    filas = []
    for fx in fixtures:
        filas += [
            f"### {fx['chunk_id_dopado']}",
            "",
            f"- **Unidad base:** `{fx['chunk_id_base']}` "
            f"({fx['chunk']['titulo'][:70]})",
            f"- **Mitad / canal esperado:** {fx['mitad']} → `{fx['espera']}`",
            f"- **Concepto plantado:** {fx['concepto']}",
            f"- **Por qué está fuera del esquema:** {fx['por_que_fuera']}",
            "- **Cláusula plantada (verbatim, se appendea como párrafo final "
            "del texto de la unidad):**",
            "",
            f"  > {fx['clausula_plantada']}",
            "",
        ]
    return "\n".join([
        "# Manifiesto de unidades dopadas — control rediseñado P1′ (U-ESQ-1d.b)",
        "",
        "**Estado: PENDIENTE DE APROBACIÓN de la autora. Ninguna corrida se",
        "paga sin esa aprobación (freno del mandato U-ESQ-1d.b; adenda P1′",
        "§3.a).**",
        "",
        "10 unidades dopadas = unidad real limpia del conjunto de desarrollo",
        "+ exactamente UNA cláusula plantada en prosa (5 de tipo nuevo, 5 de",
        "predicado nuevo). Selección de bases determinística (semilla sellada",
        "20260827; regla completa en `code/construir_dopadas_p1bis.py`).",
        "Umbral P1′: A′ ≥7/10 en total Y ≥3/5 en cada mitad — cuenta el",
        "disparo del canal esperado de cada mitad, no ningún valor de cadena",
        "particular. Las cadenas plantadas y los conceptos NO aparecen en",
        "ningún prompt ni ejemplo (no sembrar): solo en el texto de la propia",
        "unidad dopada.",
        "",
        "Alcance declarado (adenda §3): este control prueba capacidad de",
        "disparo sobre contenido claro y plantado; no mide sensibilidad sobre",
        "contenido real sutil. Las dopadas son material de instrumento: no",
        "entran a ningún conteo de ESQ-1.",
        "",
        "## Mitad TIPO (5) y mitad PREDICADO (5)",
        "",
        *filas,
    ])


def main() -> int:
    fixtures = construir()
    cc.CONTROL_DIR.mkdir(parents=True, exist_ok=True)
    doc = {
        "unidad": "U-ESQ-1d",
        "adenda": "data/experiment/esq/adenda_prerregistro_esq1_P1bis.md",
        "semilla": cc.SEMILLA,
        "regla_seleccion": ("pool C limpio ∖ 40 del control original, sin "
                            "mini-chunks, sin flags E0; 2 por TO, "
                            "Random(20260827) en orden cap→cla→ext→pro→ric; "
                            "1ª del par → tipo, 2ª → predicado"),
        "prefijo_ids": PREFIJO_DOP,
        "aprobado_por_autora": False,
        "dopadas": fixtures,
    }
    FIXTURES.write_text(json.dumps(doc, ensure_ascii=False, indent=1),
                        encoding="utf-8")
    MANIFIESTO.write_text(render_manifiesto(fixtures), encoding="utf-8")
    print(f"fixtures  -> {FIXTURES}")
    print(f"manifiesto -> {MANIFIESTO}")
    for fx in fixtures:
        print(f"  [{fx['mitad']:9s}] {fx['chunk_id_dopado']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
