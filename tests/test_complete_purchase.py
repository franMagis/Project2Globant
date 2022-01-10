"""
These tests cover SwagLabs log in.
"""
import pytest

from pages.cart import SwagLabsCartPage
from pages.home import SwagLabsHomePage
from pages.result import swagLabsResultPage
from pages.logIn import SwagLabsLogInPage
from pages.checkoutOne import SwagLabsCheckoutPageOne


#----------------------Cart test---------------------------------------------------------------#
@pytest.mark.parametrize('userName', ['standard_user', 'problem_user','performance_glitch_user'])
@pytest.mark.parametrize('password', ['secret_sauce'])
#@pytest.mark.parametrize('name', ['Francisco'])
#@pytest.mark.parametrize('lastName', ['Magis'])
@pytest.mark.parametrize('zipCode', ['11300'])

def test_complete_purchase_out(browser, userName, password,zipCode):

  logIn_page = SwagLabsLogInPage(browser)
  result_page = swagLabsResultPage(browser)
  home_page = SwagLabsHomePage(browser)
  cart_page = SwagLabsCartPage(browser)
  checkOut_page = SwagLabsCheckoutPageOne(browser)

  logIn_page.load()
  logIn_page.logIn(userName, password)

  # Given the log in page of swag
  home_page.load()
  # When the user type correct credentials

  home_page.add_back_pack()
  home_page.goCart()
  cart_page.press_checkout()

  checkOut_page.checkoutOne(userName, userName, zipCode)


  # Then the home page gets load

  assert 'Swag Labs' == browser.title
  #assert 'Products'  == home_page.title_value()
  #assert 'Products'  == home_page.title_value()