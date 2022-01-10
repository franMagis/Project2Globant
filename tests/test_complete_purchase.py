"""
These tests cover SwagLabs log in.
"""
import pytest

from pages.home import SwagLabsHomePage
from pages.result import swagLabsResultPage
from pages.logIn import SwagLabsLogInPage
from pages.logIn import SwagLabsCart


#----------------------log in---------------------------------------------------------------#
@pytest.mark.parametrize('userName', ['standard_user', 'problem_user','performance_glitch_user'])
@pytest.mark.parametrize('password', ['secret_sauce'])
def complete_purchase_out(browser, userName, password):

  logIn_page = SwagLabsLogInPage(browser)
  result_page = swagLabsResultPage(browser)
  home_page = SwagLabsHomePage(browser)
  cart_page = SwagLabsCart(browser)

  logIn_page.load()
  logIn_page.logIn(userName, password)



  # Given the log in page of swag
  home_page.load()
  # When the user type correct credentials

  home_page.add_back_pack()



  # Then the home page gets load

  assert 'Swag Labs' == browser.title
  #assert 'Products'  == home_page.title_value()
  #assert 'Products'  == home_page.title_value()