from pages.base_page import Page


class OtherProfilePage(Page):
    BASE_URL = 'https://qdaqda.ru/profile'
    CONTAINER = '.page-photo_profile'

    USER_NAME = '.profile-header__title'

    SUBSCRIBE_BUTTON = '#subscribeUserButton'
    WRITE_BUTTON = '#messageButton'

    def get_user_name(self):
        name = self.wait_until_and_get_elem_by_css(self.USER_NAME)
        return name.text

    def open_other_profile(self, n):
        self.open(self.BASE_URL + str(n))

    def click_subscribe(self):
        button = self.wait_until_and_get_elem_by_css(self.SUBSCRIBE_BUTTON)
        button.click()

    def get_subscribe_button_text(self):
        button = self.wait_until_and_get_elem_by_css(self.SUBSCRIBE_BUTTON)
        return button.text

    def get_subscribe_button(self):
        button = self.wait_presence_until_and_get_elem_by_css(self.SUBSCRIBE_BUTTON)
        return button

    def click_write_message(self):
        button = self.wait_until_and_get_elem_by_css(self.WRITE_BUTTON)
        button.click()

    def get_write_message_button(self):
        button = self.wait_presence_until_and_get_elem_by_css(self.WRITE_BUTTON)
        return button


