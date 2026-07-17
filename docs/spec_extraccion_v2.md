# Spec de extracción v2 — Re-extracción con esquema de clases (Manera B)

**Estado:** v1.0, para laudo de Agustina. Tras laudo: commit a `docs/` y ejecución por unidades.
**Base empírica:** anatomía real del pipeline (informe Claude Code 16/07/2026 sobre `run_3_ppf_core/code/`) — esta spec referencia archivos y líneas reales, no supuestos.
**Mandatos que implementa:** Lucho: "mismo pipeline, actualizar el esquema y correrlo de nuevo", en branch nueva. Juan: esquema v2 = re-extracción completa. Laudos de Agustina: Manera B (esqueleto inyectado + enum + cuarentena), listas por-TO, caché versionado, defaults de las tres ramas.

---

## 0. Resumen en cinco líneas

Se re-extraen los 5 TOs del subset con el mismo pipeline de run_3, cambiando UNA capa: los sujetos. El árbol de clases y las listas de alcance se **inyectan** desde un archivo fijo (`esquema_v2_clases.json`); el LLM ya no crea nodos de sujeto — **elige** el sujeto de un catálogo cerrado (enum en el tool schema), con válvula de cuarentena para sujetos fuera de catálogo. Todo lo demás (chunking, extracción de normas/operaciones, provenance, post-proceso de firmas) queda igual. Salida: `grafo_v2/kg.json` en branch nueva, comparable contra run_3 (baseline intocable).

## 1. Alcance y no-alcance

**Cambia:** `schema.py` (vocabulario v2), `extract.py` (tool schema con catálogo de sujetos, mensaje de usuario con lista por-TO, namespace de caché), `assemble.py` (carga del esqueleto, cuarentena, apagado del merge difuso de sujetos). **Archivo nuevo:** `esquema_v2_clases.json`.
**NO cambia:** `chunker.py` (idéntico), la mecánica de caché/retries/concurrencia (salvo namespace), la estructura del kg.json de salida, la provenance por nodo y arista.
**NO se toca jamás:** `data/experiment/run_3_ppf_core/` (baseline), harness, loader, juez, verificador, frozen eval. La app (frente T) consume el grafo nuevo vía loader sin cambios.
**Branch:** `extraccion-v2` (mandato de Lucho). El código v2 vive en `data/experiment/grafo_v2/code/` (copia del de run_3 + cambios de esta spec), para que run_3/code quede como artefacto histórico intacto.

## 2. Vocabulario v2: 7 types × 16 relaciones

**Delta declarado respecto del documento de diseño:** el diseño A-aditivo hablaba de "8 types (7 + Clase)" porque *agregaba* sobre un grafo donde los 130 nodos EntidadFinanciera persistían. Con re-extracción, ese compromiso desaparece y se corrige el nombre de raíz: **el type `EntidadFinanciera` se reemplaza por `Sujeto`** — que es lo que el censo demostró que ese type siempre fue. Resultado: 7 types, no 8.

**Types (7):** `Obligacion`, `Restriccion`, `Excepcion`, `Operacion`, `Comunicacion`, `TextoOrdenado` (los 6, sin cambios) + **`Sujeto`** (nuevo, reemplaza a EntidadFinanciera). Los nodos Sujeto provienen SOLO de dos fuentes: el esqueleto inyectado y la cuarentena. El LLM no puede emitir entidades type Sujeto (no está en su enum de entidades).

**Properties de Sujeto:** `nivel` ∈ {`clase`, `rol`, `instancia`, `propuesto`}; `jurisdiccion` ∈ {`local`, `exterior`} (opcional; default local — implementa el laudo de la rama exterior); `alias` (lista de strings, para alcanzabilidad léxica: p. ej. "Operador de cambio" como alias de EntidadCambiaria, "Superintendencia..." como alias de SEFyC); `cuarentena` (bool, solo en propuestos).

**Relaciones (16):** las 12 de v1 con firmas actualizadas donde decía EntidadFinanciera:
- `aplica_a`: {Obligacion, Restriccion} → Sujeto
- `ejecuta`: Sujeto → Operacion
- las otras 10: idénticas a v1.

