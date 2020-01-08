from .base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    EMPTY_BASKET_MESSAGE = "Your basket is empty. Continue shopping"

    def should_be_basket_page(self):
        self.should_be_basket_header()
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert '/basket/' in self.browser.current_url

    def should_be_basket_header(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HEADER_TEXT), "Header should be presented"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Product in basket is presented, but should not be"

    def should_be_basket_is_empty_message(self):
        assert BasketPage.EMPTY_BASKET_MESSAGE == self.browser.find_element(
            *BasketPageLocators.BASKET_IS_EMPTY_TEXT).text, "Should be valid 'Basket is empty' message"
