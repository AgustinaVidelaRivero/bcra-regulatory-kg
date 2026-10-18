"""B6.1, tanda 1, T3, punto 7: las cuotas por celda y la regla de asignación de las muestras de T4 (pre-registro firmado, §5.4 y §5.4 bis,
punto 2), como regla general sobre el número de elementos de cada celda. La usan umbrales_t4_t3f.py y sorteos_t4_t3f.py.
  - En cada muestra de 30: RI, 10 sin_raiz y 5 del resto; NG, 5 sin_raiz y 10 del resto (en las aceptadas, en cada estrato).
  - Una población de 30 elementos o menos se lee entera, sin celdas (§5.4 bis, punto 2, v8c).
  - Si una clase entera tiene menos elementos que su cuota (15), entran todos, y lo que falta sale de la otra clase: se reparte entre sus
    dos celdas en proporción a sus cuotas, con el redondeo a favor de la de cuota mayor (propuesta de la mesa confirmada con la firma).
  - Después, en cada clase: si una celda tiene menos elementos que su cuota, entran todos, y la otra celda de la misma clase sortea su
    cuota más lo que falta (§5.4), con su misma cadena.
"""
CELDAS = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]
CUOTA = {"RI:sin_raiz": 10, "RI:resto": 5, "NG:sin_raiz": 5, "NG:resto": 10}
CLASES = {"RI": ["RI:sin_raiz", "RI:resto"], "NG": ["NG:sin_raiz", "NG:resto"]}


def asignar(N: dict) -> dict:
    """{celda: cuántos se sortean} para una población con N[celda] elementos, y las notas de lo que se declara."""
    total = sum(N.values())
    if total <= 30:
        return {"entera_sin_celdas": True, "n": dict(N), "notas": [f"{total} elementos: se lee entera, sin celdas"]}
    q = dict(CUOTA)
    notas = []
    for k, cs in CLASES.items():
        nk, qk = sum(N[c] for c in cs), sum(CUOTA[c] for c in cs)
        if nk < qk:
            otra = [c for c in CELDAS if c not in cs]
            falta = qk - nk
            mayor, menor = sorted(otra, key=lambda c: -CUOTA[c])
            a_menor = (falta * CUOTA[menor]) // qk          # el redondeo, a favor de la de cuota mayor
            q[menor] += a_menor
            q[mayor] += falta - a_menor
            for c in cs:
                q[c] = N[c]
            notas.append(f"la clase {k} tiene {nk} de su cuota de {qk}: entran todos; faltan {falta}, que salen de la otra clase: "
                         f"{a_menor} a {menor} y {falta - a_menor} a {mayor}")
    for k, cs in CLASES.items():
        a, b = cs
        for c, o in ((a, b), (b, a)):
            if N[c] < q[c]:
                falta = q[c] - N[c]
                q[o] += falta
                notas.append(f"la celda {c} tiene {N[c]} de su cuota de {q[c]}: entran todos; {o} sortea {falta} más")
                q[c] = N[c]
    assert all(q[c] <= N[c] for c in CELDAS) and sum(q.values()) == 30, (N, q)
    return {"entera_sin_celdas": False, "n": q, "notas": notas}
