from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
    PRODUCT_TITLE = (By.ID, 'title')

    def get_product_title(self):
        return self.get_element_text(self.PRODUCT_TITLE)

    def add_to_cart(self):
        if self.is_visible(self.ADD_TO_CART_BUTTON):
            self.click_element(self.ADD_TO_CART_BUTTON)
            return True
        return False