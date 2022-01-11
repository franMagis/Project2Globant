"""
These tests cover SwagLabs log in.
"""
import pytest

from pages.cart import SwagLabsCartPage
from pages.home import SwagLabsHomePage
from pages.logIn import SwagLabsLogInPage
from pages.checkoutOne import SwagLabsCheckoutPageOne


# ----------------------Cart test---------------------------------------------------------------#
@pytest.mark.parametrize('userName', ['standard_user', 'problem_user', 'performance_glitch_user'])
@pytest.mark.parametrize('password', ['secret_sauce'])
# @pytest.mark.parametrize('name', ['Francisco'])
# @pytest.mark.parametrize('lastName', ['Magis'])
@pytest.mark.parametrize('zipCode', ['11300'])
def test_add_product(browser, userName, password, zipCode):

    logIn_page = SwagLabsLogInPage(browser)
    home_page = SwagLabsHomePage(browser)
    cart_page = SwagLabsCartPage(browser)
    checkOut_page = SwagLabsCheckoutPageOne(browser)
    logIn_page.load()
    logIn_page.logIn(userName, password)

    # Given the home page of swag
    home_page.load()

    # When the user adds a product
    home_page.add_back_pack()


    #Then the product appear in the shopping cart
    assert home_page.cart_span() == home_page.span_cart