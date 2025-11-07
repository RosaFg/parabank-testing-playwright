import pytest
from pages.login_page import LoginPage
from pages.transferencia_page import TransferenciaPage
from utils.test_data import USUARIO_VALIDO

@pytest.fixture(scope="function")
def transferencia_setup(browser_setup):
    page = browser_setup
    login_page = LoginPage(page)
    
    # Hacer login primero
    login_page.login(USUARIO_VALIDO["username"], USUARIO_VALIDO["password"])
    page.wait_for_timeout(3000)
    
    # Navegar a transferencias
    transferencia_page = TransferenciaPage(page)
    transferencia_page.ir_a_transferencias()
    page.wait_for_timeout(2000)
    
    return page, transferencia_page

@pytest.mark.smoke
def test_transferencia_exitosa(transferencia_setup, take_screenshot):
    page, transferencia_page = transferencia_setup
    
    take_screenshot(page, "transferencia_inicio")
    
    # Realizar transferencia de $100
    monto = "100"
    transferencia_page.realizar_transferencia(monto)
    
    # Esperar resultado
    page.wait_for_timeout(3000)
    take_screenshot(page, "transferencia_exitosa")
    
    # Verificaciones
    assert transferencia_page.is_transferencia_exitosa(), "La transferencia debería ser exitosa"
    
    success_message = transferencia_page.get_success_message()
    assert success_message is not None, "Debería mostrar mensaje de éxito"
    assert "Transfer Complete" in success_message or "complete" in success_message.lower()
    
    print(f"✅ Transferencia de ${monto} realizada exitosamente")

@pytest.mark.xfail(reason="BUG: Parabank permite transferencias con monto $0 - Defecto conocido", strict=False)
@pytest.mark.regression
def test_transferencia_con_monto_cero(transferencia_setup, take_screenshot):
    page, transferencia_page = transferencia_setup
    
    # Intentar transferir $0
    transferencia_page.realizar_transferencia("0")
    page.wait_for_timeout(2000)
    
    take_screenshot(page, "transferencia_monto_cero")
    
    # Verificar error o que no se completó
    error_message = transferencia_page.get_error_message()
    
    if error_message:
        print(f"✅ Error esperado: {error_message}")
        assert len(error_message) > 0
    else:
        # BUG: La aplicación permite monto 0
        print(" BUG ENCONTRADO: Parabank permite transferencia con monto $0")
        assert not transferencia_page.is_transferencia_exitosa(), "No debería permitir monto 0"
    
    print("✅ Test de monto cero completado")

@pytest.mark.xfail(reason="BUG: Parabank permite transferencias con monto negativo - Defecto conocido", strict=False)
@pytest.mark.regression
def test_transferencia_con_monto_negativo(transferencia_setup, take_screenshot):
    page, transferencia_page = transferencia_setup
    
    # Intentar transferir monto negativo
    transferencia_page.realizar_transferencia("-50")
    page.wait_for_timeout(2000)
    
    take_screenshot(page, "transferencia_monto_negativo")
    
    # Verificar error
    error_message = transferencia_page.get_error_message()
    
    if error_message:
        print(f"✅ Error esperado: {error_message}")
        assert len(error_message) > 0
    else:
        # BUG: La aplicación permite monto negativo
        print("BUG ENCONTRADO: Parabank permite transferencia con monto negativo")
        assert not transferencia_page.is_transferencia_exitosa(), "No debería permitir monto negativo"
    
    print("✅ Test de monto negativo completado")

@pytest.mark.regression
def test_transferencia_sin_monto(transferencia_setup, take_screenshot):
    page, transferencia_page = transferencia_setup
    
    # Intentar transferir sin monto
    transferencia_page.click_transfer()
    page.wait_for_timeout(2000)
    
    take_screenshot(page, "transferencia_sin_monto")
    
    # Verificar error
    error_message = transferencia_page.get_error_message()
    
    if error_message:
        print(f"✅ Error de validación: {error_message}")
        assert len(error_message) > 0
    else:
        assert not transferencia_page.is_transferencia_exitosa(), "No debería permitir transferir sin monto"
    
    print("✅ Test sin monto completado")

