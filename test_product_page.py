from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
import pytest

# class TestUserAddToCartFromProductPage:
#     @pytest.mark.parametrize(scope="function", autouse=True)

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    cart = ProductPage(browser, link)
    cart.open()
    cart.add_to_cart()
    cart.should_not_be_success_message()


def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_page()


def test_guest_cant_see_success_message(browser):
    cart = ProductPage(browser, link)
    cart.open()
    cart.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_cart(browser):
    cart = ProductPage(browser, link)
    cart.open()
    cart.add_to_cart()
    cart.success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    login = ProductPage(browser, link)
    login.open()
    login.go_to_login_page()
