# Anexo — pool de anclas elegibles y solapamiento esperado entre muestreos (U-A1.3)

Verificación adicional pedida en la revisión de la fase B ($0, sin abrir material
EV2). Pregunta: dado el pool de anclas `to:punto` que el sampler del pipeline de
sintéticas puede producir sobre KG-Refinado bajo sus gates, ¿cuánto se espera que
solapen dos muestreos independientes de 58 y 37 anclas? La mesa observó una
intersección de **28** entre las 37 anclas distintas de los 50 pares aptos de esta
unidad (`pares/pares_v3.json`, semilla `sinteticas-faseA-v3`, sin E-C) y otro
muestreo del mismo grafo (58 anclas). Acá no se necesita ni se usa saber cuáles
son esas 58: solo el tamaño y la estructura del pool.

## 1. Pool de anclas elegibles bajo los gates del sampler

Gates aplicados exactamente como los del sampler importado (`sampler.Sampler`,
sin editar): elegibilidad `_elegible_dirigido` (excluye `TextoOrdenado`,
`Comunicacion`, `rol_fuente == esqueleto`, sin ancla PDF) y gate de quemado sobre
TODAS las anclas del subgrafo (`Quemado.todas_aptas`, mapa de 5 sets); gold =
anclas del/los nodo(s) respuesta. E-C no se computa (excluido por laudo).

| estrato | candidatos aptos | anclas `to:punto` distintas en el pool |
|---|---|---|
| E-A — aristas con ambos extremos elegibles y aptos; gold = anclas del target | 1.197 | 132 |
| E-B — nodos finales elegibles/aptos con al menos un camino de largo 2 por nodos elegibles/aptos (condición necesaria y suficiente para largo 2–3); gold = anclas del nodo final | 1.022 | 107 |
| E-D — pares cuasi-duplicados (`_pares_ed`) con ambos nodos aptos; gold = anclas del objetivo (cualquiera de los dos) | 288 | 83 |
| E-E — nodos con ancla PDF, todas aptas | 2.340 | **175** |
| **TOTAL (unión de los cuatro)** | | **175** |

E-E cubre el pool completo (muestreo uniforme sobre todos los nodos con ancla apta).
Las 37 anclas distintas de los 50 aptos de esta unidad están todas dentro del pool.
El pool es chico y **muy concentrado**: la granularidad de ancla es gruesa (mediana
29 nodos por ancla), así que unas pocas anclas aparecen en muchos candidatos — en
E-A, `cap:3.1` está en 81 aristas candidatas, `cap:4.2` en 50, `ext:3.13` en 43,
`ext:7.11` en 42, `cap:6.2` en 37.

## 2. Intersección esperada de dos muestreos independientes (58 ∩ 37)

