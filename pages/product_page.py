from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_cart(self):
        cart = self.browser.find_element(*ProductPageLocators.ADDING_GOODS_TO_BASKET)
        cart.click()

    def executing_alert(self):
        alert = self.solve_quiz_and_get_code()

    def price_and_items_correct(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        item = self.browser.find_element(*ProductPageLocators.GOOD).text
        price_check = self.browser.find_element(*ProductPageLocators.PRICE_CHECK).text
        items_check = self.browser.find_element(*ProductPageLocators.GOOD_CHECK).text
        assert price == price_check, "Price is not correct!"
        assert item == items_check, "Wrong item or name of item!"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