Más 4 nuevas, **de esqueleto exclusivamente** (el LLM no las puede emitir; solo assemble las escribe):
- `subclase_de`: Sujeto → Sujeto (acíclica, un solo padre)
- `miembro_de`: Sujeto → Sujeto[nivel=rol]
- `instancia_de`: Sujeto[nivel=instancia] → Sujeto[nivel=clase]
- `parte_de`: Sujeto[nivel=instancia] → Sujeto[nivel=instancia] (uso único en v2.0: SEFyC → BCRA)

**Actualización de shapes (versionada):** S3 usa la matriz v2 (16 firmas + las combinaciones de establecida_en = 19 celdas); S6 admite `source_doc` ∈ {los 5 TOs} ∪ {"esquema_v2_clases.json"} (los nodos de esqueleto abstractos llevan esa fuente); reglas nuevas activables: S13–S17 (capa 3) quedan implementables porque el árbol ahora está EN el grafo.

## 3. `esquema_v2_clases.json` — el esqueleto

Archivo versionado en `data/experiment/grafo_v2/esquema_v2_clases.json`. Formato:

```json
{
  "version": "2.0",
  "clases": [
    {"id": "Sujeto_entidad_financiera", "label": "Entidades financieras",
     "nivel": "clase", "padre": "Sujeto_sujeto_regulado",
     "disjunta_con": ["Sujeto_entidad_cambiaria", "Sujeto_proveedor_servicios_pago"],
     "alias": [],
     "provenance": {"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
                    "location": "Punto 1.1.2.1"}}
  ],
  "roles": [
    {"id": "Sujeto_rol_sujeto_obligado_proteccion", "label": "Sujetos obligados (Protección)",
     "nivel": "rol", "to": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "miembros": ["Sujeto_entidad_financiera", "Sujeto_entidad_cambiaria", "..."],
     "provenance": {"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
                    "location": "Punto 1.1.2"}}
  ]
}
```

**Catálogo v2.0** (deriva del árbol laudado, documento de diseño Sección 1.2 + laudos de ramas; anclajes ahí documentados — acá solo la estructura):

- **Raíz y abstractas:** Sujeto (root) · SujetoRegulado · Contraparte · OrganismoPublico · Estructura *(laudo rama vehículos: rama propia bajo root)*. Provenance de abstractas: `esquema_v2_clases.json`.
- **SujetoRegulado:** EntidadFinanciera (⊥ EntidadCambiaria ⊥ ProveedorDeServiciosDePago) → Banco → BancoComercial; CompañiaFinanciera; CajaDeCredito; CajaDeCreditoCooperativa · EntidadCambiaria (alias: "Operador de cambio", "Operadores de cambio") → CasaDeCambio; AgenciaDeCambio · ProveedorDeServiciosDePago → PSPCP; PSI_BilleteraDigital · ProveedorNoFinancieroDeCredito → EmpresaNoFinancieraEmisoraDeTarjetas · PSCPP · FiduciarioDeFideicomisoFinanciero · SociedadDeGarantiaReciproca · FondoDeGarantiaPublico · EntidadDeContraparteCentral → CCPCalificada (alias: "QCCP") ⊥ CCPNoCalificada · MiembroCompensador · ECAI · **SujetoDelPerimetroConsolidado** *(laudo rama perímetro: rama bajo SujetoRegulado)* → Aseguradora; EntidadBursatil; EmpresaDeServiciosComplementarios.
- **Contraparte:** Cliente → PersonaHumana ⊥ PersonaJuridica ⊥ Universalidad · Deudor (atributos cartera/situación — NO subclases) · UsuarioDeServiciosFinancieros · Importador → ImportadorDeBienes; ImportadorDeServicios · Exportador · MiPyME · EmisorDeTitulosDeDeuda · VPU_RIGI · BeneficiarioEconomiaConocimiento · SectorPublicoNoFinanciero ⊥ SectorPrivadoNoFinanciero · AcreedorDelExterior.
- **Estructura:** Fideicomiso → FideicomisoFinanciero · SociedadDePropositoEspecial · FondoComunDeInversion.
- **OrganismoPublico:** subclases GobiernoLocal · OrganismoInternacional → BancoMultilateralDeDesarrollo · AgenciaOficialDeCredito · AutoridadNacionalDeAplicacion; instancias (nivel=instancia, con instancia_de): **BCRA** · **SEFyC** (alias: "Superintendencia de Entidades Financieras y Cambiarias"; parte_de → BCRA) · ARCA (alias: "AFIP") · MinisterioDeEconomia · SecretariaDeEnergia · SecretariaDeComercio · SecretariaDeTransporte.
- **Excluidas de v2.0 con marca:** UIF y toda clase `[FUERA DE CORPUS]` — entran en el escalado cuando su TO (p. ej. prevención de lavado) ingrese, con su anclaje real. Motivo: S4/S6 exigen provenance a fuente del corpus activo.
- **Jurisdicción como atributo** *(laudo rama exterior)*: no existen clases "del exterior"; los sujetos del exterior del censo v1 (bancos del exterior, EF extranjeras) se representan como la clase local + `jurisdiccion: "exterior"`. El catálogo agrega los alias correspondientes a EntidadFinanciera y EntidadCambiaria para la asignación.

