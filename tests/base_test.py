import unittest
from selenium import webdriver
from utilities.config import BASE_URL

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(BASE_URL)

    def tearDown(self):
        self.driver.quit()