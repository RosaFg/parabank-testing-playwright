# Parabank - Automatización de Testing Web

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-1.40.0-45ba4b?style=flat&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-7.4.3-0A9EDC?style=flat&logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)
![Tests](https://img.shields.io/badge/Tests-27%20Total-success?style=flat)
![Coverage](https://img.shields.io/badge/Coverage-3%20Modules-blue?style=flat)

> Suite completa de testing automatizado para aplicación web bancaria usando Playwright, Python y el patrón Page Object Model.

---



## Sobre este proyecto

Este proyecto demuestra habilidades en **QA Automation** implementando una suite de tests end-to-end para [Parabank](https://parabank.parasoft.com/), una aplicación bancaria de demostración.

### Objetivos del proyecto

- Demostrar dominio de **automatización web moderna** con Playwright
- Implementar **buenas prácticas** de testing (Page Object Model)
- Crear suite de tests **mantenible y escalable**
- Generar **reportes detallados** con evidencia visual
- Documentar código de forma **profesional**
- **Identificar y documentar defectos** en la aplicación

---

## Características principales

| Característica | Descripción |
|----------------|-------------|
| **Playwright** | Framework moderno multi-navegador (Chromium, Firefox, WebKit) |
| **Page Object Model** | Patrón de diseño para código mantenible y reutilizable |
| **Pytest Framework** | 27 test cases cubriendo escenarios positivos y negativos |
| **Screenshots automáticos** | Capturas en cada fallo para debugging rápido |
| **Video recording** | Grabación de ejecución para análisis post-mortem |
| **Reportes HTML** | Reportes detallados con pytest-html |
| **Test tagging** | Organización por criticidad (smoke, regression, slow) |
| **Fixtures reutilizables** | Setup/teardown automático de navegadores |
| **Bug tracking** | Documentación profesional de defectos encontrados |

---

## Cobertura de Testing

### Módulo: Login (8 test cases)

| # | Test Case | Tipo | Estado |
|---|-----------|------|--------|
| 1 | Login exitoso con credenciales válidas | Smoke | PASS |
| 2 | Login con credenciales inválidas | Smoke | PASS |
| 3 | Login con username vacío | Regression | PASS |
| 4 | Login con password vacío | Regression | PASS |
| 5 | Login con ambos campos vacíos | Regression | PASS |
| 6 | Verificación de elementos UI | Regression | PASS |
| 7 | Verificación de cambio de URL | Slow | PASS |
| 8 | Logout después de login | Regression | PASS |

**Resultado: 8/8 tests pasando (100%) | Tiempo: ~60s**

---

### Módulo: Registro (8 test cases)

| # | Test Case | Tipo | Estado |
|---|-----------|------|--------|
| 1 | Registro exitoso con datos válidos | Smoke | PASS/SKIP |
| 2 | Registro con username existente | Regression | PASS |
| 3 | Passwords no coinciden | Regression | PASS |
| 4 | Campos obligatorios vacíos | Regression | PASS |
| 5 | Registro con datos parciales | Regression | PASS |
| 6 | Verificación elementos formulario | Regression | PASS |
| 7 | Registro y login automático | Slow | PASS/SKIP |
| 8 | Navegación a registro | Regression | PASS |

**Resultado: 6/8 tests pasando, 2 skipped (ambiente compartido)**

---

### Módulo: Transferencias (11 test cases)

| # | Test Case | Tipo | Estado |
|---|-----------|------|--------|
| 1 | Transferencia exitosa | Smoke | PASS |
| 2 | Transferencia monto cero | Regression | XFAIL (Bug) |
| 3 | Transferencia monto negativo | Regression | XFAIL (Bug) |
| 4 | Transferencia sin monto | Regression | PASS |
| 5 | Texto en campo monto | Regression | PASS |
| 6 | Verificación elementos formulario | Regression | PASS |
| 7 | Verificar detalles transferencia | Smoke | PASS |
| 8 | Múltiples transferencias | Slow | PASS |
| 9 | Obtener cuentas disponibles | Regression | PASS |
| 10 | Navegación a transferencias | Regression | PASS |

**Resultado: 9/11 tests pasando, 2 xfail (bugs identificados)**

---

### Resumen Total

**Total: 27 test cases implementados**

- **23 PASSED**: Tests ejecutados exitosamente
- **2 XFAIL**: Defectos identificados y documentados
- **2 SKIPPED**: Ambiente de pruebas compartido

---

## Defectos Encontrados

Durante la ejecución de la suite de tests, se identificaron **2 defectos críticos** en la aplicación:

| ID | Descripción | Severidad | Módulo | Evidencia |
|----|-------------|-----------|--------|-----------|
| BUG-001 | Sistema permite transferencias con monto $0 | Alta | Transferencias | [Ver detalles](docs/BUGS_FOUND.md#bug-001) |
| BUG-002 | Sistema permite transferencias con monto negativo | Crítica | Transferencias | [Ver detalles](docs/BUGS_FOUND.md#bug-002) |

**[Ver reporte completo de bugs encontrados](docs/BUGS_FOUND.md)**

> **Nota:** Estos defectos demuestran la efectividad de la suite de tests automatizados para identificar vulnerabilidades de validación de datos que podrían representar riesgos de seguridad.

---

## Stack Tecnológico

- **Lenguaje:** Python 3.9+
- **Framework de Automatización:** Playwright 1.40.0
- **Framework de Testing:** Pytest 7.4.3
- **Reportes:** pytest-html 4.1.1
- **Patrón de Diseño:** Page Object Model (POM)
- **Control de Versiones:** Git

---

## Estructura del Proyecto

```
parabank-testing/
│
├── tests/                      # Test suites organizadas por módulo
│   ├── test_login.py           # 8 test cases de autenticación
│   ├── test_registro.py        # 8 test cases de registro
│   └── test_transferencias.py  # 11 test cases de transferencias
│
├── pages/                      # Page Object Model
│   ├── base_page.py            # Clase base con métodos comunes
│   ├── login_page.py           # Page Object de login
│   ├── registro_page.py        # Page Object de registro
│   └── transferencia_page.py   # Page Object de transferencias
│
├── utils/                      # Utilidades y helpers
│   └── test_data.py            # Datos de prueba centralizados
│
├── docs/                       # Documentación del proyecto
│   ├── BUGS_FOUND.md           # Defectos encontrados documentados
│   └── test_cases.md           # Documentación detallada de casos
│
├── reports/                    # Reportes generados automáticamente
│   ├── screenshots/            # Capturas de pantalla
│   ├── videos/                 # Videos de ejecución
│   └── html/                   # Reportes HTML
│
├── conftest.py                 # Configuración global de fixtures
├── pytest.ini                  # Configuración de pytest
├── requirements.txt            # Dependencias del proyecto
├── LICENSE                     # Licencia MIT
├── .gitignore                  # Archivos ignorados por Git
└── README.md                   # Este archivo
```

---

## Instalación y Configuración

### Prerrequisitos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Git

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/RosaFG/parabank-testing-playwright.git
cd parabank-testing-playwright
```

### Paso 2: Crear entorno virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Instalar navegadores de Playwright

```bash
playwright install
```

---

## Ejecución de Tests

### Comandos básicos

```bash
# Ejecutar todos los tests
pytest

# Ejecutar con output detallado
pytest -v

# Ejecutar mostrando prints
pytest -v -s

# Ejecutar tests específicos por módulo
pytest tests/test_login.py
pytest tests/test_registro.py
pytest tests/test_transferencias.py

# Ejecutar un solo test
pytest tests/test_login.py::test_login_exitoso
```

### Ejecución por tags

```bash
# Solo tests críticos (smoke)
pytest -m smoke -v

# Solo tests de regresión
pytest -m regression -v

# Excluir tests lentos
pytest -m "not slow" -v
```

### Generar reportes

```bash
# Generar reporte HTML
pytest --html=reports/html/report.html --self-contained-html

# Ejecutar tests y generar reporte
pytest -v --html=reports/html/report.html --self-contained-html
```

### Modo headless (sin ventana del navegador)

Edita `conftest.py` línea 18:

```python
browser = p.chromium.launch(headless=True)
```

---

## Habilidades Demostradas

### Testing

- Diseño de test cases (positivos y negativos)
- Automatización E2E (End-to-End)
- Estrategias de verificación (assertions)
- Manejo de waits y sincronización
- Organización de test suites
- Identificación y documentación de defectos

### Programación

- Python (POO, fixtures, decoradores)
- Patrón Page Object Model
- Manejo de selectores CSS
- Gestión de excepciones
- Documentación de código

### Herramientas

- Playwright (API moderna)
- Pytest (fixtures, marks, plugins)
- Git (control de versiones)
- Debugging con screenshots/videos

---

## Conceptos Aplicados

### Page Object Model (POM)

```python
# Separación de lógica de tests y estructura de página
class LoginPage(BasePage):
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    
    def login(self, username, password):
        self.fill_input(self.USERNAME_INPUT, username)
        self.fill_input(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
```

### Fixtures Reutilizables

```python
@pytest.fixture(scope="function")
def browser_setup():
    # Setup automático del navegador
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        # Teardown automático
        browser.close()
```

### Data-Driven Testing

```python
# Datos centralizados en utils/test_data.py
USUARIO_VALIDO = {
    "username": "john",
    "password": "demo"
}

def generar_datos_registro():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return {
        "username": f"usuario_test_{timestamp}",
        "password": "Test123!",
        # ...
    }
```

---

## Mejoras Futuras

- [ ] Agregar tests de API REST
- [ ] Implementar Allure Reports
- [ ] Dockerizar el proyecto
- [ ] Agregar tests de performance básicos
- [ ] Ejecución paralela de tests
- [ ] Tests de accesibilidad (A11y)
- [ ] Integración con herramientas de bug tracking

---

## Recursos de Aprendizaje

- [Documentación Playwright](https://playwright.dev/python/)
- [Documentación Pytest](https://docs.pytest.org/)
- [Page Object Pattern](https://martinfowler.com/bliki/PageObject.html)
- [Parabank Application](https://parabank.parasoft.com/)

---

## Autor

**RosaFG** - QA Automation Engineer

- GitHub: [@RosaFG](https://github.com/RosaFG)
- LinkedIn: [linkedin.com/in/tu-perfil](https://linkedin.com/in/rosafg)
- Email: rosafuegos@gmail.com

---

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## Agradecimientos

- Parasoft por proporcionar la aplicación de demostración Parabank
- Comunidad de Playwright por la excelente documentación
- Comunidad de Pytest por el framework flexible y extensible

---

**Si este proyecto te fue útil, considera darle una estrella en GitHub**

---

*Proyecto desarrollado con fines educativos y de demostración de habilidades en QA Automation.*