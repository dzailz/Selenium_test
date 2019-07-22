from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_cart(self):
        cart = self.browser.find_element(*ProductPageLocators.ADDING_GOODS_TO_BASKET)
        cart.click()

    def executing_alert(self):
        alert = self.solve_quiz_and_get_code()

    def price_and_goods_correct(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        good = self.browser.find_element(*ProductPageLocators.GOOD).text
        price_check = self.browser.find_element(*ProductPageLocators.PRICE_CHECK).text
        goods_check = self.browser.find_element(*ProductPageLocators.GOOD_CHECK).text
        assert price == price_check, "Price not Correct!"
        assert good == goods_check, "Good is not same!"
