from .base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert '/login/' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def is_element_present(self, how, what):
         try:
            self.browser.find_element(how, what)
         except NoSuchElementException:
            return False
         return True