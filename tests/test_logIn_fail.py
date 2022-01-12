
import pytest
from selenium.webdriver.common.by import By

from pages.home import SwagLabsHomePage
from pages.logIn import SwagLabsLogInPage


#----------------------Fail to log in---------------------------------------------------------------#
@pytest.mark.parametrize('userName', ['Francisco'])
@pytest.mark.parametrize('password', ['secret_sauce','abcd123'])
def test_logIn_Fail(browser, userName,password):

  logIn_page = SwagLabsLogInPage(browser)

  # Given the log in page of swag
  logIn_page.load()

  # When the user type incorrect credentials
  logIn_page.logIn(userName, password)

  # Then a error messeges appears
  assert logIn_page.errorMs() == "Epic sadface: Username and password do not match any user in this service"


