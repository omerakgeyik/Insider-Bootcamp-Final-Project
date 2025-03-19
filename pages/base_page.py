from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()

    def send_keys(self, by_locator, text):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text

    def is_visible(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).is_displayed()

    def scroll_to_element_center(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_contains(self, text):
        return self.wait.until(EC.url_contains(text))