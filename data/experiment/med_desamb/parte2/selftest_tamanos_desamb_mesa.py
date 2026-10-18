"""Selftest de tamanos_desamb_mesa.py (mesa, §139): casos sintéticos de respuesta conocida, sin leer ningún grafo real.
Uso: python3 -I -B selftest_tamanos_desamb_mesa.py <dir de e2_lib.py>"""
import importlib.util
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("tam", str(AQUI / "tamanos_desamb_mesa.py"))
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)
E = T.cargar_e2lib(sys.argv[1])
fallas = []


def ok(cond, que):
    print(("OK   " if cond else "FALLA") + " " + que)
    if not cond:
        fallas.append(que)


def prov(to, punto, anc):
    return {"to": to, "punto": punto, "chunk_id": f"{to}::{punto}", "rol_documental": "punto_propio", "ancestros": anc}


def nodo(i, t, label, to, punto, anc, desc=None):
    p = prov(to, punto, anc)
    props = {"descripcion": desc} if desc else {}
    return {"id": i, "type": t, "label": label, "properties": props, "provenance": p, "provenances": [p]}


def rem(src, to, p_src, p_dst):
    p = prov(to, p_src, [])
    return {"source": src, "target": "x", "relation": "remite_a", "provenance": p, "provenances": [p],
            "properties": {"alcance": "interna", "destino": f"{to}::{p_dst}"}}


# A. Operacion «Cesión de cartera» en tres puntos de d1: 1.1 y 1.2 con el mismo padre «1», 3.4 suelto -> parcial;
# «Transferencia» en 2.1 y 5.1 unidas por remite_a -> conectado; «Pase» en 4.1 y 6.1 sin nada -> sin_conexion;
# «Pase» en d2 no cuenta (otro documento); Obligacion con la misma descripción en 2 puntos del mismo padre -> conectado.
g = {"nodes": [
    nodo("o1", "Operacion", "Cesión de cartera", "d1", "1.1", ["S1", "1"]),
    nodo("o2", "Operacion", "Cesión de cartera", "d1", "1.2", ["S1", "1"]),
    nodo("o3", "Operacion", "Cesión de cartera", "d1", "3.4", ["S3", "3"]),
    nodo("o4", "Operacion", "Transferencia", "d1", "2.1", ["S2", "2"]),
    nodo("o5", "Operacion", "Transferencia", "d1", "5.1", ["S5", "5"]),
    nodo("o6", "Operacion", "Pase", "d1", "4.1", ["S4", "4"]),
    nodo("o7", "Operacion", "Pase", "d1", "6.1", ["S6", "6"]),
    nodo("o8", "Operacion", "Pase", "d2", "4.1", ["S4", "4"]),
    nodo("o9", "Operacion", "Cesiones de carteras", "d1", "7.1", ["S7", "7"]),
    nodo("b1", "Obligacion", "Informar", "d1", "8.1", ["S8", "8"], desc="Informar al BCRA"),
    nodo("b2", "Obligacion", "Informar", "d1", "8.2", ["S8", "8"], desc="Informar al BCRA"),
    nodo("b3", "Obligacion", "Informar", "d1", "9.1", ["S9", "9"], desc="Informar a la SEFyC"),
], "edges": [rem("o4", "d1", "2.1", "5.1"), rem("x", "d1", "1.1", "9.9")]}
clave = {t: (lambda n, to: E.entity_slug_r2(n, {"to": to, "punto": ""}, fase="r2b")) for t in T.TIPOS_CON_PUNTO}
A = T.cuenta_A(E, g, clave)
op = A["Operacion"]
ok(op["grupos"] == 3 and op["nodos_en_grupos"] == 7, f"Operacion: 3 grupos y 7 nodos (da {op['grupos']} y {op['nodos_en_grupos']})")
ok(op["clases_de_grupo"] == {"parcial": 1, "conectado": 1, "sin_conexion": 1}, f"Operacion: una clase de cada (da {op['clases_de_grupo']})")
ok(op["pares_de_puntos"] == {"mismo_padre": 1, "ninguno": 3, "remite_a": 1}, f"Operacion: pares (da {op['pares_de_puntos']})")
ok(op["vinculos_candidatos_O1"] == 2, f"Operacion: 2 vínculos candidatos de O1 (da {op['vinculos_candidatos_O1']})")
ob = A["Obligacion"]
ok(ob["grupos"] == 1 and ob["nodos_en_grupos"] == 2 and ob["clases_de_grupo"] == {"conectado": 1},
   f"Obligacion: la misma descripción en 8.1 y 8.2 es un grupo conectado; 9.1 dice otra cosa (da {ob['grupos']}, {ob['clases_de_grupo']})")
