# Plan de carga de KG-Reextraído-r1 a Neo4j y migración declarada

Ejecuta el laudo de promoción (`docs/laudo_promocion_r1_vigente.md`): r1 es
el grafo vigente por decisión; este plan lo convierte en el grafo SERVIDO,
con verificación antes y después de cada paso. Hasta completar el paso 4, el
estado servido sigue siendo KG-Refinado (así lo declara el laudo).

Regla transversal: **nada se desaloja**. La db única de Community separa los
grafos por label (`:KG_Refinado` / `:KG_Reextraido` / `:KG_Reextraido_r1`);
KG-Refinado y KG-Reextraído permanecen cargados — A2.1 puede necesitar
cualquiera de los dos como brazo, y esa elección vive en el pre-registro de
A2.1, no acá.

## Paso 0 — prerrequisito (cumplido en este commit)

Entrada `KG_Reextraido_r1` en `grafos.py` con sha sellado `0226e947…`,
conteos 6.529 / 17.772 y vista runtime por registro en memoria
(`ev2_r1/code/comun_r1`, precedente U-B1.8). Verificado:
`verificar_sha("KG_Reextraido_r1")` pasa y `cargar_vista_runtime` carga
6.529 nodos.

## Paso 1 — carga (idempotente, no toca los labels existentes)

```
cd data/experiment/neo4j
.venv/bin/python -B cargar_kg.py --grafo KG_Reextraido_r1
```

`cargar_kg.py` debe: (a) llamar `verificar_sha` ANTES de escribir nada
(aborta si el kg.json no coincide con el sellado); (b) cargar bajo el label
`:KG_Reextraido_r1`; (c) crear el índice full-text
`nodos_fulltext_kg_reextraido_r1` con la MISMA definición (analyzer, campos)
que los índices existentes — firma v1 del banco intacta.

## Paso 2 — verificación post-carga (obligatoria, se pega en el reporte)

1. Conteos en Neo4j == sellados: `MATCH (n:KG_Reextraido_r1) RETURN count(n)`
   → 6.529; aristas entre nodos del label → 17.772.
2. Re-verificar el sha del kg.json DESPUÉS de la carga (la carga no debe
   haber tocado el archivo): `shasum -a 256 …/salida_r1/kg.json` == `0226e947…`.
3. Equivalencia de vistas (precedente A1.1): `test_equivalencia.py` sobre la
   muestra estándar de nodos, comparando la vista runtime de `grafos.py`
   contra lo servido por Neo4j (labels, tipos, provenance citable).
4. Los otros dos labels quedaron intactos: conteos de `:KG_Refinado`
   (4.469/8.073) y `:KG_Reextraido` (6.178/11.415) sin cambios.

## Paso 3 — switch declarado de la app

En `app/main.py`: agregar `("r1_vigente", …/salida_r1/kg.json)` como primera
entrada de `GRAFOS_EXPLICITOS` (la clave visible nueva convive con
`v3_vigente`, que no se borra), y registrar el `adapter_key` de r1 en
`ADAPTER_KEYS` (r1 tiene provenance primaria `{to, archivo, punto}`, como
KG-Reextraído — sin adapter la app no puede citar). Smoke de la app: una
consulta con cita verificable contra el PDF antes de dar por hecho el switch.

## Paso 4 — declaración

En el MISMO commit del switch: actualizar `docs/tablero.md` §1 (nombre
canónico KG-Reextraído-r1, ruta `salida_r1/kg.json`, sha `0226e947…`,
6.529/17.772, registro `GRAFOS_EXPLICITOS`, laudo
`docs/laudo_promocion_r1_vigente.md`, sello de medición `774acac`) y la nota
de que KG-Refinado pasa a grafo medido/sellado (deja de ser vigente, no se
borra ni se descarga del contenedor).

## Fe de erratas (U-MIG-r1, fase 1)

El paso 1 atribuía la creación del índice full-text a `cargar_kg.py`; la
creación de índices vive en `indices.py` desde A1.1 (se ejecutó
`indices.py --grafo KG_Reextraido_r1` como parte de la carga, sin cambios de
código). Detectado y declarado por el ejecutor de U-MIG-r1; el resto del
paso se ejecutó como estaba escrito.

## Qué NO hace este plan

- No elige el brazo KG de A2.1 (pre-registro de A2.1, principio 7).
- No edita módulos sellados ni el kg.json de ningún grafo.
- No borra nada de Neo4j ni de la app.
