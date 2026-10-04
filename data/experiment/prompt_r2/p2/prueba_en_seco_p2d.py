"""
prueba_en_seco_p2d.py — U-PROMPT-R2, P2.d (USD 0): requests de E1 del perfil r2b, impresos sin llamar a la API.

Casos (mandato, P2.d, con la nota del 03/10/2026 que cambia ric::9.2 por ric::9.2.1):
  - cap::1.2 y ric::9.2.1, dos chunks con tabla serializada;
  - uno con sujeto propuesto: la primera unidad, en el orden de la corrida (manifiesto tanda0_10tos_r2b) y del
    crudo guardado de la tanda 0, cuya salida v3 trae una relación con `sujeto_propuesto`;
  - cla::5.1.1.1, el ejemplo de la tesis.
Cada request es el que construye el perfil r2b sobre la E0 e0-r2, con el modelo del runner. Se escribe el request
completo (JSON) y un resumen con el mensaje de usuario, el sha256 del system y del tool schema, y la clave de la
caché local en el namespace del perfil.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p2/prueba_en_seco_p2d.py
Escribe data/experiment/prompt_r2/p2/salida/prueba_en_seco/.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

P2 = Path(__file__).resolve().parent
REPO = P2.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2"):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REX))
import manifiesto_corpus as MC  # noqa: E402
import perfil_e1  # noqa: E402
import comun_e1  # noqa: E402
import cliente_e1  # noqa: E402
import runner_corpus as RC  # noqa: E402

SAL = P2 / "salida" / "prueba_en_seco"
CRUDO_T0 = REX / "corpus_tanda0" / "salida_dirigida"


def con_sujeto_propuesto(orden: list[str]) -> str:
    for to in orden:
        for linea in (CRUDO_T0 / to / "extracciones_e1.jsonl").read_text(encoding="utf-8").splitlines():
            r = json.loads(linea)
            ti = r.get("tool_input_crudo") or {}
            rels = ti.get("relations") if isinstance(ti, dict) else None
            if isinstance(rels, list) and any(isinstance(x, dict) and x.get("sujeto_propuesto") for x in rels):
                return r["chunk_id"]
    raise SystemExit("ninguna unidad con sujeto_propuesto en el crudo de la tanda 0")


def main() -> None:
    man = MC.cargar(MC.MANIFIESTOS_DIR / "tanda0_10tos_r2b.json")
    pf = perfil_e1.perfil(man.perfil_e1)
    assert pf.nombre == "r2b"
    casos = ["cap::1.2", "ric::9.2.1", con_sujeto_propuesto(list(man.orden_corrida)), "cla::5.1.1.1"]
    ns = cliente_e1.namespace_e1(prefijo_hash=pf.prefijo_hash_para_namespace)
    SAL.mkdir(parents=True, exist_ok=True)
    resumen = {"perfil": pf.nombre, "prefijo_hash": pf.prefijo_hash, "namespace_e1": ns, "modelo": RC.MODEL_E1,
               "e0": str(man.e0_salida.relative_to(REPO)), "casos": []}
    md = ["# Prueba en seco de P2.d: requests de E1 del perfil r2b (sin API)", "",
          f"Perfil `{pf.nombre}`, hash canónico `{pf.prefijo_hash}`, namespace `{ns}`, modelo `{RC.MODEL_E1}`, "
          f"E0 `{resumen['e0']}`.", ""]
    for cid in casos:
        to = cid.split("::")[0]
        chunk = next(c for c in comun_e1.cargar_chunks((to,), e0_dir=man.e0_salida) if c["id"] == cid)
        kw = pf.build_request_kwargs(chunk, model=RC.MODEL_E1)
        canon = cliente_e1.lc.canonical_request(kw)
        nombre = cid.replace("::", "__").replace(":", "_")
        (SAL / f"request_{nombre}.json").write_text(json.dumps(kw, ensure_ascii=False, indent=1) + "\n",
                                                    encoding="utf-8")
        fila = {"chunk_id": cid, "archivo": f"request_{nombre}.json",
                "sha256_system": hashlib.sha256(kw["system"][0]["text"].encode("utf-8")).hexdigest(),
                "sha256_tools": hashlib.sha256(json.dumps(kw["tools"], sort_keys=True, ensure_ascii=False)
                                               .encode("utf-8")).hexdigest(),
                "max_tokens": kw["max_tokens"], "tool_choice": kw["tool_choice"],
                "clave_cache_local": cliente_e1.lc.compute_key(ns, canon)}
        resumen["casos"].append(fila)
        md += [f"## {cid}", "", f"- system sha256 `{fila['sha256_system']}`; tools sha256 `{fila['sha256_tools']}`; "
               f"max_tokens {fila['max_tokens']}; clave `{fila['clave_cache_local']}`.", "",
               "Mensaje de usuario:", "", "```text", kw["messages"][0]["content"], "```", ""]
    (SAL / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (SAL / "requests.md").write_text("\n".join(md), encoding="utf-8")
    print(json.dumps({k: v for k, v in resumen.items() if k != "casos"}, ensure_ascii=False),
          [c["chunk_id"] for c in resumen["casos"]])


if __name__ == "__main__":
    main()
