from cases.base_cases import Test
from pages.activity_page import ActivityPage
from pages.other_profile_page import OtherProfilePage


class ActivitySubscriptionTest(Test):
    def setUp(self):
        super().setUp()
        self.page = ActivityPage(self.driver)
        self.login()
        self.other_profile_page = OtherProfilePage(self.driver)
        self.other_profile_page.open_other_profile(self.ID2)
        self.other_profile_page.click_subscribe()
        self.logout()
        self.login2()
        self.other_profile_page.open_other_profile(self.ID)
        self.other_profile_page.click_subscribe()
        self.logout()

    def tearDown(self):
        self.login2()
        self.other_profile_page.open_other_profile(self.ID)
        self.other_profile_page.click_subscribe()
        self.logout()
        self.login()
        self.other_profile_page.open_other_profile(self.ID2)
        self.other_profile_page.click_subscribe()
        super().tearDown()

    def test_activity_has_sub(self):
        # Имеются сообщения о новых подписках у тех, на кого подписан пользователь.
        # Переход на страницу профиля друга при нажатии на его имя.

        self.login()
        self.page.open()
        self.page.refresh()
        self.page.refresh()
        block = self.page.get_activity_block()
        flag = block.is_displayed()
        self.page.click_friend()
        friend_name = self.other_profile_page.get_user_name()
        self.logout()

        self.assertEqual(True, flag)
        self.assertEqual(self.NAME2, friend_name)
