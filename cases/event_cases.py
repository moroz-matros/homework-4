import time

from cases.base_cases import Test
from pages.event_page import EventPage
from pages.main.events_page import EventsPage
from pages.profile.events_page import ProfileEventsPage

GO_TEXT = 'Уже иду!'


class EventTest(Test):
    def setUp(self):
        super().setUp()
        self.page = EventPage(self.driver)
        main_page = EventsPage(self.driver)
        main_page.open()
        first_event = main_page.get_first_card_pic()
        self.page.BASE_URL = self.page.BASE_URL + first_event.get_attribute("id")
        print(first_event.get_attribute("id"))
        self.login()


'''
    def test_event_like_ok(self):
        # Лайк события добавляет мероприятие в избранное.

        self.page.open()
        event_title = self.page.get_title()
        self.page.click_star()
        self.page.open()
        time.sleep(5)
        status = self.page.get_status_text()
        profile = ProfileEventsPage(self.driver)
        profile.open()
        time.sleep(5)
        title = profile.get_first_event_title()

        self.assertEqual(GO_TEXT, status)
        self.assertEqual(title, event_title)

        # tear down
        self.page.open()
        self.page.click_star()
'''