| modelo | E[X] | sd | IC 95 % | P(X ≥ 28) | ¿28 dentro del IC? |
|---|---|---|---|---|---|
| (a) hipergeométrica uniforme sobre N = 175 (58 y 37 anclas sin reposición, todas equiprobables) | 12,3 | 2,55 | [7, 17] | 2,2·10⁻⁹ | no — modelo inadecuado: ignora los pesos |
| (b) simulación, 10.000 corridas, pesos reales del sampler (uniforme sobre CANDIDATOS por estrato, no sobre anclas): A = muestreo de 40/estrato acumulando samples en orden aleatorio hasta reunir 58 anclas (lo logra en el 100 % de las corridas), B = 20/estrato hasta 37 anclas; semilla `20260818` | **24,2** | 2,45 | **[19, 29]** | 8,5 % | **sí** (cola alta, ≈ percentil 92) |
| (b') ídem con A también de 40/estrato para B (semilla `20260818`) | 24,2 | 2,46 | [19, 29] | 8,8 % | sí |
| (c) simulación, 10.000 corridas, A y B de 20/estrato cada uno (semilla `20260817`); un muestreo de 80 samples reúne en promedio 49,5 anclas distintas (mín 36, máx 64), así que A alcanza 58 solo a veces y la intersección se computa contra un A menor | 21,5 | 2,59 | [17, 27] | 1,0 % | borde (fuera por 1) |

Lectura: con la distribución real de pesos, dos muestreos independientes de este
pool comparten típicamente ~24 de 37 anclas (≈ 65 %); el 28 observado cae dentro
del IC 95 % del modelo ponderado (b), en su cola alta. El solapamiento alto es una
propiedad estructural del pool (175 anclas elegibles, concentrado), no evidencia de
reuso de semilla o material: la semilla v3 es nueva, la doble corrida fue
byte-idéntica y E-C (el único estrato idéntico por construcción) quedó excluido.
El modelo uniforme (a) subestima groseramente porque trata todas las anclas como
equiprobables. Identidad de pares (misma pregunta) con el otro muestreo,
verificada por la mesa: **0**.

## 3. Reproducción (desde la raíz del repo, `.venv/bin/python -B`)

```python
import sys, random, math
from math import comb
from collections import defaultdict
from statistics import mean, pstdev
sys.path.insert(0, "data/experiment/ablacion_retrieval"); import comun_ablacion   # sys.path del pipeline
import sampler                                                                    # pipeline de sintéticas, sin editar
s = sampler.Sampler(semilla="pool"); g = s.g; Q = s.quemado
key = lambda a: f"{a['to']}:{a['ancla']}"
apt = {}
def apto(nid):
    if nid not in apt: a = g.anclas(nid); apt[nid] = bool(a) and Q.todas_aptas(a)[0]
    return apt[nid]
elig = lambda n: s._elegible_dirigido(n) is None
anc = lambda n: frozenset(key(a) for a in g.anclas(n)); ok = lambda n: elig(n) and apto(n)
ea = [anc(e["target"]) for e in g.edges if elig(e["source"]) and elig(e["target"]) and apto(e["source"]) and apto(e["target"])]
nb = defaultdict(set)
for e in g.edges:
    u, v = e["source"], e["target"]
    if ok(u) and ok(v): nb[u].add(v); nb[v].add(u)
eb = [anc(v) for v in g.por_id if ok(v) and any(len(nb[u1] - {v, u1}) > 0 for u1 in nb[v])]
ed = [(anc(p["a"]), anc(p["b"])) for p in s._pares_ed() if apto(p["a"]) and apto(p["b"])]
ee = [anc(n) for n in g.por_id if g.anclas(n) and apto(n)]
pool = lambda xs: set().union(*xs)
P = {"E-A": pool(ea), "E-B": pool(eb), "E-D": pool([a | b for a, b in ed]), "E-E": pool(ee)}
N = len(set().union(*P.values()))
print({k: len(v) for k, v in P.items()}, "TOTAL", N)                    # 132 / 107 / 83 / 175 → 175
# (a) hipergeométrica uniforme
d = {k: comb(58, k) * comb(N - 58, 37 - k) / comb(N, 37) for k in range(0, 38)}
E = sum(k * p for k, p in d.items()); print("hiper E", round(E, 2), "P>=28", sum(p for k, p in d.items() if k >= 28))
# (b) simulación ponderada
rng = random.Random(20260818)          # (c) usa 20260817 y k=20 para A y B
def muestreo(k):
    out = list(rng.sample(ea, k)) + list(rng.sample(eb, k))
    for a, b in rng.sample(ed, k): out.append(a if rng.random() < 0.5 else b)
    return out + list(rng.sample(ee, k))
def hasta(K, m):
    rng.shuffle(m); u = set()
    for x in m:
        u |= x
        if len(u) >= K: break
    return u
res = sorted(len(hasta(58, muestreo(40)) & hasta(37, muestreo(20))) for _ in range(10000))
print("sim media", round(mean(res), 2), "sd", round(pstdev(res), 2), "IC95", res[250], res[9749],
      "P>=28", sum(1 for x in res if x >= 28) / 10000)                   # 24.17 / 2.45 / [19, 29] / 0.0848
```

Insumos: `data/experiment/grafo_v2/reensamblado_v3/kg.json` (sha `26fac8b4…`, verificado
por `comun.load_kg_raw`), `data/experiment/exploracion/mapa_territorio_quemado_5TOs_5sets.json`,
`data/experiment/ablacion_retrieval/pares/pares_v3.json` (para las 37 anclas propias).
Costo: USD 0.
