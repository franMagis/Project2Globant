
import pytest

from pages.cart import SwagLabsCartPage
from pages.home import SwagLabsHomePage
from pages.logIn import SwagLabsLogInPage
from pages.checkoutOne import SwagLabsCheckoutPageOne


# ----------------------Add one back pack---------------------------------------------------------------#
@pytest.mark.parametrize('userName', ['standard_user', 'problem_user', 'performance_glitch_user'])
@pytest.mark.parametrize('password', ['secret_sauce'])
def test_add_product(browser, userName, password):

    logIn_page = SwagLabsLogInPage(browser)
    home_page = SwagLabsHomePage(browser)

    # Given the home page of swag
    logIn_page.load()
    logIn_page.logIn(userName, password)

    # When the user adds a product
    home_page.add_back_pack()

    #Then the product appear in the shopping cart
    assert home_page.cart_span() == home_page.span_cart