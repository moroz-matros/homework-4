import time

from selenium.common.exceptions import StaleElementReferenceException

from cases.base_cases import Test
from pages.chat_page import ChatPage
from pages.events_page import EventsPage
from pages.other_profile_page import OtherProfilePage

polling_time = 3


class ChatTest(Test):
    def setUp(self):
        super().setUp()
        self.login()
        self.page = ChatPage(self.driver)
        self.other_profile = OtherProfilePage(self.driver)
        self.other_profile.open_other_profile(self.ID2)
        self.page.refresh()

    def test_chat_non_read_messages(self):
        # Непрочитанные сообщения выделяются цветом.

        self.other_profile.click_write_message()
        self.page.write_message("str")
        self.page.click_send_button()
        self.page.refresh()
        style1 = self.page.get_left_card_color()
        self.logout()

        self.login2()
        self.other_profile.open_other_profile(self.ID)
        self.other_profile.click_write_message()
        self.page.refresh()
        style2 = self.page.get_left_card_color()
        self.assertNotEqual(style2, style1)

    def test_chat_empty_message(self):
        # Невозможно отправить пустое сообщение.

        self.other_profile.click_write_message()
        self.page.write_message('hello')
        self.page.click_send_button()
        self.page.refresh()
        self.page.click_send_button()
        self.page.refresh()

        text = self.page.get_last_message_text()
        self.assertNotEqual('', text)

    def test_chat_link_redirect(self):
        # Проверить, что ссылки в сообщении кликабельные и переводят на соответствующие страницы.

        self.other_profile.click_write_message()
        link = "https://qdaqda.ru/"
        self.page.write_message(link)
        self.page.click_send_button()
        self.page.click_link(link)

        main = EventsPage(self.driver)
        main.wait_for_page(main.CONTAINER)

        self.assertEqual(link, self.driver.current_url)

    ''' <BUG>
    def test_chat_max_message_length(self):
        # Ошибка при отправлении слишком большого текста (>4к символов).
    '''
















