# Documentación de Casos de Prueba

## Información General del Proyecto

**Aplicación bajo prueba:** Parabank Banking Application  
**URL:** https://parabank.parasoft.com/parabank/index.htm  
**Framework:** Playwright + Pytest + Python  
**Patrón de diseño:** Page Object Model (POM)  
**Total de casos de prueba:** 27

---

## Módulo 1: Autenticación (Login)

### Información del Módulo

**Módulo:** Autenticación de usuarios  
**Prioridad:** Alta (funcionalidad crítica)  
**Total de casos:** 8  
**Estado:** 8/8 PASSED

---

### TC001: Login exitoso con credenciales válidas

**ID:** TC001  
**Prioridad:** Alta (Smoke Test)  
**Tipo:** Positivo  
**Objetivo:** Verificar que un usuario registrado puede iniciar sesión exitosamente

**Precondiciones:**
- Navegador iniciado en página de login
- Usuario "john" con password "demo" existe en el sistema

**Datos de prueba:**
- Username: `john`
- Password: `demo`

**Pasos:**
1. Navegar a la página de login
2. Ingresar "john" en el campo username
3. Ingresar "demo" en el campo password
4. Hacer clic en el botón "Log In"

**Resultado Esperado:**
- El sistema redirige a `/overview.htm`
- Se muestra el título "Accounts Overview"
- Se muestra mensaje de bienvenida con el nombre del usuario
- URL contiene "overview"

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_login.py::test_login_exitoso`

---

### TC002: Login con credenciales inválidas

**ID:** TC002  
**Prioridad:** Alta (Smoke Test)  
**Tipo:** Negativo  
**Objetivo:** Verificar que el sistema rechaza credenciales incorrectas

**Precondiciones:**
- Navegador iniciado

**Datos de prueba:**
- Username: `usuario_invalido_12345`
- Password: `password_incorrecta_xyz`

**Pasos:**
1. Navegar a la página de login
2. Ingresar usuario inválido en el campo username
3. Ingresar password inválida en el campo password
4. Hacer clic en el botón "Log In"

**Resultado Esperado:**
- El sistema NO permite el acceso
- Se muestra mensaje de error o usuario permanece en login
- La URL NO cambia a overview

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_login.py::test_login_con_credenciales_invalidas`

---

### TC003: Login con username vacío

**ID:** TC003  
**Prioridad:** Media (Regression Test)  
**Tipo:** Negativo  
**Objetivo:** Validar comportamiento con campo username sin llenar

**Precondiciones:**
- Navegador iniciado

**Datos de prueba:**
- Username: *(vacío)*
- Password: `demo`

**Pasos:**
1. Navegar a la página de login
2. Dejar el campo username vacío
3. Ingresar "demo" en el campo password
4. Hacer clic en el botón "Log In"

**Resultado Esperado:**
- El sistema NO permite el login
- Usuario permanece en la página de login

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_login.py::test_login_con_username_vacio`

---

### TC004: Login con password vacío

**ID:** TC004  
**Prioridad:** Media (Regression Test)  
**Tipo:** Negativo  
**Objetivo:** Validar comportamiento con campo password sin llenar

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_login.py::test_login_con_password_vacio`

---

### TC005: Login con ambos campos vacíos

**ID:** TC005  
**Prioridad:** Media (Regression Test)  
**Tipo:** Negativo  
**Objetivo:** Validar comportamiento cuando se hace submit sin datos

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_login.py::test_login_con_campos_vacios`

---

### TC006: Verificación de elementos UI visibles

**ID:** TC006  
**Prioridad:** Media (Regression Test)  
**Tipo:** Funcional  
**Objetivo:** Verificar que todos los elementos de la interfaz estén presentes

**Elementos verificados:**
- Campo de texto username
- Campo de texto password
- Botón "Log In"
- Link "Register"

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_login.py::test_verificar_elementos_visibles_en_pagina_login`

---

### TC007: Verificación de cambio de URL después del login

