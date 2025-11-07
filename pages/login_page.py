from pages.base_page import BasePage

class LoginPage(BasePage):
    
    # Selectores de elementos
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "input[type='submit'][value='Log In']"
    REGISTER_LINK = "a:has-text('Register')"
    FORGOT_LOGIN_LINK = "a[href='lookup.htm']"
    LOGOUT_LINK = "a:has-text('Log Out')"
    
    # Selectores para verificar login exitoso
    ACCOUNTS_OVERVIEW_TITLE = "h1.title"
    WELCOME_MESSAGE = "p.smallText"
    
    def __init__(self, page):
        super().__init__(page)
    
    def login(self, username, password):
        self.fill_input(self.USERNAME_INPUT, username)
        self.fill_input(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
    
    def enter_username(self, username):
        self.fill_input(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        self.fill_input(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        try:
            # Intentar múltiples selectores de error
            error_selectors = [
                "div.error",
                "p.error", 
                "span.error",
                "[class*='error']",
                "text=/error/i",
                ".error"
            ]
            
            for selector in error_selectors:
                if self.is_visible(selector, timeout=2000):
                    error_text = self.get_text(selector)
                    if error_text and len(error_text.strip()) > 0:
                        return error_text
            
            return None
        except:
            return None
    
    def is_login_successful(self):
        return self.is_visible(self.ACCOUNTS_OVERVIEW_TITLE, timeout=5000)
    
    def get_welcome_message(self):
        if self.is_visible(self.WELCOME_MESSAGE):
            return self.get_text(self.WELCOME_MESSAGE)
        return None
    
    def click_register(self):
        self.click_element(self.REGISTER_LINK)
    
    def click_forgot_login(self):
        self.click_element(self.FORGOT_LOGIN_LINK)
    
    def click_logout(self):
        if self.is_visible(self.LOGOUT_LINK):
            self.click_element(self.LOGOUT_LINK)
            return True
        return False
    
    def clear_username(self):
        self.page.fill(self.USERNAME_INPUT, "")
    
    def clear_password(self):
        self.page.fill(self.PASSWORD_INPUT, "")
    
    def is_logout_visible(self):
        return self.is_visible(self.LOGOUT_LINK, timeout=3000)