from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class NavbarPage(Page):
    BASE_URL = 'https://qdaqda.ru'
    PATH = ''

    NAME_TEXT = ".navbar-profile-name"

    def get_name(self):
        name_text = self.wait_visibility_until_and_get_elem_by_css(self.NAME_TEXT)
        return name_text.text

