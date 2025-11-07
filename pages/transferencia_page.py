from pages.base_page import BasePage

class TransferenciaPage(BasePage):
    
    # Selectores de la página de transferencias
    AMOUNT_INPUT = "input[id='amount']"
    FROM_ACCOUNT_SELECT = "select[id='fromAccountId']"
    TO_ACCOUNT_SELECT = "select[id='toAccountId']"
    TRANSFER_BUTTON = "input[type='submit'][value='Transfer']"
    
    # Mensajes y resultados
    SUCCESS_MESSAGE = "h1.title:has-text('Transfer Complete')"
    ERROR_MESSAGE = "p.error"
    TRANSFER_DETAILS = "div#showResult"
    AMOUNT_TRANSFERRED = "span#amount"
    FROM_ACCOUNT_INFO = "span#fromAccountId"
    TO_ACCOUNT_INFO = "span#toAccountId"
    
    # Links de navegación
    TRANSFER_FUNDS_LINK = "a:has-text('Transfer Funds')"
    ACCOUNTS_OVERVIEW_LINK = "a:has-text('Accounts Overview')"
    
    # Elementos de cuenta
    ACCOUNT_BALANCE = "td:nth-child(2)"
    ACCOUNT_NUMBER = "td:nth-child(1) a"
    
    def __init__(self, page):

        super().__init__(page)
    
    def ir_a_transferencias(self):
        if self.is_visible(self.TRANSFER_FUNDS_LINK):
            self.click_element(self.TRANSFER_FUNDS_LINK)
    
    def realizar_transferencia(self, monto, cuenta_origen=None, cuenta_destino=None):
        # Ingresar monto
        self.fill_input(self.AMOUNT_INPUT, str(monto))
        
        # Seleccionar cuenta origen si se especifica
        if cuenta_origen is not None:
            self.select_from_dropdown(self.FROM_ACCOUNT_SELECT, str(cuenta_origen))
        
        # Seleccionar cuenta destino si se especifica
        if cuenta_destino is not None:
            self.select_from_dropdown(self.TO_ACCOUNT_SELECT, str(cuenta_destino))
        
        # Click en transferir
        self.click_element(self.TRANSFER_BUTTON)
    
    def ingresar_monto(self, monto):
        self.fill_input(self.AMOUNT_INPUT, str(monto))
    
    def seleccionar_cuenta_origen(self, indice):
        self.select_from_dropdown(self.FROM_ACCOUNT_SELECT, str(indice))
    
    def seleccionar_cuenta_destino(self, indice):
        self.select_from_dropdown(self.TO_ACCOUNT_SELECT, str(indice))
    
    def click_transfer(self):
        self.click_element(self.TRANSFER_BUTTON)
    
    def is_transferencia_exitosa(self):
        return self.is_visible(self.SUCCESS_MESSAGE, timeout=5000)
    
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
    
    def get_monto_transferido(self):
        try:
            if self.is_visible(self.AMOUNT_TRANSFERRED, timeout=3000):
                return self.get_text(self.AMOUNT_TRANSFERRED)
            return None
        except:
            return None
    
    def get_cuenta_origen_transferencia(self):
        try:
            if self.is_visible(self.FROM_ACCOUNT_INFO, timeout=3000):
                return self.get_text(self.FROM_ACCOUNT_INFO)
            return None
        except:
            return None
    
    def get_cuenta_destino_transferencia(self):
        try:
            if self.is_visible(self.TO_ACCOUNT_INFO, timeout=3000):
                return self.get_text(self.TO_ACCOUNT_INFO)
            return None
        except:
            return None
    
    def ir_a_accounts_overview(self):
        if self.is_visible(self.ACCOUNTS_OVERVIEW_LINK):
            self.click_element(self.ACCOUNTS_OVERVIEW_LINK)
    
    def get_available_accounts(self):
        try:
            # Obtener opciones del dropdown de cuenta origen
            options = self.page.locator(self.FROM_ACCOUNT_SELECT + " option").all()
            accounts = [option.inner_text() for option in options]
            return accounts
        except:
            return []
    
    def verificar_elementos_formulario(self):
        elementos = {
            "amount_input": self.is_visible(self.AMOUNT_INPUT),
            "from_account": self.is_visible(self.FROM_ACCOUNT_SELECT),
            "to_account": self.is_visible(self.TO_ACCOUNT_SELECT),
            "transfer_button": self.is_visible(self.TRANSFER_BUTTON)
        }
        return elementos
    
    def get_balance_cuenta(self, numero_cuenta):
        try:
            # Navegar a accounts overview
            self.ir_a_accounts_overview()
            self.page.wait_for_timeout(2000)
            
            # Buscar la fila de la cuenta
            row = self.page.locator(f"tr:has-text('{numero_cuenta}')").first
            
            if row.is_visible():
                # El balance está en la segunda columna
                balance = row.locator("td").nth(1).inner_text()
                return balance
            return None
        except:
            return None