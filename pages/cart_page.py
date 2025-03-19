from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_COUNT = (By.ID, 'nav-cart-count')
    DELETE_BUTTON = (By.XPATH, '//span[@data-action="delete"]')
    CART_HEADER = (By.ID, 'sc-active-items-header')
    CART_ITEM_NAME = (By.TAG_NAME, 'h4')

    def get_cart_count(self):
        return int(self.get_element_text(self.CART_COUNT))

    def delete_product(self):
        self.click_element(self.DELETE_BUTTON)

    def get_cart_product_name(self):
        return self.get_element_text(self.CART_ITEM_NAME)