from lib2to3.pgen2 import driver
from select import select
from tkinter.tix import Select

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

  CART = (By.CLASS_NAME, 'shopping_cart_link')
  CARTSPAN = (By.CLASS_NAME,'shopping_cart_badge')


  CONTEINER = (By.CLASS_NAME, 'product_sort_container')
  LOHI = (By.ID,'lohi')

  PRODUCT_BACKPACK = (By.ID,'add-to-cart-sauce-labs-backpack')

  # Initializer

  span_cart = 0
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

  def add_back_pack(self):

    button = self.browser.find_element(*self.PRODUCT_BACKPACK)
    button.click()
    self.span_cart += 1


  def order_prices(self):

    container = self.browser.find_element(*self.CONTEINER)
    container.click()

    dropdown = Select(self.browser.find_element_by_id('product_sort_container'))
    dropdown.select_by_index(3).click()

  def title_value(self):
    title = self.browser.find_element(*self.TITLE)
    value = title
    return value

  def goCart(self):

    cart = self.browser.find_element(*self.CART)
    cart.click()

  def cart_span(self):

    cart_span = self.browser.find_element(*self.CARTSPAN)
    span_count = cart_span.text
    return int(span_count)

