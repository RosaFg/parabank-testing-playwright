import pytest
from pages.login_page import LoginPage
from utils.test_data import USUARIO_VALIDO, USUARIO_INVALIDO, MENSAJES

@pytest.mark.smoke
def test_login_exitoso(browser_setup, take_screenshot):
    page = browser_setup
    login_page = LoginPage(page)
    
    # Screenshot inicial
    take_screenshot(page, "login_inicio")
    
    # Realizar login con credenciales válidas
    login_page.login(USUARIO_VALIDO["username"], USUARIO_VALIDO["password"])
    
    # Esperar a que cargue la página de cuentas
    page.wait_for_timeout(3000)
    
    # Tomar screenshot del resultado
    take_screenshot(page, "login_exitoso_resultado")
    
    # Verificaciones
    assert login_page.is_login_successful(), "El login debería ser exitoso"
    assert "overview" in page.url, "Debería redirigir a la página de overview"
    
    # Verificar mensaje de bienvenida
    welcome_message = login_page.get_welcome_message()
    assert welcome_message is not None, "Debería mostrar mensaje de bienvenida"
    
    print("✅ Test de login exitoso completado")


@pytest.mark.smoke
def test_login_con_credenciales_invalidas(browser_setup, take_screenshot):
    page = browser_setup
    login_page = LoginPage(page)
    
    # Realizar login con credenciales incorrectas
    login_page.fill_input(login_page.USERNAME_INPUT, USUARIO_INVALIDO["username"])
    login_page.fill_input(login_page.PASSWORD_INPUT, USUARIO_INVALIDO["password"])
    login_page.click_element(login_page.LOGIN_BUTTON)
    
    # Esperar a que cargue la respuesta
    page.wait_for_timeout(3000)
    
    # Tomar screenshot
    take_screenshot(page, "login_credenciales_invalidas_resultado")
    
    # Verificar que hay un mensaje de error o que no está logueado
    try:
        # Intentar encontrar mensaje de error
        error_locator = page.locator("div.error, p.error, span.error, [class*='error']")
        
        if error_locator.count() > 0:
            error_text = error_locator.first.inner_text()
            print(f"✅ Mensaje de error encontrado: {error_text}")
            assert len(error_text) > 0, "El mensaje de error no debería estar vacío"
        else:
            # Si no hay mensaje de error, verificar que NO esté en overview
            print(f"⚠️ No se encontró mensaje de error visible. URL actual: {page.url}")
            assert "overview" not in page.url, "El login no debería ser exitoso con credenciales inválidas"
    
    except Exception as e:
        print(f"⚠️ Excepción durante verificación: {e}")
        # Verificación final: asegurar que no está logueado
        assert "overview" not in page.url, "El login no debería redirigir a overview con credenciales inválidas"
    
    print("✅ Test de login con credenciales inválidas completado")


@pytest.mark.regression
def test_login_con_username_vacio(browser_setup, take_screenshot):
    page = browser_setup
    login_page = LoginPage(page)
    
    # Intentar login solo con password
    login_page.enter_password(USUARIO_VALIDO["password"])
    login_page.click_login_button()
    
    # Esperar respuesta
    page.wait_for_timeout(2000)
    take_screenshot(page, "login_username_vacio")
    
    # Verificar que muestra error o no permite login
    error_message = login_page.get_error_message()
    if error_message:
        print(f"✅ Mensaje de error: {error_message}")
        assert len(error_message) > 0
    else:
        # Verificar que no está logueado
        assert "overview" not in page.url, "No debería permitir login sin username"
    
    print("✅ Test de username vacío completado")


@pytest.mark.regression
def test_login_con_password_vacio(browser_setup, take_screenshot):
    page = browser_setup
    login_page = LoginPage(page)
    
    # Intentar login solo con username
    login_page.enter_username(USUARIO_VALIDO["username"])
    login_page.click_login_button()
    
    # Esperar respuesta
    page.wait_for_timeout(2000)
    take_screenshot(page, "login_password_vacio")
    
    # Verificar que muestra error o no permite login
    error_message = login_page.get_error_message()
    if error_message:
        print(f"✅ Mensaje de error: {error_message}")
        assert len(error_message) > 0
    else:
        # Verificar que no está logueado
        assert "overview" not in page.url, "No debería permitir login sin password"
    
    print("✅ Test de password vacío completado")


@pytest.mark.regression
def test_login_con_campos_vacios(browser_setup, take_screenshot):
    page = browser_setup
    login_page = LoginPage(page)
    
    # Hacer clic en login sin llenar campos
    login_page.click_login_button()
    
    # Esperar respuesta
    page.wait_for_timeout(2000)
    take_screenshot(page, "login_campos_vacios")
    
    # Verificar que muestra error o no permite login
    error_message = login_page.get_error_message()
    if error_message:
        print(f"✅ Mensaje de error: {error_message}")
        assert len(error_message) > 0
    else:
        # Verificar que no está logueado
        assert "overview" not in page.url, "No debería permitir login sin credenciales"
    
    print("✅ Test de campos vacíos completado")


@pytest.mark.regression
def test_verificar_elementos_visibles_en_pagina_login(browser_setup):
    page = browser_setup
    login_page = LoginPage(page)
    
    # Verificar elementos visibles
    assert login_page.is_visible(login_page.USERNAME_INPUT), "Campo username no visible"
    assert login_page.is_visible(login_page.PASSWORD_INPUT), "Campo password no visible"
    assert login_page.is_visible(login_page.LOGIN_BUTTON), "Botón login no visible"
    assert login_page.is_visible(login_page.REGISTER_LINK), "Link registro no visible"
    
    print("✅ Test de elementos visibles completado")


@pytest.mark.slow
def test_login_y_verificar_url(browser_setup, take_screenshot):
    page = browser_setup
    login_page = LoginPage(page)
    
    # Guardar URL inicial
    url_inicial = login_page.get_current_url()
    print(f"URL inicial: {url_inicial}")
    
    # Realizar login
    login_page.login(USUARIO_VALIDO["username"], USUARIO_VALIDO["password"])
    
    # Esperar a que cambie la URL
    page.wait_for_timeout(3000)
    take_screenshot(page, "login_cambio_url")
    
    # Verificar que la URL cambió
    url_final = login_page.get_current_url()
    print(f"URL final: {url_final}")
    
    assert url_inicial != url_final, "La URL no cambió después del login"
    assert "overview.htm" in url_final, "La URL no contiene 'overview.htm'"
    
    print("✅ Test de verificación de URL completado")


@pytest.mark.regression
def test_logout_despues_de_login(browser_setup, take_screenshot):
    page = browser_setup
    login_page = LoginPage(page)
    
    # Hacer login primero
    login_page.login(USUARIO_VALIDO["username"], USUARIO_VALIDO["password"])
    page.wait_for_timeout(2000)
    
    assert login_page.is_login_successful(), "Debe estar logueado"
    take_screenshot(page, "antes_logout")
    
    # Hacer logout
    logout_link = "a:has-text('Log Out')"
    if login_page.is_visible(logout_link):
        login_page.click_element(logout_link)
        page.wait_for_timeout(2000)
        take_screenshot(page, "despues_logout")
        
        # Verificar que volvió a la página de login
        assert "index.htm" in page.url or "login" in page.url.lower()
        print("✅ Logout exitoso")
    else:
        print("⚠️ Link de logout no encontrado")
    
    print("✅ Test de logout completado")