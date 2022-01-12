
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SwagLabsLogInPage:

  # URL

  URL = 'https://www.saucedemo.com/'

  # Locators

  USER_INPUT = (By.ID, 'user-name')
  PASSWORD_INPUT = (By.ID,'password')
  LOGIN =  (By.ID,'login-button')
  ERROR = (By.XPATH, '//h3[@data-test="error"]')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def logIn(self, userName, password):

    user_input = self.browser.find_element(*self.USER_INPUT)
    user_input.send_keys(userName + Keys.RETURN)

    password_input = self.browser.find_element(*self.PASSWORD_INPUT)
    password_input.send_keys(password + Keys.RETURN)

    logIn_button = self.browser.find_element(*self.LOGIN)
    logIn_button.click()

  def errorMs(self):

    error = self.browser.find_element(*self.ERROR)
    return error.text

