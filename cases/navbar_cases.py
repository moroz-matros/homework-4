from cases.base_cases import Test
from pages.activity_page import ActivityPage
from pages.chat_page import ChatPage
from pages.event_page import EventPage
from pages.login_page import LoginPage
from pages.main.events_page import EventsPage
from pages.main.navbar_page import NavbarPage
from pages.profile_page import ProfilePage

URL = 'https://qdaqda.ru/'
NO_NOTIFICATIONS = 'Пока ничего нет'

PROFILE = 'profile'
ACTIVITY = 'activity'
CHAT = 'chat'
RECOMMEND = 'jsRecommendButton'


class NavbarTest(Test):
    def setUp(self):
        super().setUp()
        self.page = NavbarPage(self.driver)

    def test_navbar_redirect_logo(self):
        # Клик по любому месту на карточке события открывает страницу эвента.

        some_page = LoginPage(self.driver)
        some_page.open()
        self.page.click_logo()

        self.assertEqual(URL, self.driver.current_url)

    def test_navbar_no_notifications(self):
        # Клик по любому месту на карточке события открывает страницу эвента.

        self.login()
        self.page.open()
        self.page.click_bell()
        text = self.page.get_no_notifications_text()

        self.assertEqual(NO_NOTIFICATIONS, text)

    def test_navbar_redirect_profile(self):
        # При клике переводит на страницу своего профиля

        self.login()
        self.page.open()
        self.page.open_menu()
        self.page.click_profile()
        profile = ProfilePage(self.driver)
        profile.wait_for_page(profile.CONTAINER)

        url = self.driver.current_url

        self.assertIn(PROFILE, url)

    def test_navbar_redirect_activity(self):
        # При клике переводит на страницу ленты активности

        self.login()
        self.page.open()
        self.page.open_menu()
        self.page.click_activity()
        activity = ActivityPage(self.driver)
        activity.wait_for_page(activity.CONTAINER)

        url = self.driver.current_url

        self.assertIn(ACTIVITY, url)

    def test_navbar_redirect_chat(self):
        # При клике переводит на страницу чата

        self.login()
        self.page.open()
        self.page.open_menu()
        self.page.click_chat()
        chat = ChatPage(self.driver)
        chat.wait_for_page(chat.CONTAINER)

        url = self.driver.current_url

        self.assertIn(CHAT, url)

    def test_navbar_logout(self):
        # При клике переводит на страницу чата

        self.login()
        self.page.open()
        self.page.open_menu()
        self.page.click_logout()

        self.assertTrue(self.page.get_registration_logo().is_displayed())
