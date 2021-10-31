from pages.main.events_page import EventsPage
from steps.base_steps import *


class EventsSteps(BaseSteps):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.page = EventsPage(self.driver)

    def get_first_card_title_and_redirect_to_event_by_pic(self):
        self.page.open()
        title_text = self.page.get_first_card_title()
        self.page.redirect_to_first_card_by_pic()
        return title_text

    def get_first_card_title_and_redirect_to_event_by_card(self):
        self.page.open()
        title_text = self.page.get_first_card_title()
        self.page.redirect_to_first_card_by_card()
        return title_text

