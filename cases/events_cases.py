from cases.base_cases import Test
from pages.event_page import EventPage
from pages.events_page import EventsPage


GEO_ERROR = 'Ошибка при определении местоположения'


class EventsTest(Test):
    def setUp(self):
        super().setUp()
        self.page = EventsPage(self.driver)

    def test_events_card_redirect_click_picture(self):
        # Клик по любому месту на карточке события открывает страницу эвента.

        self.page.open()
        title_text = self.page.get_first_card_title()
        self.page.redirect_to_first_card_by_pic()

        event_page = EventPage(self.driver)
        page_title_text = event_page.get_title()

        self.assertEqual(title_text, page_title_text)

    def test_events_card_redirect_click_card(self):
        # Клик по любому месту на карточке события открывает страницу эвента.

        self.page.open()
        title_text = self.page.get_first_card_title()
        self.page.redirect_to_first_card_by_card()

        event_page = EventPage(self.driver)
        page_title_text = event_page.get_title()

        self.assertEqual(title_text, page_title_text)

    def test_events_correct_categories(self):
        # Вкладки с категориями открывают события выбранной категории.

        self.page.open()
        title = self.page.get_first_inactive_tab_title()
        self.page.redirect_to_first_inactive_category_tab()
        title_active = self.page.get_active_tab_name()

        self.assertEqual(title, title_active)

    ''' <BUG>
    def test_events_tab_save_refresh(self):
        # Выбранная категория сохраняется после обновления страницы.
    '''

    def test_events_no_geolocation(self):
        # Ошибка при отсутствии доступа к геолокации на вкладке “Рядом”.
        self.page.open()

        self.page.redirect_to_near_tab()
        text = self.page.get_notification_text()

        self.assertEqual(GEO_ERROR, text)