**Roles v2.0 (uno por TO, con miembros):** SujetoObligado_Proteccion (7 miembros, Prot 1.1.2) · EntidadAutorizada_Exterior (EF ∪ EC, Ext 1.1) · ObligadoAClasificar_Clasificacion (EF + PNFC + Fiduciario + SGR + FondoGarantía + PSCPP, Clasif S.1+S.10) · EntidadComprendida_RegInf (EF, RI S.2) · AlcanceCapMin (EF, CapMin S.1).

## 4. Cambios por archivo

**4.1 `schema.py`:** ENTITY_TYPES del LLM pasa a 6 (sin sujeto — el LLM no crea sujetos). PREDICATES visibles al LLM: los 12. DOMAIN_RANGE: matriz v2 (aplica_a/ejecuta contra Sujeto). Constantes nuevas: SUJETOS_CATALOGO (lista de ids cargada de esquema_v2_clases.json en import), RELACIONES_ESQUELETO (las 4, para assemble).

**4.2 `extract.py`:**
- **Tool schema:** en las tripletas cuyo predicado sea `aplica_a` o `ejecuta`, el campo del sujeto es `sujeto_id` con `"enum": SUJETOS_CATALOGO` — enforcement duro: el LLM no puede inventar sujetos. Campo alternativo mutuamente excluyente: `sujeto_propuesto` (string libre) + `sujeto_propuesto_padre_sugerido` (enum del catálogo, opcional) → cuarentena.
- **SYSTEM_PROMPT:** se reescribe la sección de EntidadFinanciera por la instrucción de catálogo: "El sujeto de aplica_a/ejecuta se ELIGE del catálogo provisto; si el texto nombra un sujeto que no matchea ninguna entrada ni sus alias, usá sujeto_propuesto". Se agrega el catálogo compacto (id + label + alias) al prompt para que el modelo elija con contexto. El resto del prompt (reglas, ejemplos negativos, regula/prohibe/limita) queda igual.
- **Mensaje de usuario (por chunk):** se interpola además la **lista de alcance del TO del chunk**: "Este TO alcanza a: <rol_id> = {miembros}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, usá <rol_id> como sujeto." — mata la contaminación de vocabulario de raíz.
- **Caché:** directorio nuevo `cache_v2/` Y la key incluye `sha256(SYSTEM_PROMPT)[:12]` — doble candado contra hits del prompt viejo. (Trampa documentada: el caché v1 se indexa por `chunk_id|texto` sin prompt.)
- Tracker: corregir el double-count de cache-hits (no sumar tokens en hit) — arreglo de una línea, mejora la contabilidad del escalado.

**4.3 `assemble.py`:**
- **Paso 0 nuevo:** cargar `esquema_v2_clases.json` → crear los nodos Sujeto del esqueleto + aristas subclase_de/miembro_de/instancia_de/parte_de, ANTES de procesar el caché.
- **Resolución de sujetos:** `sujeto_id` referencia directa (no hay merge); `sujeto_propuesto` → nodo Sujeto nivel=propuesto, cuarentena=true, id `Sujeto_propuesto_<slug>`, dedup exacto por slug, y entrada en el reporte `cuarentena.json` (label propuesto, padre sugerido, chunks de origen, conteo).
- **Se APAGA** el merge difuso de EntidadFinanciera (líneas 227-234 y la pasada 304-369 del assemble v1): sin extracción libre de sujetos, no hay nada que mergear — el mecanismo que fabricó los duplicados muere.
- Validación dominio/rango: matriz v2. Reporte assemble: agrega sección de cuarentena y conteo de aristas hacia esqueleto vs. propuestos.

