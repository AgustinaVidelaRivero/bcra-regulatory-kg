"""Cifras del lote 1 del piloto de U-MED-UMBRALES (paso 2 adjudicado por la autora), para el FRENO del lote 1 (mesa, 10/10/2026).
Lee el archivo sellado de la autora (diferencias_paso2_lote1_autora.md, sha256 dc5ea3ed…) y calcula, sin mirar el acta ni el
diagnóstico: las filas por clase y por campo, y los veredictos del elemento del §2.5 de la enmienda 1.
- Un campo comparado que no aparece en el archivo es igual en el paso 1 y en el grafo: correcto.
- Una ficha sin fila de pertinencia es «pertinente» (el comparador lista la pertinencia solo si es otra o quedó sin llenar).
- Núcleo: pertinente, y correctos valor, unidad, moneda, comparación y base. Una fila de esos campos con otra clase que «correcto» o
  «no aplica» lo hace incorrecto (una base parcial cuenta como incorrecta cuando la nota de la autora lo dice: L1-11.1 y L1-15.1); una
  «no decidible» lo deja no decidible si no es ya incorrecto.
- Núcleo contra la definición: igual, pero la comparación omitida «de la definición» cuenta como correcta.
- Completo: el núcleo, más tipo de días y destino de la base (este, solo si el grafo lo guarda).
- Cotas de los no decidibles: inferior, todos incorrectos; superior, correctos los que no tienen otra fila incorrecta.
- L1-01 queda fuera de la cifra (ficha contaminada); los elementos vacíos (§2.5) se leen aparte.
Uso: python3 -I -B cifras_lote1_paso2_mesa.py <diferencias_paso2_lote1_autora.md> <salida.json>"""
import collections, hashlib, json, re, sys
src, out = sys.argv[1:3]
assert hashlib.sha256(open(src, "rb").read()).hexdigest() == "dc5ea3edd9ebd5402f000148e34344ba3036e79d77693e79fb45251a48064e20"
NUCLEO = {"valor", "unidad", "moneda", "comparacion", "base"}
COMPLETO_EXTRA = {"tipo_de_dias", "destino_de_la_base"}
PARCIAL_INCORRECTA = {"L1-11.1", "L1-15.1"}   # notas_paso2_lote1.md (d3f2b4c8…): «cuenta como INCORRECTA (L7)»
fichas, vacias, filas = [], [], collections.defaultdict(list)
for l in open(src, encoding="utf-8"):
    m = re.match(r"^## (L1-\d\d) · ", l)
    if m:
        fichas.append(m.group(1)); actual = m.group(1)
    if l.startswith("Elemento vacío (§2.5)"):
        vacias.append(actual)
    if l.startswith("| L1-"):
        c = [x.strip().replace("\\|", "|") for x in re.split(r"(?<!\\)\|", l.strip().strip("|"))]
        filas[c[0].split(".")[0]].append({"fila": c[0], "campo": c[1], "motivo": c[2], "clase": c[5], "c24": c[6], "corrige": c[7]})
assert len(fichas) == 20
todas = [r for f in fichas for r in filas[f]]
excluida = "L1-01"
res = {"fichas": len(fichas), "vacias": vacias, "excluida": excluida,
       "filas": len(todas), "filas_que_cuentan": sum(1 for r in todas if not r["fila"].startswith(excluida)),
       "por_motivo_y_clase": collections.Counter(), "por_campo_diferencias": collections.defaultdict(collections.Counter),
       "clase_2_4": collections.Counter(r["c24"] for r in todas if r["c24"] not in ("—", "")),
       "correcciones_de_campo_del_paso1": [r["fila"] for r in todas if r["corrige"].startswith("sí") and r["campo"] != "no_decidible"],
       "correcciones_de_redaccion": [r["fila"] for r in todas if r["corrige"].startswith("sí") and r["campo"] == "no_decidible"]}
for r in todas:
    if r["fila"].startswith(excluida):
        continue
    res["por_motivo_y_clase"][f"{r['motivo'].split(';')[0]} → {r['clase']}"] += 1
    if r["motivo"].startswith("diferencia"):
        res["por_campo_diferencias"][r["campo"]][r["clase"]] += 1
def veredicto(rs, campos, contra_def=False):
    estado = "correcto"
    for r in rs:
        if r["campo"] not in campos:
            continue
        cl = r["clase"]
        if cl in ("correcto", "no aplica"):
            continue
        if cl == "parcial" and r["fila"] not in PARCIAL_INCORRECTA:
            continue
        if contra_def and r["campo"] == "comparacion" and cl == "omitido" and r["c24"] == "de la definición":
            continue
        if cl == "no decidible":
            estado = "no_decidible" if estado == "correcto" else estado
        else:
            estado = "incorrecto"
    return estado
elem = {}
for f in fichas:
    if f == excluida or f in vacias:
        continue
    rs = filas[f]
    pert = next((r for r in rs if r["campo"] == "pertinencia"), None)
    pert_nd = pert is not None
    v = {}
    for nombre, campos, cd in (("nucleo", NUCLEO, False), ("nucleo_contra_la_definicion", NUCLEO, True),
                               ("completo", NUCLEO | COMPLETO_EXTRA, False)):
        e = veredicto(rs, campos, cd)
        if pert_nd:
            v[nombre] = "no_decidible_por_pertinencia" + ("_y_con_otra_fila_incorrecta" if e == "incorrecto" else "")
        else:
            v[nombre] = e
    elem[f] = v
res["elementos"] = elem
for nombre in ("nucleo", "nucleo_contra_la_definicion", "completo"):
    c = collections.Counter(v[nombre] for v in elem.values())
    corr = c["correcto"]; inc = c["incorrecto"]
    nd_ok = c["no_decidible_por_pertinencia"] + c["no_decidible"]
    nd_mal = c["no_decidible_por_pertinencia_y_con_otra_fila_incorrecta"]
    res[f"resumen_{nombre}"] = {"elementos": len(elem), "correctos": corr, "incorrectos": inc,
                                "no_decidibles": nd_ok + nd_mal, "cota_inferior": f"{corr} de {len(elem)}",
                                "cota_superior": f"{corr + nd_ok} de {len(elem)}", "sobre_decididos": f"{corr} de {corr + inc}"}
json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=dict)
print(json.dumps({k: res[k] for k in res if k.startswith("resumen") or k in ("filas", "filas_que_cuentan", "clase_2_4")}, ensure_ascii=False, default=dict, indent=1))
