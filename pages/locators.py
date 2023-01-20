from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ClickAddButton:
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class NameAddedItem:
    NAME_ADDED_ITEM = (By.CSS_SELECTOR, 'div.col-sm-6:nth-child(2) > h1:nth-child(1)')
    PRICE_ADDED_ITEM = (By.CSS_SELECTOR, 'p.price_color:nth-child(2)')
    CART_BUTTON = (By.CSS_SELECTOR, '.btn-group > a:nth-child(1)')
    NAMES_ITEMS_IN_CART = (By.CSS_SELECTOR, '#basket_formset')
    BOOK_NAME_IN_CART = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    BOOK_NAME_IN_CART_COMPARE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    PRICE_IN_CART = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    PRICE_IN_CART_COMPARE = (By.CSS_SELECTOR, ' #content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')

