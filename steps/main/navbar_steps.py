from pages.login_page import LoginPage
from pages.main.navbar_page import NavbarPage
from steps.base_steps import *


class NavbarSteps(BaseSteps):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.page = NavbarPage(self.driver)

    def get_login(self):
        return self.page.get_login()
