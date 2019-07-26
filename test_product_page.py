import time
import pytest

from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.user_can_add
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()
        email = f"{time.time()}@fakemail.test"
        password = "Ptxtvnenye;tynfrjqckj;ysqgfhjkm&"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        cart = ProductPage(browser, link)
        cart.open()
        cart.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        cart = ProductPage(browser, link)
        cart.open()
        cart.add_to_cart()
        cart.price_correct()
        cart.items_correct()


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
    cart = ProductPage(browser, link)
    cart.open()
    cart.add_to_cart()
    cart.price_correct()
    cart.items_correct()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_page()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    login = ProductPage(browser, link)
    login.open()
    login.go_to_login_page()


def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    cart = ProductPage(browser, link)
    cart.open()
    cart.add_to_cart()
    cart.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_message_disappeared_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
    cart = ProductPage(browser, link)
    cart.open()
    cart.add_to_cart()
    cart.success_message_is_disappeared()
