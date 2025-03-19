import unittest
from selenium.webdriver.support import expected_conditions as EC
from utilities.config import BASE_URL,SEARCH_TEXT, PAGE_NUMBER, PRODUCT_INDEX
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

class TestAmazon(BaseTest):
    def test_full_flow(self):
        # Step 1: Reject cookies
        home_page = HomePage(self.driver)
        home_page.rejection_of_cookies()

        # Step 2: Verify home page
        self.assertTrue(home_page.verify_home_page_loaded(), "Home page not loaded")

        # Step 3: Search for product
        home_page.search_for_product(SEARCH_TEXT)

        # Step 4: Verify search results
        search_page = SearchPage(self.driver)
        self.assertTrue(search_page.verify_search_results(SEARCH_TEXT), "No relevant search results found")

        # Step 5: Navigate to page and verify
        search_page.go_to_page(PAGE_NUMBER)
        self.assertIn(f"page={PAGE_NUMBER}", self.driver.current_url, "Page navigation failed")

        # Step 6: Click on product
        expected_product_name = search_page.click_product_by_index(PRODUCT_INDEX)

        # Step 7: Verify product page
        product_page = ProductPage(self.driver)
        actual_product_name = product_page.get_product_title()
        self.assertIn(expected_product_name, actual_product_name, "Product page mismatch")

        # Step 8: Add to cart
        initial_count = CartPage(self.driver).get_cart_count()
        added_to_cart = product_page.add_to_cart()
        self.assertTrue(added_to_cart, "Add to cart button not available")

        # Step 9: Verify cart count
        cart_page = CartPage(self.driver)
        self.assertTrue(cart_page.wait.until(
            lambda d: cart_page.get_cart_count() > initial_count
        ), "Cart count did not increase")

        # Step 10: Go to cart
        cart_page.click_element(cart_page.CART_COUNT)

        # Step 11: Verify cart contents
        self.assertTrue(cart_page.is_visible(cart_page.CART_HEADER), "Cart page not loaded")
        cart_product_name = cart_page.get_cart_product_name()
        self.assertIn(expected_product_name[:50], cart_product_name[:50], "Wrong product in cart")

        # Step 12: Delete product and verify
        before_delete_count = cart_page.get_cart_count()
        cart_page.delete_product()
        self.assertTrue(cart_page.wait.until(
            lambda d: cart_page.get_cart_count() < before_delete_count
        ), "Product not removed from cart")

        # Step 13: Return to home page
        home_page.navigate_to_home_page()
        self.assertIn(BASE_URL,self.driver.current_url, "Not returned to home page")

if __name__ == "__main__":
    unittest.main()