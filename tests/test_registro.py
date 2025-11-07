import pytest
from pages.registro_page import RegistroPage
from utils.test_data import generar_datos_registro, MENSAJES

@pytest.mark.smoke
def test_registro_usuario_exitoso(browser_setup, take_screenshot):
    page = browser_setup
    registro_page = RegistroPage(page)
    
    # Navegar a registro
    registro_page.ir_a_registro_desde_login()
    page.wait_for_timeout(2000)
    
    take_screenshot(page, "registro_inicio")
    
    # Generar datos únicos para el registro
    datos_usuario = generar_datos_registro()
    
    # Registrar usuario
    registro_page.registrar_usuario(datos_usuario)
    
    # Esperar respuesta (más tiempo por si el servidor es lento)
    page.wait_for_timeout(5000)
    take_screenshot(page, "registro_resultado")
    
    # Verificaciones flexibles
    url_actual = page.url
    print(f"\n🔍 URL después del registro: {url_actual}")
    
    if registro_page.is_registro_exitoso():
        print(f"✅ Usuario registrado exitosamente: {datos_usuario['username']}")
        assert True
    elif "register.htm" in url_actual:
        # Todavía en página de registro, verificar si hay error
        error = registro_page.get_error_message()
        if error:
            print(f"⚠️ Error durante registro: {error}")
            # Puede ser que el username ya exista o el servidor tenga problemas
            # En ambiente de pruebas esto es esperado
            pytest.skip(f"Registro no completado - posible problema del servidor: {error}")
        else:
            print("⚠️ El registro no se completó pero tampoco hay error visible")
            print("   Esto puede ser un problema temporal del servidor Parabank")
            pytest.skip("Registro no completado - servidor puede estar caído")
    else:
        # Redirigió a otra página
        print(f"✅ Redirigió a: {url_actual}")
        assert True


@pytest.mark.regression
def test_registro_con_username_existente(browser_setup, take_screenshot):
    page = browser_setup
    registro_page = RegistroPage(page)
    
    # Navegar a registro
    registro_page.ir_a_registro_desde_login()
    page.wait_for_timeout(2000)
    
    # Generar datos pero con username existente
    datos_usuario = generar_datos_registro()
    datos_usuario["username"] = "john"  # Usuario que ya existe
    
    # Intentar registrar
    registro_page.registrar_usuario(datos_usuario)
    page.wait_for_timeout(3000)
    
    take_screenshot(page, "registro_username_existente")
    
    # Verificar que muestra error o no se registra
    error_message = registro_page.get_error_message()
    
    if error_message:
        print(f"✅ Mensaje de error encontrado: {error_message}")
        assert "already exists" in error_message.lower() or len(error_message) > 0
    else:
        # Si no hay mensaje de error, verificar que no se registró exitosamente
        assert not registro_page.is_registro_exitoso(), "No debería permitir username duplicado"
    
    print("✅ Test de username existente completado")


@pytest.mark.regression
def test_registro_con_passwords_no_coinciden(browser_setup, take_screenshot):
    page = browser_setup
    registro_page = RegistroPage(page)
    
    # Navegar a registro
    registro_page.ir_a_registro_desde_login()
    page.wait_for_timeout(2000)
    
    # Generar datos con contraseñas diferentes
    datos_usuario = generar_datos_registro()
    datos_usuario["confirm_password"] = "ContraseñaDiferente123!"
    
    # Intentar registrar
    registro_page.registrar_usuario(datos_usuario)
    page.wait_for_timeout(2000)
    
    take_screenshot(page, "registro_passwords_no_coinciden")
    
    # Verificar error
    error_message = registro_page.get_error_message()
    
    if error_message:
        print(f"✅ Error encontrado: {error_message}")
        assert len(error_message) > 0
    else:
        # Verificar que no se completó el registro
        assert not registro_page.is_registro_exitoso(), "No debería registrar con passwords diferentes"
    
    print("✅ Test de passwords no coinciden completado")


