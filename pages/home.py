
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
  MENU =  (By.ID,'react-burger-menu-btn')
  LOGOUT = (By.ID,'logout_sidebar_link')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  def load(self):
    self.browser.get(self.URL)

  def log_out(self):
    menu = self.browser.find_element(*self.MENU)
    menu.click()
    logOut = self.browser.find_element(*self.LOGOUT)
    logOut.click()


  def title_value(self):
    title = self.browser.find_element(*self.TITLE)
    value = title
    return value