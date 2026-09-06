# Verificación pareada U-B5.4 — comparación mecánica contra predicciones selladas

Predicciones: `predicciones_pareada_selladas_b54.md` (commit f19e978). Después:
tool_input crudo bajo el prefijo v3 (`29af2e29880b…`); antes: capa
`validacion.relaciones` persistida (columna cruda informativa). Reproduce:
`python3 data/experiment/b54_catalogo_v3/code/comparar_pareada_b54.py`.

**Totales: 25 PASA / 3 FICHA / 6 NO_CUMPLE** (34 unidades). Por brazo: A: 9/0/1; B: 8/0/0; C: 3/3/1; D: 2/0/3; E: 3/0/0; F: 0/0/1

**P-B-global (no-migración cross-TO de roles): SIN violaciones ✓**

| unidad | brazo | veredicto | detalle | antes (validación) | después (crudo v3) |
|---|---|---|---|---|---|
| `cap::1.1` | A | **PASA** | rol propio Sujeto_rol_alcance_capmin presente | ids: rol_alcance_capmin | ids: rol_alcance_capmin |
| `cap::1.2` | A | **PASA** | rol propio Sujeto_rol_alcance_capmin presente | ids: banco, compania_financiera, rol_alcance_capmin | ids: banco, compania_financiera, rol_alcance_capmin |
| `cla::1.1` | A | **PASA** | rol propio Sujeto_rol_obligado_a_clasificar_clasificacion presente | ids: rol_obligado_a_clasificar_clasificacion | ids: rol_obligado_a_clasificar_clasificacion |
| `cla::1.2.1` | A | **PASA** | rol propio Sujeto_rol_obligado_a_clasificar_clasificacion presente | ids: rol_obligado_a_clasificar_clasificacion | ids: rol_obligado_a_clasificar_clasificacion |
| `pro::1.1.1` | A | **NO_CUMPLE** | rol propio Sujeto_rol_sujeto_obligado_proteccion AUSENTE | ids: rol_sujeto_obligado_proteccion | ids:  |
| `pro::1.1.2.7` | A | **PASA** | rol propio Sujeto_rol_sujeto_obligado_proteccion presente | ids: rol_sujeto_obligado_proteccion | ids: psi_billetera_digital, rol_sujeto_obligado_proteccion |
| `ric::1.1` | A | **PASA** | rol propio Sujeto_rol_entidad_comprendida_reginf presente | ids: rol_entidad_comprendida_reginf | ids: rol_entidad_comprendida_reginf |
| `ric::1.2` | A | **PASA** | rol propio Sujeto_rol_entidad_comprendida_reginf presente | ids: rol_entidad_comprendida_reginf | ids: rol_entidad_comprendida_reginf |
| `ext::1.2` | A | **PASA** | rol propio Sujeto_rol_entidad_autorizada_exterior presente | ids: rol_entidad_autorizada_exterior | ids: rol_entidad_autorizada_exterior |
| `ext::1.3` | A | **PASA** | rol propio Sujeto_rol_entidad_autorizada_exterior presente | ids: rol_entidad_autorizada_exterior | ids: rol_entidad_autorizada_exterior |
| `ayccef::2.9.2::intro` | B | **PASA** | Sujeto_entidad_financiera presente; rol ajeno previo ['Sujeto_rol_alcance_capmin'] ya no aparece | ids: rol_alcance_capmin | ids: entidad_financiera |
| `actgar::2.3.6.3` | B | **PASA** | Sujeto_entidad_financiera presente; rol ajeno previo ['Sujeto_rol_entidad_autorizada_exterior'] ya no aparece | ids: rol_entidad_autorizada_exterior | ids: entidad_financiera |
| `actgar::2.7.2` | B | **PASA** | Sujeto_entidad_financiera presente; rol ajeno previo ['Sujeto_rol_entidad_autorizada_exterior'] ya no aparece | ids: rol_entidad_autorizada_exterior | ids: entidad_financiera |
| `expaef::5.7.1.2` | B | **PASA** | Sujeto_entidad_financiera presente; rol ajeno previo ['Sujeto_rol_entidad_autorizada_exterior'] ya no aparece | ids: rol_entidad_autorizada_exterior | ids: entidad_financiera |
| `expaef::5.7.1.3` | B | **PASA** | Sujeto_entidad_financiera presente; rol ajeno previo ['Sujeto_rol_entidad_autorizada_exterior'] ya no aparece | ids: rol_entidad_autorizada_exterior | ids: entidad_financiera |
| `lavdin::1.1.1` | B | **PASA** | Sujeto_rol_alcance_lavdin presente; rol ajeno previo ['Sujeto_rol_sujeto_obligado_proteccion'] ya no aparece | ids: rol_sujeto_obligado_proteccion | ids: rol_alcance_lavdin |
| `lavdin::1.3.3` | B | **PASA** | Sujeto_rol_alcance_lavdin presente; rol ajeno previo ['Sujeto_rol_sujeto_obligado_proteccion'] ya no aparece | ids: bcra, rol_sujeto_obligado_proteccion | ids: bcra, rol_alcance_lavdin |
| `cryl::4.1` | B | **PASA** | Sujeto_rol_alcance_cryl presente; rol ajeno previo ['Sujeto_rol_entidad_comprendida_reginf'] ya no aparece | ids: rol_entidad_comprendida_reginf | ids: rol_alcance_cryl |
| `cap::6.2.1.1` | C | **NO_CUMPLE** | BIS no quedó en propuesto | ids: aseguradora, banco_multilateral_de_desarrollo, bcra, entidad_cambiaria, entidad_financiera, fiduciario_de_fideicomiso_financiero, sector_privado_no_financiero, sector_publico_ | ids: aseguradora, banco_central_del_exterior, banco_multilateral_de_desarrollo, bcra, entidad_cambiaria, entidad_financiera, fiduciario_de_fideicomiso_financiero, fmi, rol_alcance_ |
| `cryl::3.1` | C | **PASA** | CEC→clase; mercados/CDV→propuestos | ids: entidad_financiera, fondo_comun_de_inversion; prop: Centrales Depositarias de Valores; Cámaras Electrónicas de Compensación; Mercados de Valores | ids: bcra, camara_electronica_de_compensacion, entidad_financiera; prop: Centrales Depositarias de Valores Nacion; Fondos Comunes de Inversión cuyos cuotap; Mercados de Valores del |
| `traval::1.1::intro` | C | **FICHA** | predicción sellada: FICHA en ambos sentidos — ids=[] props=[] | ids: persona_juridica; prop: Prestadoras de Servicios de Transporte d; Transportadoras de Valores Propias de en | ids:  |
| `traval::2.3` | C | **FICHA** | predicción sellada: FICHA en ambos sentidos — ids=['Sujeto_rol_alcance_traval'] props=[] | ids: ; prop: Prestadoras de servicios de transporte d; Transportadoras de valores | ids: rol_alcance_traval |
| `traval::S2::cierre` | C | **FICHA** | predicción sellada: FICHA en ambos sentidos — ids=['Sujeto_rol_alcance_traval'] props=['PSTV'] | ids: sujeto_regulado; prop: PSTV (prestadoras de servicios de transp; TV (transportadoras de valores) | ids: rol_alcance_traval; prop: PSTV |
| `expaef::9.3` | C | **PASA** | agencia complementaria sigue en propuesto; no atraída | ids: ; prop: agencia complementaria de servicios fina; trabajadores mensualizados que cumplan j | ids: entidad_financiera; prop: agencia complementaria de servicios fina |
| `expaef::9.5.3` | C | **PASA** | agencia complementaria sigue en propuesto; no atraída | ids: entidad_financiera; prop: agencia complementaria de servicios fina | ids: entidad_financiera; prop: agencia complementaria de servicios fina |
| `ayccef::2.1` | D | **NO_CUMPLE** | ejecuta=[]; ids=['Sujeto_entidad_financiera', 'Sujeto_sector_publico_no_financiero'] | ids: bcra, entidad_financiera | ids: entidad_financiera, sector_publico_no_financiero |
| `ayccef::3.1` | D | **PASA** | ejecuta=['Sujeto_bcra']; ids=['Sujeto_bcra', 'Sujeto_entidad_financiera'] | ids: bcra, entidad_financiera | ids: bcra, entidad_financiera |
| `ayccef::4.1` | D | **NO_CUMPLE** | ejecuta=[]; ids=['Sujeto_entidad_financiera'] | ids: bcra, entidad_financiera | ids: entidad_financiera |
| `cryl::1.3` | D | **NO_CUMPLE** | ejecuta=['Sujeto_bcra', 'Sujeto_rol_alcance_cryl']; ids=['Sujeto_bcra', 'Sujeto_rol_alcance_cryl'] | ids: bcra | ids: bcra, rol_alcance_cryl |
| `cryl::3.2::intro` | D | **PASA** | ejecuta=['Sujeto_bcra']; ids=['Sujeto_bcra', 'Sujeto_rol_alcance_cryl'] | ids: bcra | ids: bcra, rol_alcance_cryl |
| `actgar::1.2` | E | **PASA** | EF presente; ids=['Sujeto_entidad_financiera'] | ids: entidad_financiera | ids: entidad_financiera |
| `actgar::2.2.2` | E | **PASA** | EF presente; ids=['Sujeto_entidad_financiera'] | ids: entidad_financiera | ids: entidad_financiera |
| `actgar::2.4.1` | E | **PASA** | EF presente; ids=['Sujeto_entidad_financiera'] | ids: entidad_financiera | ids: entidad_financiera |
| `cap::3.1.14::intro` | F | **NO_CUMPLE** | MIGRÓ a Sujeto_entidad_originante (violación de la guarda) | ids: rol_alcance_capmin, sefyc; prop: inversor; inversores y tenedores de posiciones de ; originante; originante/fiduciario | ids: entidad_originante, fiduciario_de_fideicomiso_financiero, rol_alcance_capmin, sefyc; prop: inversor |
