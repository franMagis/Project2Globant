from selenium.webdriver.common.by import By


class SwagLabsCart:

    #URL
    URL: 'https://www.saucedemo.com/cart.html'

    #Locators
    CHECKOUT = (By.ID, 'checkout')

    #Initializer
    def __init__(self, browser):
        self.browser = browser


    #Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def checkout(self):

        button = self.browser.find_element(*self.CHECKOUT)
        button.click()