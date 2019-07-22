from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators(object):
    ADDING_GOODS_AT_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CORRECT__GOODS_ARE_ADDED_TO_BASKET = (By.CSS_SELECTOR, "div.alertinner> strong")
    PRICE_IS_CORRECT = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")