**ID:** TC007  
**Prioridad:** Baja (Slow Test)  
**Tipo:** Funcional  
**Objetivo:** Verificar que la navegación funciona correctamente

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_login.py::test_login_y_verificar_url`

---

### TC008: Logout después de login exitoso

**ID:** TC008  
**Prioridad:** Media (Regression Test)  
**Tipo:** Positivo  
**Objetivo:** Verificar funcionalidad de cerrar sesión

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_login.py::test_logout_despues_de_login`

---

## Módulo 2: Registro de Usuarios

### Información del Módulo

**Módulo:** Registro de nuevos usuarios  
**Prioridad:** Alta  
**Total de casos:** 8  
**Estado:** 6/8 PASSED, 2 SKIPPED

---

### TC009: Registro exitoso con datos válidos

**ID:** TC009  
**Prioridad:** Alta (Smoke Test)  
**Tipo:** Positivo  
**Objetivo:** Verificar que un usuario nuevo puede registrarse exitosamente

**Precondiciones:**
- Navegador iniciado
- Estar en página de registro

**Datos de prueba:**
- Todos los campos del formulario con datos válidos
- Username único generado con timestamp

**Pasos:**
1. Navegar a página de registro desde login
2. Llenar todos los campos obligatorios
3. Ingresar password y confirmar password iguales
4. Hacer clic en "Register"

**Resultado Esperado:**
- Sistema muestra mensaje de éxito
- Redirige a página de cuentas
- Usuario queda logueado automáticamente

**Resultado Actual:** PASS/SKIP (depende de estado del servidor)  
**Archivo de test:** `tests/test_registro.py::test_registro_usuario_exitoso`

---

### TC010: Registro con username existente

**ID:** TC010  
**Prioridad:** Alta (Regression Test)  
**Tipo:** Negativo  
**Objetivo:** Verificar que no se puede registrar con username ya existente

**Datos de prueba:**
- Username: `john` (ya existe)
- Demás campos con datos válidos

**Resultado Esperado:**
- Sistema muestra error indicando username existente
- No se completa el registro

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_registro.py::test_registro_con_username_existente`

---

### TC011: Registro con passwords que no coinciden

**ID:** TC011  
**Prioridad:** Alta (Regression Test)  
**Tipo:** Negativo  
**Objetivo:** Verificar validación de coincidencia de contraseñas

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_registro.py::test_registro_con_passwords_no_coinciden`

---

### TC012: Registro con campos obligatorios vacíos

**ID:** TC012  
**Prioridad:** Media (Regression Test)  
**Tipo:** Negativo  
**Objetivo:** Verificar validación de campos obligatorios

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_registro.py::test_registro_con_campos_obligatorios_vacios`

---

### TC013: Registro con datos parciales

**ID:** TC013  
**Prioridad:** Media (Regression Test)  
**Tipo:** Negativo  
**Objetivo:** Verificar que se requieren todos los campos

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_registro.py::test_registro_solo_con_username_y_password`

---

### TC014: Verificación de elementos del formulario

**ID:** TC014  
**Prioridad:** Media (Regression Test)  
**Tipo:** Funcional  
**Objetivo:** Verificar que todos los campos del formulario están presentes

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_registro.py::test_verificar_elementos_formulario_registro`

---

### TC015: Registro y login automático

**ID:** TC015  
**Prioridad:** Baja (Slow Test)  
**Tipo:** Positivo  
**Objetivo:** Verificar que después del registro se hace login automático

**Resultado Actual:** PASS/SKIP  
**Archivo de test:** `tests/test_registro.py::test_registro_y_login_automatico`

---

### TC016: Navegación a página de registro

**ID:** TC016  
**Prioridad:** Media (Regression Test)  
**Tipo:** Funcional  
**Objetivo:** Verificar navegación del link de registro

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_registro.py::test_navegacion_a_registro_desde_login`

---

## Módulo 3: Transferencias Bancarias

### Información del Módulo

