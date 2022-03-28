import pytest

from config import BASE_LINK
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


@pytest.mark.need_review
@pytest.mark.parametrize('offer_number', list(range(10)))
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f"{BASE_LINK}/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.adding_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_valid_after_adding_product_data()


@pytest.mark.xfail(reason=" After adding product to basket - 'After adding' messages should be on page ")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"{BASE_LINK}/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.adding_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_after_adding_messages()


def test_guest_cant_see_success_message(browser):
    link = f"{BASE_LINK}/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.should_not_be_after_adding_messages()


@pytest.mark.xfail(
    reason=" After adding product to basket - 'After adding' messages should not be disappeared from page ")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"{BASE_LINK}/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.adding_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_disappear_after_adding_messages()


def test_guest_should_see_login_link_on_product_page(browser):
    link = f"{BASE_LINK}/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = f"{BASE_LINK}/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = f"{BASE_LINK}/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_basket_link()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_basket_page()
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_basket_is_empty_message()


@pytest.mark.user_add_to_busket_from_product_page
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = f"{BASE_LINK}/en-gb/accounts/login/"
        registration_page = LoginPage(browser, link)
        registration_page.open()
        registration_page.should_be_login_page()
        registration_page.register_new_user()
        registration_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = f"{BASE_LINK}/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_product_page()
        product_page.should_not_be_after_adding_messages()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"{BASE_LINK}/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_product_page()
        product_page.adding_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_valid_after_adding_product_data()
