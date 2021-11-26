from selenium.common.exceptions import StaleElementReferenceException

from pages.base_page import Page


class SearchPage(Page):
    BASE_URL = 'https://qdaqda.ru/search'
    PATH = ''

    CONTAINER = '.search-main-block'

    SEARCH_INPUT = "#searchInput"
    SEARCH_BUTTON = '#jsSearchRequest'
    EXHIBITION_TAB = '#exhibitionButton'
    CONCERT_TAB = '#concertButton'
    ACTIVE_TAB = '.button-active'
    USERS_TAB = '#usersTab'

    USER_NAME = '.one-user-block__title'

    PAGE_NEXT_BUTTON = '#paginationForward'
    PAGE_NUM = '#paginationCurrentCircle'

    USER = '.one-user-block'

    EVENT_TITLE = '.smbs-event__title'
    NOTHING = 'h6'

    BACK_BUTTON = '.search-main-block__back-button'

    def search(self, text):
        str = self.wait_visibility_until_and_get_elem_by_css(self.SEARCH_INPUT)
        button = self.wait_visibility_until_and_get_elem_by_css(self.SEARCH_BUTTON)
        str.send_keys(text)
        button.click()

    def get_text_no_found(self):
        text = self.wait_visibility_until_and_get_elem_by_css(self.NOTHING)
        return text.text

    def redirect_to_tab(self, tab_name):
        try:
            tab = self.wait_visibility_until_and_get_elem_by_css(tab_name)
            tab.click()
        except StaleElementReferenceException:
            tab = self.wait_visibility_until_and_get_elem_by_css(tab_name)
            tab.click()

    def get_first_event_title(self):
        title = self.wait_visibility_until_and_get_elem_by_css(self.EVENT_TITLE)
        return title.text

    def get_active_tab_title(self):
        tab = self.wait_visibility_until_and_get_elem_by_css(self.ACTIVE_TAB)
        return tab.text

    def redirect_next_page(self):
        button = self.wait_visibility_until_and_get_elem_by_css(self.PAGE_NEXT_BUTTON)
        button.click()

    def get_page_num(self):
        num = self.wait_visibility_until_and_get_elem_by_css(self.PAGE_NUM)
        return num.text

    def redirect_to_users(self):
        tab = self.wait_visibility_until_and_get_elem_by_css(self.USERS_TAB)
        tab.click()

    def redirect_to_first_user(self):
        link = self.wait_visibility_until_and_get_elem_by_css(self.USER_NAME)
        link.click()

    def get_first_user_name(self):
        name = self.wait_visibility_until_and_get_elem_by_css(self.USER_NAME)
        return name.text

    def get_first_user(self):
        user = self.wait_visibility_until_and_get_elem_by_css(self.USER)
        return user

    def redirect_to_main(self):
        button = self.wait_visibility_until_and_get_elem_by_css(self.BACK_BUTTON)
        button.click()





