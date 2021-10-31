from pages.registration_page import RegistrationPage
from steps.base_steps import *


class RegistrationSteps(BaseSteps):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.page = RegistrationPage(self.driver)

    def register(self, login, password, name):
        self.page.open()
        self.page.fill_form(login, password, name)
        self.page.click_registration_button()

    def redirect_to_login(self):
        self.page.open()
        self.page.click_redirect()
