from cases.base_cases import Test
from pages.event_page import EventPage
from pages.main.events_page import EventsPage
from steps.main.events_steps import EventsSteps


class EventsTest(Test):
    def setUp(self):
        super().setUp()
        self.page = EventsPage(self.driver)
        self.steps = EventsSteps(self.driver)

    def test_card_redirect_click_picture(self):
        title_text = self.steps.get_first_card_title_and_redirect_to_event_by_pic()

        event_page = EventPage(self.driver)
        page_title_text = event_page.get_title()

        self.assertEqual(title_text, page_title_text)

    def test_card_redirect_click_card(self):
        title_text = self.steps.get_first_card_title_and_redirect_to_event_by_card()

        event_page = EventPage(self.driver)
        page_title_text = event_page.get_title()

        self.assertEqual(title_text, page_title_text)




