"""
verificar_reexaminaciones_f2.py — U-ESQ-V3 fase 2: verificación INDEPENDIENTE
de las dos re-examinaciones del laudo (a) antes de aplicarlas.

El laudo ordena verificarlas contra los artefactos y NO aplicarlas si no
reproducen. Este script reúne la evidencia de cada una —definición y alias
del catálogo v3 sellado, pasaje completo de e0_dry, y las demás unidades del
mismo TO que tocan la distinción en juego— y recomputa el resultado de la
adjudicación bajo las dos alternativas, para que la diferencia se vea en
número y no en prosa.

No escribe miembros ni toca artefacto alguno: solo lee y reporta. USD 0.

Uso:  python3 verificar_reexaminaciones_f2.py [--out DIR]
Escribe: verificacion_reexaminaciones_f2.md
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import comun_v3m as C

CASOS = {
    "ctacor": {
        "colectivo": "Entidades financieras del país",
        "candidato": "Sujeto_entidad_financiera",
        "tesis_del_laudo": ("«del país» es calificador redundante porque la definición del "
                            "catálogo es doméstica por construcción — reclasificar a `identico`"),
        "unidades_a_mostrar": ["1.1", "1.4"],
        "veredicto": "NO_REPRODUCE",
        "hallazgo": [
            "**El ancla del laudo es exacta**: `prompt_v3_b54.py:117` dice literalmente «ES el "
            "intermediario AUTORIZADO POR EL BCRA a operar bajo la Ley de Entidades Financieras». "
            "La cita se verificó carácter por carácter.",
            "**Pero la definición no es la única parte de la entrada.** La MISMA línea del "
            "catálogo declara, entre sus alias, «Entidades financieras del exterior» y «Entidad "
            "financiera del exterior». El catálogo v3 **no tiene id separado para la entidad "
            "financiera del exterior**: la manda por alias a este mismo id. Ese es el patrón "
            "general del catálogo para lo extranjero — `Sujeto_banco` lleva el alias «Bancos del "
            "exterior» y `Sujeto_entidad_cambiaria` el alias «Compañía cambista del exterior». "
            "El `Sujeto_banco_central_del_exterior` que el laudo cita como prueba de que lo "
            "extranjero tiene id propio es el banco CENTRAL de otro estado, no una entidad "
            "financiera del exterior.",
            "Es decir: en el catálogo v3, `Sujeto_entidad_financiera` es la UNIÓN de las "
            "domésticas y las del exterior, y hay contradicción interna entre su `def` "
            "(doméstica) y sus `alias` (incluyen lo extranjero). Bajo el uso efectivo —el alias "
            "es lo que gobierna a qué id cae una mención—, «del país» es subconjunto PROPIO.",
            "**Y el propio TO lo confirma, que es la evidencia decisiva.** `ctacor::1.1` no usa "
            "«del país» como muletilla: lo contrasta en el mismo párrafo con «entidades "
            "financieras del país **y del exterior**», y el documento dedica una unidad entera, "
            "`ctacor::1.4`, titulada «Entidades financieras del exterior.». La Sección 1 regula "
            "la corresponsalía LOCAL («para la realización de transacciones locales admitidas») "
            "y las entidades del exterior se tratan aparte. «Del país» es el recorte que "
            "estructura el documento.",
            "**Consecuencia bajo el criterio del propio laudo (a):** con "
            "`Sujeto_entidad_financiera` como miembro, la regla de herencia 2 haría que el grafo "
            "afirme que las normas de corresponsalía local alcanzan también a las entidades "
            "financieras del exterior — exactamente lo que la Sección 1 excluye. Es el mismo "
            "vicio que el laudo manda retirar en las otras seis filas.",
            "**ctacor NO queda huérfano por esto**: conserva `Sujeto_casa_de_cambio`, que ya "
            "tenía por recorte declarado («Casas de cambio (Sección 3)»). Su situación es la de "
            "`depaho`: fila rechazada, rol con miembro.",
        ],
    },
    "convca": {
        "colectivo": "Entidades financieras y otras habilitadas a conversión cambiaria",
        "candidato": "Sujeto_entidad_financiera",
        "tesis_del_laudo": ("no es aplanamiento sino enumeración parcial: las EF pertenecen al "
                            "colectivo sin condición y lo que falta son las «otras», que no "
                            "tienen id — omisión con residuo declarado"),
        "unidades_a_mostrar": ["1.1"],
        "veredicto": "REPRODUCE",
        "hallazgo": [
            "El pasaje dice literalmente «a solicitud de las **entidades financieras y otras "
            "habilitadas**». Bajo la lectura llana son dos colectivos coordinados: las entidades "
            "financieras, sin condición alguna, y unas «otras» que el catálogo no tiene. Eso es "
            "omisión —falta un miembro— y no falsedad: nada de lo que el grafo afirmaría sería "
            "incorrecto. El principio §1 acepta el residuo declarado.",
            "**AMBIGÜEDAD REGISTRADA, no resuelta en silencio** (por instrucción del laudo). El "
            "parseo alternativo «(EF y otras) habilitadas» haría que el calificador alcance "
            "también a las EF, y entonces sería aplanamiento. El argumento más fuerte a su favor "
            "no es sintáctico sino léxico: el «otras» de «otras habilitadas» presupone que las "
            "entidades financieras mencionadas antes también están habilitadas, lo que sugiere "
            "un conjunto «habilitadas» del que las EF son una parte. Se deja escrito porque es "
            "el punto que haría cambiar la adjudicación si algún día se relee.",
            "Se adopta la lectura llana **por laudo de la autora**, no por resolución de esta "
            "unidad. El residuo («otras habilitadas», sin id) va a la lista de residuos "
            "declarados con su texto.",
        ],
    },
}


def _unidades(to: str) -> list[dict]:
    p = C.E0_DRY / to / f"chunks_{to}.json"
    return json.loads(p.read_text(encoding="utf-8"))


def _entrada_catalogo(sid: str) -> tuple[str, str]:
    """Línea del bloque sellado y su línea `def:` (para citar verbatim)."""
    v3 = C.cargar_v3()
    ls = v3.BLOQUE_CATALOGO_V3.split("\n")
    for i, l in enumerate(ls):
        if l.startswith(sid + " — "):
            d = ls[i + 1] if i + 1 < len(ls) and ls[i + 1].startswith("  def:") else ""
            return l, d
    return "", ""


def recomputar(aceptar_ctacor: bool, aceptar_convca: bool) -> dict:
    """Adjudicación bajo los laudos (a) y (b) — sin aplanamiento y sin
    instancias — con los dos rescates como parámetro."""
    d = json.loads((C.UNIDAD / "candidatos_miembros_v3.json").read_text(encoding="utf-8"))
    rescatados = {("ctacor", aceptar_ctacor), ("convca", aceptar_convca)}
    miembros, huerfanos = {}, []
    for r in d["roles"]:
        ms = []
        for c in r["candidatos"]:
            sid = c["candidato_id"]
            if not sid:
                continue
            if c["nivel_candidato"] == "instancia":       # laudo (b)
                continue
            if c["relacion"] == "mas_amplio":             # laudo (a)
                if (r["to"], True) in rescatados and r["to"] in ("ctacor", "convca"):
                    ms.append(sid)                        # rescate verificado
                continue
            ms.append(sid)
        ms = sorted(set(ms))
        miembros[r["to"]] = ms
        if not ms:
            huerfanos.append(r["to"])
    return {"miembros": miembros, "huerfanos": huerfanos,
            "aristas": sum(len(v) for v in miembros.values())}


CAUSAS = {
    "sin_id_en_catalogo": ["autenf", "pfmipyme", "pimf", "repefe", "retype", "traval"],
    "aplanamiento_rechazado": ["adrei", "pagjub", "ratiofn", "rdbcra", "snp_atm"],
    "instancia_rechazada": ["ordcom"],
}


def render() -> str:
    L = [
        "# U-ESQ-V3 fase 2 — Verificación independiente de las dos re-examinaciones",
        "",
        "El laudo (a) ordena verificar contra los artefactos las dos re-examinaciones **antes de "
        "aplicarlas**, y no aplicarlas si no reproducen. Esto es esa verificación.",
        "",
        "| caso | tesis del laudo | veredicto |",
        "|---|---|---|",
    ]
    for to, c in CASOS.items():
        L.append(f"| `{to}` | {c['tesis_del_laudo'][:80]}… | **{c['veredicto']}** |")
    L += [""]
    for to, caso in CASOS.items():
        linea, deff = _entrada_catalogo(caso["candidato"])
        chs = _unidades(to)
        L += [f"## {to} — «{caso['colectivo']}» — **{caso['veredicto']}**", "",
              f"**Tesis del laudo:** {caso['tesis_del_laudo']}.", "",
              f"**Entrada del catálogo v3 sellado para `{caso['candidato']}`** "
              "(línea completa, con sus alias):", "", "```", linea]
        if deff:
            L.append(deff)
        L += ["```", "", "**Pasaje(s) del TO (verbatim de e0_dry, sin editar):**", ""]
        for u in caso["unidades_a_mostrar"]:
            ch = next((c for c in chs if (c.get("unidad") or "") == u), None)
            if ch is None:
                ch = next((c for c in chs if (c.get("unidad") or "").startswith(u + ".")), None)
            if ch:
                L += [f"`{ch['id']}` · página(s) {ch['paginas']} · «{ch['titulo']}»", "",
                      "```", ch["texto"].strip(), "```", ""]
        L += ["**Verificación:**", ""]
        for h in caso["hallazgo"]:
            L += [f"- {h}"]
        L += [""]

    L += ["## Recomputo bajo las cuatro combinaciones", "",
          "Ambos laudos (a) —sin aplanamiento— y (b) —sin instancias— aplicados; los dos rescates "
          "como parámetro. Recomputado por este script sobre `candidatos_miembros_v3.json`.", "",
          "| ctacor rescatado | convca rescatado | aristas `miembro_de` | roles huérfanos |",
          "|---|---|---:|---:|"]
    for a in (True, False):
        for b in (True, False):
            r = recomputar(a, b)
            marca = ""
            if a and b:
                marca = "  ← lo que el laudo predice"
            if not a and b:
                marca = "  ← **lo que la verificación sostiene**"
            L.append(f"| {'SÍ' if a else 'NO'} | {'SÍ' if b else 'NO'} | {r['aristas']} | "
                     f"{len(r['huerfanos'])}{marca} |")
    r = recomputar(False, True)
    L += ["",
          "## Resultado verificado y su distancia con el laudo", "",
          f"**{r['aristas']} aristas `miembro_de` · {len(r['huerfanos'])} roles huérfanos.**",
          "",
          "Los **12 huérfanos y su descomposición por causa (6 / 5 / 1) coinciden exactamente** "
          "con lo laudado. La única diferencia es de **una arista**: la de `ctacor`, cuyo rescate "
          "no reproduce. El laudo predice 35; la verificación sostiene 34.",
          "",
          "| causa | n | roles |",
          "|---|---:|---|"]
    for k, v in CAUSAS.items():
        L.append(f"| `{k}` | {len(v)} | {', '.join(v)} |")
    L += [f"| **total** | **{sum(len(v) for v in CAUSAS.values())}** | |", "",
          "Control: la lista de causas reproduce la lista de huérfanos medida — "
          f"{sorted(sum(CAUSAS.values(), [])) == sorted(r['huerfanos'])}.",
          "",
          "`ctacor` NO figura entre los huérfanos: conserva `Sujeto_casa_de_cambio`. "
          "Estar en la lista de filas rechazadas y estar en la de excepciones son cosas "
          "distintas, como el propio laudo advierte para `depaho`.",
          ""]
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=C.UNIDAD)
    args = ap.parse_args()
    (args.out / "verificacion_reexaminaciones_f2.md").write_text(render(), encoding="utf-8")
    for a in (True, False):
        for b in (True, False):
            r = recomputar(a, b)
            print(f"  ctacor={'SÍ' if a else 'NO'} convca={'SÍ' if b else 'NO'} -> "
                  f"aristas={r['aristas']:3d}  huérfanos={len(r['huerfanos']):2d}")
    r = recomputar(False, True)
    print(f"\nVERIFICADO: {r['aristas']} aristas / {len(r['huerfanos'])} huérfanos "
          f"(el laudo predice 35 / 12)")
    print(f"causas reproducen la lista medida: "
          f"{sorted(sum(CAUSAS.values(), [])) == sorted(r['huerfanos'])}")
    print(f"-> {args.out / 'verificacion_reexaminaciones_f2.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
