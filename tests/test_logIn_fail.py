"""
These tests cover SwagLabs log in with wrong credentials.
"""
import pytest

from pages.home import SwagLabsHomePage
from pages.logIn import SwagLabsLogInPage


#----------------------Fail to log in---------------------------------------------------------------#
@pytest.mark.parametrize('userName', ['locked_out_user'])
@pytest.mark.parametrize('password', ['secret_sauce','abcd123'])
def test_logIn_Fail(browser, userName,password):

  logIn_page = SwagLabsLogInPage(browser)

  # Given the log in page of swag
  logIn_page.load()

  # When the user type incorrect credentials
  logIn_page.logIn(userName, password)

  # Then a error messeges appears
  logIn_page.errorMs()

