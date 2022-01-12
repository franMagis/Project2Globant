from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class SwagLabsCheckoutPageTwo:

    # URL
    URL = 'https://www.saucedemo.com/checkout-step-two.html'

    # Locators
    FINISH = (By.ID,'finish')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)


    def finish(self):

        button = self.browser.find_element(*self.FINISH)
        button.click()

