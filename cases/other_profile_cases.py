from cases.base_cases import Test
from pages.chat_page import ChatPage
from pages.other_profile_page import OtherProfilePage

SUBSCRIBE = 'Подписаться'
UNSUBSCRIBE = 'Отписаться'

class OtherProfileTest(Test):
    def setUp(self):
        super().setUp()
        self.page = OtherProfilePage(self.driver)
        self.page.open_other_profile(self.ID2)

    ''' <BUG>
    def test_planning_visited_buttons(self):
        # Вкладки не сбрасываются при обновлении страницы. 
    '''

    def test_chat_redirect_ok(self):
        # (доступно после авторизации) При клике происходит переход на страницу чата с этим пользователем
        button = self.page.get_write_message_button()

        self.assertFalse(button.is_displayed())

        self.login()
        self.page.open_other_profile(self.ID2)
        self.page.click_write_message()
        chat_page = ChatPage(self.driver)
        name = chat_page.get_current_chat_user_name()

        self.assertEqual(self.NAME2, name)

    def test_subscribe_button_changes(self):
        # (доступно после авторизации) При клике происходит подписка/отписка на/от пользователя и смена надписи на кнопке на противоположную

        button = self.page.get_subscribe_button()
        self.assertFalse(button.is_displayed())

        self.login()
        self.page.open_other_profile(self.ID2)
        self.page.refresh()
        subscribe_text = self.page.get_subscribe_button_text()
        self.page.click_subscribe()
        unsubscribe_text = self.page.get_subscribe_button_text()
        self.page.click_subscribe()

        self.assertEqual(SUBSCRIBE, subscribe_text)
        self.assertEqual(UNSUBSCRIBE, unsubscribe_text)














