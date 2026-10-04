"""
borrador_parche_p3c.py — U-PROMPT-R2, P3c-1 (USD 0, sin API): borrador del parche del prefijo r2b congelado
(`3817de475c93`, re-congelado en P3b-2, `c8c3970`), puntos a a e del ajuste de P3c (revisión de la autora del FRENO P4,
04/10/2026).

Como en P3b-1 (`p3b/borrador_parche_p3b.py`), el parche son reemplazos con ancla única sobre el texto congelado
(`prompt_r2b.PREFIJO_SISTEMA_R2B`), reversibles byte a byte. Cada reemplazo lleva el punto del ajuste y el hallazgo de
P4 que lo motiva (`p4/lectura_p4.md`, revisada por la autora). No congela nada: P3c-2 congela tras la aprobación del
texto. Los patrones se describen con palabras propias (control: nofiltracion_p3c.py).

Escribe en --salida:
  - prefijo_r2b_p3c_borrador.txt: el prefijo con el parche;
  - reemplazos_p3c_borrador.json: los reemplazos (viejo, nuevo, punto, hallazgo);
  - lado_a_lado_p3c.md: cada tramo, congelado y nuevo;
  - hashes_p3c.json: sha256 y largo del texto, y el hash canónico (system + tools) con el tool schema vigente.

Uso (desde la raíz de una copia del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3c/borrador_parche_p3c.py --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

P3C = Path(__file__).resolve().parent
REPO = P3C.parents[3]
sys.path.insert(0, str(REPO / "data" / "experiment" / "reextraccion_v2" / "e1_extractor"))
import prompt_r2b as P  # noqa: E402

BASE_HASH = "3817de475c93"

REEMPLAZOS = [
    # ---------------- a. meta_normativo, más estricta ----------------
    {"id": "P3C-a1", "punto": "a", "hallazgo": "P4, revisión d: 9 omisiones meta_normativo normativas",
     "viejo": "El contenido que predica sobre el SIGNIFICADO o el ALCANCE JURÍDICO de un acto o de una norma —y no sobre "
              "la conducta de nadie— NO tiene tipo en este esquema",
     "nuevo": "El contenido que predica sobre el SIGNIFICADO de un acto o de una norma —y no sobre la conducta de nadie, "
              "ni sobre a quién o a qué se aplica— NO tiene tipo en este esquema"},
    {"id": "P3C-a2", "punto": "a", "hallazgo": "P4, revisión d",
     "viejo": "declaraciones de objetivo, finalidad u objeto de las normas, y reglas de vigencia o de aplicabilidad "
              "temporal.",
     "nuevo": "declaraciones de objetivo, finalidad u objeto de las normas, y la fecha desde la que una norma entra en "
              "vigencia."},
    {"id": "P3C-a3", "punto": "a", "hallazgo": "P4, revisión c y d",
     "viejo": "esta regla prohíbe fabricar prescripciones falsas, no omitir permisos reales.",
     "nuevo": "esta regla prohíbe fabricar prescripciones falsas, no omitir permisos reales.\n"
              "   PRUEBA ANTES DE REGISTRAR UN `meta_normativo`: releé el tramo. Si dice un deber, una prohibición, una "
              "facultad, una condición, una excepción, un alcance (a quién o a qué se aplica una norma, qué abarca una "
              "clase o qué deja afuera) o una modalidad (si algo se exige, se permite o se aconseja, o si basta una "
              "entre varias opciones), NO es meta-normativo: extraelo con el tipo que le toca. Lo que abarca o excluye "
              "una clase que el texto nombra es una Definicion de esa clase; el alcance de una norma va en esa misma "
              "norma (su descripción, su `aplica_a`, su Condicion o su Excepcion). Si ningún tipo lo representa, "
              "registralo como `fuera_de_tipos`, nunca como `meta_normativo`. Una finalidad dice para qué existe la "
              "norma; un alcance, a qué se aplica: si quitar la frase hace que la norma valga para más casos (otro "
              "cálculo, otra operación, otro régimen), es alcance y va en la descripción de esa norma; si no cambia a "
              "qué se aplica, es finalidad. Hay un solo caso en que un deber, una modalidad, un cuantificador o una "
              "condición no se extraen en la unidad que los dice: los que un encabezado de lista fija para cada uno "
              "de sus ítems. Esos se extraen en cada ítem, y en la unidad del encabezado no se extraen ni se registran "
              "como omisión (ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA)."},
    {"id": "P3C-a4", "punto": "a", "hallazgo": "P4, revisión d",
     "viejo": "- `categoria`: `meta_normativo` (regla 9);",
     "nuevo": "- `categoria`: `meta_normativo` (regla 9 y su prueba: nunca un tramo con un deber, una prohibición, una "
              "facultad, una condición, una excepción, un alcance o una modalidad);"},
    {"id": "P3C-a5", "punto": "a", "hallazgo": "P4, revisión c (la Definicion de alcance de cla::5.1.1::intro)",
     "viejo": "no vuelve definitoria a la unidad si el cuerpo prescribe, aplica o delimita alcance en vez de definir.",
     "nuevo": "no vuelve definitoria a la unidad si el cuerpo prescribe, aplica o delimita el alcance de una norma en "
              "vez de definir; lo que una clase abarca o deja afuera sí la define."},
    {"id": "P3C-a6", "punto": "a", "hallazgo": "revisión del FRENO P4: adrei::4.3.1::intro y polcre::7.1::intro",
     "viejo": "- No se emite un nodo por el solo anuncio de la lista (regla 1), ni lo que se compone en los ítems: así no "
              "hay duplicados.\n",
     "nuevo": "- No se emite un nodo por el solo anuncio de la lista (regla 1), ni lo que se compone en los ítems: así no "
              "hay duplicados. Tampoco se registra como omisión: un encabezado que anuncia la lista con el sujeto, el "
              "deber o la modalidad, el cuantificador o la condición que valen para cada ítem no deja nada sin "
              "extraer, porque todo eso se extrae en cada ítem. No es `meta_normativo` (dice un deber o una "
              "condición) ni `fuera_de_tipos`: no es una omisión.\n"},
    # ---------------- b. Listas que exceptúan: los dos tipos ----------------
    {"id": "P3C-b1", "punto": "b", "hallazgo": "P4, estrato de listas (regla f en 4 de 8) y d",
     "viejo": "- EXCEPCIONES a una norma que el encabezado enuncia (el encabezado anuncia los casos que quedan fuera de "
              "esa norma): el ítem es una Excepcion compuesta: la salvedad del ítem junto con la norma que exceptúa, "
              "dicha en la descripción. Si esa norma está en tu unidad, conectala (ver Excepcion); si está en la "
              "unidad del encabezado o en otro punto, la Excepcion va sin `exceptua` ni `exceptua_obligacion`.\n",
     "nuevo": "- EXCEPCIONES a una norma que el encabezado enuncia. Mirá qué trae cada ítem:\n"
              "  - LO QUE QUEDA AFUERA: el encabezado nombra una clase o un conjunto y anuncia los miembros que se "
              "excluyen; cada ítem nombra uno de esos miembros (una clase de operaciones, de sujetos o de bienes). El "
              "ítem es una Excepcion: su descripción dice qué miembro queda afuera y de qué norma. Si el ítem agrega "
              "una salvedad que devuelve a la norma una parte de ese miembro (una contra-excepción: quedan afuera, "
              "salvo los que reúnan ciertas condiciones), esa parte va en el mismo ítem como manda POLARIDAD (ver "
              "Excepcion): la norma que vuelve a regir en ese supuesto, con una Condicion por cada condición y "
              "`condicion_de` hacia esa norma (si lo que vuelve a regir es que el miembro integra la clase, esa norma "
              "es el acto de clasificarlo en ella: una Operacion); y la descripción de la Excepcion menciona la "
              "salvedad.\n"
              "  - LAS CONDICIONES DE UNA SOLA EXCEPCIÓN: el encabezado enuncia la norma y una única salvedad, que rige "
              "cuando se cumple alguno de los supuestos que siguen (o todos); cada ítem describe un supuesto, no un "
              "miembro. El ítem es una Condicion de esa excepción (ver Condicion), con su cuantificador (si basta uno "
              "o se exigen todos). La excepción la extrae la unidad del encabezado; si no está en tu unidad, la "
              "Condicion va sin `condicion_de`. Si el encabezado es la línea de título de un punto (sin unidad "
              "propia), vale lo dicho para SUPUESTOS O CONDICIONES en ese caso: con supuestos alternativos, el ítem es "
              "la Excepcion compuesta con su supuesto; con supuestos que se exigen juntos, solo la Condicion.\n"
              "  - En los dos casos, la descripción de la entidad del ítem nombra la norma que se exceptúa (qué deber, "
              "prohibición, requisito o alcance deja de regir), aunque esa norma esté en otra unidad; y si no está en "
              "tu unidad, no emitas `exceptua` ni `exceptua_obligacion` (ver Excepcion).\n"},
    {"id": "P3C-b2", "punto": "b", "hallazgo": "P4, estrato de listas",
     "viejo": "- Sí se extrae lo que el encabezado enuncia aparte de la lista: una norma propia, una excepción a la lista "
              "entera, y la norma principal cuando los ítems son sus supuestos o condiciones.",
     "nuevo": "- Sí se extrae lo que el encabezado enuncia aparte de la lista: una norma propia, una excepción a la lista "
              "entera, y la norma principal cuando los ítems son sus supuestos o condiciones. Si los ítems son las "
              "condiciones de una sola excepción, esta unidad extrae la norma y esa excepción, unidas con `exceptua` o "
              "`exceptua_obligacion`; si los ítems son lo que queda afuera de una clase, extrae lo que el encabezado "
              "dice de esa clase (lo que abarca, como Definicion)."},
    {"id": "P3C-b3", "punto": "b", "hallazgo": "P4, estrato de listas",
     "viejo": "(una norma propia, una excepción a la lista entera, la norma principal cuando los ítems son sus "
              "supuestos o condiciones)",
     "nuevo": "(una norma propia, una excepción a la lista entera, la norma principal cuando los ítems son sus "
              "supuestos o condiciones, la excepción cuando los ítems son sus condiciones)"},
    # ---------------- c. Un nodo por condición ----------------
    {"id": "P3C-c1", "punto": "c", "hallazgo": "P4, revisión b (e2 de cla::5.1.1.1)",
     "viejo": "   Properties: descripcion (corta, grounded). Sus cuantías van en `umbrales`.\n\n9. **Definicion**",
     "nuevo": "   Properties: descripcion (corta, grounded). Sus cuantías van en `umbrales`.\n"
              "   UNA POR SUPUESTO: si la norma pide dos o más supuestos (unidos por «y», o uno con una cuantía y otro "
              "sin ella), emití una Condicion por cada uno, todas con `condicion_de` hacia la misma norma. En cada "
              "Condicion, el label, la descripción, el `tramo` y los `umbrales` hablan del mismo supuesto: no pongas "
              "un supuesto en el label o en los umbrales y otro en la descripción o en el tramo.\n\n9. **Definicion**"},
    {"id": "P3C-c2", "punto": "c", "hallazgo": "P4, revisión b",
     "viejo": "- `properties.descripcion`: la oración o cita textual del corpus (acá va el contenido largo, sin tope).\n",
     "nuevo": "- `properties.descripcion`: la oración o cita textual del corpus (acá va el contenido largo, sin tope).\n"
              "- El label nombra lo mismo que la descripción, el `tramo` y los `umbrales` de su entidad: un label que "
              "habla de una cosa y una descripción que habla de otra es un error.\n"},
    # ---------------- d. La norma del encabezado no se repite en el ítem ----------------
    {"id": "P3C-d1", "punto": "d", "hallazgo": "P4, estrato de listas (3 exceptua colgantes y ext::13.4.4)",
     "viejo": "emití la Excepcion sin esa relación y decí en la descripción qué norma exceptúa: no la conectes con otro "
              "elemento del chunk.",
     "nuevo": "emití la Excepcion sin esa relación y decí en la descripción qué norma exceptúa: no la conectes con otro "
              "elemento del chunk, no apuntes la relación a un `local_id` que no emitiste y no vuelvas a emitir esa "
              "norma dentro de tu unidad para tener a dónde conectarla."},
    {"id": "P3C-d2", "punto": "d", "hallazgo": "P4, estrato de listas (ext::13.4.4)",
     "viejo": "\n\nEn la norma compuesta:\n",
     "nuevo": "\n\nLa norma del encabezado no se emite como una entidad aparte dentro del ítem, en ninguno de los casos: "
              "en una lista de contenidos es la norma compuesta del ítem; en una de supuestos, condiciones o "
              "excepciones va nombrada en la descripción de la entidad del ítem.\n\nEn la norma compuesta:\n"},
    # ---------------- e. Sin mención cuando el texto no nombra al sujeto ----------------
    {"id": "P3C-e1", "punto": "e", "hallazgo": "P4, D2: 14 menciones «las entidades» que no verifican",
     "viejo": "Si el texto de la unidad no lo nombra y el sujeto está en el contexto heredado, copiala de ahí.",
     "nuevo": "Si el texto de la unidad no lo nombra y el sujeto está en el contexto heredado, copiala de ahí. Si ni la "
              "unidad ni el contexto heredado nombran al sujeto, no emitas la relación: no escribas una mención que el "
              "texto no trae, aunque el mensaje indique el alcance del TO."},
    {"id": "P3C-e2", "punto": "e", "hallazgo": "P4, D2",
     "viejo": "- Si la norma se dirige al colectivo del TO (\"las entidades\", \"los sujetos obligados\", sin otro "
              "calificativo), la mención es esa expresión y la sugerencia",
     "nuevo": "- Si el texto nombra al colectivo del TO con una expresión genérica (\"las entidades\", \"los sujetos "
              "obligados\", sin otro calificativo), la mención es esa expresión, copiada del texto, y la sugerencia"},
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
    assert P.PREFIJO_HASH_R2B == BASE_HASH and hash_canonico(congelado) == BASE_HASH
    nuevo = aplicar(congelado, REEMPLAZOS)
    t = nuevo
    for r in reversed(REEMPLAZOS):       # reversibilidad: deshaciendo en orden inverso vuelve el congelado
        assert t.count(r["nuevo"]) == 1, r["id"]
        t = t.replace(r["nuevo"], r["viejo"])
    assert t == congelado
    (sal / "prefijo_r2b_p3c_borrador.txt").write_text(nuevo, encoding="utf-8")
    (sal / "reemplazos_p3c_borrador.json").write_text(json.dumps(
        {"base_hash_canonico": BASE_HASH, "reemplazos": REEMPLAZOS}, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8")
    md = [f"# Parche P3c: el prefijo congelado (`{BASE_HASH}`) y el borrador, lado a lado", "",
          "Cada reemplazo: el tramo congelado y el nuevo. Lo que no aparece acá no cambia.", ""]
    for r in REEMPLAZOS:
        md += [f"## {r['id']} — punto {r['punto']} ({r['hallazgo']})", "", "**Congelado:**", "",
               "```text", r["viejo"].strip("\n"), "```", "", "**Nuevo:**", "", "```text", r["nuevo"].strip("\n"),
               "```", ""]
    (sal / "lado_a_lado_p3c.md").write_text("\n".join(md), encoding="utf-8")
    h = {"congelado": {"caracteres": len(congelado), "sha256": hashlib.sha256(congelado.encode()).hexdigest(),
                       "hash_canonico": BASE_HASH},
         "borrador": {"caracteres": len(nuevo), "sha256": hashlib.sha256(nuevo.encode()).hexdigest(),
                      "hash_canonico": hash_canonico(nuevo)},
         "reemplazos": len(REEMPLAZOS), "por_punto": {p: sum(r["punto"] == p for r in REEMPLAZOS) for p in "abcde"},
         "tool_schema_sha256": P.TOOL_SCHEMA_R2_SHA256_ESPERADO,
         "caracteres_agregados": len(nuevo) - len(congelado)}
    (sal / "hashes_p3c.json").write_text(json.dumps(h, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(h, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
