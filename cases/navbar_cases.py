from cases.base_cases import Test
from pages.activity_page import ActivityPage
from pages.chat_page import ChatPage
from pages.login_page import LoginPage
from pages.navbar_page import NavbarPage
from pages.profile_page import ProfilePage

URL = 'https://qdaqda.ru/'
URL_EVENTS = 'https://qdaqda.ru/events'
NO_NOTIFICATIONS = 'Пока ничего нет'

PROFILE = 'profile'
ACTIVITY = 'activity'
CHAT = 'chat'
RECOMMEND = 'jsRecommendButton'


class NavbarTest(Test):
    def setUp(self):
        super().setUp()
        self.page = NavbarPage(self.driver)
        self.login()
        self.page.open()

    def test_navbar_redirect_logo(self):
        # Нажатие на логотип возвращает на главную страницу.

        some_page = LoginPage(self.driver)
        some_page.open()
        self.page.click_logo()

        flag = (URL == self.driver.current_url) or (URL_EVENTS == self.driver.current_url)

        self.assertTrue(flag)

    def test_navbar_no_notifications(self):
        # При отсутствии уведомлений при нажатии на кнопку появляется окно с сообщением “Пока ничего нет”

        self.page.click_bell()
        text = self.page.get_no_notifications_text()

        self.assertEqual(NO_NOTIFICATIONS, text)

    def test_navbar_redirect_profile(self):
        # При клике переводит на страницу своего профиля

        self.page.open_menu()
        self.page.click_profile()
        profile = ProfilePage(self.driver)
        profile.wait_for_page(profile.CONTAINER)

        url = self.driver.current_url

        self.assertIn(PROFILE, url)

    def test_navbar_redirect_activity(self):
        # При клике переводит на страницу ленты активности

        self.page.open_menu()
        self.page.click_activity()
        activity = ActivityPage(self.driver)
        activity.wait_for_page(activity.CONTAINER)

        url = self.driver.current_url

        self.assertIn(ACTIVITY, url)

    def test_navbar_redirect_chat(self):
        # При клике переводит на страницу чата

        self.page.open_menu()
        self.page.click_chat()
        chat = ChatPage(self.driver)
        chat.wait_for_page(chat.CONTAINER)

        url = self.driver.current_url

        self.assertIn(CHAT, url)

    def test_navbar_logout(self):
        # Логаут у авторизованного пользователя производится корректно (меняется шапка).

        self.page.open_menu()
        self.page.wait_for_page(self.page.CONTAINER_MENU)
        self.page.click_logout()
        self.page.wait_for_page(self.page.CONTAINER)
        self.page.get_registration_logo()

        self.assertTrue(self.page.get_registration_logo().is_displayed())
