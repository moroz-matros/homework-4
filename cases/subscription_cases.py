from cases.base_cases import Test
from pages.other_profile_page import OtherProfilePage
from pages.profile_page import ProfilePage
from pages.subscription_page import SubscriptionPage

SUBSCRIBERS = 'Подписчики'
SUBSCRIBED_TO = 'Подписки'
NO_ONE = 'Никого не найдено =('
NO_ONE_2 = 'Тут пока пусто =('


class SubscriptionTest(Test):
    def setUp(self):
        super().setUp()
        self.login()
        self.page = SubscriptionPage(self.driver)
        self.other_profile_page = OtherProfilePage(self.driver)
        self.profile_page = ProfilePage(self.driver)

    def test_subscriptions_no_subscribers(self):
        # При отсутствии подписчиков выдает соответствующее сообщение.

        self.profile_page.open()
        self.profile_page.redirect_to_subscribers()
        self.page.wait_for_page(self.page.CONTAINER)
        tab = self.page.get_active_tab_title()
        text = self.page.get_no_one_text()

        self.assertEqual(SUBSCRIBERS, tab, 'Редирект на неверную страницу, ожидалась страница' +
                         SUBSCRIBERS + ', вернулась страница ' + tab)
        self.assertEqual(NO_ONE, text)

    def test_subscriptions_add_remove_subscription(self):
        # Наличие карточки с пользователем после появления подписки. Ее отсутствие после отписки.

        self.other_profile_page.open_other_profile(self.ID2)
        self.other_profile_page.click_subscribe()
        self.logout()

        self.login2()
        self.profile_page.open()
        self.profile_page.redirect_to_subscribers()
        name = self.page.get_sub_name()
        self.logout()

        self.login()
        self.other_profile_page.open_other_profile(self.ID2)
        self.other_profile_page.click_subscribe()
        self.logout()

        self.login2()
        self.profile_page.open()
        self.profile_page.redirect_to_subscribers()
        text = self.page.get_no_one_text()

        flag = (text == NO_ONE) or (text == NO_ONE_2)

        self.assertEqual(self.NAME, name)
        self.assertTrue(flag)

    def test_subscriptions_add_remove_subscribed_to(self):
        # Наличие карточки с пользователем после появления подписки. Ее отсутствие после отписки.

        self.other_profile_page.open_other_profile(self.ID2)
        self.other_profile_page.click_subscribe()

        self.profile_page.open()
        self.profile_page.redirect_to_subscribed_to()
        name = self.page.get_sub_name()

        self.other_profile_page.open_other_profile(self.ID2)
        self.other_profile_page.click_subscribe()

        self.profile_page.open()
        self.profile_page.redirect_to_subscribed_to()
        text = self.page.get_no_one_text()

        self.assertEqual(self.NAME2, name)
        self.assertEqual(NO_ONE, text)

    def test_subscriptions_no_subscribed_to(self):
        # При отсутствии подписок выдает соответствующее сообщение.

        self.profile_page.open()
        self.profile_page.redirect_to_subscribed_to()
        self.page.wait_for_page(self.page.CONTAINER)
        tab = self.page.get_active_tab_title()
        text = self.page.get_no_one_text()

        self.assertEqual(SUBSCRIBED_TO, tab, 'Редирект на неверную страницу, ожидалась страница' +
                         SUBSCRIBED_TO + ', вернулась страница ' + tab)
        self.assertEqual(NO_ONE, text)

    def test_subscriptions_tabs_refresh(self):
        # Происходит переключение между вкладками.
        # При обновлении страницы выбранная вкладка сохраняется.

        self.profile_page.open()
        self.profile_page.redirect_to_subscribers()
        self.page.wait_for_page(self.page.CONTAINER)
        self.page.redirect_to_subscribed_to()
        tab_subscribed_to1 = self.page.get_active_tab_title()
        self.page.refresh()
        tab_subscribed_to2 = self.page.get_active_tab_title()
        self.page.redirect_to_subscribers()
        tab_subscribers1 = self.page.get_active_tab_title()
        self.page.refresh()
        tab_subscribers2 = self.page.get_active_tab_title()

        self.assertEqual(SUBSCRIBED_TO, tab_subscribed_to1, 'неправильный редирект по ссылке ' + SUBSCRIBED_TO)
        self.assertEqual(SUBSCRIBED_TO, tab_subscribed_to2, 'вкладка ' + SUBSCRIBED_TO + ' сбрасывается при обновлении страницы')
        self.assertEqual(SUBSCRIBERS, tab_subscribers1, 'неправильный редирект по ссылке ' + SUBSCRIBERS)
        self.assertEqual(SUBSCRIBERS, tab_subscribers2,
                         'вкладка ' + SUBSCRIBERS + ' сбрасывается при обновлении страницы')


