import pytest
from playwright.sync_api import expect

from pages.logout_page import LogoutPage
from test_data.excel_reader import get_all_login_data
from pages.home_page import HomePage
from pages.login_page import LoginPage

# Login into web
@pytest.mark.sanity
@pytest.mark.parametrize("username,password", get_all_login_data())
def test_login(page, username, password):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(username, password)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

# add to cart first product
def test_home(page):
    test_login(page)
    home_page = HomePage(page)

    home_page.filter()
    home_page.option()
    home_page.jacket()

    #expect(page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]")).to_be_visible()

def test_logout(page):
    test_login(page)
    logout_page = LogoutPage(page)

    # logout
    logout_page.logout()