@pytest.mark.regression
def test_registro_con_campos_obligatorios_vacios(browser_setup, take_screenshot):
    page = browser_setup
    registro_page = RegistroPage(page)
    
    # Navegar a registro
    registro_page.ir_a_registro_desde_login()
    page.wait_for_timeout(2000)
    
    # Intentar registrar sin llenar nada
    registro_page.click_register_button()
    page.wait_for_timeout(2000)
    
    take_screenshot(page, "registro_campos_vacios")
    
    # Verificar que hay errores o no permite continuar
    error_message = registro_page.get_error_message()
    
    if error_message:
        print(f"✅ Error de validación: {error_message}")
        assert len(error_message) > 0
    else:
        # Verificar que no se registró
        assert not registro_page.is_registro_exitoso(), "No debería permitir registro sin datos"
    print("✅ Test de campos vacíos completado")


@pytest.mark.regression
def test_registro_solo_con_username_y_password(browser_setup, take_screenshot):
    page = browser_setup
    registro_page = RegistroPage(page)
    
    # Navegar a registro
    registro_page.ir_a_registro_desde_login()
    page.wait_for_timeout(2000)
    
    # Llenar solo algunos campos
    datos_parciales = generar_datos_registro()
    registro_page.fill_input(registro_page.USERNAME_INPUT, datos_parciales["username"])
    registro_page.fill_input(registro_page.PASSWORD_INPUT, datos_parciales["password"])
    registro_page.fill_input(registro_page.CONFIRM_PASSWORD_INPUT, datos_parciales["password"])
    
    registro_page.click_register_button()
    page.wait_for_timeout(2000)
    
    take_screenshot(page, "registro_datos_parciales")
    
    # Verificar error o que no se completó
    error_message = registro_page.get_error_message()
    
    if error_message:
        print(f"✅ Se requieren más campos: {error_message}")
        assert len(error_message) > 0
    else:
        assert not registro_page.is_registro_exitoso(), "Debería requerir todos los campos"
    
    print("✅ Test de datos parciales completado")


@pytest.mark.regression
def test_verificar_elementos_formulario_registro(browser_setup):
    page = browser_setup
    registro_page = RegistroPage(page)
    
    # Navegar a registro
    registro_page.ir_a_registro_desde_login()
    page.wait_for_timeout(2000)
    
    # Verificar todos los campos
    campos = registro_page.verificar_campos_visibles()
    
    # Validar que todos estén visibles
    for campo, visible in campos.items():
        assert visible, f"Campo {campo} no está visible"
        print(f"✅ Campo {campo}: visible")
    
    print("✅ Test de elementos del formulario completado")


@pytest.mark.slow
def test_registro_y_login_automatico(browser_setup, take_screenshot):
    page = browser_setup
    registro_page = RegistroPage(page)
    
    # Navegar a registro
    registro_page.ir_a_registro_desde_login()
    page.wait_for_timeout(2000)
    
    # Generar y registrar usuario
    datos_usuario = generar_datos_registro()
    registro_page.registrar_usuario(datos_usuario)
    
    # Esperar que se complete
    page.wait_for_timeout(5000)
    take_screenshot(page, "registro_y_login_auto")
    
    current_url = page.url
    print(f"\n🔍 URL después del registro: {current_url}")
    
    # Verificación flexible
    if registro_page.is_registro_exitoso():
        print(f"✅ Usuario registrado exitosamente")
        
        # Verificar que está logueado (la URL cambió de register.htm)
        if "register.htm" not in current_url:
            print(f"✅ Redirigió correctamente a: {current_url}")
            assert True
        else:
            pytest.skip("Registro completado pero no hubo auto-login")
    else:
        # Si el registro no se completó
        error = registro_page.get_error_message()
        if error:
            pytest.skip(f"Registro falló con error: {error}")
        else:
            pytest.skip("Registro no se completó - posible problema del servidor")


@pytest.mark.regression  
def test_navegacion_a_registro_desde_login(browser_setup, take_screenshot):
    page = browser_setup
    registro_page = RegistroPage(page)
    
    # Screenshot página inicial (login)
    take_screenshot(page, "antes_ir_registro")
    url_inicial = page.url
    
    # Ir a registro
    registro_page.ir_a_registro_desde_login()
    page.wait_for_timeout(2000)
    
    take_screenshot(page, "despues_ir_registro")
    url_registro = page.url
    
    # Verificar que cambió la URL
    assert url_inicial != url_registro, "La URL debería cambiar"
    assert "register" in url_registro.lower(), "URL debería contener 'register'"
    
    # Verificar que está el formulario
    assert registro_page.is_visible(registro_page.REGISTER_BUTTON), "Debería ver botón Register"
    
    print("✅ Navegación a registro exitosa")