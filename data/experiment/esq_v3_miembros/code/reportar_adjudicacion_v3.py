"""
reportar_adjudicacion_v3.py — U-ESQ-V3 fase 2: rinde la adjudicación en dos
artefactos legibles.

  tabla_adjudicacion_final_v3.md  — las 69 filas con su decisión y su
      fundamento, más la lista de excepciones de S15 con su causa y su
      remedio, y los conteos recomputados contra el JSON.
  residuos_declarados_v3.md       — todo lo que el recurso NO afirma y por
      qué: los 26 colectivos sin id, las «otras habilitadas» de convca con
      su ambigüedad registrada y su chequeo de anidación, y los 2 candidatos
      de nivel instancia rechazados con su motivo.

Nada de esto decide: rinde lo que adjudicar_miembros_v3.py ya resolvió con
los laudos. USD 0.

Uso:  python3 reportar_adjudicacion_v3.py [--out DIR]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import comun_v3m as C

# Chequeo ordenado por el laudo §3 antes de escribir el residuo de convca.
ANCLAJE_CONVCA = {
    "pregunta": ("¿alguna norma del corpus establece que las entidades financieras DEBEN "
                 "mantener cuenta corriente en el BCRA? De eso depende si el colectivo "
                 "operativo del TO —«titulares de cuenta corriente en este Banco Central»— "
                 "contiene al colectivo EF, y por lo tanto si la arista es segura."),
    "rama": "SÍ EXISTE",
    "ancla": "ccbcra::1.1",
    "verbatim": ("Las entidades financieras deberán mantener abierta en el Banco Central de la "
                 "República Argentina una cuenta corriente en pesos. Dicha cuenta tendrá "
                 "carácter optativo para las cajas de crédito (Ley 25.782) y las entidades "
                 "cambiarias."),
    "criterio_operativo_del_to": [
        ("convca::1.1", "sus cuentas corrientes abiertas en el Banco Central"),
        ("convca::2.1.3", "Los titulares de cuentas corrientes en este Banco Central"),
    ],
}


def _corto(s: str, n: int) -> str:
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 1] + "…"


def tabla_md(a: dict) -> str:
    k = a["conteos"]
    L = [
        "# U-ESQ-V3 fase 2 — Adjudicación FINAL de los miembros de los 30 roles v3",
        "",
        "Los laudos aplicados fila por fila. Cada decisión lleva su fundamento; ninguna se "
        "resolvió por conveniencia del número.",
        "",
        f"**{k['aristas_miembro_de']} aristas `miembro_de` · {k['roles_huerfanos']} roles sin "
        f"miembro adjudicable ({' / '.join(f'{v} {kk}' for kk, v in k['por_causa'].items())}).**",
        "",
        "Filas por decisión, recomputadas contra `adjudicacion_final_v3.json`: "
        + " · ".join(f"`{d}` {n}" for d, n in k["filas_por_decision"].items())
        + f" · **total {sum(k['filas_por_decision'].values())}**.",
        "",
        "## Las 69 filas",
        "",
        "| # | TO | rol_id | colectivo que el pasaje nombra | id | decisión | fundamento |",
        "|---:|---|---|---|---|---|---|",
    ]
    i = 0
    for r in a["roles"]:
        for j, f in enumerate(r["filas"]):
            i += 1
            sid = f"`{f['candidato_id']}`" if f["candidato_id"] else "—"
            marca = "✔" if f["decision"].startswith("aceptado") else "✘"
            L.append(
                f"| {i} | {r['to'] if j == 0 else ''} | "
                f"{'`' + r['id'] + '`' if j == 0 else ''} | {_corto(f['colectivo'], 80)} | "
                f"{sid} | {marca} `{f['decision']}` | {_corto(f['fundamento'], 200)} |")
    L += ["", "## Los 30 roles y sus miembros", "",
          "| TO | rol_id | miembros | cita |", "|---|---|---|---|"]
    for r in a["roles"]:
        ms = "<br>".join(f"`{m}`" for m in r["miembros"]) or \
             f"**— sin miembro adjudicable** (`{r.get('causa_sin_miembro')}`)"
        L.append(f"| {r['to']} | `{r['id']}` | {ms} | `{r['cita_chunk_id']}` |")
    L += ["", "## Lista declarada de excepciones de S15", "",
          "Doce roles, tres deudas distintas con tres remedios distintos. No se agrupan: una "
          "lista sin causa dice cuántos faltan, no qué hacer para achicarla.", ""]
    for causa, roles in a["conteos"]["roles_por_causa"].items():
        ex = [e for e in a["excepciones"] if e["causa"] == causa]
        L += [f"### `{causa}` — {len(roles)} roles", "",
              f"**Remedio:** {ex[0]['remedio'] if ex else '—'}", "",
              "| TO | rol_id | colectivo(s) que el pasaje nombra |", "|---|---|---|"]
        for e in ex:
            L.append(f"| {e['to']} | `{e['rol_id']}` | "
                     + "<br>".join(_corto(c, 90) for c in e["colectivos"]) + " |")
        L.append("")
    return "\n".join(L) + "\n"


def residuos_md(a: dict) -> str:
    sin_id = [(r, f) for r in a["roles"] for f in r["filas"]
              if f["decision"] == "sin_id_en_catalogo"]
    inst = [(r, f) for r in a["roles"] for f in r["filas"]
            if f["decision"] == "rechazado_instancia"]
    apl = [(r, f) for r in a["roles"] for f in r["filas"]
           if f["decision"] == "rechazado_aplanamiento"]
    ac = ANCLAJE_CONVCA
    L = [
        "# U-ESQ-V3 — RESIDUOS DECLARADOS",
        "",
        "Lo que el recurso **no** afirma, y por qué. El principio §1 del laudo del esquema "
        "congelado acepta la omisión con residuo declarado y manda retirar la falsedad; esto es "
        "el registro de las omisiones que esa regla produjo.",
        "",
        f"**{len(sin_id)}** colectivos sin id en el catálogo · **{len(apl)}** filas rechazadas "
        f"por aplanamiento · **{len(inst)}** candidatos de nivel instancia rechazados · "
        "**1** enumeración parcial aceptada con su faltante.",
        "",
        "## 1. Los 26 colectivos que el pasaje nombra y el catálogo v3 no tiene",
        "",
        "El matcheo no sube al padre: hacerlo sería colapsar a la madre. **Remedio: abrir id, "
        "que es re-sello del prefijo v3 y unidad propia.**",
        "",
        "| # | TO | colectivo |", "|---:|---|---|",
    ]
    for n, (r, f) in enumerate(sin_id, 1):
        L.append(f"| {n} | {r['to']} | {_corto(f['colectivo'], 100)} |")

    L += ["", "## 2. Las 7 filas rechazadas por aplanamiento (laudo (a))", "",
          "Su candidato era la clase madre del colectivo. Adoptarlo habría hecho que el grafo "
          "afirme la norma sobre toda la clase y, por la regla 1, sobre cada subclase. "
          "**Remedio: una clase más específica en el catálogo.**", "",
          "| TO | colectivo | clase madre descartada |", "|---|---|---|"]
    for r, f in apl:
        L.append(f"| {r['to']} | {_corto(f['colectivo'], 85)} | `{f['candidato_id']}` |")
    L += ["",
          "`ctacor` y `depaho` figuran acá y **no** en la lista de excepciones de S15: conservan "
          "otro miembro. Estar en la lista de filas rechazadas y estar en la de excepciones son "
          "cosas distintas.", ""]

    L += ["## 3. Los 2 candidatos de nivel instancia rechazados (laudo (b))", "",
          "`miembro_de` es Clase → Rol. Admitir una instancia cambia la firma del esquema "
          "congelado, que es laudo de la autora y jamás efecto de esta unidad. **Costo asumido y "
          "declarado: `ordcom` queda sin miembro; `fabcra` sobrevive con los suyos.**", "",
          "| TO | colectivo | id descartado | nivel |", "|---|---|---|---|"]
    for r, f in inst:
        L.append(f"| {r['to']} | {_corto(f['colectivo'], 60)} | `{f['candidato_id']}` | "
                 f"{f['nivel_candidato']} |")

    L += ["", "## 4. `convca` — la enumeración parcial y lo que le falta", "",
          "El pasaje (`convca::1.1`) dice «a solicitud de las **entidades financieras y otras "
          "habilitadas**». `Sujeto_entidad_financiera` entra como miembro por la lectura llana, "
          "laudada. **Lo que falta: las «otras habilitadas», que no tienen id en el catálogo v3.**",
          "",
          "### Ambigüedad REGISTRADA, no resuelta en silencio",
          "",
          "Bajo el parseo alternativo «(EF y otras) habilitadas» el calificador alcanzaría también "
          "a las entidades financieras y volvería a ser aplanamiento. El argumento más fuerte a "
          "su favor no es sintáctico sino léxico: el «otras» de «otras habilitadas» presupone que "
          "las EF mencionadas antes también están habilitadas, lo que sugiere un conjunto "
          "«habilitadas» del que las EF serían una parte. **Se adopta la lectura llana por laudo "
          "de la autora, no por resolución de esta unidad**, y se deja escrito porque es el punto "
          "que haría cambiar la adjudicación si algún día se relee. Verificado además que el TO "
          "no la resuelve: ninguna de sus 13 unidades enumera las «otras habilitadas» ni declara "
          "que todas las EF lo estén.",
          "",
          "### Chequeo de anidación ordenado antes de escribir este residuo",
          "",
          f"**Pregunta:** {ac['pregunta']}",
          "",
          "El criterio operativo que el propio TO usa no es «entidad financiera» sino ser titular "
          "de cuenta corriente en el BCRA:",
          ""]
    for cid, txt in ac["criterio_operativo_del_to"]:
        L.append(f"- `{cid}`: «{txt}»")
    L += ["",
          f"**Rama verificada: {ac['rama']}.** El corpus sí trae esa norma, en `{ac['ancla']}`:",
          "", "```", ac["verbatim"], "```", "",
          "Los conjuntos se anidan y **la arista es segura**: la obligación de mantener cuenta "
          "corriente en el BCRA recae sobre las entidades financieras por norma expresa, de modo "
          "que el colectivo operativo del TO contiene al colectivo EF. El residuo se escribe "
          "entonces como **aproximación con anclaje**: el recurso afirma la norma sobre las "
          "entidades financieras, que es un subconjunto veraz del colectivo operativo; lo que no "
          "afirma es el resto de ese colectivo.",
          "",
          "**Matiz que la propia norma introduce y que no se absorbe:** la misma cláusula dice "
          "que la cuenta «tendrá carácter optativo para las cajas de crédito (Ley 25.782) y las "
          "entidades cambiarias». Las cajas de crédito de la Ley 25.782 **son** entidades "
          "financieras según el catálogo (`Sujeto_caja_de_credito`: «ES la entidad financiera "
          "“caja de crédito” de la Ley 25.782»), de modo que la anidación EF ⊆ titulares "
          "**no es estricta**: hay un subconjunto de entidades financieras para el que la "
          "titularidad es optativa. La arista se mantiene —la regla general es la obligación— "
          "pero la excepción queda escrita, y no se afirma «toda EF es titular por construcción», "
          "que es la forma de argumento que ya falló en `ctacor`.",
          ""]
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=C.UNIDAD)
    args = ap.parse_args()
    a = json.loads((C.UNIDAD / "adjudicacion_final_v3.json").read_text(encoding="utf-8"))
    (args.out / "tabla_adjudicacion_final_v3.md").write_text(tabla_md(a), encoding="utf-8")
    (args.out / "residuos_declarados_v3.md").write_text(residuos_md(a), encoding="utf-8")
    print(f"-> {args.out / 'tabla_adjudicacion_final_v3.md'}")
    print(f"-> {args.out / 'residuos_declarados_v3.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
