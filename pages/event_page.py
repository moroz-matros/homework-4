from pages.base_page import Page


class EventPage(Page):
    BASE_URL = 'https://qdaqda.ru/event'
    PATH = ''

    TITLE = '.event-description__title'

    def get_title(self):
        title = self.wait_until_and_get_elem_by_css(self.TITLE)
        return title.text