**Módulo:** Transferencias entre cuentas  
**Prioridad:** Alta (funcionalidad crítica)  
**Total de casos:** 11  
**Estado:** 9/11 PASSED, 2 XFAIL (bugs identificados)

---

### TC017: Transferencia exitosa

**ID:** TC017  
**Prioridad:** Alta (Smoke Test)  
**Tipo:** Positivo  
**Objetivo:** Verificar que se puede realizar una transferencia exitosa

**Precondiciones:**
- Usuario logueado
- Al menos 2 cuentas disponibles

**Datos de prueba:**
- Monto: $100

**Pasos:**
1. Navegar a "Transfer Funds"
2. Ingresar monto válido
3. Seleccionar cuenta origen y destino
4. Hacer clic en "Transfer"

**Resultado Esperado:**
- Sistema muestra mensaje "Transfer Complete!"
- Se muestran detalles de la transferencia
- Monto se refleja correctamente

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_transferencias.py::test_transferencia_exitosa`

---

### TC018: Transferencia con monto cero

**ID:** TC018  
**Prioridad:** Alta (Regression Test)  
**Tipo:** Negativo  
**Objetivo:** Verificar que no se puede transferir monto $0

**Datos de prueba:**
- Monto: $0

**Resultado Esperado:**
- Sistema rechaza la transferencia
- Muestra mensaje de error

**Resultado Actual:** XFAIL (BUG ENCONTRADO)  
**Defecto:** Sistema permite transferencias con monto $0  
**Severidad:** Alta  
**Archivo de test:** `tests/test_transferencias.py::test_transferencia_con_monto_cero`  
**Documentación:** [BUG-001](BUGS_FOUND.md#bug-001)

---

### TC019: Transferencia con monto negativo

**ID:** TC019  
**Prioridad:** Crítica (Regression Test)  
**Tipo:** Negativo  
**Objetivo:** Verificar que no se puede transferir monto negativo

**Datos de prueba:**
- Monto: -$50

**Resultado Esperado:**
- Sistema rechaza la transferencia
- Muestra mensaje de error de validación

**Resultado Actual:** XFAIL (BUG ENCONTRADO)  
**Defecto:** Sistema permite transferencias con monto negativo  
**Severidad:** Crítica  
**Archivo de test:** `tests/test_transferencias.py::test_transferencia_con_monto_negativo`  
**Documentación:** [BUG-002](BUGS_FOUND.md#bug-002)

---

### TC020: Transferencia sin monto

**ID:** TC020  
**Prioridad:** Media (Regression Test)  
**Tipo:** Negativo  
**Objetivo:** Verificar validación de campo monto vacío

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_transferencias.py::test_transferencia_sin_monto`

---

### TC021: Transferencia con texto en campo monto

**ID:** TC021  
**Prioridad:** Media (Regression Test)  
**Tipo:** Negativo  
**Objetivo:** Verificar que no se acepta texto en campo numérico

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_transferencias.py::test_transferencia_con_texto_en_monto`

---

### TC022: Verificación de elementos del formulario

**ID:** TC022  
**Prioridad:** Media (Regression Test)  
**Tipo:** Funcional  
**Objetivo:** Verificar que todos los elementos están presentes

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_transferencias.py::test_verificar_elementos_formulario_transferencia`

---

### TC023: Verificar detalles de transferencia

**ID:** TC023  
**Prioridad:** Alta (Smoke Test)  
**Tipo:** Positivo  
**Objetivo:** Verificar que se muestran los detalles de la transferencia

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_transferencias.py::test_transferencia_y_verificar_detalles`

---

### TC024: Múltiples transferencias consecutivas

**ID:** TC024  
**Prioridad:** Baja (Slow Test)  
**Tipo:** Positivo  
**Objetivo:** Verificar que se pueden realizar múltiples transferencias

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_transferencias.py::test_multiples_transferencias_consecutivas`

---

### TC025: Obtener cuentas disponibles

