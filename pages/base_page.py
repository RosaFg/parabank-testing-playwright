class BasePage:
    def __init__(self, page):
        self.page = page
    
    def navigate_to(self, url):
        self.page.goto(url)
    
    def click_element(self, selector):
        self.page.click(selector)
    
    def fill_input(self, selector, text):
        self.page.fill(selector, text)
    
    def get_text(self, selector):
        return self.page.inner_text(selector)
    
    def is_visible(self, selector, timeout=5000):
        try:
            self.page.wait_for_selector(selector, timeout=timeout, state="visible")
            return True
        except:
            return False
    
    def wait_for_element(self, selector, timeout=10000):
        self.page.wait_for_selector(selector, timeout=timeout)
    
    def get_current_url(self):
        return self.page.url
    
    def take_screenshot(self, name):
        from datetime import datetime
        import os
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"reports/screenshots/{name}_{timestamp}.png"
        os.makedirs("reports/screenshots", exist_ok=True)
        self.page.screenshot(path=screenshot_path)
        return screenshot_path
    
    def select_from_dropdown(self, selector, value):
        self.page.select_option(selector, value)
    
    def get_page_title(self):
        return self.page.title()
    
    def refresh_page(self):
        self.page.reload()
    
    def go_back(self):
        self.page.go_back()
    
    def wait_for_url(self, url_pattern, timeout=10000):
        self.page.wait_for_url(f"**/{url_pattern}**", timeout=timeout)
    
    def is_element_present(self, selector):
        return self.page.locator(selector).count() > 0
    
    def get_element_count(self, selector):
        return self.page.locator(selector).count()