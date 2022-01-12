
import pytest

from pages.home import SwagLabsHomePage
from pages.logIn import SwagLabsLogInPage


#---------------------- Order list of price ---------------------------------------------------------------#
@pytest.mark.parametrize('userName', ['standard_user','performance_glitch_user'])
@pytest.mark.parametrize('password', ['secret_sauce'])
def test_order_prices(browser, userName, password):

  logIn_page = SwagLabsLogInPage(browser)
  home_page = SwagLabsHomePage(browser)


  # Given the home page of swag
  logIn_page.load()
  logIn_page.logIn(userName, password)

  # When the user order the prices
  home_page.order_prices()

  #The assert is done in the order_prices method