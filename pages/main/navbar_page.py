from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class NavbarPage(Page):
    BASE_URL = 'https://qdaqda.ru'
    PATH = ''

    LOGIN_TEXT = ".navbar-profile-name"
    LOGO = '.logo'
    BELL = '#JSNavbarBell'
    NO_NOTIFICATION_TITLE = '.notification-empty__title'

    PROFILE = '.dropdown-menu__profile'
    ACTIVITY = '.dropdown-menu__activity'
    CHAT = '.dropdown-menu__chat'
    LOGOUT = '.dropdown-menu__logout'

    DROP_DOWN_MENU = '#jsProfileNav'

    REGISTRATION = '.navbar-menu__signup'

    def get_login(self):
        login_text = self.wait_until_and_get_elem_by_css(self.LOGIN_TEXT)
        return login_text.text

    def click_logo(self):
        logo = self.wait_until_and_get_elem_by_css(self.LOGO)
        logo.click()

    def click_bell(self):
        bell = self.wait_until_and_get_elem_by_css(self.BELL)
        bell.click()

    def get_no_notifications_text(self):
        title = self.wait_until_and_get_elem_by_css(self.NO_NOTIFICATION_TITLE)
        return title.text

    def click_profile(self):
        profile = self.wait_until_and_get_elem_by_css(self.PROFILE)
        profile.click()

    def click_activity(self):
        activity = self.wait_until_and_get_elem_by_css(self.ACTIVITY)
        activity.click()

    def click_chat(self):
        chat = self.wait_until_and_get_elem_by_css(self.CHAT)
        chat.click()

    def click_logout(self):
        logout = self.wait_until_and_get_elem_by_css(self.LOGOUT)
        logout.click()

    def open_menu(self):
        menu = self.wait_until_and_get_elem_by_css(self.DROP_DOWN_MENU)
        menu.click()

    def get_registration_logo(self):
        logo = self.wait_until_and_get_elem_by_css(self.REGISTRATION)
        return logo






