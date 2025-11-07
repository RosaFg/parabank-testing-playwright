# Defectos Encontrados en Parabank

Este documento lista los bugs/defectos encontrados durante la ejecución de la suite de tests automatizados.

---

## Resumen

| ID | Módulo | Severidad | Estado | Fecha |
|----|--------|-----------|--------|-------|
| BUG-001 | Transferencias | 🔴 Alta | Abierto | 2024-11-06 |
| BUG-002 | Transferencias | 🔴 Alta | Abierto | 2024-11-06 |

---

## BUG-001: Sistema permite transferencias con monto $0

### Información General
- **ID:** BUG-001
- **Módulo:** Transferencias Bancarias
- **Severidad:** 🔴 Alta
- **Prioridad:** Alta
- **Estado:** Abierto
- **Encontrado por:** Test automatizado `test_transferencia_con_monto_cero`
- **Fecha:** 06/11/2024
- **Ambiente:** https://parabank.parasoft.com

### Descripción
El sistema permite realizar transferencias bancarias con monto $0 (cero dólares), cuando debería mostrar un mensaje de error y rechazar la operación.

### Pasos para Reproducir
1. Hacer login con usuario válido
2. Navegar a "Transfer Funds"
3. Ingresar monto: `0`
4. Seleccionar cuenta origen y destino
5. Hacer clic en "Transfer"

### Resultado Actual
- ❌ La transferencia se procesa exitosamente
- ❌ Se muestra mensaje "Transfer Complete!"
- ❌ El sistema acepta el monto $0

### Resultado Esperado
- ✅ El sistema debe mostrar mensaje de error
- ✅ El sistema debe indicar "El monto debe ser mayor a $0"
- ✅ La transferencia NO debe procesarse

### Evidencia
- Screenshot: `reports/screenshots/transferencia_monto_cero_*.png`
- Test: `tests/test_transferencias.py::test_transferencia_con_monto_cero`

### Impacto
- **Funcional:** Alto - Permite operaciones inválidas
- **Negocio:** Medio - Puede generar registros innecesarios
- **Usuario:** Bajo - Usuario puede notar comportamiento extraño

### Recomendación
Agregar validación client-side y server-side para rechazar montos menores o iguales a $0.

---

## BUG-002: Sistema permite transferencias con monto negativo

### Información General
- **ID:** BUG-002
- **Módulo:** Transferencias Bancarias
- **Severidad:** 🔴 Alta
- **Prioridad:** Crítica
- **Estado:** Abierto
- **Encontrado por:** Test automatizado `test_transferencia_con_monto_negativo`
- **Fecha:** 06/11/2024
- **Ambiente:** https://parabank.parasoft.com

### Descripción
El sistema permite realizar transferencias bancarias con montos negativos (ej: -$50), lo cual representa un riesgo de seguridad importante ya que podría permitir manipulación de balances.

### Pasos para Reproducir
1. Hacer login con usuario válido
2. Navegar a "Transfer Funds"
3. Ingresar monto: `-50`
4. Seleccionar cuenta origen y destino
5. Hacer clic en "Transfer"

### Resultado Actual
- ❌ La transferencia se procesa exitosamente
- ❌ Se muestra mensaje "Transfer Complete!"
- ❌ El sistema acepta montos negativos
- ❌ Posible manipulación de balances

### Resultado Esperado
- ✅ El sistema debe rechazar montos negativos
- ✅ Mostrar mensaje: "El monto debe ser un número positivo"
- ✅ La transferencia NO debe procesarse

### Evidencia
- Screenshot: `reports/screenshots/transferencia_monto_negativo_*.png`
- Test: `tests/test_transferencias.py::test_transferencia_con_monto_negativo`

### Impacto
- **Funcional:** Crítico - Permite operaciones inválidas
- **Seguridad:** Alto - Posible vulnerabilidad de manipulación de datos
- **Negocio:** Alto - Riesgo de pérdidas financieras
- **Usuario:** Alto - Puede afectar integridad de cuentas

### Recomendación
**URGENTE:** Implementar validación estricta de montos:
1. Validación client-side (JavaScript) para feedback inmediato
2. Validación server-side (obligatoria) para seguridad
3. Usar tipo de dato apropiado (unsigned/positive)
4. Agregar tests de seguridad adicionales

---

## Estadísticas

### Por Severidad
- 🔴 Alta/Crítica: 2
- 🟡 Media: 0
- 🟢 Baja: 0

### Por Módulo
- Transferencias: 2
- Login: 0
- Registro: 0

### Por Estado
- Abierto: 2
- En Progreso: 0
- Cerrado: 0

---

## Notas para Desarrolladores

### Validaciones Recomendadas

```javascript
// Client-side validation (ejemplo)
function validateAmount(amount) {
    if (amount <= 0) {
        return "El monto debe ser mayor a $0";
    }
    if (amount > 10000) {
        return "El monto excede el límite de $10,000";
    }
    return null; // válido
}
```

```java
// Server-side validation (ejemplo)
public void validateTransferAmount(BigDecimal amount) {
    if (amount.compareTo(BigDecimal.ZERO) <= 0) {
        throw new InvalidAmountException("Amount must be positive");
    }
}
```

---

## Proceso de Reporte

Los bugs fueron encontrados mediante:
1. Ejecución automática de test suite
2. Validación de casos negativos
3. Captura automática de screenshots
4. Documentación en este archivo

**Test Execution Date:** 06/11/2024
**Environment:** Parabank Demo Application
**Tester:** Automated Test Suite (Playwright + Pytest)

---
*Documento generado como parte del proceso de QA automatizado*