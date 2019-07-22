from .pages.product_page import ProductPage
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


@pytest.mark.parametrize('link', urls)

def test_guest_can_add_goods_to_cart(browser, link):
    cart = ProductPage(browser, link)
    cart.open()
    cart.add_to_cart()
    cart.executing_alert()
    cart.price_and_goods_correct()