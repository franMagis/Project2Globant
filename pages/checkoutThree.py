from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class SwagLabsCheckoutPageThree:

    # URL
    URL = 'https://www.saucedemo.com/checkout-complete.html'

    # Locators

    HOME = (By.ID,'back-to-products"')
    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def back(self):

        back_home = self.browser.find_element(*self.HOME)
        back_home.click()


