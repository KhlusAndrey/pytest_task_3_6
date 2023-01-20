from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from pytest_task.pages.locators import ClickAddButton, NameAddedItem
import math


class ProductPage(BasePage):
    def click_to_add_cart(self):
        login_link = self.browser.find_element(*ClickAddButton.ADD_BUTTON)
        login_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_added_name_to_cart_item(self) -> str:
        added_item_name = self.browser.find_element(*NameAddedItem.NAME_ADDED_ITEM).text
        return added_item_name

    def get_added_price_to_cart_item(self) -> str:
        added_item_price = self.browser.find_element(*NameAddedItem.PRICE_ADDED_ITEM).text
        return added_item_price

    def click_to_cart(self):
        login_link = self.browser.find_element(*NameAddedItem.CART_BUTTON)
        login_link.click()

    def check_cart_name_price_dict(self, book_name: str, book_price: str) -> bool:
        """
        :param book_name: Название книги в каталоге
        :param book_price: Стоимость книги в каталоге
        :return: True если наименование и стоимость в каталоге и в корзине одинаковы
        """
        name_in_cart = self.browser.find_elements(*NameAddedItem.NAMES_ITEMS_IN_CART)
        pair_book_name_price = {}
        for n in name_in_cart:
            item_str = n.text.split('\n')
            name_added_item = item_str[0]
            price_added_item = item_str[4]
            pair_book_name_price[name_added_item] = price_added_item
        return pair_book_name_price.get(book_name) == book_price

    def compare_added_name_in_cart(self):
        name_in_cart = self.browser.find_element(*NameAddedItem.BOOK_NAME_IN_CART).text
        name_in_cart_compare = self.browser.find_element(*NameAddedItem.BOOK_NAME_IN_CART_COMPARE).text
        return name_in_cart == name_in_cart_compare

    def compare_added_price_in_cart(self):
        price_in_cart = self.browser.find_element(*NameAddedItem.PRICE_IN_CART).text
        price_in_cart_compare = self.browser.find_element(*NameAddedItem.PRICE_IN_CART_COMPARE).text
        return price_in_cart == price_in_cart_compare

