from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_cart(self):
        cart = self.browser.find_element(*ProductPageLocators.ADDING_GOODS_AT_BASKET)
        cart.click()
    def executing_alert(self):
        alert = self.solve_quiz_and_get_code()