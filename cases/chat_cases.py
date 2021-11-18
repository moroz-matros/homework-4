import time

from cases.base_cases import Test
from pages.chat_page import ChatPage
from pages.event_page import EventPage
from pages.main.events_page import EventsPage
from pages.other_profile_page import OtherProfilePage
from pages.search_page import SearchPage


RGB = 'rgba(255, 255, 255, 1)'

class ChatTest(Test):
    def setUp(self):
        super().setUp()
        self.login()
        self.page = ChatPage(self.driver)
        self.other_profile = OtherProfilePage(self.driver)
        self.other_profile.open_other_profile(self.ID2)

'''
    def test_chat_non_read_messages(self):
        # Непрочитанные сообщения выделяются цветом.

        self.other_profile.click_write_message()
        self.page.write_message("str")
        self.page.click_send_button()
        # ATTENTION
        # Чат сделан на поллинге, то есть чисто технически проверить,
        # что ничего не отправилось, можно только таким способом (ничего лучше не придумалось :с)
        time.sleep(3)
        style1 = ''
        while style1 == '':
            style1 = self.page.get_left_card_color()

        self.logout()

        self.login2()
        self.other_profile.open_other_profile(self.ID)
        self.other_profile.click_write_message()
        time.sleep(3)
        style2 = self.page.get_left_card_color()
        print(style1, '/n', style2)
        self.assertNotEqual(style2, style1)

'''
    def test_chat_empty_message(self):
        # Невозможно отправить пустое сообщение.

        self.other_profile.click_write_message()
        self.page.click_send_button()
        # ATTENTION
        # Чат сделан на поллинге, то есть чисто технически проверить,
        # что ничего не отправилось, можно только таким способом (ничего лучше не придумалось :с)
        time.sleep(3)

        text = self.page.get_last_message_text()
        self.assertNotEqual("", text)













