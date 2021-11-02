from pages.base_page import Page


class ProfileEventsPage(Page):
    BASE_URL = 'https://qdaqda.ru/profile?tab=eventsTab'
    PATH = ''

    TITLE_CLASS = '.smbs-event__title'

    def get_first_event_title(self):
        title = self.wait_until_and_get_elem_by_css(self.TITLE_CLASS)
        return title.text


