"""
selftest_prompt_r2b.py — U-PROMPT-R2, P2 y P3b-2: selftest OFFLINE del perfil r2b (prompt_r2b.py). Cero llamadas a la
API.

  A. Candados: el texto armado y el hash canónico son los congelados (re-congelados en P3b-2); el tool schema, la
     tabla de alcance r2, los labels, el bloque de catálogo, los reemplazos de P2 y el parche de P3b tienen los sha
     esperados.
  B. Fuera de los tramos reemplazados, el texto es byte a byte el del sellado v3_b54 (precedente:
     selftest_prompt_v3_b54.py): cada `nuevo` del parche de P3b aparece una sola vez y, revirtiéndolos, se obtiene
     el prefijo de P2 (14d6b63b508e); cada `nuevo` de P2 aparece una sola vez en él y, revirtiendo esos reemplazos
     en orden inverso y el bloque de catálogo, se obtiene exactamente prompt_v3_b54.PREFIJO_SISTEMA_V3.
  C. El prefijo de P2 es el del borrador B aprobado en el FRENO P1 (prompt_r2/p1/salida/prefijo_r2_borrador_B.txt) y
     el congelado es el borrador de P3b-1 aprobado (prompt_r2/p3b/salida/prefijo_r2b_parche_borrador.txt), con los
     mismos 12 reemplazos (reemplazos_p3b_borrador.json).
  D. Request: system como bloque único con cache_control al final, tools = el tool schema r2, tool_choice forzado,
     max_tokens 8.192; prefijo idéntico entre unidades; mismo chunk → mismo request.
  E. Mensaje: igual, en las 2.434 unidades de la e0-r2 de la tanda 0, al del borrador de P3b-1 aprobado
     (prompt_r2/p3b/mensaje_p3b_borrador.build_user_message_p3b); igual al de P1
     (prompt_r2/p1/mensaje_r2_borrador.build_user_message_r2, con la tabla de alcance v3, que coincide con la r2)
     salvo en los 1.053 ítems (g) y los 121 mini-chunks a mitad de oración (h); la línea del recorte de E0 va solo
     en un chunk con `herencia_recortada`.
  F. Tablas forzadas a residual: con una tabla en la lista, cambia el mensaje de su unidad y no el prefijo.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/reextraccion_v2/e1_extractor/selftest_prompt_r2b.py
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(AQUI))
import comun_e1  # noqa: E402
import prompt_r2b as P  # noqa: E402
import prompt_v3_b54 as v3  # noqa: E402  (en el path vía prompt_r2b)

P1 = REPO / "data" / "experiment" / "prompt_r2" / "p1"
sys.path.insert(0, str(P1))
import mensaje_r2_borrador as MB  # noqa: E402

P3B = REPO / "data" / "experiment" / "prompt_r2" / "p3b"
sys.path.insert(0, str(P3B))
import mensaje_p3b_borrador as MB3  # noqa: E402

OK = FAIL = 0


def check(nombre: str, cond: bool, detalle: str = "") -> None:
    global OK, FAIL
    if cond:
        OK += 1
        print(f"  ok  {nombre}")
    else:
        FAIL += 1
        print(f"  FAIL {nombre} {detalle}")


def main() -> int:
    print("[A] candados")
    check("sha256 del texto y hash canónico congelados",
          P.PREFIJO_SHA256_R2B == P.PREFIJO_SHA256_R2B_ESPERADO and P.PREFIJO_HASH_R2B == P.PREFIJO_HASH_R2B_ESPERADO,
          f"{P.PREFIJO_SHA256_R2B[:12]} {P.PREFIJO_HASH_R2B}")
    for nombre, ruta, esperado in (("tool schema", P.TOOL_SCHEMA_R2_JSON, P.TOOL_SCHEMA_R2_SHA256_ESPERADO),
                                   ("rol_por_to_r2", P.ROL_POR_TO_R2_JSON, P.ROL_POR_TO_R2_SHA256_ESPERADO),
                                   ("labels_e2_r2", P.LABELS_E2_R2_JSON, P.LABELS_E2_R2_SHA256_ESPERADO),
                                   ("bloque de catálogo r2", P.BLOQUE_CATALOGO_R2, P.BLOQUE_CATALOGO_R2_SHA256_ESPERADO),
                                   ("reemplazos congelados", P.REEMPLAZOS_JSON, P.REEMPLAZOS_SHA256_ESPERADO),
                                   ("parche de P3b", P.PARCHE_P3B_JSON, P.PARCHE_P3B_SHA256_ESPERADO)):
        check(f"{nombre}: sha256 esperado", hashlib.sha256(ruta.read_bytes()).hexdigest() == esperado)
    man = json.loads((P.BLOQUE_CATALOGO_R2.parent / "manifest_generados_r2.json").read_text(encoding="utf-8"))
    check("bloque de catálogo r2 = el de su manifiesto (LN-8)",
          man["archivos"]["bloque_catalogo_r2.txt"] == P.BLOQUE_CATALOGO_R2_SHA256_ESPERADO)
    check("el sellado v3_b54 sigue intacto", v3.PREFIJO_SHA256_V3 == P.PREFIJO_SHA256_V3_ESPERADO
          and v3.PREFIJO_HASH_V3 == "54a111e2175f")
    check("re-congelado de P3b-2: 3817de475c93", P.PREFIJO_HASH_R2B == "3817de475c93"
          and len(P.PREFIJO_SISTEMA_R2B) == 55105, f"{P.PREFIJO_HASH_R2B} {len(P.PREFIJO_SISTEMA_R2B)}")
    check("prefijo de P2: sha esperado (14d6b63b508e)",
          hashlib.sha256(P.PREFIJO_SISTEMA_R2B_P2.encode("utf-8")).hexdigest() == P.PREFIJO_SHA256_R2B_P2)

    print("\n[B] fuera de los tramos reemplazados, byte a byte el sellado")
    t = P.PREFIJO_SISTEMA_R2B
    check("cada texto nuevo del parche de P3b aparece una sola vez (12 reemplazos)",
          all(t.count(r["nuevo"]) == 1 for r in P.REEMPLAZOS_P3B) and len(P.REEMPLAZOS_P3B) == 12)
    for r in reversed(P.REEMPLAZOS_P3B):
        t = t.replace(r["nuevo"], r["viejo"])
    check("revirtiendo el parche de P3b se obtiene el prefijo de P2 byte a byte", t == P.PREFIJO_SISTEMA_R2B_P2)
    bloque = P.BLOQUE_CATALOGO_R2.read_text(encoding="utf-8")
    check("el bloque de catálogo r2 aparece una sola vez", t.count(bloque) == 1)
    i = v3.PREFIJO_SISTEMA_V3.index(P.ANCLA_INICIO_BLOQUE)
    k = v3.PREFIJO_SISTEMA_V3.index(P.ANCLA_FIN_BLOQUE)
    t = t.replace(bloque, v3.PREFIJO_SISTEMA_V3[i:k])
    unicos = all(t.count(r["nuevo"]) == 1 for r in P.REEMPLAZOS_R2B)
    check("cada texto nuevo aparece una sola vez (30 reemplazos)", unicos and len(P.REEMPLAZOS_R2B) == 30)
    for r in reversed(P.REEMPLAZOS_R2B):
        t = t.replace(r["nuevo"], r["viejo"])
    check("revirtiendo reemplazos y bloque se obtiene el sellado v3_b54 byte a byte", t == v3.PREFIJO_SISTEMA_V3)

    print("\n[C] el texto congelado es el de los borradores aprobados")
    b = (P1 / "salida" / "prefijo_r2_borrador_B.txt").read_text(encoding="utf-8")
    check("prefijo_r2_borrador_B.txt == prefijo de P2", b == P.PREFIJO_SISTEMA_R2B_P2)
    b3 = (P3B / "salida" / "prefijo_r2b_parche_borrador.txt").read_text(encoding="utf-8")
    check("prefijo_r2b_parche_borrador.txt (P3b-1) == PREFIJO_SISTEMA_R2B", b3 == P.PREFIJO_SISTEMA_R2B)
    r3 = json.loads((P3B / "salida" / "reemplazos_p3b_borrador.json").read_text(encoding="utf-8"))
    check("los 12 reemplazos congelados == los del borrador de P3b-1", r3 == P.REEMPLAZOS_P3B)
    check("las dos oraciones del FRENO P1 están en el texto (R8 y R14)",
          "emití la Condicion sin condicion_de: no la conectes con otro elemento del chunk." in P.PREFIJO_SISTEMA_R2B
          and "Esto no cambia la Comunicacion: una Comunicación o una norma externa citada sigue siendo una entidad "
              "Comunicacion, con su referencia desde el TextoOrdenado; lo que no emitís es la remisión desde el "
              "contenido." in P.PREFIJO_SISTEMA_R2B
          and "| `referencia` | TextoOrdenado → Comunicacion |" in P.PREFIJO_SISTEMA_R2B)

    print("\n[D] request")
    tos = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
    e0r2 = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_tanda0_r2"
    chunks = comun_e1.cargar_chunks(tos, e0_dir=e0r2)
    check("2.434 unidades en la e0-r2 de la tanda 0", len(chunks) == 2434, str(len(chunks)))
    prefijos, deterministas = set(), 0
    for c in chunks:
        a = P.build_request_kwargs_r2b(c, model="m")
        prefijos.add(json.dumps({x: a[x] for x in ("system", "tools", "tool_choice", "max_tokens")}, sort_keys=True,
                                ensure_ascii=False))
        deterministas += a == P.build_request_kwargs_r2b(json.loads(json.dumps(c)), model="m")
    a = P.build_request_kwargs_r2b(chunks[0], model="m")
    check("system: un bloque, cache_control ephemeral al final", len(a["system"]) == 1
          and a["system"][-1]["cache_control"] == {"type": "ephemeral"})
    check("tools = tool schema r2; tool_choice forzado; max_tokens 8.192",
          a["tools"] == [P.TOOL_SCHEMA_R2B] and a["tool_choice"] == {"type": "tool", "name": "extraer_kg_e1"}
          and a["max_tokens"] == 8192)
    check("prefijo idéntico entre las 2.434 unidades", len(prefijos) == 1, str(len(prefijos)))
    check("mismo chunk → mismo request (2.434)", deterministas == 2434, str(deterministas))

    print("\n[E] mensaje igual a los borradores aprobados")
    iguales3 = sum(P.build_user_message_r2b(c) == MB3.build_user_message_p3b(c) for c in chunks)
    check("mensaje r2b == borrador de P3b-1 en las 2.434 unidades", iguales3 == 2434, f"{iguales3}/2434")
    cambian = [c for c in chunks if P.es_item(c) or P.mini_a_mitad(c)]
    check("ítems (g) y mini-chunks a mitad de oración (h): 1.053 + 121 = 1.174",
          sum(P.es_item(c) for c in chunks) == 1053 and sum(P.mini_a_mitad(c) for c in chunks) == 121
          and len(cambian) == 1174, f"{len(cambian)}")
    ids_cambian = {c["id"] for c in cambian}
    iguales = sum(P.build_user_message_r2b(c) == MB.build_user_message_r2(c, v3.ROL_POR_TO_V3, comun_e1.puntos_admitidos,
                                                                           comun_e1.es_mini_chunk)
                  for c in chunks if c["id"] not in ids_cambian)
    check("fuera de esos 1.174, mensaje r2b == borrador de P1 (1.260)", iguales == 1260, f"{iguales}/1260")
    check("ninguna unidad de la e0-r2 de la tanda 0 lleva herencia_recortada, ni la línea del recorte",
          not any(c.get("herencia_recortada") for c in chunks)
          and not any(P.LINEA_RECORTE in P.build_user_message_r2b(c) for c in chunks))
    c_rec = json.loads(json.dumps(next(c for c in chunks if c.get("herencia"))))
    c_rec["herencia_recortada"] = True
    check("con herencia_recortada, el mensaje lleva la línea del recorte una vez y el prefijo no cambia",
          P.build_user_message_r2b(c_rec).count(P.LINEA_RECORTE) == 1
          and P.build_request_kwargs_r2b(c_rec, model="m")["system"] == P.bloques_sistema_r2b())
    check("tabla de alcance r2 == la v3 en los 71 TOs", P.ROL_POR_TO_R2 == v3.ROL_POR_TO_V3)

    print("\n[F] tablas forzadas a residual")
    c6 = next(c for c in chunks if c["id"] == "cap::6.2.2.6")
    normal = P.build_user_message_r2b(c6)
    viejo = P.TABLAS_RESIDUALES_FORZADAS
    try:
        P.TABLAS_RESIDUALES_FORZADAS = frozenset({"cap::tabla037"})
        forzado = P.build_user_message_r2b(c6)
        sistema_forzado = P.build_request_kwargs_r2b(c6, model="m")["system"]
    finally:
        P.TABLAS_RESIDUALES_FORZADAS = viejo
    check("la lista versionada está vacía hoy", viejo == frozenset())
    check("con cap::tabla037 en la lista, cambia el mensaje de cap::6.2.2.6 y lo declara no confiable",
          forzado != normal and "se tratan como contenido NO-CONFIABLE (`cap::tabla037`)" in forzado)
    check("con la lista, el prefijo no cambia", sistema_forzado == P.bloques_sistema_r2b())

    print(f"\nRESULTADO: {OK} ok, {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
