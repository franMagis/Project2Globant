from lib2to3.pgen2 import driver
from select import select
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


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

    product_sort_container = Select(self.browser.find_element(By.CLASS_NAME,'product_sort_container'))
    product_sort_container.select_by_value('lohi')

    elements_prices = self.browser.find_elements(By.CLASS_NAME,'inventory_item_price')

    price_element_list = []
    for price in elements_prices :
      price_element_list.append(float(price.text[1:]))
    assert price_element_list == sorted(price_element_list)

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

