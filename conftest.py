import pytest
from playwright.sync_api import sync_playwright
from datetime import datetime
import os

# Configuración global
BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"
SCREENSHOT_DIR = "reports/screenshots"
REPORTS_DIR = "reports/html"
VIDEOS_DIR = "reports/videos"

# Crear directorios si no existen
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(VIDEOS_DIR, exist_ok=True)

@pytest.fixture(scope="function")
def browser_setup():
    with sync_playwright() as p:
        # Configuración del navegador
        browser = p.chromium.launch(
            headless=False,  # Cambiar a True para ejecución sin interfaz
            slow_mo=500      # Ralentiza las acciones para ver mejor (en milisegundos)
        )
        
        # Crear contexto con configuración adicional
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            record_video_dir=VIDEOS_DIR,  # Graba videos de los tests
        )
        
        page = context.new_page()
        page.goto(BASE_URL)
        
        # Retorna el page object para usarlo en los tests
        yield page
        
        # Cleanup: cierra todo después del test
        context.close()
        browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Obtiene el page object del test
        page = item.funcargs.get('browser_setup')
        
        if page:
            # Genera nombre único para el screenshot
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name
            screenshot_name = f"{test_name}_{timestamp}_FAILED.png"
            screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)
            
            # Captura el screenshot
            try:
                page.screenshot(path=screenshot_path, full_page=True)
                print(f"\n Screenshot capturado: {screenshot_path}")
            except Exception as e:
                print(f"\n⚠️ No se pudo capturar screenshot: {e}")

@pytest.fixture(scope="function")
def take_screenshot():
    def _take_screenshot(page, name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)
        try:
            page.screenshot(path=screenshot_path)
            print(f"\n Screenshot guardado: {screenshot_path}")
            return screenshot_path
        except Exception as e:
            print(f"\n⚠️ Error al guardar screenshot: {e}")
            return None
    
    return _take_screenshot

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: marca tests como smoke tests (críticos)"
    )
    config.addinivalue_line(
        "markers", "regression: marca tests de regresión completa"
    )
    config.addinivalue_line(
        "markers", "slow: marca tests lentos"
    )