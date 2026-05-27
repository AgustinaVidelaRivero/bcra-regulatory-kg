"""
Checkpoint pre-assembly: reporta lo que el usuario pidió antes de canonizar/ensamblar.

1. Resumen global: chunks ok/empty/fail por TO, costo acumulado, totales.
2. Tipos crudos NUEVOS que aparecieron en los 4 TOs (Clasificación, RI, Exterior, Capitales)
   y NO estaban en el smoke#2 sobre Protección, con frecuencia.
3. Tipos emergentes que matchean el patrón de jerarquía documental del backstop
   (Comuns A/B, Ley, Decreto, Resolución, Circular), por si aparecen variantes.
"""

import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

EXTRACT_DIR = Path(__file__).resolve().parent / "cache" / "extract"
FAILURES_PATH = EXTRACT_DIR / "_failures.jsonl"

TOS = {
    "Protección": "TO_proteccion_usuarios_servicios_financieros_actual",
    "Clasificación Deudores": "TO_clasificacion_deudores_actual",
    "RI Cont. Mensual": "TO_regimen_informativo_contable_mensual_actual",
    "Exterior y Cambios": "TO_exterior_cambios_actual",
    "Capitales Mínimos": "TO_capitales_minimos_actual",
}

# Backstop patterns (exactamente como pidió la autora)
BACKSTOP_PATTERNS = [
    re.compile(r"^comunicacion_(a|b)"),
    re.compile(r"^ley(_nacional)?$"),
    re.compile(r"^decreto"),
    re.compile(r"^resolucion"),
    re.compile(r"^circular"),
]


def slug_normalize(s: str) -> str:
    """Normalización superficial: lowercase, strip acentos, snake_case."""
    s = s.lower().strip()
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = s.strip("_")
    return s


def matches_backstop(type_normalized: str) -> bool:
    return any(p.search(type_normalized) for p in BACKSTOP_PATTERNS)


def load_to(prefix: str) -> list[dict]:
    """Lee todas las extracciones de un TO."""
    out = []
    for p in sorted(EXTRACT_DIR.glob(f"{prefix}__chunk_*.json")):
        try:
            out.append(json.loads(p.read_text()))
        except Exception as e:
            print(f"[warn] {p}: {e}")
    return out


