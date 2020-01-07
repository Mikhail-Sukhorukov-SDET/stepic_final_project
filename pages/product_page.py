from .base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_catalogue_url()
        self.should_be_add_product_to_basket_button()
        self.should_be_product_price()
        self.should_be_product_name()

    def adding_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TO_BASKET_BUTTON).click()

    def product_data_get_text(self):
        product_data = {
            "price": self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text,
            "name": self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_TEXT).text
        }
        return product_data

    def after_adding_messages_data_get_text(self):
        after_adding_messages = {
            "basket_price": self.browser.find_element(*ProductPageLocators.AFTER_ADDING_BASKET_PRICE_TEXT).text,
            "name": self.browser.find_element(*ProductPageLocators.AFTER_ADDING_PRODUCT_NAME_TEXT).text
        }
        return after_adding_messages

    def should_be_catalogue_url(self):
        assert '/catalogue/' in self.browser.current_url

    def should_be_add_product_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_PRODUCT_TO_BASKET_BUTTON), "Add product to basket button is not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_OF_PRODUCT), "Price of product text is not presented"

    def should_be_product_name(self):
        assert self.is_element_present(
            *ProductPageLocators.NAME_OF_PRODUCT_TEXT), "Name of product text is not presented"

    def should_be_valid_after_adding_product_data(self):
        after_adding_messages = self.after_adding_messages_data_get_text()
        product_data = self.product_data_get_text()
        assert after_adding_messages["basket_price"] == product_data[
            "price"], "Price of basket should be equal price of added product"
        assert after_adding_messages["name"] == product_data[
            "name"], "Name of product in after adding message should be equal name of added product"
