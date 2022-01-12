from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class SwagLabsCheckoutPageOne:

    # URL
    URL = 'https://www.saucedemo.com/checkout-step-one.html'

    # Locators
    NAME = (By.ID,'first-name')
    LASTNAME = (By.ID,'last-name')
    ZIPCODE = (By.ID,'postal-code')
    CONTINUE = (By.ID,'continue')
    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)


    def checkoutOne(self, name, lastName, zipCode):

        name_user = self.browser.find_element(*self.NAME)
        name_user.send_keys(name)
        last_name_user = self.browser.find_element(*self.LASTNAME)
        last_name_user.send_keys(lastName)
        zip_code_User = self.browser.find_element(*self.ZIPCODE)
        zip_code_User.send_keys(zipCode)


        continue_button = self.browser.find_element(*self.CONTINUE)
        continue_button.click()