plegada = T.cuenta_A(E, g, {"Operacion": lambda n, to: tuple(sorted(T.palabras(E, n.get("label") or ""))) or None})["Operacion"]
ok(plegada["grupos"] == 3 and plegada["nodos_en_grupos"] == 8,
   f"plegada: «Cesiones de carteras» se suma al grupo de «Cesión de cartera» (da {plegada['grupos']} grupos, {plegada['nodos_en_grupos']} nodos)")
# r2a: un solo nodo en dos puntos cuenta como grupo (ocurrencias)
n = nodo("u", "Operacion", "Canje", "d1", "1.1", ["S1", "1"])
n["provenances"].append(prov("d1", "2.2", ["S2", "2"]))
A2 = T.cuenta_A(E, {"nodes": [n], "edges": []}, clave)["Operacion"]
ok(A2["grupos"] == 1 and A2["nodos_en_grupos"] == 1 and A2["ocurrencias_en_grupos"] == 2, "r2a: un nodo unido entre dos puntos es un grupo de 2 ocurrencias")

# B. Estratos
base = {"desacuerdo_regla_modelo": False, "mencion_verificada": "exacta", "regla_texto": None, "id_regla_texto": None, "sujeto_id_modelo": "S_a"}
casos = [({"metodo_resolucion": "R1_label_exacto"}, "E1"), ({"metodo_resolucion": "R1_alias_exacto", "desacuerdo_regla_modelo": True}, "E2"),
         ({"metodo_resolucion": "R4_sugerencia_modelo", "regla_texto": "R3", "id_regla_texto": "S_a"}, "E3"),
         ({"metodo_resolucion": "R4_sugerencia_modelo", "regla_texto": "R2", "id_regla_texto": "S_b"}, "E4"),
         ({"metodo_resolucion": "R4_sugerencia_modelo"}, "E5"), ({"metodo_resolucion": "R4_sugerencia_modelo", "mencion_verificada": "tokens"}, "E5"),
         ({"metodo_resolucion": "R4_sugerencia_modelo", "mencion_verificada": "no"}, "E6"),
         ({"metodo_resolucion": "R2_id_slug+label_singularizado"}, "E7"), ({"metodo_resolucion": "R2_calificador"}, "E8"),
         ({"metodo_resolucion": "R3"}, "E9"), ({"metodo_resolucion": "R4_sugerencia_modelo", "mencion_verificada": "ausente"}, "E10"),
         ({"metodo_resolucion": "cuarentena"}, "cuarentena")]
for c, esperado in casos:
    ok(T.estrato({**base, **c}) == esperado, f"estrato {esperado}: {c}")

# C. Normalización de C1
def com(cod, tipo):
    return {"type": "Comunicacion", "properties": {"codigo": cod, "tipo": tipo}}
pares = [(("A-6847", "A"), "A 6847"), (("Com. A 6847", "A"), "A 6847"), (("Comunicación A 6847", "A"), "A 6847"),
         (("A-<sin especificar>", "A"), None), (("Lineamientos-5.6", "referencia"), None), (("PC", "TO"), None),
         (("Ley de Entidades Financieras", "externa"), "ley de entidades financieras"),
         (("B-12000", "B"), "B 12000"), (("A-0684", "A"), "A 684")]
for (cod, tipo), esp in pares:
    ok(T.codigo_normalizado(com(cod, tipo)) == esp, f"C1: «{cod}» ({tipo}) → {esp!r} (da {T.codigo_normalizado(com(cod, tipo))!r})")
ok(T.codigo_normalizado(com("A-6847", "A")) != T.codigo_normalizado(com("A-6874", "A")), "C1: A 6847 y A 6874 no colisionan")
gC = [("g", {"nodes": [dict(nodo("c1", "Comunicacion", "Com. A 6847", "d1", "1", []), properties={"codigo": "A-6847", "tipo": "A"}),
                       dict(nodo("c2", "Comunicacion", "Comunicación A 6847", "d2", "4", []), properties={"codigo": "Comunicación A 6847", "tipo": "A"}),
                       dict(nodo("c3", "Comunicacion", "Com. A —", "d3", "2", []), properties={"codigo": "A-<sin especificar>", "tipo": "A"}),
                       dict(nodo("c4", "Comunicacion", "Com. A —", "d4", "2", []), properties={"codigo": "A-<sin especificar>", "tipo": "A"})],
             "edges": []})]
C = T.cuenta_C(E, gC)
ok(C["repetidas_por_codigo_c1"] == {"grupos": 1, "nodos": 2, "con_codigos_crudos_distintos": 1},
   f"C: A 6847 en d1 y d2 es una colisión con códigos crudos distintos, los marcadores no (da {C['repetidas_por_codigo_c1']})")
ok(C["repetidas_por_clave_e2"]["grupos"] == 1, f"C: por la clave de E2 solo se repiten los dos marcadores (da {C['repetidas_por_clave_e2']})")
print("FALLAS:", len(fallas))
sys.exit(1 if fallas else 0)
