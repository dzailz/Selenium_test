from selenium.webdriver.common.by import By


class CartLocators(object):
    CART_IS_EMPTY = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/p")
    ITEMS_IN_CART = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/div[1]/div/h2")


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_LINK = (By.XPATH, "/html/body/header/div[1]/div/div[2]/span/a")


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators(object):
    GOOD = (By.XPATH, "/html/body/div[2]/div/ul/li[5]")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    ADDING_GOODS_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    GOOD_CHECK = (By.CSS_SELECTOR, "div.alertinner> strong")
    PRICE_CHECK = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")
