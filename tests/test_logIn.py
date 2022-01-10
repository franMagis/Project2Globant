"""
These tests cover SwagLabs log in.
"""
import pytest

from pages.home import SwagLabsHomePage
from pages.result import swagLabsResultPage
from pages.logIn import SwagLabsLogInPage


#----------------------log in---------------------------------------------------------------#
@pytest.mark.parametrize('userName', ['standard_user', 'problem_user','performance_glitch_user'])
@pytest.mark.parametrize('password', ['secret_sauce'])
def test_logIn(browser, userName, password):

  logIn_page = SwagLabsLogInPage(browser)
  result_page = swagLabsResultPage(browser)
  home_page = SwagLabsHomePage(browser)

  # Given the log in page of swag
  logIn_page.load()

  # When the user type correct credentials
  logIn_page.logIn(userName,password)


  # Then the home page gets load

  home_page.load()
  assert 'Swag Labs' == browser.title
  #assert 'Products'  == home_page.title_value()

#----------------------Fail to log in---------------------------------------------------------------#
@pytest.mark.parametrize('userName', ['locked_out_user'])
@pytest.mark.parametrize('password', ['secret_sauce','abcd123'])
def test_logIn_Fail(browser, userName,password):

  logIn_page = SwagLabsLogInPage(browser)

  # Given the log in page of swag
  logIn_page.load()

  # When the user type correct credentials
  logIn_page.logIn(userName, password)

  # Then a error messeges appears

  logIn_page.errorMs()


#esto puede ser innecesario
  # And the search result links pertain to the phrase
  #for title in result_page.result_link_titles():
  #  assert phrase.lower() in title.lower()

  # And the search result title contains the phrase
  # (Putting this assertion last guarantees that the page title will be ready)
 # assert phrase in result_page.title()