def main():
    print("=" * 70)
    print("PRE-ASSEMBLY CHECKPOINT — Run 4 schema-light puro")
    print("=" * 70)
    print()

    # ---- 1) Resumen por TO + costo acumulado ----
    print("--- Resumen por TO ---")
    print(f"{'TO':<25} {'chunks':>7} {'ok':>5} {'empty':>6} {'fail':>5} {'ent':>6} {'rel':>6} {'cost':>9}")
    total = {"chunks": 0, "ok": 0, "empty": 0, "fail": 0, "ent": 0, "rel": 0, "cost": 0.0,
             "in_tok": 0, "out_tok": 0}

    types_by_to = defaultdict(Counter)
    all_data_by_to = {}

    for name, prefix in TOS.items():
        data = load_to(prefix)
        all_data_by_to[name] = data
        n_chunks = len(data)
        n_ok = sum(1 for d in data if d["status"] == "ok")
        n_empty = sum(1 for d in data if d["status"] == "empty")
        # fails los contamos desde el JSONL
        n_ent = sum(len(d["entities"]) for d in data)
        n_rel = sum(len(d["relations"]) for d in data)
        in_tok = sum(d.get("usage", {}).get("input_tokens", 0) for d in data)
        out_tok = sum(d.get("usage", {}).get("output_tokens", 0) for d in data)
        cost = in_tok * 1.0 / 1e6 + out_tok * 5.0 / 1e6
        for d in data:
            for e in d["entities"]:
                types_by_to[name][e["type"]] += 1

        # contar fails desde el JSONL
        n_fail = 0
        if FAILURES_PATH.exists():
            for line in FAILURES_PATH.read_text().splitlines():
                if not line.strip():
                    continue
                try:
                    rec = json.loads(line)
                    if rec.get("source_pdf", "").startswith(prefix.replace(".pdf", "")):
                        n_fail += 1
                except Exception:
                    pass

        print(f"{name:<25} {n_chunks:>7} {n_ok:>5} {n_empty:>6} {n_fail:>5} {n_ent:>6} {n_rel:>6} ${cost:>7.3f}")
        total["chunks"] += n_chunks
        total["ok"] += n_ok
        total["empty"] += n_empty
        total["fail"] += n_fail
        total["ent"] += n_ent
        total["rel"] += n_rel
        total["cost"] += cost
        total["in_tok"] += in_tok
        total["out_tok"] += out_tok

    print(f"{'TOTAL':<25} {total['chunks']:>7} {total['ok']:>5} {total['empty']:>6} {total['fail']:>5} {total['ent']:>6} {total['rel']:>6} ${total['cost']:>7.3f}")
    print()
    print(f"Tokens totales: in={total['in_tok']}, out={total['out_tok']}")
    print(f"Failures persistentes en _failures.jsonl: {total['fail']}")
    print()

    # ---- 2) Tipos crudos NUEVOS en los 4 TOs (vs smoke#2 de Protección) ----
    proteccion_types = set(types_by_to["Protección"].keys())

    # Combinar los 4 TOs nuevos
    new_tos_types = Counter()
    for name in ["Clasificación Deudores", "RI Cont. Mensual", "Exterior y Cambios", "Capitales Mínimos"]:
        new_tos_types += types_by_to[name]

    new_types = {t: n for t, n in new_tos_types.items() if t not in proteccion_types}

    print(f"--- Tipos crudos NUEVOS (aparecen en los 4 TOs y NO en smoke#2 sobre Protección) ---")
    print(f"Total tipos en smoke#2 Protección: {len(proteccion_types)}")
    print(f"Total tipos únicos en los 4 TOs:   {len(new_tos_types)}")
    print(f"Tipos NUEVOS (no overlap):          {len(new_types)}")
    print()

    # Top por frecuencia
    print(f"--- Top 60 tipos NUEVOS por frecuencia ---")
    sorted_new = sorted(new_types.items(), key=lambda x: -x[1])
    for t, n in sorted_new[:60]:
        print(f"  {n:5d}  {t}")
    print(f"  ... y {max(0, len(sorted_new) - 60)} tipos más (freq decreciente)")
    print()

    # Distribución de freq
    freq_dist = Counter()
    for n in new_types.values():
        if n >= 10:
            freq_dist[">=10"] += 1
        elif n >= 5:
            freq_dist["5-9"] += 1
        elif n >= 2:
            freq_dist["2-4"] += 1
        else:
            freq_dist["1 (singleton)"] += 1
    print(f"--- Distribución de freq de los tipos NUEVOS ---")
    for label in [">=10", "5-9", "2-4", "1 (singleton)"]:
        print(f"  {label:<15}: {freq_dist[label]}")
    print()

    # ---- 3) Tipos que matchean el backstop estructural ----
    print(f"--- Tipos que matchean el BACKSTOP estructural ---")
    print(f"Patrones: ^comunicacion_(a|b), ^ley(_nacional)?$, ^decreto, ^resolucion, ^circular")
    print()

    # Computar sobre TODOS los tipos (los 5 TOs)
    all_types = Counter()
    for c in types_by_to.values():
        all_types += c

    matched = []
    for t, n in all_types.items():
        norm = slug_normalize(t)
        if matches_backstop(norm):
            matched.append((t, norm, n))

    if not matched:
        print("  (ninguno — backstop limpio)")
    else:
        print(f"  {'type_raw':<55} {'normalized':<35} {'freq':>5}")
        for t, norm, n in sorted(matched, key=lambda x: -x[2]):
            print(f"  {t:<55} {norm:<35} {n:>5}")
    print()

    # Adicionalmente: tipos que matchean patrones aproximados (para sugerir nuevos backstops si aparece algo no cubierto)
    print(f"--- Tipos que CONTIENEN palabras clave de jerarquía documental (sospechosos, no necesariamente backstop) ---")
    sospechosos_keywords = ["comunicacion", "comunicación", "ley", "decreto", "resolucion", "resolución",
                            "circular", "punto", "anexo", "articulo", "artículo", "seccion", "sección",
                            "capitulo", "capítulo", "texto_ordenado"]
    susp = []
    for t, n in all_types.items():
        norm = slug_normalize(t)
        if matches_backstop(norm):
            continue  # ya reportado arriba
        if any(kw in norm for kw in sospechosos_keywords):
            susp.append((t, norm, n))

    if not susp:
        print("  (ninguno)")
    else:
        print(f"  {'type_raw':<55} {'normalized':<35} {'freq':>5}")
        for t, norm, n in sorted(susp, key=lambda x: -x[2]):
            print(f"  {t:<55} {norm:<35} {n:>5}")
    print()

    # ---- 4) Conteo de entidades por TO que matchean el backstop (sería filtrado en assemble) ----
    print(f"--- Conteo de ENTITIES (con duplicados) que el backstop dropearia ---")
    for name, data in all_data_by_to.items():
        n_drop = 0
        for d in data:
            for e in d["entities"]:
                if matches_backstop(slug_normalize(e["type"])):
                    n_drop += 1
        print(f"  {name:<25}: {n_drop}")

    # Guardar payload estructurado
    payload = {
        "summary_by_to": {
            name: {
                "n_chunks": len(all_data_by_to[name]),
                "n_ok": sum(1 for d in all_data_by_to[name] if d["status"] == "ok"),
                "n_empty": sum(1 for d in all_data_by_to[name] if d["status"] == "empty"),
                "n_entities": sum(len(d["entities"]) for d in all_data_by_to[name]),
                "n_relations": sum(len(d["relations"]) for d in all_data_by_to[name]),
            }
            for name in TOS
        },
        "total": total,
        "new_types_count": len(new_types),
        "new_types_top60": sorted_new[:60],
        "backstop_matches": [{"type_raw": t, "normalized": n, "freq": f} for t, n, f in matched],
        "suspicious_types": [{"type_raw": t, "normalized": n, "freq": f} for t, n, f in susp],
    }
    out = Path(__file__).resolve().parent / "cache" / "preassembly_checkpoint.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(f"\n[preassembly_report] structured payload → {out}")


if __name__ == "__main__":
    main()
