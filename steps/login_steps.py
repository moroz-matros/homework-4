from pages.login_page import LoginPage
from steps.base_steps import *


class LoginSteps(BaseSteps):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.page = LoginPage(self.driver)

    def login(self, login, password):
        self.page.open()
        self.page.fill_form(login, password)
        self.page.click_login_button()

    def redirect_to_registration(self):
        self.page.open()
        self.page.click_redirect()
