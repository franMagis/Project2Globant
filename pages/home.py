
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SwagLabsHomePage:

  # URL

  URL = 'https://www.saucedemo.com/inventory.html'

  # Locators

  USER_INPUT = (By.ID, 'user-name')
  PASSWORD_INPUT = (By.ID,'password')
  LOGIN =  (By.ID,'login-button')
  TITLE = (By.CLASS_NAME, 'title')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)


  def title_value(self):
    title = self.browser.find_element(*self.TITLE)
    value = title
    return value