import time
import quopri
from urllib.parse import unquote

from cases.base_cases import Test
from pages.event_page import EventPage
from pages.main.events_page import EventsPage
from pages.profile.events_page import ProfileEventsPage
from pages.search_page import SearchPage

GO_TEXT = 'Уже иду!'
NOT_GO_TEXT = 'Пойти на мероприятие'


class EventTest(Test):
    def setUp(self):
        super().setUp()
        self.page = EventPage(self.driver)
        main_page = EventsPage(self.driver)
        main_page.open()
        first_event = main_page.get_first_card_pic()
        self.page.BASE_URL = self.page.BASE_URL + first_event.get_attribute("id")
        self.login()

    def test_event_like_dislike_ok(self):
        # Лайк события добавляет мероприятие в избранное.
        # Повторный лайк убирает мероприятие из избранного.

        self.page.open()
        self.page.click_star()
        # Обновление страницы
        self.page.refresh()
        status_ok = self.page.get_status_text()

        self.page.click_star()
        self.page.refresh()
        status_not_ok = self.page.get_status_text()

        self.assertEqual(GO_TEXT, status_ok)
        self.assertEqual(NOT_GO_TEXT, status_not_ok)

    def test_event_redirect_tag_ok(self):
        # Нажатие на теги приводит к поиску по тегу.

        self.page.open()
        tag = self.page.get_first_tag_text()
        self.page.redirect_first_tag_search()

        search_page = SearchPage(self.driver)
        search_page.wait_for_page(search_page.CONTAINER)

        redirect_url = self.driver.current_url
        redirect_url = unquote(redirect_url)

        self.assertIn(tag, redirect_url)

    def test_event_share_ok(self):
        # Клик по кнопке “поделиться” открывает окно шаринга, в котором есть кнопки “поделиться в vk” и “скопировать”

        self.page.open()
        self.page.click_share()
        self.assertTrue(self.page.get_vk_button().is_displayed())
        self.assertTrue(self.page.get_copy_button().is_displayed())

    def test_event_invite_ok(self):
        # Клик кнопке “пригласить” открывает список друзей для выбора.

        self.page.open()
        self.page.click_invite()
        self.assertTrue(self.page.get_friends_list().is_displayed())










