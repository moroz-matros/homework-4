import time

from cases.base_cases import Test
from pages.event_page import EventPage
from pages.events_page import EventsPage
from pages.profile_page import ProfilePage


class ProfileEventCardTest(Test):
    def setUp(self):
        super().setUp()
        self.page = ProfilePage(self.driver)
        self.page.BASE_URL = 'https://qdaqda.ru/profile?tab=eventsTab'
        self.login()
        self.events_page = EventsPage(self.driver)
        self.event_page = EventPage(self.driver)

        self.events_page.open()
        self.events_page.redirect_to_first_card_by_card()
        self.event_page.click_star()
        self.description = self.event_page.get_description()
        self.title = self.event_page.get_title()
        self.page.open()

    def tearDown(self):
        self.events_page.open()
        self.events_page.redirect_to_first_card_by_card()
        self.event_page.click_star()
        super().tearDown()

    def test_profile_events_card_change(self):
        # При нажатии на стрелку на карточке показывается описание события. При повторном нажатии на стрелку на карточке в описании возвращается исходный вид.

        time.sleep(1)
        self.page.click_arrow_down()
        self.page.wait_for_page(self.page.CONTAINER_DESCRIPTION)
        text = self.page.get_event_description()
        self.page.click_arrow_up()
        t = self.page.get_event_title()

        self.assertEqual(self.title, t)
        self.assertEqual(self.description, text)

    def test_profile_events_card_share(self):
        # При нажатии на кнопку шаринга появляется окно со ссылкой, где есть кнопка “скопировать” и “поделиться в вк”.

        time.sleep(1)
        self.page.click_arrow_down()
        self.page.click_share_button()
        is_vk = self.page.get_vk_button().is_displayed()
        is_copy = self.page.get_copy_button().is_displayed()

        self.assertEqual(True, is_vk)
        self.assertEqual(True, is_copy)
