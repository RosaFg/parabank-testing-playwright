from datetime import datetime

# Datos de usuario para login
USUARIO_VALIDO = {
    "username": "john",
    "password": "demo"
}

USUARIO_INVALIDO = {
    "username": "usuario_invalido_12345",
    "password": "password_incorrecta_xyz"
}

# Datos para registro de nuevo usuario
def generar_datos_registro():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return {
        "first_name": "Juan",
        "last_name": "Pérez",
        "address": "Calle Principal 123",
        "city": "Santiago",
        "state": "Región Metropolitana",
        "zip_code": "12345",
        "phone": "123456789",
        "ssn": "123-45-6789",
        "username": f"usuario_test_{timestamp}",
        "password": "Test123!",
        "confirm_password": "Test123!"
    }

#  para transferencias
TRANSFERENCIA_VALIDA = {
    "monto": "100",
    "cuenta_destino": "13344"  # Cuenta de ejemplo
}

# Mensajes esperados
MENSAJES = {
    "login_exitoso": "Accounts Overview",
    "login_fallido": "The username and password could not be verified.",
    "registro_exitoso": "Your account was created successfully",
    "transferencia_exitosa": "Transfer Complete!",
    "error_monto_invalido": "The amount cannot be empty"
}

# URLs importantes
URLS = {
    "base": "https://parabank.parasoft.com/parabank/index.htm",
    "registro": "https://parabank.parasoft.com/parabank/register.htm",
    "login": "https://parabank.parasoft.com/parabank/index.htm",
    "overview": "https://parabank.parasoft.com/parabank/overview.htm",
    "transferencia": "https://parabank.parasoft.com/parabank/transfer.htm"
}