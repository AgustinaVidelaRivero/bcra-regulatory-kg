"""
borrador_parche_p3b.py — U-PROMPT-R2, P3b-1 (USD 0, sin API): borrador del parche del prefijo r2b congelado
(`14d6b63b508e`), puntos a a f de la etapa P3b (nota del 04/10/2026 al pie del mandato, `4f3bcff`).

El parche son reemplazos con ancla única sobre el texto congelado (`prompt_r2b.PREFIJO_SISTEMA_R2B`), como el
borrador de P1 sobre el sellado v3. Cada reemplazo lleva el punto de la etapa y el hallazgo de la revisión
independiente que lo motiva (reports/u_revision_libre/, `54f57cd`). No congela nada: P3b-2 congela tras la
aprobación del texto.

Escribe en --salida:
  - prefijo_r2b_parche_borrador.txt: el prefijo con el parche;
  - reemplazos_p3b_borrador.json: los reemplazos (viejo, nuevo, punto, hallazgo);
  - lado_a_lado_p3b.md: cada tramo, congelado y nuevo;
  - hashes_p3b.json: sha256 y largo del texto, y el hash canónico (system + tools) con el tool schema vigente.

Uso (desde la raíz de una copia del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3b/borrador_parche_p3b.py --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

P3B = Path(__file__).resolve().parent
REPO = P3B.parents[3]
sys.path.insert(0, str(REPO / "data" / "experiment" / "reextraccion_v2" / "e1_extractor"))
import prompt_r2b as P  # noqa: E402

REEMPLAZOS = [
    # ---------------- a. Recomendación (hallazgo 1.3) ----------------
    {"id": "P3B-a1", "punto": "a", "hallazgo": "1.3",
     "viejo": "`otra` es el residuo: usalo cuando el deber no cae en ninguno de los anteriores, no como caja por "
              "defecto.",
     "nuevo": "`otra` es el residuo: usalo cuando el deber no cae en ninguno de los anteriores, no como caja por "
              "defecto.\n"
              "   RECOMENDACIÓN: si el texto no manda una conducta sino que la aconseja (la califica de deseable, de "
              "conveniente o de práctica que se espera), extraela igual como Obligacion y marcala de dos maneras: "
              "copiá en `otras_propiedades`, clave `modalidad`, el tramo literal que la califica, tal cual; y decí en "
              "la descripción que es una recomendación y no un deber. El código clasifica la modalidad desde ese "
              "tramo. Si la calificación está en el encabezado de una lista, cada ítem compuesto lleva las dos "
              "marcas."},
    {"id": "P3B-a2", "punto": "a", "hallazgo": "1.3",
     "viejo": "su modalidad (deber, prohibición o facultad)",
     "nuevo": "su modalidad (deber, prohibición, facultad o recomendación: ver Obligacion)"},
    # ---------------- b. Consecuencia de un incumplimiento (hallazgo 1.4) ----------------
    {"id": "P3B-b1", "punto": "b", "hallazgo": "1.4",
     "viejo": "   Properties: descripcion (corta, grounded), tipo (\"prohibicion\"|\"limite_cuantitativo\"|"
              "\"limite_cualitativo\"). Sus cuantías van en `umbrales` (ver UMBRALES), no en properties.",
     "nuevo": "   Properties: descripcion (corta, grounded), tipo (\"prohibicion\"|\"limite_cuantitativo\"|"
              "\"limite_cualitativo\"). Sus cuantías van en `umbrales` (ver UMBRALES), no en properties.\n"
              "   CONSECUENCIA DE UN INCUMPLIMIENTO (una sanción, una multa, un cargo o un débito, la baja de una "
              "autorización, lo que se hace con quien no cumplió): NO es una Restriccion. Si el texto nombra a "
              "quien la aplica, es una Obligacion de ese sujeto cuando el texto la manda, o una Potestad cuando la "
              "habilita, con `aplica_a` hacia él; si no lo nombra, va a `omisiones` con categoría `fuera_de_tipos`, "
              "su tramo y, en `nota`, que es una consecuencia. En los dos casos copiá en `otras_propiedades`, clave "
              "`consecuencia`, el tramo literal que la ata a la falta, tal cual. Sus cuantías (el porcentaje de una "
              "multa, sus topes) van en `umbrales` si es una Obligacion, y en la descripción si es una Potestad."},
    {"id": "P3B-b2", "punto": "b", "hallazgo": "1.4",
     "viejo": "definir qué es un exceso o fijar la consecuencia de un incumplimiento no es un límite.",
     "nuevo": "definir qué es un exceso o fijar la consecuencia de un incumplimiento no es un límite (la "
              "consecuencia va como dice Restriccion)."},
    # ---------------- c. Excepcion conectada (hallazgo 2.8) ----------------
    {"id": "P3B-c1", "punto": "c", "hallazgo": "2.8",
     "viejo": "   Properties: descripcion (corta). Sus cuantías van en `umbrales`.\n   POLARIDAD: la Excepcion",
     "nuevo": "   Properties: descripcion (corta). Sus cuantías van en `umbrales`.\n"
              "   CONEXIÓN: si la norma que la Excepcion exceptúa está en tu unidad, conectala: `exceptua` hacia la "
              "Restriccion, `exceptua_obligacion` hacia la Obligacion. Si esa norma no está en tu unidad (está en "
              "la unidad del encabezado de una lista o en otro punto), emití la Excepcion sin esa relación y decí "
              "en la descripción qué norma exceptúa: no la conectes con otro elemento del chunk.\n"
              "   POLARIDAD: la Excepcion"},
    # ---------------- d. Predicados (hallazgo 3.2) ----------------
    {"id": "P3B-d1", "punto": "d", "hallazgo": "3.2",
     "viejo": "| `regula` | {Restriccion, Obligacion} → Operacion |",
     "nuevo": "| `regula` | {Restriccion, Obligacion} → Operacion (desde Restriccion no se usa: ver REGLA `regula` / "
              "`prohibe` / `limita`) |"},
    {"id": "P3B-d2", "punto": "d", "hallazgo": "3.2",
     "viejo": "| `condicion_de` | Condicion → {Excepcion, Obligacion, Restriccion, Operacion, Potestad} |\n\n",
     "nuevo": "| `condicion_de` | Condicion → {Excepcion, Obligacion, Restriccion, Operacion, Potestad} |\n\n"
              "Tres predicados unen un deber con un acto; elegí por el sentido del vínculo:\n"
              "- `regula` (Obligacion → Operacion): el deber fija cómo se hace el acto: su forma, sus requisitos, "
              "su procedimiento.\n"
              "- `condiciona` (Obligacion → Operacion): el acto solo puede hacerse si antes se cumplió el deber; el "
              "deber es una condición previa del acto.\n"
              "- `requiere` (Operacion → Obligacion): hacer el acto hace nacer el deber; el deber es consecuencia "
              "del acto.\n"
              "Si el vínculo no es ninguno de los tres, no lo fuerces: registralo como `relacion_sin_predicado`.\n\n"},
    {"id": "P3B-d3", "punto": "d", "hallazgo": "3.2",
     "viejo": "- Una Restriccion NUNCA usa `regula`: `regula` queda RESERVADO para Obligacion→Operacion. Cuando una "
              "Obligacion regula cómo se hace una Operacion, usá `regula`.",
     "nuevo": "- Una Restriccion NUNCA usa `regula`, aunque la tabla de predicados lo admita desde Restriccion: una "
              "Restriccion usa `prohibe` o `limita`. `regula` es de Obligacion → Operacion (ver su definición en "
              "PREDICADOS)."},
    # ---------------- e y f. Composición: listas dentro de la unidad y listas de excepciones ----------------
    {"id": "P3B-ef1", "punto": "e, f y g", "hallazgo": "1.18, U-DIAG-VINCULO, 1.2",
     "viejo": "Si el contexto heredado termina en un encabezado así y tu unidad es uno de sus ítems, mirá qué son "
              "los ítems:",
     "nuevo": "Si el contexto heredado trae un encabezado así (el mensaje lo señala; después de él puede haber "
              "párrafos de cierre del punto que lo contiene) y tu unidad es uno de sus ítems, mirá qué son los "
              "ítems:"},
    {"id": "P3B-f1", "punto": "f", "hallazgo": "U-DIAG-VINCULO",
     "viejo": "  - si se exigen juntos («y», «la totalidad», «concurrentemente») o no queda claro, el ítem es solo "
              "una Condicion, y la norma del encabezado no se extrae en ningún ítem: repetirla con una sola "
              "condición la daría por suficiente.\n",
     "nuevo": "  - si se exigen juntos («y», «la totalidad», «concurrentemente») o no queda claro, el ítem es solo "
              "una Condicion, y la norma del encabezado no se extrae en ningún ítem: repetirla con una sola "
              "condición la daría por suficiente.\n"
              "- EXCEPCIONES a una norma que el encabezado enuncia (el encabezado anuncia los casos que quedan "
              "fuera de esa norma): el ítem es una Excepcion compuesta: la salvedad del ítem junto con la norma que "
              "exceptúa, dicha en la descripción. Si esa norma está en tu unidad, conectala (ver Excepcion); si está "
              "en la unidad del encabezado o en otro punto, la Excepcion va sin `exceptua` ni "
              "`exceptua_obligacion`.\n"},
    {"id": "P3B-e1", "punto": "e", "hallazgo": "1.18",
     "viejo": "- Sí se extrae lo que el encabezado enuncia aparte de la lista: una norma propia, una excepción a la "
              "lista entera, y la norma principal cuando los ítems son sus supuestos o condiciones.\n",
     "nuevo": "- Sí se extrae lo que el encabezado enuncia aparte de la lista: una norma propia, una excepción a la "
              "lista entera, y la norma principal cuando los ítems son sus supuestos o condiciones.\n\n"
              "Lista dentro de tu unidad: la composición vale también cuando el encabezado y su lista están en el "
              "texto de tu unidad (una oración que termina en «:» seguida de ítems marcados con guiones, letras o "
              "números que no son puntos del documento). Cada ítem se compone con el encabezado como arriba, con "
              "`punto` = tu unidad, y el `tramo` lleva los dos segmentos, los dos del texto de tu unidad. No emitas "
              "cada ítem como una norma suelta sin el sujeto ni la modalidad del encabezado.\n"},
    {"id": "P3B-g1", "punto": "g", "hallazgo": "1.2",
     "viejo": "El supuesto puede estar enunciado por el ENCABEZADO HEREDADO: si el contexto heredado termina "
              "anunciando las condiciones o supuestos que los ítems siguientes enumeran,",
     "nuevo": "El supuesto puede estar enunciado por el ENCABEZADO HEREDADO: si el contexto heredado trae el "
              "encabezado que anuncia las condiciones o supuestos que los ítems siguientes enumeran (el mensaje lo "
              "señala),"},
]


def aplicar(texto: str, reemplazos: list[dict]) -> str:
    for r in reemplazos:
        n = texto.count(r["viejo"])
        if n != 1:
            raise SystemExit(f"{r['id']}: el ancla aparece {n} veces en el texto (se exige 1)")
        texto = texto.replace(r["viejo"], r["nuevo"])
    return texto


def hash_canonico(texto: str) -> str:
    bloque = {"type": "text", "text": texto, "cache_control": {"type": "ephemeral"}}
    can = json.dumps({"system": [bloque], "tools": [P.TOOL_SCHEMA_R2B]}, sort_keys=True, ensure_ascii=False,
                     separators=(",", ":"))
    return hashlib.sha256(can.encode("utf-8")).hexdigest()[:12]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    sal = ap.parse_args().salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    sal.mkdir(parents=True, exist_ok=True)
    congelado = P.PREFIJO_SISTEMA_R2B
    assert P.PREFIJO_HASH_R2B == "14d6b63b508e" and hash_canonico(congelado) == P.PREFIJO_HASH_R2B
    nuevo = aplicar(congelado, REEMPLAZOS)
    # reversibilidad: deshaciendo los reemplazos en orden inverso vuelve el congelado
    t = nuevo
    for r in reversed(REEMPLAZOS):
        assert t.count(r["nuevo"]) == 1, r["id"]
        t = t.replace(r["nuevo"], r["viejo"])
    assert t == congelado
    (sal / "prefijo_r2b_parche_borrador.txt").write_text(nuevo, encoding="utf-8")
    (sal / "reemplazos_p3b_borrador.json").write_text(json.dumps(REEMPLAZOS, ensure_ascii=False, indent=1) + "\n",
                                                       encoding="utf-8")
    md = ["# Parche P3b: el prefijo congelado (`14d6b63b508e`) y el borrador, lado a lado", "",
          "Cada reemplazo: el tramo congelado y el nuevo. Lo que no aparece acá no cambia.", ""]
    for r in REEMPLAZOS:
        md += [f"## {r['id']} — punto {r['punto']} (hallazgo {r['hallazgo']})", "", "**Congelado:**", "",
               "```text", r["viejo"].rstrip("\n"), "```", "", "**Nuevo:**", "", "```text", r["nuevo"].rstrip("\n"),
               "```", ""]
    (sal / "lado_a_lado_p3b.md").write_text("\n".join(md), encoding="utf-8")
    h = {"congelado": {"caracteres": len(congelado), "sha256": hashlib.sha256(congelado.encode()).hexdigest(),
                       "hash_canonico": P.PREFIJO_HASH_R2B},
         "borrador": {"caracteres": len(nuevo), "sha256": hashlib.sha256(nuevo.encode()).hexdigest(),
                      "hash_canonico": hash_canonico(nuevo)},
         "reemplazos": len(REEMPLAZOS), "tool_schema_sha256": P.TOOL_SCHEMA_R2_SHA256_ESPERADO,
         "caracteres_agregados": len(nuevo) - len(congelado)}
    (sal / "hashes_p3b.json").write_text(json.dumps(h, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(h, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
