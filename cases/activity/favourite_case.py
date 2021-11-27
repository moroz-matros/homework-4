import time

from cases.base_cases import Test
from pages.activity_page import ActivityPage
from pages.event_page import EventPage
from pages.events_page import EventsPage
from pages.other_profile_page import OtherProfilePage


class ActivityFavouriteTest(Test):
    def setUp(self):
        super().setUp()
        self.page = ActivityPage(self.driver)
        self.login()
        self.other_profile_page = OtherProfilePage(self.driver)
        self.other_profile_page.open_other_profile(self.ID2)

        self.other_profile_page.click_subscribe()
        self.logout()

        self.events_page = EventsPage(self.driver)
        self.event_page = EventPage(self.driver)

        self.login2()
        self.events_page.open()
        event = self.events_page.get_first_card_pic()
        event.click()
        self.event_title = self.event_page.get_title()
        self.event_page.click_star()
        self.logout()

    def tearDown(self):
        self.page.open()
        self.login2()
        self.events_page.open()
        event = self.events_page.get_first_card_pic()
        event.click()
        self.event_page.click_star()
        self.logout()
        self.login()
        self.other_profile_page.open_other_profile(self.ID2)

        self.other_profile_page.click_subscribe()
        super().tearDown()

    def test_activity_has_fav(self):
        # Имеются сообщения о добавлении мероприятия в избранное у тех, на кого подписан пользователь.
        # Переход на страницу события при нажатии на его название.

        self.login()
        self.page.open()
        self.page.refresh()
        block = self.page.get_activity_block()
        flag = block.is_displayed()
        self.page.click_event()
        event_title_redirect = self.event_page.get_title()
        self.logout()

        self.assertEqual(True, flag)
        self.assertEqual(self.event_title, event_title_redirect)

    ''' <BUG>
    def test_activity_not_available_unauthorized(self):
        # Недоступна для неавторизованного пользователя.
    '''
