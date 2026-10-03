"""
lado_a_lado.py — U-PROMPT-R2, P1 (USD 0): sección «lado a lado» del documento
de diseño, generada desde los reemplazos del borrador (sin transcribir a mano).

Uso (desde la raíz del repo, después de reproducir_p1.py):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p1/lado_a_lado.py
Escribe data/experiment/prompt_r2/p1/salida/lado_a_lado.md.
"""
from __future__ import annotations

import json
from pathlib import Path

SAL = Path(__file__).resolve().parent / "salida"
SECC = {"R0": "Encabezado", "R1": "TIPOS · 1 Comunicacion", "R2": "TIPOS · 2 TextoOrdenado",
        "R3": "TIPOS · 3 Operacion", "R4": "TIPOS · 4 Restriccion", "R5": "TIPOS · 5 Excepcion",
        "R6": "TIPOS · 6 Obligacion", "R7": "TIPOS · 8 Condicion (definición)",
        "R8": "TIPOS · 8 Condicion (destino de condicion_de)", "R9": "TIPOS · 8 Condicion (properties)",
        "R10": "TIPOS · 9 Definicion", "R11": "Secciones nuevas COPIA LITERAL y UMBRALES (antes de PREDICADOS)",
        "R12": "PREDICADOS · aplica_a", "R13": "PREDICADOS · ejecuta",
        "R14": "PREDICADOS · condicion_de y remisiones", "R15": "SUJETOS", "R16": "REGLAS · 1",
        "R17": "REGLAS · 4", "R18": "REGLAS · 7", "R19": "REGLAS · 9 (título)", "R20": "REGLAS · 9 (cierre)",
        "R21": "CONTENIDO NO-PROSA", "R22": "EJEMPLOS NEGATIVOS · predicados",
        "R23": "EJEMPLOS NEGATIVOS · aplica_a", "R24": "EJEMPLOS NEGATIVOS · sujetos y polaridad",
        "R25": "REGLA regula / prohibe / limita", "R26": "OMISIONES (nueva) y FORMATO DE SALIDA",
        "R27": "Bloque de catálogo (de «## Sujetos regulados» a «## Roles de alcance por TO»)",
        "R28": "Encabezado · chunk de punto", "R29": "PROVENANCE · el contexto ancla, la unidad extrae",
        "R30": "COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA (sección nueva, antes de REGLAS)"}


def main() -> None:
    A = json.loads((SAL / "reemplazos_r2_borrador_A.json").read_text(encoding="utf-8"))
    B = {x["id"]: x for x in json.loads((SAL / "reemplazos_r2_borrador_B.json").read_text(encoding="utf-8"))}
    out = []
    for ra in A:
        rid = ra["id"]
        if rid != "R6" and B[rid] != ra:
            raise SystemExit(f"{rid}: las variantes A y B difieren fuera de R6")
        out.append(f"### {rid} · {SECC[rid]}\n\nManda: {ra['decision']}.\n")
        if rid == "R27":
            out.append(f"- Sellado: {ra['viejo']}.\n- Nuevo: {ra['nuevo']}, el archivo generado por U-CAT-UNICO desde "
                       f"`catalogo_sujetos_r2.json` (`data/experiment/catalogo_unico/generados_r2/bloque_catalogo_r2.txt`, "
                       f"el sha256 de su `manifest_generados_r2.json`), tal cual.\n")
            continue
        out.append("Sellado:\n\n```text\n" + ra["viejo"].strip("\n") + "\n```\n")
        if rid == "R6":
            out.append("Nuevo, variante A (regla actual):\n\n```text\n" + ra["nuevo"].strip("\n") + "\n```\n")
            out.append("Nuevo, variante B (plazos sin cuantía temporal fuera de `frecuencia`):\n\n```text\n"
                       + B["R6"]["nuevo"].strip("\n") + "\n```\n")
        else:
            out.append("Nuevo:\n\n```text\n" + ra["nuevo"].strip("\n") + "\n```\n")
    (SAL / "lado_a_lado.md").write_text("\n".join(out), encoding="utf-8")
    print(f"{len(A)} reemplazos")


if __name__ == "__main__":
    main()