## 5. Criterios de aceptación (medibles, pre-registrados)

Sobre el smoke y sobre el subset completo:
1. `shapes_validator.py` con matriz v2 sobre el grafo resultante: S1–S6 PASS (con S6 ampliada según §2).
2. Cero nodos con type EntidadFinanciera; todo nodo Sujeto tiene nivel ∈ {clase, rol, instancia, propuesto}.
3. El 100% de los destinos de aplica_a y ejecuta son ids del esqueleto o nodos en cuarentena — cero sujetos "sueltos".
4. `cuarentena.json` existe (puede estar vacío); en el smoke de Protección se espera cuarentena baja (el catálogo se diseñó mirando ese TO).
5. `cache_v2/` es el único caché tocado; `run_3_ppf_core/` byte-idéntico (git status limpio fuera de la branch de trabajo).
6. El loader carga el grafo v2 sin error y el harness responde una pregunta manual de humo contra él. **[VERIFICAR EN REPO — pregunta lateral del primer prompt: ¿loader.py o harness.py hardcodean el string "EntidadFinanciera" en algún lugar (normalización, prompts de tools)? Si sí, listar las líneas — se decide el tratamiento antes de la unidad 2.]**
7. Pregunta lateral 2 (arrastrada): provenance completa de los nodos v1 #99 y #126 (emisoras ambiguas) para cerrar su clase.

## 6. Plan de ejecución por unidades (prompts separados, revisión entre cada una)

- **U1:** `esquema_v2_clases.json` completo (catálogo §3 con anclajes del documento de diseño) + preguntas laterales de §5.6–5.7. → revisión acá.
- **U2:** `schema.py` + `extract.py` v2 (sin correr nada). → revisión de diffs.
- **U3:** `assemble.py` v2 (sin correr). → revisión.
- **U4:** **Smoke Protección** (37 chunks, ~USD 0,60) + shapes + reporte. → COMPUERTA: revisión profunda del mini-grafo (muestreo de aplica_a, lectura de cuarentena). Nada avanza sin este OK.
- **U5:** subset completo (5 TOs) → `grafo_v2/kg.json` + shapes + cuarentena. → revisión → commit y medición (Fase 3 del plan general).

## 7. Escalado — Fase 0 y presupuesto (informativo, se ejecuta post-Fase 3)

- **Fase 0 "censo de alcances":** script barato que extrae de cada uno de los 161 PDFs su sección de alcance (primeras páginas; heurística: encabezados "Sujetos/Entidades comprendidas/obligadas/alcanzadas") y compila un documento único → lectura humana en una tarde → pre-poblado de roles y clases nuevas por tanda ANTES de extraer; la cuarentena queda como red, no como mecanismo principal.
- **Presupuesto medido:** subset 15,4 MB = 508 llamadas = USD 7,82 registrados. Corpus 173,5 MB ≈ 11,3× → ~5.700 llamadas ≈ USD 90 lineal; con varianza de densidad (15–78 chunks/MB entre TOs), retries e iteraciones: **orden USD 150–250 total**. Restricciones reales: tiempo humano del loop de alcances y wall-time (CONCURRENCY=2 → evaluar subirla en la tanda grande).
- **Tandas propuestas a Lucho:** A = núcleo normativo (~114 TOs no-`ri_*`); B = familia `ri_*` (47) si aporta. Validación del grafo grande: shapes, no adjudicación humana. La medición de fidelidad de la tesis queda en el subset (pendiente: confirmación de una línea con Lucho).

## 8. Integración con el refinamiento y medición

- run_3 = baseline intocable. Escalón 1: run_3 vs. grafo_v2 (misma frozen eval, mismo juez, verificador congelado atribuyendo causas; seguimiento del destino de cada falla diagnosticada — las de alcanzabilidad_kg y las del genérico deberían desaparecer; puede no pasar, y se reporta igual).
- El reporte de shapes sobre grafo_v2 = backlog de entrada del pipeline kg-refinement (capa de contenido). Escalón 2: grafo_v2 vs. grafo_v2_refinado.
- Skills (agente, verificador, kg-refinement): actualización por referencia — un archivo de esquema v2 citado, no reescritura de skills. Se hace entre U5 y la medición.
