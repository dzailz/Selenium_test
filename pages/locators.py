from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators(object):
    GOOD = (By.XPATH, "/html/body/div[2]/div/ul/li[5]")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADDING_GOODS_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    GOOD_CHECK = (By.CSS_SELECTOR, "div.alertinner> strong")
    PRICE_CHECK = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")
