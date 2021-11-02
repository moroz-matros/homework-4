from pages.base_page import Page


class EventPage(Page):
    BASE_URL = 'https://qdaqda.ru/event'
    PATH = ''

    TITLE = '.event-description__title'

    STAR = '#jsEventStar'
    STATUS_TEXT = '#jsGoingText'


    def get_title(self):
        title = self.wait_until_and_get_elem_by_css(self.TITLE)
        return title.text

    def click_star(self):
        star = self.wait_until_and_get_elem_by_css(self.STAR)
        star.click()

    def get_status_text(self):
        text = self.wait_until_and_get_elem_by_css(self.STATUS_TEXT)
        return text