**ID:** TC025  
**Prioridad:** Media (Regression Test)  
**Tipo:** Funcional  
**Objetivo:** Verificar que se pueden obtener las cuentas disponibles

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_transferencias.py::test_obtener_cuentas_disponibles`

---

### TC026: Navegación a transferencias desde menú

**ID:** TC026  
**Prioridad:** Media (Regression Test)  
**Tipo:** Funcional  
**Objetivo:** Verificar navegación desde menú a transferencias

**Resultado Actual:** PASS  
**Archivo de test:** `tests/test_transferencias.py::test_navegacion_a_transferencias_desde_menu`

---

## Resumen General de Resultados

### Por Módulo

| Módulo | Total | Passed | Failed | Skipped | XFail |
|--------|-------|--------|--------|---------|-------|
| Login | 8 | 8 | 0 | 0 | 0 |
| Registro | 8 | 6 | 0 | 2 | 0 |
| Transferencias | 11 | 9 | 0 | 0 | 2 |
| **TOTAL** | **27** | **23** | **0** | **2** | **2** |

### Por Categoría

| Categoría | Total | Passed | Failed | Skipped | XFail |
|-----------|-------|--------|--------|---------|-------|
| Smoke Tests | 5 | 4 | 0 | 1 | 0 |
| Regression Tests | 19 | 16 | 0 | 1 | 2 |
| Slow Tests | 3 | 3 | 0 | 0 | 0 |

### Por Tipo

| Tipo | Total | Porcentaje |
|------|-------|------------|
| Positivos | 8 | 29.6% |
| Negativos | 17 | 63.0% |
| Funcionales | 2 | 7.4% |

---

## Defectos Encontrados

Durante la ejecución de la suite de tests se identificaron **2 defectos críticos**:

### BUG-001: Sistema permite transferencias con monto $0
- **Severidad:** Alta
- **Módulo:** Transferencias
- **Test Case:** TC018
- **Documentación:** [Ver detalles completos](BUGS_FOUND.md#bug-001)

### BUG-002: Sistema permite transferencias con monto negativo
- **Severidad:** Crítica
- **Módulo:** Transferencias
- **Test Case:** TC019
- **Documentación:** [Ver detalles completos](BUGS_FOUND.md#bug-002)

---

## Métricas de Cobertura

**Cobertura por módulo:** 100% (3/3 módulos principales)  
**Tasa de éxito:** 85.2% (23/27 tests)  
**Defectos encontrados:** 2  
**Tiempo total de ejecución:** ~5.5 minutos  
**Última ejecución:** 2024-11-06

---

## Notas Técnicas

### Selectores Utilizados

#### Login
```python
USERNAME_INPUT = "input[name='username']"
PASSWORD_INPUT = "input[name='password']"
LOGIN_BUTTON = "input[type='submit'][value='Log In']"
```

#### Registro
```python
FIRST_NAME_INPUT = "input[id='customer.firstName']"
USERNAME_INPUT = "input[id='customer.username']"
REGISTER_BUTTON = "input[type='submit'][value='Register']"
```

#### Transferencias
```python
AMOUNT_INPUT = "input[id='amount']"
FROM_ACCOUNT_SELECT = "select[id='fromAccountId']"
TRANSFER_BUTTON = "input[type='submit'][value='Transfer']"
```

### Configuración de Timeouts

- Timeout por defecto: 5000ms
- Timeout para elementos: 10000ms
- Wait explícito en tests: 2000-5000ms
- Slow_mo navegador: 500ms

### Datos de Prueba

Los datos de prueba están centralizados en `utils/test_data.py`:
- Usuario válido: john/demo
- Usuarios de registro generados con timestamp
- Validaciones centralizadas

---

## Mantenimiento

Este documento debe actualizarse cuando:
- Se agregan nuevos casos de prueba
- Se modifican casos existentes
- Se encuentran nuevos defectos
- Cambian los resultados de ejecución

--

*Documento generado como parte del proyecto de automatización de testing*