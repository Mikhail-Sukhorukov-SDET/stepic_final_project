import pytest

from config import BASE_LINK
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    @pytest.mark.xfail(reason="Main page contain different login link #registration_link from other pages #login_link")
    def test_guest_can_go_to_login_page(self, browser):
        link = f"{BASE_LINK}/catalogue/the-shellcoders-handbook_209?promo=midsummer"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.should_be_login_page()

    @pytest.mark.xfail(reason="Main page contain different login link #registration_link from other pages #login_link")
    def test_guest_should_see_login_link(self, browser):
        link = f"{BASE_LINK}/catalogue/the-shellcoders-handbook_209?promo=midsummer"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = f"{BASE_LINK}/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_basket_link()
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_basket_page()
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_basket_is_empty_message()
