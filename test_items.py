from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_be_button_add_to_cart(browser):
    browser.get(link)
    button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    # time.sleep(30)
    assert bool(button) is True, 'No button add cart on the page'

