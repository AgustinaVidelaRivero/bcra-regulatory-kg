# Diseño de esquema v2 — Jerarquía de clases para el KG regulatorio BCRA

**Estado:** Secciones 1–6 completas. Opción B **implementada y corrida** (14/07/2026): `scripts/shapes_validator.py`, reporte `reports/shapes_run_3_v0.md` — 6 reglas PASS, 6 con violaciones medidas (103 nodos duplicados, 123 sin anclaje documental, 755 sin sujeto explícito, 27 excepciones huérfanas, 53 con doble key de descripción).
**Fecha:** 14/07/2026 (última actualización: cierre de Secciones 4–6)
**Alcance:** documento de diseño en papel. No modifica run_3 (congelado), ni el harness, ni el juez, ni la frozen eval. Toda intervención sobre el grafo es una propuesta futura del pipeline de refinamiento (secuencia B→A acordada con mentores).
**Fuentes:** los 5 Textos Ordenados del corpus (citas textuales verificadas contra los PDFs) y el censo de vocabulario sobre `data/experiment/run_3_ppf_core/kg.json` y `data/experiment/run_5_hybrid/kg.json` (informe Claude Code del 14/07/2026, verificado de forma independiente; `git status` limpio post-censo).

**Convenciones de marcado:**
- `[FUERA DE CORPUS]` — clase/instancia no nombrada por los 5 TOs; se incluye por diseño de dominio y se declara explícitamente ante mentores.
- `[DUP]` — cluster de nodos casi-duplicados detectado en run_3 (presa de la regla de unicidad, Sección 3).
- `⊥` — disyunción entre clases.
- Los números de nodo (#1–#130) refieren al censo completo de nodos type EntidadFinanciera de run_3 (Anexo 1.A).

---

## Sección 1 — Árbol de clases (v1)

### 1.0 Por qué un árbol, y por qué ahora

El diagnóstico de los mentores (Luciano: "al esquema le falta la capa de clases; en un KG las clases son casi más importantes que las entidades"; Micaela: subclases explícitas + reglas por nivel + validación determinística) dejó de ser una opinión de diseño el 14/07/2026, cuando el censo del grafo congelado lo convirtió en defecto medido:

1. **El type `EntidadFinanciera` de run_3 no contiene entidades financieras: contiene el universo completo de sujetos del dominio, aplastado.** Entre sus 130 nodos están el BCRA (#72), gobiernos locales (#73), organismos internacionales (#44), personas humanas (#22), residentes (#88), no residentes (#94), deudores (#96), MiPyMEs (#23), importadores (#70), exportadores (#95) y usuarios de servicios financieros (#122). Es la clase raíz **Sujeto** con la etiqueta equivocada y cero estructura interna.
2. **El 68% de las aristas `aplica_a` (991 de 1.464) termina en un único nodo genérico, "Sujetos obligados" (#65).** Dos tercios de la conectividad normativa del grafo no informa a *cuál* de los sujetos aplica cada norma. El grafo ya intentó representar el rol "sujeto obligado" — informalmente, sin miembros y sin herencia.
3. **run_3 tiene ~15 clusters de nodos duplicados** (Anexo 1.B): grupos A/B/C por duplicado, fiduciarios por triplicado, emisoras de tarjetas en cuatro variantes, VPU en cinco, y un par (#48/#49) con label y categoria cruzados entre sí. Sin clases ni reglas de unicidad, los duplicados proliferan — y ya proliferaron en el grafo congelado, no solo en run_5.

Consecuencia de diseño: **el árbol no agrega una capa nueva al grafo — formaliza la que la extracción ya pobló a ciegas.** La subtipificación existe hoy, escondida en `properties.categoria` y en los labels; el árbol la hace navegable, heredable y validable.

### 1.1 Decisión estructural: dos ejes (laudada — Decisión 1)

El corpus usa dos vocabularios de sujetos que el diseño separa:

**Eje A — Clases ontológicas: qué ES el sujeto.** Identidad estable (un banco comercial ES un banco ES una entidad financiera). Acá viven `subclase_de`, la herencia taxonómica y las disyunciones.

**Eje B — Roles: qué papel cumple el sujeto frente a una norma.** Dos sabores:

- **Roles de alcance normativo**: cada TO define su propio sujeto colectivo con término técnico y enumeración propia. Son clases-unión sobre el eje A, no clases hermanas:
  | Rol | TO que lo define | Anclaje | Miembros |
  |---|---|---|---|
  | EntidadAutorizada ("entidades") | Exterior | 1.1: "entidades financieras o cambiarias autorizadas a operar en cambios por el Banco Central de la República Argentina (BCRA), en adelante 'entidades'" | EntidadFinanciera ∪ EntidadCambiaria |
  | SujetoObligado | Protección | 1.1.2 (enumeración cerrada de 7) | EF, OperadorDeCambio, Fiduciario, EmisoraNoFinanciera, PNFC, PSPCP, PSI |
  | ObligadoAClasificar | Clasificación | Secciones 1 y 10 | EF + PNFC + Fiduciario + SGR + FondoGarantíaPúblico + PSCPP |
  | EntidadComprendida | Rég. Informativo | Sección 2 + 10.1.1: "deberá ser cumplido por todas las entidades financieras" | EntidadFinanciera |
  | SujetoAlcanzado (relevamiento) | Exterior | 1.9 | [VERIFICAR EN REPO: población exacta] |

- **Roles funcionales**: funciones que una entidad del eje A desempeña en una operatoria (entidad encargada del seguimiento, entidad nominada, entidad liquidadora, cedente, originante, interviniente...). Exterior los asigna masivamente. Son roles con dominio = EntidadAutorizada (o subclase), no tipos de entidad.

**Regla de oro del diseño:** un nodo del eje A puede portar N roles del eje B; un rol nunca es subclase ni superclase de una clase ontológica. La herencia de `aplica_a` funciona distinto según el destino (se especifica en la Sección 2): hacia clase ontológica baja por `subclase_de`; hacia rol baja por membresía y después por `subclase_de`.

**Evidencia que valida el eje B:** el nodo #65 "Sujetos obligados" (991 aristas entrantes) y el #67 "Sujetos alcanzados" ya existen en run_3 como nodos — el grafo pide esta estructura a gritos.

### 1.2 El árbol (v1, laudado)

```
Sujeto (ROOT)  ← hoy: el type "EntidadFinanciera" de run_3, mal etiquetado
│
├── SujetoRegulado                                      [abstracta]
│   │
│   ├── EntidadFinanciera            ⊥ EntidadCambiaria, ⊥ ProveedorDeServiciosDePago
│   │   │  Anclaje: Exterior 1.6 (Ley de Entidades Financieras); Protección 1.1.2.1
│   │   │  Atributos (no subclases): grupo ∈ {A,B,C} · estado ∈ {nueva, en funcionamiento}
│   │   ├── Banco                     Anclaje: CapMin 1.2 "Según la clase de entidad...
│   │   │   │                         exigencias básicas: Bancos / Restantes entidades"
│   │   │   └── BancoComercial        Población: #130. (BancoDeInversión y BancoHipotecario:
│   │   │                             sin población en el grafo → trabajo futuro, Ley 21.526)
│   │   ├── CompañíaFinanciera        Anclaje: CapMin 1.2. Población: #3
│   │   ├── CajaDeCrédito             Población: #8
│   │   └── CajaDeCréditoCooperativa  Anclaje: CapMin 1.2 "(salvo Cajas de Crédito
│   │                                 Cooperativas)". Población: #2
│   │
│   ├── EntidadCambiaria             ⊥ EntidadFinanciera
│   │   │  Anclaje disyunción: Exterior 5.4.2.2 "según se trate de entidades financieras
│   │   │  o cambiarias, respectivamente". Población: #18
│   │   │  Alias léxico: "Operador de cambio" (Protección 1.1.2.2; régimen Decreto 27/18).
│   │   │  Población del alias: #119
│   │   ├── CasaDeCambio              Anclaje: Exterior 5.9.2. Población: #74
│   │   ├── AgenciaDeCambio           Anclaje: Exterior 5.9.2. Población: #113
│   │   └── OficinaDeCambio           [anclaje débil: solo título Com. A 6443] [sin población]
│   │
│   ├── ProveedorDeServiciosDePago   ⊥ EntidadFinanciera
│   │   ├── PSPCP                     Anclaje: Protección 1.1.2.6. Población: #120
│   │   └── PSI_BilleteraDigital      Anclaje: Protección 1.1.2.7. Población: #121
│   │
│   ├── ProveedorNoFinancieroDeCrédito (PNFC)
│   │   │  Anclaje: Protección 1.1.2.5; Clasificación 10.1. Población: #52
│   │   └── EmpresaNoFinancieraEmisoraDeTarjetas   (laudada subclase — Decisión 4a:
│   │          el "Otros proveedores..." de Protección 1.1.2.5 y Clasificación 10.1
│   │          implica que las emisoras SON PNFC). Población: #66, #100 [DUP]
│   │
│   ├── PSCPP                         Anclaje: Clasificación 10.4. Población: #54
│   ├── FiduciarioDeFideicomisoFinanciero
│   │      Anclaje: Protección 1.1.2.3; Clasificación 10.2. Población: #25,#53,#97 [DUP ×3]
│   ├── SociedadDeGarantíaRecíproca   Anclaje: Clasificación 10.3. Población: #41
│   ├── FondoDeGarantíaPúblico        Anclaje: Clasificación 10.3. Población: #42
│   │
│   ├── EntidadDeContraparteCentral (CCP)     (laudada — Decisión 4b)
│   │   │  Anclaje: CapMin ("entidades de contraparte central"). Población: #32, #38 [DUP]
│   │   ├── CCPCalificada  ⊥ CCPNoCalificada  Población: #36; #33 (QCCP) [DUP probable con #36]
│   │   └── CCPNoCalificada                    Población: #37
│   ├── MiembroCompensador            Anclaje: CapMin. Población: #34
│   └── ECAI                          Anclaje: CapMin (calificadoras reconocidas). Población: #6
│
├── Contraparte                                          [abstracta]
│   ├── Cliente                       Anclaje: Exterior 1.2 "personas humanas o jurídicas
│   │   │                             y los patrimonios y otras universalidades, en
│   │   │                             adelante 'clientes'". Población: #35, #101, #64
│   │   ├── PersonaHumana ⊥ PersonaJurídica ⊥ Universalidad   Población: #22; #68, #90; #92
│   │   ├── (dimensión residencia)    Residente ⊥ NoResidente — ATRIBUTO, no subclase.
│   │   │                             Población de los nodos actuales: #88, #94, #101
│   │   └── Deudor                    Anclaje: Clasificación (todo el TO). Población: #96
│   │          cartera ∈ {comercial, consumo o vivienda} — ATRIBUTO (Clasif. 5.1)
│   │          situación ∈ {1..6} — ESTADO mutable (Clasif. 7.2, 7.3), nunca subclase
│   │          Nodo actual #58 "Deudores cartera comercial" = Deudor + atributo
│   ├── UsuarioDeServiciosFinancieros Anclaje: Protección 1.1.1. Población: #122
│   ├── Importador                    Población: #70; subclases con anclaje en Exterior:
│   │       ImportadorDeBienes (#102) · ImportadorDeServicios (#105)
│   ├── Exportador                    Población: #95
│   ├── MiPyME                        Anclaje: Clasificación 10.3. Población: #23, #123 [DUP]
│   ├── EmisorDeTítulosDeDeuda        Población: #87, #98 [DUP probable]
│   ├── VPU (Vehículo de Proyecto Único, RIGI)
│   │       Anclaje: Exterior Sección 14. Población: #78,#79,#80,#81,#84 [DUP ×5]
│   ├── BeneficiarioEconomíaDelConocimiento  Población: #85, #89 [DUP]
│   ├── SectorPúblicoNoFinanciero ⊥ SectorPrivadoNoFinanciero
│   │       Anclaje: CapMin. Población: #39; #21
│   └── (otros con población menor: #7, #29, #30, #45, #76, #86, #116 — ver Anexo 1.A)
│
├── OrganismoPúblico                  ⊥ SujetoRegulado (ver nota al pie)
│   ├── BCRA                          [INSTANCIA] Anclaje: Exterior 1.1; Protección 1.2.
│   │   │                             Población: #72 (hoy con categoria "banco central")
│   │   └── SEFyC  — parte_de → BCRA  (laudada nodo propio — Decisión 3)
│   │          Anclaje: Clasificación 5.1.1.2 "...(SEFyC)"; Exterior 3.17.4.2.
│   │          Presencia en run_3: 19 labels, 47 descriptions.
│   │          Alias léxico: "Superintendencia de Entidades Financieras y Cambiarias".
│   │          Gerencias Principales: NO son nodos en v0 (presencia débil: 2 labels,
│   │          11 descriptions reales) — quedan como menciones dentro de BCRA.
│   ├── ARCA (ex AFIP)                [INSTANCIA] Anclaje: Exterior (conteo word-boundary:
│   │                                 2 labels, 7 descriptions). [sin nodo propio hoy]
│   ├── MinisterioDeEconomía          [INSTANCIA] Anclaje: Exterior. [sin nodo propio hoy]
│   ├── SecretaríaDeEnergía / DeComercio / DeTransporte  [INSTANCIAS] Anclaje: Exterior
│   ├── AutoridadNacionalDeAplicación Anclaje: Protección 1.3
│   ├── GobiernoLocal                 Población: #73
│   ├── OrganismoInternacional        Población: #44 · BancoMultilateralDeDesarrollo: #43
│   ├── AgenciaOficialDeCrédito       Población: #77
│   └── UIF                           [FUERA DE CORPUS — 0 menciones en los 5 TOs y 0 en
│                                     ambos grafos. Se incluye por completitud del dominio
│                                     con marca explícita; tendrá 0 aristas hasta que
│                                     ingrese otro TO al corpus.]
│
└── Roles (eje B — no son clases ontológicas; se listan acá por completitud del censo)
    ├── SujetoObligado (Protección)        Población: #65 — 991 aristas aplica_a entrantes
    ├── SujetoAlcanzado (Exterior 1.9)     Población: #67
    ├── PersonaAutorizada                  Población: #83
    └── Roles funcionales de Exterior      Población: #26,#27,#31,#56,#69,#71,#75,#82,
        (encargada de seguimiento, nominada,  #103,#104,#106,#111,#114,#115,#117,#118
         liquidadora, cedente, originante,    [DUPs internos: ver Anexo 1.B]
         interviniente, SEPAIMPO, ...)
```

**Nota sobre OrganismoPúblico ⊥ SujetoRegulado:** la disyunción vale entre *ser* organismo y *ser* entidad regulada, no entre organismo y Contraparte: el SectorPúblicoNoFinanciero es contraparte de crédito en CapMin. Por eso SectorPúblicoNoFinanciero vive bajo Contraparte y no bajo OrganismoPúblico — mismo mundo, roles distintos (otra aplicación del eje A/B).

**Casos fuera de árbol detectados por el censo (mal tipificados en run_3):**
- #125 "Casas operativas": no es un sujeto — es el punto físico de atención al usuario (Protección 2.2.1: "puntos de atención al usuario (casas operativas)"). Nodo mal tipificado; candidato a re-tipificación o exclusión en refinamiento.
- #124 "Entidades financieras emisoras de tarjetas de crédito": no va bajo PNFC (es *financiera*) — es EntidadFinanciera + rol funcional emisor. Distinta de #66/#100 (no financieras).
- #15, #16/#19 [DUP], #20, #17: empresas de servicios complementarios, aseguradoras, bursátiles — sujetos del perímetro de supervisión consolidada (CapMin), no entidades financieras. Rama menor a resolver en Sección 2 [pregunta abierta para Lucho].

### 1.3 Registro de decisiones (laudos)

| # | Decisión | Laudo | Fecha | Fundamento |
|---|---|---|---|---|
| 1 | Separación eje A (clases) / eje B (roles) | **Aceptada** | 14/07/2026 | Única estructura que sostiene disyunciones + reglas por nivel a la vez; el corpus define los roles explícitamente (Sección 1 de cada TO); el nodo #65 con 68% del tráfico `aplica_a` la valida empíricamente |
| 2 | Subclases de Banco | **Solo BancoComercial** | 14/07/2026 | Criterio pre-registrado "aparece en el grafo → entra": BancoComercial tiene población (#130); Inversión e Hipotecario, cero menciones → trabajo futuro (Ley 21.526) |
| 3 | SEFyC | **Nodo propio, `parte_de → BCRA`** | 14/07/2026 | 19 labels + 47 descriptions en run_3; agencia propia en el corpus. Gerencias: no (2/11, débil) |
| 4a | Emisoras de tarjetas vs PNFC | **Subclase de PNFC** | 14/07/2026 | El "**Otros** proveedores no financieros de crédito" de Protección 1.1.2.5 (tras enumerar emisoras en 1.1.2.4) y de Clasificación 10.1 implica que las emisoras SON PNFC |
| 4b | CCP | **Clase propia bajo SujetoRegulado, con subclases Calificada ⊥ NoCalificada** | 14/07/2026 | Población real: #32, #33, #36, #37, #38 + MiembroCompensador #34; CapMin le impone exigencias → regulada |

**Criterio pre-registrado usado en 2, 3 y 4b (definido antes de ver el censo):** una clase entra al árbol v1 si tiene población o menciones en run_3; si no, se documenta como trabajo futuro. Excepción explícita y marcada: UIF ([FUERA DE CORPUS], incluida por completitud de dominio).

### 1.4 Qué habilita esta sección (forward references)

- **Sección 2** (semántica de predicados): la regla de herencia de `aplica_a` según destino clase/rol; el destino dominante a refactorizar es el nodo #65.
- **Sección 3** (shapes caseras): las disyunciones del árbol + la regla de unicidad ya tienen presa medible — los ~15 clusters del Anexo 1.B y el par cruzado #48/#49.
- **Sección 4** (decisión metadato vs. grafo navegable): el mapeo del Anexo 1.A es el costo real de la opción "navegable" — se re-tipifican ~130 nodos, no 4.050.
- **Taxonomía de defectos (verificador)**: los hallazgos del censo instancian estructural_kg (type-bolsa), alcanzabilidad_kg (alias Superintendencia/SEFyC, singular/plural en labels) y contenido_kg (label/categoria cruzados en #48/#49).

---

## Anexo 1.A — Mapeo de los 130 nodos EntidadFinanciera de run_3 al árbol v1

Fuente: censo Claude Code 14/07/2026 (P1), lista completa verificada (130/130). Formato: #nodo → clase o tratamiento propuesto.

**→ EntidadFinanciera y subclases:** #1 (Banco) · #130 (BancoComercial) · #3 (CompañíaFinanciera) · #8 (CajaDeCrédito) · #2 (CajaDeCréditoCooperativa)
**→ atributos de EntidadFinanciera (no clases):** #4, #5 (estado: nueva / en funcionamiento) · #46, #47, #51 [DUP], #10, #13 [DUP], #11, #128 [DUP], #12, #129 [DUP] (grupo: 1/2/A/B/C — atributo `grupo`)
**→ EntidadCambiaria y subclases:** #18 (la clase) · #119 (alias OperadorDeCambio) · #74 (CasaDeCambio) · #113 (AgenciaDeCambio)
**→ ProveedorDeServiciosDePago:** #120 (PSPCP) · #121 (PSI)
**→ PNFC y subclase:** #52 (PNFC) · #66, #100 [DUP] (EmisoraNoFinanciera) · #99, #126 (emisoras ambiguas — [VERIFICAR EN REPO: provenance para decidir si financiera o no financiera])
**→ PSCPP:** #54
**→ Fiduciario:** #25, #53, #97 [DUP ×3]
**→ SGR / FondoGarantía:** #41 · #42
**→ CCP y satélites:** #32, #38 [DUP] (CCP) · #36, #33 [DUP probable] (CCPCalificada/QCCP) · #37 (CCPNoCalificada) · #34 (MiembroCompensador) · #6 (ECAI)
**→ Contraparte / Cliente:** #35, #101, #64 (Cliente) · #22 (PersonaHumana) · #68, #90 (PersonaJurídica) · #92 (Universalidad) · #88, #94 (residencia — atributo) · #96 (Deudor) · #58 (Deudor + cartera comercial) · #7 (cliente actividad agrícola) · #122 (UsuarioDeServiciosFinancieros) · #127 (AsociaciónDeConsumidores)
**→ Contraparte / comercio exterior y mercado de capitales:** #70, #102, #105 (Importador y subclases) · #95 (Exportador) · #87, #98 [DUP probable] (EmisorDeTítulos) · #29 (Inversor) · #30 (AcreedorInicial) · #116 (AcreedorDelExterior) · #86 (ProveedorTurismoInternacional) · #76 (EmpresaAeronavegación) · #85, #89 [DUP] (BeneficiarioEconomíaConocimiento) · #78, #79, #80, #81, #84 [DUP ×5] (VPU) · #23, #123 [DUP] (MiPyME) · #21 (SectorPrivadoNoFinanciero) · #45 (EmpresaConGradoInversión)
**→ OrganismoPúblico:** #72 (BCRA) · #73 (GobiernoLocal) · #39 (SectorPúblicoNoFinanciero → bajo Contraparte, ver nota) · #44 (OrganismoInternacional) · #43 (BancoMultilateralDesarrollo) · #77 (AgenciaOficialDeCrédito)
**→ Roles de alcance (eje B):** #65 (SujetoObligado) · #67 (SujetoAlcanzado) · #83 (PersonaAutorizada)
**→ Roles funcionales (eje B):** #24, #27 [DUP] (originante) · #26 (administrador) · #31 (agente de cobro) · #56 (cedente) · #69 (interviniente) · #71 (encargada de seguimiento) · #75 (operadora comercio exterior) · #82, #104 [DUP] (SEPAIMPO) · #103 (suscriptora) · #106 (intermediaria) · #111 (adherida) · #114, #118 [DUP] (nominada) · #115 (liquidadora) · #117 (encargada)
**→ Sujetos del exterior (rama a laudar en Sección 2):** #59 (casa matriz banco exterior) · #60 (sucursal local banco exterior) · #61 (filial/subsidiaria banco exterior) · #62 (banco exterior conveniado) · #93 (EF del exterior) · #108 (EF estatal del exterior) · #109 (EF y cambiaria del exterior) · #110 (compañía cambista del exterior) · #107 (sucursal de banco oficial en exterior)
**→ Estructuras y vehículos (rama a laudar en Sección 2):** #57, #91 (Fideicomiso/FideicomisoFinanciero) · #28 (SPE) · #40 (FondoComúnDeInversión)
**→ Perímetro de supervisión consolidada (rama a laudar):** #14, #55, #63 [DUP-ish] (sucursales/subsidiarias locales) · #48, #49 [DUP + label/categoria CRUZADOS] (subsidiarias) · #50 (controlante) · #15 (servicios complementarios) · #16, #19 [DUP] (aseguradoras) · #20 (bursátiles) · #17 (no sujeta a supervisión)
**→ Mal tipificados / fuera de árbol:** #125 (casa operativa: es un local, no un sujeto)

## Anexo 1.B — Clusters de duplicados detectados en run_3 (presa de la regla de unicidad)

| Cluster | Nodos | Observación |
|---|---|---|
| Grupo A | #47, #51 | mismo concepto, ids distintos |
| Grupo B | #11, #128 | ídem |
| Grupo C | #12, #129 | ídem |
| Grupo 2 | #10, #13 | ídem |
| MiPyME | #23, #123 | ídem |
| Fiduciario | #25, #53, #97 | triplicado; #53 y #97 casi idénticos hasta en el id |
| Emisoras de tarjetas | #66, #99, #100, #126 (+#124 financiera) | cuatro variantes no financieras/ambiguas + una financiera |
| VPU / RIGI | #78, #79, #80, #81, #84 | quintuplicado |
| Beneficiario Econ. Conocimiento | #85, #89 | duplicado |
| CCP | #32, #38 | duplicado |
| QCCP / CCP calificada | #33, #36 | mismo concepto en inglés/castellano |
| Emisor de títulos | #87, #98 | duplicado probable |
| SEPAIMPO | #82, #104 | duplicado |
| Entidad nominada | #114, #118 | duplicado |
| Aseguradoras | #16, #19 | duplicado |
| Subsidiarias | #48, #49 | duplicado con **label y categoria cruzados entre sí** — caso testigo de contenido_kg |
| Originante | #24, #27 | duplicado (genérico / entidad financiera originante) |

**Lectura para la Sección 3:** la regla de unicidad ("no puede haber dos nodos con label normalizado equivalente dentro de la misma clase") tendría al menos 17 clusters de detección inmediata sobre el grafo congelado — la validación determinística de Micaela tiene retorno medible desde el día uno.

## Anexo 1.C — Duplicados del operador de cambio en run_5 (evidencia original, actualizada)

El censo encontró **4** nodos (no 3, como se registró originalmente): `entidad_operadora_en_mercado_de_cambios__otra`, `operador_de_cambios__otra`, `operadores_de_cambio__agencia_cambio`, `operador_de_cambio__agencia_cambio` — cuatro ids, cuatro labels (variantes singular/plural y "operador"/"entidad operadora"), 3 con provenance en Exterior y 1 en Protección. El nodo 2 porta la description "Entidad financiera autorizada a operar en el mercado de cambios", que contradice Exterior 1.1 ("entidades financieras **o cambiarias**") con provenance a una sección de BOPREAL que no funda ese contenido — el caso testigo de que el conflato clase/entidad causa fallas medidas (falla adjudicada por el juez en run_5).

---

## Sección 2 — Semántica de los 12 predicados y regla de herencia

**Fuente empírica:** censo estructural #2 (14/07/2026) sobre run_3. Datos base: las 6.634 aristas caen en exactamente **16 combinaciones** (relación, dominio, rango); cada relación tiene **rango único**; 8 de 12 tienen además dominio único; 0 aristas fuera del vocabulario; 0 aristas colgantes. Los 12 totales coinciden uno a uno con la presentación congelada del esquema (validación cruzada independiente).

### 2.1 Firma real y definición operativa, relación por relación

| Relación | Firma real (censo) | Definición operativa propuesta | Ambigüedades / notas |
|---|---|---|---|
| `establecida_en` (2.453) | {Obligación 1.246, Restricción 810, Operación 250, Excepción 147} → TextoOrdenado | Anclaje de la unidad al documento que la instituye | Desde Operación (250) el sentido real es "definida_en", no "instituida": una operación no se *establece*, se *describe*. Se documenta como matiz, no se cambia el nombre (comparabilidad) |
| `aplica_a` (1.464) | {Obligación 895, Restricción 569} → EntidadFinanciera | **"Recae en"**: conecta la unidad normativa con el sujeto que debe cumplirla | **Excepción tiene 0 aplica_a** — su sujeto es implícito, heredado vía `exceptúa`. Brecha entre esquema declarado ("la unidad regulatoria... conecta con el sujeto") y grafo real. Ver 2.3 |
| `regula` (716) | {Obligación 683, Restricción 33} → Operación | Gobierna la *modalidad* de la operación (cómo se hace) — la deóntica residual | Las 33 desde Restricción comparten firma con `limita` y `prohíbe`: candidatas a reclasificación (medible). Ver 2.2 |
| `limita` (570) | Restricción → Operación | Impone cota **cuantitativa** a la operación | Correlato natural: property `umbral` en el origen (presente en 301/818 Restricciones) — shape candidata en modo WARN |
| `prohíbe` (131) | Restricción → Operación | **Veda total** de la operación (sin cota: cero) | Distinción crítica downstream (ya en el deck congelado) |
| `condiciona` (178) | Obligación → Operación | La operación solo es accesible si la obligación se satisface (precondición) | Frontera con `requiere` definida por la dirección: condiciona va de la norma a la operación |
| `requiere` (53) | Operación → Obligación | Ejecutar la operación **dispara** la obligación | Inversa conceptual de `condiciona`; el par queda documentado como tal |
| `exceptúa` (174) | Excepción → Restricción | Recorta el alcance de la restricción | Mecanismo de bloqueo de herencia (2.3) |
| `exceptúa_obligación` (76) | Excepción → Obligación | Ídem sobre obligaciones | Ídem |
| `ejecuta` (204) | EntidadFinanciera → Operación | El sujeto realiza la operación | 104/204 (51%) salen del nodo genérico "Sujetos obligados" — mismo defecto que aplica_a |
| `referencia` (558) | TextoOrdenado → Comunicación | El TO cita la comunicación de origen | Capa documental, sin cambios |
| `modificada_por` (57) | TextoOrdenado → Comunicación | La comunicación modifica al TO | Capa documental, sin cambios |

### 2.2 La pregunta de Micaela, respondida con el grafo

*"¿La obligación REGULA la operación o RECAE EN la operación?"* — El esquema ya separa las dos cosas, pero con nombres que no lo explicitan: **"recae en" es `aplica_a` y apunta al sujeto** (quién cumple); **`regula` apunta a la operación** (qué gobierna). La unidad normativa es un nodo con dos brazos: sujeto y operación. La confusión de Micaela es señal de que la documentación del esquema debe declarar esta lectura — y el censo muestra dónde la semántica sí está genuinamente borrosa: las tres relaciones que comparten la firma Restricción→Operación (`regula` 33, `limita` 570, `prohíbe` 131) y las dos que comparten Obligación→Operación (`regula` 683, `condiciona` 178). Para esas, las definiciones operativas de 2.1 son el criterio de asignación; las 33 `regula` desde Restricción son la población candidata a auditoría (¿debieron ser limita/prohíbe?) — auditable a mano, son 33.

### 2.3 Relaciones nuevas que exige la jerarquía + regla de herencia

Relaciones nuevas (solo en diseño B como metadato; en diseño A como aristas):

- `subclase_de` (Clase → Clase): taxonómica, transitiva, acíclica, árbol (cada clase un solo padre en v1).
- `instancia_de` (nodo → Clase): tipificación fina de los nodos existentes. El Anexo 1.A es su población inicial (~130 asignaciones).
- `miembro_de` (Clase → Rol): define las uniones del eje B (los 7 de SujetoObligado, EF∪EC de EntidadAutorizada, etc.).
- `parte_de` (Instancia → Instancia): SEFyC → BCRA. Uso mínimo, no transitiviza nada en v1.

**Regla de herencia explícita (v1):**

1. `aplica_a` hacia una **clase ontológica** C: la norma alcanza a C y a toda subclase de C (descenso por `subclase_de`), salvo bloqueo (regla 3).
2. `aplica_a` hacia un **rol** R: la norma alcanza a cada miembro de R (por `miembro_de`) y desde ahí desciende por la regla 1.
3. **Bloqueo por excepción:** si una Excepción `exceptúa` la unidad U, y el contenido de la excepción nombra una subclase S del destino de `aplica_a` de U, la herencia hacia S se corta. Caso testigo real del grafo: 'Excepción Cajas de Crédito Cooperativas' —exceptúa→ 'Exigencia básica bancos' (CapMin 1.2: la exigencia aplica a "Restantes entidades **(salvo Cajas de Crédito Cooperativas)**"). La regulación ya escribe herencia-con-excepción; la regla la formaliza.
4. La herencia **no asciende nunca** (lo que aplica a Banco no aplica a EntidadFinanciera) y **no cruza disyunciones**.

**Brecha documentada (no se resuelve acá):** Excepción sin `aplica_a` (0/258). Dos lecturas posibles — (a) es correcto: el sujeto de la excepción se hereda de la unidad exceptuada; (b) es un faltante del esquema. Se lleva a mentores como pregunta de diseño (Sección 6). La regla 3 asume (a).

### 2.4 Hallazgo: contaminación de vocabulario entre TOs

Las muestras del censo revelan que el nodo genérico "Sujetos obligados" recibe `aplica_a` desde normas de **Capitales Mínimos** (ej.: 'Calcular responsabilidad patrimonial computable' → 'Sujetos obligados', provenance CapMin Punto 1.3), cuando "sujeto obligado" es un término que solo **Protección 1.1.2** define — CapMin dice "entidades comprendidas". El genérico no solo pierde especificidad: **mezcla los vocabularios de alcance de los 5 TOs en un solo balde**. Consecuencia de diseño: los roles del eje B deben ser **por-TO** (SujetoObligado_Protección ≠ EntidadComprendida_RegInf), nunca un rol único global. Consecuencia para la taxonomía de defectos: caso medido de contenido_kg con raíz estructural.

---

## Sección 3 — Shapes caseras v0

Reglas de validación determinística sobre el kg.json, sin LLM (el pedido de Micaela: "no apoyarse siempre en LLMs para evaluar; te ayuda a ver dónde iterar"). Organizadas en tres capas según su estado esperado hoy — la estructura importa: la capa 1 protege lo que ya está bien, la capa 2 tiene presa medida, la capa 3 es la que el diseño habilita.

**Capa 1 — Invariantes que hoy PASAN (guardia de regresión para todo refinamiento futuro):**

| # | Regla | Estado medido en run_3 |
|---|---|---|
| S1 | Toda arista usa una de las 12 relaciones del esquema | PASS (6.634/6.634) |
| S2 | Integridad referencial: origen y destino de toda arista existen | PASS (0 colgantes) |
| S3 | Toda arista respeta la matriz de firmas (las 16 combinaciones de 2.1; ampliable solo por decisión versionada) | PASS por construcción; la shape lo vuelve *verificable* en vez de confiado |
| S4 | Todo nodo y toda arista tienen provenance `{source_doc, location}` completa | PASS (4.050 + 6.634, 100%) |
| S5 | Todo `location` contiene "punto" (normalizado) | PASS (100%). **Nota de diseño:** el patrón numérico N.N NO sirve como regla — cubre solo 452/699 en Comunicación; "punto" es el invariante real |
| S6 | Todo `source_doc` pertenece al conjunto de los 5 TOs | [VERIFICAR EN REPO: correr la shape; esperado PASS] |

**Capa 2 — Reglas que hoy FALLAN, con presa contada (medida por `shapes_validator.py`, reporte v0 del 14/07/2026):**

| # | Regla | Violaciones medidas en run_3 |
|---|---|---|
| S7 | Unicidad exacta: (type, label normalizado) único | **FAIL: 48 grupos, 103 nodos involucrados** (35 Operación, 10 Obligación, 2 Restricción, 1 Excepción) |
| S8 | Colisión de label entre types (WARN, no ERROR: ambigüedad léxica para buscar_nodos, no siempre duplicado) | **8 grupos** cross-type |
| S9 | Descripción canónica: exactamente una key de descripción por nodo | **FAIL: 53 nodos con ambas keys** (17 Obligación, 34 Restricción, 2 Excepción) + bifurcación descripcion/description transversal |
| S10 | Toda unidad regulatoria (R/O/E) tiene ≥1 `establecida_en` | **FAIL: 123 nodos sin anclaje documental** — 4 Obligaciones, 8 Restricciones, **111 Excepciones** (el 43% de las Excepciones del grafo) |
| S11 | Toda R/O tiene ≥1 `aplica_a` (WARN: sujeto explícito) | **WARN: 755 nodos sin sujeto explícito** — 458 Obligaciones (37%), 297 Restricciones (36%) — decidir con mentores si es defecto o diseño (L2) |
| S12 | Toda Excepción tiene ≥1 salida `exceptúa`/`exceptúa_obligación` | **FAIL: 27 excepciones huérfanas** (ni exceptúan nada ni tienen sujeto: invisibles para el consultor) |

**Capa 3 — Reglas que la jerarquía habilita (solo ejecutables con el diseño B en vigor):**

| # | Regla |
|---|---|
| S13 | Todo destino de `aplica_a` es una clase del árbol de Sujetos, un rol declarado, o una instancia mapeada (contra Anexo 1.A) |
| S14 | Ningún nodo instancia dos clases disjuntas (EF ⊥ EC ⊥ PSP; CCPCalificada ⊥ NoCalificada; SectorPúblico ⊥ Privado; Residente ⊥ NoResidente como atributo excluyente) |
| S15 | Todo rol tiene `miembro_de` no vacío, y sus miembros son clases del árbol |
| S16 | `subclase_de` es acíclica y cada clase tiene un solo padre |
| S17 | Unicidad intra-clase: dos nodos `instancia_de` la misma clase no comparten label normalizado (versión fina de S7) |
| S18 | Si una Restricción tiene arista `limita`, tiene property `umbral` (WARN — hoy 301 umbral vs 570 limita: la brecha se mide, no se presume error) |

**Límite honesto de la capa determinística:** S7 detecta duplicados *exactos* de label; los 17 clusters del Anexo 1.B (censo #1) son casi-duplicados con labels distintos ("Entidades del grupo A" / "Entidades Grupo A") que S7 **no** atrapa. La detección de casi-duplicados requiere similitud → es semi-automática con revisión humana, y queda explícitamente fuera de las shapes (va al pipeline de refinamiento). Este límite se declara en el memo: SHACL-style valida forma, no semántica.

---

## Sección 4 — Decisión A/B dimensionada [LAUDADA 14/07/2026: B ya · A-aditiva como propuesta a mentores · A+ trabajo futuro condicionado]

**Opción B — El árbol como metadato validable (sin tocar ningún grafo):**
- Qué es: el árbol + el mapeo del Anexo 1.A viven en archivos de diseño (`esquema_v2.md` + un `mapeo_clases.json`); el script de shapes valida run_3 contra ellos en solo lectura.
- Costo: ~1 script + 2 archivos de datos. Días, no semanas.
- Riesgo metodológico: **cero** — run_3, harness, juez y frozen eval intactos; comparabilidad total.
- Qué mide: cuánto del grafo congelado viola el diseño (las capas 1–2 completas + 3 contra el mapeo). Resultado citable en la tesis aunque nunca se implemente A.
- Qué NO arregla: la alcanzabilidad — buscar_nodos sigue sin poder navegar por clases; alcanzabilidad_kg sigue viva.

**Opción A — Clases navegables en el grafo (solo sobre `run_3_refinamiento`):**
- Versión mínima recomendada (**A-aditiva**): agregar ~35–45 nodos type Clase + aristas `instancia_de` desde los ~130 nodos del Anexo 1.A + `subclase_de` + `miembro_de` de los roles. **No se modifica ni elimina ninguna arista existente.** El agente gana navegación por clases (el arreglo estructural de alcanzabilidad_kg) con revisión humana de ~170 decisiones puntuales, todas ya pre-resueltas en el Anexo 1.A.
- Versión extendida (**A+, NO recomendada para v1**): re-target de las 991 `aplica_a` genéricas hacia clases específicas. Exige releer la provenance de cada arista (991 lecturas con juicio normativo), es la intervención de mayor riesgo del proyecto, y contamina la comparación si se hace junto con A-aditiva. Se documenta como segunda etapa condicionada a los resultados de A.
- Costo A-aditiva: actualización de la skill del agente y del verificador (Lucho ya lo anticipó), corrida de eval sobre la rama de refinamiento, revisión humana.
- Riesgo: medio — aditivo y reversible, pero el efecto en fidelidad puede ser nulo o negativo (y eso se reporta igual).

**Recomendación (a laudar por Agustina + mentores):** B ya — es casi gratis y produce números citables; A-aditiva como propuesta formal al pipeline de refinamiento, presentada en la reunión con el dimensionamiento de arriba; A+ como trabajo futuro condicionado. B y A no compiten: B es el instrumento de medición que A necesita para evaluarse.

### 4.1 Nota de extensibilidad — del subcorpus de 5 TOs al corpus BCRA completo

El esquema v2 no requiere rediseño para escalar: requiere **crecimiento aditivo bajo las mismas reglas**. La distinción entre niveles: la **arquitectura** (ejes A/B, regla de herencia, criterio clase-vs-atributo, shapes capas 1–2) es independiente del corpus — en particular, el eje B es por-TO por construcción: cada TO nuevo aporta su propio rol de alcance con sus miembros, sin tocar los existentes (el hallazgo de contaminación de vocabulario de 2.4 es la demostración de por qué un rol global no escala). El **contenido del árbol** sí crece con el corpus, de tres formas previstas: clases nuevas (mismo criterio pre-registrado de admisión: anclaje textual + población), clases marcadas que ganan anclaje (UIF está `[FUERA DE CORPUS]` hoy; el TO de Prevención del Lavado de Activos del corpus completo la nombra — la marca anticipa exactamente ese evento), y ramas hoy diferidas que se vuelven prioritarias (sujetos del exterior, vehículos, perímetro de consolidación). El costo recurrente real de escalar no es el diseño sino el **mapeo nodo→clase por cada grafo nuevo** (el Anexo 1.A es un artefacto del grafo, no del diseño) — trabajo del pipeline de refinamiento con revisión humana. Riesgo declarado: texto nuevo puede tensionar disyunciones (señal ya presente: el nodo #109 "Entidades financieras y cambiarias del exterior"); si ocurre, S14 lo detecta y la disyunción se revisa con changelog, nunca en silencio. Para la tesis: la defensa se hace sobre los 5 TOs congelados; esta nota fundamenta la sección de trabajo futuro con mecanismo, no con expresión de deseos.

---

## Sección 5 — Memo RDF/SHACL (1 página, para Luciano y Micaela)

**Asunto: qué tomamos de sus sugerencias y por qué esta vía no rompe el experimento**

**Lo que pidieron.** Luciano: una capa de clases — "en un KG las clases son casi más importantes que las entidades: te permiten navegar y agrupar"; distinguir clase de entidad; organismos regulatorios como tipo propio. Micaela: subclases explícitas al estilo RDF/ontologías, reglas por nivel de abstracción, y validación determinística tipo SHACL para no depender siempre de LLMs al evaluar.

**Por qué no migramos a RDF ahora.** El experimento central de la tesis compara la fidelidad del RAG con y sin la organización en KG, sobre un harness y una eval congelados. Migrar el sustrato a RDF/SPARQL en medio de la medición confundiría la variable central: cualquier cambio de fidelidad sería inatribuible (¿fue la jerarquía o el cambio de motor?). Además el agente actual usa 3 tools léxicas sobre JSON, no SPARQL.

**La tercera vía (qué hicimos en su lugar).**
(a) **Jerarquía de clases diseñada sobre el corpus** — árbol de Sujetos con dos ejes (clases ontológicas / roles por TO), disyunciones ancladas en el texto regulatorio (Exterior 5.4.2.2), y regla de herencia explícita con bloqueo por excepción — patrón que la propia regulación escribe ("Restantes entidades, salvo Cajas de Crédito Cooperativas", CapMin 1.2). Cada clase tiene anclaje textual y población real en el grafo (Secciones 1–2 del documento adjunto).
(b) **Shapes caseras** — 18 reglas determinísticas tipo SHACL sobre el JSON, en 3 capas: invariantes que hoy pasan (guardia de regresión), reglas que hoy fallan con violaciones contadas (48 grupos de duplicados exactos; ≥111 excepciones sin anclaje documental; bifurcación de keys de descripción), y reglas que la jerarquía habilita (disyunciones, unicidad intra-clase). Sin LLM en el loop de validación (Sección 3).
(c) **Export unidireccional a RDF** con rdflib + validación pySHACL, como anexo formal citable — el pipeline no lo toca.
(d) **Migración total a RDF: trabajo futuro documentado.**

**Qué se gana.** Navegación y agrupación por clases (pedido de Luciano); reglas por nivel — la exigencia básica se cuelga de Banco, no de EntidadFinanciera (pedido de Micaela); validación determinística con retorno inmediato: las violaciones ya están contadas sobre el grafo congelado; y una capa de evidencia nueva para el verificador (varias fallas del dev set instancian defectos que las shapes detectan).

**Qué se pierde (y se declara).** Razonamiento OWL nativo e inferencia automática de herencia (se implementa ad hoc y acotada); SPARQL; y las shapes solo validan *forma*: los casi-duplicados con labels distintos requieren similitud + revisión humana y quedan en el pipeline de refinamiento, no en la validación.

**Qué les pedimos en la reunión.** Los laudos de la Sección 6 — en particular, en qué punto del pipeline entra el esquema (pregunta L4, la decisión de diseño experimental más importante de esta etapa).

---

## Sección 6 — Preguntas abiertas para la reunión

### Para Luciano (diseño)

- **L1.** Excepción sin `aplica_a` (0/258 en el grafo): ¿es diseño correcto (el sujeto se hereda de la unidad exceptuada, regla de herencia 3) o es un faltante del esquema a cubrir en el refinamiento?
- **L2.** Unidades regulatorias sin sujeto explícito (medido: 458 Obligaciones y 297 Restricciones sin `aplica_a` — el 37% y 36% de cada type): ¿defecto de extracción o casos legítimos (normas auto-referidas al TO)? Define si S11 es ERROR o WARN. Dato conexo: 27 Excepciones no exceptúan nada ni tienen sujeto (S12) — huérfanas totales.
- **L3.** Tres ramas del árbol pendientes de laudo: sujetos del exterior (¿subclases o atributo `jurisdicción`?), vehículos (fideicomisos, SPE, FCI: ¿rama propia "Estructura"?), y perímetro de supervisión consolidada (aseguradoras, bursátiles, controlantes).
- **L4 — LA decisión de esta etapa: ¿dónde entra el esquema v2 al pipeline?** Opciones con costos:
  - **Camino 1 — refinamiento aditivo sobre `run_3_refinamiento`:** se agrega la capa de clases al grafo ya extraído (~40 nodos Clase + ~130 `instancia_de` pre-resueltos, cero aristas existentes modificadas). Mide el efecto de la jerarquía **aislado** (misma extracción, una variable). Las tools léxicas navegan los nodos Clase sin tocar el harness congelado; solo se actualiza la skill del agente. Piloto sobre un TO acotado antes del grafo completo (loops baratos).
  - **Camino 2 — re-extracción desde los PDFs con esquema v2:** el grafo "final" nace con clases, pero cambia todo a la vez (extracción no determinística) → el efecto de la jerarquía queda confundido. Caro en tiempo con defensa en noviembre.
  - **Camino 3 (recomendación) — secuencial:** camino 1 para la tesis; camino 2 como trabajo futuro o capítulo extra solo si el 1 da señal y hay calendario.
- **L5.** Las 991 `aplica_a` al nodo genérico "Sujetos obligados": ¿el re-target (A+) queda como trabajo futuro condicionado, como proponemos, o quieren un piloto acotado (p. ej. solo las de CapMin)?
- **L6.** N de repeticiones para la comparación baseline vs refinamiento (el caché colapsa repeticiones; la frozen eval usó N=3 sin caché) — [laudo compartido con Juan].

### Para Micaela (formales)

- **M1.** Regla de herencia v1 (descenso por subclase, membresía de roles, bloqueo por excepción, sin ascenso, sin cruce de disyunciones): ¿le ve huecos formales? ¿Conviene documentar la correspondencia con rdfs:subClassOf / owl:disjointWith en el anexo RDF?
- **M2.** Roles por-TO como clases-unión (owl:unionOf en el export): ¿es la formalización correcta para "sujeto obligado ≠ entidad comprendida", dado el hallazgo de contaminación de vocabulario entre TOs (Sección 2.4)?
- **M3.** Shapes capa 2: ¿el criterio ERROR/WARN por regla le parece bien asignado? En particular S11 (sujeto explícito) y S18 (limita sin umbral).
- **M4.** Estados vs. clases: modelamos `situación` (1..6) y `cartera` del deudor como atributos con dominio cerrado, no como subclases (mutabilidad, Clasificación 7.3). ¿Consistente con la práctica ontológica que ella recomienda?
- **M5.** Export RDF: ¿alcanza rdflib + pySHACL como anexo citable, o sugiere un perfil concreto (SHACL core vs SHACL-SPARQL) para las 18 reglas?

### Ya laudado que se informa (no se consulta)

Separación eje A/B; solo BancoComercial como subclase poblada de Banco; SEFyC nodo propio `parte_de` BCRA; emisoras ⊂ PNFC; CCP con subclases disjuntas; B se implementa ya (script de shapes de solo lectura); A-aditiva se propone, no se ejecuta sin su OK; A+ no se propone para v1.
