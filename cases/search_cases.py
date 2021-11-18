import random
import string
from urllib.parse import unquote

from cases.base_cases import Test
from pages.event_page import EventPage
from pages.main.events_page import EventsPage
from pages.other_profile_page import OtherProfilePage
from pages.profile_page import ProfilePage
from pages.search_page import SearchPage

letters = string.ascii_lowercase

long_str = 'q' * 1024
special_str = '@' + ''.join(random.choice(letters) for i in range(10))
str = ''.join(random.choice(letters) for i in range(10))
comma_str = ',' + ''.join(random.choice(letters) for i in range(10))
empty_str = ''

NO_ONE = 'Никого не найдено =('


class SearchTest(Test):
    def setUp(self):
        super().setUp()
        self.page = SearchPage(self.driver)
        self.page.open()

    ''' <BUG>
    def test_search_error_long(self):
        # Ошибка при вводе длинной строки (>1000 символов).
    '''

    def test_search_special_symbol(self):
        # Осуществляет поиск при вводе: специальных символов
        # Если результатов не найдено, появляется соответствующая надпись.

        self.page.search(special_str)
        self.page.get_text_no_found()
        redirect_url = self.driver.current_url
        redirect_url = unquote(redirect_url)
        self.assertIn(special_str, redirect_url)

    def test_search_comma_symbol(self):
        # Осуществляет поиск при вводе: специальных символов

        self.page.search(comma_str)
        self.page.get_text_no_found()
        redirect_url = self.driver.current_url
        redirect_url = unquote(redirect_url)
        self.assertIn(comma_str, redirect_url)

    def test_search_refresh(self):
        # Введенные данные сохраняются при обновлении страницы.

        self.page.search(str)
        self.page.get_text_no_found()
        self.page.refresh()
        redirect_url = self.driver.current_url
        redirect_url = unquote(redirect_url)
        self.assertIn(str, redirect_url)

    def test_search_tabs_different(self):
        # При клике по категории обновляется список результатов поиска
        # Выбранная категория сохраняется при обновлении страницы.
        # Есть результаты при пустом поле ввода

        self.page.search(empty_str)
        self.page.wait_for_page(self.page.CONTAINER)
        self.page.redirect_to_tab(self.page.EXHIBITION_TAB)
        title1 = self.page.get_first_event_title()
        self.page.redirect_to_tab(self.page.CONCERT_TAB)
        title2 = self.page.get_first_event_title()
        tab = self.page.get_active_tab_title()
        self.page.refresh()
        tab2 = self.page.get_active_tab_title()

        self.assertNotEquals(title1, title2)
        self.assertEqual(tab, tab2)

    def test_search_pagination_refresh(self):
        # Номер текущей страницы сохраняется при обновлении страницы.

        self.page.search(empty_str)
        self.page.redirect_next_page()
        num1 = self.page.get_page_num()
        self.page.refresh()
        num2 = self.page.get_page_num()

        self.assertEqual(num1, num2)

    def test_search_people_redirect_refresh(self):
        # При клике на вкладку “Люди" поиск отображает результат поиска по людям.
        # Вкладка не сбрасывается при обновлении страницы.

        self.page.redirect_to_users()
        self.page.refresh()
        user = self.page.get_first_user()

        self.assertEqual(True, user.is_displayed())

    def test_search_people_nobody(self):
        # Если результатов не найдено, появляется соответствующая надпись.

        self.page.redirect_to_users()
        self.page.search(special_str)
        text = self.page.get_text_no_found()

        self.assertEqual(NO_ONE, text)

    def test_search_people_empty_str(self):
        # Есть результаты при пустом поле ввода

        self.page.redirect_to_users()
        self.page.search(empty_str)
        user = self.page.get_first_user()

        self.assertEqual(True, user.is_displayed())

    def test_search_redirect_to_user(self):
        # Переходит на страницу профиля пользователя при нажатии на имя на карточке.

        self.page.redirect_to_users()
        name = self.page.get_first_user_name()
        self.page.redirect_to_first_user()
        profile_page = OtherProfilePage(self.driver)
        profile_name = profile_page.get_user_name()

        self.assertEqual(name, profile_name)

    def test_search_back_button(self):
        # Переадресовывает на главную страницу.

        self.page.redirect_to_main()
        page = EventsPage(self.driver)
        page.wait_for_page(page.CONTAINER)

        self.assertEqual("https://qdaqda.ru/", self.driver.current_url)






