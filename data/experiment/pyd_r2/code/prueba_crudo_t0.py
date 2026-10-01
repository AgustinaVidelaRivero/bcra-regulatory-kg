"""
prueba_crudo_t0.py — U-PYD, etapa P2 (b) y (c): corrida del validador r2 sobre
el crudo guardado de r1 y de la tanda 0 (grupos r1, desarrollo, cinco, diez;
capas L0 y L0r), con los controles de reproducción.

Escribe resultados/prueba_crudo_t0.json y .md (o en --salida). Salida
determinística, sin fechas ni rutas absolutas: dos corridas dan los mismos bytes.

Controles (mandato U-PYD, P2 c):
  C1  los valores fuera de lista del crudo, contados con la regla de N1
      (u_listas_n1.contar, importado sin editar), coinciden con N1
      (grupos.<g>.capas.<capa>.fuera y resumen_por_lista); la reconciliación
      lleva cada valor de N1 a su tratamiento r2 y lista aparte lo que cambia
      por las listas r2;
  C2  las relaciones que solo valen por la matriz ampliada (marca
      no_verificada_e3), en la primera pasada, coinciden con la columna A de
      U-ESTUDIO-MATRIZ (P01, P02); y se reconcilian con la columna B (434 y 263
      en diez, tablero de correcciones [c19]) unidad por unidad, con la población
      final de U-ESTUDIO-MATRIZ;
  C3  ningún elemento que el validador v3 aceptaba se pierde: v3 aceptado ⊆ r2
      aceptado, por índice, en L0 (validación guardada, re-verificada) y en L0r
      (validador v3 re-corrido); las omisiones v3 se conservan.
  C4  (informativo) las relaciones con la marca `incoherente` de BKL-0038 en la
      población final de la tanda 0 contra las del grafo ensamblado (desarrollo
      y diez), que L-ESQ-R2 §1.1 cita como 4.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/pyd_r2/code/prueba_crudo_t0.py
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))
import modelos_r2 as M  # noqa: E402
import validador_r2 as V  # noqa: E402
import lector_crudo_v3 as L  # noqa: E402

REPO = M.REPO
SALIDA = M.PYD_R2 / "resultados"
COMANDO = "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/pyd_r2/code/prueba_crudo_t0.py"

N1_SCRIPT = "reports/u_listas_nomap/u_listas_n1.py"
N1_SCRIPT_SHA = "6b1b991a26ed1c04950c4f4c989caac05f0ba57b9477eccd837e74552c4c8b69"
POBLACION_FINAL = "reports/u_estudio_matriz/uestmat_poblacion_final.json"
POBLACION_FINAL_SHA = "299c45211bcf714d47d297861e1c8c5ea83305c4ebf5b3b25bdca2a604a89b7c"
REPORTE_MATRIZ = "reports/u_estudio_matriz/uestmat_reporte_U-ESTUDIO-MATRIZ.md"
REPORTE_MATRIZ_SHA = "ee864b34f2ed1f440dba738e9a385b35ae896a7c7f487bedb50858c130853b0f"
# Tabla del punto 1 de U-ESTUDIO-MATRIZ (7e72051), filas P01 y P02: (diez, desarrollo).
ESPERADO_A = {"Operacion": (424, 383), "Potestad": (231, 208)}
ESPERADO_B = {"Operacion": (434, 388), "Potestad": (263, 239)}
FILAS_REPORTE = ("| P01 | condicion_de: rango+Operacion | 424 / 383 | 434 / 388 |",
                 "| P02 | condicion_de: rango+Potestad | 231 / 208 | 263 / 239 |")
CAMPOS_N1 = ("tipo_entidad", "predicado", "sujeto_id", "Obligacion.tipo", "Restriccion.tipo",
             "Comunicacion.tipo", "claves")
CAPA_N1 = {"L0": "crudo", "L0r": "reintentos_crudo"}
RESUMEN_N1 = {"L0": "fuera_crudo", "L0r": "fuera_reintentos_crudo"}


def importar_n1():
    p = REPO / N1_SCRIPT
    s = hashlib.sha256(p.read_bytes()).hexdigest()
    firmado = L.sha256_bytes(L.git_show(L.COMMIT_MANDATO, N1_SCRIPT))
    if s != N1_SCRIPT_SHA or firmado != N1_SCRIPT_SHA:
        raise L.FrenoLectura(f"{N1_SCRIPT}: sha del árbol {s[:12]}…, en {L.COMMIT_MANDATO} {firmado[:12]}…, "
                             f"esperado {N1_SCRIPT_SHA[:12]}…")
    sys.path.insert(0, str(p.parent))
    import u_listas_n1 as N1  # noqa: PLC0415 — se importa sin editar
    return N1


def _sumar(dst: dict, src: dict) -> None:
    for k, v in src.items():
        if isinstance(v, dict):
            _sumar(dst.setdefault(k, {}), v)
        else:
            dst[k] = dst.get(k, 0) + v


def _ordenar(d):
    if isinstance(d, dict):
        return {k: _ordenar(d[k]) for k in sorted(d)}
    return d


def _indices(rechazos: list, n_ent: int, n_rel: int) -> tuple[set, set]:
    """Índices aceptados (entidades, relaciones) desde la lista de rechazos,
    con la misma lectura que N1 (u_listas_n1.indices_rechazados)."""
    ent_r, rel_r, chunk = set(), set(), False
    for r in rechazos or []:
        if r.get("nivel") == "chunk":
            chunk = True
            continue
        m = re.match(r"(entities|relations)\[(\d+)\]", r.get("detalle") or "")
        if m:
            (ent_r if m.group(1) == "entities" else rel_r).add(int(m.group(2)))
    if chunk:
        return set(), set()
    return set(range(n_ent)) - ent_r, set(range(n_rel)) - rel_r


def _motivos(rechazos: list) -> tuple[dict, dict, str | None]:
    ent, rel, chunk = {}, {}, None
    for r in rechazos or []:
        if r.get("nivel") == "chunk":
            chunk = r.get("motivo")
            continue
        m = re.match(r"(entities|relations)\[(\d+)\]", r.get("detalle") or "")
        if m:
            (ent if m.group(1) == "entities" else rel).setdefault(int(m.group(2)), r.get("motivo"))
    return ent, rel, chunk


def _largos(ti) -> tuple[int, int]:
    if isinstance(ti, str):
        try:
            ti = json.loads(ti)
        except json.JSONDecodeError:
            return 0, 0
    if not isinstance(ti, dict):
        return 0, 0
    e, r = V._coerce_lista(ti.get("entities")), V._coerce_lista(ti.get("relations"))
    if e is None or r is None:
        return 0, 0
    return len(e), len(r)


def correr() -> dict:
    N1 = importar_n1()
    import perfil_e1  # noqa: PLC0415 — en el path vía N1
    import validador_e1  # noqa: PLC0415
    esquemas = {"r1": None, "t0": perfil_e1.perfil("v3_b54").esquema}
    listas_n1 = N1.listas_v3(perfil_e1.perfil("v3_b54"))
    crudo = L.Crudo()
    pol = V.politica_default()
    n1 = crudo.n1
    pf = json.loads(L.leer_firmado(L.COMMIT_MANDATO, POBLACION_FINAL, POBLACION_FINAL_SHA).decode("utf-8"))
    rep = L.leer_firmado(L.COMMIT_MANDATO, REPORTE_MATRIZ, REPORTE_MATRIZ_SHA).decode("utf-8")
    filas_rep_ok = all(f in rep for f in FILAS_REPORTE)

    grupos: dict = OrderedDict()
    controles: dict = OrderedDict()
    c1 = OrderedDict()
    c3 = OrderedDict()
    reconc = []
    nuevas_por_unidad: dict = {}      # (capa, chunk_id u origen) → Counter(tipo_target)
    incoherentes = []
    inc_t0 = []
    for g, cfg in L.GRUPOS.items():
        gen = cfg["gen"]
        grupos[g] = OrderedDict()
        for capa in ("L0", "L0r"):
            regs = crudo.registros(g, capa)
            ag = {"registros": len(regs), "metricas": {}, "contadores": {}, "valores": {},
                  "adaptacion_v3": {}, "rechazos_por_motivo": {}}
            fuera_n1 = {k: Counter() for k in CAMPOS_N1}
            perdidos, ganados = [], Counter()
            omis_v3, omis_r2 = 0, 0
            reproduce_v3 = Counter()
            recuperadas = Counter()
            pend = Counter()
            for reg in regs:
                ch = crudo.chunks[reg["chunk_id"]]
                ti = reg["tool_input"]
                res = V.validar(ti, ch, pol, forma="v3")
                _sumar(ag["contadores"], res["contadores"])
                _sumar(ag["valores"], res["valores"])
                _sumar(ag["adaptacion_v3"], res["adaptacion_v3"])
                _sumar(ag["rechazos_por_motivo"], res["metricas"]["rechazos_por_motivo"])
                _sumar(ag["metricas"], {k: v for k, v in res["metricas"].items() if isinstance(v, int)})
                for p in res["pendientes_no_mapeados"]:
                    pend[p["motivo"]] += 1
                n_nuevas = Counter(x["tipo_target"] for x in res["relaciones"] if x["no_verificada_e3"])
                recuperadas.update(n_nuevas)
                if g in ("r1", "diez"):
                    nuevas_por_unidad[(gen, capa, reg["chunk_id"] if capa == "L0" else reg["origen"])] = n_nuevas
                for x in res["relaciones"]:
                    if x.get("coherencia_tipo_predicado") == "incoherente" and g == "diez":
                        inc_t0.append((capa, reg["chunk_id"], reg["origen"]))
                    if x.get("coherencia_tipo_predicado") == "incoherente" and g in ("r1", "diez"):
                        src = next(e for e in res["entidades"] if e["local_id"] == x["source"])
                        incoherentes.append({"grupo": g, "capa": capa, "chunk_id": reg["chunk_id"],
                                             "indice_relacion": x["indice_crudo"], "predicado": x["predicate"],
                                             "restriccion_tipo": src["properties"].get("tipo"),
                                             "restriccion_label": src["label"]})
                # C1: conteo de N1 sobre el mismo crudo.
                E, R, _ = N1.elementos_crudo(ti)
                _, f, _ = N1.contar(E, R, listas_n1, True)
                for k in CAMPOS_N1:
                    fuera_n1[k].update(f[k])
                # C3: aceptados por v3 ⊆ aceptados por r2.
                if capa == "L0":
                    val3 = reg["validacion_v3"]
                    re3 = validador_e1.validar_salida(ti, ch, esquema=esquemas[gen]).as_dict()
                    reproduce_v3["igual" if re3 == val3 else "distinta"] += 1
                else:
                    val3 = validador_e1.validar_salida(ti, ch, esquema=esquemas[gen]).as_dict()
                ne, nr = _largos(ti)
                a3e, a3r = _indices(val3.get("rechazos"), ne, nr)
                a2e, a2r = _indices(res["rechazos"], ne, nr)
                m3e, m3r, m3c = _motivos(val3.get("rechazos"))
                for i in sorted(a3e - a2e):
                    perdidos.append({"chunk_id": reg["chunk_id"], "elemento": f"entities[{i}]"})
                for i in sorted(a3r - a2r):
                    perdidos.append({"chunk_id": reg["chunk_id"], "elemento": f"relations[{i}]"})
                for i in a2e - a3e:
                    ganados[f"entidad:{m3c or m3e.get(i)}"] += 1
                for i in a2r - a3r:
                    ganados[f"relacion:{m3c or m3r.get(i)}"] += 1
                omis_v3 += len(val3.get("omisiones_no_prosa") or [])
                omis_r2 += sum(1 for o in res["omisiones"] if o["origen"] == "v3_omisiones_no_prosa")
            ag["recuperadas_matriz_no_verificadas_e3"] = dict(sorted(recuperadas.items()))
            ag["pendientes_no_mapeados_por_motivo"] = dict(sorted(pend.items()))
            grupos[g][capa] = _ordenar(ag)
            # C1
            esperado = n1["grupos"][g]["capas"][CAPA_N1[capa]]["fuera"]
            obtenido = {k: dict(sorted(fuera_n1[k].items())) for k in CAMPOS_N1}
            iguales = all(obtenido[k] == {kk: vv for kk, vv in esperado[k].items()} for k in CAMPOS_N1)
            resumen_ok = all(sum(obtenido[k].values()) == n1["resumen_por_lista"][k][g][RESUMEN_N1[capa]]
                             for k in CAMPOS_N1)
            c1[f"{g}|{capa}"] = {"registros_n1": n1["grupos"][g]["capas"][CAPA_N1[capa]]["registros"],
                                 "registros": len(regs), "fuera_igual_a_n1": iguales,
                                 "totales_igual_a_resumen_por_lista": resumen_ok,
                                 "fuera_por_campo": {k: sum(obtenido[k].values()) for k in CAMPOS_N1}}
            reconc.extend(reconciliar(g, capa, obtenido, ag["valores"]))
            c3[f"{g}|{capa}"] = {"perdidos": perdidos, "ganados_por_motivo_v3": dict(sorted(ganados.items())),
                                 "omisiones_v3": omis_v3, "omisiones_r2_desde_v3": omis_r2,
                                 "validacion_v3_reproduce_la_guardada": dict(reproduce_v3)}
    controles["c1_fuera_de_lista_contra_n1"] = c1
    controles["reconciliacion"] = reconc
    controles["c2_matriz"] = control_matriz(grupos, pf, crudo, nuevas_por_unidad, filas_rep_ok)
    controles["c3_sin_perdidas"] = c3
    controles["c4_bkl_0038_poblacion_final_vs_grafo"] = control_bkl(inc_t0, pf, crudo)
    return {
        "unidad": "U-PYD", "etapa": "P2", "comando": COMANDO,
        "politica": {"ruta": str(V.POLITICA.relative_to(REPO)), "sha256": pol.sha256},
        "fuentes": {
            "n1_inventario": {"ruta": L.N1_RUTA, "commit": L.COMMIT_MANDATO, "sha256": L.N1_SHA256},
            "u_listas_n1": {"ruta": N1_SCRIPT, "commit": L.COMMIT_MANDATO, "sha256": N1_SCRIPT_SHA},
            "poblacion_final_u_estudio_matriz": {"ruta": POBLACION_FINAL, "commit": L.COMMIT_MANDATO,
                                                 "sha256": POBLACION_FINAL_SHA},
            "reporte_u_estudio_matriz": {"ruta": REPORTE_MATRIZ, "commit": L.COMMIT_MANDATO,
                                         "sha256": REPORTE_MATRIZ_SHA},
            "crudo": crudo.sellos,
        },
        "grupos": grupos,
        "bkl_0038_incoherentes": incoherentes,
        "controles": controles,
    }


def reconciliar(g: str, capa: str, n1_fuera: dict, valores: dict) -> list:
    filas = []
    vistos = defaultdict(set)
    for campo in CAMPOS_N1:
        for v, n in sorted(n1_fuera[campo].items()):
            claves = [v]
            if campo in ("Obligacion.tipo", "Restriccion.tipo", "Comunicacion.tipo") and v == "":
                claves = ["", "<ausente>"]
            r2 = Counter()
            for k in claves:
                r2.update(valores.get(campo, {}).get(k, {}))
                vistos[campo].add(k)
            filas.append({"grupo": g, "capa": capa, "campo": campo, "valor": v, "n1": n,
                          "r2": dict(sorted(r2.items())), "cierra": sum(r2.values()) == n, "origen": "n1"})
    # Lo que trata r2 y N1 no contaba fuera de lista (listas r2 o tratamiento nuevo).
    for campo, d in sorted(valores.items()):
        for v, t in sorted(d.items()):
            if campo in CAMPOS_N1 and v in vistos[campo]:
                continue
            filas.append({"grupo": g, "capa": capa, "campo": campo, "valor": v, "n1": None,
                          "r2": dict(sorted(t.items())), "cierra": None, "origen": "solo_r2"})
    return filas


def control_matriz(grupos, pf, crudo, nuevas_por_unidad, filas_rep_ok) -> dict:
    out = {"filas_P01_P02_en_el_reporte": filas_rep_ok, "A": {}, "B": {}}
    for i, g in enumerate(("diez", "desarrollo")):
        rec = grupos[g]["L0"]["recuperadas_matriz_no_verificadas_e3"]
        out["A"][g] = {t: {"r2": rec.get(t, 0), "u_estudio_matriz": ESPERADO_A[t][i],
                           "coincide": rec.get(t, 0) == ESPERADO_A[t][i]} for t in ESPERADO_A}
    rec5 = grupos["cinco"]["L0"]["recuperadas_matriz_no_verificadas_e3"]
    out["A"]["cinco"] = {t: {"r2": rec5.get(t, 0), "diez_menos_desarrollo": ESPERADO_A[t][0] - ESPERADO_A[t][1],
                             "coincide": rec5.get(t, 0) == ESPERADO_A[t][0] - ESPERADO_A[t][1]} for t in ESPERADO_A}
    # B: población final = A con el crudo del reintento en las unidades aceptadas tras reintento.
    claves_t0 = {a["key"]: a["chunk_id"] for a in crudo.reintentos["t0"]}
    unidades = []
    fuentes = Counter()
    for k, u in sorted(pf.items()):
        fuentes[u["fuente_crudo"]] += 1
        if u["fuente_crudo"] != "cache_reintentos":
            continue
        if len(u.get("cache_keys") or []) != 1 or u["cache_keys"][0] not in claves_t0:
            raise L.FrenoLectura(f"población final: {k} sin una clave de reintento asignada")
        key = u["cache_keys"][0]
        if claves_t0[key] != u["chunk_id"]:
            raise L.FrenoLectura(f"población final: la clave de {k} es de otro chunk")
        a = nuevas_por_unidad.get(("t0", "L0", u["chunk_id"]), Counter())
        b = nuevas_por_unidad.get(("t0", "L0r", key), Counter())
        d = {t: b.get(t, 0) - a.get(t, 0) for t in ESPERADO_A}
        unidades.append({"to": u["to"], "chunk_id": u["chunk_id"], "clave_reintento": key,
                         "L0": {t: a.get(t, 0) for t in ESPERADO_A},
                         "L0r": {t: b.get(t, 0) for t in ESPERADO_A}, "delta": d})
    out["poblacion_final_fuentes"] = dict(sorted(fuentes.items()))
    for i, g in enumerate(("diez", "desarrollo")):
        tos = L.GRUPOS[g]["tos"]
        us = [u for u in unidades if u["to"] in tos]
        res = {}
        for t in ESPERADO_A:
            a = grupos[g]["L0"]["recuperadas_matriz_no_verificadas_e3"].get(t, 0)
            mas = sum(u["L0r"][t] for u in us)
            menos = sum(u["L0"][t] for u in us)
            res[t] = {"A": a, "menos_L0_de_las_reintentadas": menos, "mas_L0r_de_las_reintentadas": mas,
                      "B_calculada": a - menos + mas, "B_tablero_c19": ESPERADO_B[t][i],
                      "coincide": a - menos + mas == ESPERADO_B[t][i],
                      "unidades_con_delta": sum(1 for u in us if u["delta"][t] != 0)}
        out["B"][g] = {"unidades_aceptadas_tras_reintento": len(us), "por_par": res}
    out["unidades_reintentadas_con_delta"] = [u for u in unidades if any(u["delta"].values())]
    return out


def control_bkl(inc_t0: list, pf: dict, crudo) -> dict:
    fuente = {u["chunk_id"]: u["fuente_crudo"] for u in pf.values()}
    claves = {u["cache_keys"][0] for u in pf.values() if u["fuente_crudo"] == "cache_reintentos"}
    pob = sorted(cid for capa, cid, origen in inc_t0
                 if (capa == "L0" and fuente.get(cid) != "cache_reintentos")
                 or (capa == "L0r" and origen in claves))
    out = {}
    for g in ("desarrollo", "diez"):
        tos = L.GRUPOS[g]["tos"]
        kg = json.loads(crudo._verificado(f"{g}_kg.json").decode("utf-8"))
        nodos = {n["id"]: n for n in kg["nodes"]}
        graf = sorted(e["provenance"].get("chunk_id") for e in kg["edges"]
                      if e["relation"] in ("limita", "prohibe") and nodos[e["source"]]["type"] == "Restriccion"
                      and (nodos[e["source"]]["properties"].get("tipo") == "prohibicion") != (e["relation"] == "prohibe")
                      and isinstance(nodos[e["source"]]["properties"].get("tipo"), str)
                      and (nodos[e["source"]]["properties"].get("tipo") == "prohibicion"
                           or nodos[e["source"]]["properties"].get("tipo", "").startswith("limite_")))
        p = [c for c in pob if c.split("::")[0] in tos]
        out[g] = {"poblacion_final_r2": p, "grafo": graf, "coincide": p == graf}
    return out


# ------------------------------------------------------------------------- #
# Markdown                                                                    #
# ------------------------------------------------------------------------- #
def _t(filas, cab):
    out = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    for f in filas:
        out.append("| " + " | ".join(str(x) for x in f) + " |")
    return out


def _trat(d: dict) -> str:
    return ", ".join(f"{k} {v}" for k, v in sorted(d.items())) or "—"


def escribir_md(J: dict) -> str:
    L_ = [f"# U-PYD P2 — validador r2 sobre el crudo guardado (r1 y tanda 0)", "",
          f"Comando: `{J['comando']}`", "",
          f"Política: `{J['politica']['ruta']}`, sha256 `{J['politica']['sha256']}`. Fuentes leídas en "
          f"`{L.COMMIT_MANDATO}` (firma del mandato) con candado de sha256; crudo con los sellos de N1 "
          f"({len(J['fuentes']['crudo'])} archivos).", "",
          "Capas: L0 = primer intento de E1 (`tool_input_crudo`); L0r = reintentos de E3 "
          "(`e1_reintentos.db`, immutable=1).", ""]
    G = J["grupos"]
    L_ += ["## 1. Volumen y rechazos", ""]
    filas = []
    for g, capas in G.items():
        for capa, a in capas.items():
            m = a["metricas"]
            filas.append([g, capa, a["registros"], m.get("entities_in", 0), m.get("entities_out", 0),
                          m.get("relations_in", 0), m.get("relations_out", 0), _trat(a["rechazos_por_motivo"])])
    L_ += _t(filas, ["grupo", "capa", "registros", "entidades in", "entidades out", "relaciones in",
                     "relaciones out", "rechazos por motivo"]) + [""]
    L_ += ["## 2. Valores fuera de lista por campo y tratamiento", "",
           "Cada fila: valor original y tratamiento de la política r2 (normalizado, registrado con marca, "
           "rechazado).", ""]
    filas = []
    for g, capas in G.items():
        for capa, a in capas.items():
            for campo in ("tipo_entidad", "predicado", "Obligacion.tipo", "Restriccion.tipo",
                          "Comunicacion.tipo", "Obligacion.frecuencia", "sujeto_id", "padre_sugerido"):
                for v, t in a["valores"].get(campo, {}).items():
                    filas.append([g, capa, campo, repr(v), _trat(t)])
    L_ += _t(filas, ["grupo", "capa", "campo", "valor", "tratamiento"]) + [""]
    L_ += ["## 3. Claves, valores y campos del ítem", ""]
    filas = []
    for g, capas in G.items():
        for capa, a in capas.items():
            for campo in ("claves", "valores", "campos_del_item_entidad", "campos_del_item_relacion"):
                for v, t in a["valores"].get(campo, {}).items():
                    filas.append([g, capa, campo, v, _trat(t)])
    L_ += _t(filas, ["grupo", "capa", "campo", "clave o valor", "tratamiento"]) + [""]
    L_ += ["## 4. Marcas: BKL-0038, mención, omisiones, matriz", ""]
    filas = []
    for g, capas in G.items():
        for capa, a in capas.items():
            c = a["contadores"]
            filas.append([g, capa, _trat(c.get("coherencia_tipo_predicado", {})),
                          _trat(c.get("sujeto_mencion", {})),
                          c.get("omisiones", {}).get("fuera_de_tipos_por_tipo_rechazado", 0),
                          c.get("omisiones", {}).get("v3_sin_categoria_ni_tramo", 0),
                          _trat(a["recuperadas_matriz_no_verificadas_e3"]),
                          _trat(a["pendientes_no_mapeados_por_motivo"])])
    L_ += _t(filas, ["grupo", "capa", "coherencia tipo–predicado", "mención", "omisiones fuera_de_tipos",
                     "omisiones v3 leídas", "recuperadas por la matriz (no verificadas E3)",
                     "pendientes no mapeados"]) + [""]
    if J["bkl_0038_incoherentes"]:
        L_ += ["Relaciones con la marca `incoherente` (BKL-0038), grupos r1 y diez:", ""]
        L_ += _t([[x["grupo"], x["capa"], x["chunk_id"], x["indice_relacion"], x["restriccion_tipo"],
                   x["predicado"], x["restriccion_label"]] for x in J["bkl_0038_incoherentes"]],
                 ["grupo", "capa", "chunk", "relación", "Restriccion.tipo", "predicado", "label"]) + [""]
    C = J["controles"]
    L_ += ["## 5. Controles", "", "### C1. Fuera de lista contra N1", ""]
    L_ += _t([[k, v["registros_n1"], v["registros"], v["fuera_igual_a_n1"], v["totales_igual_a_resumen_por_lista"],
               _trat(v["fuera_por_campo"])] for k, v in C["c1_fuera_de_lista_contra_n1"].items()],
             ["grupo|capa", "registros N1", "registros", "fuera = N1", "totales = resumen_por_lista",
              "fuera por campo"]) + [""]
    L_ += ["### Reconciliación valor por valor", "",
           "`origen n1`: valor fuera de lista en N1 y su tratamiento r2 (`cierra` = la suma del tratamiento r2 "
           "es el conteo de N1). `origen solo_r2`: lo que r2 trata y N1 no contaba fuera de lista.", ""]
    L_ += _t([[f["grupo"], f["capa"], f["campo"], repr(f["valor"]), f["n1"] if f["n1"] is not None else "—",
               _trat(f["r2"]), f["cierra"] if f["cierra"] is not None else "—", f["origen"]]
              for f in C["reconciliacion"]],
             ["grupo", "capa", "campo", "valor", "N1", "tratamiento r2", "cierra", "origen"]) + [""]
    M2 = C["c2_matriz"]
    L_ += ["### C2. Relaciones recuperadas por la matriz ampliada", "",
           f"Filas P01 y P02 presentes en el reporte de U-ESTUDIO-MATRIZ: {M2['filas_P01_P02_en_el_reporte']}.", ""]
    filas = []
    for g, d in M2["A"].items():
        for t, x in d.items():
            ref = x.get("u_estudio_matriz", x.get("diez_menos_desarrollo"))
            filas.append([g, t, x["r2"], ref, x["coincide"]])
    L_ += _t(filas, ["grupo", "→", "r2 (L0)", "U-ESTUDIO-MATRIZ, columna A", "coincide"]) + [""]
    L_ += [f"Fuentes de la población final: {_trat(M2['poblacion_final_fuentes'])}.", ""]
    filas = []
    for g, d in M2["B"].items():
        for t, x in d["por_par"].items():
            filas.append([g, t, x["A"], x["menos_L0_de_las_reintentadas"], x["mas_L0r_de_las_reintentadas"],
                          x["B_calculada"], x["B_tablero_c19"], x["coincide"], x["unidades_con_delta"]])
    L_ += _t(filas, ["grupo", "→", "A", "− L0 de las reintentadas", "+ L0r de las reintentadas", "B calculada",
                     "B (tablero [c19])", "coincide", "unidades con delta"]) + [""]
    L_ += ["Unidades aceptadas tras reintento con delta distinto de cero:", ""]
    L_ += _t([[u["to"], u["chunk_id"], u["L0"]["Operacion"], u["L0r"]["Operacion"], u["delta"]["Operacion"],
               u["L0"]["Potestad"], u["L0r"]["Potestad"], u["delta"]["Potestad"]]
              for u in M2["unidades_reintentadas_con_delta"]],
             ["TO", "chunk", "→Op L0", "→Op L0r", "Δ Op", "→Pot L0", "→Pot L0r", "Δ Pot"]) + [""]
    C4 = C["c4_bkl_0038_poblacion_final_vs_grafo"]
    L_ += ["### C4. BKL-0038: población final contra el grafo ensamblado", ""]
    L_ += _t([[g, len(v["poblacion_final_r2"]), len(v["grafo"]), v["coincide"], ", ".join(v["grafo"])]
              for g, v in C4.items()], ["grupo", "población final (r2)", "grafo", "coincide", "chunks del grafo"])
    L_ += [""]
    L_ += ["### C3. Ningún elemento aceptado por v3 se pierde", ""]
    L_ += _t([[k, len(v["perdidos"]), _trat(v["ganados_por_motivo_v3"]), v["omisiones_v3"],
               v["omisiones_r2_desde_v3"], _trat(v["validacion_v3_reproduce_la_guardada"])]
              for k, v in C["c3_sin_perdidas"].items()],
             ["grupo|capa", "perdidos", "ganados (motivo del rechazo v3)", "omisiones v3", "omisiones r2 desde v3",
              "v3 re-corrido = guardado (L0)"]) + [""]
    return "\n".join(L_) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default=str(SALIDA))
    args = ap.parse_args()
    out = Path(args.salida)
    out.mkdir(parents=True, exist_ok=True)
    J = correr()
    b_json = (json.dumps(J, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    b_md = escribir_md(J).encode("utf-8")
    for nombre, b in (("prueba_crudo_t0.json", b_json), ("prueba_crudo_t0.md", b_md)):
        (out / nombre).write_bytes(b)
        print(f"{hashlib.sha256(b).hexdigest()}  {nombre}")


if __name__ == "__main__":
    main()
