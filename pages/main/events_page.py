from pages.base_page import Page


class EventsPage(Page):
    BASE_URL = 'https://qdaqda.ru/events'
    PATH = ''

    CARD_CLASS = '.events-block'
    CARD_TITLE = '.events-block__title'
    CARD_PIC = '.events-block__photo'

    def get_first_card_title(self):
        card = self.wait_until_and_get_elem_by_css(self.CARD_TITLE)
        return card.text

    def redirect_to_first_card_by_pic(self):
        pic = self.wait_until_and_get_elem_by_css(self.CARD_PIC)
        pic.click()

    def redirect_to_first_card_by_card(self):
        card = self.wait_until_and_get_elem_by_css(self.CARD_CLASS)
        card.click()