@pytest.mark.regression
def test_transferencia_con_texto_en_monto(transferencia_setup, take_screenshot):
    page, transferencia_page = transferencia_setup
    
    # Intentar transferir con texto
    transferencia_page.ingresar_monto("abc")
    transferencia_page.click_transfer()
    page.wait_for_timeout(2000)
    
    take_screenshot(page, "transferencia_texto_monto")
    
    # Verificar que no permite o da error
    error_message = transferencia_page.get_error_message()
    
    if error_message:
        print(f"✅ Error: {error_message}")
        assert len(error_message) > 0
    else:
        assert not transferencia_page.is_transferencia_exitosa(), "No debería aceptar texto como monto"
    
    print("✅ Test con texto en monto completado")

@pytest.mark.regression
def test_verificar_elementos_formulario_transferencia(transferencia_setup):
    page, transferencia_page = transferencia_setup
    
    # Verificar elementos
    elementos = transferencia_page.verificar_elementos_formulario()
    
    # Validar que todos estén visibles
    for elemento, visible in elementos.items():
        assert visible, f"Elemento {elemento} no está visible"
        print(f"✅ Elemento {elemento}: visible")
    
    print("✅ Test de elementos del formulario completado")

@pytest.mark.smoke
def test_transferencia_y_verificar_detalles(transferencia_setup, take_screenshot):
    page, transferencia_page = transferencia_setup
    
    # Realizar transferencia
    monto = "50"
    transferencia_page.realizar_transferencia(monto)
    page.wait_for_timeout(3000)
    
    take_screenshot(page, "transferencia_detalles")
    
    # Verificar que fue exitosa
    assert transferencia_page.is_transferencia_exitosa(), "Transferencia debería ser exitosa"
    
    # Verificar detalles (si están disponibles en la página)
    monto_transferido = transferencia_page.get_monto_transferido()
    
    if monto_transferido:
        print(f"✅ Monto transferido: ${monto_transferido}")
        assert monto in monto_transferido, f"El monto debería ser ${monto}"
    
    print("✅ Test de detalles de transferencia completado")

@pytest.mark.slow
def test_multiples_transferencias_consecutivas(transferencia_setup, take_screenshot):
    page, transferencia_page = transferencia_setup
    
    # Primera transferencia
    transferencia_page.realizar_transferencia("25")
    page.wait_for_timeout(2000)
    
    assert transferencia_page.is_transferencia_exitosa(), "Primera transferencia debería ser exitosa"
    take_screenshot(page, "primera_transferencia")
    
    # Volver a transferencias
    transferencia_page.ir_a_transferencias()
    page.wait_for_timeout(2000)
    
    # Segunda transferencia
    transferencia_page.realizar_transferencia("30")
    page.wait_for_timeout(2000)
    
    assert transferencia_page.is_transferencia_exitosa(), "Segunda transferencia debería ser exitosa"
    take_screenshot(page, "segunda_transferencia")
    
    print("✅ Test de múltiples transferencias completado")

@pytest.mark.regression
def test_obtener_cuentas_disponibles(transferencia_setup):
    page, transferencia_page = transferencia_setup
    
    # Obtener cuentas disponibles
    cuentas = transferencia_page.get_available_accounts()
    
    print(f"Cuentas disponibles: {cuentas}")
    
    # Verificar que hay cuentas
    assert len(cuentas) > 0, "Debería haber al menos una cuenta disponible"
    
    print(f"✅ Se encontraron {len(cuentas)} cuenta(s) disponible(s)")

@pytest.mark.regression
def test_navegacion_a_transferencias_desde_menu(browser_setup, take_screenshot):
    page = browser_setup
    login_page = LoginPage(page)
    
    # Login
    login_page.login(USUARIO_VALIDO["username"], USUARIO_VALIDO["password"])
    page.wait_for_timeout(2000)
    
    url_inicial = page.url
    take_screenshot(page, "antes_ir_transferencias")
    
    # Navegar a transferencias
    transferencia_page = TransferenciaPage(page)
    transferencia_page.ir_a_transferencias()
    page.wait_for_timeout(2000)
    
    take_screenshot(page, "despues_ir_transferencias")
    url_transferencias = page.url
    
    # Verificar navegación
    assert url_inicial != url_transferencias, "La URL debería cambiar"
    assert "transfer" in url_transferencias.lower(), "URL debería contener 'transfer'"
    
    # Verificar elementos del formulario
    assert transferencia_page.is_visible(transferencia_page.TRANSFER_BUTTON), "Debería ver botón Transfer"
    
    print("✅ Navegación a transferencias exitosa")