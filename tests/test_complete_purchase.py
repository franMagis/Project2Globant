import pytest

from pages.cart import SwagLabsCartPage
from pages.home import SwagLabsHomePage
from pages.logIn import SwagLabsLogInPage
from pages.checkoutOne import SwagLabsCheckoutPageOne
from pages.checkoutTwo import SwagLabsCheckoutPageTwo
from pages.checkoutThree import SwagLabsCheckoutPageThree


# ----------------------Complete purchase---------------------------------------------------------------#
@pytest.mark.parametrize('userName', ['standard_user', 'performance_glitch_user'])
@pytest.mark.parametrize('password', ['secret_sauce'])
@pytest.mark.parametrize('name', ['Francisco'])
@pytest.mark.parametrize('lastName', ['Magis'])
@pytest.mark.parametrize('zipCode', ['11300'])
def test_complete_purchase_out(browser, userName, password, zipCode, name, lastName):
    logIn_page = SwagLabsLogInPage(browser)
    home_page = SwagLabsHomePage(browser)
    cart_page = SwagLabsCartPage(browser)
    checkOut_page = SwagLabsCheckoutPageOne(browser)
    checkOut_page_Two = SwagLabsCheckoutPageTwo(browser)
    checkOut_page_Three = SwagLabsCheckoutPageThree(browser)

    # Given the home page of swag
    logIn_page.load()
    logIn_page.logIn(userName, password)

    # When the user adds a product
    home_page.add_back_pack()

    # Then the user moves to the cart page
    home_page.goCart()

    # Then the user moves to checkout page
    cart_page.press_checkout()

    assert browser.current_url == 'https://www.saucedemo.com/checkout-step-one.html'
    checkOut_page.checkoutOne(name, lastName, zipCode)

    checkOut_page_Two.finish()
