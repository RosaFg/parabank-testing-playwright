import pytest
from pages.registro_page import RegistroPage
from utils.test_data import generar_datos_registro

def test_debug_registro(browser_setup):
    page = browser_setup
    registro_page = RegistroPage(page)
    
    # Ir a registro
    registro_page.ir_a_registro_desde_login()
    page.wait_for_timeout(2000)
    
    print(f"\n URL después de ir a registro: {page.url}")
    
    # Generar datos
    datos = generar_datos_registro()
    print(f"\n Datos generados: {datos}")
    
    # Llenar formulario
    registro_page.registrar_usuario(datos)
    page.wait_for_timeout(5000)  # Esperar más tiempo
    
    # Debug: Ver qué hay en la página
    print(f"\n URL después de registro: {page.url}")
    print(f"\n Título de la página: {page.title()}")
    
    # Tomar screenshot para ver qué pasó
    page.screenshot(path="debug_registro.png", full_page=True)
    print("\n Screenshot guardado: debug_registro.png")
    
    # Buscar diferentes elementos
    print("\n Buscando elementos...")
    
    if page.locator("h1.title").count() > 0:
        title_text = page.locator("h1.title").first.inner_text()
        print(f"   Título encontrado: {title_text}")
    
    if page.locator("p").count() > 0:
        paragraphs = page.locator("p").all()
        print(f"   Párrafos encontrados: {len(paragraphs)}")
        for i, p in enumerate(paragraphs[:3]):  # Primeros 3
            print(f"      P{i}: {p.inner_text()[:100]}")