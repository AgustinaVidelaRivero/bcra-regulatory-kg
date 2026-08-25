# Laudo — Promoción de KG-Reextraído-r1 a grafo vigente

Fecha: 2026-08-25. Decisión de la autora, con revisión de mesa.

## Decisión

**KG-Reextraído-r1** (`kg.json` sha256 `0226e947…`, sellado en `185e042`,
medido en EV2 con cierre en `774acac`) **se promueve a grafo VIGENTE** del
proyecto: el grafo que sirve la app y sobre el que trabajan las unidades
nuevas, y el único editable — exclusivamente vía el circuito de refinamiento
con propuesta sellada + laudo (release r2, principio 9; en r1 no se corrige
nada).

La promoción es del **entregable**, no un veredicto de fidelidad: la tabla
definitiva de r1 quedó dentro de la banda de no-señal contra KG-Refinado y
así se declara (ver Fundamento). Ningún material EV2 se toca: los cuatro
grafos medidos quedan sellados con sus tablas.

## Fundamento

1. **Primer grafo del pipeline completo E0–E5.** KG-Refinado es Gen. 2 con
   correcciones manuales laudadas (C1–C7); r1 es la primera release
   reproducible de punta a punta (doble corrida byte-idéntica, `185e042`),
   que es lo que la tesis entrega como método.
2. **Tabla definitiva 6/26/8** (`774acac`): la mejor de las cuatro — primer
   grafo bajo 9 incorrectos y el de más correctos — **dentro de la banda de
   no-señal vs KG-Refinado (6/26/8 vs 5/26/9; diferencias de 1–2 preguntas
   no son señal, regla del plan)**. La promoción no se apoya en superioridad
   EV2; se apoya en que, a fidelidad indistinguible, r1 aporta todo lo demás.
3. **Juez validado contra la adjudicación de la autora**: muestra simétrica
   4/4 exacto, 15/15 por criterio, 0 sobre / 0 sub-acreditación (leído con
   las salvedades de
   `data/experiment/ev2_r1/adjudicacion/nota_episodios_adjudicacion.md`).
4. **Estructura requerida por A2 y la app**, que KG-Refinado no tiene:
   5.680 aristas `referencia` con evidencia (remisiones norma→norma,
   multi-hop real), esqueleto de contenedores, provenance rica
   (`chunk_id`, `paginas`, `ancestros`).

**Costo anotado (no se esconde):** cobertura de criterios 69 vs 73 de
KG-Refinado; el perfil causal de r1 mantiene la granularidad de ancla (H24:
7 anclas frontera E0 + 2 contenedor, censo de `6c5507b`) que solo se
resuelve en r2/E0, no por parche.

## Alcance y qué NO decide este laudo

- **El brazo KG de A2.1 NO se decide acá**: va dentro del pre-registro de
  A2.1, citando la tabla de `774acac` (principio 7: EV2 no se re-mide; el
  pre-registro elige brazo con la evidencia sellada).
- **Estado servido vs decisión**: el contenedor Neo4j y la app hoy sirven
  KG-Refinado. La migración a r1 se hace **declarada**, por el plan de carga
  (`data/experiment/neo4j/plan_carga_r1.md`), con sha verificado antes y
  después de la carga. La declaración operativa de `docs/tablero.md` §1 se
  actualiza en el commit que ejecute la migración; hasta entonces rige este
  laudo como decisión y KG-Refinado como estado servido.
- **EV1/CQ/CQN/CQN2 siguen quemados**; EV2 sellado. r1 se midió una sola vez.

## Registro técnico

- Entrada de r1 en `data/experiment/neo4j/grafos.py` (`KG_Reextraido_r1`,
  path `corpus_v2/salida_r1/kg.json`, sha `0226e947…`, 6.529 / 17.772,
  vista runtime por registro en memoria — precedente U-B1.8, sin editar
  módulos sellados). Prerrequisito de todo `cargar_kg.py`, cumplido en este
  commit.
- Plan de carga y migración: `data/experiment/neo4j/plan_carga_r1.md`.
