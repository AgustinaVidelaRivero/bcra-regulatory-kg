"""
estimacion_cobertura_esq2.py — FASE (b) de U-ESQ-2: estimación anclada ($0)
de la extracción E1-solo de las 762 unidades de los 10 TOs, contra el tope
USD 6,50 (laudo ESQ-2 §1.i).

Anclaje en medición real (usage de producción): los factores por unidad se
recomputan sobre las 1.769 líneas con usage de los cinco jsonl de la corrida
cerrada de producción (comun_control_esq.factores_produccion, mismo alcance
que el comando sellado del scoping §5.2 — decisión D-f de U-ESQ-1c):

  t_in   = input tokens no cacheados por unidad (el mensaje de usuario)
  t_out  = output tokens por unidad
  t_cr   = cache read por unidad (lectura del prefijo cacheado)
  pref   = tokens del prefijo por escritura (cache_write // n_escrituras)
  n_escr = escrituras de prefijo observadas en producción (expiraciones TTL)

Ajuste por tamaño (declarado): los chunks de los 10 TOs no son los del subset;
t_in y t_out se escalan por el cociente de chars REALES del mensaje de usuario
(prompt_e1.build_user_message, función pura) entre el corpus ESQ-2 y el de
producción. Para t_out el escalado se aplica solo si agranda (cota
conservadora: la salida no se supone más barata por mensajes más cortos).
t_cr no se escala (el prefijo es constante).

Aritmética a la vista (fórmula D2, decisiones_caching_extraccion.md:32-42):
  costo = 762 × (t_in_adj×P_in + t_out_adj×P_out + t_cr×P_cr)/1e6
        + n_escr_est × pref × P_cw/1e6
Tarifas: MODEL_E1 y P_E1 verbatim de
data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py:76-78
(claude-haiku-4-5 — 1,00 / 5,00 / 1,25 / 0,10 USD/MTok).

Salida: cobertura/estimacion_cobertura_esq2.json + .md.
Uso:  .venv/bin/python3 -B data/experiment/esq/code/estimacion_cobertura_esq2.py
"""

from __future__ import annotations

import json
import math
import sys
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_cobertura_esq2 as cc      # noqa: E402
import comun_control_esq as ctrl       # noqa: E402  (factores de producción)
import comun_e1                        # noqa: E402
import prompt_e1                       # noqa: E402


def chars_mensajes(chunks: list[dict]) -> dict:
    """Chars reales del mensaje de usuario por chunk (función pura del chunk:
    lo que efectivamente viaja después del breakpoint)."""
    largos = [len(prompt_e1.build_user_message(c)) for c in chunks]
    return {"n": len(largos), "total_chars": sum(largos),
            "media_chars": sum(largos) / len(largos)}


