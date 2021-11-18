from pages.base_page import Page


class ProfilePage(Page):
    BASE_URL = 'https://qdaqda.ru/profile'
    PATH = ''

    TITLE_CLASS = '.smbs-event__title'
    SUBSCRIBER = ':first-of-type.my-profile-header__followers-block'
    SUBSCRIBED_TO = ':last-of-type.my-profile-header__followers-block'
    USER_NAME = '.profile-header__title'

    CONTAINER = '.page-photo_profile'
    SUBSCRIBE_BUTTON = '#subscribeUserButton'

    def get_first_event_title(self):
        title = self.wait_until_and_get_elem_by_css(self.TITLE_CLASS)
        return title.text

    def get_user_name(self):
        name = self.wait_until_and_get_elem_by_css(self.USER_NAME)
        return name.text

    def redirect_to_subscribers(self):
        button = self.wait_until_and_get_elem_by_css(self.SUBSCRIBER)
        button.click()

    def redirect_to_subscribed_to(self):
        button = self.wait_until_and_get_elem_by_css(self.SUBSCRIBED_TO)
        button.click()
