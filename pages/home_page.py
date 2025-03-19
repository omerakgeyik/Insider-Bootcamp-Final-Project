from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT_BUTTON = (By.ID, 'nav-search-submit-button')
    HOME_LOGO = (By.ID, 'nav-logo-sprites')
    REJECT_COOKIE = (By.ID, 'sp-cc-rejectall-link')

    def rejection_of_cookies(self):
        cookies = self.wait.until(EC.presence_of_element_located(self.REJECT_COOKIE))
        self.click_element(cookies)

    def verify_home_page_loaded(self):
        return self.is_visible(self.SEARCH_BOX)

    def search_for_product(self, text):
        self.send_keys(self.SEARCH_BOX, text)
        self.click_element(self.SEARCH_SUBMIT_BUTTON)
    
    def navigate_to_home_page(self):
        self.click_element(self.HOME_LOGO)