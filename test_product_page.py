from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_goods_to_cart(browser):
    cart = ProductPage(browser, link)
    cart.open()
    cart.add_to_cart()
    cart.executing_alert()
    cart.price_and_goods_correct()