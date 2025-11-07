from pages.base_page import BasePage

class RegistroPage(BasePage):
    
    # Selectores de campos del formulario
    FIRST_NAME_INPUT = "input[id='customer.firstName']"
    LAST_NAME_INPUT = "input[id='customer.lastName']"
    ADDRESS_INPUT = "input[id='customer.address.street']"
    CITY_INPUT = "input[id='customer.address.city']"
    STATE_INPUT = "input[id='customer.address.state']"
    ZIP_CODE_INPUT = "input[id='customer.address.zipCode']"
    PHONE_INPUT = "input[id='customer.phoneNumber']"
    SSN_INPUT = "input[id='customer.ssn']"
    USERNAME_INPUT = "input[id='customer.username']"
    PASSWORD_INPUT = "input[id='customer.password']"
    CONFIRM_PASSWORD_INPUT = "input[id='repeatedPassword']"
    
    # Botón de registro
    REGISTER_BUTTON = "input[type='submit'][value='Register']"
    
    # Link para ir a registro desde login
    REGISTER_LINK = "a:has-text('Register')"
    
    # Mensajes de éxito/error
    SUCCESS_MESSAGE = "h1.title, p:has-text('successfully'), div#rightPanel"
    ERROR_MESSAGE = "span.error"
    WELCOME_TITLE = "h1.title"
    CUSTOMER_NAME = "p.smallText"
    
    def __init__(self, page):
        super().__init__(page)
    
    def ir_a_registro_desde_login(self):
        if self.is_visible(self.REGISTER_LINK):
            self.click_element(self.REGISTER_LINK)
    def llenar_formulario_completo(self, datos):
        self.fill_input(self.FIRST_NAME_INPUT, datos.get("first_name", ""))
        self.fill_input(self.LAST_NAME_INPUT, datos.get("last_name", ""))
        self.fill_input(self.ADDRESS_INPUT, datos.get("address", ""))
        self.fill_input(self.CITY_INPUT, datos.get("city", ""))
        self.fill_input(self.STATE_INPUT, datos.get("state", ""))
        self.fill_input(self.ZIP_CODE_INPUT, datos.get("zip_code", ""))
        self.fill_input(self.PHONE_INPUT, datos.get("phone", ""))
        self.fill_input(self.SSN_INPUT, datos.get("ssn", ""))
        self.fill_input(self.USERNAME_INPUT, datos.get("username", ""))
        self.fill_input(self.PASSWORD_INPUT, datos.get("password", ""))
        self.fill_input(self.CONFIRM_PASSWORD_INPUT, datos.get("confirm_password", ""))
    
    def click_register_button(self):
        self.click_element(self.REGISTER_BUTTON)
    
    def registrar_usuario(self, datos):

        self.llenar_formulario_completo(datos)
        self.click_register_button()
    
    def is_registro_exitoso(self):
        # Opción 1: Verificar mensaje de éxito
        if self.is_visible("h1.title:has-text('Welcome')", timeout=5000):
            return True
        
        # Opción 2: Verificar que está en página de accounts
        if "overview" in self.page.url or "accounts" in self.page.url:
            return True
        
        # Opción 3: Verificar mensaje de bienvenida
        if self.is_visible(self.CUSTOMER_NAME, timeout=3000):
            return True
        
        return False
    
    def get_success_message(self):
        if self.is_visible(self.SUCCESS_MESSAGE):
            return self.get_text(self.SUCCESS_MESSAGE)
        return None
    
    def get_error_message(self):
        try:
            if self.is_visible(self.ERROR_MESSAGE, timeout=3000):
                return self.get_text(self.ERROR_MESSAGE)
            return None
        except:
            return None
    
    def verificar_campos_visibles(self):
        campos = {
            "first_name": self.is_visible(self.FIRST_NAME_INPUT),
            "last_name": self.is_visible(self.LAST_NAME_INPUT),
            "address": self.is_visible(self.ADDRESS_INPUT),
            "city": self.is_visible(self.CITY_INPUT),
            "state": self.is_visible(self.STATE_INPUT),
            "zip_code": self.is_visible(self.ZIP_CODE_INPUT),
            "phone": self.is_visible(self.PHONE_INPUT),
            "ssn": self.is_visible(self.SSN_INPUT),
            "username": self.is_visible(self.USERNAME_INPUT),
            "password": self.is_visible(self.PASSWORD_INPUT),
            "confirm_password": self.is_visible(self.CONFIRM_PASSWORD_INPUT),
            "register_button": self.is_visible(self.REGISTER_BUTTON)
        }
        return campos
    
    def clear_all_fields(self):
        """Limpia todos los campos del formulario"""
        fields = [
            self.FIRST_NAME_INPUT, self.LAST_NAME_INPUT, self.ADDRESS_INPUT,
            self.CITY_INPUT, self.STATE_INPUT, self.ZIP_CODE_INPUT,
            self.PHONE_INPUT, self.SSN_INPUT, self.USERNAME_INPUT,
            self.PASSWORD_INPUT, self.CONFIRM_PASSWORD_INPUT
        ]
        for field in fields:
            self.page.fill(field, "")