from selenium.webdriver.common.by import By
from utilities.config import PAGE_NUMBER
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time

class SearchPage(BasePage):
    PRODUCTS_LIST = (By.XPATH, '//*[@role="listitem"]/div[@class="sg-col-inner"]')
    PRODUCT_NAME = (By.XPATH, './/h2')
    PAGE_LINK = (By.XPATH, f'(//*[@class="s-pagination-strip"]//li)[{PAGE_NUMBER}]')

    def verify_search_results(self, search_text):
        first_product = self.wait.until(EC.visibility_of_any_elements_located(self.PRODUCTS_LIST))[0]
        product_name = first_product.find_element(*self.PRODUCT_NAME).text.lower()
        return search_text.lower() in product_name

    def go_to_page(self, page_number):
        page_element = (By.XPATH, f'(//*[@class="s-pagination-strip"]//li)[{page_number}]')
        element = self.wait.until(EC.element_to_be_clickable(page_element))
        self.scroll_to_element_center(element)
        self.click_element(page_element)
        self.wait_for_url_contains(f'page={page_number}')

    def click_product_by_index(self, index):
        time.sleep(7)
        products = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCTS_LIST))
        if len(products) > index:
            product = products[index]
            self.scroll_to_element_center(product)
            product_name = product.find_element(*self.PRODUCT_NAME).text
            product.click()
            return product_name
        raise IndexError(f"Product index {index} out of range")