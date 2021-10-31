from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class NavbarPage(Page):
    BASE_URL = 'https://qdaqda.ru'
    PATH = ''

    LOGIN_TEXT = ".navbar-profile-name"

    def get_login(self):
        login_text = self.wait_until_and_get_elem_by_css(self.LOGIN_TEXT)
        return login_text.text