def main() -> int:
    # --- anclas medidas (producción, 1.769 usages) ---
    f = ctrl.factores_produccion()
    agg = f["agg"]

    # --- chars reales de mensajes: producción vs ESQ-2 ---
    chunks_prod = comun_e1.cargar_chunks(comun_e1.TOS,
                                         e0_dir=comun_e1.E0_SALIDA_ENM01)
    chunks_esq2 = cc.cargar_chunks_esq2()
    m_prod = chars_mensajes(chunks_prod)
    m_esq2 = chars_mensajes(chunks_esq2)
    ratio = m_esq2["media_chars"] / m_prod["media_chars"]

    n = len(chunks_esq2)
    p = cc.P_E1
    t_in_adj = f["t_in"] * ratio
    t_out_adj = f["t_out"] * max(1.0, ratio)   # cota conservadora
    t_cr = f["t_cr"]

    marginal_u = (t_in_adj * p["precio_in_por_mtok"]
                  + t_out_adj * p["precio_out_por_mtok"]
                  + t_cr * p["precio_cache_read_por_mtok"]) / 1e6
    costo_marginal = n * marginal_u

    # Escrituras de prefijo: tasa observada en producción (expiraciones TTL
    # del prompt cache en corrida secuencial), aplicada a 762 llamadas, con
    # piso 1 y redondeo hacia arriba.
    tasa_escr = agg["n_escrituras"] / agg["n"]
    n_escr_est = max(1, math.ceil(tasa_escr * n))
    costo_escrituras = n_escr_est * f["pref_tok"] * p["precio_cache_write_por_mtok"] / 1e6

    estimado = costo_marginal + costo_escrituras
    margen = 1.2   # margen declarado sobre la estimación (reintentos de API,
                   # variación de salida); el freno real es el tope duro
    estimado_con_margen = estimado * margen

    doc = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "modelo": cc.MODEL_E1,
        "tarifas_usd_mtok": {**p, "ancla": "reextraccion_v2/corpus_v2/runner_corpus.py:76-78"},
        "anclas_produccion": {
            "fuente": ("comun_control_esq.factores_produccion() sobre los 5 "
                       "jsonl de corpus_v2/salida/*/extracciones_e1.jsonl "
                       "(1.769 usages; scoping §5.2, decisión D-f)"),
            "n_usages": agg["n"],
            "t_in_tok_u": round(f["t_in"], 2),
            "t_out_tok_u": round(f["t_out"], 2),
            "t_cr_tok_u": round(f["t_cr"], 2),
            "pref_tok_escritura": f["pref_tok"],
            "n_escrituras_produccion": agg["n_escrituras"],
            "r_marg_usd_u": round(f["r_marg"], 8),
        },
        "ajuste_tamano": {
            "media_chars_msg_produccion": round(m_prod["media_chars"], 1),
            "media_chars_msg_esq2": round(m_esq2["media_chars"], 1),
            "ratio": round(ratio, 4),
            "regla": ("t_in × ratio; t_out × max(1, ratio) — cota "
                      "conservadora; t_cr sin escalar (prefijo constante)"),
        },
        "aritmetica": {
            "n_unidades": n,
            "t_in_adj_tok_u": round(t_in_adj, 2),
            "t_out_adj_tok_u": round(t_out_adj, 2),
            "marginal_usd_u": round(marginal_u, 8),
            "costo_marginal_usd": round(costo_marginal, 4),
            "tasa_escrituras_produccion": round(tasa_escr, 5),
            "n_escrituras_estimadas": n_escr_est,
            "costo_escrituras_usd": round(costo_escrituras, 4),
            "formula": ("762 × (t_in_adj×1,00 + t_out_adj×5,00 + t_cr×0,10)/1e6 "
                        "+ n_escr × pref × 1,25/1e6  (fórmula D2, "
                        "decisiones_caching_extraccion.md:32-42)"),
        },
        "estimado_usd": round(estimado, 4),
        "margen_declarado": margen,
        "estimado_con_margen_usd": round(estimado_con_margen, 4),
        "tope_usd": cc.TOPE_USD,
        "estimacion_gruesa_laudo_usd": 5.5,
        "cabe_en_tope": estimado_con_margen <= cc.TOPE_USD,
    }
    cc.COBERTURA_DIR.mkdir(parents=True, exist_ok=True)
    (cc.COBERTURA_DIR / "estimacion_cobertura_esq2.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

    md = f"""# Estimación anclada — extracción E1-solo ESQ-2 (762 unidades)

Generado: {doc['generado']} · Modelo: {cc.MODEL_E1} · Tarifas:
1,00 / 5,00 / 1,25 / 0,10 USD/MTok (`runner_corpus.py:76-78`).

## Anclas (producción, {agg['n']} usages reales)

| factor | valor |
|---|---|
| t_in (tok/u) | {f['t_in']:.2f} |
| t_out (tok/u) | {f['t_out']:.2f} |
| t_cr (tok/u) | {f['t_cr']:.2f} |
| prefijo (tok/escritura) | {f['pref_tok']} |
| escrituras en producción | {agg['n_escrituras']} de {agg['n']} llamadas |

## Ajuste por tamaño (chars reales del mensaje de usuario)

media producción {m_prod['media_chars']:.0f} chars → media ESQ-2
{m_esq2['media_chars']:.0f} chars → **ratio {ratio:.4f}**.
t_in × ratio; t_out × max(1, ratio) (cota conservadora); t_cr sin escalar.

## Aritmética (fórmula D2)

- marginal/u = ({t_in_adj:.1f}×1,00 + {t_out_adj:.1f}×5,00 + {t_cr:.1f}×0,10)/1e6
  = USD {marginal_u:.6f}
- 762 × marginal/u = **USD {costo_marginal:.4f}**
- escrituras: tasa producción {tasa_escr:.5f} × 762 → {n_escr_est} escrituras
  × {f['pref_tok']} tok × 1,25/1e6 = **USD {costo_escrituras:.4f}**

## Resultado

| | USD |
|---|---|
| estimado | **{estimado:.4f}** |
| estimado × margen {margen} | **{estimado_con_margen:.4f}** |
| estimación gruesa del laudo | 5,50 |
| tope duro de la unidad | {cc.TOPE_USD:.2f} |

Cabe en el tope: **{'SÍ' if doc['cabe_en_tope'] else 'NO'}**.
El freno real durante el gasto es el tope duro cableado en el cliente
(proyección pre-llamada) más el chequeo de proyección por TO del runner.
"""
    (cc.COBERTURA_DIR / "estimacion_cobertura_esq2.md").write_text(
        md, encoding="utf-8")

    print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
